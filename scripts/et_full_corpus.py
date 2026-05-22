"""Run E(t) integration across every Dagstuhl piece with both audio and network.

Sprint-3 Phase E. Reads the WP1 per-singer parquets and the WP3 standard-
Granger GEXF for each take that has both, calls ``compute_entanglement`` and
``compute_entanglement_null`` (200 circular-shift permutations), tabulates
per-piece summary stats to ``data/processed/dagstuhl/_et_corpus.csv`` and
renders the cross-piece comparison scatter at
``data/figures/et_corpus_comparison.png``.

In our current corpus, V(t) is NaN throughout (Dagstuhl is audio-only); E(t)
is therefore the weight-reallocated mean of A and N. The visual signal is
re-introduced once Tier-3 multimodal recordings exist.

Usage:
    python -m scripts.et_full_corpus
"""

from __future__ import annotations

import time
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from choir_entanglement.entanglement import (
    compute_entanglement,
    compute_entanglement_null,
)

PROCESSED_ROOT = Path("data/processed/dagstuhl")
CORPUS_CSV = PROCESSED_ROOT / "_et_corpus.csv"
FIGURE_OUT = Path("data/figures/et_corpus_comparison.png")
WINDOW_SEC = 10.0
STEP_SEC = 0.5  # 2 Hz: enough resolution for cross-piece comparison; keeps null pass fast
N_NULL_SHUFFLES = 200
NETWORK_METHOD = "standard"  # use the parametric Granger GEXFs as N(t)


def discover_eligible_takes() -> list[str]:
    """Every take dir that has both at least 2 per-singer parquets and a standard GEXF."""
    takes: list[str] = []
    for take_dir in sorted(PROCESSED_ROOT.iterdir()):
        if not take_dir.is_dir():
            continue
        gexf = take_dir / f"influence_graph_{NETWORK_METHOD}.gexf"
        parquets = list(take_dir.glob("*.parquet"))
        if gexf.exists() and len(parquets) >= 2:
            takes.append(take_dir.name)
    return takes


def process_take(take_id: str) -> tuple[dict[str, object], pd.DataFrame, np.ndarray]:
    take_dir = PROCESSED_ROOT / take_id
    audio = {p.stem: p for p in sorted(take_dir.glob("*.parquet"))}
    gexf = take_dir / f"influence_graph_{NETWORK_METHOD}.gexf"

    timeline = compute_entanglement(
        audio_parquets=audio,
        network_gexf=gexf,
        video_parquet=None,
        window_sec=WINDOW_SEC,
        step_sec=STEP_SEC,
    )
    e_values = timeline["E"].dropna().to_numpy()
    a_values = timeline["A"].dropna().to_numpy()
    n_value = float(timeline["N"].iloc[0]) if timeline["N"].notna().any() else float("nan")

    null = compute_entanglement_null(
        audio_parquets=audio,
        network_gexf=gexf,
        video_parquet=None,
        window_sec=WINDOW_SEC,
        step_sec=STEP_SEC,
        n_shuffles=N_NULL_SHUFFLES,
        seed=42,
    )
    null_finite = null[np.isfinite(null)]
    observed_mean = float(e_values.mean()) if e_values.size else float("nan")
    p_null = float((null_finite >= observed_mean).mean()) if null_finite.size else float("nan")

    row = {
        "take_id": take_id,
        "n_singers": len(audio),
        "n_windows": len(timeline),
        "duration_sec": round(float(timeline["time_sec"].iloc[-1]) - float(timeline["time_sec"].iloc[0]) + STEP_SEC, 2),
        "A_mean": round(float(a_values.mean()) if a_values.size else float("nan"), 4),
        "A_std": round(float(a_values.std()) if a_values.size else float("nan"), 4),
        "N_density": round(n_value, 4),
        "E_mean": round(observed_mean, 4),
        "E_std": round(float(e_values.std()) if e_values.size else float("nan"), 4),
        "E_peak": round(float(e_values.max()) if e_values.size else float("nan"), 4),
        "null_mean": round(float(null_finite.mean()) if null_finite.size else float("nan"), 4),
        "null_std": round(float(null_finite.std()) if null_finite.size else float("nan"), 4),
        "p_null": round(p_null, 4),
        "n_null_shuffles": int(null_finite.size),
    }
    return row, timeline, null_finite


def render_figure(rows: list[dict[str, object]], nulls: dict[str, np.ndarray]) -> Path:
    FIGURE_OUT.parent.mkdir(parents=True, exist_ok=True)
    fig, ax = plt.subplots(figsize=(11, 6))

    df = pd.DataFrame(rows).sort_values("E_mean", ascending=False).reset_index(drop=True)
    xs = np.arange(len(df))

    for i, row in df.iterrows():
        null_arr = nulls[row["take_id"]]
        if null_arr.size:
            q025, q975 = np.quantile(null_arr, [0.025, 0.975])
            null_mean = float(null_arr.mean())
            ax.errorbar(
                i, null_mean, yerr=[[null_mean - q025], [q975 - null_mean]],
                fmt="o", color="#888888", markersize=5, capsize=6, alpha=0.7,
                label="null mean (95% interval)" if i == 0 else None,
            )
    ax.scatter(
        xs, df["E_mean"], color="#d62728", s=90, zorder=3,
        label="observed mean E(t)",
    )
    for i, row in df.iterrows():
        marker = "***" if row["p_null"] < 0.001 else ("*" if row["p_null"] < 0.05 else "ns")
        ax.text(i, float(row["E_mean"]) + 0.015, marker, ha="center", fontsize=10, color="#d62728")

    ax.set_xticks(xs)
    ax.set_xticklabels(df["take_id"], rotation=20, ha="right", fontsize=9)
    ax.set_ylabel("Mean E(t) (audio + network, V absent)")
    ax.set_title(
        "WP3+E(t) cross-piece comparison · Dagstuhl WP3 corpus (5 pieces) · "
        f"{WINDOW_SEC:.0f}s windows @ {1/STEP_SEC:.0f} Hz, {N_NULL_SHUFFLES}-shuffle null"
    )
    ax.set_ylim(0.4, 1.0)
    ax.legend(loc="lower left", fontsize=9)
    ax.grid(True, alpha=0.3, axis="y")

    fig.tight_layout()
    fig.savefig(FIGURE_OUT, dpi=150, bbox_inches="tight")
    plt.close(fig)
    return FIGURE_OUT


def run() -> None:
    takes = discover_eligible_takes()
    print(f"Found {len(takes)} eligible takes (audio + standard GEXF): {takes}")

    rows: list[dict[str, object]] = []
    nulls: dict[str, np.ndarray] = {}
    total_start = time.perf_counter()

    for take_id in takes:
        start = time.perf_counter()
        row, _, null_arr = process_take(take_id)
        rows.append(row)
        nulls[take_id] = null_arr
        print(
            f"  {take_id:24s} mean E={row['E_mean']} (null {row['null_mean']}±{row['null_std']}) "
            f"p_null={row['p_null']:.4f}  [{time.perf_counter() - start:.1f}s]"
        )

    df = pd.DataFrame(rows).sort_values("take_id").reset_index(drop=True)
    df.to_csv(CORPUS_CSV, index=False)
    print(f"\nWrote {CORPUS_CSV} ({len(df)} rows; {(time.perf_counter() - total_start)/60:.1f} min total)")

    figure_path = render_figure(rows, nulls)
    print(f"Wrote {figure_path}")


if __name__ == "__main__":
    run()
