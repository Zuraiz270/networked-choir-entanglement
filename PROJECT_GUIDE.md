# Project 8 — Networked Choir Entanglement Platform

**The team guide · v1.1 · drafted 2026-04-18 · last-updated 2026-04-24**

> Team-facing master document. If you are on the team, read sections 1–10 before anything else. Section 11 is a technical reference — skim only if you need a formula or a library decision.

> **v1.1 changelog (2026-04-24):** 27/27 primary and secondary sources deep-read re-ingested against PDFs; Citrinitas and Rubedo concept pages cascaded; Rule-2 LINT applied. Full audit log at `onsidian vault/OSN-M/wiki/00_overview/deep_read_audit.md`. Surgical edits in §4, §11.1, §11.4, §12.

---

## 1. TL;DR

We are building a tool that measures **how well people are coordinating when they sing together over the internet**. We will test it on 20 to 30 hand-curated virtual-choir videos (visual signals, no post-produced content) and a handful of academic multi-microphone recordings (audio plus network signals, which is where our latency conclusions actually come from). By **July 17**, we deliver: a working piece of software, a paper, and a live 20-minute presentation with a 60-second demo. Supervisor: Prof. Janine Hacker (Uni Bamberg). Second grader: Prof. Peter Gloor (Uni Köln / ex-MIT).

---

## 2. The Real Problem We're Solving

**Everybody felt it during COVID. Nobody measured it.**

Millions of people sang together over Zoom, over YouTube-collab videos, over low-latency tools like SoundJack and Jamulus. Every one of them felt the difference between "this feels like being in a room together" and "this is fighting against the network." A human listener can hear that a Zoom choir sounds *off* compared to an in-person one. But there is **no number** that says *coordination collapsed at latency X*. No benchmark. No objective metric.

Without that number, NMP tool developers (SoundJack, Jamulus, Jacktrip) design by intuition, music educators plan remote programs by anecdote, and researchers can't compare one setup against another. **We are building that number.**

**Why choirs — not meetings, not Slack.** Coordination science mostly runs on meetings, negotiations, and speed-dating — soft settings where *"did they coordinate well?"* is a judgment call. Did the deal close? Did they click? Choirs are different. The outcome is **acoustically measurable**: two singers either hit the same note at the same moment, or they didn't — the recording shows it in milliseconds. Choir video is to coordination science what Drosophila is to genetics: a clean, high-signal, low-cost natural laboratory. That lets us test Pentland's *Honest Signals* theory (MIT 2008) against an *objective* coordination outcome for the first time.

**The binary we're actually testing.** Is latency a hard ceiling on human coordination, or do bodies compensate? Two answers — both matter:

- **Hard ceiling.** If coordination collapses below a clear latency threshold and bodies can't make up for it, NMP tools need **fundamentally new architectures, not better codecs, but predictive models that compensate for the ceiling itself. Public money spent on remote-music-education programs is either well-spent (under the threshold) or largely wasted (over it).
- **Bodies compensate.** If visual cues (posture, breath, micro-sway) let singers coordinate through latencies that should theoretically break them, Honest Signals theory gets its cleanest external test, and the design lesson flips: **remote-collaboration tools should prioritise visual channel fidelity over audio latency**. That transfers to remote surgery, teleoperated robotics, distributed gaming — any setting where people have to move together in time without being in the same room.

Either finding is publishable. Either finding reshapes a real field.

**What we build, concretely.** A system that takes a choir video as input and outputs a set of numbers describing how tightly the singers are coordinating — their timing, their body movement, their breathing, who is leading whom. We call this composite measurement an **Entanglement Index**, E(t). We test whether it distinguishes Zoom-class from SoundJack-class sessions.

**The two lenses we must honour:**

- **Gloor's lens (COINs / Honest Signals):** online choirs *are* Collaborative Innovation Networks expressing themselves through voice. We must produce one "alchemical-stage" diagram showing raw → refined signal.
- **Hacker's lens (virtual-team trust):** latency and leader-follower visibility either enable or inhibit engagement. We must produce one publication-quality **directed influence graph** showing who-leads-whom in a choir.

## 2.5 The Meta-Level: COINs Methodology Integration

The seminar requires us to treat our own team as a COIN (Collaborative Innovation Network). We are not just observing entanglement in choirs; we are measuring our own entanglement as a team to achieve "groupflow." 

**What this means for our workflow:**
- **Virtual Mirror (May 21)**: We will export our team's WhatsApp group chat and run it through the SocialCompass tool.
- **Five Archetypes**: We will analyze whether our team consists of Bees, Ants, Butterflies, Capybaras, or Leeches.
- **Scope Exclusion Acknowledgment**: While the official project description allows for "qualitative interviews," we have explicitly scoped this out (see §8) due to ethical and logistical constraints, focusing purely on objective audio-visual indicators.

---

## 3. Glossary — Terms You'll Need

Every technical word used in sections 1–10 is explained once here. Keep this open on a second screen the first time you read the doc.

