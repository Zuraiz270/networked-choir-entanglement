"""Summarize the paired H1 onset-synchrony result from the latency grid.

The Tier-3 latency grid contains repeated conditions for each musical piece.
This script pairs the clean and Zoom endpoints within each piece, reports the
percentage drop, and tests whether decreases occur more often than chance.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import binomtest

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "data/processed/tier3/_latency_grid_2000.csv"
DEFAULT_OUTPUT = ROOT / "data/processed/tier3/_h1_paired_test.csv"


def _paired_drops(frame: pd.DataFrame) -> pd.Series:
    paired = frame.pivot(index="piece", columns="level", values="onset_sync")
    missing = {"clean", "zoom"} - set(paired.columns)
    if missing:
        raise ValueError(f"missing latency endpoint columns: {sorted(missing)}")
    paired = paired[["clean", "zoom"]].dropna()
    if paired.empty:
        raise ValueError("no complete clean/zoom piece pairs")
    if (paired["clean"] <= 0).any():
        raise ValueError("clean onset synchrony must be positive")
    return 100.0 * (paired["clean"] - paired["zoom"]) / paired["clean"]


def _summary_row(
    dataset: str,
    frame: pd.DataFrame,
    *,
    n_bootstrap: int,
    rng: np.random.Generator,
) -> dict[str, float | int | str]:
    drops = _paired_drops(frame)
    values = drops.to_numpy(dtype=float)
    n_pieces = len(values)
    n_decreased = int(np.count_nonzero(values > 0))
    bootstrap_means = rng.choice(values, size=(n_bootstrap, n_pieces), replace=True).mean(axis=1)
    ci_low, ci_high = np.percentile(bootstrap_means, [2.5, 97.5])
    return {
        "dataset": dataset,
        "n_pieces": n_pieces,
        "n_decreased": n_decreased,
        "mean_drop_pct": float(values.mean()),
        "median_drop_pct": float(np.median(values)),
        "min_drop_pct": float(values.min()),
        "max_drop_pct": float(values.max()),
        "sign_test_p_one_sided": float(
            binomtest(n_decreased, n_pieces, p=0.5, alternative="greater").pvalue
        ),
        "bootstrap_ci_low_pct": float(ci_low),
        "bootstrap_ci_high_pct": float(ci_high),
    }


def summarize_onset_drop(
    grid: pd.DataFrame,
    *,
    n_bootstrap: int = 10_000,
    seed: int = 42,
) -> pd.DataFrame:
    """Return per-dataset and overall paired clean-to-Zoom H1 summaries."""
    required = {"dataset", "piece", "level", "onset_sync"}
    missing = required - set(grid.columns)
    if missing:
        raise ValueError(f"missing required columns: {sorted(missing)}")
    if n_bootstrap <= 0:
        raise ValueError("n_bootstrap must be positive")

    rng = np.random.default_rng(seed)
    rows = [
        _summary_row(str(dataset), frame, n_bootstrap=n_bootstrap, rng=rng)
        for dataset, frame in grid.groupby("dataset", sort=True)
    ]
    rows.append(_summary_row("all", grid, n_bootstrap=n_bootstrap, rng=rng))
    return pd.DataFrame(rows)


def run(input_path: Path, output_path: Path, *, n_bootstrap: int, seed: int) -> pd.DataFrame:
    """Read the latency grid, write the paired H1 summary, and return it."""
    result = summarize_onset_drop(
        pd.read_csv(input_path),
        n_bootstrap=n_bootstrap,
        seed=seed,
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    result.to_csv(output_path, index=False, float_format="%.10g")
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--bootstrap", type=int, default=10_000)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()
    result = run(args.input, args.output, n_bootstrap=args.bootstrap, seed=args.seed)
    print(result.to_string(index=False))
    print(f"Wrote {args.output}")


if __name__ == "__main__":
    main()
