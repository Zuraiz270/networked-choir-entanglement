"""Re-validate URLs previously marked 'url-unavailable' with the working yt-dlp
player-client args. Updates manifest rows in place.
"""

from __future__ import annotations

import csv
import json
import subprocess
import sys
from pathlib import Path

MANIFEST = Path("data/tier1_corpus_manifest.csv")
YT_DLP = r"C:\Users\zurai\AppData\Local\Programs\Python\Python311\Scripts\yt-dlp.exe"


def fetch(url: str) -> dict:
    result = subprocess.run(
        [
            YT_DLP, "--simulate", "--no-warnings",
            "--extractor-args", "youtube:player_client=web,android",
            "-j", url,
        ],
        capture_output=True, text=True, timeout=60,
    )
    if result.returncode != 0:
        return {"_error": result.stderr.strip()[:200]}
    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        return {"_error": f"JSON parse: {exc}"}


def main() -> int:
    with MANIFEST.open(encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fields = list(reader.fieldnames or [])
        rows = list(reader)

    n_revived = 0
    for row in rows:
        if row["download_sha256"] != "url-unavailable":
            continue
        print(f"Re-checking {row['video_id']}...", end=" ", flush=True)
        meta = fetch(row["url"])
        if "_error" in meta:
            print(f"still dead: {meta['_error'][:60]}")
            continue
        row["title"] = meta.get("title") or row["title"]
        row["channel"] = meta.get("uploader") or row["channel"]
        row["upload_date"] = meta.get("upload_date") or row["upload_date"]
        row["duration_s"] = str(meta.get("duration", "")) or row["duration_s"]
        row["license"] = meta.get("license") or "Standard YouTube License"
        row["download_sha256"] = "pending-sprint3"
        old_notes = row["notes"].split(" | yt-dlp failed:")[0].rstrip()
        row["notes"] = f"{old_notes} | revived 2026-05-19 via yt-dlp player_client=web,android workaround"
        n_revived += 1
        print(f"REVIVED ({row['duration_s']}s)")

    with MANIFEST.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

    print(f"\nRevived {n_revived} previously-dead URLs")
    return 0


if __name__ == "__main__":
    sys.exit(main())
