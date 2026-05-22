# Team Brief — Project 8

**SNA-OSN-M Summer 2026 · Uni Bamberg · Last updated 2026-05-22**

> Read this once before doing anything else on the project. About 20 minutes. After this, your role section in §4 is the page you re-read each iteration.

---

## 1. The 30-second pitch

We are measuring something millions of people felt during COVID but nobody has put a number on: how well a virtual choir is actually coordinating when they cannot be in the same room. We call our number the **Entanglement Index, E(t)**. We test it on three kinds of data, write a paper, build a small dashboard, and present on July 23. Two supervisors — Prof. Janine Hacker (primary, Uni Bamberg) and Prof. Peter Gloor (second grader, Uni Köln) — each get a flagship figure that speaks their research language.

Project deadline: **2026-07-23 final presentation**, **2026-07-31 final paper**.

---

## 2. What we are building, in plain English

### 2.1 The problem

When choirs sang over Zoom during COVID, every singer felt the difference between "this feels like the same room" and "this is fighting the network." There is no number that captures that difference. NMP (Networked Music Performance) tool makers (Jamulus, SoundJack, JackTrip) design by intuition. Music educators plan remote programs by anecdote. Researchers cannot compare one setup to another.

We are building that number.

Why choirs and not, say, meetings? Because in a choir, coordination is acoustically measurable. Two singers either hit the same note at the same moment, or they did not. The recording shows it in milliseconds. That makes choirs the *Drosophila* of coordination science: clean, high-signal, available on YouTube at scale.

### 2.2 The binary we are testing

