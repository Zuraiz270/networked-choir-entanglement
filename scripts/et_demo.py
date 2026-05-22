"""Compute the E(t) timeline on LI_QuartetA_Take02 and render the demo figure.

Dagstuhl is audio-only (no video), so V(t) is NaN throughout and the
composite is the weight-reallocated E(t) = mean(A, N). This is the honest
single-piece end-to-end demo for Phase D; the full-corpus run lives in
Phase E.

Usage:
    python -m scripts.et_demo
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from choir_entanglement.entanglement import (
    compute_entanglement,
    compute_entanglement_null,
)

TAKE_ID = "LI_QuartetA_Take02"
AUDIO_DIR = Path("data/processed/dagstuhl") / TAKE_ID
NETWORK_GEXF = AUDIO_DIR / "influence_graph_standard.gexf"
FIGURE_OUT = Path("data/figures/et_timeline_LI_QA_Take02.png")
WINDOW_SEC = 10.0
STEP_SEC = 0.1
N_NULL_SHUFFLES = 200


def run() -> None:
    audio_parquets = {p.stem: p for p in sorted(AUDIO_DIR.glob("*.parquet"))}
    if not audio_parquets:
        raise FileNotFoundError(f"no audio parquets under {AUDIO_DIR}")
    print(f"Loaded {len(audio_parquets)} singer parquets: {sorted(audio_parquets)}")

    timeline = compute_entanglement(
        audio_parquets=audio_parquets,
        network_gexf=NETWORK_GEXF,
        video_parquet=None,
        window_sec=WINDOW_SEC,
        step_sec=STEP_SEC,
    )
    observed_mean = float(timeline["E"].mean())
    print(f"E(t) timeline: {len(timeline)} rows, mean E = {observed_mean:.4f}")

    print(f"Running {N_NULL_SHUFFLES}-shuffle circular-shift null...")
    null = compute_entanglement_null(
        audio_parquets=audio_parquets,
        network_gexf=NETWORK_GEXF,
        video_parquet=None,
        window_sec=WINDOW_SEC,
        step_sec=STEP_SEC,
        n_shuffles=N_NULL_SHUFFLES,
        seed=42,
    )
    p_null = float((null >= observed_mean).mean())
    print(
        f"Null mean = {np.nanmean(null):.4f} (std {np.nanstd(null):.4f}); "
        f"observed mean = {observed_mean:.4f}; p_null = {p_null:.4f}"
    )

    _plot(timeline, observed_mean, null, p_null, FIGURE_OUT)
    print(f"Wrote {FIGURE_OUT}")


def _plot(timeline, observed_mean, null, p_null, output: Path) -> None:
    fig, axes = plt.subplots(2, 1, figsize=(11, 7), gridspec_kw={"height_ratios": [3, 1]})

    ax_ts = axes[0]
    ax_ts.plot(timeline["time_sec"], timeline["A"], label="A(t) audio coupling",
               color="#1f77b4", linewidth=1.1)
    ax_ts.plot(timeline["time_sec"], timeline["N"], label="N(t) network density",
               color="#2ca02c", linewidth=1.1, linestyle="--")
    ax_ts.plot(timeline["time_sec"], timeline["V"], label="V(t) visual (NaN: Dagstuhl audio-only)",
               color="#ff7f0e", linewidth=1.1)
    ax_ts.plot(timeline["time_sec"], timeline["E"], label="E(t) composite (weight-reallocated)",
               color="#d62728", linewidth=2.0)
    ax_ts.axhline(observed_mean, color="#d62728", alpha=0.3, linestyle=":",
                  label=f"mean E = {observed_mean:.3f}")
    ax_ts.set_xlabel("Time (s)")
    ax_ts.set_ylabel("Coupling / coherence")
    ax_ts.set_title(
        f"E(t) integration demo · Dagstuhl {TAKE_ID} · "
        f"{WINDOW_SEC:.0f}s window @ {1/STEP_SEC:.0f} Hz\n"
        f"V(t) absent (no video) → E = mean(A, N); H1/H3 visual test deferred to Tier-1 pairing"
    )
    ax_ts.legend(loc="lower right", fontsize=8, ncol=2)
    ax_ts.grid(True, alpha=0.3)

    ax_null = axes[1]
    finite_null = null[np.isfinite(null)]
    ax_null.hist(finite_null, bins=30, color="#888888", alpha=0.7, edgecolor="black")
    ax_null.axvline(observed_mean, color="#d62728", linewidth=2.0,
                    label=f"observed = {observed_mean:.3f}")
    ax_null.set_xlabel("Mean E(t) under 200 circular-shift permutations")
    ax_null.set_ylabel("Count")
    ax_null.set_title(f"Empirical null distribution · p_null = {p_null:.4f}")
    ax_null.legend(fontsize=8)
    ax_null.grid(True, alpha=0.3)

    fig.tight_layout()
    output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output, dpi=150, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    run()