| Term                                   | Plain meaning + analogy                                                                                                                                                                                                                                                    |
| :------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Entanglement / E(t)**          | Our composite score of how coordinated a choir is at time t. Think of it like a credit score, but for togetherness. Ranges continuously; we z-score it against a random baseline.                                                                                          |
| **Coupling**                     | A weaker word for "are these two things moving together?" — e.g. if soprano F0 and alto F0 rise together, they are coupled.                                                                                                                                               |
| **Onset**                        | The exact moment a note starts. If we give 10 singers the same sheet music, their onsets of note #1 should all line up — do they?                                                                                                                                         |
| **Pitch / F0**                   | The fundamental frequency of a voice (how high or low it sounds). Soprano high F0, bass low F0.                                                                                                                                                                            |
| **Tempo**                        | How fast the music goes, in beats per minute.                                                                                                                                                                                                                              |
| **Latency**                      | The lag between singing a note and the other singers hearing it. Zoom latency: 150–400 ms (roughly half a beat out). SoundJack latency: 20–60 ms (close to being in the same room). Analogy: talking on a walkie-talkie (Zoom) vs. talking in the same room (SoundJack). |
| **RTT (Round-Trip Time)**        | How long it takes for a packet of audio to go from you to someone else and back. Latency ≈ RTT / 2.                                                                                                                                                                       |
| **Jitter**                       | How*variable* the latency is. Constant 100 ms of lag is manageable; 100 ms that jumps to 500 ms randomly destroys timing.                                                                                                                                                |
| **Packet loss**                  | Pieces of the audio stream that just don't arrive. The listener hears silence or glitches.                                                                                                                                                                                 |
| **Zoom-class / NMP / SoundJack** | Zoom-class = consumer video tools, high latency. NMP (Networked Music Performance) = purpose-built low-latency tools. SoundJack and Jamulus are the main NMP platforms.                                                                                                    |
| **Pose estimation**              | Software that locates body joints (shoulders, elbows, hips) in a video frame.                                                                                                                                                                                              |
| **MediaPipe**                    | Google's open-source pose + face detection library. We use it to extract body coordinates per frame.                                                                                                                                                                       |
| **FaceMesh**                     | MediaPipe's face detector — gives 468 points around the face (lips, eyes, jaw). We use lip points to measure mouth opening.                                                                                                                                               |
| **DTW (Dynamic Time Warping)**   | A way of asking "how similar are these two audio signals if I allow one to be stretched or compressed in time?" Analogy: matching two recordings of the same speech even if one speaker talks slower.                                                                      |
| **pyin**                         | A Python audio library function that extracts F0 (pitch) from a*single-voice* recording. **Important limitation: it only works on one voice at a time**, not choirs.                                                                                               |
| **Demucs**                       | A neural-network audio separator that splits mixed music into vocals / drums / bass / other.**Important limitation: it separates *instruments*, not *individual singers within a vocal mix*.**                                                                   |
| **Stereo mixdown**               | A single 2-channel audio file where all singers are mixed together. What YouTube gives us.                                                                                                                                                                                 |
| **Multitrack**                   | Separate audio file per singer (one file per microphone). What academic datasets give us.                                                                                                                                                                                  |
| **Granger causality**            | A statistical test. If knowing X's past helps predict Y's future (beyond Y's own past), we say*X Granger-causes Y*. In a choir: if sopranos start notes a fraction early and altos reliably follow, sopranos Granger-cause altos.                                        |
| **Directed influence graph**     | A diagram with an arrow from X to Y if X Granger-causes Y. Hacker's deliverable.                                                                                                                                                                                           |
| **Centrality**                   | A graph metric. A node with high centrality is "central" — many others depend on it. In a choir: the singer everyone follows.                                                                                                                                             |
| **Modularity**                   | A graph metric. High modularity = clear sub-groups within the whole. In a choir: the SATB sections forming separate clusters.                                                                                                                                              |
| **Null model**                   | A random baseline we compare against. We shuffle our data 200 times, compute the same metric each time, then check whether our real-data metric is unusual relative to the shuffled distribution. Without a null model, any number looks meaningful.                       |
| **BagIt**                        | A file-packaging standard that attaches checksums to every data file, so we can prove nothing was corrupted or swapped.                                                                                                                                                    |
| **yt-dlp**                       | A command-line tool that downloads YouTube videos and their metadata. Open-source successor to youtube-dl.                                                                                                                                                                 |
| **SHA-256**                      | A cryptographic fingerprint. Two files have the same SHA-256 if and only if they are bit-identical. We store it per downloaded video to prove provenance.                                                                                                                  |
| **SATB**                         | Soprano / Alto / Tenor / Bass. The four standard choir voice sections.                                                                                                                                                                                                     |
| **Honest Signals**               | Pentland's term (MIT 2008) for the unconscious body-language, timing, and vocal-rhythm cues humans emit during collaboration. Measurable, predictive, mostly involuntary.                                                                                                  |
| **COIN**                         | Collaborative Innovation Network (Gloor, Oxford 2005). A distributed group self-organising toward a shared creative goal.                                                                                                                                                  |
| **EBSE**                         | Evidence-Based Software Engineering. Every technical decision we make must be backed by documented evidence (papers, standards, docs) with a stated confidence level. Enforced by the top-level CLAUDE.md.                                                                 |

---

## 4. Where We Are Today (2026-05-21)

**Concrete status**, no spin:

- **Team**: confirmed 4 members — Zuraiz, Hammad Anwar, Hassan Ahmed, Kumaran Vasu. All at Uni Bamberg.
- **Seminar progress**: Block course (April 15–16) attended. Chapter 14 presentation delivered Apr 16. Iteration 1 status meeting held Apr 16.
- **Code**: scaffold landed 2026-04-25 on the `scaffold` branch. `pyproject.toml` with WP-scoped deps, `uv.lock` (166 packages, numpy 1.26.4 across Win+Linux), GitHub Actions CI on `ubuntu-22.04` (apt-installed ffmpeg + libgl + libglib), 3 canary smoke tests, `Makefile`, pre-commit hooks. **Docker dropped from scaffold** (over-engineered for a semester project; uv.lock + winget host setup gives the same reproducibility). `py-feat==0.6.2` deferred to WP2 sub-plan (nltools/numpy conflict, tracked as L-H-9). **All 4 WPs shipped Sprint-2 milestones (2026-05-17)**: WP1 audio (`src/choir_entanglement/audio/{pipeline,coupling}.py` — pyin F0 + onsets + RMS, pairwise A(t)); WP2 video (`src/choir_entanglement/video/{schema,pose}.py` — MediaPipe Pose + FaceMesh + derived shoulder_rise/head_sway/trunk_lean); WP3 network (`src/choir_entanglement/network/{granger,influence_graph}.py` — circular-shift null, NetworkX DiGraph); WP4 frontend (`frontend/{wireframe.md,README.md}` — dashboard design doc). 15/15 smoke tests pass, ruff clean, mypy strict clean. Demo scripts under `scripts/wp{1,2,3,4}_*.py`. **Sprint-3 Phase A (2026-05-22)**: WP1 scaled across all 25 Dagstuhl musical takes via `scripts/wp1_dagstuhl_batch.py` (resumable, canonical mic per singer DYN>HSM>LRX). 130 newly-extracted singer parquets + 288 pairwise couplings; corpus summary at `data/processed/dagstuhl/_summary.csv`. **Sprint-3 Phase B (2026-05-22)**: WP3 scaled to 5 Dagstuhl pieces × 2 methods (standard Granger + COP-GC via Zanin-2021 ordinal-pattern transform) via `scripts/wp3_dagstuhl_batch.py`; per-piece GEXFs + flat metrics at `data/processed/dagstuhl/_network_metrics.csv`; 2x3 grid figure at `data/figures/wp3_influence_graphs_5pieces.png`. Tests now 18/18 (+3 for COP-GC). **Sprint-3 Phase C (2026-05-22)**: WP2 pose batched across 10 Tier-1 videos (stratified by NMP regime) via `scripts/wp2_tier1_batch.py`; per-video quality summary at `data/processed/tier1/_pose_summary.csv` (5/10 pass 50% pose-detection floor — the documented "try and iterate" outcome from Status Meeting III); v2 V(t) figure at `data/figures/wp2_visual_features_v2.png`. **Sprint-3 Phase D (2026-05-22)**: (D1) WP4 dashboard scaffold — React 18.3 + Vite 5.3 + TS strict + D3 7.9 + Plotly 2.33 at `frontend/` plus FastAPI 0.111 backend at `src/choir_entanglement/dashboard/app.py` (3 mock endpoints). 4-panel layout (video / influence graph / E(t) timeline / metadata) verified end-to-end via Playwright screenshot at `data/figures/wp4_dashboard_scaffold.png`. (D2) E(t) integration at `src/choir_entanglement/entanglement.py` with NaN-aware weight reallocation (no single piece in our corpus has all three signals natively) and 200-shuffle circular-shift null. `scripts/et_demo.py` on LI_QuartetA_Take02 (A+N only, V=NaN): mean E = 0.744, null mean 0.573 ± 0.008, p_null = 0.0000; figure at `data/figures/et_timeline_LI_QA_Take02.png`. Tests now 23/23 (+5 entanglement).
- **Data**: **Tier-2 Dagstuhl on disk 2026-05-17** (5.1 GB, MD5 verified vs Zenodo). **Tier-1 corpus manifest** at `data/tier1_corpus_manifest.csv` (29 verified + downloaded + SHA-256 hashed URLs in Hacker schema as of 2026-05-19, 4 Hacker seeds re-confirmed + 25 new; stratification 11 Jamulus / 5 Jamulus+Zoom / 4 SoundJack / 9 Zoom-only). 1.3 GB of Tier-1 mp4s under `data/raw/tier1/` (gitignored), held for Sprint-3 WP2 pose extraction. **Per-singer feature parquets for all 25 Dagstuhl musical takes (LI Basses/QuartetA/QuartetB/FullChoir + TP QuartetA/FullChoir)** at `data/processed/dagstuhl/{take_id}/*.parquet` (gitignored); corpus-level pairwise-coupling summary at `data/processed/dagstuhl/_summary.csv` (tracked). **WP3 derived artefacts (Sprint-3 Phase B)**: 10 directed influence graphs at `data/processed/dagstuhl/{take_id}/influence_graph_{standard,cop_gc}.gexf` (5 pieces × 2 methods, Gephi-compatible) plus the flat per-piece metrics table at `data/processed/dagstuhl/_network_metrics.csv`. **Virtual Mirror data captured 2026-05-18** (SC Chat Analyzer outputs at `data/sc chat analyzer/`, 3 cropped views under `cropped/`).
- **Scope (post-Status-Meeting-III, 2026-05-21)**: Confirmed as **semester project with internal seminar report**, not peer-reviewed paper. Consequence: DPIA / DPO sign-off NOT required for Tier-1 extraction; arXiv jurisdiction question is moot; publication-venue decisions out of scope. Reproducibility hygiene (SHA-256, uv.lock, parquet schemas) remains in scope for the report. See [[status_meeting_3_outcome]] in vault for the full decision record.
- **Planning artefacts**: this guide. Vault restructured into numbered directories. 26 papers migrated into `01_primary_sources/` and `02_secondary_sources/`.
- **Evidence layer (new, 2026-04-24)**: 27 primary + secondary sources re-ingested full-text against the original PDFs, replacing the prior shallow Gemini Flash digests. Audit log at `onsidian vault/OSN-M/wiki/00_overview/deep_read_audit.md`. Concept pages ([[entanglement_index]], [[latency_thresholds]], [[limitations_register]]) cascaded to match. Rule-2 LINT applied. P-04 Pentland *Honest Signals* remains TO-ACQUIRE.
- **Blockers today**: None.
  1. Prof. Hacker's YouTube URL list is received (5 URLs from Jamulus).
  2. The Cybernetic Alchemy PDF by Prof. Gloor is in `raw/`.
- **Upcoming deadlines**:

| Date                        | What                                                                                                                                                            |
| :-------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Apr 30, 14:00 CET** ✓ done | **Hacker + Gloor joint status meeting.** Deck/script archived in commit 9f8c677. |
| **May 8** ✓ done 05-17       | First audio-pipeline milestone (delayed; SATB A(t) figure at `data/figures/wp1_satb_coupling.png`). |
| **May 21, 14:00 CET** ✓ done | **Status #3 + Virtual Mirror**. Both supervisors satisfied. Two decisions out of Q&A: (a) DPIA / DPO sign-off NOT required (semester-project scope, not peer-reviewed paper); (b) MediaPipe calibration downgrades to lightweight "try and iterate" instead of formal OpenPose study. Full outcome at `onsidian vault/OSN-M/wiki/01_project/status_meeting_3_outcome.md`. |
| **Jul 23**            | **Final 20-minute presentation.** End of project.                                                                                                                   |
| **Jul 31, 23:59**     | **Final Paper due.**                                                                                                                   |

---

## 4.5 Evidence Execution Matrix

Our 26 migrated papers must be ingested into the vault and mapped to deliverables. We triage ingestion based on the seminar timeline:

| Phase | Target Date | Papers | Focus |
|:--|:--|:--|:--|
| **1 — Scope & Method** | Apr 30 | S-02, P-11, P-14, P-12, P-09, S-03 | Define E(t), establish NMP landscape, latency thresholds |
| **2 — Data & Legal** | May 21 | P-01, P-13, P-07, P-17, S-04, P-15, P-08 | Dataset acquisition, legal framework, multimodal methods |
| **3 — Implementation** | Jun 25 | P-16, P-18, P-05, P-06, P-19, P-20, P-21, P-22, P-23, P-02, P-03 | Technique-specific papers as we code each WP |
| **4 — Paper & Final** | Jul 23 | P-10, S-01 | Discussion framing, alchemical diagram |

---

## 5. Where We Need to Be by July 17

Three concrete deliverables. In plain words:

1. **A working tool.** Give it a choir video → it outputs a set of coordination numbers + a visualisation. This is the `choir_entanglement` Python package plus a small web dashboard. A new teammate cloning the repo must be able to reproduce our results in under 15 minutes on a fresh Windows 11 laptop, using `uv run make all` inside Docker.
2. **A paper.** 8–12 pages in IEEE or LNCS format. Every claim backed by a DOI or primary citation. Must include our reproducibility appendix. Lead author: Zuraiz.
3. **A 20-minute presentation** on July 17 with a live 60-second demo of the dashboard. Ideally ≤ 10 slides.

**Plus two stakeholder-specific artefacts** that we *must* produce because each professor has asked for them in their own research language:

- **For Prof. Hacker — a directed influence graph.** One polished figure showing which singer influences which (arrows), with edge weight = strength of Granger-causality on note onsets. WP3's primary output. (Prof. Hacker's research is on engagement + trust in virtual teams — she cares about "who leads whom" topologies.)
- **For Prof. Gloor — an alchemical-stage Honest-Signals diagram.** One polished figure showing how raw signal (Nigredo) transforms through stages (Albedo → Citrinitas → Rubedo) into meaning. WP4's primary output. (Prof. Gloor's research framework is the alchemical pipeline + Pentland's Honest Signals.)

**What we will claim, specifically**, if the results support it (note on test bed: H1 and H2 are tested on Tier 2 multitrack plus Tier 3 controlled latency injection; Tier 1 YouTube serves as a visual-feature sanity check for H3, not as the latency-discrimination test bed):

- **Claim 1 (H1).** E(t) distinguishes Zoom-class from SoundJack-class performance with a statistical effect size of Cohen's d ≥ 0.5 on at least two of the three sub-scores (audio, visual, network).
- **Claim 2 (H2).** The network topology (how dense, how modular, how leader-dominated) differs between the two regimes at p < 0.05 vs. a 200-permutation null.
- **Claim 3 (H3).** Honest-Signals visual features (body sway plus breathing) add meaningfully (ΔR² ≥ 0.10) to E(t) beyond what audio alignment alone can predict.

If any claim fails, we report the failure honestly — a negative result is a valid contribution.

---

## 6. The Roadmap — Week by Week

Every deadline, in order, with the engineering-jargon stripped out.