**Either** latency is a hard ceiling on coordination (in which case NMP tools need fundamentally new architectures) **or** human bodies compensate through visual cues like sway and breath (in which case Pentland's Honest Signals theory gets its cleanest external test). Both findings are publishable; we just need to honestly report which one we find.

### 2.3 What we deliver

1. A Python package called `choir_entanglement` that takes a choir video and outputs a coordination score timeline. Already scaffolded; runs on Win 11 in under 12 minutes from a fresh clone.
2. An 8-12 page paper in IEEE/LNCS format. Zuraiz first author.
3. A 20-minute presentation on July 23 with a 60-second live dashboard demo.
4. **Two flagship figures**:
   - **For Prof. Hacker**: a directed influence graph showing who-leads-whom in a choir, with arrows weighted by Granger-causality strength. This is Hassan's primary deliverable.
   - **For Prof. Gloor**: an alchemical-stage diagram showing how raw video becomes refined meaning across four stages (Nigredo to Albedo to Citrinitas to Rubedo). This is Kumaran's primary deliverable.

### 2.4 The metric (a one-line summary)

E(t) = (1/3) audio coupling + (1/3) visual coupling + (1/3) network coherence.

We are upfront with supervisors that the formula was originally validated on email patterns over 7-day windows; our application to choir audio is novel. H1 (regime discrimination), H2 (network topology), H3 (visual contribution) are the first empirical tests on music. This honesty is a feature of the project, not a weakness.

---

## 3. Where we are today (2026-05-21)

| Track                                                          | Status                                                                 |
| :------------------------------------------------------------- | :--------------------------------------------------------------------- |
| **Evidence layer** (vault, audit, citations)             | Done. 27 sources deep-read against original PDFs. Audit log committed. |
| **Repo scaffold** (pyproject, lockfile, CI, smoke tests) | Done.`make smoke` runs in 8 seconds warm. uv-only, no Docker.        |
| **Documentation**                                        | PROJECT_GUIDE.md v1.1 is the spec. This file is the team brief.        |
| **Tier 0 data** (Hacker's 5 Jamulus URLs)                | Received.                                                              |
| **Tier 1 data** (YouTube curated, 20-30 videos)          | **Done 2026-05-19.** 29 verified + downloaded + SHA-256 hashed URLs in Hacker schema (4 Hacker seeds re-confirmed + 25 new). Stratification: 11 Jamulus, 5 Jamulus+Zoom, 4 SoundJack, 9 Zoom-only. 1.3 GB of mp4s under `data/raw/tier1/` (gitignored), held for Sprint-3 WP2 pose extraction. Manifest with hashes at `data/tier1_corpus_manifest.csv`. |
| **Tier 2 data** (Dagstuhl + ESMUC + ChoralSynth)         | **Dagstuhl on disk 2026-05-17** (5.1 GB, MD5 `82b95faa…` verified vs Zenodo). ESMUC + ChoralSynth deferred. |
| **Feature code** (audio, video, network, dashboard)      | **All 4 WPs shipped Sprint-2 milestones.** WP1: SATB A(t) coupling on Dagstuhl. WP2: MediaPipe pose extraction on a Tier-1 SoundJack video (79.5% detection). WP3: Granger influence graph (11/12 SATB edges significant). WP4: dashboard wireframe + alchemical diagram drafted. **Sprint-3 Phase A (2026-05-22):** WP1 scaled to all 25 Dagstuhl musical takes (LI + TP), 130 newly-extracted singer parquets + 288 pairwise A(t) couplings; corpus summary at `data/processed/dagstuhl/_summary.csv`. **Sprint-3 Phase B (2026-05-22):** WP3 scaled to 5 pieces × 2 methods (standard Granger + COP-GC, Zanin 2021 P-22); per-piece GEXFs + network metrics at `data/processed/dagstuhl/_network_metrics.csv`; 2x3 grid figure at `data/figures/wp3_influence_graphs_5pieces.png`. 18/18 tests. **Sprint-3 Phase C (2026-05-22):** WP2 pose extraction batched across 10 Tier-1 videos stratified by NMP regime; 5/10 pass the 50% detection floor (consistent with the Status-Meeting-III "try and iterate" decision); summary at `data/processed/tier1/_pose_summary.csv`; v2 V(t) figure at `data/figures/wp2_visual_features_v2.png` (ZKthfLPWBCQ, 98.5% detection). **Sprint-3 Phase D (2026-05-22):** WP4 dashboard scaffold (React 18.3 + Vite 5.3 + TypeScript strict + D3 7.9 + Plotly 2.33 + FastAPI 0.111) — 4-panel layout fetches mock JSON from FastAPI and renders end-to-end; screenshot at `data/figures/wp4_dashboard_scaffold.png`. E(t) integration module at `src/choir_entanglement/entanglement.py` with circular-shift null at the composite level; LI_QuartetA_Take02 demo: mean E = 0.744, null mean 0.573 ± 0.008, p_null = 0.0000; figure at `data/figures/et_timeline_LI_QA_Take02.png`. 23/23 tests. **Sprint-3 Phase E (2026-05-22):** E(t) run on all 5 WP3 Dagstuhl pieces with 200-shuffle null. All 5 beat null at p < 0.001; piece-level clustering LI 0.74-0.80 vs TP 0.57-0.68. Corpus table at `data/processed/dagstuhl/_et_corpus.csv`; cross-piece scatter at `data/figures/et_corpus_comparison.png`; Sprint-3 narrative + four honest limitations at `sprint3_results.md` (deck source material). |
| **Virtual Mirror** (SC Chat Analyzer on team WhatsApp) | **Done 2026-05-18.** 5 participants. Archetype: Tree Hugger consensus across all 4 humans. Chat character: HIGH-Meaning / LOW-Emotion / MEDIUM-Relationship. Writeup at [virtual_mirror_sprint1.md](virtual_mirror_sprint1.md); raw screenshots at `data/sc chat analyzer/`. |

Sprint 2 milestones slipped 9 to 17 days on intermediate dates but all landed before May 21. Tier-1 corpus downloaded + SHA-256 hashed 2026-05-19 (1.3 GB, mp4s held for Sprint-3 WP2). Virtual Mirror data captured + analyzed 2026-05-18. May-21 deliverables shipped 2026-05-20: `OSN.pptx` deck, `may21_script.md` (Hammad presenting), `may21_qa_prep.md` (21 Q&A entries). **Status Meeting III complete (2026-05-21): both supervisors satisfied; DPIA NOT required (semester-project scope, no paper); MediaPipe calibration downgrades to "try and iterate". See `onsidian vault/OSN-M/wiki/01_project/status_meeting_3_outcome.md` for the decision record.**

---

## 4. Who owns what — your role in detail

Read your section three times. Re-read it at the start of each iteration.

The principle: each person has **one clear lead area** and **one concrete primary deliverable**. Zuraiz integrates across all of them; teammates work in parallel and hand off via well-defined data formats.

---

### 4.1 Zuraiz — Project lead, Audio (WP1), Integration, Paper

**What you own**: the project as a whole — every supervisor email, every iteration report, every architectural decision, every commit on `main`. The audio half of the pipeline (librosa, demucs, pyin). Integration of WP1 + WP2 + WP3 outputs into the E(t) timeline. The paper, as first author. The Apr 30 and Jul 23 presentations.

**Primary deliverables**:

| Date                       | Deliverable                                                            |
| :------------------------- | :--------------------------------------------------------------------- |
| 2026-04-30 ✓               | Apr 30 status meeting (deck and script in repo root)                   |
| 2026-05-01 ✓ (done 05-17)  | Tier 2 datasets downloaded with SHA-256 manifest                       |
| 2026-05-08 ✓ (done 05-17)  | WP1 audio pipeline runs end-to-end on Dagstuhl, parquet feature output |
| 2026-05-21 ✓               | May 21 status meeting (Hammad presented; both supervisors satisfied)   |
| 2026-06-14                 | E(t) end-to-end on full corpus, null model running                     |
| 2026-07-07                 | Paper draft v1                                                         |
| 2026-07-23                 | Final 20-minute presentation                                           |
| 2026-07-31                 | Final paper submitted                                                  |

**Stack**: Python 3.11, librosa 0.10.2, demucs 4.0.1, numpy 1.26.4, scipy, pandas, pyarrow.

**Acceptance for "done"**: by July 31, a fresh clone on a Win 11 laptop can run `make all` and reproduce the paper's headline numbers and figures.

---

### 4.2 Hammad Anwar — Computer vision (WP2)

**What you own**: turning each choir video into a per-frame, per-singer parquet of body and face coordinates. Specifically: pose keypoints (33 from MediaPipe Pose), face landmarks (468 from FaceMesh, lip subset only), shoulder-rise breath proxy. You also own the validation study that confirms MediaPipe head-sway is reliable enough for our V(t) formula.

**Sprint-2 status (2026-05-17)**: Pose schema + extractor shipped in `src/choir_entanglement/video/{schema,pose.py}` (33-keypoint MediaPipe Pose + 40 lip landmarks + 3 derived features). First pose parquet ran on a Tier-1 SoundJack video (`data/processed/tier1/ouFyQKszE_Y/pose.parquet`, 595 frames, 79.5% pose detection rate). Calibration note at `wp2_calibration_sprint2.md`. Smoke tests 4/4 pass.

**Primary deliverable**: per-singer parquet feature files at `processed/<video_id>/pose/<singer>.parquet` for at least 10 Tier-2 videos by **2026-05-22**, plus a one-page calibration study documenting head-sway Pearson correlation against a reference tool. If correlation is below 0.70, the fallback is OpenPose (CMU); the calibration study triggers that decision.

| Date                       | What you deliver                                                                                     |
| :------------------------- | :--------------------------------------------------------------------------------------------------- |
| 2026-04-29                 | Read the four papers in your reading list (§4.2, below).                                            |
| 2026-05-08 ✓ (done 05-17)  | Schema design for `pose/<singer>.parquet` finalised in `src/choir_entanglement/video/schema.py`. |
| 2026-05-22 ✓ (1/10, done 05-17) | Pose pipeline produces parquet for 10 videos. Calibration study committed.                           |
| 2026-06-30                 | All Tier-2 + Tier-1 videos processed.                                                                |

**Stack**: Python 3.11, mediapipe 0.10.14, opencv-python 4.10, pandas, pyarrow.

**Tools and files**:

- Source code lives in `src/choir_entanglement/video/`.
- Test data: start with one of Hacker's 5 Tier-0 URLs (downloaded by Zuraiz to `raw/youtube/<video_id>/`).
- The MediaPipe smoke test in `tests/test_smoke.py::test_mediapipe_pose_instantiates` is a working example of the API.
- Reference: PROJECT_GUIDE.md §11.1 for the V(t) formula and which keypoints feed which sub-feature.

**First-day onboarding (do these in order)**:

1. Clone the repo and run `make smoke`. Three tests should pass in under 90 seconds.
2. Read this brief in full (you are reading it now — good).
3. Read PROJECT_GUIDE.md sections 1-10 (skip section 11 for now).
4. Read these four papers in `onsidian vault/OSN-M/raw/01_primary_sources/`:
   - `On-device Real-time Body Pose Tracking…` (P-03 BlazePose) — what MediaPipe Pose actually does.
   - `huSync_…` (P-14) — how to operationalise sync from pose data.
   - `Preprocessing MediaPipe Joint Annotation…` (P-20) — confidence-weighted interpolation tricks (relevant to your pipeline).
   - `Multimodal_Machine_Learning_…Videoconference_Fluidity_…` (P-08) — what visual features predict coordination quality.
5. Skim the corresponding Citrinitas concept pages in `onsidian vault/OSN-M/wiki/` (`pose_standardization.md`, `handedness_bias.md`, `joint_visibility_loss.md`).
6. Run `mediapipe.solutions.pose.Pose()` on one Tier-0 video and inspect the keypoint output for one frame.
7. Open a `feat/wp2-schema` branch, draft the parquet schema, push, ask for review.

**Acceptance for "done"**: by 2026-06-30, every video in `raw/youtube/` and every Tier-2 piece has a corresponding `processed/<video_id>/pose/*.parquet` that downstream WP3 can consume without modification.

**Where to ask for help**: WhatsApp first. Tag Zuraiz if blocked more than 4 hours.

---

### 4.3 Hassan Ahmed — Network science (WP3, Prof. Hacker's pillar)

**What you own**: the influence-graph half of the project. Given per-singer note onsets (from WP1), you run pairwise Granger-causality tests in sliding windows, build a directed graph, compute network metrics (density, modularity, centrality), and validate against a null model. The polished SVG of this graph for one representative piece is **Prof. Hacker's flagship figure**, mentioned by name on slide 7 of the Apr 30 deck.

**Sprint-2 status (2026-05-17)**: Granger module + influence-graph builder shipped in `src/choir_entanglement/network/{granger,influence_graph}.py`, with circular-shift null (200 shuffles). Pairwise Granger on Dagstuhl SATB Quartet A Take 02 RMS envelopes: 11/12 directed edges significant at p_null < 0.05, graph density 0.92, most-central voice Soprano. First draft of Hacker's flagship figure: `data/figures/wp3_influence_graph.png`. Smoke tests 4/4 pass.

**Primary deliverable**: a publication-quality directed influence graph for at least one Tier-2 piece by **2026-05-31**, plus the code that regenerates it for any new piece. By June 14, the same code runs on the full corpus and outputs one graph per piece.

| Date                       | What you deliver                                                                                                                                    |
| :------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| 2026-04-29                 | Read the three papers in your reading list (below).                                                                                                 |
| 2026-05-15 ✓ (done 05-17)  | Granger causality prototype on synthetic data (sanity check).                                                                                       |
| 2026-05-31 ✓ (done 05-17)  | First real influence graph on a Dagstuhl piece. Standard Granger + circular-shift null (200 shuffles) running. COP-GC variant deferred to Sprint 3. |
| 2026-06-14                 | All Tier-2 + Tier-3 pieces have computed graphs. Network metrics tabulated.                                                                         |
| 2026-07-07                 | Hacker's flagship figure polished for the paper. SVG output, Gephi-cleaned. (Draft already at `data/figures/wp3_influence_graph.png`.)         |

**Stack**: Python 3.11, networkx 3.3, statsmodels 0.14.2, python-louvain 0.16, scikit-learn 1.5, Gephi for figure polish.

**Tools and files**:

- Source code lives in `src/choir_entanglement/network/`.
- Input data: per-singer onset time-series produced by WP1 (Zuraiz). Format: parquet with columns `[singer_id, onset_time_s, onset_strength]`.
- Reference: PROJECT_GUIDE.md §11.1 for the N(t) formula and §11.4 Decision 4 for the Granger-vs-COP-GC choice.

**First-day onboarding (do these in order)**:

1. Clone the repo and run `make smoke`.
2. Read this brief in full.
3. Read PROJECT_GUIDE.md sections 1-10.
4. Read these three papers in `onsidian vault/OSN-M/raw/01_primary_sources/`:
   - `Augmenting Granger Causality through Ordinal Patterns.pdf` (P-22) — the COP-GC method, Zanin's recommendation to run both variants.
   - `Granger Causal Representation Learning for Groups.pdf` (P-21) — group-level causal structure (note: T ≥ 500 sample-size floor).
   - `Multimodal_Machine_Learning_…Videoconference_Fluidity_…` (P-08) — they use Granger on body motion for fluidity prediction.
5. Skim the Citrinitas concept pages: `granger_influence_index.md`, `ordinal_synchrony_pattern.md`, `non_linear_causal_leakage.md`.
6. Prototype: `from statsmodels.tsa.stattools import grangercausalitytests` on a synthetic two-singer onset series. Make it return a non-trivial F-statistic.
7. Open a `feat/wp3-granger` branch, push, ask for review.

**Acceptance for "done"**: Hacker's flagship figure exists as an SVG in `results/figures/` by July 7, generated by code committed to `src/choir_entanglement/network/`. The figure is reviewable, reproducible, and looks publication-clean.

**Where to ask for help**: WhatsApp first. Tag Zuraiz if blocked more than 4 hours. Granger stationarity is genuinely tricky; do not silently power through it.

---

### 4.4 Kumaran Vasu — Dashboard and figures (WP4, Prof. Gloor's pillar)

**What you own**: the human-facing layer of the project. A small web dashboard that takes a video, plays it back with overlays (pose skeletons, E(t) timeline, network animation), and lets the user scrub through it. The polished alchemical-stage diagram that is **Prof. Gloor's flagship figure**, mentioned on slide 8 of the Apr 30 deck. All paper figures with consistent visual style.

**Sprint-2 status (2026-05-17)**: Dashboard wireframe + design doc shipped at `frontend/{wireframe.md,README.md}` (4-panel layout: video+pose / influence graph / E(t) timeline / metadata). First draft of Gloor's flagship alchemical-stage figure: `data/figures/wp4_alchemical_stages.png` (4-stage Nigredo→Albedo→Citrinitas→Rubedo pipeline). React+Vite scaffold lands Sprint 3.

**Primary deliverable**: a working dashboard by **2026-06-21** that runs the 60-second live demo without crashing on July 23. The alchemical-stage diagram polished and ready for the paper by July 7.

| Date                       | What you deliver                                                                                                          |
| :------------------------- | :------------------------------------------------------------------------------------------------------------------------ |
| 2026-04-29                 | Read the two papers in your reading list (below).                                                                         |
| 2026-05-22 ✓ (done 05-17)  | Dashboard wireframe (markdown + ASCII layout) at `frontend/wireframe.md`.                                              |
| 2026-06-21                 | Dashboard alpha: takes a video ID, displays timeline + pose overlay + network graph. Runs locally on a Windows 11 laptop. |
| 2026-07-07                 | Alchemical-stage diagram polished. Paper figure pipeline (consistent colors, fonts) in place. (Draft at `data/figures/wp4_alchemical_stages.png`.) |
| 2026-07-23                 | 60-second live demo runs without crashing in front of the supervisors.                                                    |

**Stack**: React 18.3 + Vite 5.3 + TypeScript 5.5 + D3 7.9 + Plotly 2.33 frontend. FastAPI 0.111 + uvicorn 0.30 backend. Tailwind CSS for styling. Playwright for end-to-end tests.

**Tools and files**:

- Frontend lives in `src/choir_entanglement/dashboard/` (FastAPI backend) plus a separate `frontend/` directory you will create for the React app (this is a structural decision we will lock together once you start).
- Input data: parquet files from WP1, WP2, WP3 plus the computed E(t) timeline.
- Reference: PROJECT_GUIDE.md §10 Gate D for what "polish" means in this project.

**First-day onboarding (do these in order)**:

1. Clone the repo and run `make smoke`.
2. Read this brief in full.
3. Read PROJECT_GUIDE.md sections 1-10.
4. Read these two papers in `onsidian vault/OSN-M/raw/01_primary_sources/` and `02_secondary_sources/`:
   - `Cybernetic_Alchemy_Complete.pdf` (S-01, Gloor's book) — Chapter 14 in detail (*Data as Prima Materia*) and the prologue. The alchemical-stage framing for Gloor's flagship figure comes from here.
   - `'Entanglement' – A new dynamic metric to measure team flow.pdf` (S-02) — the original entanglement formula. Helps you understand what we are visualising.
5. Skim `onsidian vault/OSN-M/wiki/04_logistics/alchemical_data_pipeline.md` for the visual mapping we have already drafted.
6. Sketch a wireframe for the dashboard (Figma, Excalidraw, or paper) and post it in the WhatsApp group for feedback.
7. Open a `feat/wp4-dashboard` branch, push the wireframe and a `frontend/README.md`, ask for review.

**Acceptance for "done"**: on July 23, with two supervisors watching, you click "play" and the dashboard runs for 60 seconds without crashing, scrubbing through one piece, with all three overlays (pose, E(t), network) animating.

**Where to ask for help**: WhatsApp first. Tag Zuraiz if blocked more than 4 hours. Frontend tooling has a way of swallowing a day; flag early.

---

## 5. How we work together

### 5.1 Iteration cadence

Six iterations between Apr 17 and Jul 23. Each iteration ends on a status meeting with deliverables, not a status update.

| Iteration | Status meeting             | Date              |
| :-------- | :------------------------- | :---------------- |
| 1         | Status #1 (block course)   | 2026-04-16 (done) |
| 2         | Status #2 (Hacker + Gloor) | 2026-04-30        |
| 3         | Status #3 + Virtual Mirror | 2026-05-21        |
| 4         | Status #4                  | 2026-06-11        |
| 5         | Status #5                  | 2026-06-25        |
| 6         | Final presentation         | 2026-07-23        |

### 5.2 Communication

- **Git** — atomic commits, conventional commit messages (`feat:`, `fix:`, `docs:`, etc.), branch per WP (`feat/wp2-*`, `feat/wp3-*`, `feat/wp4-*`).
- **Vault wiki** — for everything that has to outlive a WhatsApp scroll: source digests, evidence trails, decisions. Zuraiz maintains.

### 5.3 Iteration deliverable rule

Each iteration ends with **one named artefact** per WP that is reviewable. Not "I worked on X this week." A parquet file. A pull request. A figure. An SVG. A wireframe. Something the rest of the team can open and look at.

### 5.4 Don't be silent on a blocker

Four-hour rule: if you have been stuck on the same issue for more than four hours, post in WhatsApp and tag Zuraiz. Eight-hour silence on a blocker costs the team a day in the back-end. Coming early is a strength, not a weakness.

---

## 6. Where to find things

| You need…                                        | Look in…                                                                        |
| :------------------------------------------------ | :------------------------------------------------------------------------------- |
| Project spec, formulas, decisions, limitations    | `PROJECT_GUIDE.md` (this is the technical source of truth)                     |
| Project briefing for humans (this file)           | `TEAM_BRIEF.md`                                                                |
| Apr 30 / Jul 23 deck and speaker script           | `apr30_deck.md`, `apr30_script.md`                                           |
| Source PDFs                                       | `onsidian vault/OSN-M/raw/01_primary_sources/` and `02_secondary_sources/`   |
| Per-paper digests with page citations             | `onsidian vault/OSN-M/wiki/03_models/`, `05_metrics/`, `06_failure_modes/` |
| Concept syntheses across multiple papers          | `onsidian vault/OSN-M/wiki/` (Citrinitas / Rubedo pages, see `index.md`)     |
| Audit of which prior digests were wrong (and how) | `onsidian vault/OSN-M/wiki/00_overview/deep_read_audit.md`                     |
| Project log of all wiki operations                | `onsidian vault/OSN-M/wiki/log.md`                                             |
| Code                                              | `src/choir_entanglement/`                                                      |
| Tests                                             | `tests/`                                                                       |
| Datasets                                          | `raw/` (text manifests committed; binaries gitignored)                         |
| Computed features                                 | `processed/` and `features/` (gitignored)                                    |
| Final results                                     | `results/` (gitignored, recreated by `make all`)                             |

---

## 7. FAQ

### Why aren't we just recording ourselves singing?

Three reasons: ethics overhead (we would need IRB), we are not trained singers (self-selection bias), and the original scope explicitly forbade self-recording. We use publicly available YouTube and published academic datasets instead.

### Can we separate individual singers from a YouTube mix?

No. YouTube gives us a mixed stereo track. Demucs separates instruments not voices, and pyin is monophonic. That is exactly why H1 (the regime-discrimination test) runs on Tier 2 multitrack with controlled latency injection (Tier 3), where each singer is on a separate microphone. Tier 1 YouTube is used for visual analysis only.

### What is the Virtual Mirror on May 21?

The seminar requires us to treat our own team as a COIN. We export our team WhatsApp group, run it through SocialCompass, classify the team archetype (Bee, Ant, Butterfly, Capybara, or Leech), and report the result. Not the same as analysing choir data; this is meta-level self-reflection.

### What is EBSE and why does it keep coming up?

Evidence-Based Software Engineering: every technical decision is documented with source, confidence rating, applicability rating. See `PROJECT_GUIDE.md` §11.4 for examples. Practical implication: when you make a non-trivial choice (e.g. "use library X over library Y"), drop a one-table evidence trail in the relevant Citrinitas concept page in the vault, or in your PR description.

### What is the binary we are testing?

Either latency above some threshold breaks coordination (hard ceiling, NMP tools need new architectures) or human bodies compensate through visual cues (Honest Signals theory holds, design lesson flips to visual fidelity). Either finding is publishable.

### Where do I push my code?

Branch per WP: `feat/wp2-*`, `feat/wp3-*`, `feat/wp4-*`. Push to origin. Open a PR against `main`. Zuraiz reviews and merges.

### What if I find a problem with PROJECT_GUIDE.md?

Open an issue or post in WhatsApp. Do not edit PROJECT_GUIDE.md without coordination; it is the spec, not a working document.

### What if a supervisor emails me directly?

Forward to me before replying. All supervisor correspondence routes through the project lead so we keep one consistent voice and timeline.
