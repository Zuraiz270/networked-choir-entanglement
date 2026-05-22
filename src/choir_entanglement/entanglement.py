"""E(t) composite entanglement timeline.

Combines per-piece audio coupling A(t), visual coupling V(t), and network
coherence N(t) on a common time grid and emits the composite

    E(t) = mean(available signals at t)

Per `PROJECT_GUIDE.md` §11.1 the published formula is the equal-weight
``E(t) = (A + V + N) / 3``; when any signal is missing (NaN) the available
ones are averaged so the composite is always defined. This NaN-aware
behaviour is required because in our corpus no single piece natively carries
all three signals (Dagstuhl = audio + network only; Tier-1 = video only),
so partial composites are the realistic case for Sprint 3.

Public API:
- ``compute_entanglement(audio_parquets, network_gexf, video_parquet=None,
  window_sec=10.0, step_sec=0.1)`` -> DataFrame[time_sec, A, V, N, E, n_available]
- ``compute_entanglement_null(audio_parquets, network_gexf, ..., n_shuffles=200,
  seed=0)`` -> 1-D array of mean E(t) values under circular-shift permutations
"""

from __future__ import annotations

from collections.abc import Mapping
from itertools import combinations
from pathlib import Path

import networkx as nx
import numpy as np
import numpy.typing as npt
import pandas as pd


FloatArray = npt.NDArray[np.float64]

DEFAULT_WINDOW_SEC = 10.0
DEFAULT_STEP_SEC = 0.1  # 10 Hz output grid
POSE_FEATURE_COLUMNS: tuple[str, ...] = ("shoulder_rise", "head_sway", "trunk_lean")


def compute_entanglement(
    audio_parquets: Mapping[str, Path] | None,
    network_gexf: Path | None,
    video_parquet: Path | None = None,
    window_sec: float = DEFAULT_WINDOW_SEC,
    step_sec: float = DEFAULT_STEP_SEC,
) -> pd.DataFrame:
    """Time-align A(t), V(t), N(t) on a step_sec grid and emit E(t).

    Each row of the returned DataFrame corresponds to a window centered at
    ``time_sec``. ``E`` is ``np.nanmean([A, V, N])`` (weight is reallocated
    across available signals). ``n_available`` records how many of the three
    sub-signals are non-NaN at that timestamp.
    """
    audio_frames = _load_audio_frames(audio_parquets)
    video_frame = _load_video_frame(video_parquet)
    network_density = _load_network_density(network_gexf)

    duration_sec = _common_duration(audio_frames, video_frame)
    if duration_sec <= window_sec:
        raise ValueError(
            f"piece duration {duration_sec:.1f}s shorter than window {window_sec}s"
        )

    grid = np.arange(window_sec / 2, duration_sec - window_sec / 2, step_sec)
    a_series = _audio_series(audio_frames, grid, window_sec)
    v_series = _video_series(video_frame, grid, window_sec)
    n_series = _network_series(network_density, grid)

    stacked = np.vstack([a_series, v_series, n_series])
    n_available = np.sum(~np.isnan(stacked), axis=0).astype(np.int64)
    with np.errstate(invalid="ignore"):
        e_series = np.where(n_available > 0, np.nanmean(stacked, axis=0), np.nan)

    return pd.DataFrame(
        {
            "time_sec": grid.astype(np.float64),
            "A": a_series,
            "V": v_series,
            "N": n_series,
            "E": e_series,
            "n_available": n_available,
        }
    )


def compute_entanglement_null(
    audio_parquets: Mapping[str, Path] | None,
    network_gexf: Path | None,
    video_parquet: Path | None = None,
    window_sec: float = DEFAULT_WINDOW_SEC,
    step_sec: float = DEFAULT_STEP_SEC,
    n_shuffles: int = 200,
    seed: int = 0,
) -> FloatArray:
    """Mean-E(t) distribution under circular-shift permutations of audio.

    For each of ``n_shuffles`` iterations we circular-shift every singer's
    RMS series by an independent random offset (preserving within-stream
    autocorrelation per Stevens 2013), recompute the full E(t) timeline, and
    record its mean. The returned array can be used as the empirical null for
    an observed mean-E(t) test (e.g. ``p_null = (null >= observed).mean()``).
    """
    if audio_parquets is None:
        raise ValueError("null model requires audio parquets to shuffle")

    audio_frames = _load_audio_frames(audio_parquets)
    video_frame = _load_video_frame(video_parquet)
    network_density = _load_network_density(network_gexf)
    duration_sec = _common_duration(audio_frames, video_frame)
    grid = np.arange(window_sec / 2, duration_sec - window_sec / 2, step_sec)
    rng = np.random.default_rng(seed)

    null_means = np.zeros(n_shuffles, dtype=np.float64)
    for i in range(n_shuffles):
        shuffled = {s: _circular_shift_frame(df, rng) for s, df in audio_frames.items()}
        a = _audio_series(shuffled, grid, window_sec)
        v = _video_series(video_frame, grid, window_sec)
        n = _network_series(network_density, grid)
        stacked = np.vstack([a, v, n])
        with np.errstate(invalid="ignore"):
            e = np.nanmean(stacked, axis=0)
        null_means[i] = float(np.nanmean(e)) if not np.all(np.isnan(e)) else np.nan
    return null_means


