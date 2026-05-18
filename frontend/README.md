# Frontend — Choir Entanglement Dashboard

WP4 deliverable. See [wireframe.md](wireframe.md) for the Sprint-2 design doc.

**Status (2026-05-17)**: design doc + ASCII wireframe shipped. React + Vite scaffold lands Sprint 3.

**Stack** (pinned per PROJECT_GUIDE §11.8):
- React 18.3
- Vite 5.3
- TypeScript 5.5
- D3 7.9
- Plotly 2.33
- Tailwind CSS (latest stable)
- Playwright (E2E)

**Backend**: FastAPI 0.111 + uvicorn 0.30 in `src/choir_entanglement/dashboard/`.

## Layout

See [wireframe.md](wireframe.md).

## Run (Sprint 3+)

```bash
# Backend
uv run uvicorn choir_entanglement.dashboard.app:app --reload --port 8000

# Frontend
cd frontend && npm install && npm run dev
```

## Acceptance for Jul 23

60-second live demo runs without crashing during the final presentation.
