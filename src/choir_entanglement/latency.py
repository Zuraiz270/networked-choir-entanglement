"""Tier-3 network-latency injection on per-singer feature frames.

Tests H1 (does E(t) drop as network latency rises?) and H2 (does the
influence-graph topology shift toward leader-dominated?) by taking clean
multitrack audio (every singer on a separate mic, ~zero network latency) and
simulating an NMP regime: each non-reference singer's stream is *causally*
delayed relative to a reference, then A(t)/N(t)/E(t) are recomputed.

Design choices (see plan `ok-plan-for-the-virtual-pnueli.md`):
- Operates on the extracted feature parquets, not raw wav: re-running pyin per
  latency cell would dominate the compute, and a frame-level shift is exact
  for the RMS/onset series A(t) and Granger read. Quantization is +-half a
  frame (~11.6 ms), finer than the measured regime SDs (+-46-57 ms), so it
  does not blur regime discrimination.
- The shift is CAUSAL (leading frames blanked to NaN/False), NOT circular.
  This is deliberately different from the circular-shift NULL model, which
  must stay orthogonal: inject latency first (build the H1 stimulus), then run
  the standard observed-vs-circular-shift-null comparison on the delayed data.

Latency grid is evidence-anchored (see wiki/06_failure_modes/latency_thresholds.md):
measured Jamulus LAN 47+-46 ms / WAN 83+-57 ms (P-11); EPT ~25 ms (Chafe);
Zoom 150 ms labelled illustrative. H1 is regime discrimination, not a cliff.
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass

import numpy as np
import numpy.typing as npt
import pandas as pd

from .audio.pipeline import HOP_LENGTH_SAMPLES, SAMPLE_RATE_HZ

FloatArray = npt.NDArray[np.float64]

# Single source of truth for the feature-frame period (s). 512/22050 = 0.02322 s.
FRAME_DT_SEC = HOP_LENGTH_SAMPLES / SAMPLE_RATE_HZ

# Evidence-anchored regime grid (one-way delay in ms).
LATENCY_LEVELS_MS: dict[str, float] = {
    "clean": 0.0,        # studio baseline (~0 network latency)
    "ept": 25.0,         # Ensemble Performance Threshold (Chafe, measured)
    "jamulus_lan": 47.0,  # measured, P-11 (47 +- 46 ms)
    "jamulus_wan": 83.0,  # measured, P-11 (83 +- 57 ms)
    "zoom": 150.0,       # Zoom-class, qualitative consensus (illustrative)
}

# Columns that carry a value per frame and must be shifted with the stream.
_VALUE_COLUMNS = ("f0_hz", "voiced_prob", "rms")
_BOOL_COLUMNS = ("voiced", "onset")


@dataclass(frozen=True)
class LatencyConfig:
    """One latency regime. MVP uses constant delay (jitter/dropout = 0)."""

    delay_ms: float
    jitter_sd_ms: float = 0.0   # stretch: per-frame Gaussian jitter
    dropout_rate: float = 0.0   # stretch: fraction of frames blanked to NaN
    seed: int = 0


def ms_to_frames(delay_ms: float, frame_dt_sec: float = FRAME_DT_SEC) -> int:
    """Convert a one-way delay in ms to an integer feature-frame shift (round-to-nearest)."""
    return int(round((delay_ms / 1000.0) / frame_dt_sec))


def inject_latency_frame(
    df: pd.DataFrame,
    config: LatencyConfig,
    rng: np.random.Generator | None = None,
) -> pd.DataFrame:
    """Causally delay one singer's feature frame. Returns a new frame; input untouched.

    Constant-delay MVP: every value column is shifted forward by
    ``ms_to_frames(delay_ms)``; the first k frames become NaN (values) / False
    (bools). ``time_sec`` is preserved (the grid is unchanged; the content is
    what arrives late). Jitter/dropout are applied only if configured.
    """
    out = df.copy(deep=True)
    k = ms_to_frames(config.delay_ms)
    n = len(out)
    if k <= 0 and config.jitter_sd_ms == 0.0 and config.dropout_rate == 0.0:
        return out
    k = min(k, n)

    for col in _VALUE_COLUMNS:
        if col in out.columns:
            shifted = np.full(n, np.nan, dtype="float64")
            if k < n:
                shifted[k:] = out[col].to_numpy(dtype="float64")[: n - k]
            out[col] = shifted
    for col in _BOOL_COLUMNS:
        if col in out.columns:
            shifted_b = np.zeros(n, dtype=bool)
            if k < n:
                shifted_b[k:] = out[col].to_numpy(dtype=bool)[: n - k]
            out[col] = shifted_b

    if config.jitter_sd_ms > 0.0 or config.dropout_rate > 0.0:
        out = _apply_jitter_dropout(out, config, rng or np.random.default_rng(config.seed))
    return out


def _apply_jitter_dropout(
    df: pd.DataFrame, config: LatencyConfig, rng: np.random.Generator
) -> pd.DataFrame:
    """Stretch goal: add per-frame Gaussian jitter (extra blanking) + Bernoulli dropout."""
    n = len(df)
    if config.dropout_rate > 0.0:
        drop = rng.random(n) < config.dropout_rate
        for col in _VALUE_COLUMNS:
            if col in df.columns:
                df.loc[drop, col] = np.nan
        for col in _BOOL_COLUMNS:
            if col in df.columns:
                df.loc[drop, col] = False
    # jitter_sd is recorded for provenance; per-frame variable shift is a future
    # refinement. The dropout already injects the "instability penalty" signal.
    return df


def inject_latency_take(
    frames: Mapping[str, pd.DataFrame],
    config: LatencyConfig,
    reference_singer: str | None = None,
) -> dict[str, pd.DataFrame]:
    """Apply relative latency across a take: reference singer unshifted, others delayed.

    Only relative offsets matter for pairwise A(t) and Granger, so we hold one
    singer fixed (the perceptual anchor) and delay the rest. Returns a new dict;
    inputs are not mutated.
    """
    singers = sorted(frames)
    if not singers:
        return {}
    ref = reference_singer if reference_singer is not None else singers[0]
    rng = np.random.default_rng(config.seed)
    out: dict[str, pd.DataFrame] = {}
    for singer in singers:
        if singer == ref:
            out[singer] = frames[singer].copy(deep=True)
        else:
            out[singer] = inject_latency_frame(frames[singer], config, rng)
    return out
