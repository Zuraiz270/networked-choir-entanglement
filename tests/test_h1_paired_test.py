"""Tests for the piece-level H1 onset-synchrony analysis."""

from __future__ import annotations

import pandas as pd
from scripts.h1_paired_test import summarize_onset_drop


def test_summarize_onset_drop_uses_within_piece_pairs() -> None:
    rows = []
    for piece, clean in (("p1", 0.8), ("p2", 0.6), ("p3", 0.4), ("p4", 0.2)):
        rows.extend(
            [
                {"dataset": "demo", "piece": piece, "level": "clean", "onset_sync": clean},
                {"dataset": "demo", "piece": piece, "level": "zoom", "onset_sync": clean / 2},
            ]
        )

    result = summarize_onset_drop(pd.DataFrame(rows), n_bootstrap=200, seed=7)
    demo = result[result["dataset"] == "demo"].iloc[0]

    assert demo["n_pieces"] == 4
    assert demo["n_decreased"] == 4
    assert demo["mean_drop_pct"] == 50.0
    assert demo["sign_test_p_one_sided"] == 0.0625
    assert demo["bootstrap_ci_low_pct"] == 50.0
    assert demo["bootstrap_ci_high_pct"] == 50.0
