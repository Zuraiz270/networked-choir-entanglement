"""Tier-3 cross-regime grid: E(t) and influence-graph topology vs injected latency.

For each piece and each latency level, causally delays the per-singer feature
frames (clean studio audio -> simulated NMP regime), recomputes the influence
graph (standard Granger), and the E(t) timeline with a circular-shift null,
then records a tidy long row. This is the first test of H1 (E drops with
latency) and H2 (topology shifts toward leader-dominated).

Compute control (per plan): standard Granger only, 100-shuffle null, 0.5s step.
Latency is deterministic (constant delay), so no seed replication.

Usage:
    python -m scripts.tier3_latency_grid --dataset dagstuhl
    python -m scripts.tier3_latency_grid --dataset dagstuhl --pieces LI_QuartetA_Take02 --levels clean,zoom
"""

from __future__ import annotations

import argparse
import tempfile
import time
from itertools import combinations
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scripts.wp3_dagstuhl_batch import run_pairwise

from choir_entanglement.audio.coupling import onset_synchrony
from choir_entanglement.entanglement import compute_entanglement, compute_entanglement_null
from choir_entanglement.latency import LATENCY_REGIMES, inject_latency_take
from choir_entanglement.network.influence_graph import build_influence_graph, graph_metrics

PROCESSED_BASE = Path("data/processed")
OUT_DIR = Path("data/processed/tier3")
GRID_CSV = OUT_DIR / "_latency_grid.csv"
FIGURE_OUT = Path("data/figures/tier3_latency_grid.png")
STEP_SEC = 0.5
N_NULL = 100
MAXLAG = 8


def load_clean_frames(processed_root: Path, piece: str) -> dict[str, pd.DataFrame]:
    return {p.stem: pd.read_parquet(p) for p in sorted((processed_root / piece).glob("*.parquet"))}


def gini(values: np.ndarray) -> float:
    """Gini coefficient of a non-negative vector (0 = equal, ->1 = concentrated)."""
    v = np.sort(np.asarray(values, dtype=np.float64))
    n = v.size
    if n == 0 or v.sum() == 0:
        return 0.0
    cum = np.cumsum(v)
    return float((n + 1 - 2 * np.sum(cum) / cum[-1]) / n)


def process_cell(
    dataset: str,
    piece: str,
    unit: str,
    level: str,
    clean: dict[str, pd.DataFrame],
    n_shuffles: int = N_NULL,
) -> dict[str, object]:
    config = LATENCY_REGIMES[level]
    delay_ms = config.delay_ms
    delayed = inject_latency_take(clean, config)

    # Zero-lag onset synchrony on the JITTERED onset trains (not concealment-
    # filled): the physical attack-timing quantity latency degrades. Mean over
    # all singer pairs.
    onset_arrays = {s: df["onset"].fillna(False).to_numpy(bool) for s, df in delayed.items()}
    sync_vals = [
        onset_synchrony(onset_arrays[a], onset_arrays[b])
        for a, b in combinations(sorted(onset_arrays), 2)
    ]
    sync_finite = [v for v in sync_vals if np.isfinite(v)]
    onset_sync = float(np.mean(sync_finite)) if sync_finite else float("nan")

    rms_series = {s: df["rms"].to_numpy(np.float64) for s, df in delayed.items()}
    n_min = min(len(a) for a in rms_series.values())
    rms_series = {s: a[:n_min] for s, a in rms_series.items()}

    # Latency injection blanks frames to NaN (leading frames from the causal
    # shift, scattered frames from dropout). Granger (statsmodels) rejects NaN,
    # so fill via packet-loss CONCEALMENT (hold last received value: ffill then
    # bfill) - which is what real NMP clients do. compute_entanglement keeps the
    # raw NaN series (it is NaN-tolerant) for A(t)/null.
    rms_series = {
        s: pd.Series(a).ffill().bfill().to_numpy(np.float64) for s, a in rms_series.items()
    }

    results = run_pairwise(rms_series, method="standard", maxlag=MAXLAG, n_shuffles=n_shuffles)
    graph = build_influence_graph(results, significance=0.05)
    m = graph_metrics(graph)
    out_degrees = np.array([d for _, d in graph.out_degree()], dtype=np.float64)

    with tempfile.TemporaryDirectory(prefix="tier3_") as tmp:
        tmpdir = Path(tmp)
        audio_paths = {}
        for s, df in delayed.items():
            p = tmpdir / f"{s}.parquet"
            df.to_parquet(p)
            audio_paths[s] = p
        gexf = tmpdir / "g.gexf"
        import networkx as nx

        nx.write_gexf(graph, gexf)
        # E column semantics: envelope-only A(t) (include_onsets=False), the
        # definition every published Sprint-3/4 number used; E_comb_mean adds
        # the onset-folded A(t) (2026-07 definition) alongside, never instead.
        timeline = compute_entanglement(
            audio_paths, gexf, window_sec=10.0, step_sec=STEP_SEC, include_onsets=False
        )
        e = timeline["E"].dropna().to_numpy()
        a = timeline["A"].dropna().to_numpy()
        timeline_comb = compute_entanglement(
            audio_paths, gexf, window_sec=10.0, step_sec=STEP_SEC, include_onsets=True
        )
        e_comb = timeline_comb["E"].dropna().to_numpy()
        null = compute_entanglement_null(
            audio_paths,
            gexf,
            window_sec=10.0,
            step_sec=STEP_SEC,
            n_shuffles=n_shuffles,
            seed=42,
            include_onsets=False,
        )

    null = null[np.isfinite(null)]
    e_mean = float(e.mean()) if e.size else float("nan")
    p_null = float((null >= e_mean).mean()) if null.size else float("nan")
    return {
        "dataset": dataset,
        "piece": piece,
        "unit": unit,
        "level": level,
        "delay_ms": delay_ms,
        "jitter_sd_ms": config.jitter_sd_ms,
        "dropout_rate": config.dropout_rate,
        "n_singers": len(rms_series),
        "A_mean": round(float(a.mean()) if a.size else float("nan"), 4),
        "onset_sync": round(onset_sync, 4),
        "N_density": round(float(m.density), 4),
        "E_mean": round(e_mean, 4),
        "E_comb_mean": round(float(e_comb.mean()) if e_comb.size else float("nan"), 4),
        "n_sig_edges": int(m.n_edges),
        "max_eigen_centrality": round(float(m.most_central_score), 4),
        "gini_out_degree": round(gini(out_degrees), 4),
        "null_mean": round(float(null.mean()) if null.size else float("nan"), 4),
        "p_null": round(p_null, 4),
    }


