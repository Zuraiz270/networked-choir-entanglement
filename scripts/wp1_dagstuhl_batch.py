"""Scale WP1 audio pipeline across all Dagstuhl ChoirSet pieces.

Walks ``data/raw/dagstuhl/DagstuhlChoirSet_V1.2.3/audio_wav_22050_mono/``,
groups by ``(piece, section, take, singer)``, picks the canonical mic per
singer (DYN > HSM > LRX), runs ``extract_to_parquet`` per singer, then
computes per-take pairwise A(t) coupling and writes a corpus-level summary
to ``data/processed/dagstuhl/_summary.csv``.

The run is resumable: existing per-singer parquets are detected and reused;
the take-level coupling and summary row are recomputed each invocation so
the summary always reflects the latest parquet set.

Usage:
    python -m scripts.wp1_dagstuhl_batch [--limit N] [--takes-only]
"""

from __future__ import annotations

import argparse
import re
import time
from collections import defaultdict
from dataclasses import dataclass
from itertools import combinations
from pathlib import Path

import pandas as pd

from choir_entanglement.audio.coupling import compute_pairwise_coupling, load_feature_parquet
from choir_entanglement.audio.pipeline import extract_to_parquet

DAGSTUHL_AUDIO_DIR = Path("data/raw/dagstuhl/DagstuhlChoirSet_V1.2.3/audio_wav_22050_mono")
PROCESSED_ROOT = Path("data/processed/dagstuhl")
SUMMARY_CSV = PROCESSED_ROOT / "_summary.csv"

# Filename pattern: DCS_{piece}_{section}_{take}_{singer}_{mic}.wav
# Per-singer mics only; stereo mics (STL/STM/STR/SPL/SPR) and StereoReverb files skipped.
FILENAME_RE = re.compile(
    r"^DCS_(?P<piece>[A-Z]+)_(?P<section>[A-Za-z]+)_(?P<take>[A-Za-z0-9]+)_"
    r"(?P<singer>[SATB]\d)_(?P<mic>DYN|HSM|LRX)\.wav$"
)
MIC_PRIORITY = {"DYN": 0, "HSM": 1, "LRX": 2}


@dataclass(frozen=True)
class TakeManifest:
    """One Dagstuhl take with its canonical per-singer wav paths."""

    piece: str
    section: str
    take: str
    singer_wavs: dict[str, Path]  # singer_id -> canonical mic wav path

    @property
    def take_id(self) -> str:
        return f"{self.piece}_{self.section}_{self.take}"

    @property
    def out_dir(self) -> Path:
        return PROCESSED_ROOT / self.take_id


def build_manifest(audio_dir: Path, takes_only: bool) -> list[TakeManifest]:
    """Walk audio_dir, group per-singer wavs by take, pick canonical mic per singer."""
    by_take: dict[tuple[str, str, str], dict[str, list[tuple[int, Path]]]] = defaultdict(
        lambda: defaultdict(list)
    )
    for wav in sorted(audio_dir.glob("*.wav")):
        match = FILENAME_RE.match(wav.name)
        if not match:
            continue
        piece = match["piece"]
        section = match["section"]
        take = match["take"]
        if takes_only and not take.lower().startswith("take"):
            continue
        singer = match["singer"]
        mic = match["mic"]
        by_take[(piece, section, take)][singer].append((MIC_PRIORITY[mic], wav))

    manifests: list[TakeManifest] = []
    for (piece, section, take), singers in by_take.items():
        canonical: dict[str, Path] = {
            singer: min(candidates, key=lambda pair: pair[0])[1]
            for singer, candidates in singers.items()
        }
        if len(canonical) < 2:
            # Pairwise coupling needs at least 2 singers; solos are skipped.
            continue
        manifests.append(TakeManifest(piece, section, take, canonical))
    return sorted(manifests, key=lambda m: m.take_id)


def process_take(manifest: TakeManifest) -> dict[str, object]:
    """Extract features for each singer (resume-safe), compute pairwise coupling, return summary row."""
    manifest.out_dir.mkdir(parents=True, exist_ok=True)
    features: dict[str, pd.DataFrame] = {}
    reused = 0
    extracted = 0
    duration_sec = 0.0

    for singer, wav in manifest.singer_wavs.items():
        parquet = manifest.out_dir / f"{singer}.parquet"
        if parquet.exists():
            features[singer] = load_feature_parquet(parquet)
            reused += 1
        else:
            features[singer] = extract_to_parquet(wav, parquet)
            extracted += 1
        duration_sec = max(duration_sec, float(features[singer]["time_sec"].iloc[-1]))

    singers = sorted(features)
    couplings: list[float] = []
    for a, b in combinations(singers, 2):
        try:
            result = compute_pairwise_coupling(
                features[a], features[b], max_lag_sec=1.0, signal="rms"
            )
        except ValueError:
            # Insufficient overlap — skip this pair.
            continue
        couplings.append(result.peak_correlation)

    coupling_series = pd.Series(couplings, dtype="float64")
    return {
        "take_id": manifest.take_id,
        "piece": manifest.piece,
        "section": manifest.section,
        "take": manifest.take,
        "n_singers": len(singers),
        "n_pairs": len(couplings),
        "duration_sec": round(duration_sec, 2),
        "mean_coupling": round(float(coupling_series.mean()), 4) if len(coupling_series) else float("nan"),
        "max_coupling": round(float(coupling_series.max()), 4) if len(coupling_series) else float("nan"),
        "min_coupling": round(float(coupling_series.min()), 4) if len(coupling_series) else float("nan"),
        "singers_extracted": extracted,
        "singers_reused": reused,
    }


def run(limit: int | None, takes_only: bool) -> None:
    manifests = build_manifest(DAGSTUHL_AUDIO_DIR, takes_only=takes_only)
    if limit:
        manifests = manifests[:limit]

    print(f"Found {len(manifests)} multi-singer takes to process.")
    PROCESSED_ROOT.mkdir(parents=True, exist_ok=True)
    rows: list[dict[str, object]] = []
    total_start = time.perf_counter()

    for i, manifest in enumerate(manifests, 1):
        take_start = time.perf_counter()
        row = process_take(manifest)
        elapsed = time.perf_counter() - take_start
        rows.append(row)
        print(
            f"  [{i}/{len(manifests)}] {manifest.take_id}: "
            f"{row['n_singers']} singers, {row['n_pairs']} pairs, "
            f"mean coupling {row['mean_coupling']}, "
            f"{row['singers_extracted']} extracted / {row['singers_reused']} reused, "
            f"{elapsed:.1f}s"
        )

    summary = pd.DataFrame(rows).sort_values("take_id").reset_index(drop=True)
    summary.to_csv(SUMMARY_CSV, index=False)
    total_elapsed = time.perf_counter() - total_start
    print(
        f"\nWrote {SUMMARY_CSV} with {len(summary)} rows "
        f"(total runtime {total_elapsed/60:.1f} min)."
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--limit", type=int, default=None, help="Process only the first N takes (default: all)."
    )
    parser.add_argument(
        "--takes-only",
        action="store_true",
        help="Restrict to musical Take## (skip Tuning/Cadence/Humming/Scale exercises).",
    )
    args = parser.parse_args()
    run(limit=args.limit, takes_only=args.takes_only)


if __name__ == "__main__":
    main()
