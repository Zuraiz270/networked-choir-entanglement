"""Scale WP3 Granger + influence-graph across 5 Dagstuhl pieces (standard + COP-GC).

For each piece, loads all per-singer RMS parquets produced by WP1
(``data/processed/dagstuhl/{take_id}/{singer}.parquet``), runs pairwise
Granger causality with both ``method="standard"`` and ``method="cop_gc"``,
builds the directed influence graph at ``p_null < 0.05``, computes density,
modularity (python-louvain on the undirected projection) and eigenvector
centrality, writes per-piece GEXF for Gephi, and appends a flat per-piece
metrics row to ``data/processed/dagstuhl/_network_metrics.csv``.

Also emits a 2x3 grid figure (5 pieces + Sprint-2 demo for comparison) at
``data/figures/wp3_influence_graphs_5pieces.png``.

Usage:
    python -m scripts.wp3_dagstuhl_batch
"""

from __future__ import annotations

import time
from itertools import permutations
from pathlib import Path
from typing import Literal

import community.community_louvain as community_louvain
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import pandas as pd

from choir_entanglement.network.granger import (
    GrangerMethod,
    GrangerResult,
    pairwise_granger,
)
from choir_entanglement.network.influence_graph import build_influence_graph, graph_metrics

PROCESSED_ROOT = Path("data/processed/dagstuhl")
METRICS_CSV = PROCESSED_ROOT / "_network_metrics.csv"
FIGURE_OUT = Path("data/figures/wp3_influence_graphs_5pieces.png")

# 5 pieces spanning the corpus variation. SE has no "Take##" recordings (only
# tuning/cadence exercises), so the original plan's SE_QuartetA_Take01 is
# replaced with TP_FullChoir_Take01 — better stratification anyway.
PIECES: list[str] = [
    "LI_QuartetA_Take02",   # Sprint-2 reference (4 singers)
    "LI_QuartetB_Take01",   # second quartet (4 singers)
    "LI_FullChoir_Take01",  # full choir, same piece (8 singers)
    "TP_QuartetA_Take01",   # contrasting piece, quartet (4 singers)
    "TP_FullChoir_Take01",  # contrasting piece, full choir (8 singers)
]

VOICE_COLOR = {"S": "#d62728", "A": "#ff7f0e", "T": "#2ca02c", "B": "#1f77b4"}


def load_piece_rms(take_id: str) -> dict[str, np.ndarray]:
    """Load RMS series for every singer in a take. Truncate to common length."""
    take_dir = PROCESSED_ROOT / take_id
    if not take_dir.exists():
        raise FileNotFoundError(f"missing per-singer parquets for {take_id}")
    singers: dict[str, np.ndarray] = {}
    for parquet in sorted(take_dir.glob("*.parquet")):
        singer = parquet.stem
        singers[singer] = pd.read_parquet(parquet)["rms"].to_numpy(dtype=np.float64)
    n_min = min(len(s) for s in singers.values())
    return {k: v[:n_min] for k, v in singers.items()}


def run_pairwise(
    series: dict[str, np.ndarray],
    method: GrangerMethod,
    maxlag: int = 8,
    n_shuffles: int = 200,
) -> list[GrangerResult]:
    """Run pairwise Granger across all ordered singer pairs."""
    singers = sorted(series)
    results: list[GrangerResult] = []
    for cause, effect in permutations(singers, 2):
        results.append(
            pairwise_granger(
                series[cause], series[effect], cause, effect,
                maxlag=maxlag, n_shuffles=n_shuffles, seed=42, method=method,
            )
        )
    return results


def piece_metrics_row(
    take_id: str,
    method: GrangerMethod,
    results: list[GrangerResult],
    graph: nx.DiGraph,
) -> dict[str, object]:
    """Compute the flat metrics row for the corpus CSV."""
    base = graph_metrics(graph)
    undirected = graph.to_undirected()
    if undirected.number_of_edges() > 0:
        partition = community_louvain.best_partition(undirected, random_state=42)
        modularity = community_louvain.modularity(partition, undirected)
        n_communities = len(set(partition.values()))
    else:
        modularity = 0.0
        n_communities = base.n_nodes
    n_tested = len(results)
    n_significant = base.n_edges
    return {
        "take_id": take_id,
        "method": method,
        "n_singers": base.n_nodes,
        "n_tested_pairs": n_tested,
        "n_significant_edges": n_significant,
        "density": round(base.density, 4),
        "avg_in_degree": round(base.avg_in_degree, 4),
        "avg_out_degree": round(base.avg_out_degree, 4),
        "modularity": round(float(modularity), 4),
        "n_communities": int(n_communities),
        "most_central": base.most_central,
        "most_central_score": round(base.most_central_score, 4),
    }


def write_gexf(graph: nx.DiGraph, take_id: str, method: GrangerMethod) -> Path:
    """Write a Gephi-compatible GEXF of the influence graph."""
    out = PROCESSED_ROOT / take_id / f"influence_graph_{method}.gexf"
    out.parent.mkdir(parents=True, exist_ok=True)
    nx.write_gexf(graph, out)
    return out


def _voice_color(singer: str) -> str:
    return VOICE_COLOR.get(singer[0], "#888888")


