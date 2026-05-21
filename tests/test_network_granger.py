"""Smoke tests for WP3 Granger + influence-graph."""

from __future__ import annotations

import numpy as np
import numpy.typing as npt
import pytest

from choir_entanglement.network.granger import (
    ordinal_pattern_indices,
    pairwise_granger,
)
from choir_entanglement.network.influence_graph import (
    build_influence_graph,
    graph_metrics,
)

FloatPair = tuple[npt.NDArray[np.float64], npt.NDArray[np.float64]]


@pytest.fixture
def coupled_pair() -> FloatPair:
    """Generate cause and effect=cause[t-1]+noise: cause should Granger-cause effect."""
    rng = np.random.default_rng(42)
    n = 500
    cause = rng.normal(0, 1, n).cumsum()
    effect = np.concatenate([[0.0], cause[:-1]]) + rng.normal(0, 0.3, n)
    return cause.astype(np.float64), effect.astype(np.float64)


@pytest.fixture
def independent_pair() -> FloatPair:
    rng = np.random.default_rng(7)
    return rng.normal(0, 1, 500).cumsum().astype(np.float64), rng.normal(0, 1, 500).cumsum().astype(np.float64)


@pytest.fixture
def nonlinear_coupled_pair() -> FloatPair:
    """Effect = (lagged cause)^3 + noise on a stationary AR(1) cause.

    The cube is strongly non-linear but monotonic, so the ordinal-pattern
    transform preserves the coupling. This is the regime where COP-GC has a
    clear theoretical advantage over parametric Granger.
    """
    rng = np.random.default_rng(11)
    n = 600
    cause = np.zeros(n, dtype=np.float64)
    eps = rng.normal(0, 1, n)
    for i in range(1, n):
        cause[i] = 0.6 * cause[i - 1] + eps[i]
    lagged = np.concatenate([[0.0], cause[:-1]])
    effect = lagged**3 + rng.normal(0, 0.5, n)
    return cause, effect.astype(np.float64)


def test_granger_detects_coupling(coupled_pair: FloatPair) -> None:
    cause, effect = coupled_pair
    result = pairwise_granger(cause, effect, "A", "B", maxlag=5, n_shuffles=50)
    assert result.p_value_null < 0.05, f"Should detect coupling, got p_null={result.p_value_null}"
    assert result.f_stat > 0


def test_granger_does_not_falsely_flag_independent(independent_pair: FloatPair) -> None:
    cause, effect = independent_pair
    result = pairwise_granger(cause, effect, "A", "B", maxlag=5, n_shuffles=50)
    assert result.p_value_null > 0.05, f"Should not flag independent, got p_null={result.p_value_null}"


def test_build_influence_graph_includes_significant_edges_only() -> None:
    results = [
        type("R", (), {"cause": "A", "effect": "B", "f_stat": 10.0, "p_value_null": 0.01, "lag": 1})(),
        type("R", (), {"cause": "B", "effect": "C", "f_stat": 5.0, "p_value_null": 0.40, "lag": 1})(),
        type("R", (), {"cause": "C", "effect": "A", "f_stat": 8.0, "p_value_null": 0.001, "lag": 2})(),
    ]
    graph = build_influence_graph(results, significance=0.05)
    assert graph.number_of_nodes() == 3
    assert graph.number_of_edges() == 2
    assert graph.has_edge("A", "B")
    assert graph.has_edge("C", "A")
    assert not graph.has_edge("B", "C")


def test_ordinal_pattern_indices_encodes_known_permutations() -> None:
    """Order-3 Lehmer codes: monotone-up = 0; monotone-down = 5; check length."""
    rising = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    patterns = ordinal_pattern_indices(rising, order=3)
    assert patterns.shape == (3,)
    assert (patterns == 0.0).all()

    falling = np.array([5.0, 4.0, 3.0])
    assert ordinal_pattern_indices(falling, order=3).tolist() == [5.0]


def test_cop_gc_detects_nonlinear_coupling(nonlinear_coupled_pair: FloatPair) -> None:
    cause, effect = nonlinear_coupled_pair
    result = pairwise_granger(
        cause, effect, "A", "B", maxlag=5, n_shuffles=50, method="cop_gc", ordinal_order=3
    )
    assert result.method == "cop_gc"
    assert result.p_value_null < 0.05, f"Should detect non-linear coupling, got p_null={result.p_value_null}"
    assert result.f_stat > 0


def test_cop_gc_does_not_falsely_flag_independent(independent_pair: FloatPair) -> None:
    cause, effect = independent_pair
    result = pairwise_granger(
        cause, effect, "A", "B", maxlag=5, n_shuffles=50, method="cop_gc", ordinal_order=3
    )
    assert result.method == "cop_gc"
    assert result.p_value_null > 0.05, f"COP-GC should not flag independent, got p_null={result.p_value_null}"


def test_graph_metrics_computes_density_and_centrality() -> None:
    results = [
        type("R", (), {"cause": "A", "effect": "B", "f_stat": 10.0, "p_value_null": 0.01, "lag": 1})(),
        type("R", (), {"cause": "A", "effect": "C", "f_stat": 9.0, "p_value_null": 0.02, "lag": 1})(),
        type("R", (), {"cause": "B", "effect": "C", "f_stat": 7.0, "p_value_null": 0.01, "lag": 1})(),
    ]
    graph = build_influence_graph(results, significance=0.05)
    m = graph_metrics(graph)
    assert m.n_nodes == 3
    assert m.n_edges == 3
    assert 0 < m.density <= 1
