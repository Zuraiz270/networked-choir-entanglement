"""Find candidate Zoom-only choir videos for Tier-1 corpus supplement.

Uses yt-dlp's ytsearch to query YouTube directly across multiple Zoom-related
queries, filters by duration and obvious disqualifiers (Jamulus/SoundJack
mentions in title), de-duplicates against the existing tier1_corpus_manifest,
and writes candidates to data/zoom_only_candidates.csv for user eyeball
selection.

Usage:
    python -m scripts.search_zoom_only_candidates
"""

from __future__ import annotations

import csv
import json
import subprocess
import sys
from pathlib import Path

EXISTING_MANIFEST = Path("data/tier1_corpus_manifest.csv")
OUTPUT_CSV = Path("data/zoom_only_candidates.csv")
YT_DLP = r"C:\Users\zurai\AppData\Local\Programs\Python\Python311\Scripts\yt-dlp.exe"

QUERIES = [
    "zoom choir rehearsal live",
    "zoom choir covid lockdown",
    "church choir zoom rehearsal",
    "virtual choir zoom singing",
    "online choir zoom call",
]
RESULTS_PER_QUERY = 25

MIN_DURATION_SEC = 120
MAX_DURATION_SEC = 1800

DISQUALIFIER_KEYWORDS = (
    "jamulus", "soundjack", "jacktrip",
    "acapella", "smule", "charadi",
    "official audio", "official video", "music video",
    "compilation", "best of",
)

OUTPUT_COLUMNS = [
    "video_id", "url", "title", "channel", "upload_date",
    "duration_s", "view_count", "search_query", "reason_kept",
]


def load_existing_ids() -> set[str]:
    """Read existing manifest, return set of video_ids we already have."""
    if not EXISTING_MANIFEST.exists():
        return set()
    with EXISTING_MANIFEST.open(encoding="utf-8") as f:
        return {row["video_id"] for row in csv.DictReader(f)}


def search(query: str, n_results: int) -> list[dict]:
    """Run yt-dlp ytsearch and return list of metadata dicts."""
    spec = f"ytsearch{n_results}:{query}"
    result = subprocess.run(
        [YT_DLP, "--simulate", "--no-warnings", "--flat-playlist", "-j", spec],
        capture_output=True, text=True, timeout=120,
    )
    if result.returncode != 0:
        print(f"  WARN: yt-dlp failed for query '{query}': {result.stderr.strip()[:200]}")
        return []
    rows = []
    for line in result.stdout.splitlines():
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return rows


def is_candidate(meta: dict, existing_ids: set[str]) -> tuple[bool, str]:
    """Return (keep, reason) for a candidate. Reason is keep-justification or rejection-reason."""
    video_id = meta.get("id", "")
    if not video_id:
        return False, "no video_id"
    if video_id in existing_ids:
        return False, "already in manifest"

    title = (meta.get("title") or "").lower()
    for kw in DISQUALIFIER_KEYWORDS:
        if kw in title:
            return False, f"title contains '{kw}'"

    duration = meta.get("duration")
    if duration is None:
        return False, "no duration"
    if not (MIN_DURATION_SEC <= duration <= MAX_DURATION_SEC):
        return False, f"duration {duration}s outside [{MIN_DURATION_SEC}, {MAX_DURATION_SEC}]"

    return True, f"title mentions zoom + choir, {duration}s duration"


def main() -> int:
    existing_ids = load_existing_ids()
    print(f"Loaded {len(existing_ids)} existing video_ids from manifest")

    seen: set[str] = set()
    candidates: list[dict] = []

    for query in QUERIES:
        print(f"\nSearching: {query!r}")
        results = search(query, RESULTS_PER_QUERY)
        print(f"  {len(results)} raw results")
        kept_this_query = 0
        for meta in results:
            video_id = meta.get("id", "")
            if video_id in seen:
                continue
            keep, reason = is_candidate(meta, existing_ids)
            if not keep:
                continue
            seen.add(video_id)
            candidates.append({
                "video_id": video_id,
                "url": meta.get("url") or f"https://youtu.be/{video_id}",
                "title": meta.get("title", ""),
                "channel": meta.get("channel") or meta.get("uploader") or "",
                "upload_date": meta.get("upload_date") or "",
                "duration_s": str(meta.get("duration") or ""),
                "view_count": str(meta.get("view_count") or ""),
                "search_query": query,
                "reason_kept": reason,
            })
            kept_this_query += 1
        print(f"  {kept_this_query} candidates kept (after de-dup + filters)")

    OUTPUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_CSV.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=OUTPUT_COLUMNS)
        writer.writeheader()
        writer.writerows(candidates)

    print(f"\nWrote {len(candidates)} candidates to {OUTPUT_CSV}")
    print("\nNext step: watch ~30 seconds of each candidate. Keep if audio is")
    print("audibly chaotic (real Zoom latency); reject if audio sounds clean")
    print("and on-beat (post-produced or not actually Zoom).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
