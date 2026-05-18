"""Pairwise Granger-causality testing with circular-shift null model.

Per the project's H2 hypothesis, we use Granger causality on per-singer onset
time-series to construct a directed influence graph (who-leads-whom). The null
model is circular-shift (Stevens 2013) which preserves within-stream
autocorrelation, unlike i.i.d. shuffle.

Reference:
- Granger 1969 (foundational); statsmodels `grangercausalitytests`
- Zanin 2021 (P-22) for COP-GC variant; this module implements standard
  parametric Granger as the primary method.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import numpy.typing as npt
from statsmodels.tsa.stattools import grangercausalitytests

FloatArray = npt.NDArray[np.float64]


@dataclass(frozen=True)
class GrangerResult:
    """Single directed pairwise test outcome (cause -> effect)."""

    cause: str
    effect: str
    f_stat: float
    p_value: float
    p_value_null: float  # empirical p vs circular-shift null
    lag: int
    n_samples: int


def pairwise_granger(
    cause_series: FloatArray,
    effect_series: FloatArray,
    cause_name: str,
    effect_name: str,
    maxlag: int = 10,
    n_shuffles: int = 200,
    seed: int = 0,
) -> GrangerResult:
    """Run Granger(cause -> effect) and a circular-shift null model.

    Returns the F-statistic, the parametric p-value, and the empirical p-value
    against `n_shuffles` circular-shift permutations of the cause series.
    """
    if cause_series.shape != effect_series.shape:
        raise ValueError("cause and effect series must have equal length")
    n = cause_series.size
    if n <= maxlag + 1:
        raise ValueError(f"need > {maxlag + 1} samples, got {n}")

    f_stat, p_value, best_lag = _run_granger(cause_series, effect_series, maxlag)
    null_f_stats = _shuffle_null(cause_series, effect_series, maxlag, n_shuffles, seed)
    p_null = float((null_f_stats >= f_stat).mean())

    return GrangerResult(
        cause=cause_name,
        effect=effect_name,
        f_stat=f_stat,
        p_value=p_value,
        p_value_null=p_null,
        lag=best_lag,
        n_samples=n,
    )


def _run_granger(cause: FloatArray, effect: FloatArray, maxlag: int) -> tuple[float, float, int]:
    """Return (F-stat at best lag, p-value, best lag) for cause -> effect."""
    data = np.column_stack([effect, cause])
    results = grangercausalitytests(data, maxlag=maxlag, verbose=False)
    best_lag = 1
    best_f = -np.inf
    best_p = 1.0
    for lag, (stats, _) in results.items():
        f, p, _, _ = stats["ssr_ftest"]
        if f > best_f:
            best_f = f
            best_p = p
            best_lag = lag
    return float(best_f), float(best_p), int(best_lag)


def _shuffle_null(
    cause: FloatArray, effect: FloatArray, maxlag: int, n_shuffles: int, seed: int
) -> FloatArray:
    rng = np.random.default_rng(seed)
    n = cause.size
    f_stats = np.zeros(n_shuffles, dtype=np.float64)
    min_shift = maxlag + 1
    for i in range(n_shuffles):
        shift = int(rng.integers(min_shift, n - min_shift))
        shuffled = np.roll(cause, shift)
        f_stats[i], _, _ = _run_granger(shuffled, effect, maxlag)
    return f_stats
