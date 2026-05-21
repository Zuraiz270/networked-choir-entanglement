"""Scale WP2 MediaPipe pose extraction across 10 Tier-1 videos.

Picks 10 videos from ``data/tier1_corpus_manifest.csv`` stratified by NMP regime
(4 Jamulus, 3 Zoom-only, 2 SoundJack, 1 Jamulus+Zoom). Reads each mp4 from
``data/raw/tier1/{video_id}/{video_id}.mp4`` (Sprint-2 hashing run downloaded
all 29; no re-download). Runs ``extract_pose_to_parquet`` with frame_skip=3
and max_frames=600 (~ first 60s of source @ 30fps; ~ 1 min runtime per video).
Resumable: any existing ``pose.parquet`` is reused and re-summarised, not
re-extracted.

Per-video quality summary written to ``data/processed/tier1/_pose_summary.csv``
with detection rates + derived-feature stability and a quality flag for the
H1 regime-discrimination test downstream.

Usage:
    python -m scripts.wp2_tier1_batch
"""

from __future__ import annotations

import csv
import time
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from choir_entanglement.video.pose import extract_pose_to_parquet

MANIFEST = Path("data/tier1_corpus_manifest.csv")
RAW_ROOT = Path("data/raw/tier1")
PROCESSED_ROOT = Path("data/processed/tier1")
SUMMARY_CSV = PROCESSED_ROOT / "_pose_summary.csv"
FIGURE_OUT = Path("data/figures/wp2_visual_features_v2.png")

# Stratified pick: 4 Jamulus / 3 Zoom-only / 2 SoundJack / 1 Jamulus+Zoom = 10
# Picked deterministically (shortest videos per regime — frame_skip=3 +
# max_frames=600 caps each at ~60s of source content anyway).
# ouFyQKszE_Y is the Sprint-2 SoundJack pilot; its parquet will be reused.
SELECTED_VIDEOS: list[str] = [
    # NMP-Jamulus (4)
    "VlOB9_-08pw",  # 141s, 20 singers
    "ZDZ98tl2wAQ",  # 144s, 60 singers
    "ZKthfLPWBCQ",  # 208s, 6 singers
    "w0ywMP8mOc4",  # 278s, 24 singers
    # NMP-Jamulus+Zoom (1)
    "bT6B5hjk34M",  # 210s, 20 singers
    # NMP-SoundJack (2)
    "NCXnQAMq0pY",  # 45s, 16 singers
    "ouFyQKszE_Y",  # 71s, 12 singers (Sprint-2 pilot)
    # Zoom-only (3)
    "Z-cH7j5iB3k",  # 45s, 15 singers
    "VsnvueTan4I",  # 255s, 30 singers
    "m0B7eYw7oEk",  # 497s, 20 singers
]

FRAME_SKIP = 3
MAX_FRAMES = 600
DETECTION_THRESHOLD = 0.50  # rough sanity floor for H1 inclusion


def load_manifest_lookup() -> dict[str, dict[str, str]]:
    with MANIFEST.open(encoding="utf-8") as f:
        return {r["video_id"]: r for r in csv.DictReader(f)}


def process_video(video_id: str, meta: dict[str, str]) -> dict[str, object]:
    mp4 = RAW_ROOT / video_id / f"{video_id}.mp4"
    if not mp4.exists():
        raise FileNotFoundError(f"missing mp4 for {video_id} at {mp4}")
    parquet = PROCESSED_ROOT / video_id / "pose.parquet"
    if parquet.exists():
        df = pd.read_parquet(parquet)
        reused = True
    else:
        df = extract_pose_to_parquet(
            mp4, parquet, singer_id=video_id, frame_skip=FRAME_SKIP, max_frames=MAX_FRAMES
        )
        reused = False
    return summarise(video_id, meta, df, reused)


