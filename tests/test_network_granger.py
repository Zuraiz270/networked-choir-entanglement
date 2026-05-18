"""Smoke tests for WP3 Granger + influence-graph."""

from __future__ import annotations

import numpy as np
import numpy.typing as npt
import pytest

from choir_entanglement.network.granger import pairwise_granger
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
