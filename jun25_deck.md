# Jun 25 Status Meeting V, Deck

**Project 8 · Entanglement in Online Choir · 2026-06-25 · 14:00-16:00 CET**

> 8 slides, 8-10 min spoken, coordinators' rubric: goals+plan recap, last-iteration progress, next-iteration plan, retrospective, problems/questions. Presenters: Zuraiz and Kumaran Vasu. Speaker notes in `jun25_script.md`; Q&A bank in `jun25_qa_prep.md`. All numbers are final and verified against `data/processed/tier3/_latency_grid.csv` (28 pieces, 3 datasets).

---

## Slide 1: Title

**Status Meeting V**

Project 8: Entanglement in Online Choir

SNA-OSN-M Summer 2026 · Uni Bamberg × Uni Köln × HSLU

Presented by Zuraiz and Kumaran Vasu, on behalf of the team

Supervisors: Prof. Janine Hacker (Uni Bamberg) · Prof. Peter Gloor (Köln)

2026-06-25 · 14:00 CET

---

## Slide 2: Recap, goals and plan

**Kicker**: RECAP

**E(t)** = mean( A(t) audio, V(t) visual, N(t) network ): one coordination score per moment.

**Three hypotheses (unchanged)**:
- H1: low-latency tools score higher E(t) than high-latency.
- H2: influence-network topology shifts democratic → leader-dominated as latency rises.
- H3: visual signals add explanatory power over audio.

**Where we are**: status meeting **5 of 6**. Apr-block ✓ · Apr 30 ✓ · May 21 ✓ · Jun 11 ✓ (E(t) operational) · **Jun 25 TODAY** · Jul 9 · Jul 23 final.

**This iteration's job**: test H1 for the first time, via Tier-3 latency injection.

**Takeaway**: this iteration we found the latency signal, and learned exactly where it lives.

---

## Slide 3: Headline, we found the H1 latency signal (and where the naive metric missed it)

**Kicker**: PROGRESS · LAST ITERATION

**The journey (honest)**:
1. Injected **constant delay** into clean multitrack → E(t) unchanged. Confound: our audio coupling is lag-tolerant by design, it absorbs a constant shift.
2. Pivoted to **realistic jitter** (SD = the *measured* Jamulus inter-chorister timing SD, 46/57 ms from P-11) → envelope E(t) *still* flat. Deeper reason: 10-second loudness envelopes are physically robust to tens-of-ms timing noise.
3. Added **zero-lag onset synchrony** (do singers attack notes at the same instant?), the physical quantity latency actually breaks → **the H1 signal appears.**

**Result (5 Dagstuhl pieces)**: onset synchrony falls **49-61%** from clean to Zoom-class jitter, monotonically, every piece. Envelope coupling barely moves (−9%).

**Takeaway**: latency degrades *attack timing*, not loudness coupling, which is why a naive envelope metric would have reported "latency doesn't matter."

---

## Slide 4: The dissociation (the figure)

**Kicker**: PROGRESS · LAST ITERATION

**Visual**: `data/figures/tier3_corpus_summary.png` (2 panels, mean ± SD per dataset):
- Left, **attack-timing onset synchrony** vs jitter: all 3 datasets fall steeply (the H1 signal).
- Right, **envelope E(t)** vs jitter: flat (latency-robust).

**One-line read**: same data, two measures, opposite verdicts. The dissociation *is* the finding.

**Method honesty**: jitter SDs are measured (not tuned); onset synchrony chosen a priori as the physical target; null reported throughout; constant-delay confound reported, not hidden.

**Takeaway**: H1 is supported, on attack-timing synchrony, with the mechanism explained.

---

## Slide 5: It replicates, and the corpus grew

**Kicker**: PROGRESS · LAST ITERATION

**Cross-dataset replication (28 pieces, 3 corpora)**, onset synchrony clean → Zoom:
- **Dagstuhl** (real human, 5 pieces): 0.287 → 0.124, **−57%**
- **ESMUC** (real human, independent, 3 takes): 0.254 → 0.087, **−66%**
- **ChoralSynth** (synthetic, 20 pieces): 0.308 → 0.075, **−76%**

All monotonic; two independent human datasets plus synthetic. Not a single-dataset artifact.

**Corpus growth (Phase 1)**: added both Tier-2 datasets, downloaded + MD5-verified vs Zenodo (ESMUC CC BY 4.0; ChoralSynth CC BY-SA 4.0), via a unified dataset-adapter layer, one pipeline now ingests all three corpora.

**Takeaway**: the latency→attack-timing effect holds across real and synthetic choirs.

---

## Slide 6: Dashboard alpha, on real data

**Kicker**: PROGRESS · LAST ITERATION

**Visual**: `data/figures/wp4_dashboard_realdata.png` (live screenshot, real Dagstuhl piece LI_QuartetA_Take02).

The dashboard now runs on **real outputs**, not mock data:
- E(t) timeline from the real entanglement pipeline.
- Influence graph from the real Granger GEXF (who-leads-whom).
- 33-keypoint **pose overlay** synced to video playback.
- Metadata shows the signals each piece actually carries.

Honest by construction: Dagstuhl pieces show audio+network; Tier-1 videos show video+pose (no piece has all three yet).

**Takeaway**: the Jun-21 dashboard-alpha milestone is met, on real data.

---

## Slide 7: Next iteration plan (Jun 26 → Jul 9)

**Kicker**: NEXT ITERATION

| Track | What ships |
|:--|:--|
| Integration | Fold onset-synchrony into the E(t) definition as the timing-sensitive component (with the envelope term) |
| WP3 | Per-window time-varying N(t); cleaner H2 topology measure |
| Paper | Start the seminar-report methods + results sections |
| WP2 / H3 | First visual-onset V(t): pair pose onsets with audio onsets on the 18 usable Tier-1 videos |

**Hard milestone before Jul 9**: report draft v1 with the H1 result written up.

**Takeaway**: from "found the signal" to "written up and corpus-complete."

---

## Slide 8: Retrospective + open problems

**Kicker**: RETROSPECTIVE · OPEN PROBLEMS

**What worked**: a wrong first manipulation (constant delay) was caught by its own null and turned into a sharper method; every dataset claim traces to a verified file.

**What we fixed**: the "ESMUC proprietary" stale note (it is open on Zenodo); curation now filters on singer visibility.

**Open problems (honest)**:
- **H1 rests on *simulated* latency** injected into studio audio, this models transmission delay, not a live singer's behavioural adaptation. Real latency-varied recordings would test it directly.
- **H3 (visual) is still data-blocked**: no piece has audio and video together; envelope E(t) alone is latency-blind, so a visual-onset signal is the next step.
- **H2 (topology vs latency)** is not cleanly measured yet (fixed-lag density artifact).

Thank you.