def summarise(
    video_id: str, meta: dict[str, str], df: pd.DataFrame, reused: bool
) -> dict[str, object]:
    n_frames = len(df)
    pose_detection = float(df["pose_nose_x"].notna().mean()) if n_frames else 0.0
    face_detection = float(df["lip_61_x"].notna().mean()) if n_frames else 0.0
    shoulder_std = (
        float(np.nanstd(df["shoulder_rise"])) if df["shoulder_rise"].notna().any() else 0.0
    )
    head_sway_std = (
        float(np.nanstd(df["head_sway"])) if df["head_sway"].notna().any() else 0.0
    )
    quality_pass = pose_detection >= DETECTION_THRESHOLD
    return {
        "video_id": video_id,
        "regime": meta["latency_regime_label"],
        "duration_s": int(meta["duration_s"]),
        "singer_count_est": int(meta["singer_count_est"]),
        "n_frames_processed": n_frames,
        "pose_detection_rate": round(pose_detection, 4),
        "face_detection_rate": round(face_detection, 4),
        "shoulder_rise_std": round(shoulder_std, 6),
        "head_sway_std": round(head_sway_std, 6),
        "quality_pass": quality_pass,
        "reused_parquet": reused,
    }


def render_v2_figure(summary: pd.DataFrame, lookup: dict[str, dict[str, str]]) -> Path:
    """Render V(t) features for the highest pose-detection video in the batch."""
    best_id = summary.loc[summary["pose_detection_rate"].idxmax(), "video_id"]
    meta = lookup[best_id]
    parquet = PROCESSED_ROOT / best_id / "pose.parquet"
    df = pd.read_parquet(parquet)
    voiced = df["pose_nose_x"].notna()

    fig, axes = plt.subplots(3, 1, figsize=(11, 7), sharex=True)
    axes[0].plot(df["time_sec"], df["head_sway"], color="#1f77b4", linewidth=0.9)
    axes[0].set_ylabel("Head sway\n(nose vs shoulder midpoint)")
    axes[0].grid(True, alpha=0.3)
    axes[0].set_title(
        f"WP2 visual features v2 · Tier-1 {meta['latency_regime_label']} "
        f"({best_id}, {meta['singer_count_est']} singers)\n"
        f"Best pose detection in 10-video batch: {voiced.mean()*100:.1f}% of {len(df)} frames"
    )
    axes[1].plot(df["time_sec"], df["shoulder_rise"], color="#2ca02c", linewidth=0.9)
    axes[1].set_ylabel("Shoulder rise\n(breath proxy)")
    axes[1].grid(True, alpha=0.3)
    axes[2].plot(df["time_sec"], df["trunk_lean"], color="#d62728", linewidth=0.9)
    axes[2].set_ylabel("Trunk lean\n(rad)")
    axes[2].set_xlabel("Time (s)")
    axes[2].grid(True, alpha=0.3)

    fig.tight_layout()
    FIGURE_OUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(FIGURE_OUT, dpi=150, bbox_inches="tight")
    plt.close(fig)
    return FIGURE_OUT


def run() -> None:
    lookup = load_manifest_lookup()
    PROCESSED_ROOT.mkdir(parents=True, exist_ok=True)
    rows: list[dict[str, object]] = []
    total_start = time.perf_counter()

    for i, video_id in enumerate(SELECTED_VIDEOS, 1):
        meta = lookup.get(video_id)
        if meta is None:
            raise KeyError(f"video_id not in manifest: {video_id}")
        start = time.perf_counter()
        row = process_video(video_id, meta)
        elapsed = time.perf_counter() - start
        rows.append(row)
        flag = "PASS" if row["quality_pass"] else "FAIL"
        source = "reused" if row["reused_parquet"] else "extracted"
        print(
            f"  [{i:2d}/{len(SELECTED_VIDEOS)}] {video_id:14s} "
            f"({row['regime']:18s}) "
            f"{row['n_frames_processed']:>4d} frames, "
            f"pose {row['pose_detection_rate']:.1%}, "
            f"face {row['face_detection_rate']:.1%}, "
            f"shoulder_std={row['shoulder_rise_std']:.4f} "
            f"[{flag}, {source}, {elapsed:.1f}s]"
        )

    summary = pd.DataFrame(rows).sort_values(["regime", "video_id"]).reset_index(drop=True)
    summary.to_csv(SUMMARY_CSV, index=False)
    n_pass = int(summary["quality_pass"].sum())
    print(
        f"\nWrote {SUMMARY_CSV} with {len(summary)} rows "
        f"({n_pass}/{len(summary)} passed detection threshold {DETECTION_THRESHOLD:.0%}). "
        f"Total extraction {(time.perf_counter() - total_start)/60:.1f} min."
    )
    figure_path = render_v2_figure(summary, lookup)
    print(f"Wrote V(t) figure for best-detection video: {figure_path}")


if __name__ == "__main__":
    run()
