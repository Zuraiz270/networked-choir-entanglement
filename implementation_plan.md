# Project 8 — Networked Choir Entanglement Platform

**Deep Implementation Plan (v2.1)** · drafted 2026-04-17 · presenter & PI: Zuraiz
**Supervisor**: Prof. Dr. Janine Hacker (Uni Bamberg) · **Second grader**: Prof. Peter Gloor (MIT)
**Target**: A+ · **Scope**: 24 ECTS · **Final**: 2026-07-17

> **v2.1 changelog (2026-04-17, post-review)**: Fixed DSP blocker flagged by external review — mixed-stereo YouTube audio cannot yield per-singer pairwise audio or Granger-network features (Demucs separates *instruments*, not *singers*; `pyin` is monophonic). Tier 1 repositioned from "audio+visual all-rounder" to **Visual-Primary**; per-singer audio + network moved to Tier 2 (academic multitrack) + Tier 3 (controlled latency-injection). Added April 30 Hacker/Gloor status meeting milestone. Self-recording remains forbidden per original user instruction.

---

## Context

This plan replaces the v1 implementation_plan.md and supplements [Claude_Code_Project_8_Context.md](Claude_Code_Project_8_Context.md).

**Why a new plan now**: The v1 plan named the architecture but was **not EBSE-compliant** — no DOIs, no evidence trails, no dataset checksums, no measurable success gates, no legal-basis reasoning for YouTube scraping, no formula for "entanglement", no Obsidian-vault alchemy integration, and no role-specific effort budget. Prof. Hacker will review at **Iteration 2 (Apr 24)**; we need rigor matching her Chair-of-Information-Systems standards while honouring Gloor's Honest-Signals / COINs lens.

**Scientific question**: Do online choirs exhibit **measurable multi-modal entanglement** — coupled audio, visual, and social-network signals — and does this coupling discriminate between Zoom-class (high-latency, 150–400 ms RTT) and SoundJack-class (low-latency NMP, 20–60 ms RTT) regimes?

**Intended outcome**: an open-source, reproducible platform + 8–12 page paper + 20 min final presentation that (a) operationalises an *Entanglement Index* E(t), (b) discriminates regimes at Cohen's d ≥ 0.5 via **controlled latency injection on multitrack data** (Tier 3, not natural YouTube), (c) produces one publication-quality directed influence graph (Hacker deliverable) and one alchemical-stage Honest-Signals diagram (Gloor deliverable).

**Near-term milestone**: **Apr 30 2026, 14:00 CET** — Hacker/Gloor status meeting, 5–10 min presentation covering *team / goals / project plan / next iteration / way-of-working*. This plan IS that presentation's content source.

**Verified ground truth (2026-04-17)**:

- Team = 4 Bamberg students: Zuraiz, Hammad Anwar, Hassan Ahmed, **Kumaran Vasu**
- Cybernetic Alchemy PDF present at [onsidian vault/OSN-M/raw/Cybernetic_Alchemy_Complete.pdf](onsidian%20vault/OSN-M/raw/Cybernetic_Alchemy_Complete.pdf) — **not yet ingested**
- Prof. Hacker's Tier-0 YouTube URL list is **not in the vault** — first blocker
- Git state: branch `main`, 1 commit, 3 untracked .md files
- Existing wiki schema uses alchemy dirs: `raw/` → `wiki/entities/` → `wiki/concepts/` → `wiki/` root

---

## §1 End Goals (4 levels)

### L1 Research (scientific question) — hypothesis → tier mapping

