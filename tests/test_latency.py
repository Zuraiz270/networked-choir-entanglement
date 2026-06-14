"""Known-answer tests for Tier-3 latency injection."""

from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from choir_entanglement.audio.coupling import compute_pairwise_coupling
from choir_entanglement.latency import (
    FRAME_DT_SEC,
    LatencyConfig,
    inject_latency_frame,
    inject_latency_take,
    ms_to_frames,
)

FRAME_RATE_HZ = 1.0 / FRAME_DT_SEC  # ~43.07


def _frame(n: int = 400, seed: int = 0) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    t = np.arange(n) / FRAME_RATE_HZ
    return pd.DataFrame(
        {
            "time_sec": t,
            "f0_hz": 220.0 + rng.normal(0, 1, n),
            "voiced": np.ones(n, dtype=bool),
            "voiced_prob": np.full(n, 0.9),
            "rms": 0.5 + 0.2 * np.sin(2 * np.pi * 0.5 * t) + 0.02 * rng.normal(size=n),
            "onset": np.zeros(n, dtype=bool),
        }
    )


def test_ms_to_frames_known() -> None:
    assert ms_to_frames(0.0) == 0
    assert ms_to_frames(FRAME_DT_SEC * 1000) == 1          # exactly one frame
    assert ms_to_frames(FRAME_DT_SEC * 1000 * 2) == 2
    assert ms_to_frames(47.0) == round(0.047 / FRAME_DT_SEC)  # ~2 frames


def test_zero_delay_is_identity_and_input_untouched() -> None:
    df = _frame()
    original = df.copy(deep=True)
    out = inject_latency_frame(df, LatencyConfig(delay_ms=0.0))
    pd.testing.assert_frame_equal(out, original)
    pd.testing.assert_frame_equal(df, original)  # input not mutated


def test_delay_blanks_leading_frames_not_circular() -> None:
    df = _frame()
    k = ms_to_frames(100.0)
    out = inject_latency_frame(df, LatencyConfig(delay_ms=100.0))
    assert out["rms"].iloc[:k].isna().all()           # leading frames blanked
    assert not out["onset"].iloc[:k].any()
    # value at position k equals the ORIGINAL value at 0 (shifted, not wrapped)
    assert out["rms"].iloc[k] == pytest.approx(df["rms"].iloc[0])
    # last original value must NOT reappear at the front (no circular wrap)
    assert not np.isclose(out["rms"].iloc[0], df["rms"].iloc[-1])


def test_constant_delay_recovers_known_lag() -> None:
    base = _frame(seed=1)
    delayed = inject_latency_frame(base, LatencyConfig(delay_ms=100.0))
    # cross-correlate base (leader) vs delayed (follower) on rms
    res = compute_pairwise_coupling(base, delayed, max_lag_sec=0.5, signal="rms")
    expected_lag = ms_to_frames(100.0) * FRAME_DT_SEC
    # magnitude of the recovered lag equals the injected delay (sign is a
    # cross-correlation convention detail, not the quantity under test)
    assert abs(res.peak_lag_sec) == pytest.approx(expected_lag, abs=2 * FRAME_DT_SEC)


def test_reference_singer_unshifted() -> None:
    frames = {"S1": _frame(seed=1), "A1": _frame(seed=2)}
    out = inject_latency_take(frames, LatencyConfig(delay_ms=83.0), reference_singer="S1")
    pd.testing.assert_frame_equal(out["S1"], frames["S1"])      # reference untouched
    assert out["A1"]["rms"].iloc[: ms_to_frames(83.0)].isna().all()  # other delayed


def test_dropout_blanks_expected_fraction() -> None:
    df = _frame(n=2000)
    out = inject_latency_frame(df, LatencyConfig(delay_ms=0.0, dropout_rate=0.2, seed=7))
    blanked = out["rms"].isna().mean()
    assert 0.15 < blanked < 0.25  # ~20% within sampling tolerance
