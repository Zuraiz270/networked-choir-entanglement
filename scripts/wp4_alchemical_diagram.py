"""Draft Prof. Gloor's flagship figure: the alchemical-stage Honest Signals pipeline.

Shows how raw choir video transforms through the four alchemical stages into
quantified entanglement. Mirrors Gloor's *Cybernetic Alchemy* framework
(Ch. 14, *Data as Prima Materia*).
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

FIGURE_OUT = Path("data/figures/wp4_alchemical_stages.png")

STAGES = [
    {
        "name": "Nigredo",
        "color": "#1a1a1a",
        "text_color": "white",
        "subtitle": "Prima Materia",
        "bullets": [
            "Raw choir mp4 from YouTube",
            "Dagstuhl multitrack wav files",
            "No structure, no meaning",
            "Just bytes on disk",
        ],
    },
    {
        "name": "Albedo",
        "color": "#e8e8e8",
        "text_color": "#1a1a1a",
        "subtitle": "Purification",
        "bullets": [
            "Per-singer F0 + onset parquets",
            "MediaPipe pose + face parquets",
            "Schema validated, NaN-safe",
            "Reproducible, hashable",
        ],
    },
    {
        "name": "Citrinitas",
        "color": "#f4c430",
        "text_color": "#1a1a1a",
        "subtitle": "Illumination",
        "bullets": [
            "Pairwise A(t) audio coupling",
            "Pairwise V(t) visual coupling",
            "Granger N(t) influence edges",
            "Patterns emerge across singers",
        ],
    },
    {
        "name": "Rubedo",
        "color": "#c62828",
        "text_color": "white",
        "subtitle": "Magnum Opus",
        "bullets": [
            "E(t) = (A + V + N) / 3",
            "Directed influence graph",
            "Regime contrast (Zoom vs SoundJack)",
            "Honest Signals quantified",
        ],
    },
]


def run() -> None:
    fig, ax = plt.subplots(figsize=(13, 6))
    n = len(STAGES)
    box_w = 2.8
    box_h = 3.4
    gap = 0.5
    total_w = n * box_w + (n - 1) * gap
    x0 = -total_w / 2

    for i, stage in enumerate(STAGES):
        x = x0 + i * (box_w + gap)
        rect = mpatches.FancyBboxPatch(
            (x, -box_h / 2), box_w, box_h,
            boxstyle="round,pad=0.05,rounding_size=0.15",
            facecolor=stage["color"], edgecolor="#333333", linewidth=1.5,
        )
        ax.add_patch(rect)
        ax.text(
            x + box_w / 2, box_h / 2 - 0.35,
            stage["name"],
            ha="center", va="top",
            fontsize=18, fontweight="bold",
            color=stage["text_color"],
        )
        ax.text(
            x + box_w / 2, box_h / 2 - 0.85,
            stage["subtitle"],
            ha="center", va="top",
            fontsize=10, style="italic",
            color=stage["text_color"],
        )
        for j, bullet in enumerate(stage["bullets"]):
            ax.text(
                x + 0.15, 0.45 - j * 0.45,
                f"• {bullet}",
                ha="left", va="top",
                fontsize=9,
                color=stage["text_color"],
            )

        if i < n - 1:
            arrow_x = x + box_w + 0.05
            ax.annotate(
                "",
                xy=(arrow_x + gap - 0.1, 0),
                xytext=(arrow_x, 0),
                arrowprops=dict(arrowstyle="->", color="#555555", lw=2.5),
            )

    ax.set_xlim(x0 - 0.5, -x0 + 0.5)
    ax.set_ylim(-box_h / 2 - 1.5, box_h / 2 + 0.8)
    ax.axis("off")
    ax.set_title(
        "WP4 alchemical-stage Honest Signals pipeline (Gloor flagship, draft)\n"
        "Cybernetic Alchemy applied to networked choir performance",
        fontsize=13, pad=15,
    )
    ax.text(
        0, -box_h / 2 - 0.9,
        "Raw audio + video → reproducible features → cross-singer patterns → quantified group flow",
        ha="center", va="top", fontsize=10, style="italic", color="#444444",
    )
    ax.text(
        0, -box_h / 2 - 1.3,
        "Source: Gloor, *Cybernetic Alchemy* (Ch. 14, Data as Prima Materia). Pipeline implementation: this project, Sprint 2.",
        ha="center", va="top", fontsize=8, color="#666666",
    )

    FIGURE_OUT.parent.mkdir(parents=True, exist_ok=True)
    fig.tight_layout()
    fig.savefig(FIGURE_OUT, dpi=150, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"Figure: {FIGURE_OUT}")


if __name__ == "__main__":
    run()
