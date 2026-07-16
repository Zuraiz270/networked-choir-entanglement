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

# Evidence-anchored constant-delay grid (one-way delay in ms). Retained for the
# "journey" comparison: constant delay is a KNOWN-confounded manipulation on
# pre-coordinated studio audio (lag-tolerant coupling absorbs a constant shift).
LATENCY_LEVELS_MS: dict[str, float] = {
    "clean": 0.0,
    "ept": 25.0,
    "jamulus_lan": 47.0,
    "jamulus_wan": 83.0,
    "zoom": 150.0,
}

# Columns that carry a value per frame and must be shifted with the stream.
_VALUE_COLUMNS = ("f0_hz", "voiced_prob", "rms")
_BOOL_COLUMNS = ("voiced", "onset")


@dataclass(frozen=True)
class LatencyConfig:
    """One latency regime: mean delay + per-frame jitter SD + dropout fraction."""

    delay_ms: float
    jitter_sd_ms: float = 0.0  # per-frame Gaussian jitter (the real H1 driver)
    dropout_rate: float = 0.0  # fraction of frames blanked to NaN (packet loss)
    seed: int = 0


# Evidence-anchored JITTER regime grid (the scientifically valid H1 manipulation:
# variable jitter scrambles relative timing and CANNOT be absorbed by lag-tolerant
# coupling, unlike a constant delay). Jitter SD is taken directly from the measured
# inter-chorister timing SD in P-11 (47 +- 46 ms LAN, 83 +- 57 ms WAN) - i.e. the
# "+- SD" IS the network jitter. Dropout rates are illustrative (increasing).
# See wiki/06_failure_modes/latency_thresholds.md.
LATENCY_REGIMES: dict[str, LatencyConfig] = {
    "clean": LatencyConfig(delay_ms=0.0, jitter_sd_ms=0.0, dropout_rate=0.00),
    "ept": LatencyConfig(delay_ms=25.0, jitter_sd_ms=10.0, dropout_rate=0.00),
    "jamulus_lan": LatencyConfig(delay_ms=47.0, jitter_sd_ms=46.0, dropout_rate=0.01),  # measured
    "jamulus_wan": LatencyConfig(delay_ms=83.0, jitter_sd_ms=57.0, dropout_rate=0.03),  # measured
    "zoom": LatencyConfig(delay_ms=150.0, jitter_sd_ms=80.0, dropout_rate=0.08),  # illustrative
}


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
    n = len(out)
    rng = rng or np.random.default_rng(config.seed)

    base_k = ms_to_frames(config.delay_ms)
    if base_k <= 0 and config.jitter_sd_ms == 0.0 and config.dropout_rate == 0.0:
        return out

    # Per-frame source offset: constant base delay + Gaussian jitter. Output
    # frame i takes content from source frame (i - k_i); k_i varies frame to
    # frame, which scrambles relative timing (the part lag-tolerant coupling
    # CANNOT undo). k_i < 0 is clamped to 0 (cannot receive future content).
    jitter_frames = (config.jitter_sd_ms / 1000.0) / FRAME_DT_SEC
    if jitter_frames > 0.0:
        k = base_k + np.round(rng.normal(0.0, jitter_frames, size=n)).astype(int)
    else:
        k = np.full(n, base_k, dtype=int)
    k = np.clip(k, 0, n)
    src = np.arange(n) - k
    valid = src >= 0

    for col in _VALUE_COLUMNS:
        if col in out.columns:
            vals = out[col].to_numpy(dtype="float64")
            gathered = np.full(n, np.nan, dtype="float64")
            gathered[valid] = vals[src[valid]]
            out[col] = gathered
    for col in _BOOL_COLUMNS:
        if col in out.columns:
            vals_b = out[col].to_numpy(dtype=bool)
            gathered_b = np.zeros(n, dtype=bool)
            gathered_b[valid] = vals_b[src[valid]]
            out[col] = gathered_b

    if config.dropout_rate > 0.0:
        drop = rng.random(n) < config.dropout_rate
        for col in _VALUE_COLUMNS:
            if col in out.columns:
                out.loc[drop, col] = np.nan
        for col in _BOOL_COLUMNS:
            if col in out.columns:
                out.loc[drop, col] = False
    return out


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