def render_figure(df: pd.DataFrame, output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(16, 5.2))
    x = "jitter_sd_ms" if "jitter_sd_ms" in df.columns else "delay_ms"
    panels = [
        (ax1, "onset_sync", "Zero-lag onset synchrony", "Attack-timing (latency-sensitive)"),
        (ax2, "E_mean", "Mean E(t) (envelope+network)", "Envelope E(t) (latency-robust)"),
        (ax3, "N_density", "Influence-graph density", "Network topology"),
    ]
    for ax, col, ylab, title in panels:
        if col not in df.columns:
            continue
        for piece, g in df.groupby("piece"):
            g = g.sort_values(x)
            ax.plot(g[x], g[col], marker="o", label=piece, linewidth=1.2)
        ax.set_xlabel("Injected jitter SD (ms)" if x == "jitter_sd_ms" else "Delay (ms)")
        ax.set_ylabel(ylab)
        ax.set_title(title)
        ax.grid(True, alpha=0.3)
    ax1.legend(fontsize=7, loc="best")
    fig.suptitle(
        "Tier-3 latency injection (jitter model, standard Granger, 100-shuffle null)", fontsize=12
    )
    fig.tight_layout()
    fig.savefig(output, dpi=150, bbox_inches="tight")
    plt.close(fig)


def discover_pieces(processed_root: Path) -> list[str]:
    return sorted(
        d.name
        for d in processed_root.iterdir()
        if d.is_dir() and len(list(d.glob("*.parquet"))) >= 2
    )


def run(
    dataset: str,
    pieces: list[str] | None,
    levels: list[str],
    n_shuffles: int = N_NULL,
    out: Path | None = None,
) -> None:
    """Full run merges into the shared grid CSV; ``out`` = shard mode.

    Shard mode (HPC): write ONLY this invocation's rows to ``out``, no
    merge with the shared CSV and no figure, so concurrent SLURM array
    tasks never read-modify-write the same file. Merge shards afterwards
    with scripts/tier3_merge_shards.py.
    """
    processed_root = PROCESSED_BASE / dataset
    unit = "part" if dataset == "choralsynth" else "singer"
    if pieces is None:
        pieces = discover_pieces(processed_root)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    print(f"{dataset}: {len(pieces)} pieces x {len(levels)} levels x {n_shuffles} shuffles")
    rows: list[dict[str, object]] = []
    t0 = time.perf_counter()
    for piece in pieces:
        clean = load_clean_frames(processed_root, piece)
        if len(clean) < 2:
            print(f"  skip {piece} (<2 singers)")
            continue
        for level in levels:
            t = time.perf_counter()
            row = process_cell(dataset, piece, unit, level, clean, n_shuffles=n_shuffles)
            rows.append(row)
            print(
                f"  {piece} [{level:11s}] E={row['E_mean']} density={row['N_density']} "
                f"p_null={row['p_null']} ({time.perf_counter()-t:.0f}s)"
            )

    df = pd.DataFrame(rows)
    if out is not None:
        out.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(out, index=False)
        print(f"\nWrote shard {out} ({len(df)} rows; {(time.perf_counter()-t0)/60:.1f} min)")
        return
    # merge with any existing grid rows from other datasets
    if GRID_CSV.exists():
        prev = pd.read_csv(GRID_CSV)
        prev = prev[~prev["dataset"].eq(dataset)]
        df = pd.concat([prev, df], ignore_index=True)
    df.to_csv(GRID_CSV, index=False)
    print(f"\nWrote {GRID_CSV} ({len(df)} rows; {(time.perf_counter()-t0)/60:.1f} min)")
    render_figure(df, FIGURE_OUT)
    print(f"Wrote {FIGURE_OUT}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dataset", required=True, choices=["dagstuhl", "esmuc", "choralsynth"])
    parser.add_argument(
        "--pieces", default=None, help="comma-separated piece ids (default: discover)"
    )
    parser.add_argument(
        "--levels", default=",".join(LATENCY_REGIMES), help="comma-separated latency regimes"
    )
    parser.add_argument(
        "--shuffles",
        type=int,
        default=N_NULL,
        help=f"null permutations for Granger + E(t) (default {N_NULL}; paper-grade 2000)",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=None,
        help="shard mode: write rows to this CSV only (no merge, no figure)",
    )
    args = parser.parse_args()
    pieces = args.pieces.split(",") if args.pieces else None
    levels = [lv.strip() for lv in args.levels.split(",") if lv.strip()]
    run(args.dataset, pieces, levels, n_shuffles=args.shuffles, out=args.out)


if __name__ == "__main__":
    main()