def _load_audio_frames(
    audio_parquets: Mapping[str, Path] | None,
) -> dict[str, pd.DataFrame]:
    if not audio_parquets:
        return {}
    return {name: pd.read_parquet(p) for name, p in audio_parquets.items()}


def _load_video_frame(video_parquet: Path | None) -> pd.DataFrame | None:
    if video_parquet is None:
        return None
    return pd.read_parquet(video_parquet)


def _load_network_density(network_gexf: Path | None) -> float:
    if network_gexf is None:
        return float("nan")
    graph = nx.read_gexf(network_gexf)
    if graph.number_of_nodes() < 2:
        return float("nan")
    return float(nx.density(graph))


def _common_duration(
    audio_frames: Mapping[str, pd.DataFrame], video_frame: pd.DataFrame | None
) -> float:
    durations: list[float] = []
    for df in audio_frames.values():
        durations.append(float(df["time_sec"].iloc[-1]))
    if video_frame is not None and len(video_frame) > 1:
        durations.append(float(video_frame["time_sec"].iloc[-1]))
    if not durations:
        raise ValueError("no audio or video data provided")
    return min(durations)


def _audio_series(
    audio_frames: Mapping[str, pd.DataFrame], grid: FloatArray, window_sec: float
) -> FloatArray:
    """Mean absolute pairwise Pearson correlation of RMS envelopes per window.

    For E(t)'s scalar A(t) we don't need the full lag-aware cross-correlation
    machinery in ``audio.coupling``; a windowed Pearson on the aligned RMS
    samples is the natural reduction and is two orders of magnitude faster.
    """
    if len(audio_frames) < 2:
        return np.full(len(grid), np.nan, dtype=np.float64)

    arrays = {name: df["rms"].to_numpy(dtype=np.float64) for name, df in audio_frames.items()}
    times = {name: df["time_sec"].to_numpy(dtype=np.float64) for name, df in audio_frames.items()}
    pairs = list(combinations(sorted(audio_frames), 2))

    out = np.full(len(grid), np.nan, dtype=np.float64)
    for i, t in enumerate(grid):
        t_lo, t_hi = t - window_sec / 2, t + window_sec / 2
        couplings: list[float] = []
        for a, b in pairs:
            slice_a = _slice_by_time(arrays[a], times[a], t_lo, t_hi)
            slice_b = _slice_by_time(arrays[b], times[b], t_lo, t_hi)
            n = min(slice_a.size, slice_b.size)
            if n < 10:
                continue
            r = _pearson_r(slice_a[:n], slice_b[:n])
            if r is not None:
                couplings.append(abs(r))
        if couplings:
            out[i] = float(np.mean(couplings))
    return out


def _pearson_r(a: FloatArray, b: FloatArray) -> float | None:
    mask = np.isfinite(a) & np.isfinite(b)
    if mask.sum() < 5:
        return None
    a_m, b_m = a[mask], b[mask]
    a_d = a_m - a_m.mean()
    b_d = b_m - b_m.mean()
    denom = float(np.sqrt((a_d * a_d).sum() * (b_d * b_d).sum()))
    if denom == 0.0:
        return None
    return float((a_d * b_d).sum() / denom)


def _video_series(
    video_frame: pd.DataFrame | None, grid: FloatArray, window_sec: float
) -> FloatArray:
    if video_frame is None or len(video_frame) == 0:
        return np.full(len(grid), np.nan, dtype=np.float64)
    times = video_frame["time_sec"].to_numpy(dtype=np.float64)
    feats = {
        col: video_frame[col].to_numpy(dtype=np.float64)
        for col in POSE_FEATURE_COLUMNS
        if col in video_frame.columns
    }
    if not feats:
        return np.full(len(grid), np.nan, dtype=np.float64)

    out = np.full(len(grid), np.nan, dtype=np.float64)
    for i, t in enumerate(grid):
        t_lo, t_hi = t - window_sec / 2, t + window_sec / 2
        in_window = (times >= t_lo) & (times <= t_hi)
        if not in_window.any():
            continue
        per_feature = []
        for arr in feats.values():
            window_arr = arr[in_window]
            window_arr = window_arr[np.isfinite(window_arr)]
            if window_arr.size < 2:
                continue
            std = float(np.std(window_arr))
            per_feature.append(std)
        if per_feature:
            out[i] = float(np.tanh(np.mean(per_feature)))
    return out


def _network_series(network_density: float, grid: FloatArray) -> FloatArray:
    return np.full(len(grid), network_density, dtype=np.float64)


def _slice_by_time(values: FloatArray, times: FloatArray, t_lo: float, t_hi: float) -> FloatArray:
    mask = (times >= t_lo) & (times <= t_hi)
    return values[mask]


def _circular_shift_frame(df: pd.DataFrame, rng: np.random.Generator) -> pd.DataFrame:
    rms = df["rms"].to_numpy(dtype=np.float64)
    n = rms.size
    if n < 4:
        return df
    shift = int(rng.integers(2, n - 2))
    shifted = pd.DataFrame(
        {"time_sec": df["time_sec"].to_numpy(), "rms": np.roll(rms, shift)}
    )
    return shifted
