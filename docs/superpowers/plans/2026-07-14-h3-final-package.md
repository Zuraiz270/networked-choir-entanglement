# H3 Visual-Onset + Jul-23 Final Package Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Deliver the H3 first visual-onset experiment (18-video CSV + figure), the Jul-23 final presentation package, and the doc/bookkeeping updates, per `docs/superpowers/specs/2026-07-14-h3-final-presentation-design.md`.

**Architecture:** A new analysis script `scripts/h3_visual_onset.py` (pure functions + batch main, mirroring `scripts/tier3_latency_grid.py`) computes audio-visual onset coupling per Tier-1 video with a circular-shift null. The presentation package follows the repo's `*_deck.md` + `generate_*_pptx.py` pattern. Docs updated last, from verified artifacts.

**Tech Stack:** Python 3.11.9 (uv-managed), librosa 0.10.2, pandas, numpy, matplotlib, python-pptx (dev extra), imageio-ffmpeg (new, for MP4 audio decode; no system ffmpeg on this machine).

## Global Constraints

- Branch: `dev-hammad`. Atomic conventional commits. Never commit raw media (`data/` is gitignored; force-add only small derived CSVs/figures like the existing `_latency_grid.csv` precedent).
- Every number on deck/docs traceable to a repo CSV: `_latency_grid_2000.csv`, `_h2_centralization.csv`, `_h3_visual_onset.csv`, `_pose_summary.csv`.
- pytest green + ruff clean before every commit. Baseline suite: 39 passing.
- Audio constants come from `choir_entanglement.audio.pipeline`: `SAMPLE_RATE_HZ = 22050`, `HOP_LENGTH_SAMPLES = 512`.
- Null convention: circular shift, offset drawn `rng.integers(2, n-2)` (matches `entanglement._circular_shift_frame`), p = (1 + #{null ≥ obs}) / (1 + n_shuffles).
- Verified data facts (2026-07-14): 18 videos with `quality_pass=True` in `_pose_summary.csv`; pose parquets have ONE `singer_id` stream, ~8-10 Hz effective rate, covering the first 60-72 s only, NaN rate 3-15% in derived columns (`head_sway`, `trunk_lean`, `shoulder_rise`).

---

### Task 1: HPC bookkeeping commit

**Files:**
- Modify: `scripts/hpc/tier3_2000.sbatch`
- Add (force): `data/processed/tier3/_latency_grid_2000.csv`

**Interfaces:** Produces the committed 2000-shuffle grid all later tasks cite.

- [ ] **Step 1: Apply the five cluster-proven fixes to the local sbatch.** Final content of the `#SBATCH` block and run line (replacing the placeholder versions; keep surrounding comments intact, update the header comment that says placeholders must be filled to say the values are validated on NHR@FAU TinyGPU, job 1744899, 2026-07-14):

```bash
#SBATCH --job-name=tier3-2000
#SBATCH --partition=work          # NHR@FAU TinyGPU; adjust for other clusters
#SBATCH --gres=gpu:1              # TinyGPU mandates >=1 GPU per job (CPU-only work still needs it)
#SBATCH --cpus-per-task=1
#SBATCH --time=24:00:00
#SBATCH --output=scripts/hpc/logs/%x_%a.out
# NOTE: no --mem-per-cpu: TinyGPU forbids explicit memory on GPU jobs.

set -euo pipefail
export PATH="$HOME/.local/bin:$PATH"   # uv lives here; SLURM env is not the login env
mkdir -p scripts/hpc/logs data/processed/tier3/shards
```

and the run line becomes:

```bash
uv run --no-sync python -m scripts.tier3_latency_grid \
```

(`--no-sync` is load-bearing: concurrent `uv run` syncs stripped the venv extras mid-run on 2026-07-14 and killed 65 tasks with ModuleNotFoundError. Tasks must treat the venv as read-only; sync happens once on the login node via `uv sync --extra all`.)

- [ ] **Step 2: Verify tests still pass** (no code touched, sanity): `uv run pytest -q` → expect `39 passed`.
- [ ] **Step 3: Commit**

```bash
git add scripts/hpc/tier3_2000.sbatch
git add -f data/processed/tier3/_latency_grid_2000.csv
git commit -m "fix(hpc): TinyGPU-validated sbatch + 2000-shuffle latency grid

Five fixes proven on NHR@FAU job 1744899 (140/140 cells, 2026-07-14):
partition=work, --gres=gpu:1, no --mem-per-cpu, PATH export, uv run
--no-sync (venv-stripping race: concurrent uv run syncs uninstalled
extras mid-run). Headline drops unchanged vs 100-shuffle grid:
Dagstuhl 56.5% / ESMUC 65.1% / ChoralSynth 75.1% clean->zoom."
```

### Task 2: MP4 audio decode dependency

**Files:**
- Modify: `pyproject.toml` (wp1-audio extra), `uv.lock`

**Interfaces:** Produces `imageio_ffmpeg.get_ffmpeg_exe()` for Task 3's `_load_mp4_audio`.

- [ ] **Step 1:** `uv add --optional wp1-audio imageio-ffmpeg` then pin the resolved version exactly in `pyproject.toml` (repo convention: `==`).
- [ ] **Step 2:** `uv sync --extra all`
- [ ] **Step 3: Verify:** `uv run python -c "import imageio_ffmpeg; print(imageio_ffmpeg.get_ffmpeg_exe())"` → prints a real exe path.
- [ ] **Step 4: Commit:** `git add pyproject.toml uv.lock && git commit -m "build(deps): imageio-ffmpeg in wp1-audio for Tier-1 MP4 audio decode"`

### Task 3: H3 core functions (TDD)

**Files:**
- Create: `scripts/h3_visual_onset.py`
- Create: `tests/test_h3_visual_onset.py`

**Interfaces (produced, used by Task 4):**
- `visual_motion_signal(pose: pd.DataFrame, grid_hz: float = 10.0) -> tuple[np.ndarray, np.ndarray]` — (times, motion); nan-aware z-scored sum of |Δ| of the three derived columns, mean across `singer_id` groups, linearly interpolated onto a uniform grid spanning observed time.
- `audio_onset_envelope(y: np.ndarray, times_grid: np.ndarray) -> np.ndarray` — librosa onset strength resampled onto `times_grid`.
- `max_lag_correlation(audio_env, visual_env, grid_hz, max_lag_s=2.0) -> tuple[float, float]` — (r, lag_s); **positive lag = visual leads audio**; NaN-pairs dropped per lag; lags with <10 valid pairs skipped.
- `circular_null_p(audio_env, visual_env, grid_hz, max_lag_s=2.0, n_shuffles=1000, seed=0) -> float` — null r computed with the SAME max-over-lags procedure (avoids selection bias).
- `_load_mp4_audio(mp4: Path, max_seconds: float = 90.0) -> np.ndarray` — imageio-ffmpeg subprocess → temp mono 22050 Hz WAV → librosa.load.

- [ ] **Step 1: Write failing tests** in `tests/test_h3_visual_onset.py`:

```python
import numpy as np
import pandas as pd

from scripts.h3_visual_onset import (
    circular_null_p,
    max_lag_correlation,
    visual_motion_signal,
)


def _smooth_noise(n: int, seed: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    return np.convolve(rng.standard_normal(n), np.ones(5) / 5, mode="same")


def test_max_lag_correlation_recovers_visual_lead() -> None:
    a = _smooth_noise(600, 0)
    v = np.roll(a, -5)  # visual shows at t what audio does at t+0.5s -> visual leads
    r, lag = max_lag_correlation(a, v, grid_hz=10.0, max_lag_s=2.0)
    assert r > 0.95
    assert abs(lag - 0.5) < 1e-9


def test_max_lag_correlation_handles_nans() -> None:
    a = _smooth_noise(600, 1)
    v = a.copy()
    v[100:150] = np.nan
    r, _ = max_lag_correlation(a, v, grid_hz=10.0, max_lag_s=2.0)
    assert r > 0.95


def test_circular_null_p_coupled_vs_independent() -> None:
    a = _smooth_noise(600, 2)
    coupled = a + 0.1 * _smooth_noise(600, 3)
    independent = _smooth_noise(600, 4)
    assert circular_null_p(a, coupled, grid_hz=10.0, n_shuffles=200, seed=0) < 0.05
    assert circular_null_p(a, independent, grid_hz=10.0, n_shuffles=200, seed=0) > 0.05


def test_visual_motion_signal_grid_and_motion() -> None:
    t = np.arange(0, 60, 0.12)
    pose = pd.DataFrame({
        "time_sec": t,
        "singer_id": "P1",
        "head_sway": np.sin(t),
        "trunk_lean": np.cos(t),
        "shoulder_rise": np.zeros_like(t),
    })
    times, motion = visual_motion_signal(pose, grid_hz=10.0)
    assert np.allclose(np.diff(times), 0.1)
    assert np.nanstd(motion) > 0
```

- [ ] **Step 2:** `uv run pytest tests/test_h3_visual_onset.py -q` → FAIL (module missing).
- [ ] **Step 3: Implement** `scripts/h3_visual_onset.py` (module docstring cites the spec; functions per the interfaces above; core loops vectorized with numpy; `_zscore` guards zero std; module constants `GRID_HZ = 10.0`, `MAX_LAG_S = 2.0`, `N_SHUFFLES = 1000`, `AUDIO_WINDOW_S = 90.0`).
- [ ] **Step 4:** `uv run pytest tests/test_h3_visual_onset.py -q` → all pass; `uv run ruff check scripts/h3_visual_onset.py tests/test_h3_visual_onset.py` → clean.
- [ ] **Step 5: Commit:** `feat(h3): visual-onset coupling core (max-lag r, circular-shift null)`

### Task 4: H3 batch run, CSV, figure

**Files:**
- Modify: `scripts/h3_visual_onset.py` (add `main()`)
- Add (force): `data/processed/tier1/_h3_visual_onset.csv`, `data/figures/h3_visual_onset.png`

**Interfaces:** CSV columns `video_id, singer_count_est, pose_coverage, analysis_window_s, r_obs, best_lag_s, p_null, significant`. One row per quality-pass video (expected 18, asserted).

- [ ] **Step 1: Implement `main()`**: read `_pose_summary.csv`, filter `quality_pass == True`, assert 18; per video: load `data/processed/tier1/<id>/pose.parquet` + `data/raw/tier1/<id>/<id>.mp4` audio (first 90 s), clip both to the overlapping window, compute r/lag/p, collect row; write CSV; figure = observed r (dot) vs per-video null distribution (violin/box), significance marked, following the matplotlib style of `scripts/tier3_corpus_figure.py`.
- [ ] **Step 2: Run:** `uv run python -m scripts.h3_visual_onset` → CSV with 18 rows, no NaNs; runtime sanity-logged per video.
- [ ] **Step 3: Validate:** re-read CSV; assert 18 rows, all `video_id` in the quality-pass set, p in [0,1]. Record the headline (how many of 18 significant, median r, median lag sign) for Task 5.
- [ ] **Step 4:** full `uv run pytest -q` green, ruff clean.
- [ ] **Step 5: Commit:** `feat(h3): first visual-onset run on 18 Tier-1 videos (CSV + figure)` (force-add the two artifacts).

### Task 5: Jul-23 deck, script, Q&A markdown

**Files:**
- Create: `jul23_deck.md`, `jul23_script.md`, `jul23_qa_prep.md`

14 content slides + 1 backup, 20-minute budget, presenters Hammad (slides 1-5) and Zuraiz (6-14 + demo):

1. Title — Project 8 "Entanglement in Online Choir", final presentation, 2026-07-23, team.
2. Questions & hypotheses — H1/H2/H3 each with operational metric + predicted direction.
3. Data tiers — Tier 1 YouTube video (visual), Tier 2 multitrack (audio+network ground truth), Tier 3 latency injection; the signal-split reality.
4. Method — E(t) composite + onset synchrony; pipeline diagram (existing figure).
5. Latency regimes — clean/ept/jamulus_lan/jamulus_wan/zoom, injection approach + caveat (simulated, not live adaptation).
6. H1 headline — onset synchrony drop clean→Zoom: **56.5% Dagstuhl / 65.1% ESMUC / 75.1% ChoralSynth**, 28 pieces × 5 levels, **2000-shuffle null** (paper-grade rerun 2026-07-14); figure `tier3_latency_grid.png`.
7. H1 dissociation — attack timing collapses, loudness envelope robust; that dissociation is the finding.
8. H2 — leader dominance = out-degree Gini 0.154 vs matched-null 0.139; significant in human data only (Dagstuhl 3/5, ESMUC 2/3, ChoralSynth 2/20).
9. H3 — first visual-onset attempt on 18 Tier-1 videos, first-minute window: report Task 4's actual result (r, lags, k/18 significant) + honest status (ΔR² still data-blocked); figure `h3_visual_onset.png`.
10. Live demo — 60 s dashboard run; fallback slide right after with `wp4_dashboard_realdata.png`.
11. Limitations — simulated latency; signal split (no piece has A+V+N); per-cell null caveats; pose = single tracked stream, first minute only.
12. Contributions — E(t) domain transfer, latency signature, leadership structure, open pipeline.
13. Future work — real latency-varied live recordings; audio+video corpus for ΔR².
14. Thanks / questions.
Backup: reproducibility (`make reproduce`, HPC 2000-shuffle protocol).

- [ ] **Step 1:** Write `jul23_deck.md` with per-slide content + numbers, every number annotated with its source CSV in an HTML comment.
- [ ] **Step 2:** Write `jul23_script.md`, two voices, ≤19 min spoken (word budget ≈ 2400), demo choreography for slide 10.
- [ ] **Step 3:** Write `jul23_qa_prep.md`: carry forward still-true Jul-9 entries; rewrite H3 and reproducibility entries; add 2000-shuffle and venv-incident questions.
- [ ] **Step 4: Audit:** grep every numeric claim against its CSV. Commit: `feat(presentation): Jul-23 final deck, script, Q&A bank`

### Task 6: PPTX generator

**Files:**
- Create: `scripts/generate_jul23_pptx.py`
- Create: `output/jul23_final_presentation.pptx`

- [ ] **Step 1:** Implement generator following `scripts/generate_jul09_pptx.py` exactly (import shared helpers `_solid_bg, _text, _card, _stat_card, _takeaway, _picture_fit` and palette from `scripts.generate_jun11_pptx`; `TOTAL_SLIDES = 15`).
- [ ] **Step 2:** `uv run python scripts/generate_jul23_pptx.py` → writes pptx; open-check via `python-pptx` reload (slide count == 15).
- [ ] **Step 3:** ruff clean. Commit: `feat(presentation): Jul-23 PPTX generator + deck artifact`

### Task 7: Documentation sync

**Files:**
- Modify: `PROJECT_GUIDE.md` (§11 Claim 1 + Claim 3 status, milestone table), `TEAM_BRIEF.md` (status block)
- Modify: `onsidian vault/OSN-M/wiki/log.md` (one append-only entry)

- [ ] **Step 1:** PROJECT_GUIDE: Claim 1 gains "2000-shuffle paper-grade rerun 2026-07-14, drops unchanged"; Claim 3 status changes from "data-blocked, first attempt planned" to the actual Task-4 result (ΔR² claim remains data-blocked); milestone table: add Jul-14 HPC row + Jul-23 package row.
- [ ] **Step 2:** TEAM_BRIEF: final-phase status refresh (what exists, what remains: rehearsal + delivery).
- [ ] **Step 3:** Vault log entry `[2026-07-14] schema | 2000-shuffle rerun + H3 first visual-onset + Jul-23 package` covering: HPC run (140/140), the uv venv-stripping incident + `--no-sync` fix, H3 method + result, package files; obey log Rule 1/Rule 2 conventions visible in existing entries.
- [ ] **Step 4:** Commit: `docs(final): sync PROJECT_GUIDE, TEAM_BRIEF, vault log through Jul-14 state`

### Task 8: Final verification

- [ ] `uv run pytest -q` → all green (39 baseline + new H3 tests).
- [ ] `uv run ruff check .` → clean.
- [ ] Number audit: every figure/number cited in `jul23_deck.md` re-checked against its CSV (scripted grep + manual pass).
- [ ] `git log --oneline` shows the six atomic commits; working tree clean.
- [ ] Report summary to user: H3 result, package location, what remains manual (rehearsal, OneDrive if ever needed).

## Self-Review

- Spec coverage: Part 1 → Tasks 2-4; Part 2 → Tasks 5-6; Part 3 → Task 7; Part 4 → Tasks 1-7 commits; verification gates → Task 8. No gaps.
- Placeholders: none; all code/steps concrete. Deck prose is authored in Task 5 by design with per-slide content specified.
- Type consistency: function signatures consistent between Tasks 3 and 4; constants single-sourced in the module.
