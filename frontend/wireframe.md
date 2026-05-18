# WP4 Dashboard — Sprint 2 Wireframe

**Purpose**: Take one video ID, load its WP1+WP2+WP3 outputs, scrub through E(t) timeline with pose + network overlays. 60-second live demo on July 23.

**Stack** (per PROJECT_GUIDE.md §11.8 and TEAM_BRIEF §4.4):
- Frontend: React 18.3 + Vite 5.3 + TypeScript 5.5 + D3 7.9 + Plotly 2.33 + Tailwind CSS
- Backend: FastAPI 0.111 + uvicorn 0.30
- E2E tests: Playwright

## ASCII Layout

```
+-----------------------------------------------------------------------+
| Choir Entanglement Dashboard            [Video: NCXnQAMq0pY ▾] [↻]    |
+-----------------------------------------------------------------------+
|                                                                       |
|  +-----------------------------+   +------------------------------+   |
|  |                             |   |                              |   |
|  |     VIDEO PLAYBACK          |   |   INFLUENCE GRAPH (D3)       |   |
|  |     (with pose overlay)     |   |   (Hacker flagship)          |   |
|  |                             |   |                              |   |
|  |   - 33-keypoint skeleton    |   |   Animated edges weighted    |   |
|  |     overlaid per singer     |   |   by Granger F-statistic     |   |
|  |   - playback controls       |   |   over sliding 10-s window   |   |
|  |                             |   |                              |   |
|  +-----------------------------+   +------------------------------+   |
|                                                                       |
|  +-----------------------------------------------------------------+  |
|  |              E(t) TIMELINE (Plotly)                             |  |
|  |              ─── A(t) audio coupling                            |  |
|  |              ─── V(t) visual coupling                           |  |
|  |              ─── N(t) network coherence                         |  |
|  |              ─── E(t) = (A+V+N) / 3                             |  |
|  |  [|>]  [0:00 ▬▬▬●▬▬▬▬▬▬▬▬▬▬ 1:11]                                |  |
|  +-----------------------------------------------------------------+  |
|                                                                       |
|  +-----------------------------------------------------------------+  |
|  | METADATA                       | METRICS (current 10-s window)  |  |
|  | NMP regime: SoundJack          | E(t):  0.72                    |  |
|  | Singers:    12                 | A(t):  0.81                    |  |
|  | Duration:   71 s               | V(t):  0.65                    |  |
|  | Provenance: Tier-1, SHA-256 ✓  | N(t):  0.70                    |  |
|  +-----------------------------------------------------------------+  |
+-----------------------------------------------------------------------+
```

## Components

### 1. Video player + pose overlay (top left)
- HTML5 `<video>` element with playback controls
- D3 SVG overlay synced to video currentTime
- Reads pose keypoints from `/api/pose/{video_id}` (FastAPI streams parquet rows)
- Renders 33-keypoint skeleton per detected singer, color-coded by tile region

### 2. Influence graph (top right)
- D3 force-directed layout, nodes = singers, edges = Granger arrows
- Edge thickness ∝ Granger F-statistic
- Sliding 10-s window: graph re-renders as user scrubs the timeline
- Reads from `/api/influence_graph/{video_id}?t_start=X&t_end=Y`

### 3. E(t) timeline (middle)
- Plotly multi-trace line chart
- Four series: A(t), V(t), N(t), E(t) composite
- Click-to-seek behaviour syncs the video player
- Reads from `/api/entanglement/{video_id}` returning JSON time-series

### 4. Metadata + metrics panel (bottom)
- Static metadata from manifest
- Live-updating metrics (current 10-s window averages)
- Tier-1 SHA-256 provenance shown explicitly for reproducibility audit

## Backend API (FastAPI)

```
GET /api/videos                          → list available video_ids
GET /api/metadata/{video_id}             → manifest row + processing status
GET /api/pose/{video_id}                 → streaming parquet rows
GET /api/audio/{video_id}                → per-singer F0 + onset + RMS
GET /api/entanglement/{video_id}         → E(t) + A(t) + V(t) + N(t)
GET /api/influence_graph/{video_id}      → directed graph (nodes + edges)
                                            ?t_start=X&t_end=Y
```

## Sprint-3 next steps

1. FastAPI backend skeleton with the 6 endpoints above; mock data first, real data via parquet readers second.
2. React + Vite frontend scaffold; render the static layout above.
3. D3 pose overlay synced to one video as a vertical slice.
4. Playwright E2E test: load page, play video, scrub to 30 s, assert timeline metrics update.
5. Visual style anchored to the paper-figure pipeline (`data/figures/wp1_satb_coupling.png`, `wp2_visual_features.png`, `wp3_influence_graph.png`) — same color palette, same fonts.

## Acceptance for Jul 23

User opens the URL, clicks Play, the dashboard plays the chosen video for 60 seconds without crashing, with all three overlays (pose skeleton, influence graph animating, E(t) timeline scrubbing) live and synced.
