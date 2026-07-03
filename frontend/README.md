# Frontend - Choir Entanglement Dashboard

WP4 dashboard deliverable. See `wireframe.md` for the original Sprint-2 design
doc.

**Status (2026-07-09):** dashboard alpha. The React frontend and FastAPI
backend are implemented, and the backend serves real analysis outputs:

- Dagstuhl pieces: real E(t) timeline and real Granger influence graph.
- Tier-1 videos: real MediaPipe pose parquet and video playback route.
- Metadata: signal availability per piece.

No current corpus item has all three native signals together. The final demo
should therefore use an honest two-piece path: one audio/network piece and one
video/pose piece.

## Stack

- React 18.3
- Vite 5.3
- TypeScript 5.5
- D3 7.9
- Plotly 2.33
- Tailwind CSS 3.4
- FastAPI 0.111 + uvicorn 0.30 backend in `src/choir_entanglement/dashboard/`

## Run

Backend:

```bash
uv run uvicorn choir_entanglement.dashboard.app:app --reload --port 8000
```

Frontend:

```bash
cd frontend
npm install
npm run dev
```

Open the Vite URL, normally `http://localhost:5173`.

## Acceptance for Jul 23

The presentation laptop can run the backend and frontend, switch between one
audio/network example and one video/pose example, and complete a rehearsed
60-second demo without crashing. Keep `data/figures/wp4_dashboard_realdata.png`
as the screenshot fallback.
