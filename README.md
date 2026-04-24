# choir-entanglement

Networked choir entanglement measurement platform for SNA-OSN-M Project 8
(Uni Bamberg × Uni Köln × HSLU, Summer 2026).

**Status:** scaffold only. No feature code yet; see `PROJECT_GUIDE.md` §6 for the roadmap and §11 for the technical reference.

---

## Quickstart (target: < 15 minutes on a fresh Win 11 laptop)

### Prerequisites

- **Docker Desktop** ≥ 4.30 (Win 11 or Linux)
- **git** (any recent version)

That is the entire prerequisite list for reproducibility. No Python install required on the host.

### Clone and run

```bash
git clone https://github.com/Zuraiz270/networked-choir-entanglement.git choir-entanglement
cd choir-entanglement
docker build -t choir-entanglement:dev .   # ~8 min cold cache, ~30 s warm
docker run --rm choir-entanglement:dev     # runs `make smoke`; expect 3 passing tests
```

Total elapsed time on a fresh clone with warm Docker layer cache: **under 10 minutes**. Cold cache: **under 15 minutes**.

### Local Python development (optional, not required for reproducibility)

If you want to iterate on code without rebuilding the Docker image each time:

1. Install `uv`: <https://docs.astral.sh/uv/getting-started/installation/> (one command).
2. Install `make`: Win 11 → `winget install ezwinports.make`. Linux → `apt install make`.
3. `uv sync --frozen --all-extras` (installs the full stack into `.venv/`).
4. `make smoke` to verify (or `uv run --all-extras pytest tests/test_smoke.py -v` without make).

---

## Repository structure

```text
src/choir_entanglement/     # package (WP1 audio, WP2 video, WP3 network, WP4 dashboard)
tests/                      # canary smoke tests
raw/                        # immutable source data (git-tracked metadata only)
processed/                  # Albedo: stems, pose, breath — runtime artefacts (gitignored)
features/                   # Citrinitas: parquet feature tables (gitignored)
results/                    # Rubedo: E(t) tables, graphs, figures (gitignored)
onsidian vault/             # LLM-maintained project wiki (Obsidian)
PROJECT_GUIDE.md            # team-facing master document (v1.1)
Dockerfile                  # multi-stage, python:3.11.9-slim-bookworm
Makefile                    # canonical entry points
pyproject.toml              # dependency truth (WP-scoped optional deps)
uv.lock                     # frozen resolution (Win+Linux, Python 3.11)
.github/workflows/ci.yml    # lint + typecheck + test + docker-build on ubuntu-22.04
```

## Make targets

- `make sync` — install deps from lockfile (all groups + dev).
- `make smoke` — three canary tests (< 90 s).
- `make lint` / `make typecheck` / `make test` — quality gates.
- `make docker-build` / `make docker-smoke` — container round-trip.
- `make all` — full pipeline (stub today; lands with WP1).
- `make reproduce` — rebuild results from committed features (stub today).

## Dependency groups

Installed on demand per work package. Useful when iterating on one WP without pulling the whole 160+ package stack:

- `wp1-audio` — librosa, demucs, soundfile, ffmpeg-python
- `wp2-video` — mediapipe, opencv-python (py-feat deferred, see PROJECT_GUIDE §12 L-H-9)
- `wp3-network` — networkx, statsmodels, python-louvain, teneto, scikit-learn
- `wp4-dashboard` — fastapi, uvicorn
- `dev` — pytest, pytest-cov, ruff, mypy, pre-commit
- `all` — everything above

Example WP-focused install:

```bash
uv sync --frozen --extra wp1-audio --extra dev
```

## Licence

MIT.

## Stakeholder-facing docs

- Team guide: `PROJECT_GUIDE.md` (read sections 1–10 first; §11 is technical reference).
- Obsidian vault (research evidence): `onsidian vault/OSN-M/wiki/`.
- Deep-read audit (source provenance): `onsidian vault/OSN-M/wiki/00_overview/deep_read_audit.md`.
