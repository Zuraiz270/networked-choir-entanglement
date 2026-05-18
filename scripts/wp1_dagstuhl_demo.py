"""Run WP1 audio pipeline on Dagstuhl ChoirSet QuartetA Take02 (Locus Iste).

Extracts F0 + onsets + RMS for SATB singers (S2/A1/T1/B1, dynamic mic), writes
per-singer feature parquets to data/processed/, computes pairwise A(t) couplings,
and saves the first deck figure to data/figures/.

Usage:
    python -m scripts.wp1_dagstuhl_demo
"""

from __future__ import annotations

from itertools import combinations
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from choir_entanglement.audio.coupling import compute_pairwise_coupling
from choir_entanglement.audio.pipeline import extract_to_parquet

DAGSTUHL_AUDIO_DIR = Path("data/raw/dagstuhl/DagstuhlChoirSet_V1.2.3/audio_wav_22050_mono")
PROCESSED_DIR = Path("data/processed/dagstuhl/LI_QuartetA_Take02")
FIGURES_DIR = Path("data/figures")
PIECE = "DCS_LI_QuartetA_Take02"
MIC = "DYN"
SINGERS = ["S2", "A1", "T1", "B1"]
VOICE_NAMES = {"S2": "Soprano", "A1": "Alto", "T1": "Tenor", "B1": "Bass"}
VOICE_COLORS = {"S2": "#d62728", "A1": "#ff7f0e", "T1": "#2ca02c", "B1": "#1f77b4"}


def run() -> None:
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)

    features = {}
    for singer in SINGERS:
        wav = DAGSTUHL_AUDIO_DIR / f"{PIECE}_{singer}_{MIC}.wav"
        parquet = PROCESSED_DIR / f"{singer}.parquet"
        if not wav.exists():
            raise FileNotFoundError(f"Missing: {wav}")
        print(f"  Extracting {VOICE_NAMES[singer]} ({singer}) from {wav.name}")
        features[singer] = extract_to_parquet(wav, parquet)

    print("\n--- Per-singer summary ---")
    for singer, df in features.items():
        voiced_pct = df["voiced"].mean() * 100
        median_f0 = df.loc[df["voiced"], "f0_hz"].median()
        onsets = int(df["onset"].sum())
        duration = df["time_sec"].iloc[-1]
        print(
            f"  {VOICE_NAMES[singer]:8s} {singer}: "
            f"{duration:.1f}s, voiced {voiced_pct:.1f}%, "
            f"median F0 {median_f0:.1f} Hz, {onsets} onsets"
        )

    print("\n--- Pairwise A(t) couplings (RMS envelope) ---")
    couplings: dict[tuple[str, str], object] = {}
    for a, b in combinations(SINGERS, 2):
        result = compute_pairwise_coupling(features[a], features[b], max_lag_sec=1.0, signal="rms")
        couplings[(a, b)] = result
        print(
            f"  {VOICE_NAMES[a]:8s}-{VOICE_NAMES[b]:8s} "
            f"peak corr {result.peak_correlation:+.3f}, lag {result.peak_lag_sec:+.3f}s"
        )

    _plot_satb_overview(features, couplings, FIGURES_DIR / "wp1_satb_coupling.png")
    print(f"\n  Figure: {FIGURES_DIR / 'wp1_satb_coupling.png'}")


def _plot_satb_overview(features: dict, couplings: dict, output: Path) -> None:
    fig, axes = plt.subplots(2, 1, figsize=(11, 7), gridspec_kw={"height_ratios": [2, 1]})

    ax_f0 = axes[0]
    for singer in SINGERS:
        df = features[singer]
        voiced_only = df["f0_hz"].where(df["voiced"])
        ax_f0.plot(
            df["time_sec"],
            voiced_only,
            color=VOICE_COLORS[singer],
            label=f"{VOICE_NAMES[singer]} ({singer})",
            linewidth=1.0,
        )
    ax_f0.set_ylabel("F0 (Hz)")
    ax_f0.set_xlabel("Time (s)")
    ax_f0.set_title(
        "WP1 audio pipeline · Dagstuhl ChoirSet · Locus Iste, Quartet A Take 02\n"
        "Per-singer F0 trajectories (pyin, dynamic mic)"
    )
    ax_f0.legend(loc="upper right", ncol=4, fontsize=8)
    ax_f0.grid(True, alpha=0.3)

    ax_mat = axes[1]
    n = len(SINGERS)
    corr_matrix = np.eye(n)
    for i, a in enumerate(SINGERS):
        for j, b in enumerate(SINGERS):
            if i == j:
                continue
            pair = (a, b) if (a, b) in couplings else (b, a)
            corr_matrix[i, j] = couplings[pair].peak_correlation
    im = ax_mat.imshow(corr_matrix, cmap="RdBu_r", vmin=-1, vmax=1, aspect="auto")
    ax_mat.set_xticks(range(n), [VOICE_NAMES[s] for s in SINGERS])
    ax_mat.set_yticks(range(n), [VOICE_NAMES[s] for s in SINGERS])
    ax_mat.set_title("Pairwise A(t) coupling: peak RMS-envelope cross-correlation")
    for i in range(n):
        for j in range(n):
            ax_mat.text(j, i, f"{corr_matrix[i, j]:+.2f}", ha="center", va="center", fontsize=9)
    fig.colorbar(im, ax=ax_mat, fraction=0.03, pad=0.02)

    fig.tight_layout()
    fig.savefig(output, dpi=150, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    run()
