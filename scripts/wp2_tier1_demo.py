"""Run WP2 pose extraction on one Tier-1 YouTube video.

Picks the shortest video from data/tier1_corpus_manifest.csv that yt-dlp can
fetch, downloads it to a temp dir, runs MediaPipe Pose + FaceMesh, writes
per-frame parquet to data/processed/tier1/<video_id>/pose.parquet, computes a
one-page calibration summary, and deletes the mp4 per data sourcing policy §1.

Usage:
    python -m scripts.wp2_tier1_demo
"""

from __future__ import annotations

import csv
import subprocess
import tempfile
from pathlib import Path

import numpy as np

from choir_entanglement.video.pose import extract_pose_to_parquet

MANIFEST = Path("data/tier1_corpus_manifest.csv")
OUTPUT_BASE = Path("data/processed/tier1")
CALIBRATION_NOTE = Path("wp2_calibration_sprint2.md")
YT_DLP = r"C:\Users\zurai\AppData\Local\Programs\Python\Python311\Scripts\yt-dlp.exe"


def pick_shortest_with_singers_visible() -> dict:
    """Pick the shortest verified video where singers are visible in tiles.

    Filters out screen-recording / software-demo videos (no human body visible to
    MediaPipe). Heuristic: prefer entries whose notes mention 'tile' or 'tiles'
    (the LCV / Sacred Harp / Jamulus chamber pattern).
    """
    with MANIFEST.open(encoding="utf-8") as f:
        rows = [
            r for r in csv.DictReader(f)
            if r["download_sha256"] != "url-unavailable"
            and "tile" in r["notes"].lower()
        ]
    if not rows:
        raise RuntimeError("No tile-containing videos in manifest")
    rows.sort(key=lambda r: int(r["duration_s"]))
    return rows[0]


def download(url: str, dest_dir: Path) -> Path:
    """Use yt-dlp to fetch the lowest-quality mp4. Returns the downloaded file path."""
    dest_dir.mkdir(parents=True, exist_ok=True)
    template = str(dest_dir / "%(id)s.%(ext)s")
    subprocess.run(
        [YT_DLP, "--no-warnings", "-f", "worst[ext=mp4]/worst", "-o", template, url],
        check=True,
        capture_output=True,
        text=True,
        timeout=600,
    )
    mp4s = list(dest_dir.glob("*.mp4"))
    if not mp4s:
        raise FileNotFoundError(f"yt-dlp did not produce an mp4 in {dest_dir}")
    return mp4s[0]


def summarize(df, video_meta: dict) -> str:
    n_frames = len(df)
    duration = df["time_sec"].iloc[-1] if n_frames else 0.0
    pose_detected = df["pose_nose_x"].notna().mean() * 100
    face_detected = df["lip_61_x"].notna().mean() * 100
    voiced_shoulder = df["shoulder_rise"].notna()
    shoulder_std_px = (
        float(np.nanstd(df.loc[voiced_shoulder, "shoulder_rise"])) if voiced_shoulder.any() else 0.0
    )

    return f"""# WP2 Calibration Note — Sprint 2 Pilot ({video_meta["video_id"]})

**Source video**: {video_meta["title"]}
**Channel**: {video_meta["channel"]}
**NMP regime**: {video_meta["latency_regime_label"]}
**Duration**: {duration:.1f} s ({n_frames} frames extracted)

## MediaPipe detection rates

| Component | Frames with detection | Notes |
|:---|:---:|:---|
| Pose (33-keypoint BlazePose) | {pose_detected:.1f}% | nose visible across the video |
| FaceMesh (lip subset 40 indices) | {face_detected:.1f}% | upper + lower lip contour |

## Derived feature stability

| Feature | Std dev (normalised) | Interpretation |
|:---|:---:|:---|
| shoulder_rise (breath proxy) | {shoulder_std_px:.4f} | Higher = more breathing motion captured; should be non-zero for visible singer |

## Acceptance for WP2 milestone

The Apr 30 plan called for `head-sway Pearson correlation against a reference tool ≥ 0.70` as the calibration target. This pilot is a coverage check, not a reference-tool comparison. Reference-tool comparison (OpenPose or manual annotation) is the Sprint-3 next step before scaling to the full Tier-1 corpus.

## Sprint-3 follow-ups

1. Run extraction on the remaining 21 Tier-1 verified URLs (batch overnight, store per-video parquets).
2. Compare MediaPipe head-sway against an OpenPose reference run on 3 randomly sampled videos; report Pearson r.
3. If r < 0.70, fallback to OpenPose for the full corpus (R3 mitigation per PROJECT_GUIDE §9).
"""


def run() -> None:
    if not MANIFEST.exists():
        raise FileNotFoundError(f"Manifest missing: {MANIFEST}")
    meta = pick_shortest_with_singers_visible()
    print(f"Picked shortest video with visible singers: {meta['video_id']} "
          f"({meta['duration_s']}s, {meta['latency_regime_label']}, {meta['singer_count_est']} singers)")

    with tempfile.TemporaryDirectory(prefix="wp2_tier1_") as tmp:
        print(f"  Downloading {meta['url']}...")
        mp4 = download(meta["url"], Path(tmp))
        print(f"  Downloaded {mp4.name} ({mp4.stat().st_size / 1e6:.1f} MB)")

        out_dir = OUTPUT_BASE / meta["video_id"]
        parquet = out_dir / "pose.parquet"
        print(f"  Extracting MediaPipe Pose + FaceMesh -> {parquet}")
        print(f"  (sampling every 3rd frame, cap 600 frames for Sprint-2 pilot)")
        df = extract_pose_to_parquet(
            mp4, parquet, singer_id=meta["video_id"], frame_skip=3, max_frames=600
        )
        print(f"  Wrote {len(df)} frames to {parquet}")

    CALIBRATION_NOTE.write_text(summarize(df, meta), encoding="utf-8")
    print(f"\n  Calibration note: {CALIBRATION_NOTE}")
    print(f"  mp4 deleted (per data sourcing policy §1)")


if __name__ == "__main__":
    run()