def _draw_piece(ax: plt.Axes, graph: nx.DiGraph, title: str) -> None:
    if graph.number_of_nodes() == 0:
        ax.text(0.5, 0.5, "(no data)", ha="center", va="center")
        ax.set_axis_off()
        return
    pos = nx.circular_layout(graph)
    colors = [_voice_color(n) for n in graph.nodes]
    nx.draw_networkx_nodes(graph, pos, node_color=colors, node_size=600, alpha=0.85, ax=ax)
    nx.draw_networkx_labels(graph, pos, font_size=8, font_color="white", font_weight="bold", ax=ax)
    if graph.number_of_edges() > 0:
        edges = list(graph.edges(data=True))
        weights = np.array([d.get("weight", 1.0) for _, _, d in edges])
        widths = (0.5 + 2.0 * (weights / weights.max())).tolist() if weights.max() > 0 else [0.5] * len(edges)
        nx.draw_networkx_edges(
            graph, pos,
            edgelist=[(u, v) for u, v, _ in edges],
            width=widths, edge_color="#444444", alpha=0.6,
            arrows=True, arrowsize=10, connectionstyle="arc3,rad=0.1", ax=ax,
        )
    ax.set_title(title, fontsize=9)
    ax.set_axis_off()


def render_grid_figure(graphs: dict[str, nx.DiGraph], output: Path) -> None:
    """2x3 grid: 5 batch pieces (standard method) + Sprint-2 demo for comparison."""
    output.parent.mkdir(parents=True, exist_ok=True)
    fig, axes = plt.subplots(2, 3, figsize=(13, 8.5))
    flat = axes.ravel()
    for ax, (label, graph) in zip(flat, graphs.items(), strict=False):
        edges = graph.number_of_edges()
        nodes = graph.number_of_nodes()
        max_edges = nodes * (nodes - 1) if nodes > 1 else 1
        _draw_piece(ax, graph, f"{label}\n{edges}/{max_edges} significant edges")
    # Hide any unused panel
    for ax in flat[len(graphs):]:
        ax.set_axis_off()
    fig.suptitle(
        "WP3 directed influence graphs · Dagstuhl 5-piece batch (standard Granger, p_null<0.05) "
        "+ COP-GC method comparison",
        fontsize=11, y=0.99,
    )
    fig.tight_layout()
    fig.savefig(output, dpi=150, bbox_inches="tight")
    plt.close(fig)


def run(figure_only: bool = False) -> None:
    PROCESSED_ROOT.mkdir(parents=True, exist_ok=True)
    rows: list[dict[str, object]] = []
    standard_graphs: dict[str, nx.DiGraph] = {}
    cop_gc_graphs: dict[str, nx.DiGraph] = {}
    total_start = time.perf_counter()

    if figure_only:
        for take_id in PIECES:
            standard_graphs[take_id] = nx.read_gexf(
                PROCESSED_ROOT / take_id / "influence_graph_standard.gexf"
            )
            cop_gc_graphs[take_id] = nx.read_gexf(
                PROCESSED_ROOT / take_id / "influence_graph_cop_gc.gexf"
            )
    else:
        for take_id in PIECES:
            piece_start = time.perf_counter()
            print(f"\n=== {take_id} ===")
            series = load_piece_rms(take_id)
            print(f"  {len(series)} singers, series length {len(next(iter(series.values())))}")

            for method in ("standard", "cop_gc"):
                method_start = time.perf_counter()
                results = run_pairwise(series, method)
                graph = build_influence_graph(results, significance=0.05)
                write_gexf(graph, take_id, method)
                row = piece_metrics_row(take_id, method, results, graph)
                rows.append(row)
                elapsed = time.perf_counter() - method_start
                print(
                    f"  [{method:8s}] {row['n_significant_edges']:2d}/{row['n_tested_pairs']:2d} edges "
                    f"density={row['density']:.3f} modularity={row['modularity']:+.3f} "
                    f"central={row['most_central']} ({elapsed:.1f}s)"
                )
                (standard_graphs if method == "standard" else cop_gc_graphs)[take_id] = graph

            print(f"  piece total: {time.perf_counter() - piece_start:.1f}s")

        metrics_df = pd.DataFrame(rows).sort_values(["take_id", "method"]).reset_index(drop=True)
        metrics_df.to_csv(METRICS_CSV, index=False)
        print(f"\nWrote {METRICS_CSV} with {len(metrics_df)} rows.")

    # 2x3 grid: 5 pieces (standard) + TP_FullChoir_Take01 COP-GC as the 6th
    # panel, where the method difference is largest (42/56 standard vs 25/56
    # COP-GC), making the comparison visible at a glance.
    grid: dict[str, nx.DiGraph] = {p: standard_graphs[p] for p in PIECES}
    grid["TP_FullChoir_Take01 · COP-GC"] = cop_gc_graphs["TP_FullChoir_Take01"]
    render_grid_figure(grid, FIGURE_OUT)
    print(f"Wrote {FIGURE_OUT}")

    if not figure_only:
        total = time.perf_counter() - total_start
        print(f"\nTotal runtime: {total/60:.1f} min")


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--figure-only", action="store_true",
        help="Skip the (expensive) Granger pass; just re-render the figure from saved GEXFs.",
    )
    args = parser.parse_args()
    run(figure_only=args.figure_only)


if __name__ == "__main__":
    main()
