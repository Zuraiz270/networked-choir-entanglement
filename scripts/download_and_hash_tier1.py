"""Download every Tier-1 video that still has download_sha256=='pending-sprint3'
and write its SHA-256 hash back to the manifest.

Resumable: re-running skips any row whose download_sha256 already has a real
hex digest. mp4s land under data/raw/tier1/<video_id>/ and stay there until
WP2 pose extraction in Sprint 3.
"""

from __future__ import annotations

import csv
import hashlib
import subprocess
import sys
import time
from pathlib import Path

MANIFEST = Path("data/tier1_corpus_manifest.csv")
DOWNLOAD_ROOT = Path("data/raw/tier1")
YT_DLP = r"C:\Users\zurai\AppData\Local\Programs\Python\Python311\Scripts\yt-dlp.exe"

PENDING_TOKEN = "pending-sprint3"


def is_pending(row: dict) -> bool:
    val = row.get("download_sha256", "")
    return val == PENDING_TOKEN or val.strip() == ""


def is_hashed(row: dict) -> bool:
    val = row.get("download_sha256", "")
    return len(val) == 64 and all(c in "0123456789abcdef" for c in val)


def download_video(video_id: str, url: str) -> Path | None:
    """Returns Path to the downloaded mp4 or None on failure."""
    out_dir = DOWNLOAD_ROOT / video_id
    out_dir.mkdir(parents=True, exist_ok=True)
    output_template = str(out_dir / f"{video_id}.%(ext)s")
    result = subprocess.run(
        [
            YT_DLP,
            "-f", "worst[ext=mp4]/worst",
            "--continue",
            "--retries", "50",
            "--fragment-retries", "50",
            "--extractor-args", "youtube:player_client=web,android",
            "--no-warnings",
            "-o", output_template,
            url,
        ],
        capture_output=True, text=True, timeout=1800,
    )
    if result.returncode != 0:
        print(f"    yt-dlp failed: {result.stderr.strip().splitlines()[-1][:120]}")
        return None
    candidates = list(out_dir.glob(f"{video_id}.*"))
    return candidates[0] if candidates else None


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def write_manifest(rows: list[dict], fields: list[str]) -> None:
    with MANIFEST.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    with MANIFEST.open(encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fields = list(reader.fieldnames or [])
        rows = list(reader)

    pending = [r for r in rows if is_pending(r)]
    already = [r for r in rows if is_hashed(r)]
    print(f"Manifest: {len(rows)} rows | {len(pending)} pending | {len(already)} already hashed")
    print(f"Output root: {DOWNLOAD_ROOT.resolve()}\n")

    start = time.time()
    for i, row in enumerate(pending, 1):
        vid = row["video_id"]
        url = row["url"]
        print(f"[{i:2d}/{len(pending)}] {vid} ({row['title'][:50]})")
        path = download_video(vid, url)
        if path is None:
            print(f"    SKIP: download failed for {vid}")
            continue
        size_mb = path.stat().st_size / (1 << 20)
        digest = sha256_of(path)
        row["download_sha256"] = digest
        write_manifest(rows, fields)
        elapsed = time.time() - start
        print(f"    OK   {size_mb:.1f} MB  sha256={digest[:16]}...  ({elapsed:.0f}s elapsed total)")

    final_hashed = sum(1 for r in rows if is_hashed(r))
    final_pending = sum(1 for r in rows if is_pending(r))
    print(f"\nDone. {final_hashed} hashed, {final_pending} still pending.")
    return 0 if final_pending == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