- **L1.1 (H1)** E(t) discriminates Zoom vs SoundJack regimes at Cohen's d ≥ 0.5 on ≥ 2 sub-components — tested on **Tier 3** controlled latency-injection (within-piece paired design).
- **L1.2 (H2)** Granger-causal directed onset-graph topology differs across regimes (density, modularity, Burt's constraint) at p<0.05 vs 200-permutation null — tested on **Tier 2 + Tier 3** multitrack.
- **L1.3 (H3)** Honest Signals (Pentland 2008) — trunk-sway + breath synchrony — contribute ΔR² ≥ 0.10 to E(t) beyond audio DTW alignment (hierarchical regression) — tested on **Tier 1 (visual, N=150) + Tier 2 (audio ground truth)**.

### L2 Technical (artefacts)

- **L2.1** `choir_entanglement/` Python package, MIT-licensed, reproducible via `uv run make all` in Docker < 15 min on fresh Windows 11.
- **L2.2** React+Vite+FastAPI dashboard with 60 s live demo (timeline scrubber, pose overlay, animated network graph).
- **L2.3** BagIt-conformant data provenance: every derived artefact → raw YouTube `video_id` + SHA-256.

### L3 Academic (paper + presentation)

- **L3.1** 8–12 page IEEE/LNCS paper, DOI-backed citations only, full reproducibility appendix.
- **L3.2** ≤ 10 slide, 20-min final presentation (Jul 17) with single embedded 60 s live dashboard demo.
- **L3.3** One Hacker-deliverable (publication-quality directed influence graph) + one Gloor-deliverable (alchemical HS transformation diagram).

### L4 Process (COINs-as-we-go)

- **L4.1** Team operates as a CIN itself: public Git, atomic Conventional Commits, weekly honest-signals micro-retro.
- **L4.2** Kumaran onboarded with documented 14-day ramp (Apr 17 – May 1) including backfill of his SocialCompass data.
- **L4.3** All EBSE evidence trails logged in vault `log.md` per alchemical-wiki protocol.

---

## §2 Theoretical Foundation

### 2.1 Gloor — COINs × Alchemical Pipeline

| Stage | Vault/repo dir | Pipeline action | Artefact |
|---|---|---|---|
| **Nigredo** | `raw/` | yt-dlp ingest | .mp4 + .info.json + sha256 |
| **Albedo** | `processed/`, `wiki/entities/` | Demucs stems + MediaPipe keypoints | voice_i.wav, pose.parquet |
| **Citrinitas** | `features/`, `wiki/concepts/` | feature extraction + synthesis | entanglement_index.md, onset_graph.gpickle |
| **Rubedo** | `results/`, `wiki/` root | paper + dashboard | paper.pdf, dashboard bundle |

**COINs** (Gloor, *Swarm Creativity*, Oxford 2005; *Collaborative Innovation Networks*, Springer 2017): a distributed choir **is** a CIN expressing itself through voice.

### 2.2 Hacker — Engagement + Trust-in-Virtual-Teams

- Hacker et al. 2013, *Enablers and Inhibitors of Engagement in Enterprise Social Networks* — latency = inhibitor; leader-follower visibility = enabler. Both operationalised as N-features.
- Hacker et al. 2019, *Trust in Virtual Teams: A Multidisciplinary Review* — **swift-trust** predicts sustained coordination. Testable: onset-variance in first 15 s predicts E(t) in minutes 2–5 at r ≥ 0.4.

### 2.3 Pentland — Honest Signals (MIT Press 2008)

| Pentland channel | Feature | Modality |
|---|---|---|
| Influence | Granger-cause onset delay (N1) | audio→network |
| Mimicry | Trunk-sway xcorr (V1) | video |
| Activity | Breath-rate envelope (V3, A8) | video+audio |
| Consistency | Tempo variance, F0 drift (A5, A3) | audio |

---

## §3 "Entanglement" — Operational Definition

```
E(t) = (1/3)·A(t) + (1/3)·V(t) + (1/3)·N(t)    # equal-weight baseline; ablated
```

**A(t) — Acoustic coupling**:

```
A(t) = 0.4·(1 − DTW_cost_norm)                 # librosa.sequence.dtw
     + 0.3·mean_pairwise_F0_xcorr(|lag|<50ms)  # pyin
     + 0.3·onset_sync_kappa(50ms bins)         # Fleiss κ on onsets
```

**V(t) — Visual coupling**:

```
V(t) = 0.5·trunk_sway_xcorr(|lag|<500ms)       # MediaPipe Pose lm 11,12,23,24
     + 0.3·breath_envelope_xcorr                # shoulder-rise proxy
     + 0.2·mouth_aperture_sync                  # FaceMesh lm 13,14,78,308
```

**N(t) — Network coherence**:

```
G_t = digraph; edge i→j weight = Granger F-stat on onset-delay (window 10s, lag AIC-selected)
N(t) = 0.4·(1 − |density_dev_from_null|)
     + 0.3·inverse_Gini(eigenvector_centrality)   # → collective leadership
     + 0.3·modularity_Q(Louvain)
```

**Null model**: 200× time-shuffled singer streams. E(t) reported as z against null.

> **DSP reality check**: A(t) and N(t) both require *per-singer* audio streams. Tier 1 mixed-stereo YouTube cannot satisfy this; only V(t) is fully computable there. On Tier 1 we substitute A_ens(t) (collective tempo stability, global onset density, spectral-flux consistency) — descriptive only, not on the H1 discrimination path. Multi-f0 SATB estimation (Cuesta/Gómez/Bittner 2020, ISMIR) kept as Tier 1 stretch.

---

## §4 Metrics Catalog (Tier-gated)

- **T1** = mixed-stereo YouTube (N=150)
- **T2** = multitrack (Dagstuhl/ESMUC/ChoralSynth)
- **T3** = controlled latency-injection experiment

### Audio (11 features)

| # | Feature | Tier | P/S |
|---|---|---|---|
| A1 | Ensemble onset density (spectral flux) | T1+T2+T3 | **P** |
| A2 | Pairwise DTW cost | T2+T3 only | **P** |
| A3 | Pairwise F0 xcorr (pyin per-singer) | T2+T3 only | **P** |
| A3* | Per-section (S/A/T/B) multi-f0 (Cuesta 2020) | T1 stretch | S |
| A4 | Global spectral-flux sync | T1+T2+T3 | **P** |
| A5 | Collective tempo variance | T1+T2+T3 | **P** |
| A6 | Vibrato 5–7 Hz coupling | T2+T3 | S |
| A7 | Harmonic coherence | T2+T3 | S |
| A8 | Pairwise breath alignment | T2+T3 | **P** |
| A9 | Pairwise consonant-onset drift | T2+T3 | **P** |
| A10 | Expressivity index | T2+T3 | S |
| A11 | Demucs-residual energy | T2+T3 | S |

### Visual (9 features) — all Tier 1 compatible

V1 trunk sway xcorr **P** · V2 head sway (calibrated) S · V3 mouth aperture **P** · V4 blink sync S · V5 FFI proxy via py-feat S · V6 head-yaw coupling **P** · V7 hand-gesture mirror S · V8 gaze if face>200 px S · V9 smile-onset sync S

### Network (8 features) — T2+T3 only (require per-singer streams)

N1 Granger-cause digraph **P** · N2 eigenvector/PageRank/betweenness/closeness **P** · N3 density **P** · N4 Louvain modularity **P** · N5 temporal 3-node motifs S · N6 Burt's constraint (leadership) **P** · N7 Pearson-r tie strength **P** · N8 community NMI S

On Tier 1 we report *visual-derived tie strength*: pairwise xcorr of trunk-sway time-series = V-tie → visual-only network analogue for H3.

### Empirical (literature-only; no self-recording)

E1 Group Environment Questionnaire (Brawley-Widmeyer 1987) · E2 Flow State Scale-2 (Jackson & Eklund 2004) · E3 NASA-TLX · E4 Post-session interview meta-coding (Cairns 2024) · E5 ~~self-reported~~ **dropped** (human subjects).

---

## §5 Data-Sourcing Policy (STRICT)

### Tier 0 — Prof. Hacker's curated URLs (must obtain by Apr 21)

- **Apr 17 action**: Zuraiz emails Hacker requesting YT URL list. Store at `raw/hacker_url_list.csv`; digest at `wiki/sources/hacker_url_list.md`.
- **Go/no-go Apr 22 09:00**: if silent → escalate + proceed on Tier 1 only (log in `log.md`).

### Tier 1 — YouTube COVID virtual-choir corpus (VISUAL-PRIMARY, target 150 / stretch 200 videos)

**Scientific role**: large-N corpus for visual entanglement (V1–V9) + ensemble-descriptive acoustic (A1, A4, A5). Serves **H3**. Does **not** serve H1 (mixed audio + unreliable regime labels).

- Queries (yt-dlp search): `"virtual choir"`, `"zoom choir"`, `"soundjack choir"`, `"online choir performance"`, `"distributed choir COVID"`, `"SATB virtual"`, `"Eric Whitacre virtual choir"`.
- Date filter: **2020-03-01 to 2022-06-30**.
- **Inclusion**: SATB visible, English title, ≥ 3 min, CC or §60d UrhG-fair-use, ≥ 4 visible singers.
- **Exclusion**: heavy post-prod, single-performer multitrack, copyright-struck, private.
- **Legal basis**: §60d UrhG (DE TDM research exception), EU DSM Dir. 2019/790 Art. 3, GDPR Art. 6(1)(f) + Art. 89 — store only feature vectors long-term, delete mp4 after extraction, never redistribute.
- **Manifest schema** `raw/corpus_manifest.csv`: `video_id, url, title, channel, upload_date, duration_s, license, singer_count_est, latency_regime_label, satb_confirmed, download_sha256, ingest_date`.

### Tier 2 — Academic multitrack baselines (AUDIO+NETWORK PRIMARY)

**Scientific role**: per-singer isolated audio enables A2, A3, A8, A9 + all N1–N8. Serves **H2**.

- **Dagstuhl ChoirSet** · Rosenzweig et al., *TISMIR* 2020 · DOI [10.5334/tismir.48](https://doi.org/10.5334/tismir.48).
- **ESMUC Choral Singing Dataset** · Cuesta et al. · Zenodo 1286570 — 3 pieces, 16 singers.
- **Cairns 2024 York thesis** — NMP / SoundJack comparator.
- **DUST Dataset** — packet-loss traces (verify access by Apr 24).
- **ChoralSynth** — synthetic SATB.

### Tier 3 — Controlled latency injection (REGIME-DISCRIMINATION PRIMARY, v2.1 elevated)

**Scientific role**: primary ground-truth design for **H1**. Take Dagstuhl/ESMUC multitrack and *programmatically* apply regime-characterising profiles:

| Regime | RTT (ms) | Jitter σ (ms) | Packet loss % | Source |
|---|---|---|---|---|
| SoundJack-low | 20–40 | 3 | 0 | Carôt & Werner 2007 |
| SoundJack-mid | 40–80 | 8 | 0.5 | Lazzaro 2020 |
| Zoom-typical | 150–250 | 30 | 1 | Zoom whitepaper + field measurements |
| Zoom-degraded | 300–500 | 60 | 3 | COVID-era internet reports |

Apply via `scipy.signal.delay` + jitter draw + periodic sample zero-out. Per piece × regime → compute E(t), N1, discrimination stats. **Falsifiable, reproducible** — this is what H1 needs.

### Forbidden

Self-recording · asking third-party choirs to perform · PII beyond public metadata · full-face storage beyond feature extraction window.

### Directory discipline

```
raw/youtube/<video_id>/             # Nigredo · immutable
processed/<video_id>/stems|pose/    # Albedo
features/<video_id>.parquet         # Citrinitas
results/Et.parquet, graphs/, figures/   # Rubedo
```

---

## §6 Four Work Packages (~180 h each)

### WP1 — Zuraiz · Principal Investigator + Audio ML & Integration Lead

**Why flagship**: E(t) is the paper's central scientific contribution; owning it = first-authorship = most visible A+ signal for both profs. Aligns with Zuraiz's Master's thesis on Audio-Language Models.

**Stack**: Python 3.11.9 · librosa 0.10.2 · demucs 4.0.1 · numpy 1.26.4 · scipy 1.13.1 · pandas 2.2.2 · pyarrow 16.1.0 · uv 0.4.x · pytest 8.2 · ruff 0.5 · mypy 1.10 · pre-commit 3.7 · Docker 26.

**Deliverables**:

1. Repo scaffold: `pyproject.toml` + `uv.lock` + GitHub Actions CI + Dockerfile.
2. `choir_entanglement/ingest/` — yt-dlp wrapper + SHA-256 provenance + license capture.
3. `choir_entanglement/audio/` — ensemble features (A1, A4, A5) on Tier 1 + per-singer (A2, A3, A8, A9) on Tier 2 + Cuesta multi-f0 stretch.
4. `choir_entanglement/latency_injection/` — Tier 3 programmatic latency module. **Owns H1 experimental design.**
5. `choir_entanglement/integration/` — **E(t) computation**.
6. Tier-2 loader (Dagstuhl + ESMUC) with pinned MD5s.
7. `make all` orchestrator → `features/*.parquet` + `results/Et.parquet`.
8. **Paper first-author** + figure coordinator.
9. **April 30 presentation deck** — Zuraiz delivers.
10. Weekly sprint update + EBSE evidence trails.

**Fallback**: if Demucs CPU too slow → `librosa.effects.hpss` + spectral gating.

### WP2 — Kumaran · Computer Vision Engineer

**Why Kumaran**: joined project-phase only, no SocialCompass data. CV is the most modular self-contained pillar — clear success criterion (pose parquet per video), minimum upstream coupling.

**Stack**: mediapipe 0.10.14 · opencv-python 4.10.0.84 · ffmpeg-python 0.2.0 · py-feat 0.6.2.

**Deliverables**:

1. 14-day onboarding (Apr 17 – May 1) + SocialCompass backfill.
2. `choir_entanglement/video/` — per-singer face detect + crop.
3. Pose extraction → `processed/<id>/pose/<singer>.parquet`.
4. FaceMesh mouth-aperture + blink extractors (V3, V4).
5. Head-sway calibration vs OpenFace on 5 clips → `wiki/concepts/pose_validity.md`.
6. Feature module V1, V3, V6 primary + V2, V4, V5, V7 secondary.
7. Validity caveat for paper Methods.

**Interface**: `pose/*.parquet` schema frozen May 8.
**Fallback**: OpenPose in Docker.

### WP3 — Hammad · Network Scientist (Hacker pillar)

**Why Hammad**: Capybara archetype (deliberate, 2 h avg latency) fits methodical Granger-causality work.

**Scope**: operates on **Tier 2 + Tier 3** per-singer onset streams. Tier 1 not in his domain — instead WP3 uses WP2's visual-derived tie matrix as parallel visual-network comparison (negative-control study).

**Stack**: networkx 3.3 · statsmodels 0.14.2 · python-louvain 0.16 · teneto 0.5.3 · scikit-learn 1.5 · Gephi 0.10.1 · matplotlib 3.9.

**Deliverables**:

1. Granger-causality (N1) with AIC lag selection, 10 s / 2 s sliding window.
2. Centrality + density + modularity (N2–N4, N6).
3. Null-model generator (200× time-shuffled; z-score).
4. Temporal motif census (N5).
5. Gephi export → `results/figures/network_*.svg`.
6. Regime-discrimination test (Mann-Whitney U on N1 density Zoom vs SoundJack).
7. **Publication-quality directed influence graph** (Hacker-honouring artefact).

**Fallback**: transfer entropy via IDTxl if stationarity violated.

### WP4 — Hassan · Empirical + Dashboard (Rubedo pillar)

**Why Hassan**: Ant archetype + Happy Perceptiface + high risk tolerance = suited to integration + UX risk. Rubedo artefact is the most "show-off" component for Gloor.

**Stack**: React 18.3 · Vite 5.3 · TypeScript 5.5 · d3 7.9 · visx 3.11 · Plotly 2.33 · FastAPI 0.111 · uvicorn 0.30 · Tailwind 3.4 · Playwright 1.45.

**Deliverables**:

1. FastAPI `/api/v1/video/{id}` endpoint.
2. Dashboard: timeline scrubber + 3-panel view.
3. 60 s demo script (review by Jun 21).
4. Literature-meta: Group Flow indicators from Cairns 2024 + NMP lit.
5. **Honest-Signals alchemical diagram** (Gloor-honouring artefact).
6. Playwright E2E smoke test.
7. Paper-figure coordinator (unified colormap + typography).

**Fallback**: Plotly Dash if React timeline heavy.

---

## §7 Timeline & Milestones

| Date | Sprint | Deliverable | Owner | Evidence-of-done |
|---|---|---|---|---|
| **Apr 17** | S0 kickoff | Hacker URL email · repo scaffold commit · PDF-ingest plan | Zuraiz | email sent; `log.md` entry |
| Apr 18–23 | S0 | Cybernetic Alchemy PDF ingested → 4 wiki pages | Zuraiz + LLM | Rule 1 check in `log.md` |
| **Apr 21** | Gate | Hacker URL list received or fallback triggered | Zuraiz | CSV at `raw/` or escalation log |
| **Apr 24** | S0 end | Iteration-2 report to Hacker | Zuraiz | PDF |
| **Apr 30, 14:00** | **Milestone** | **Hacker+Gloor status meeting · 5–10 min deck** | Zuraiz | deck + notes |
| May 1 | S1 mid | Tier-2 datasets checksummed; Tier-3 latency script prototyped | Zuraiz | `data/tier2/manifest.json` + `scripts/inject_latency.py` |
| May 8 | S1 | Audio pipeline MVP (A1–A5) on Dagstuhl | Zuraiz | parquet schema frozen |
| May 15 | S1 end | Tier-1 corpus ≥ 80 videos (target 150) | Zuraiz+Hassan | `corpus_manifest.csv` |
| May 22 | S2 | Pose pipeline MVP (V1, V3) on 10 videos | Kumaran | `pose/*.parquet` + validity note |
| May 31 | S2 end | Network MVP: Granger graph on 5 videos | Hammad | `.gpickle` + Gephi render |
| Jun 14 | S3 mid | E(t) on 80+ videos · null running | all | `results/Et_v1.parquet` |
| Jun 21 | S3 | Dashboard alpha | Hassan | Playwright smoke pass |
| **Jun 30** | S3 end | Full pipeline on 150-video corpus · ablations done | all | `make all` green |
| Jul 7 | S4 | Paper draft v1 | Zuraiz coord | PDF in `wiki/` |
| Jul 14 | S4 end | Paper v2 + slides + rehearsal | all | rehearsal log |
| **Jul 17** | Final | 20-min presentation | Zuraiz | delivered |

---

## §8 Top-5 Architectural Decisions — EBSE Evidence Trails

### Decision 1 — yt-dlp (not YouTube Data API)

| # | Source | Level | Year | Conf | Appl | Status |
|--|--|--|--|--|--|--|
| 1 | §60d UrhG (DE TDM research exception) | L3 | 2021 | HIGH | HIGH | ACCEPTED |
| 2 | EU DSM Dir. 2019/790 Art. 3 | L3 | 2019 | HIGH | HIGH | ACCEPTED |
| 3 | yt-dlp GitHub docs | L1 | 2024 | HIGH | HIGH | ACCEPTED |
| 4 | YouTube Data API ToS | L3 | 2024 | HIGH | MED | Rejected R3 |

**Decision**: yt-dlp + per-video license capture. Statutory > platform policy.

### Decision 2 — MediaPipe Pose (not OpenPose)

| # | Source | Level | Year | Conf | Appl | Status |
|--|--|--|--|--|--|--|
| 1 | MediaPipe Pose docs (Google) | L1 | 2024 | HIGH | HIGH | ACCEPTED |
| 2 | Pearson r 0.80–0.91 vs Vicon (limb only) | L2 | 2022 | HIGH | MED | ACCEPTED w/ caveat |
| 3 | OpenPose (CMU) | L1 | 2021 | HIGH | LOW (Win) | REJECTED R7 |

**Decision**: MediaPipe primary; head-sway calibration mandatory.

### Decision 3 — librosa DTW + pyin

| # | Source | Level | Year | Conf | Appl | Status |
|--|--|--|--|--|--|--|
| 1 | librosa docs | L1 | 2024 | HIGH | HIGH | ACCEPTED |
| 2 | Dagstuhl ChoirSet TISMIR (10.5334/tismir.48) | L2 | 2020 | HIGH | HIGH | ACCEPTED |
| 3 | CREPE neural F0 | L2 | 2018 | HIGH | MED (GPU) | DEFERRED |

**Decision**: librosa pyin; CREPE ablation only.

### Decision 4 — Granger causality primary (TE fallback)

| # | Source | Level | Year | Conf | Appl | Status |
|--|--|--|--|--|--|--|
| 1 | statsmodels docs | L1 | 2024 | HIGH | HIGH | ACCEPTED |
| 2 | Pentland *Honest Signals* ch. 3 | L2 | 2008 | HIGH | HIGH | ACCEPTED |
| 3 | IDTxl transfer entropy | L1 | 2023 | HIGH | MED | FALLBACK |

**Decision**: Granger primary; IDTxl if stationarity fails.

### Decision 5 — uv (not poetry/conda)

| # | Source | Level | Year | Conf | Appl | Status |
|--|--|--|--|--|--|--|
| 1 | uv docs (Astral) | L1 | 2024 | HIGH | HIGH | ACCEPTED |
| 2 | poetry docs | L1 | 2024 | HIGH | MED | REJECTED R7 |
| 3 | conda-forge mediapipe lag | L4 | 2024 | MED | LOW | REJECTED R2 |

**Decision**: uv + pyproject.toml.

---

## §9 Evaluation Gates (must pass all 4)

**A — Methodological**: EBSE evidence trail on top-5 decisions · Dockerised `make reproduce` passes · BagIt validates · every figure traces to parquet + video_id.

**B — Scientific**: E(t) discriminates regimes d ≥ 0.5 on ≥ 2 sub-indices · null-model |z| > 2 on ≥ 1 network metric · ≥ 1 honestly-reported negative result.

**C — Stakeholder**: 1 Hacker deliverable (influence graph) · 1 Gloor deliverable (alchemical HS diagram).

**D — Aesthetic**: dashboard demo ≤ 60 s · paper satisfies both profs.

---

## §10 Risk Register

| # | Risk | P | I | Mitigation | Trigger |
|---|---|---|---|---|---|
| R1 | Tier-0 URL list never arrives | M | H | Tier-1 self-sourced covers space | No reply Apr 22 09:00 |
| R2 | YouTube ToS / throttling | M | M | Rotate UA; rate-limit 1/30s; auditable manifest | HTTP 429 |
| R3 | MediaPipe head-sway invalid | H | M | Primary = trunk (V1); head = Secondary | Calibration r<0.7 |
| R4 | Audio pipeline >12 h on 150 videos | M | H | Chunk parallelism; skip silent; cache stems | >12 h observed |
| R5 | Kumaran onboarding lag | H | M | Ramp plan + Zuraiz pairing Wks 1–2 | Missed May 22 gate |
| R6 | Dashboard over-engineering | M | M | Freeze Jun 21; 60 s rule | Hassan >20 h/w on polish |
| R7 | Paper bottleneck | M | H | Figures paper-first; skeleton May 15 | No draft by Jun 30 |
| R8 | Scope creep (empirical) | M | M | E1–E5 literature-only | Proposal to run GEQ |
| R9 | Tier 2 corpus too small for H1 | M | H | Tier 3 injection × 4 regimes × 3 seeds = 12× multiplier | N < 30 after Tier 3 |
| R10 | Cuesta 2020 multi-f0 install friction | L | L | Stretch only; not critical path | >2 days stuck |

---

## §11 Obsidian Vault Update Plan

**New wiki pages** (Rule 1: ≥ 3 pages per ingest):

| Path (relative to `onsidian vault/OSN-M/`) | Stage | Created |
|---|---|---|
| `wiki/Project_8_MOC.md` | Rubedo | **Apr 17 (today)** |
| `wiki/concepts/entanglement_index.md` | Citrinitas | **Apr 17 (today)** |
| `wiki/concepts/data_sourcing_policy.md` | Citrinitas | **Apr 17 (today)** |
| `wiki/sources/cybernetic_alchemy_complete_pdf.md` | Nigredo | Apr 18 |
| `wiki/entities/Alex_Pentland.md` | Albedo | Apr 18 |
| `wiki/concepts/honest_signals.md` | Citrinitas | Apr 18 |
| `wiki/concepts/coin_framework.md` | Citrinitas | Apr 18 |
| `wiki/sources/hacker_url_list.md` | Nigredo | Apr 21 (on receipt) |
| `wiki/sources/dagstuhl_choirset.md` | Nigredo | May 1 |
| `wiki/sources/esmuc_choral.md` | Nigredo | May 1 |
| `wiki/concepts/feature_schema.md` | Citrinitas | May 8 |
| `wiki/sources/cairns_2024_thesis.md` | Nigredo | May 8 |
| `wiki/entities/{Alan_Cuesta,Christof_Weiss,Sebastian_Rosenzweig}.md` | Albedo | May 1–8 |
| `wiki/concepts/pose_validity.md` | Citrinitas | May 22 |
| `wiki/concepts/network_null_model.md` | Citrinitas | May 31 |

**Graph-linking rule**: every concept page backlinks to ≥ 2 source digests, ≥ 1 entity, `Project_8_MOC`. Verified via Obsidian graph view at each LINT cycle (5-ingest cadence).

**Git commit sequence** (Conventional Commits):

1. `feat(plan): Project 8 deep implementation plan v2.1 + vault MOC`
2. `feat(scaffold): uv pyproject + repo skeleton + CI`
3. `feat(vault): ingest Cybernetic Alchemy PDF + 4 wiki pages`
4. `feat(data): sourcing policy + Tier-2 loaders`
5. `feat(audio): librosa feature pipeline A1–A5`
6. `feat(video): MediaPipe pose pipeline V1, V3`
7. `feat(network): Granger influence graph + null model`
8. `feat(integration): Entanglement Index E(t)`
9. `feat(dashboard): FastAPI + React scrubber`
10. `docs(paper): v1 draft`
11. `chore(release): v1.0 final`

---

## §12 Critical Files to Modify

**Replace**: this file (`implementation_plan.md`) — done in commit 1.

**Create (repo root)**:

- `pyproject.toml` · `uv.lock` · `Makefile` · `Dockerfile` · `.github/workflows/ci.yml`
- `choir_entanglement/__init__.py` + subpackages `ingest/`, `audio/`, `video/`, `network/`, `integration/`, `latency_injection/`
- `tests/`

**Create (vault)**: 15 wiki files per §11 table.

**Preserve untouched**: `CLAUDE.md` files · `Claude_Code_Project_8_Context.md`.

**Existing reusable utilities**: none — project is 0% code.

---

## §13 Verification (end-to-end)

1. **Scraper dry-run**: `uv run yt-dlp --simulate --print "%(id)s %(license)s" <3 URLs>` → license field populated.
2. **Librosa smoke**: `python -c "import librosa; y,sr=librosa.load(librosa.ex('trumpet')); print(librosa.onset.onset_detect(y=y,sr=sr)[:10])"`.
3. **MediaPipe Win11 install**: `uv pip install mediapipe==0.10.14 && python -c "import mediapipe as mp; print(mp.solutions.pose.Pose())"`.
4. **Granger smoke**: `python -c "from statsmodels.tsa.stattools import grangercausalitytests; import numpy as np; grangercausalitytests(np.random.randn(100,2), maxlag=3, verbose=False)"`.
5. **Vault graph**: Obsidian graph view → `Project_8_MOC` has ≥ 8 edges after Apr 24.
6. **Docker**: `docker build -t choir . && docker run --rm choir make smoke` < 5 min.
7. **CI**: push to `main` triggers lint + pytest + mypy.
8. **BagIt**: `bagit.py --validate results/` passes at each tag.

---

## §14 DSP Reality Correction (v2.1 transparency)

External review (Gemini 3.1 Pro, 2026-04-17) flagged that v2.0 misapplied DSP expectations:

1. **Demucs v4** separates *instrument classes*, not individual singers in a vocal mix.
2. **`librosa.pyin`** is strictly monophonic — garbage on polyphonic choir audio.
3. Therefore **Tier 1 YouTube cannot yield per-singer pairwise audio or Granger-causal onset networks.**

**v2.1 response**:

- Tier 1 → Visual-Primary + ensemble-acoustic descriptive.
- H1 → Tier 3 controlled latency injection on Tier 2 multitrack (strictly *better* science — known ground truth, paired within-piece).
- H2 → Tier 2 + Tier 3 only.
- H3 → Tier 1 large-N visual + Tier 2 audio ground truth.
- Self-recording remains forbidden per original user instruction; Option C rejected on user-preference grounds.
- Multi-f0 SATB estimation (Cuesta/Gómez/Bittner 2020, ISMIR) kept as Tier 1 stretch for per-section F0.

**Why this is a feature, not a bug**: forcing H1 to Tier 3 gives falsifiability no natural YouTube corpus could — we *know* the injected latency profile. Aligns with Hacker's empirical-rigor standards.
