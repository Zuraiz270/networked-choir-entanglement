"""Render the WP3 Hacker flagship influence graph as a publication SVG.

Reads a persisted influence-graph GEXF and draws a clean directed graph
(edge width ~ Granger F-stat, SATB voice colours, arrows = who-leads-whom).
Vector SVG output for the paper. Pulls forward the brief's Jul-7 deliverable.

Usage:
    python -m scripts.wp3_flagship_svg --piece LI_QuartetA_Take02 --method standard
"""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

PROCESSED = Path("data/processed/dagstuhl")
OUT_DIR = Path("data/figures")
VOICE_COLOR = {"S": "#d62728", "A": "#ff7f0e", "T": "#2ca02c", "B": "#1f77b4"}
VOICE_NAME = {"S": "Soprano", "A": "Alto", "T": "Tenor", "B": "Bass"}


def render(piece: str, method: str) -> Path:
    gexf = PROCESSED / piece / f"influence_graph_{method}.gexf"
    if not gexf.exists():
        raise FileNotFoundError(gexf)
    g = nx.read_gexf(gexf)
    pos = nx.circular_layout(g)
    fig, ax = plt.subplots(figsize=(7, 7))

    colors = [VOICE_COLOR.get(str(n)[0], "#888888") for n in g.nodes]
    nx.draw_networkx_nodes(g, pos, node_color=colors, node_size=2200, alpha=0.9, ax=ax)
    nx.draw_networkx_labels(
        g,
        pos,
        labels={n: str(n) for n in g.nodes},
        font_size=12,
        font_color="white",
        font_weight="bold",
        ax=ax,
    )
    if g.number_of_edges():
        edges = list(g.edges(data=True))
        w = np.array([d.get("weight", 1.0) for _, _, d in edges], dtype=float)
        widths = (0.6 + 3.4 * (w / w.max())).tolist() if w.max() > 0 else [1.0] * len(edges)
        nx.draw_networkx_edges(
            g,
            pos,
            edgelist=[(u, v) for u, v, _ in edges],
            width=widths,
            edge_color="#555555",
            alpha=0.7,
            arrows=True,
            arrowsize=20,
            connectionstyle="arc3,rad=0.12",
            node_size=2200,
            ax=ax,
        )

    present = sorted({str(n)[0] for n in g.nodes})
    handles = [
        plt.Line2D(
            [0],
            [0],
            marker="o",
            linestyle="",
            markersize=11,
            markerfacecolor=VOICE_COLOR[s],
            markeredgecolor="none",
            label=VOICE_NAME.get(s, s),
        )
        for s in present
        if s in VOICE_COLOR
    ]
    ax.legend(handles=handles, loc="upper right", frameon=False, fontsize=10)
    ax.set_title(
        f"Directed influence graph (who-leads-whom)\n"
        f"Dagstuhl {piece} · {method} Granger · "
        f"{g.number_of_edges()} significant edges (p_null < 0.05)",
        fontsize=12,
    )
    ax.axis("off")
    fig.tight_layout()

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out = OUT_DIR / f"wp3_flagship_{piece}_{method}.svg"
    fig.savefig(out, format="svg", bbox_inches="tight")
    fig.savefig(out.with_suffix(".png"), dpi=150, bbox_inches="tight")
    plt.close(fig)
    return out


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--piece", default="LI_QuartetA_Take02")
    p.add_argument("--method", default="standard", choices=["standard", "cop_gc"])
    args = p.parse_args()
    out = render(args.piece, args.method)
    print(f"Wrote {out} (+ .png)")


if __name__ == "__main__":
    main()
