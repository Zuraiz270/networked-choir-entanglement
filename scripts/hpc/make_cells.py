"""Write the SLURM array cell list: one '<dataset> <piece> <level>' per line.

Cells are the (dataset, piece, level) triples of the PUBLISHED 28-piece
latency corpus (read from data/processed/tier3/_latency_grid.csv), so the
2000-shuffle rerun covers exactly the same grid as the report numbers,
no scope drift. 140 cells total.

One array task per (piece, level): at 2000 shuffles the largest cell
(12-singer ESMUC, 132 ordered pairs) is ~11 h at the measured ~5 min/pair,
safely inside a 24 h wall-time limit; per-piece sharding (5 levels serial)
would exceed it (~55 h).

Usage (from repo root):
    python -m scripts.hpc.make_cells > scripts/hpc/cells.txt
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd

GRID = Path("data/processed/tier3/_latency_grid.csv")

df = pd.read_csv(GRID)
cells = df[["dataset", "piece", "level"]].drop_duplicates()
for dataset, piece, level in sorted(cells.itertuples(index=False)):
    print(f"{dataset} {piece} {level}")
