"""Write the SLURM array cell list: one '<dataset> <piece>' per line.

Cells are the (dataset, piece) pairs of the PUBLISHED 28-piece latency corpus
(read from data/processed/tier3/_latency_grid.csv), so the 2000-shuffle rerun
covers exactly the same pieces as the report numbers, no scope drift.

One array task per piece (all 5 latency levels serially): cells of one piece
share the loaded clean frames, and the longest piece (12-singer ESMUC,
132 pairs x 5 levels) bounds the wall time.

Usage (from repo root):
    python -m scripts.hpc.make_cells > scripts/hpc/cells.txt
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd

GRID = Path("data/processed/tier3/_latency_grid.csv")

df = pd.read_csv(GRID)
for dataset, piece in sorted(df[["dataset", "piece"]].drop_duplicates().itertuples(index=False)):
    print(f"{dataset} {piece}")
