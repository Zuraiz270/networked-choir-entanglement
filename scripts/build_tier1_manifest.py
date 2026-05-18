"""Build Tier-1 corpus manifest from the Perplexity-curated CSV.

Reads data/nmp_choir_corpus_strict.csv, validates each URL with yt-dlp
(metadata-only fetch), and produces data/tier1_corpus_manifest.csv in the
schema that matches Prof. Hacker's Tier-0 list.

SHA-256 column is left as ``pending-sprint3``. Hashing requires the actual
binary, which Sprint 3 downloads, hashes, and deletes per the data sourcing
policy (§1).
"""

from __future__ import annotations

import csv
import datetime as dt
import json
import subprocess
import sys
from pathlib import Path

INPUT_CSV = Path("data/nmp_choir_corpus_strict.csv")
OUTPUT_CSV = Path("data/tier1_corpus_manifest.csv")
YT_DLP = r"C:\Users\zurai\AppData\Local\Programs\Python\Python311\Scripts\yt-dlp.exe"

LATENCY_LABEL = {
    "Jamulus": "NMP-Jamulus",
    "SoundJack": "NMP-SoundJack",
    "Jamulus+Zoom": "NMP-Jamulus+Zoom",
    "Zoom": "Zoom-only",
}

HACKER_SEED_IDS = {"isIV1XsKCgQ", "YiUJM6f8YpQ", "zp1qLCckgLk", "m811fZiPyaQ"}

OUTPUT_COLUMNS = [
    "video_id",
    "url",
    "title",
    "channel",
    "upload_date",
    "duration_s",
    "license",
    "singer_count_est",
    "latency_regime_label",
    "satb_confirmed",
    "download_sha256",
    "ingest_date",
    "notes",
    "tier",
]


def fetch_metadata(url: str) -> dict:
    """Run yt-dlp --simulate -j to get YouTube metadata as JSON."""
    result = subprocess.run(
        [YT_DLP, "--simulate", "--no-warnings", "-j", url],
        capture_output=True,
        text=True,
        timeout=60,
    )
    if result.returncode != 0:
        return {"_error": result.stderr.strip() or "unknown yt-dlp error"}
    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        return {"_error": f"JSON parse: {exc}"}


def build_row(perplexity_row: dict, metadata: dict, ingest_date: str) -> dict:
    """Map (Perplexity row + yt-dlp metadata) to Hacker-schema manifest row."""
    video_id = perplexity_row["video_id"]
    is_seed = video_id in HACKER_SEED_IDS
    notes_parts = []
    if is_seed:
        notes_parts.append("Hacker Tier-0 seed (re-confirmed)")
    notes_parts.append(perplexity_row["why_not_post_produced"])

    if "_error" in metadata:
        return {
            "video_id": video_id,
            "url": perplexity_row["url"],
            "title": perplexity_row["title"],
            "channel": perplexity_row["channel"],
            "upload_date": perplexity_row["upload_date"],
            "duration_s": perplexity_row["duration_s"],
            "license": "UNAVAILABLE",
            "singer_count_est": perplexity_row["singer_count_est"],
            "latency_regime_label": LATENCY_LABEL.get(
                perplexity_row["nmp_system"], perplexity_row["nmp_system"]
            ),
            "satb_confirmed": "unknown",
            "download_sha256": "url-unavailable",
            "ingest_date": ingest_date,
            "notes": f"yt-dlp failed: {metadata['_error']}",
            "tier": "Tier-0" if is_seed else "Tier-1",
        }

    return {
        "video_id": video_id,
        "url": perplexity_row["url"],
        "title": metadata.get("title") or perplexity_row["title"],
        "channel": metadata.get("uploader") or perplexity_row["channel"],
        "upload_date": metadata.get("upload_date") or perplexity_row["upload_date"],
        "duration_s": str(metadata.get("duration") or perplexity_row["duration_s"]),
        "license": metadata.get("license") or "Standard YouTube License",
        "singer_count_est": perplexity_row["singer_count_est"],
        "latency_regime_label": LATENCY_LABEL.get(
            perplexity_row["nmp_system"], perplexity_row["nmp_system"]
        ),
        "satb_confirmed": "unknown",
        "download_sha256": "pending-sprint3",
        "ingest_date": ingest_date,
        "notes": " | ".join(notes_parts),
        "tier": "Tier-0" if is_seed else "Tier-1",
    }


def main() -> int:
    if not INPUT_CSV.exists():
        print(f"ERROR: input CSV not found at {INPUT_CSV}", file=sys.stderr)
        return 1

    today = dt.date.today().isoformat()
    rows_out: list[dict] = []

    with INPUT_CSV.open(encoding="utf-8") as f:
        perplexity_rows = list(csv.DictReader(f))

    print(f"Validating {len(perplexity_rows)} URLs via yt-dlp...")
    for i, row in enumerate(perplexity_rows, 1):
        url = row["url"]
        print(f"  [{i:2d}/{len(perplexity_rows)}] {row['video_id']}", end=" ", flush=True)
        meta = fetch_metadata(url)
        out_row = build_row(row, meta, today)
        rows_out.append(out_row)
        status = "FAIL" if "yt-dlp failed" in out_row["notes"] else "ok"
        print(f"{status:4s}  license={out_row['license']:25.25s}  dur={out_row['duration_s']}s")

    OUTPUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_CSV.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=OUTPUT_COLUMNS)
        writer.writeheader()
        writer.writerows(rows_out)

    n_ok = sum(1 for r in rows_out if "yt-dlp failed" not in r["notes"])
    print(f"\nWrote {len(rows_out)} rows to {OUTPUT_CSV} ({n_ok} validated, {len(rows_out) - n_ok} failed)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