| Date                       | What happens                                                                                             | Plain English                                                                                                                       |
| :------------------------- | :------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------- |
| **Apr 16 (done)**    | Virtual status #1                                                                               | First check-in at block course                                                                                             |
| **Apr 23 (today)**   | Vault restructuring + Core Papers Ingest                                 | Aligning with COINs 2026 official dates and method                                                  |
| **Apr 30 14:00 CET** ✓ done       | **Virtual status #2 (Hacker + Gloor)**                                                                  | **5–10 minute presentation of team, goals, plan, way-of-working, next iteration.**    |
| **May 1** ✓ (done 05-17)          | Academic multitrack datasets downloaded                                | The "Tier 2" data is on disk (Dagstuhl 5.1 GB, MD5 verified)            |
| **May 8** ✓ (done 05-17)          | Audio pipeline first milestone                                                                           | WP1 audio pipeline runs end-to-end on Dagstuhl SATB Quartet A Take 02; per-singer parquets + pairwise A(t) figure shipped |
| **May 15** ✓ (done 05-17, supplemented + hashed 05-19, 29 URLs) | YouTube corpus fully curated, downloaded, and SHA-256 hashed at 20 to 30 videos                                                         | 29 verified + hashed Tier-1 URLs in Hacker schema (4 Hacker seeds re-confirmed + 25 new). Stratification: 11 Jamulus, 5 Jamulus+Zoom, 4 SoundJack, 9 Zoom-only. 1.3 GB of mp4s held for Sprint-3 WP2. |
| **May 18** ✓ done            | **Virtual Mirror analysis** (project-level meta task)                                                   | SC Chat Analyzer applied to team WhatsApp; team archetype = Tree Hugger consensus; chat character HIGH Meaning / LOW Emotion / MEDIUM Relationship; outputs at `data/sc chat analyzer/`. |
| **May 20** ✓ done            | **May-21 deck + script + Q&A bank ready**                                                               | `OSN.pptx`, `may21_script.md` (Hammad as presenter, 10 slides, 9:15 budget), `may21_qa_prep.md` (21 Q&A entries across 3 categories). |
| **May 21 14:00 CET** ✓ done  | **Status Meeting III** (Hacker + Gloor + coordinators)                                                  | Both supervisors satisfied. Key decisions: DPIA NOT required for semester scope; MediaPipe calibration downgrades to "try and iterate"; publication scope = internal seminar report only. See [[status_meeting_3_outcome]]. |
| **May 21**           | **Virtual status #3 + Virtual Mirror**                                                                           | **WhatsApp analysis ✓ done 2026-05-18** (SC Chat Analyzer outputs at `data/sc chat analyzer/`, writeup at `virtual_mirror_sprint1.md`). Status meeting itself: Thu 14:00 CET. |
| **May 22** ✓ (10/10, done 05-22) | Video pipeline first milestone                                                                           | WP2 code extracts body/face coordinates from a Tier-1 SoundJack video (595 frames, 79.5% pose detection). **Sprint-3 Phase C scaled to 10 stratified Tier-1 videos**; 5/10 pass 50% pose-detection floor (matching the "try and iterate" decision from Status Meeting III). Summary at `data/processed/tier1/_pose_summary.csv`. |
| **May 31** ✓ (done 05-17)       | Network pipeline first milestone                                                                         | WP3 produces Hacker's directed influence graph for Dagstuhl SATB Quartet A Take 02 (11/12 significant edges at p_null < 0.05, density 0.92). |
| **Jun 4** ✓ (done 05-22)        | WP1 audio pipeline scaled to all Dagstuhl pieces                                                         | Sprint-3 Phase A. 25 musical takes batch-processed (130 newly-extracted singer parquets + 288 pairwise A(t) couplings); corpus summary at `data/processed/dagstuhl/_summary.csv`. Pulled forward 13 days from Jun-4 target. |
| **Jun 11** ✓ (done 05-22 partial) | WP3 Granger scaled to 5 Dagstuhl pieces + COP-GC variant                                              | Sprint-3 Phase B. Standard Granger + COP-GC (Zanin 2021 ordinal-pattern transform) on 5 pieces (LI QuartetA/B Take/01-02, LI FullChoir Take01, TP QuartetA/FullChoir Take01). 10 GEXFs + `_network_metrics.csv` + 2x3 grid figure at `data/figures/wp3_influence_graphs_5pieces.png`. Tests 18/18. |
| **Jun 14** ✓ (done 05-22 one-piece) | E(t) end-to-end + 200-shuffle circular-shift null + WP4 dashboard scaffold      | Sprint-3 Phase D. E(t) integration module + LI_QuartetA_Take02 single-piece demo (mean E = 0.744, p_null = 0.0000); React+Vite+FastAPI dashboard scaffold renders mock-data 4-panel layout. Pulled forward 23 days from Jun-14 brief target. Full-corpus E(t) goes to Phase E (Jun-6/7/8). |
| **Jun 11**           | **Virtual status #4**                                                          | Progress check-in                                                                                        |
| **Jun 14**           | E(t) computed on 80+ videos; null-model running                                                          | The full Entanglement Index works end-to-end                                                                                        |
| **Jun 21**           | Dashboard alpha version                                                                                  | WP4 web UI shows a video + overlays + network graph side-by-side                                                                    |
| **Jun 25**           | **Virtual status #5**                                                    | Progress check-in                                                                                                       |
| **Jun 30**           | Full pipeline on Tier 1 + Tier 2 + Tier 3 completed                                                    | We have numbers for the paper                                                                                                       |
| **Jul 7**            | Paper draft v1                                                                                           | First complete draft circulated                                                                                                     |
| **Jul 9**            | **Virtual status #6**                                                                      | Last check-in before final                                                                                                                        |
| **Jul 23**           | **Final 20-minute presentation**                                                                   | 10-12 min presentation + Q&A                                                                                                                      |
| **Jul 31, 23:59**    | **Final paper due**                                                                   | 10 to 20 pages                                                                                                                      |

---

## 7. Work Packages

The project is organised into four **work packages** (WPs). Each WP is ~180 hours over the project (the 6-ECTS × 4-members = 24-ECTS budget, roughly 30 hours/week for the active phase). Each WP in plain language, then its stack, then its single most important deliverable.

### WP1 — Lead, audio, integration, paper

WP1 owns the audio side of the project (what the choir *sounds* like — timing, pitch, onsets, tempo) and stitches the four pieces together into one running system. Also delivers the paper as first author, and gives the Apr 30 + Jul 17 presentations. This is the flagship WP because the Entanglement Index itself is the paper's central contribution, and the WP that owns it is the paper's first author.

**Stack**: Python 3.11 · `librosa` (audio analysis) · `demucs` (stem separation) · `numpy` / `scipy` / `pandas` · `uv` (package manager) · Docker.

**Most important deliverable**: the `choir_entanglement` Python package, running end-to-end via `uv run make all` on a fresh Windows 11 laptop in < 15 minutes inside Docker. Plus the paper.

### WP2 — Video / computer vision

WP2 takes each choir video frame-by-frame and extracts what each visible singer's body and face are doing — posture, upper-body sway, mouth opening, breathing (visible as shoulder rise). This produces the "V" half of the Entanglement Index.

**Stack**: Python · `mediapipe` (pose + face) · `opencv-python` (video I/O) · `py-feat` (facial action units).

**Most important deliverable**: a parquet file per video at `processed/<video_id>/pose/<singer>.parquet`, containing the per-frame body and face coordinates. Schema frozen by May 8 so that downstream WPs can build on top of it.

### WP3 — Network science (Prof. Hacker's pillar)

WP3 looks at *who is following whom* in the choir. Using per-singer audio (from academic datasets, not YouTube), it runs Granger-causality tests on the note onsets of each singer against every other singer, producing a directed graph where an arrow from A to B means "A's timing predicts B's timing." It then computes standard network metrics on this graph — density, modularity, centrality. Primary deliverable: the **publication-quality directed influence graph** that Prof. Hacker specifically wants to see.

**Stack**: Python · `networkx` (graph algorithms) · `statsmodels` (Granger causality) · `python-louvain` (community detection) · Gephi (figure polish).

**Most important deliverable**: one publication-quality SVG of a directed influence graph for a representative piece, plus the code that generates it for any new piece.

### WP4 — Dashboard, paper figures, alchemical diagram (Prof. Gloor's pillar)

WP4 builds the web-based dashboard that demonstrates the whole system visually — upload a video, see its timeline, see the singers' body coordinates overlaid, see the network graph animate over time. Also delivers all paper figures with consistent visual style (colour map, fonts). Plus the **alchemical-stage Honest-Signals diagram** that Prof. Gloor specifically wants to see — one polished figure showing raw signal → refined meaning through the four alchemical stages.

**Stack**: React + Vite + TypeScript + D3 + Plotly (frontend) · FastAPI + uvicorn (backend) · Tailwind CSS · Playwright (end-to-end tests).

**Most important deliverable**: a working dashboard that plays a 60-second live demo during the Jul 17 presentation without crashing.

---

## 8. The Three Data Sources, Simply

We use three tiers of data — each fills a different job. Understanding this is critical for reading the roadmap and the paper.

### Tier 1 — YouTube virtual-choir videos (target: 20 to 30, hand-curated)

**What it is.** We search YouTube for virtual-choir videos from the COVID era (March 2020 to June 2022). Queries: *"virtual choir", "zoom choir", "soundjack choir", "distributed choir COVID", "SATB virtual", "Eric Whitacre virtual choir"*, etc. We download each video and its metadata with `yt-dlp`, record its SHA-256, and keep a manifest of every video we touched.

**Inclusion rule (v2.2, 2026-04-19).** Heavily edited or post-produced content is **excluded** from the Tier 1 corpus: virtual-composite videos where each singer recorded alone against a click-track and a producer stitched the result in a DAW. The timing offset between those singers is an editorial signal, not a coordination signal (see §12 L-A-4 and L-B-10). Quality over quantity: 20 to 30 well-chosen videos beat 150 noisy ones at this sample size. If a candidate shows explicit "recorded separately" language in its description, or shows obvious lip-sync misalignment with audio on inspection, it is rejected and logged in `corpus_manifest.csv` with `rejection_reason`.

**What it's for.** The **visual half** of our analysis. YouTube gives us a large quantity of data (hundreds of real-world choirs), but the audio is a single mixed stereo track — we *cannot* separate individual singers' voices from a mix, so we cannot run per-singer audio analysis on Tier 1. We *can* analyse video (each singer is typically in their own Zoom-grid tile). So Tier 1 serves hypothesis **H3** (Honest-Signals visual features matter) and contributes descriptive ensemble-audio statistics — but not the precise audio coupling or the influence graph.

