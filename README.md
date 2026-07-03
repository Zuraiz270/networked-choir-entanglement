# choir-entanglement

Networked choir entanglement measurement platform for SNA-OSN-M Project 8
(Uni Bamberg x Uni Koeln x HSLU, Summer 2026).

**Status:** report-stage prototype. The audio, video, network, Tier-3 latency,
and dashboard-alpha paths are implemented; Status Meeting VI materials are in
`jul09_*` and `output/jul09_status_meeting_vi.pptx`. The current scientific
claim is H1 support in the onset-timing channel, partial H2 support in human
datasets, and H3 data-blocked because no corpus item has audio and video
together.

---

## Quickstart (target: < 15 minutes on a fresh Win 11 laptop)

### One-time host setup

```powershell
winget install astral-sh.uv ezwinports.make Gyan.FFmpeg
```

`uv` is the Python toolchain, `make` provides canonical entry points, and
`ffmpeg` is needed for audio I/O. On Linux: `apt install make ffmpeg libgl1
libglib2.0-0` and install `uv` per the official installation guide.

### Clone and run

```bash
git clone https://github.com/Zuraiz270/networked-choir-entanglement.git choir-entanglement
cd choir-entanglement
uv sync --frozen --all-extras
make smoke
```

### If you do not want `make` on Windows

Direct equivalents:

```bash
uv run --all-extras pytest tests/test_smoke.py -v
uv run --all-extras ruff format --check .
uv run --all-extras mypy src tests
uv run --all-extras pytest tests/ -v
```

---

## Repository Structure

```text
src/choir_entanglement/     # WP1 audio, WP2 video, WP3 network, WP4 dashboard
tests/                      # focused regression and smoke tests
data/raw/                   # source-data manifests and checksums
data/processed/             # committed report-stage summaries and selected outputs
data/figures/               # generated figures for decks and report
features/                   # parquet schema documentation
output/                     # rendered status-meeting decks
onsidian vault/             # LLM-maintained project wiki and research evidence
PROJECT_GUIDE.md            # technical source of truth
TEAM_BRIEF.md               # human-readable team status
Makefile                    # canonical entry points
pyproject.toml              # dependency truth
uv.lock                     # frozen resolution
```

## Make Targets

- `make sync` - install deps from lockfile.
- `make smoke` - run canary smoke tests.
- `make lint` / `make typecheck` / `make test` - quality gates.
- `make all` - run tests and rebuild report-stage artefacts.
- `make reproduce` - rebuild committed report figures and the Status VI deck.

## Dependency Groups

- `wp1-audio` - librosa, demucs, soundfile, ffmpeg-python
- `wp2-video` - mediapipe, opencv-python
- `wp3-network` - networkx, statsmodels, python-louvain, teneto, scikit-learn
- `wp4-dashboard` - fastapi, uvicorn
- `dev` - pytest, pytest-cov, ruff, mypy, pre-commit
- `all` - everything above

Example WP-focused install:

```bash
uv sync --frozen --extra wp1-audio --extra dev
```

## Reproducibility

This is an academic semester project, not a production deployment. Full raw
extraction depends on large gitignored media, but report-stage reproducibility
is handled by `uv.lock`, committed processed summaries, and `make reproduce`.

The current report-stage pass regenerates:

- H2 centralization table: `data/processed/tier3/_h2_centralization.csv`
- H1 corpus figure: `data/figures/tier3_corpus_summary.png`
- Status Meeting VI deck: `output/jul09_status_meeting_vi.pptx`

## Licence

MIT.

## Stakeholder-Facing Docs

- Team guide: `PROJECT_GUIDE.md`
- Current team status: `TEAM_BRIEF.md`
- Status VI deck source: `jul09_deck.md`
- Status VI speaker script: `jul09_script.md`
- Status VI Q&A prep: `jul09_qa_prep.md`
- Obsidian vault: `onsidian vault/OSN-M/wiki/`
