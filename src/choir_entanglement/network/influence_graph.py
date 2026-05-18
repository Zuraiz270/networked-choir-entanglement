"""Build a directed influence graph from pairwise Granger results."""

from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass

import networkx as nx

from .granger import GrangerResult


@dataclass(frozen=True)
class GraphMetrics:
    n_nodes: int
    n_edges: int
    density: float
    avg_in_degree: float
    avg_out_degree: float
    most_central: str
    most_central_score: float


def build_influence_graph(
    results: Iterable[GrangerResult], significance: float = 0.05
) -> nx.DiGraph:
    """Make a directed graph where an edge A->B means A Granger-causes B at p_null < significance."""
    graph = nx.DiGraph()
    for r in results:
        graph.add_node(r.cause)
        graph.add_node(r.effect)
        if r.p_value_null < significance:
            graph.add_edge(
                r.cause,
                r.effect,
                weight=float(r.f_stat),
                p_null=float(r.p_value_null),
                lag=int(r.lag),
            )
    return graph


def graph_metrics(graph: nx.DiGraph) -> GraphMetrics:
    n = graph.number_of_nodes()
    e = graph.number_of_edges()
    density = nx.density(graph) if n > 1 else 0.0
    in_deg = dict(graph.in_degree())
    out_deg = dict(graph.out_degree())
    avg_in = sum(in_deg.values()) / n if n else 0.0
    avg_out = sum(out_deg.values()) / n if n else 0.0
    centrality = nx.eigenvector_centrality_numpy(graph) if e > 0 else {n: 0.0 for n in graph.nodes}
    if centrality:
        most_central = max(centrality, key=centrality.get)
        most_central_score = float(centrality[most_central])
    else:
        most_central = ""
        most_central_score = 0.0
    return GraphMetrics(
        n_nodes=n,
        n_edges=e,
        density=float(density),
        avg_in_degree=float(avg_in),
        avg_out_degree=float(avg_out),
        most_central=most_central,
        most_central_score=most_central_score,
    )