**Legal basis.** §60d UrhG (Germany's text-and-data-mining research exception) and EU DSM Directive 2019/790 Art. 3 give us statutory rights to scrape and analyse copyrighted media for non-commercial research. GDPR Art. 6(1)(f) + Art. 89 cover the personal-data angle. We never redistribute video, we only keep feature vectors long-term, and we delete mp4s after extraction. Details in section 11 / `wiki/concepts/data_sourcing_policy.md`.

**Edge case.** If YouTube rate-limits us (HTTP 429), we slow down to 1 request per 30 seconds and rotate user agents. If a video is copyright-struck, we skip it and log why in the manifest. We never download private or locked videos.

### Tier 2 — Academic multitrack recordings

**What it is.** Purpose-built research datasets where each singer was recorded on a separate microphone. Primary: **Dagstuhl ChoirSet** (Rosenzweig et al., TISMIR 2020, DOI `10.5334/tismir.48`). Also: **ESMUC Choral Singing Dataset** (Cuesta et al., Zenodo 1286570), **ChoralSynth** (synthetic SATB), **Cairns 2024 York PhD thesis** (NMP comparator data), **DUST Dataset** (packet-loss traces — access to verify by Apr 24).

**What it's for.** The **audio and network halves** of our analysis. Because each singer is on their own microphone, we can run per-singer pitch (pyin), per-pair DTW alignment, Granger-causality onset networks, and everything else that needs per-singer streams. Tier 2 serves hypothesis **H2** (network topology differs across regimes) and provides the audio ground truth for **H3**.

**Edge case.** Dagstuhl is small (a handful of pieces). The number of *natural* Zoom-vs-SoundJack pairs in Tier 2 is insufficient for the statistical power we need for H1. Which is why we need Tier 3.

### Tier 3 — Controlled latency-injection experiments

**What it is.** We take the Tier-2 multitrack recordings and *programmatically* apply network conditions to them: we delay each singer's track by a regime-characterising amount, add jitter, simulate packet loss. Four regimes:

| Regime        | Delay       | Jitter  | Packet loss |
| :------------ | :---------- | :------ | :---------- |
| SoundJack-low | 20–40 ms   | ±3 ms  | 0 %         |
| SoundJack-mid | 40–80 ms   | ±8 ms  | 0.5 %       |
| Zoom-typical  | 150–250 ms | ±30 ms | 1 %         |
| Zoom-degraded | 300–500 ms | ±60 ms | 3 %         |

Then we recompute the Entanglement Index on each synthetic version.

**What it's for.** Tier 3 is the **clean test** of hypothesis **H1** (E(t) distinguishes the regimes). Because we *know* exactly what latency profile we injected, we have perfect ground truth. This is actually better science than natural YouTube comparisons, where we can never be sure what regime a given video was actually produced under.

### What we do NOT do

- **No self-recording.** We do not record ourselves. Reason: ethics (human-subject considerations), PII management, self-selection bias. Explicitly forbidden by original user instruction at project outset.
- **No asking third-party choirs to perform for us.** Same reason.
- **No face storage beyond feature extraction.** We delete mp4 files after extracting pose + face coordinates.
- **No full questionnaires.** We reference survey instruments from published literature (Group Environment Questionnaire, NASA-TLX, Flow State Scale-2) to frame our discussion, but we do not administer them ourselves.

---

## 9. What Could Go Wrong, and What We'll Do About It

Top 7 risks. For each: *what could happen · how we'll know it's happening · what we'll do instead*.

### R1 — Prof. Hacker never replies with the URL list

- *Warning sign:* no reply by Apr 22, 09:00 CET.
- *What we do:* escalate one level (CC Prof. Gloor on a follow-up), and in parallel proceed on self-sourced YouTube search using the queries listed in §8. The Tier 1 search is not blocked on her list — her list would just save us hours of manual curation and bias.

### R2 — YouTube throttles or blocks our scraper

- *Warning sign:* HTTP 429 errors from `yt-dlp`.
- *What we do:* drop to 1 request per 30 seconds; rotate user agents; keep an auditable manifest of every attempt. If YouTube blocks us hard, we fall back to Internet Archive mirrors.

### R3 — MediaPipe's head-sway readings turn out to be unreliable for choir video

- *Warning sign:* in the WP2 calibration study (scheduled May 22), head-sway correlation vs. a reference tool drops below r = 0.70.
- *What we do:* demote head-sway from a primary feature to a secondary one, and rely on *trunk-sway* (shoulders + hips) as the primary visual coupling signal. Trunk-sway is already validated at Pearson 0.80–0.91 vs. Vicon motion capture.

### R4 — Audio pipeline runs too slowly on the full corpus

- *Warning sign:* end-to-end `make all` takes > 4 hours on the 20 to 30 curated Tier 1 videos plus Tier 2 multitrack.
- *What we do:* run Demucs stem separation in parallel across videos, skip silent regions, cache stems on disk so reruns are incremental. Fallback: swap Demucs for `librosa.effects.hpss` (harmonic-percussive separation), which is ~5× faster but lower quality.
- *v2.2 note:* risk likelihood downgraded from MED to LOW. At N = 30 (not N = 150), estimated end-to-end Demucs runtime drops from 12 to 25 h to 2 to 5 h on a single CPU. The original runtime risk was driven by the large-N assumption.

### R5 — WP2 video-pipeline milestone slips

- *Warning sign:* missed May 22 video-pipeline milestone.
- *What we do:* prototype on a single reference video first (frame-by-frame sanity check) before batch extraction. If MediaPipe pose extraction still isn't working by May 22, fall back to OpenPose (older, Docker-bundled alternative).

### R6 — Paper doesn't start early enough

- *Warning sign:* no paper skeleton by May 15.
- *What we do:* hard rule — the paper skeleton is drafted in May, before experiments finish. Figures drive the paper, not the other way around. If code work overruns, figure-first layout (WP4 output) becomes the fallback spine for the draft.

### R7 — Scope creep into doing our own empirical data collection

- *Warning sign:* discussion turns toward "let's run a Group Environment Questionnaire on a sample" or "let's record ourselves on SoundJack."
- *What we do:* firm no. Our scope is literature-plus-open-data only. We cite published survey instruments but administer zero. Self-recording was explicitly forbidden at project outset.

---

## 10. How We'll Know We Succeeded

Four evaluation gates. We have to pass all four for the project to be an A+.

- **Gate A — Methodology.** Every major decision (scraper choice, pose library, audio analysis library, causality test, package manager) has a documented evidence trail with confidence + applicability ratings (see §11.4). The full pipeline runs inside Docker on a fresh machine via `make reproduce`. Every derived artefact traces back to a raw video ID + SHA-256.
- **Gate B — Science.** The Entanglement Index distinguishes Zoom-class from SoundJack-class regimes with Cohen's d ≥ 0.5 on at least two of its three sub-indices. The null-model z-score exceeds 2 on at least one network metric. We report at least one honest negative result somewhere in the paper.
- **Gate C — Stakeholders.** One publication-quality directed influence graph exists (for Prof. Hacker). One alchemical-stage Honest-Signals diagram exists (for Prof. Gloor). Both make it into the paper and the presentation. Under the v2.2 scope cut, these are the flagship deliverables: exactly one polished figure per professor. Any additional visualisations live in the paper appendix, not the main narrative. Simpler story, clearer claim.
- **Gate D — Polish.** The dashboard demo runs in ≤ 60 seconds without crashing. The paper reads cleanly. Both professors leave the final presentation satisfied.

---

## 11. Appendix — Technical Reference

The rest of this document is dense, jargon-heavy, and **not required reading** for most team members. It is preserved here verbatim from the previous `implementation_plan.md` (v2.1) so that nothing is lost. Use §11 as a lookup when you need a specific formula, library version, or evidence trail.

### §11.1 — Entanglement Index E(t): Formulas

```
E(t) = (1/3)·A(t) + (1/3)·V(t) + (1/3)·N(t)    # equal-weight baseline; ablated
```

> **Provenance caveat (2026-04-24 deep-read):** Gloor's Entanglement formula (S-02) was **validated on email data with 7-day windows**, n=111-113 per case, Pearson r = .522-.707 where significant. Adaptation to continuous music-domain streams is a **novel domain transfer with no prior validation**. H1-H3 are the first empirical test of E(t) on music. See `onsidian vault/OSN-M/wiki/05_metrics/entanglement_index.md` and §12 L-H-5.

**A(t) — Acoustic coupling**:

```
A(t) = 0.4·(1 − DTW_cost_norm)                 # librosa.sequence.dtw
     + 0.3·mean_pairwise_F0_xcorr(|lag|<50ms)  # pyin
     + 0.3·onset_sync_kappa(50ms bins)         # Fleiss κ on onsets
```

**V(t) — Visual coupling**:

```
V(t) = 0.5·trunk_sway_xcorr(|lag|<500ms)       # MediaPipe Pose lm 11,12,23,24
     + 0.3·breath_envelope_xcorr               # shoulder-rise proxy
     + 0.2·mouth_aperture_sync                 # FaceMesh lm 13,14,78,308
```

**N(t) — Network coherence**:

```
G_t = digraph; edge i→j weight = Granger F-stat on onset-delay
      (window 10s, stride 2s, lag AIC-selected)

N(t) = 0.4·(1 − |density_dev_from_null|)
     + 0.3·inverse_Gini(eigenvector_centrality)   # → collective leadership
     + 0.3·modularity_Q(Louvain)
```

**Null model**: 200× circularly time-shuffled singer streams. E(t) reported as z against null. Circular shift preserves within-stream autocorrelation while destroying cross-stream timing — the correct null for coordination vs independent structure.

**Tier-1 degraded variant (DSP reality check)**: A(t) and N(t) both require per-singer audio streams. Tier-1 mixed-stereo YouTube cannot satisfy this; only V(t) is fully computable. On Tier 1 we substitute a reduced ensemble variant `A_ens(t)`:

```
A_ens(t) = 0.4·collective_tempo_stability
         + 0.3·global_onset_density
         + 0.3·spectral_flux_consistency
```

`A_ens(t)` feeds H3 descriptive stats only — it is **not** on the H1 discrimination path. Multi-f0 SATB estimation (Cuesta, Gómez, Bittner 2020, ISMIR) is kept as a Tier-1 stretch experiment for per-*section* F0.

### §11.2 — Metrics Catalog (tier-gated)

Tier key: **T1** = mixed-stereo YouTube (N = 20 to 30, hand-curated, no post-produced content) · **T2** = multitrack (Dagstuhl/ESMUC/ChoralSynth) · **T3** = controlled latency-injection. **P** = primary feature, **S** = secondary.

**v2.2 scope rule (2026-04-19):** E(t) weights are frozen at (1/3, 1/3, 1/3). No regime-specific reweighting, no learned weights, no extra terms. Simplicity keeps the claim defensible at this sample size; complexity without validation is not.

**Audio (11 features)**

| #   | Feature                                      | Tier       | P/S         |
| --- | -------------------------------------------- | ---------- | ----------- |
| A1  | Ensemble onset density (spectral flux)       | T1+T2+T3   | **P** |
| A2  | Pairwise DTW cost                            | T2+T3 only | **P** |
| A3  | Pairwise F0 xcorr (pyin per-singer)          | T2+T3 only | **P** |
| A3* | Per-section (S/A/T/B) multi-f0 (Cuesta 2020) | T1 stretch | S           |
| A4  | Global spectral-flux sync                    | T1+T2+T3   | **P** |
| A5  | Collective tempo variance                    | T1+T2+T3   | **P** |
| A6  | Vibrato 5–7 Hz coupling                     | T2+T3      | S           |
| A7  | Harmonic coherence                           | T2+T3      | S           |
| A8  | Pairwise breath alignment                    | T2+T3      | **P** |
| A9  | Pairwise consonant-onset drift               | T2+T3      | **P** |
| A10 | Expressivity index                           | T2+T3      | S           |
| A11 | Demucs-residual energy                       | T2+T3      | S           |

**Visual (9 features)** — all Tier 1 compatible:

V1 trunk sway xcorr **P** · V2 head sway (calibrated) S · V3 mouth aperture **P** · V4 blink sync S · V5 FFI proxy via py-feat S · V6 head-yaw coupling **P** · V7 hand-gesture mirror S · V8 gaze if face > 200 px S · V9 smile-onset sync S.

**Network (8 features)** — T2+T3 only (require per-singer streams):

N1 Granger-cause digraph **P** · N2 eigenvector/PageRank/betweenness/closeness **P** · N3 density **P** · N4 Louvain modularity **P** · N5 temporal 3-node motifs S · N6 Burt's constraint (leadership) **P** · N7 Pearson-r tie strength **P** · N8 community NMI S.

On Tier 1 we report *visual-derived tie strength*: pairwise xcorr of trunk-sway time-series = V-tie → visual-only network analogue for H3.

**Empirical** (literature-only, no self-recording):

E1 Group Environment Questionnaire (Brawley-Widmeyer 1987) · E2 Flow State Scale-2 (Jackson & Eklund 2004) · E3 NASA-TLX · E4 Post-session interview meta-coding (Cairns 2024) · E5 ~~self-reported~~ **dropped** (human subjects).

### §11.3 — Directory Discipline

```
raw/youtube/<video_id>/             # Nigredo · immutable
processed/<video_id>/stems|pose/    # Albedo
features/<video_id>.parquet         # Citrinitas
results/Et.parquet, graphs/, figures/   # Rubedo
```

Conventional Commits for all git work. Atomic branches. BagIt validation at each tagged release. No secrets in git (`.env` is ignored).

### §11.4 — EBSE Evidence Trails (top-5 architectural decisions)

#### Decision 1 — `yt-dlp` (not YouTube Data API)

| # | Source                                 | Level | Year | Conf | Appl | Status      |
| - | -------------------------------------- | ----- | ---- | ---- | ---- | ----------- |
| 1 | §60d UrhG (DE TDM research exception) | L3    | 2021 | HIGH | HIGH | ACCEPTED    |
| 2 | EU DSM Dir. 2019/790 Art. 3            | L3    | 2019 | HIGH | HIGH | ACCEPTED    |
| 3 | yt-dlp GitHub docs                     | L1    | 2024 | HIGH | HIGH | ACCEPTED    |
| 4 | YouTube Data API ToS                   | L3    | 2024 | HIGH | MED  | REJECTED R3 |

**Decision**: yt-dlp + per-video license capture. Statutory rights > platform policy.

#### Decision 2 — MediaPipe Pose (not OpenPose)

| # | Source                                    | Level | Year | Conf | Appl      | Status             |
| - | ----------------------------------------- | ----- | ---- | ---- | --------- | ------------------ |
| 1 | MediaPipe Pose docs (Google)              | L1    | 2024 | HIGH | HIGH      | ACCEPTED           |
| 2 | Pearson r 0.80–0.91 vs Vicon (limb only) | L2    | 2022 | HIGH | MED       | ACCEPTED w/ caveat |
| 3 | OpenPose (CMU)                            | L1    | 2021 | HIGH | LOW (Win) | REJECTED R7        |

**Decision**: MediaPipe primary; head-sway calibration mandatory (WP2 May 22 study).

#### Decision 3 — librosa DTW + pyin

| # | Source                                       | Level | Year | Conf | Appl      | Status   |
| - | -------------------------------------------- | ----- | ---- | ---- | --------- | -------- |
| 1 | librosa docs                                 | L1    | 2024 | HIGH | HIGH      | ACCEPTED |
| 2 | Dagstuhl ChoirSet TISMIR (10.5334/tismir.48) | L2    | 2020 | HIGH | HIGH      | ACCEPTED |
| 3 | CREPE neural F0                              | L2    | 2018 | HIGH | MED (GPU) | DEFERRED |

**Decision**: librosa pyin primary; CREPE ablation only if we have GPU time.

#### Decision 4 — Granger causality primary (COP-GC secondary, transfer entropy fallback)

| # | Source                                                   | Level | Year | Conf | Appl | Status                               |
| - | -------------------------------------------------------- | ----- | ---- | ---- | ---- | ------------------------------------ |
| 1 | statsmodels docs                                         | L1    | 2024 | HIGH | HIGH | ACCEPTED                             |
| 2 | Pentland *Honest Signals* ch. 3                          | L2    | 2008 | HIGH | HIGH | ACCEPTED                             |
| 3 | Zanin 2022 (P-22) Augmented Granger via Ordinal Patterns | L2    | 2022 | HIGH | MED  | ACCEPTED (implemented Sprint-3 Phase B 2026-05-22; `method="cop_gc"` in `granger.py`) |
| 4 | IDTxl transfer entropy                                   | L1    | 2023 | HIGH | MED  | FALLBACK                             |

**Decision**: Granger primary + P-22 COP-GC secondary (run both and compare, per Zanin's explicit recommendation since ordinal-pattern GC captures non-linear coupling that standard GC misses); IDTxl if stationarity tests fail on > 30 % of windows.

#### Decision 5 — `uv` (not poetry / conda)

| # | Source                    | Level | Year | Conf | Appl | Status      |
| - | ------------------------- | ----- | ---- | ---- | ---- | ----------- |
| 1 | uv docs (Astral)          | L1    | 2024 | HIGH | HIGH | ACCEPTED    |
| 2 | poetry docs               | L1    | 2024 | HIGH | MED  | REJECTED R7 |
| 3 | conda-forge mediapipe lag | L4    | 2024 | MED  | LOW  | REJECTED R2 |

**Decision**: uv + `pyproject.toml` + lockfile committed.

### §11.5 — Verification Smoke Tests (end-to-end)

1. **Scraper dry-run**: `uv run yt-dlp --simulate --print "%(id)s %(license)s" <3 URLs>` → license field populated.
2. **Librosa smoke**: `python -c "import librosa; y,sr=librosa.load(librosa.ex('trumpet')); print(librosa.onset.onset_detect(y=y,sr=sr)[:10])"`.
3. **MediaPipe Win11 install**: `uv pip install mediapipe==0.10.14 && python -c "import mediapipe as mp; print(mp.solutions.pose.Pose())"`.
4. **Granger smoke**: `python -c "from statsmodels.tsa.stattools import grangercausalitytests; import numpy as np; grangercausalitytests(np.random.randn(100,2), maxlag=3, verbose=False)"`.
5. **Vault graph**: Obsidian graph view → `Project_8_MOC` has ≥ 8 edges after Apr 24.
6. **Fresh-clone smoke (replaces former Docker round-trip, 2026-04-25)**: from a fresh clone, `uv sync --frozen --all-extras && make smoke` completes < 12 min cold cache, < 90 s warm. No container required for this academic semester project; reproducibility lives in `uv.lock` plus the documented host prerequisites (`uv` + `make` + `ffmpeg`).
7. **CI**: push to `main` triggers lint + pytest + mypy on `ubuntu-22.04` with system `ffmpeg`/`libgl1` installed via apt.
8. **BagIt**: `bagit.py --validate results/` passes at each tag.

### §11.6 — DSP Reality Correction (v2.1 transparency)

External review (Gemini 3.1 Pro, 2026-04-17) flagged that the v2.0 plan misapplied DSP expectations:

1. **Demucs v4** separates *instrument classes* (vocals / drums / bass / other), not individual singers within a vocal mix.
2. **`librosa.pyin`** is strictly monophonic — returns garbage on polyphonic choir audio.
3. Therefore **Tier 1 YouTube cannot yield per-singer pairwise audio features or Granger-causal onset networks.**

**v2.1 response** (retained here):

- Tier 1 → Visual-Primary + ensemble-acoustic descriptive only.
- H1 → Tier 3 controlled latency injection on Tier 2 multitrack (strictly *better* science — known ground truth, paired within-piece).
- H2 → Tier 2 + Tier 3 only.
- H3 → Tier 1 large-N visual + Tier 2 audio ground truth.
- Self-recording remains forbidden per original user instruction.
- Multi-f0 SATB estimation (Cuesta/Gómez/Bittner 2020, ISMIR) kept as Tier 1 stretch for per-section F0.

Forcing H1 to Tier 3 gives falsifiability no natural YouTube corpus could — we *know* the injected latency profile. This aligns with Hacker's empirical-rigor standards.

### §11.7 — Obsidian Vault Integration

Project-specific wiki pages (rooted at `onsidian vault/OSN-M/wiki/`) are structured into numbered physical folders to align with the OSN-M master architecture, while retaining alchemical stages in frontmatter metadata:

- `00_overview/` — Maps of Content (e.g. `Project_8_MOC.md`) and high-level synthesis
- `01_project/` — Core definitions, constraints, team profiles
- `02_research_questions/` — Citrinitas-level abstractions
- `03_models/` — Architecture, landscape, conceptual boundaries
- `04_datasets/` — Source inventories and dataset specifications
- `05_metrics/` — E(t) definition, tool specifics (e.g. huSync)
- `06_failure_modes/` — Latency thresholds, legal policies (e.g. data sourcing)

Full vault operating protocol in `onsidian vault/OSN-M/CLAUDE.md`. Rules: Rule 1 (≥ 3 pages touched per ingest), Rule 2 (LINT every 5 ingests). Maintained by the LLM against the `raw/` source repository.

### §11.8 — Stack Versions (pinned)

- Python 3.11.9
- librosa 0.10.2 · demucs 4.0.1 · numpy 1.26.4 · scipy 1.13.1 · pandas 2.2.2 · pyarrow 16.1.0
- mediapipe 0.10.14 · opencv-python 4.10.0.84 · ffmpeg-python 0.2.0 · py-feat 0.6.2
- networkx 3.3 · statsmodels 0.14.2 · python-louvain 0.16 · teneto 0.5.3 · scikit-learn 1.5 · Gephi 0.10.1 · matplotlib 3.9
- React 18.3 · Vite 5.3 · TypeScript 5.5 · d3 7.9 · visx 3.11 · Plotly 2.33 · FastAPI 0.111 · uvicorn 0.30 · Tailwind 3.4 · Playwright 1.45
- uv 0.4.x · pytest 8.2 · ruff 0.5 · mypy 1.10 · pre-commit 3.7 · Docker 26

---

## 12. Limitations Register

Auditable EBSE inventory of everything that can undermine H1–H3 or Gates A–D (§10). Each entry is **specified** (what breaks), **rated** for severity, and either **mitigated** (concrete action + owner + date) or **escalated** (context + verbatim search queries Zuraiz can paste into Google Scholar / arXiv / SSRN). Supersedes §9 Risks for technical/statistical/legal concerns; §9 remains the team-facing risk-prose.

**Totals**: 64 limitations across 9 categories · 44 Mitigated · 6 Escalated · 8 Open · 1 Accepted · 5 Resolved · 22 newly-introduced beyond v1.0 (flagged `★`). v1.1 adds deep-read cascade entries (L-H-5..L-H-8) and scaffold finding L-H-9.

### §12.0 Executive Heat-Map

Legend — **Likelihood** (L / M / H) × **Impact** (H1 / H2 / H3, or Gate A / B / C / D). Entries in HIGH-impact cells are the ones that can kill a hypothesis or a gate if left unmanaged.

| Impact ↓ · Likelihood →            | LOW                                                           | MED                               | HIGH                |
| :------------------------------------ | :------------------------------------------------------------ | :-------------------------------- | :------------------ |
| **H1 — regime discrimination** | L-C-10, L-H-7 ★                                              | L-A-4, L-B-7, L-C-4, L-H-6 ★      | L-C-5, L-C-7, L-C-8 |
| **H2 — network topology**      | L-C-2, L-C-9                                                  | L-A-10, L-C-1, L-D-5              | L-C-6               |
| **H3 — Honest-Signals ΔR²**  | L-B-5, L-B-8, L-B-9                                           | L-A-3, L-B-4, L-D-4               | L-B-3               |
| **Gate A — Methodology**       | L-A-5, L-A-6, L-A-7, L-A-8, L-H-8 ★                          | L-H-3                             | L-E-3, L-F-5        |
| **Gate B — Science**           | —                                                            | L-D-7, L-D-8, L-B-10, L-H-5 ★     | L-E-1               |
| **Gate C — Stakeholders**      | L-G-1, L-G-3, L-G-4                                           | L-D-1, L-E-2                      | L-G-2               |
| **Gate D — Polish**            | L-A-9, L-B-1, L-B-2, L-B-6, L-D-2, L-D-3, L-D-6, L-F-6, L-H-4 | L-F-4, L-F-7, L-F-8, L-H-1, L-H-2 | —                  |

**Coverage completeness** — every prior open question is indexed below (Verification Rule 1):

| Prior source                       | Item                       | Register entry                                  |
| :--------------------------------- | :------------------------- | :---------------------------------------------- |
| §9                                | R1–R7                     | L-D-1, L-D-2, L-B-1, L-A-9, L-F-1, L-F-2, L-F-3 |
| §11.6                             | Demucs / pyin / Tier-1 DSP | L-A-1, L-A-2                                    |
| `entanglement_index.md` §7 Q1   | A_ens reporting            | paper-drafting — out of register               |
| `entanglement_index.md` §7 Q2   | pose-validity study        | L-B-1, L-B-3                                    |
| `entanglement_index.md` §7 Q3   | Granger stationarity       | L-C-1                                           |
| `data_sourcing_policy.md` §9 Q1 | DUST licence               | L-D-5                                           |
| `data_sourcing_policy.md` §9 Q2 | ChoralSynth Tier-3 scale   | L-C-3                                           |
| `data_sourcing_policy.md` §9 Q3 | §60d UrhG foreign repo    | L-E-2                                           |
| `Project_8_MOC.md` Open Q1       | Hacker URL list            | L-D-1                                           |
| `Project_8_MOC.md` Open Q3       | DUST access                | L-D-5                                           |
| `Project_8_MOC.md` Open Q4       | Cuesta 2020                | L-A-3                                           |

---

### §12.1 Audio / DSP (10)

| ID                  | Title                                                        | Severity    | Status    | Action · Owner · Date                                                           |
| :------------------ | :----------------------------------------------------------- | :---------- | :-------- | :-------------------------------------------------------------------------------- |
| L-A-1               | Demucs separates instrument classes, not singers             | H × H3     | Resolved  | See §11.6; Tier-1 off A(t) primary path                                          |
| L-A-2               | `pyin` is monophonic                                       | H × H3     | Resolved  | See §11.6;`A_ens(t)` substitution                                              |
| **L-A-3 ★**  | Cuesta 2020 multi-f0 per-voice accuracy not scale-validated  | M × H3     | Escalated | See details below                                                                 |
| **L-A-4 ★**  | **Virtual choirs are post-synchronised in production** | M × H1/H3  | Mitigated | `post_aligned_flag` in manifest + paper caveat · Zuraiz · 2026-05-15          |
| L-A-5               | DTW norm across unequal-duration pieces                      | L × Gate A | Mitigated | Müller 2015 ch.4 path-length norm · WP1 · 2026-05-08                           |
| L-A-6               | Onset detection on sustained-vowel audio                     | L × Gate A | Mitigated | Spectral-flux low threshold + consonant-onset fallback · WP1 · 2026-05-08       |
| L-A-7               | Vibrato 5–7 Hz contaminates F0 xcorr                        | L × Gate A | Mitigated | 3-Hz Butterworth LPF on F0 before xcorr · WP1 · 2026-05-08                      |
| L-A-8               | Fleiss κ bin-size choice                                    | L × Gate A | Mitigated | 25 / 50 / 100 ms sensitivity ablation · WP1 · 2026-06-14                        |
| L-A-9               | Demucs CPU runtime on N = 20 to 30 (~2 to 5 h) [v2.2 rescope]                    | L × Gate D | Mitigated | Overnight Docker + disk cache; HPSS fallback (R4) · WP1 · 2026-05-15            |
| **L-A-10 ★** | Dagstuhl headset-mic cross-talk bleed                        | M × H2     | Mitigated | `noisereduce` spectral gating + silent-portion xcorr check · WP1 · 2026-05-08 |

#### L-A-3 · Cuesta 2020 multi-f0 per-voice accuracy

**Specification**: Cuesta, Gómez, Bittner (2020, ISMIR) introduced a deep-learning multi-f0 estimator trained on synthetic SATB with a reported per-voice OA score of ~0.75 on synthetic test sets. No independent evaluation on (a) natural YouTube mixes, (b) non-studio acoustic conditions, or (c) non-Western polyphonic repertoires exists. Our Tier-1 `A3*` stretch feature depends on it.
**Evidence**: Cuesta et al. 2020 ISMIR *Multiple F0 Estimation in Vocal Ensembles using Convolutional Neural Networks* (L2).
**Severity**: Likelihood MED × Impact H3 (stretch feature).
**Status**: Escalated.
**Search-queries**:

- `"multi-f0" choir SATB Cuesta 2020 evaluation benchmark`
- `multipitch estimation polyphonic singing accuracy ISMIR site:archives.ismir.net`
- `"deep salience" voice assignment choir comparison 2023..2025`

#### L-A-4 ★ · Virtual choirs are post-synchronised

**Specification**: Eric Whitacre-style virtual choirs are typically assembled by (1) each singer recording alone against a click-track, (2) a producer manually aligning tracks in a DAW, (3) mixing + video compositing. The timing offset between singers in the output is an *editorial* signal, not an ensemble-coordination signal. Applying A(t) or N(t) to such audio measures editing precision, not remote coordination. H3's Tier-1 visual claim is confounded if bodies were also re-timed.
**Evidence**: Whitacre *Virtual Choir* production notes (L4/L5); Daffern et al. 2019 *The Impact of Vocal Range on the Sung Intonation of Large Amateur Choirs* (L2, context on ensemble performance).
**Severity**: Likelihood MED × Impact H1/H3 if uncontrolled.
**Status**: Mitigated.
**Strategy**:

1. Add `post_aligned_flag` column to `corpus_manifest.csv`. Populate from (a) description text-mining ("click-track", "recorded separately", "DAW"), (b) manual single-pass review by Zuraiz.
2. Explicit §Methods caveat: Tier-1 A-features are ensemble-descriptive only, never used in H1. Tier-1 V-features measure body-sway against a shared click-track — this remains a Honest-Signals question (does sway correlate with self-recorded breathing?) independent of network coordination.
3. Power-sensitivity: compute H3 ΔR² with/without post-aligned subset; report both.

---

### §12.2 Computer Vision (10)

| ID                  | Title                                                                    | Severity    | Status    | Action · Owner · Date                                                  |
| :------------------ | :----------------------------------------------------------------------- | :---------- | :-------- | :----------------------------------------------------------------------- |
| L-B-1               | MediaPipe head-sway unreliable                                           | M × Gate D | Mitigated | R3 — demote to secondary; trunk-sway primary                            |
| L-B-2               | Trunk-sway needs shoulders + hips visible                                | M × Gate D | Mitigated | §3.2 inclusion rule + per-video framing tag · WP2 · 2026-05-15        |
| **L-B-3 ★**  | MediaPipe validation covers limbs, not breath-frequency torso micro-sway | H × H3     | Escalated | Details below; WP2 calibration study 2026-05-22                          |
| **L-B-4 ★**  | **Mouth-aperture sync confounded by shared lyrics**                | M × H3     | Mitigated | Details below                                                            |
| L-B-5               | py-feat AUs trained on actors                                            | L × H3     | Mitigated | Demote to secondary; body-only primary · WP2                            |
| L-B-6               | Zoom-grid format heterogeneity                                           | L × Gate D | Mitigated | Auto grid-cell contour detector + manual layout tag · WP2 · 2026-05-22 |
| **L-B-7 ★**  | Lip-sync editing artefact (paired with L-A-4)                            | M × H1     | Mitigated | Shared mitigation with L-A-4                                             |
| L-B-8               | Framerate variation 24 / 30 / 60 fps                                     | L × H3     | Mitigated | Resample pose to 30 Hz linear interp · WP2 · 2026-05-15                |
| L-B-9               | Camera distance unknown → scale                                         | L × H3     | Mitigated | Normalise pose by inter-shoulder distance · WP2                         |
| **L-B-10 ★** | Fake-composite "virtual choirs" (studio + visual comp)                   | M × Gate B | Mitigated | Manual review ~5 h +`suspected_composite` flag · Zuraiz · 2026-05-15 |

#### L-B-3 · MediaPipe breath-frequency torso validity

**Specification**: Google's published MediaPipe Pose accuracy (Pearson r = 0.80–0.91 vs Vicon) was measured on gross limb motion — walking, waving, yoga poses. Torso oscillation at 0.2–0.5 Hz (respiratory rate during singing) with amplitude of a few pixels at webcam resolution has not been independently validated. If MediaPipe's noise floor exceeds the signal amplitude, breath-envelope xcorr (V(t) component 2) is spurious.
**Evidence**: Bazarevsky et al. 2020 *BlazePose* (L1, Google); no L2 breath-rate-from-pose study in our prior review.
**Severity**: Likelihood MED × Impact H3 (V(t) primary feature at risk).
**Status**: Escalated; mitigated-pending by scheduled WP2 calibration study 2026-05-22, but outcome uncertain.
**Search-queries**:

- `"MediaPipe Pose" breathing detection webcam accuracy site:arxiv.org`
- `pose estimation subtle torso oscillation RGB video validation`
- `"respiration rate" video remote photoplethysmography pose 2023..2025`

#### L-B-4 ★ · Mouth-aperture sync confound

**Specification**: Mouth opening (FaceMesh landmarks 13, 14, 78, 308) is driven almost entirely by lyrical content — singers performing the same text have identical vowel-triggered mouth dynamics regardless of network coordination. A raw mouth-aperture xcorr will trivially score high for any shared-text performance, indistinguishable from a coordination signal.
**Evidence**: Patterson & Jack 2020 *The Role of Viseme Generation in Lipreading* (L2); Hilton et al. 2021 audio-visual speech corpora reviews (L2).
**Severity**: Likelihood HIGH if used raw × Impact H3 (visual coupling interpretation).
**Status**: Mitigated.
**Strategy**:

1. Residualise mouth-aperture time-series against a viseme-sequence target from lyrics (Whisper alignment + grapheme-to-phoneme; synthesise expected aperture envelope; subtract before xcorr).
2. OR drop mouth-aperture from V(t) entirely (0.2 weight redistributed to trunk-sway 0.6 + breath-envelope 0.4).
3. Ablation: V(t) with and without mouth component; report both.
   **Owner · Date**: WP2 + WP1 · 2026-05-22 (folded into pose-validity study).

---

### §12.3 Network / Statistics (10)

| ID                 | Title                                                  | Severity   | Status    | Action · Owner · Date                                                                      |
| :----------------- | :----------------------------------------------------- | :--------- | :-------- | :------------------------------------------------------------------------------------------- |
| L-C-1              | Granger stationarity failure                           | M × H2    | Mitigated | Per-window ADF; IDTxl fallback (Decision 4) · WP3 · 2026-05-31                             |
| L-C-2              | Circular-shift null at seam edges                      | L × H2    | Mitigated | Shift range [0.05T, 0.95T] · WP1 · 2026-06-14                                              |
| L-C-3              | Dagstuhl N too small for natural H1                    | M × H2    | Mitigated | Tier-3 12× multiplier; ChoralSynth top-up gate 2026-05-15                                   |
| L-C-4              | Tier-3 synthetic latency ≠ real Zoom bursts           | M × H1    | Mitigated | DUST traces if access; else Carôt & Werner 2007 empirical · WP1 · 2026-05-01              |
| **L-C-5 ★** | **Cohen's d ≥ 0.5 target — no power analysis** | M × H1    | Mitigated | Drill-down below · Zuraiz · 2026-07-01                                                     |
| L-C-6              | Louvain stochastic partitioning                        | H × H2    | Mitigated | 100-seed ensemble consensus (Lancichinetti 2012) · WP3 · 2026-05-31                        |
| **L-C-7 ★** | **200-permutation null → p-floor 0.005**        | H × H1/H2 | Mitigated | Raise to N = 1000; log-log convergence plot · WP1 · 2026-06-30                             |
| **L-C-8 ★** | **Multiple-hypothesis correction missing**       | H × H1/H2 | Mitigated | Benjamini–Hochberg FDR q = 0.05; raw + adjusted p · Zuraiz · 2026-06-30                   |
| L-C-9              | Eigenvector centrality density-dependent               | L × H2    | Mitigated | Normalise-density before centrality; cross-check PageRank + betweenness · WP3 · 2026-05-31 |
| L-C-10             | Onset-timing uncertainty → Granger F                  | L × H1    | Mitigated | ±10 ms jitter bootstrap × 100; 95 % CI · WP3 · 2026-05-31                                |

#### L-C-5 ★ · Power analysis

**Specification**: The claim "Cohen's d ≥ 0.5 on ≥ 2 sub-indices" (§5 Claim 1, Gate B §10) requires paired-sample design with sufficient power. Without formal analysis, the claim is a wish.
**Evidence**: Faul et al. 2007 *G*Power 3* (L1 tool); Cohen 1988 *Statistical Power Analysis* (L2).
**Compute**: paired t-test, α = 0.05 (one-sided), power 0.80, d = 0.50 → n = 26 pairs required. Our design: Dagstuhl (n ≈ 10) + ESMUC (n = 3) × 4 regimes × 3 jitter seeds = (10 + 3) × 12 = 156 within-piece paired observations. **Conclusion: well-powered for d ≥ 0.50; marginally for d ≥ 0.30.**
**Action**: formal §Methods power note in paper referencing the above computation.

#### L-C-7 ★ · Permutation N

**Specification**: B = 200 permutations yields p-floor 1/(B+1) ≈ 0.005. After Benjamini–Hochberg FDR at q = 0.05 on ~130 comparisons, surviving q ≤ 0.0004 is impossible at B = 200.
**Evidence**: Phipson & Smyth 2010 *Permutation P-values Should Never Be Zero* (L2).
**Action**: raise B to 1000 on final analysis. Cost: dominated by 12× pipeline at ~6 min/permutation → ~100 h CPU; run on Hetzner spot GPU ~€25 (see L-F-8).

#### L-C-8 ★ · Multiple-hypothesis correction

**Specification**: 33 features × 4 regimes pairwise ≤ 132 simultaneous tests. Uncorrected α = 0.05 gives expected 6.6 false discoveries per run. Without correction, at least one "significant" result is guaranteed by chance.
**Evidence**: Benjamini & Hochberg 1995 *Controlling the False Discovery Rate* (L2, seminal).
**Action**: apply `statsmodels.stats.multitest.multipletests(method='fdr_bh')` per hypothesis block. Report both raw and q-adjusted p-values.

---

### §12.4 Data Sourcing (8)

| ID                 | Title                                       | Severity    | Status    | Action · Owner · Date                                                      |
| :----------------- | :------------------------------------------ | :---------- | :-------- | :--------------------------------------------------------------------------- |
| L-D-1              | Hacker URL list absent                      | H × Gate C | Resolved  | R1 — received 2026-04-22; `raw/hacker_url_list.csv` created                  |
| L-D-2              | YouTube rate-limit                          | M × Gate D | Mitigated | R2 — 1 req / 30 s; UA rotation; Archive.org fallback                        |
| L-D-3              | Video takedowns during project              | L × Gate D | Mitigated | Archive.org mirror check at ingest; flag in manifest                         |
| **L-D-4 ★** | SATB labels absent from YT metadata         | M × H3     | Mitigated | Cuesta 2020 section classifier + manual pass · Zuraiz · 2026-05-15         |
| L-D-5              | DUST packet-loss corpus access pending      | M × H2     | Escalated | Details below; gate 2026-04-24                                               |
| L-D-6              | yt-dlp license field null / wrong           | L × Gate A | Mitigated | Treat null as conservative; §60d UrhG basis · WP1 · 2026-05-01            |
| L-D-7              | Regional content blocks (DE)                | L × Gate B | Mitigated | Skip + log; document geographic bias in paper §Limitations                  |
| **L-D-8 ★** | English-title filter biases cultural sample | M × Gate B | Mitigated | Expand to {EN, DE, ES, FR, IT}; sensitivity analysis · Zuraiz · 2026-05-15 |

#### L-D-5 · DUST dataset access

**Specification**: DUST (cited in NMP literature as a packet-loss trace corpus) has unverified access terms and licence compatibility. If paywalled or ND-restricted, derived traces cannot be published with the paper.
**Evidence**: References in Carôt & Werner 2007, Lazzaro 2020 NMP reviews (L2); corpus homepage not yet located.
**Status**: Escalated.
**Strategy**: direct access by 2026-04-24; fallback Carôt & Werner 2007 published latency/jitter/loss distributions (synthesise our own traces).
**Search-queries**:

- `DUST dataset NMP packet loss access licence`
- `"networked music performance" packet trace corpus download`
- `Carôt SoundJack dataset public archive`

---

### §12.5 Legal / GDPR (5)

| ID                 | Title                                                       | Severity    | Status    | Action · Owner · Date                                          |
| :----------------- | :---------------------------------------------------------- | :---------- | :-------- | :--------------------------------------------------------------- |
| **L-E-1 ★** | **FaceMesh landmarks = biometric under GDPR Art. 9?** | H × Gate A | Escalated | Details below; Bamberg DPO consult pre-2026-05-08                |
| L-E-2              | §60d UrhG jurisdiction for foreign repo (arXiv)            | M × Gate C | Escalated | Bamberg legal desk before 2026-07-07                             |
| **L-E-3 ★** | **DPIA (Art. 35) not yet drafted**                    | H × Gate A | Mitigated | 2-page DPIA by 2026-05-08 · Zuraiz · Bamberg DPO template      |
| L-E-4              | YouTube ToS vs statutory-rights conflict                    | L × Gate A | Accepted  | Statutory > ToS per CLAUDE.md §3; residual risk accepted        |
| L-E-5              | Non-consented identifiable singers                          | L × Gate A | Mitigated | §60d + Art. 9(2)(j); no re-id; no redistribution; features-only |

#### L-E-1 ★ · FaceMesh as biometric data

**Specification**: GDPR Art. 4(14) defines biometric data as "personal data resulting from specific technical processing … which allow or confirm the unique identification of a natural person." 468 FaceMesh points are derived from face images. The legal question: do they enable unique identification, triggering Art. 9(1) prohibition subject to Art. 9(2)(j) research exception + Art. 89 safeguards?

Empirical literature (Kortli et al. 2020; Xu et al. 2022) shows 3D-face landmark-only features achieve face-recognition accuracy ≥ 90 % on controlled datasets. This is sufficient for "allow or confirm" identification — conservative classification is **biometric under Art. 9**.

**Evidence**: GDPR Art. 4(14), Art. 9, Art. 9(2)(j), Art. 89 (L3 statute); EDPB Guidelines 3/2019 on video devices (L3); Kortli et al. 2020 *Face Recognition Systems — a Survey* (L2).
**Severity**: Likelihood HIGH × Impact HIGH on Gate A if DPIA + Art. 9(2)(j) framing absent.
**Status**: Escalated.
**Strategy default**: treat as Art. 9 biometric. Rely on Art. 9(2)(j) + Art. 89 (aggregate, pseudonymise, no re-id attempts, delete raw mp4 after feature extraction). Consult Bamberg DPO before 2026-05-08; draft DPIA (L-E-3) as supporting evidence.
**Search-queries**:

- `facial landmark identifiability GDPR Article 9 legal opinion`
- `MediaPipe FaceMesh pseudonymisation biometric classification`
- `"face landmarks" privacy EDPB guideline research exception`
- `"Article 9" biometric "research exception" German DPO opinion`

#### L-E-2 · §60d UrhG foreign publication

**Specification**: §60d UrhG and EU DSM Art. 3 grant DE-based researchers TDM rights. If the paper (or supplementary materials) is published on arXiv (US jurisdiction), the derivative work may fall outside the DE exception. Practical question: can we publish extracted feature vectors + trained models on arXiv?
**Evidence**: §60d UrhG (L3); EU DSM Directive 2019/790 Art. 3 (L3); Geiger et al. 2021 *The Copyright Implications of Text and Data Mining* (L2).
**Status**: Escalated.
**Strategy**: consult Uni Bamberg legal desk before 2026-07-07 paper draft v1. Fallback: publish on Zenodo (EU-jurisdiction) mirrored from arXiv; or publish only derived statistics with no raw-feature redistribution.
**Search-queries**:

- `§60d UrhG TDM exception publication arXiv jurisdiction`
- `EU DSM Directive Article 3 cross-border publication research`
- `German copyright research exception open access repository`

#### L-E-3 ★ · DPIA

**Specification**: GDPR Art. 35 requires a Data Protection Impact Assessment for high-risk processing. Large-scale biometric-landmark extraction + automated analysis qualifies (Art. 35(3)(b) + EDPB-identified criteria).
**Action**: draft 2-page DPIA following Bamberg DPO template. Content: data categories (public video URLs, derived pose + face landmarks), purposes (§60d UrhG research + Art. 9(2)(j)), lawfulness, risks (re-identification, leakage), safeguards (pseudonymisation, aggregation, 30-day raw-mp4 retention then delete, no cross-dataset linkage), DPO consultation outcome.
**Owner · Date**: Zuraiz · 2026-05-08.

---

### §12.6 Project / Reproducibility (8)

| ID                 | Title                                                               | Severity    | Status    | Action · Owner · Date                                                                                |
| :----------------- | :------------------------------------------------------------------ | :---------- | :-------- | :----------------------------------------------------------------------------------------------------- |
| L-F-1              | WP2 video-pipeline milestone slip                                   | L × Gate D | Mitigated | R5 — single-video prototype + OpenPose fallback                                                       |
| L-F-2              | Paper starts too late                                               | L × Gate D | Mitigated | R6 — skeleton by 2026-05-15                                                                           |
| L-F-3              | Scope creep into self-recording                                     | L × Gate D | Mitigated | R7 — firm no                                                                                          |
| **L-F-4 ★** | ~~Docker Desktop WSL2 GPU passthrough fragile on Win 11~~ | M × Gate D | **Resolved 2026-04-25** | **Resolved by dropping Docker entirely from scaffold** (semester project does not need containerization; `uv.lock` + host `ffmpeg` is sufficient reproducibility). CPU-only execution remains canonical; GPU optional via `torch` runtime detection if a member has CUDA available. |
| **L-F-5 ★** | MediaPipe 0.10.14 × Py 3.11 × Win 11 wheel                  | H × Gate A | Resolved  | **RESOLVED 2026-04-24**. Smoke-test passed: `mediapipe==0.10.14` installs cleanly on Win 11 × Py 3.11.0; `mp.solutions.pose.Pose()` instantiates and TFLite XNNPACK delegate initialises. No fallback to 0.10.9 needed. Note: mediapipe 0.10.14 pulls numpy 2.4.4 rather than §11.8's pinned 1.26.4 — version drift logged to L-H-3. |
| L-F-6              | 15-min reproducibility claim un-tested                              | L × Gate D | Mitigated | Monthly fresh-laptop test · WP1                                                                       |
| L-F-7              | `make all` referenced but no Makefile yet                         | M × Gate D | Resolved  | **RESOLVED 2026-04-25**. Makefile landed on `scaffold` branch with sync / smoke / all (stub) / reproduce (stub) / lint / typecheck / test / clean targets.                                               |
| **L-F-8 ★** | Compute budget undisclosed (~10 to 20 GPU-h at N = 30) [v2.2 rescope]                          | L × Gate D | Mitigated | Hetzner spot T4 ~€10 personal OR CPU-only OR Bamberg HPC · Zuraiz · 2026-05-01                      |

---

### §12.7 Stakeholder (4)

| ID                 | Title                                         | Severity    | Status    | Action · Owner · Date                                                    |
| :----------------- | :-------------------------------------------- | :---------- | :-------- | :------------------------------------------------------------------------- |
| L-G-1              | Hacker-rigor vs Gloor-narrative divergence    | L × Gate C | Mitigated | Two stakeholder-specific artefacts (§5)                                   |
| **L-G-2 ★** | **Apr 30 joint-deck not started**       | H × Gate C | Open      | Draft 2026-04-25; team critique 2026-04-28; rehearsal 2026-04-29 · Zuraiz |
| L-G-3              | Paper venue undecided                         | L × Gate C | Mitigated | Decide by 2026-06-01: IEEE Access default / LNCS ICCCN fallback            |
| L-G-4              | Hacker Tier-0 URLs may violate §3.2 criteria | L × Gate C | Mitigated | Tier-0 own analysis track; §3.2 applies to Tier-1 self-sourced            |

---

### §12.8 Integration / Engineering (4)

| ID                 | Title                                            | Severity    | Status    | Action · Owner · Date                                                               |
| :----------------- | :----------------------------------------------- | :---------- | :-------- | :------------------------------------------------------------------------------------ |
| **L-H-1 ★** | Parquet schemas (WP2 → WP3) not specified       | M × Gate D | Open      | `features/schema.md` + pydantic model before 2026-05-08 · Zuraiz                   |
| **L-H-2 ★** | Dashboard live-demo feasibility (60 s)           | M × Gate D | Mitigated | Pre-baked results for 3 videos; "live" = animate pre-computed · Zuraiz · 2026-06-21 |
| L-H-3              | Version skew (mediapipe × opencv × tensorflow) | L × Gate A | Mitigated | Pin all via `uv.lock`; Docker fresh-build per commit                                |
| L-H-4              | Vault merge conflicts (4 concurrent editors)     | L × Gate D | Mitigated | One-owner-per-page + Obsidian merge plugin                                            |

---

### §12.10 Deep-Read Cascade Findings (4, all `★`, added v1.1 · 2026-04-24)

Added from the 2026-04-24 deep-read audit of all 27 primary and secondary sources. Each entry corrects a claim that prior shallow digests projected onto the source where the source itself does not support it. Full per-paper evidence at `onsidian vault/OSN-M/wiki/00_overview/deep_read_audit.md`.

| ID | Title | Severity | Status | Action · Owner · Date |
| :--- | :--- | :--- | :--- | :--- |
| **L-H-5 ★** | S-02 entanglement formula validated on email, not music | M × Gate B | Open | Paper must explicitly frame E(t) as a novel domain transfer; do not cite S-02 as prior validation of an acoustic entanglement metric · Zuraiz · paper draft v1 (2026-07-07) |
| **L-H-6 ★** | P-23 XR-vs-baseline QoE advantage confounded with 70 ms lower latency (144 ms vs 74 ms A2S) | M × H1 | Open | Do not cite P-23 as evidence for H1 without explicit latency-equalisation caveat; paper Methods must acknowledge the confound · Zuraiz · paper draft v1 (2026-07-07) |
| **L-H-7 ★** | P-11 "100 ms threshold" is a Jamulus design target, not an empirical coordination cliff | L × H1 | Open | Paper and Apr 30 deck must not quote 100 ms as a phase transition; use P-11's measured 83±57 / 47±46 ms inter-chorister timing instead · Zuraiz · 2026-04-30 |
| **L-H-8 ★** | P-18 / P-19 false vocal-to-limb causal analogy | L × Gate A | Mitigated | V(t) pipeline does not use voice as a pose prior; stated explicitly in §11.1 and [[entanglement_index]] — confirms Project 8 is not affected · Zuraiz · 2026-04-24 |
| **L-H-9 ★** | `py-feat==0.6.2` deferred from scaffold: transitive `nltools>=0.5.1 → numpy<1.24` conflicts with §11.8 `numpy==1.26.4` pin | L × H3 | Mitigated | V5 FFI-proxy is a §11.2 secondary feature; WP2 sub-plan adds py-feat with a resolved numpy strategy (likely a dedicated `wp2-face` extra with a relaxed numpy range) · Zuraiz · WP2 kick-off (≈ 2026-05-22) |

---

### §12.9 Pre-Apr-30 Watch List

The five items that **must** land before the 2026-04-30 14:00 CET Hacker + Gloor joint status meeting. Each has a single owner and a hard acceptance criterion. Under the v2.2 scope cut (2026-04-19), GDPR is on the critical path, not deferred to May 8: W4 and W5 were promoted from later deadlines so the legal framing can be presented to the professors before any large-scale data work begins.

#### W1 · L-D-1 — Hacker URL list receipt

- **Owner**: Zuraiz
- **Deadline**: 2026-04-22 09:00 CET (go/no-go)
- **Acceptance**: **RESOLVED 2026-04-22**. Email received with 5 URLs 3 hrs before deadline. Manifest created at `raw/hacker_url_list.csv`; metadata logged at `onsidian vault/OSN-M/wiki/sources/hacker_tier0_reply.md`.

#### W2 · L-F-5 — MediaPipe wheel smoke-test

- **Owner**: Zuraiz
- **Deadline**: 2026-04-25
- **Acceptance**: **RESOLVED 2026-04-24** (one day early). §11.5 Test 3 (`uv pip install mediapipe==0.10.14 && python -c "import mediapipe as mp; print(mp.solutions.pose.Pose())"`) completed without error on Windows 11 × Python 3.11.0 × uv 0.10.10. Pose object instantiated; TensorFlow Lite XNNPACK delegate loaded for CPU inference. Side-finding: mediapipe 0.10.14 forces numpy 2.4.4 (§11.8 pins 1.26.4) — tracked as L-H-3 version-skew; real pyproject.toml will need to resolve.

#### W3 · L-G-2 — Apr 30 joint-deck draft

- **Owner**: Zuraiz (team reviews)
- **Deadline**: 2026-04-25 (draft) · 2026-04-28 (team critique) · 2026-04-29 (rehearsal)
- **Acceptance**: 5–10 slide deck covering (1) team + archetypes, (2) problem + two-lens framing (Pentland + Hacker), (3) three data tiers, (4) roadmap with Apr 17–Jul 17 milestones, (5) §12 top-3 open items transparently flagged. Team critique round incorporated before rehearsal.

#### W4 · L-E-1 — FaceMesh biometric classification (promoted under v2.2)

- **Owner**: Zuraiz
- **Deadline**: 2026-04-29 (position drafted), presented 2026-04-30 to professors
- **Acceptance**: a written position that treats FaceMesh landmarks as GDPR Art. 9 biometric data by default, relying on Art. 9(2)(j) research exception plus Art. 89 safeguards. One paragraph, ready to quote verbatim on the joint deck. Bamberg DPO contact request filed (reply does not need to arrive pre-Apr-30, but the request must be logged).

#### W5 · L-E-3 — DPIA outline (promoted under v2.2)

- **Owner**: Zuraiz
- **Deadline**: 2026-04-29 (outline), full 2-page DPIA still due 2026-05-08
- **Acceptance**: one-page DPIA outline using the Bamberg DPO template, enumerating data categories, purposes, lawfulness, risks, and safeguards. Does not need to be signed off; needs to exist in `drafts/dpia_outline.md` so the professors see that GDPR is on the critical path, not an afterthought.

---

### §12.10 Register maintenance

- **Owner**: Zuraiz (WP1).
- **Review cadence**: opened at each iteration-2+ status report, and before each milestone gate in §6.
- **Update protocol**: new limitations get next available `L-<CAT>-<N>` ID; status transitions (Open → Mitigated → Resolved) logged in `onsidian vault/OSN-M/wiki/log.md` as `lint` entries; obsolete entries marked `[SUPERSEDED YYYY-MM-DD]` rather than deleted (auditability).
- **Paper integration**: a curated subset (primarily Escalated + Open + highest-impact Mitigated) becomes the §Threats to Validity section of the paper, drafted in parallel with v1 draft 2026-07-07.
