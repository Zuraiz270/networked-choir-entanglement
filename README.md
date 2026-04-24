# choir-entanglement

Networked choir entanglement measurement platform for SNA-OSN-M Project 8
(Uni Bamberg × Uni Köln × HSLU, Summer 2026).

**Status:** scaffold only. No feature code yet; see `PROJECT_GUIDE.md` §6 for the roadmap and §11 for the technical reference.

---

## Quickstart (target: < 15 minutes on a fresh Win 11 laptop)

### One-time host setup

```powershell
winget install astral-sh.uv ezwinports.make Gyan.FFmpeg
```

(`uv` for the Python toolchain, `make` for the canonical entry points, `ffmpeg` for librosa audio I/O.) On Linux: `apt install make ffmpeg libgl1 libglib2.0-0` and install `uv` per the [official installation guide](https://docs.astral.sh/uv/getting-started/installation/).

### Clone and run

```bash
git clone https://github.com/Zuraiz270/networked-choir-entanglement.git choir-entanglement
cd choir-entanglement
uv sync --frozen --all-extras   # ~8 min cold cache, ~30 s warm
make smoke                      # 3 canary tests, ~8 s warm
```

Total elapsed time on a fresh clone (warm uv cache): **under 5 minutes**. Cold cache: **under 12 minutes**.

### If you do not want `make` on Windows

Direct equivalents:

```bash
uv run --all-extras pytest tests/test_smoke.py -v       # = make smoke
uv run --all-extras ruff format --check .               # = make lint (check)
uv run --all-extras mypy src tests                      # = make typecheck
uv run --all-extras pytest tests/ -v                    # = make test
```

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
Makefile                    # canonical entry points
pyproject.toml              # dependency truth (WP-scoped optional deps)
uv.lock                     # frozen resolution (Win+Linux, Python 3.11)
.github/workflows/ci.yml    # lint + typecheck + test on ubuntu-22.04
```

## Make targets

- `make sync` — install deps from lockfile (all groups + dev).
- `make smoke` — three canary tests (< 90 s warm).
- `make lint` / `make typecheck` / `make test` — quality gates.
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

## Reproducibility

This is an academic semester project, not a production deployment. Reproducibility is handled by `uv.lock` (which pins every Python wheel exactly across Win 11 and Linux x86_64) plus the documented host prerequisites (`uv`, `make`, `ffmpeg`). No container required. The same `uv sync --frozen` command runs on your laptop and on CI; if it works in one place it works in the other.

## Licence

MIT.

## Stakeholder-facing docs

- Team guide: `PROJECT_GUIDE.md` (read sections 1–10 first; §11 is technical reference).
- Obsidian vault (research evidence): `onsidian vault/OSN-M/wiki/`.
- Deep-read audit (source provenance): `onsidian vault/OSN-M/wiki/00_overview/deep_read_audit.md`.
