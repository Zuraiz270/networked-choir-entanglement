"""Tests for the H3 visual-onset coupling core (scripts/h3_visual_onset.py)."""

from __future__ import annotations

import numpy as np
import pandas as pd
from scripts.h3_visual_onset import (
    circular_null_p,
    max_lag_correlation,
    visual_motion_signal,
)


def _smooth_noise(n: int, seed: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    return np.convolve(rng.standard_normal(n), np.ones(5) / 5, mode="same")


def test_max_lag_correlation_recovers_visual_lead() -> None:
    a = _smooth_noise(600, 0)
    v = np.roll(a, -5)  # visual shows at t what audio does at t+0.5s -> visual leads
    r, lag = max_lag_correlation(a, v, grid_hz=10.0, max_lag_s=2.0)
    assert r > 0.95
    assert abs(lag - 0.5) < 1e-9


def test_max_lag_correlation_handles_nans() -> None:
    a = _smooth_noise(600, 1)
    v = a.copy()
    v[100:150] = np.nan
    r, _ = max_lag_correlation(a, v, grid_hz=10.0, max_lag_s=2.0)
    assert r > 0.95


def test_circular_null_p_coupled_vs_independent() -> None:
    a = _smooth_noise(600, 2)
    coupled = a + 0.1 * _smooth_noise(600, 3)
    independent = _smooth_noise(600, 4)
    assert circular_null_p(a, coupled, grid_hz=10.0, n_shuffles=200, seed=0) < 0.05
    assert circular_null_p(a, independent, grid_hz=10.0, n_shuffles=200, seed=0) > 0.05


def test_visual_motion_signal_grid_and_motion() -> None:
    t = np.arange(0, 60, 0.12)
    pose = pd.DataFrame(
        {
            "time_sec": t,
            "singer_id": "P1",
            "head_sway": np.sin(t),
            "trunk_lean": np.cos(t),
            "shoulder_rise": np.zeros_like(t),
        }
    )
    times, motion = visual_motion_signal(pose, grid_hz=10.0)
    assert np.allclose(np.diff(times), 0.1)
    assert np.nanstd(motion) > 0
