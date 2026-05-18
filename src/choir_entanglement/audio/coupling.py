"""Pairwise audio coupling A(t) between two singer feature parquets.

Reads two parquets produced by pipeline.py, returns lag-aware cross-correlation
of their F0 traces. The peak lag tells us which singer leads which in time.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np
import numpy.typing as npt
import pandas as pd
import pyarrow.parquet as pq
from scipy.signal import correlate, correlation_lags

FloatArray = npt.NDArray[np.float64]


@dataclass(frozen=True)
class CouplingResult:
    """Output of compute_pairwise_coupling."""

    peak_correlation: float
    peak_lag_sec: float
    correlation_curve: FloatArray
    lags_sec: FloatArray
    overlap_sec: float


def _aligned_pair(
    df_a: pd.DataFrame, df_b: pd.DataFrame, column: str
) -> tuple[FloatArray, FloatArray, float]:
    """Trim both frames to common time window. Return raw arrays + overlap duration."""
    t_start = max(df_a["time_sec"].iloc[0], df_b["time_sec"].iloc[0])
    t_end = min(df_a["time_sec"].iloc[-1], df_b["time_sec"].iloc[-1])
    mask_a = (df_a["time_sec"] >= t_start) & (df_a["time_sec"] <= t_end)
    mask_b = (df_b["time_sec"] >= t_start) & (df_b["time_sec"] <= t_end)
    a = df_a.loc[mask_a, column].to_numpy(dtype="float64")
    b = df_b.loc[mask_b, column].to_numpy(dtype="float64")
    n = min(len(a), len(b))
    return a[:n], b[:n], float(t_end - t_start)


def _zero_mean_unit_var(x: FloatArray) -> FloatArray:
    """Center and scale x. NaN-aware: NaN replaced with 0 after centering (drops them from corr)."""
    finite = np.isfinite(x)
    if not finite.any():
        return np.zeros_like(x)
    mean = x[finite].mean()
    centered: FloatArray = np.where(finite, x - mean, 0.0)
    std = float(centered[finite].std())
    if std <= 0:
        return centered
    return (centered / std).astype(np.float64)


def compute_pairwise_coupling(
    df_a: pd.DataFrame,
    df_b: pd.DataFrame,
    max_lag_sec: float = 2.0,
    signal: str = "rms",
) -> CouplingResult:
    """Lag-aware cross-correlation of two singer feature streams.

    ``signal`` defaults to "rms" (envelope, always defined). Use "f0_hz" for
    pitch-based coupling — NaN frames are zeroed and excluded from the correlation.
    """
    a, b, overlap_sec = _aligned_pair(df_a, df_b, signal)
    if len(a) < 10:
        raise ValueError(f"Insufficient overlap: {len(a)} frames")

    a_z = _zero_mean_unit_var(a)
    b_z = _zero_mean_unit_var(b)
    corr = correlate(a_z, b_z, mode="full") / max(len(a_z), 1)

    frame_dt_sec = float(df_a["time_sec"].diff().median())
    lag_samples = correlation_lags(len(a_z), len(b_z), mode="full")
    lags_sec = lag_samples * frame_dt_sec

    window_mask = np.abs(lags_sec) <= max_lag_sec
    corr_windowed = corr[window_mask]
    lags_windowed = lags_sec[window_mask]
    peak_idx = int(np.argmax(np.abs(corr_windowed)))

    return CouplingResult(
        peak_correlation=float(corr_windowed[peak_idx]),
        peak_lag_sec=float(lags_windowed[peak_idx]),
        correlation_curve=corr_windowed,
        lags_sec=lags_windowed,
        overlap_sec=overlap_sec,
    )


def load_feature_parquet(path: Path) -> pd.DataFrame:
    """Load a per-singer feature parquet written by pipeline.py."""
    return pq.read_table(path).to_pandas()
