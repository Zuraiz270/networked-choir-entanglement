"""Clean deck figure: onset synchrony vs latency, mean +- SD per dataset.

The raw tier3 grid figure plots all 28 pieces (unreadable legend). This makes
the publication/deck version: one line per dataset (mean across pieces) with a
shaded +-1 SD band, plus the envelope-E(t) panel for the dissociation.

Usage:
    python -m scripts.tier3_corpus_figure
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

GRID_CSV = Path("data/processed/tier3/_latency_grid.csv")
OUT = Path("data/figures/tier3_corpus_summary.png")
ORDER = ["clean", "ept", "jamulus_lan", "jamulus_wan", "zoom"]
XLABEL = {"clean": 0, "ept": 10, "jamulus_lan": 46, "jamulus_wan": 57, "zoom": 80}
COLOR = {"dagstuhl": "#1f77b4", "esmuc": "#2ca02c", "choralsynth": "#d62728"}
LABEL = {"dagstuhl": "Dagstuhl (real, n=5)", "esmuc": "ESMUC (real, n=3)",
         "choralsynth": "ChoralSynth (synthetic, n=20)"}


def _series(df: pd.DataFrame, ds: str, col: str) -> tuple[list[float], list[float], list[float]]:
    d = df[df.dataset == ds]
    xs, means, sds = [], [], []
    for lv in ORDER:
        vals = d[d.level == lv][col].dropna()
        if len(vals):
            xs.append(XLABEL[lv])
            means.append(float(vals.mean()))
            sds.append(float(vals.std()))
    return xs, means, sds


def run() -> None:
    df = pd.read_csv(GRID_CSV)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.2))
    for ds in ["dagstuhl", "esmuc", "choralsynth"]:
        if not (df.dataset == ds).any():
            continue
        for ax, col in ((ax1, "onset_sync"), (ax2, "E_mean")):
            xs, m, sd = _series(df, ds, col)
            m_a, sd_a = np.array(m), np.array(sd)
            ax.plot(xs, m_a, marker="o", color=COLOR[ds], linewidth=2,
                    label=LABEL[ds] if ax is ax1 else None)
            ax.fill_between(xs, m_a - sd_a, m_a + sd_a, color=COLOR[ds], alpha=0.15)
    ax1.set_title("Attack-timing onset synchrony (latency-sensitive)", fontsize=12)
    ax1.set_ylabel("Zero-lag onset synchrony")
    ax2.set_title("Envelope E(t) (latency-robust)", fontsize=12)
    ax2.set_ylabel("Mean E(t)")
    for ax in (ax1, ax2):
        ax.set_xlabel("Injected jitter SD (ms)")
        ax.grid(True, alpha=0.3)
    ax1.legend(fontsize=9, loc="upper right")
    fig.suptitle(
        "Tier-3 latency injection: attack timing degrades, loudness coupling does not\n"
        "28 pieces across 3 datasets (2 real + 1 synthetic), mean +- 1 SD",
        fontsize=12,
    )
    fig.tight_layout()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    run()
