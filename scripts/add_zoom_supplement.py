"""Validate Perplexity-supplied Zoom-only candidates and merge into Tier-1 manifest.

Reads candidate URLs from the Perplexity CSV passed inline, validates each via
yt-dlp metadata-only fetch (same flow as build_tier1_manifest.py), maps to
Hacker schema, and appends to data/tier1_corpus_manifest.csv. Dedupes by
video_id.
"""

from __future__ import annotations

import csv
import datetime as dt
import json
import subprocess
import sys
from pathlib import Path

MANIFEST = Path("data/tier1_corpus_manifest.csv")
YT_DLP = r"C:\Users\zurai\AppData\Local\Programs\Python\Python311\Scripts\yt-dlp.exe"

CANDIDATES = [
    {
        "video_id": "VsnvueTan4I",
        "url": "https://www.youtube.com/watch?v=VsnvueTan4I",
        "nmp_system": "Zoom",
        "singer_count_est": "30",
        "perplexity_note": "First virtual rehearsal of Roanoke Valley Children's Choir on Zoom, Apr 2020. Raw Zoom audio with uneven entrances.",
    },
    {
        "video_id": "KJruTaWTWlY",
        "url": "https://www.youtube.com/watch?v=KJruTaWTWlY",
        "nmp_system": "Zoom",
        "singer_count_est": "25",
        "perplexity_note": "Roanoke choir warm-up demo over native Zoom; latency-aware loose alignment, no DAW mix. BORDERLINE (workshop framing in title).",
    },
    {
        "video_id": "s3ZVr6ki2vw",
        "url": "https://www.youtube.com/watch?v=s3ZVr6ki2vw",
        "nmp_system": "Zoom",
        "singer_count_est": "35",
        "perplexity_note": "Rick McCollum church choir, week 2 Zoom rehearsal, May 2020. 45 min raw capture with talkover, dropouts. OVER 30-MIN LIMIT.",
    },
    {
        "video_id": "DLdFR7m1thI",
        "url": "https://www.youtube.com/watch?v=DLdFR7m1thI",
        "nmp_system": "Zoom",
        "singer_count_est": "35",
        "perplexity_note": "Rick McCollum church choir, week 4 Zoom rehearsal, May 2020. 50 min with sectional run-throughs, mute issues. OVER 30-MIN LIMIT.",
    },
    {
        "video_id": "q1rLPIsIPZI",
        "url": "https://www.youtube.com/watch?v=q1rLPIsIPZI",
        "nmp_system": "Zoom",
        "singer_count_est": "35",
        "perplexity_note": "Rick McCollum church choir, week 6 Zoom rehearsal, Jun 2020. 29 min with live accompaniment and mute issues.",
    },
]

LATENCY_LABEL = {"Zoom": "Zoom-only"}


def fetch_metadata(url: str) -> dict:
    result = subprocess.run(
        [
            YT_DLP, "--simulate", "--no-warnings",
            "--extractor-args", "youtube:player_client=web,android",
            "-j", url,
        ],
        capture_output=True, text=True, timeout=60,
    )
    if result.returncode != 0:
        return {"_error": result.stderr.strip()[:200] or "unknown yt-dlp error"}
    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        return {"_error": f"JSON parse: {exc}"}


def load_existing() -> tuple[list[dict], list[str], set[str]]:
    with MANIFEST.open(encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = list(reader.fieldnames or [])
        rows = list(reader)
    ids = {r["video_id"] for r in rows}
    return rows, fieldnames, ids


def build_row(c: dict, meta: dict, fieldnames: list[str], ingest_date: str) -> dict:
    is_dead = "_error" in meta
    row = {col: "" for col in fieldnames}
    row["video_id"] = c["video_id"]
    row["url"] = c["url"]
    row["title"] = (meta.get("title") if not is_dead else "UNAVAILABLE")
    row["channel"] = (meta.get("uploader") if not is_dead else "")
    row["upload_date"] = (meta.get("upload_date") if not is_dead else "")
    row["duration_s"] = str(meta.get("duration", "")) if not is_dead else ""
    row["license"] = (meta.get("license") or "Standard YouTube License") if not is_dead else "UNAVAILABLE"
    row["singer_count_est"] = c["singer_count_est"]
    row["latency_regime_label"] = LATENCY_LABEL[c["nmp_system"]]
    row["satb_confirmed"] = "unknown"
    row["download_sha256"] = "url-unavailable" if is_dead else "pending-sprint3"
    row["ingest_date"] = ingest_date
    notes = f"Zoom-stratum supplement (Sprint-2 patch): {c['perplexity_note']}"
    if is_dead:
        notes += f" | yt-dlp failed: {meta['_error']}"
    row["notes"] = notes
    row["tier"] = "Tier-1"
    return row


def main() -> int:
    if not MANIFEST.exists():
        print(f"ERROR: manifest missing at {MANIFEST}", file=sys.stderr)
        return 1
    rows, fieldnames, existing_ids = load_existing()
    today = dt.date.today().isoformat()

    print(f"Existing manifest: {len(rows)} rows")
    new_rows = []
    for c in CANDIDATES:
        vid = c["video_id"]
        if vid in existing_ids:
            print(f"  [{vid}] SKIP: already in manifest")
            continue
        print(f"  [{vid}] validating...", end=" ", flush=True)
        meta = fetch_metadata(c["url"])
        out = build_row(c, meta, fieldnames, today)
        new_rows.append(out)
        status = "DEAD" if "_error" in meta else "ok"
        print(f"{status:4s} dur={out['duration_s']}s license={out['license']:25.25s}")

    rows.extend(new_rows)
    with MANIFEST.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    n_dead = sum(1 for r in new_rows if r["license"] == "UNAVAILABLE")
    print(f"\nAppended {len(new_rows)} rows ({len(new_rows) - n_dead} validated, {n_dead} dead) to {MANIFEST}")
    print(f"Manifest now contains {len(rows)} total rows")
    return 0


if __name__ == "__main__":
    sys.exit(main())
