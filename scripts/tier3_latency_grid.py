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
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from choir_entanglement.entanglement import compute_entanglement, compute_entanglement_null
from choir_entanglement.latency import LATENCY_LEVELS_MS, LatencyConfig, inject_latency_take
from choir_entanglement.network.influence_graph import build_influence_graph, graph_metrics
from scripts.wp3_dagstuhl_batch import run_pairwise

PROCESSED_BASE = Path("data/processed")
OUT_DIR = Path("data/processed/tier3")
GRID_CSV = OUT_DIR / "_latency_grid.csv"
FIGURE_OUT = Path("data/figures/tier3_latency_grid.png")
STEP_SEC = 0.5
N_NULL = 100
MAXLAG = 8


def load_clean_frames(processed_root: Path, piece: str) -> dict[str, pd.DataFrame]:
    return {
        p.stem: pd.read_parquet(p)
        for p in sorted((processed_root / piece).glob("*.parquet"))
    }


def gini(values: np.ndarray) -> float:
    """Gini coefficient of a non-negative vector (0 = equal, ->1 = concentrated)."""
    v = np.sort(np.asarray(values, dtype=np.float64))
    n = v.size
    if n == 0 or v.sum() == 0:
        return 0.0
    cum = np.cumsum(v)
    return float((n + 1 - 2 * np.sum(cum) / cum[-1]) / n)


def process_cell(
    dataset: str, piece: str, unit: str, level: str, delay_ms: float,
    clean: dict[str, pd.DataFrame],
) -> dict[str, object]:
    delayed = inject_latency_take(clean, LatencyConfig(delay_ms=delay_ms))
    rms_series = {s: df["rms"].to_numpy(np.float64) for s, df in delayed.items()}
    n_min = min(len(a) for a in rms_series.values())
    rms_series = {s: a[:n_min] for s, a in rms_series.items()}

    # Latency injection blanks leading frames to NaN; Granger (statsmodels)
    # rejects NaN. Trim the blanked head uniformly so we analyse the
    # steady-state delayed region. (compute_entanglement is NaN-tolerant and
    # keeps the full series for A(t)/null.)
    stacked = np.vstack(list(rms_series.values()))
    finite_cols = np.all(np.isfinite(stacked), axis=0)
    first = int(np.argmax(finite_cols)) if finite_cols.any() else n_min
    rms_series = {s: a[first:] for s, a in rms_series.items()}

    results = run_pairwise(rms_series, method="standard", maxlag=MAXLAG, n_shuffles=N_NULL)
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
        timeline = compute_entanglement(audio_paths, gexf, window_sec=10.0, step_sec=STEP_SEC)
        e = timeline["E"].dropna().to_numpy()
        a = timeline["A"].dropna().to_numpy()
        null = compute_entanglement_null(audio_paths, gexf, window_sec=10.0,
                                         step_sec=STEP_SEC, n_shuffles=N_NULL, seed=42)

    null = null[np.isfinite(null)]
    e_mean = float(e.mean()) if e.size else float("nan")
    p_null = float((null >= e_mean).mean()) if null.size else float("nan")
    return {
        "dataset": dataset, "piece": piece, "unit": unit, "level": level,
        "delay_ms": delay_ms, "n_singers": len(rms_series),
        "A_mean": round(float(a.mean()) if a.size else float("nan"), 4),
        "N_density": round(float(m.density), 4),
        "E_mean": round(e_mean, 4),
        "n_sig_edges": int(m.n_edges),
        "max_eigen_centrality": round(float(m.most_central_score), 4),
        "gini_out_degree": round(gini(out_degrees), 4),
        "null_mean": round(float(null.mean()) if null.size else float("nan"), 4),
        "p_null": round(p_null, 4),
    }


def render_figure(df: pd.DataFrame, output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.5))
    for piece, g in df.groupby("piece"):
        g = g.sort_values("delay_ms")
        ax1.plot(g["delay_ms"], g["E_mean"], marker="o", label=piece, linewidth=1.3)
        ax2.plot(g["delay_ms"], g["N_density"], marker="s", label=piece, linewidth=1.3)
    for ax, ylab, title in (
        (ax1, "Mean E(t) (audio+network)", "H1: coordination vs latency"),
        (ax2, "Influence-graph density", "H2: topology vs latency"),
    ):
        ax.set_xlabel("Injected one-way latency (ms)")
        ax.set_ylabel(ylab)
        ax.set_title(title)
        ax.grid(True, alpha=0.3)
    ax1.legend(fontsize=7, loc="best")
    fig.suptitle("Tier-3 latency injection (constant delay, standard Granger, 100-shuffle null)",
                 fontsize=12)
    fig.tight_layout()
    fig.savefig(output, dpi=150, bbox_inches="tight")
    plt.close(fig)


def discover_pieces(processed_root: Path) -> list[str]:
    return sorted(
        d.name for d in processed_root.iterdir()
        if d.is_dir() and len(list(d.glob("*.parquet"))) >= 2
    )


def run(dataset: str, pieces: list[str] | None, levels: list[str]) -> None:
    processed_root = PROCESSED_BASE / dataset
    unit = "part" if dataset == "choralsynth" else "singer"
    if pieces is None:
        pieces = discover_pieces(processed_root)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    print(f"{dataset}: {len(pieces)} pieces x {len(levels)} levels")
    rows: list[dict[str, object]] = []
    t0 = time.perf_counter()
    for piece in pieces:
        clean = load_clean_frames(processed_root, piece)
        if len(clean) < 2:
            print(f"  skip {piece} (<2 singers)")
            continue
        for level in levels:
            t = time.perf_counter()
            row = process_cell(dataset, piece, unit, level, LATENCY_LEVELS_MS[level], clean)
            rows.append(row)
            print(f"  {piece} [{level:11s}] E={row['E_mean']} density={row['N_density']} "
                  f"p_null={row['p_null']} ({time.perf_counter()-t:.0f}s)")

    df = pd.DataFrame(rows)
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
    parser.add_argument("--pieces", default=None, help="comma-separated piece ids (default: discover)")
    parser.add_argument("--levels", default=",".join(LATENCY_LEVELS_MS),
                        help="comma-separated latency levels")
    args = parser.parse_args()
    pieces = args.pieces.split(",") if args.pieces else None
    levels = [lv.strip() for lv in args.levels.split(",") if lv.strip()]
    run(args.dataset, pieces, levels)


if __name__ == "__main__":
    main()
