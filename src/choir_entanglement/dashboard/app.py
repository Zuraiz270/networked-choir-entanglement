"""FastAPI mock backend for the WP4 dashboard scaffold.

Sprint-3 Phase D scaffold: serves three endpoints with mock data shaped like
the real API contract documented in ``frontend/wireframe.md``. Real parquet-
backed implementations land in the WP4 sub-plan (Jun-21 dashboard alpha).

Run with:
    uv run uvicorn choir_entanglement.dashboard.app:app --reload --port 8000
"""

from __future__ import annotations

import math
from typing import Any

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Choir Entanglement Dashboard (mock)",
    description="Sprint-3 Phase D scaffold; mock data only.",
    version="0.1.0-mock",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

_MOCK_VIDEOS: list[dict[str, Any]] = [
    {
        "video_id": "LI_QuartetA_Take02",
        "title": "Dagstuhl ChoirSet · Locus Iste · Quartet A · Take 02",
        "regime": "Dagstuhl-Tier2",
        "n_singers": 4,
        "duration_s": 143,
    },
    {
        "video_id": "ZKthfLPWBCQ",
        "title": "Tier-1 NMP-Jamulus rehearsal (best pose detection)",
        "regime": "NMP-Jamulus",
        "n_singers": 6,
        "duration_s": 208,
    },
    {
        "video_id": "ouFyQKszE_Y",
        "title": "Tier-1 NMP-SoundJack rehearsal (Sprint-2 pilot)",
        "regime": "NMP-SoundJack",
        "n_singers": 12,
        "duration_s": 71,
    },
]


@app.get("/api/videos")
def list_videos() -> list[dict[str, Any]]:
    return _MOCK_VIDEOS


@app.get("/api/entanglement/{video_id}")
def get_entanglement(video_id: str) -> dict[str, Any]:
    meta = _require_video(video_id)
    duration = int(meta["duration_s"])
    step = 1.0
    times = [round(t * step, 2) for t in range(int(duration / step))]
    return {
        "video_id": video_id,
        "window_sec": 10.0,
        "step_sec": step,
        "series": {
            "time_sec": times,
            "A": [round(0.55 + 0.15 * math.sin(0.4 * t), 4) for t in times],
            "V": [round(0.40 + 0.20 * math.sin(0.3 * t + 1.2), 4) for t in times],
            "N": [round(0.62 + 0.05 * math.cos(0.2 * t), 4) for t in times],
            "E": [
                round((0.55 + 0.15 * math.sin(0.4 * t)
                       + 0.40 + 0.20 * math.sin(0.3 * t + 1.2)
                       + 0.62 + 0.05 * math.cos(0.2 * t)) / 3, 4)
                for t in times
            ],
        },
    }


@app.get("/api/influence_graph/{video_id}")
def get_influence_graph(video_id: str) -> dict[str, Any]:
    meta = _require_video(video_id)
    n = int(meta["n_singers"])
    nodes = [
        {"id": f"singer_{i}", "label": f"S{i+1}", "section": _section(i, n)}
        for i in range(n)
    ]
    edges = [
        {
            "source": f"singer_{i}",
            "target": f"singer_{j}",
            "weight": round(2.0 + 1.5 * ((i + j) % 3), 3),
            "lag": (i + j) % 4 + 1,
        }
        for i in range(n)
        for j in range(n)
        if i != j and (i + j) % 2 == 0
    ]
    return {"video_id": video_id, "nodes": nodes, "edges": edges}


def _require_video(video_id: str) -> dict[str, Any]:
    for v in _MOCK_VIDEOS:
        if v["video_id"] == video_id:
            return v
    raise HTTPException(status_code=404, detail=f"unknown video_id: {video_id}")


def _section(i: int, n: int) -> str:
    sections = ["S", "A", "T", "B"]
    return sections[i % len(sections)] + str((i // len(sections)) + 1)
