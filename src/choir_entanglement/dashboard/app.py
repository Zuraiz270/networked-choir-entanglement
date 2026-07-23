"""FastAPI backend for the WP4 dashboard (real data).

Serves the analysis outputs on disk:
- Dagstuhl pieces (audio + network): real E(t) timeline (computed on demand and
  cached) + real influence graph (read from the standard-Granger GEXF).
- Tier-1 videos (video + pose): real pose-keypoint stream for the overlay.

No single piece carries all signals (Dagstuhl is audio-only, Tier-1 is
video-only), so each endpoint serves what the piece actually has; missing
signals come back as null, which the frontend renders as gaps.

Run with:
    uv run uvicorn choir_entanglement.dashboard.app:app --reload --port 8000
"""

from __future__ import annotations

import math
from functools import lru_cache
from pathlib import Path
from typing import Any

import networkx as nx
import pandas as pd
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

from choir_entanglement.entanglement import compute_entanglement

DAGSTUHL_ROOT = Path("data/processed/dagstuhl")
TIER1_ROOT = Path("data/processed/tier1")
RAW_TIER1 = Path("data/raw/tier1")
NETWORK_METHOD = "standard"
STEP_SEC = 0.5

app = FastAPI(
    title="Choir Entanglement Dashboard",
    description="WP4 dashboard backend serving real analysis outputs.",
    version="0.2.0",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["GET"],
    allow_headers=["*"],
)


def _nan_to_none(values: list[float]) -> list[float | None]:
    return [
        None if (v is None or (isinstance(v, float) and math.isnan(v))) else round(float(v), 4)
        for v in values
    ]


def _dagstuhl_pieces() -> list[str]:
    if not DAGSTUHL_ROOT.exists():
        return []
    return sorted(
        d.name
        for d in DAGSTUHL_ROOT.iterdir()
        if d.is_dir() and (d / f"influence_graph_{NETWORK_METHOD}.gexf").exists()
    )


def _tier1_videos() -> list[str]:
    if not TIER1_ROOT.exists():
        return []
    return sorted(d.name for d in TIER1_ROOT.iterdir() if (d / "pose.parquet").exists())


@lru_cache(maxsize=1)
def _video_index() -> dict[str, dict[str, Any]]:
    """Build the video catalogue once from on-disk outputs."""
    index: dict[str, dict[str, Any]] = {}
    for piece in _dagstuhl_pieces():
        parquets = list((DAGSTUHL_ROOT / piece).glob("*.parquet"))
        index[piece] = {
            "video_id": piece,
            "title": f"Dagstuhl · {piece.replace('_', ' ')}",
            "regime": "Dagstuhl-Tier2 (audio+network)",
            "kind": "audio_network",
            "n_singers": len(parquets),
            "has_video": False,
        }
    for vid in _tier1_videos():
        index[vid] = {
            "video_id": vid,
            "title": f"Tier-1 video · {vid}",
            "regime": "Tier-1 (video+pose)",
            "kind": "video_pose",
            "n_singers": None,
            "has_video": (RAW_TIER1 / vid / f"{vid}.mp4").exists(),
        }
    return index


@app.get("/api/videos")
def list_videos() -> list[dict[str, Any]]:
    return list(_video_index().values())


@lru_cache(maxsize=64)
def _entanglement_cached(video_id: str) -> dict[str, Any]:
    take_dir = DAGSTUHL_ROOT / video_id
    audio = {p.stem: p for p in sorted(take_dir.glob("*.parquet"))}
    gexf = take_dir / f"influence_graph_{NETWORK_METHOD}.gexf"
    df = compute_entanglement(
        audio,
        gexf if gexf.exists() else None,
        video_parquet=None,
        window_sec=10.0,
        step_sec=STEP_SEC,
        # Match the envelope-only definition used by every published E(t) value.
        include_onsets=False,
    )
    return {
        "video_id": video_id,
        "window_sec": 10.0,
        "step_sec": STEP_SEC,
        "series": {
            "time_sec": _nan_to_none(df["time_sec"].tolist()),
            "A": _nan_to_none(df["A"].tolist()),
            "V": _nan_to_none(df["V"].tolist()),
            "N": _nan_to_none(df["N"].tolist()),
            "E": _nan_to_none(df["E"].tolist()),
        },
    }


@app.get("/api/entanglement/{video_id}")
def get_entanglement(video_id: str) -> dict[str, Any]:
    meta = _require_video(video_id)
    if meta["kind"] != "audio_network":
        raise HTTPException(status_code=404, detail=f"{video_id} has no audio E(t) (video-only)")
    return _entanglement_cached(video_id)


@app.get("/api/influence_graph/{video_id}")
def get_influence_graph(video_id: str) -> dict[str, Any]:
    meta = _require_video(video_id)
    gexf = DAGSTUHL_ROOT / video_id / f"influence_graph_{NETWORK_METHOD}.gexf"
    if meta["kind"] != "audio_network" or not gexf.exists():
        raise HTTPException(status_code=404, detail=f"{video_id} has no influence graph")
    g = nx.read_gexf(gexf)
    nodes = [{"id": n, "label": n, "section": str(n)[:1]} for n in g.nodes]
    edges = [
        {
            "source": u,
            "target": v,
            "weight": round(float(d.get("weight", 1.0)), 3),
            "lag": int(d.get("lag", 0)),
        }
        for u, v, d in g.edges(data=True)
    ]
    return {"video_id": video_id, "nodes": nodes, "edges": edges}


@app.get("/api/pose/{video_id}")
def get_pose(video_id: str, max_frames: int = 600) -> dict[str, Any]:
    meta = _require_video(video_id)
    parquet = TIER1_ROOT / video_id / "pose.parquet"
    if meta["kind"] != "video_pose" or not parquet.exists():
        raise HTTPException(status_code=404, detail=f"{video_id} has no pose data")
    df = pd.read_parquet(parquet)
    if len(df) > max_frames:
        df = df.iloc[:: max(1, len(df) // max_frames)].head(max_frames)
    keypoint_cols = [c for c in df.columns if c.startswith("pose_") and c.endswith(("_x", "_y"))]
    frames = [
        {
            "time_sec": round(float(r["time_sec"]), 3),
            "keypoints": {
                c: (None if pd.isna(r[c]) else round(float(r[c]), 4)) for c in keypoint_cols
            },
        }
        for _, r in df.iterrows()
    ]
    return {"video_id": video_id, "n_frames": len(frames), "frames": frames}


@app.get("/api/video/{video_id}")
def get_video_file(video_id: str) -> FileResponse:
    meta = _require_video(video_id)
    mp4 = RAW_TIER1 / video_id / f"{video_id}.mp4"
    if meta["kind"] != "video_pose" or not mp4.exists():
        raise HTTPException(status_code=404, detail=f"{video_id} has no mp4")
    return FileResponse(mp4, media_type="video/mp4")


def _require_video(video_id: str) -> dict[str, Any]:
    idx = _video_index()
    if video_id not in idx:
        raise HTTPException(status_code=404, detail=f"unknown video_id: {video_id}")
    return idx[video_id]
