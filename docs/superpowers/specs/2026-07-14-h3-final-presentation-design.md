# Design: H3 First V(t) Attempt + Jul-23 Final Presentation Package

**Date**: 2026-07-14 · **Author**: Zuraiz (via Claude Code) · **Branch**: dev-hammad
**Deadline**: final presentation 2026-07-23 (20 min + 60 s live dashboard demo); final paper 2026-07-31.

## Goal

Deliver the "full final package" for Project 8:

1. The H3 first visual-onset experiment on the 18 pose-usable Tier-1 videos (the analysis promised in the Jun-25 deck, PROJECT_GUIDE §11 Claim 3, and report_draft_v1 "Next").
2. The Jul-23 final presentation package (deck, speaker script, Q&A bank, generated PPTX).
3. Documentation updates: PROJECT_GUIDE.md, TEAM_BRIEF.md, vault log.
4. Repo bookkeeping from the 2026-07-14 HPC run (sbatch fixes, 2000-shuffle grid).

Out of scope: completing the final report (due Jul 31, separate task; only its H1 numbers
source changes to `_latency_grid_2000.csv`), dashboard feature work, H3 ΔR² test
(remains data-blocked; this design does not change that claim).

## Decisions already made (user-confirmed)

- Scope: full final package (H3 + presentation + docs). Hammad receives the two data
  zips via OneDrive and verifies independently.
- Professors confirmed a **live dashboard demo** on Jul 23.
- H1 numbers: **2000-shuffle grid** (`data/processed/tier3/_latency_grid_2000.csv`,
  produced and validated 2026-07-14; headline drops identical to prior grid:
  Dagstuhl 56.5%, ESMUC 65.1%, ChoralSynth 75.1% clean→Zoom).
- Presenters: **Zuraiz + Hammad** (Zuraiz: results + demo; Hammad: intro + methods).
- H3 framing stays honest: "data-blocked for ΔR², first visual-onset analysis delivered."
  Result reported whichever way it lands; a null result is a valid contribution.

## Part 1 — H3 experiment: `scripts/h3_visual_onset.py`

**Question**: do visual onsets (anticipatory trunk-sway movements) co-occur with
ensemble audio onsets on real choir videos?

**Per video** (18 pose-usable Tier-1 IDs):
- Usable set derived from `data/processed/tier1/_pose_summary.csv` (pose-detection
  floor per the May-22 milestone), NOT hardcoded. Expected n=18; assert and fail loudly
  if the data disagrees.
- **Audio channel**: onset-strength envelope from the MP4 audio track, using the
  `SAMPLE_RATE_HZ` / `HOP_LENGTH_SAMPLES` conventions from `audio/pipeline.py`.
- **Visual channel**: per-singer trunk-sway velocity from `pose.parquet`
  (schema per `video/schema.py`, verified at implementation), aggregated across
  detected singers into one ensemble visual-onset signal.
- **Coupling**: resample both to a common rate; Pearson r at the best lag inside an
  anticipatory window (visual may lead audio; window ±2 s, exact value justified from
  breath-gesture literature already cited in the vault, else stated as a
  pragmatic choice).
- **Null**: circular-shift of the visual signal, 1000 shuffles, per video
  (the project's established null model). p = fraction of null r ≥ observed.

**Outputs**:
- `data/processed/tier1/_h3_visual_onset.csv` — 18 rows:
  `video_id, n_singers, pose_coverage, r_obs, best_lag_s, p_null, significant`.
- `data/figures/h3_visual_onset.png` — one figure: per-video observed r vs null
  distribution, significance marked.
- Unit tests (synthetic signals: coupled pair → high r / low p; independent pair →
  p ≈ uniform), added to the pytest suite.

## Part 2 — Jul-23 presentation package

Follows the established repo pattern (`*_deck.md` + `*_script.md` + `*_qa_prep.md` +
`scripts/generate_*_pptx.py` → `output/*.pptx`):

- `jul23_deck.md`: ~14–16 slides for 20 minutes. Narrative: project question →
  data-tier story → E(t) method → H1 headline (2000-shuffle numbers) → H2
  (Gini 0.154 vs null 0.139, human-only) → H3 first visual-onset result →
  60 s live demo segment (with `wp4_dashboard_realdata.png` fallback slide) →
  limitations (honest: simulated latency, signal split, per-cell null caveats) →
  contributions + future work.
- `jul23_script.md`: two-voice script (Hammad: slides 1–6, Zuraiz: results + demo +
  close), timed to ≤ 19 min spoken.
- `jul23_qa_prep.md`: updated Q&A bank; carries forward the Jul-9 entries that remain
  true, updates H3 and reproducibility entries.
- `scripts/generate_jul23_pptx.py` → `output/jul23_final_presentation.pptx`.

**Audit rule**: every number on every slide traceable to a CSV in the repo
(`_latency_grid_2000.csv`, `_h2_centralization.csv`, `_h3_visual_onset.csv`,
`_pose_summary.csv`). Same convention as the audited Jul-9 deck.

## Part 3 — Documentation updates

- `PROJECT_GUIDE.md`: §11 Claim 3 status updated with the H3 first-attempt result;
  H1 claim annotated with the 2000-shuffle rerun; milestone table gains the Jul-14
  HPC row and Jul-23 package row.
- `TEAM_BRIEF.md`: final-phase status refresh.
- `onsidian vault/OSN-M/wiki/log.md`: one append-only entry (schema-compliant)
  covering: the 2000-shuffle HPC run incl. the uv venv-stripping incident and its
  `--no-sync` fix, the H3 experiment and result, the Jul-23 package.
- Docs are written only AFTER the artifacts exist; they describe verified reality.

## Part 4 — Commits (atomic, conventional, on dev-hammad)

1. `fix(hpc)`: cluster-validated sbatch (partition `work`, `--gres=gpu:1`, no
   `--mem-per-cpu`, PATH export, `uv run --no-sync`) — five fixes proven on job
   1744899. `data(tier3)`: force-add `_latency_grid_2000.csv`.
2. `feat(h3)`: experiment script + CSV + figure + tests.
3. `feat(presentation)`: jul23 deck/script/qa + generator + pptx.
4. `docs(final)`: PROJECT_GUIDE / TEAM_BRIEF / vault log.

## Verification gates

- pytest suite green (39/39 baseline + new H3 tests) before each commit.
- H3 CSV: exactly 18 rows, no NaNs, every video_id in the pose-usable set.
- Deck numbers cross-checked against source CSVs before the pptx is generated.
- `ruff` clean on new/changed Python.

## Risks

- MP4 audio decode on Windows needs ffmpeg via librosa/audioread; verify before
  writing the pipeline, fall back to extracting WAV via imageio-ffmpeg if needed.
- Pose parquets may have gaps (low-coverage frames); handle NaN stretches explicitly
  (interpolate short gaps, mask long ones, coverage reported per video).
- If the H3 result is null across all 18 videos, the deck slide reports that as a
  negative result with the measurement-validity check shown (per the 2026-06-22 lesson).
