"""Merge HPC shard CSVs from tier3_latency_grid --out into one grid CSV.

Usage:
    python -m scripts.tier3_merge_shards --shards data/processed/tier3/shards --out data/processed/tier3/_latency_grid_2000.csv
"""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--shards", type=Path, required=True, help="directory of shard CSVs")
    p.add_argument("--out", type=Path, required=True)
    args = p.parse_args()

    files = sorted(args.shards.glob("*.csv"))
    if not files:
        raise SystemExit(f"no shard CSVs under {args.shards}")
    df = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)
    before = len(df)
    df = df.drop_duplicates(subset=["dataset", "piece", "level"], keep="last")
    df = df.sort_values(["dataset", "piece", "level"]).reset_index(drop=True)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(args.out, index=False)
    print(
        f"Merged {len(files)} shards -> {args.out} ({len(df)} rows; {before - len(df)} duplicate rows dropped)"
    )
    # completeness check: expected 5 levels per (dataset, piece)
    counts = df.groupby(["dataset", "piece"]).size()
    incomplete = counts[counts != 5]
    if len(incomplete):
        print("WARNING, incomplete pieces (expected 5 levels each):")
        print(incomplete.to_string())
    else:
        print(f"Completeness OK: {counts.size} pieces x 5 levels.")


if __name__ == "__main__":
    main()
