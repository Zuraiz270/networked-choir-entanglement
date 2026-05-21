"""Pairwise Granger-causality testing with circular-shift null model.

Per the project's H2 hypothesis, we use Granger causality on per-singer onset
time-series to construct a directed influence graph (who-leads-whom). The null
model is circular-shift (Stevens 2013) which preserves within-stream
autocorrelation, unlike i.i.d. shuffle.

Two methods:
- ``"standard"``: parametric VAR-based Granger (statsmodels). Linear couplings.
- ``"cop_gc"``: COP-GC (Zanin 2021, P-22). Each series is first mapped to its
  ordinal-pattern sequence (Lehmer code of each consecutive `order`-window),
  then the same parametric Granger machinery is applied. Captures non-linear
  couplings that the standard test misses.

Reference:
- Granger 1969 (foundational); statsmodels `grangercausalitytests`
- Zanin 2021 (P-22) "Augmenting Granger Causality through Ordinal Patterns"
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

import numpy as np
import numpy.typing as npt
from statsmodels.tsa.stattools import grangercausalitytests

FloatArray = npt.NDArray[np.float64]
GrangerMethod = Literal["standard", "cop_gc"]

_FACTORIALS = np.array([1, 1, 2, 6, 24, 120, 720], dtype=np.int64)


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
    method: GrangerMethod = "standard"


def pairwise_granger(
    cause_series: FloatArray,
    effect_series: FloatArray,
    cause_name: str,
    effect_name: str,
    maxlag: int = 10,
    n_shuffles: int = 200,
    seed: int = 0,
    method: GrangerMethod = "standard",
    ordinal_order: int = 3,
) -> GrangerResult:
    """Run Granger(cause -> effect) and a circular-shift null model.

    Returns the F-statistic, the parametric p-value, and the empirical p-value
    against `n_shuffles` circular-shift permutations of the cause series.

    ``method="cop_gc"`` first maps both series to ordinal-pattern integers of
    the given ``ordinal_order`` (default 3 → 6 patterns; Zanin 2021), then
    applies the same parametric Granger test on the transformed series.
    """
    if cause_series.shape != effect_series.shape:
        raise ValueError("cause and effect series must have equal length")

    cause_t, effect_t = _maybe_transform(cause_series, effect_series, method, ordinal_order)
    n = cause_t.size
    if n <= maxlag + 1:
        raise ValueError(f"need > {maxlag + 1} samples after transform, got {n}")

    f_stat, p_value, best_lag = _run_granger(cause_t, effect_t, maxlag)
    null_f_stats = _shuffle_null(cause_t, effect_t, maxlag, n_shuffles, seed)
    p_null = float((null_f_stats >= f_stat).mean())

    return GrangerResult(
        cause=cause_name,
        effect=effect_name,
        f_stat=f_stat,
        p_value=p_value,
        p_value_null=p_null,
        lag=best_lag,
        n_samples=n,
        method=method,
    )


def _maybe_transform(
    cause: FloatArray, effect: FloatArray, method: GrangerMethod, order: int
) -> tuple[FloatArray, FloatArray]:
    if method == "standard":
        return cause, effect
    if method == "cop_gc":
        return ordinal_pattern_indices(cause, order), ordinal_pattern_indices(effect, order)
    raise ValueError(f"unknown method: {method!r}")


def ordinal_pattern_indices(series: FloatArray, order: int = 3) -> FloatArray:
    """Map each consecutive length-``order`` window to its Lehmer-code permutation index.

    Returns a float array of length ``n - order + 1`` with values in
    ``[0, order! - 1]``. The mapping is deterministic: identical windows
    in different series get the same code, which is required for cross-series
    Granger comparisons.
    """
    if order < 2 or order >= _FACTORIALS.size:
        raise ValueError(f"order must be in [2, {_FACTORIALS.size - 1}], got {order}")
    n = series.size
    if n < order:
        raise ValueError(f"need >= {order} samples, got {n}")

    n_patterns = n - order + 1
    out = np.zeros(n_patterns, dtype=np.float64)
    for i in range(n_patterns):
        window = series[i : i + order]
        perm = np.argsort(window, kind="stable")
        code = 0
        remaining = perm.tolist()
        for j in range(order):
            v = remaining.pop(0)
            code += sum(1 for r in remaining if r < v) * int(_FACTORIALS[order - 1 - j])
        out[i] = float(code)
    return out


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
