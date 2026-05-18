"""Run WP3 Granger + influence graph on Dagstuhl SATB Quartet A Take 02.

Reads the per-singer RMS-envelope parquets produced by WP1, runs pairwise
Granger causality (cause -> effect) for all 12 directed SATB pairs, builds the
directed influence graph at p_null < 0.05, and saves Hacker's flagship figure
to data/figures/wp3_influence_graph.png.

Usage:
    python -m scripts.wp3_dagstuhl_demo
"""

from __future__ import annotations

from itertools import permutations
from pathlib import Path

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import pandas as pd

from choir_entanglement.network.granger import pairwise_granger
from choir_entanglement.network.influence_graph import build_influence_graph, graph_metrics

PARQUET_DIR = Path("data/processed/dagstuhl/LI_QuartetA_Take02")
FIGURE_OUT = Path("data/figures/wp3_influence_graph.png")
SINGERS = ["S2", "A1", "T1", "B1"]
VOICE_LABEL = {"S2": "Soprano", "A1": "Alto", "T1": "Tenor", "B1": "Bass"}
VOICE_COLOR = {"S2": "#d62728", "A1": "#ff7f0e", "T1": "#2ca02c", "B1": "#1f77b4"}


def load_rms_series(singer: str) -> np.ndarray:
    df = pd.read_parquet(PARQUET_DIR / f"{singer}.parquet")
    return df["rms"].to_numpy(dtype=np.float64)


def run() -> None:
    series = {s: load_rms_series(s) for s in SINGERS}
    n_min = min(len(s) for s in series.values())
    series = {s: arr[:n_min] for s, arr in series.items()}
    print(f"Loaded {len(SINGERS)} singer RMS series of length {n_min}")

    results = []
    print("\n--- Pairwise Granger (cause -> effect) ---")
    for cause, effect in permutations(SINGERS, 2):
        r = pairwise_granger(
            series[cause], series[effect], cause, effect, maxlag=8, n_shuffles=200, seed=42
        )
        results.append(r)
        verdict = "*" if r.p_value_null < 0.05 else " "
        print(
            f"  {VOICE_LABEL[cause]:8s} -> {VOICE_LABEL[effect]:8s}  "
            f"F={r.f_stat:6.2f}  p_null={r.p_value_null:.3f}  lag={r.lag}  {verdict}"
        )

    graph = build_influence_graph(results, significance=0.05)
    metrics = graph_metrics(graph)
    print(f"\n--- Graph metrics ---")
    print(f"  nodes={metrics.n_nodes}  edges={metrics.n_edges}  density={metrics.density:.3f}")
    print(f"  avg in-deg={metrics.avg_in_degree:.2f}  avg out-deg={metrics.avg_out_degree:.2f}")
    print(f"  most central: {VOICE_LABEL[metrics.most_central]} "
          f"(score {metrics.most_central_score:.3f})")

    _plot(graph, metrics, FIGURE_OUT)
    print(f"\n  Figure: {FIGURE_OUT}")


def _plot(graph: nx.DiGraph, metrics, out: Path) -> None:
    fig, ax = plt.subplots(figsize=(8, 7))
    pos = {
        "S2": (0, 1),
        "A1": (1, 0.5),
        "T1": (0, -1),
        "B1": (-1, 0.5),
    }
    node_colors = [VOICE_COLOR[n] for n in graph.nodes]
    nx.draw_networkx_nodes(graph, pos, node_color=node_colors, node_size=2500, alpha=0.85, ax=ax)
    nx.draw_networkx_labels(
        graph, pos,
        labels={n: VOICE_LABEL[n] for n in graph.nodes},
        font_size=11, font_color="white", font_weight="bold", ax=ax,
    )

    if graph.number_of_edges() > 0:
        edges = list(graph.edges(data=True))
        weights = np.array([d["weight"] for _, _, d in edges])
        widths = 1.0 + 4.0 * (weights / weights.max()) if weights.max() > 0 else [1.0] * len(edges)
        nx.draw_networkx_edges(
            graph, pos,
            edgelist=[(u, v) for u, v, _ in edges],
            width=widths.tolist() if hasattr(widths, "tolist") else widths,
            edge_color="#444444", alpha=0.7, arrows=True, arrowsize=22,
            connectionstyle="arc3,rad=0.12", ax=ax,
        )
        edge_labels = {(u, v): f"F={d['weight']:.1f}\nlag={d['lag']}" for u, v, d in edges}
        nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_size=8, ax=ax)

    ax.set_title(
        "WP3 directed influence graph (Hacker flagship, draft)\n"
        "Dagstuhl ChoirSet · Locus Iste Quartet A Take 02 · "
        f"Granger p_null < 0.05 ({metrics.n_edges}/{12} edges)\n"
        f"Most central voice: {VOICE_LABEL[metrics.most_central]} "
        f"(eigenvector centrality {metrics.most_central_score:.2f})"
    )
    ax.axis("off")
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)

    out.parent.mkdir(parents=True, exist_ok=True)
    fig.tight_layout()
    fig.savefig(out, dpi=150, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    run()
