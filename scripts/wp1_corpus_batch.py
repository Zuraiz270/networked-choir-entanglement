"""Dataset-agnostic WP1 batch: extract per-singer features for any Tier-2 dataset.

Generalizes ``wp1_dagstuhl_batch.py`` via the dataset adapters in
``choir_entanglement.datasets``. Produces the same
``data/processed/{dataset}/{piece_id}/{singer}.parquet`` layout WP3/E(t)
consume, plus a per-dataset ``_summary.csv`` of pairwise RMS coupling.

Resumable: existing per-singer parquets are reused, not re-extracted.

Usage:
    python -m scripts.wp1_corpus_batch --dataset esmuc
    python -m scripts.wp1_corpus_batch --dataset choralsynth --limit 5
    python -m scripts.wp1_corpus_batch --dataset dagstuhl --takes-only
"""

from __future__ import annotations

import argparse
import time
from itertools import combinations

import pandas as pd

from choir_entanglement.audio.coupling import compute_pairwise_coupling, load_feature_parquet
from choir_entanglement.audio.pipeline import extract_to_parquet
from choir_entanglement.datasets import PROCESSED_ROOT, PieceManifest, build_manifests


def process_piece(manifest: PieceManifest) -> dict[str, object]:
    """Extract features per singer (resume-safe), compute pairwise coupling, return summary row."""
    manifest.out_dir.mkdir(parents=True, exist_ok=True)
    features: dict[str, pd.DataFrame] = {}
    extracted = reused = 0
    duration_sec = 0.0

    for singer, src in manifest.singer_wavs.items():
        parquet = manifest.out_dir / f"{singer}.parquet"
        if parquet.exists():
            features[singer] = load_feature_parquet(parquet)
            reused += 1
        else:
            features[singer] = extract_to_parquet(src, parquet)
            extracted += 1
        duration_sec = max(duration_sec, float(features[singer]["time_sec"].iloc[-1]))

    couplings: list[float] = []
    for a, b in combinations(sorted(features), 2):
        try:
            r = compute_pairwise_coupling(features[a], features[b], max_lag_sec=1.0, signal="rms")
        except ValueError:
            continue
        couplings.append(r.peak_correlation)

    s = pd.Series(couplings, dtype="float64")
    return {
        "dataset": manifest.dataset,
        "piece_id": manifest.piece_id,
        "unit": manifest.unit,
        "n_singers": len(features),
        "n_pairs": len(couplings),
        "duration_sec": round(duration_sec, 2),
        "mean_coupling": round(float(s.mean()), 4) if len(s) else float("nan"),
        "max_coupling": round(float(s.max()), 4) if len(s) else float("nan"),
        "min_coupling": round(float(s.min()), 4) if len(s) else float("nan"),
        "singers_extracted": extracted,
        "singers_reused": reused,
    }


def run(dataset: str, limit: int | None, takes_only: bool) -> None:
    manifests = build_manifests(dataset)
    if takes_only:
        manifests = [m for m in manifests if "take" in m.piece_id.lower()]
    if limit:
        manifests = manifests[:limit]
    print(f"{dataset}: {len(manifests)} pieces to process.")

    out_root = PROCESSED_ROOT / dataset
    out_root.mkdir(parents=True, exist_ok=True)
    rows: list[dict[str, object]] = []
    t0 = time.perf_counter()

    for i, manifest in enumerate(manifests, 1):
        t = time.perf_counter()
        row = process_piece(manifest)
        rows.append(row)
        print(
            f"  [{i}/{len(manifests)}] {manifest.piece_id}: "
            f"{row['n_singers']} {row['unit']}s, {row['n_pairs']} pairs, "
            f"mean coupling {row['mean_coupling']}, "
            f"{row['singers_extracted']} extracted / {row['singers_reused']} reused, "
            f"{time.perf_counter() - t:.1f}s"
        )

    summary = pd.DataFrame(rows).sort_values("piece_id").reset_index(drop=True)
    summary_path = out_root / "_summary.csv"
    summary.to_csv(summary_path, index=False)
    print(f"\nWrote {summary_path} ({len(summary)} rows, {(time.perf_counter() - t0)/60:.1f} min).")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dataset", required=True, choices=["dagstuhl", "esmuc", "choralsynth"])
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument(
        "--takes-only", action="store_true",
        help="Dagstuhl/ESMUC: restrict to piece_ids containing 'take'.",
    )
    args = parser.parse_args()
    run(dataset=args.dataset, limit=args.limit, takes_only=args.takes_only)


if __name__ == "__main__":
    main()
