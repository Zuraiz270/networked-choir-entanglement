# choir-entanglement

Networked choir entanglement measurement platform for SNA-OSN-M Project 8
(Uni Bamberg x Uni Koeln x HSLU, Summer 2026).

**Status:** final seminar package complete. H1 is supported in the onset-timing
channel: all 28 pieces decrease from clean to Zoom (paired sign-test p =
3.73e-9). H2 has limited human-only evidence after final-grid correction (2 of
8 human pieces, 0 of 20 synthetic pieces). The exploratory H3 coupling is null
(1 of 17 significant); the full visual incremental-value claim still requires
paired per-singer audio and video.

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
output/                     # rendered decks and final report PDF
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
- `make all` - run tests and rebuild final report artifacts.
- `make reproduce` - rebuild final statistics, the H1 figure, and the report PDF.
- `make ieee-report` - build the separate IEEE-style two-column report PDF.

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

The final report-stage pass regenerates:

- H1 paired summary: `data/processed/tier3/_h1_paired_test.csv`
- H2 centralization table: `data/processed/tier3/_h2_centralization.csv`
- H1 corpus figure: `data/figures/tier3_corpus_summary.png`
- Final report: `output/pdf/networked_choir_final_report.pdf`

An editable IEEE-style Word counterpart is available at
`output/docx/networked_choir_final_report_ieee.docx`. Regenerate it from the
same Markdown source with `python -m scripts.render_report_ieee_docx` in an
environment that provides `python-docx`.

The optional IEEE-style export is generated from the same report source with
`make ieee-report` and written to
`output/pdf/networked_choir_final_report_ieee.pdf`. It is a course-delivery
alternative, not a claim of IEEE Xplore compliance; an IEEE submission would
still require the target conference template and PDF eXpress validation.

The live dashboard needs the gitignored media and feature parquets on the
presentation laptop. The committed screenshot is the portable fallback; full
raw extraction is outside `make reproduce`.

## Licence

MIT.

## Stakeholder-Facing Docs

- Team guide: `PROJECT_GUIDE.md`
- Current team status: `TEAM_BRIEF.md`
- Final report source: `report_final.md`
- Jul-23 deck source: `jul23_deck.md`
- Jul-23 speaker script and Q&A: `jul23_script.md`, `jul23_qa_prep.md`
- Obsidian vault: `onsidian vault/OSN-M/wiki/`
