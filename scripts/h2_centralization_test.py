"""H2 (redone): is there leadership structure in real choir influence networks?

The original H2 ("topology shifts democratic -> leader-dominated as latency
rises") was untestable with our design (latency injection on pre-coordinated
studio audio cannot create a behavioural leader, and fixed-lag Granger
saturates under delay). This redo asks the part we CAN test on real data:

    At zero latency, is a choir's directed influence network more centralized
    (leader-like) than a random graph with the same number of singers and
    edges?

Operationalization: out-degree centralization = Gini coefficient of node
out-degree in the clean-level Granger influence graph. 0 = every singer
exerts equal outgoing influence (democratic); ->1 = one singer drives all
(leader). We compare each piece's observed Gini to an Erdos-Renyi null with
the same node and edge count (1000 draws), one-sided empirical p.

Reads the clean-level rows already computed in the Tier-3 grid (observed
Gini, singer count, edge count). Writes data/processed/tier3/_h2_centralization.csv.

Usage:
    python -m scripts.h2_centralization_test
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
from numpy.typing import NDArray

GRID_CSV = Path("data/processed/tier3/_latency_grid_2000.csv")
OUT_CSV = Path("data/processed/tier3/_h2_centralization.csv")
N_NULL = 1000
SEED = 42
FloatArray = NDArray[np.float64]


def gini(x: FloatArray) -> float:
    x = np.sort(np.asarray(x, dtype=np.float64))
    n = x.size
    if n == 0 or x.sum() == 0:
        return 0.0
    return float((n + 1 - 2 * np.sum(np.cumsum(x)) / x.sum()) / n)


def null_gini_distribution(n_nodes: int, n_edges: int, rng: np.random.Generator) -> FloatArray:
    """Out-degree Gini for ER digraphs with n_nodes, n_edges (no self-loops)."""
    max_edges = n_nodes * (n_nodes - 1)
    n_edges = min(n_edges, max_edges)
    # enumerate the directed off-diagonal cell -> source-node mapping
    sources = np.array([i for i in range(n_nodes) for j in range(n_nodes) if i != j])
    out = np.empty(N_NULL, dtype=np.float64)
    for k in range(N_NULL):
        chosen = rng.choice(max_edges, size=n_edges, replace=False)
        outdeg = np.bincount(sources[chosen], minlength=n_nodes).astype(np.float64)
        out[k] = gini(outdeg)
    return out


def empirical_upper_p(observed: float, null: FloatArray) -> float:
    """Return a plus-one upper-tail p-value for a four-decimal observation."""
    rounding_tolerance = 0.5e-4 + np.finfo(float).eps
    exceedances = int(np.count_nonzero(null >= observed - rounding_tolerance))
    return (exceedances + 1) / (len(null) + 1)


def run() -> None:
    g = pd.read_csv(GRID_CSV)
    clean = g[g.level == "clean"].copy()
    rng = np.random.default_rng(SEED)
    rows = []
    for _, r in clean.iterrows():
        n, m = int(r["n_singers"]), int(r["n_sig_edges"])
        obs = float(r["gini_out_degree"])
        null = null_gini_distribution(n, m, rng)
        p_more = empirical_upper_p(obs, null)
        rows.append(
            {
                "dataset": r["dataset"],
                "piece": r["piece"],
                "unit": r["unit"],
                "n_singers": n,
                "n_edges": m,
                "density": round(m / (n * (n - 1)), 3),
                "obs_gini_outdeg": round(obs, 4),
                "null_gini_mean": round(float(null.mean()), 4),
                "null_gini_sd": round(float(null.std()), 4),
                "p_more_centralized": round(p_more, 4),
            }
        )
    out = pd.DataFrame(rows).sort_values(["dataset", "piece"]).reset_index(drop=True)
    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(OUT_CSV, index=False)

    # summary
    sig = out[out["p_more_centralized"] < 0.05]
    print(f"Wrote {OUT_CSV} ({len(out)} clean pieces)")
    print(
        f"Mean observed out-degree Gini: {out['obs_gini_outdeg'].mean():.3f} "
        f"(null mean {out['null_gini_mean'].mean():.3f})"
    )
    print(
        f"Pieces significantly MORE centralized than random (p<0.05): " f"{len(sig)} / {len(out)}"
    )
    print(f"Mean density: {out['density'].mean():.2f}")
    for ds in ["dagstuhl", "esmuc", "choralsynth"]:
        d = out[out.dataset == ds]
        if len(d):
            print(
                f"  {ds}: obs Gini {d['obs_gini_outdeg'].mean():.3f} vs null "
                f"{d['null_gini_mean'].mean():.3f}; {int((d['p_more_centralized']<0.05).sum())}/{len(d)} sig"
            )


if __name__ == "__main__":
    run()
