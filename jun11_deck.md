# Jun 11 Status Meeting IV, Deck

**Project 8 · Entanglement in Online Choir · 2026-06-11 · 14:00 CET**

> Format: 8 slides for an 8-10 minute presentation (target ~9 minutes spoken). Structure follows the coordinators' rubric exactly: (1) goals + plan recap, (2) progress during the last iteration, (3) plan for the next iteration, (4) retrospective output, (5) problems / questions. Speaker notes in [jun11_script.md](jun11_script.md). Q&A bank in [jun11_qa_prep.md](jun11_qa_prep.md). Design language: figure-led slides, stat cards over bullet walls, one takeaway line per slide.

---

## Slide 1: Title (15 sec)

**Status Meeting IV**

Project 8: Entanglement in Online Choir

SNA-OSN-M Summer 2026 · Uni Bamberg × Uni Köln × HSLU

Presented by Hassan Ahmed, on behalf of the team

Supervisors: Prof. Janine Hacker (Uni Bamberg), Prof. Peter Gloor (MIT/Köln)

---

## Slide 2: Our goals and plan, a 60-second recap (rubric §1)

**Kicker**: RECAP

**Visual**: left half: E(t) formula card (large) + the three hypotheses as three compact cards. Right half: horizontal timeline strip Apr 16 → Jul 31 with the six status meetings marked, "WE ARE HERE" marker on Jun 11.

**Research question**: when a choir sings together over the internet, can we put a number on how well they coordinate?

**The number**: E(t) = mean of A(t) audio coupling, V(t) visual coupling, N(t) network coherence.

**Three hypotheses**:
- H1: low-latency tools (Jamulus, SoundJack) score higher E(t) than Zoom.
- H2: influence network shifts from democratic to leader-dominated as latency rises.
- H3: visual signals add ≥ 10 points of explained variance over audio alone.

**Timeline**: block course Apr 15-16 → six status meetings → final presentation Jul 23 → paper Jul 31. We are at status meeting four of six.

**Takeaway line**: same goals as April, no scope drift; this iteration was about making E(t) real.

---

## Slide 3: Last iteration, the headline: E(t) is operational (rubric §2)

**Kicker**: PROGRESS · LAST ITERATION

**Visual**: hero figure `data/figures/et_corpus_comparison.png` at ~70% slide width. Right rail: three stat cards.

**Stat cards**:
- **5 / 5** pieces beat the null (p < 0.001)
- **200** circular-shift permutations per piece
- **0.57 – 0.80** observed mean E(t) range

**The result in one sentence**: the Entanglement Index runs end-to-end on five real multitrack choir pieces, and on every piece the observed coordination is far above what random chance produces.

**The pattern**: Locus Iste (homophonic chant) clusters at 0.74-0.80; Tu Pauper Es (polyphonic) at 0.57-0.68. The split follows musical structure, not ensemble size. The metric is sensitive to what the choir is actually doing.

**Takeaway line**: the number we promised in April now exists, is repeatable, and is statistically defensible.

---

## Slide 4: Last iteration, the audio + network engine behind it (rubric §2)

**Kicker**: PROGRESS · LAST ITERATION

**Visual**: hero figure `data/figures/wp3_influence_graphs_5pieces.png` at ~65% width. Right rail: stat cards.

**Stat cards**:
- **25** Dagstuhl takes processed (was 1)
- **288** pairwise audio couplings
- **2** causality methods per piece

**WP1 audio**: every musical take in the Dagstuhl ChoirSet now has per-singer pitch, onset, and loudness features. Coupling pattern matches musical structure (within-section 0.78-0.87, full-choir polyphonic 0.40-0.45).

**WP3 network (Hacker flagship v2)**: directed influence graphs for 5 pieces under both standard Granger and the ordinal-pattern COP-GC variant. The two methods agree on quartets and diverge on full choir (42/56 vs 25/56 significant edges), which is itself a finding: about a third of standard edges depend on linear magnitude, not pattern structure.

**Takeaway line**: the influence-graph pipeline reproduces last sprint's result exactly and now scales.

---

## Slide 5: Last iteration, video + dashboard (rubric §2)

**Kicker**: PROGRESS · LAST ITERATION

**Visual**: hero figure `data/figures/wp4_dashboard_scaffold.png` (left, ~55% width). Right rail: WP2 mini-figure `data/figures/wp2_visual_features_v2.png` (small) + stat cards.

**Stat cards**:
- **10** Tier-1 videos pose-processed
- **5 / 10** pass the 50% detection floor
- **23 / 23** tests green

**WP2 video**: pose extraction across 10 YouTube videos stratified by NMP regime. Half pass cleanly (best: 98.5% detection); half are software-UI captures or low-res tile grids with no detectable body. Per the "try and iterate" decision from last meeting, the 5 passing videos become our working set; limitation documented.

**WP4 dashboard**: the React + FastAPI scaffold is up. Four panels (video, influence graph, E(t) timeline, metadata) render end-to-end against mock data. Screenshot is the real app running locally.

**Takeaway line**: every work package moved; nothing is blocked.

---

## Slide 6: Plan for the next iteration, Jun 12 → Jun 25 (rubric §3)

**Kicker**: NEXT ITERATION

**Visual**: 5-row track table, full width, generous row height.

| Track | Next-iteration work |
|:---|:---|
| WP1 audio | per-window Granger → time-varying N(t) for the dashboard timeline |
| WP2 video | pose on remaining Tier-1 videos, quality-first triage |
| WP3 network | **Tier-3 latency injection**: synthetic jitter on Dagstuhl audio at 4 regime levels, E(t) per level. First cross-regime test of H1/H2. |
| WP4 dashboard | swap mock JSON for real parquet readers + pose overlay |
| Data | download ChoralSynth (openly licensed, Zenodo); follow up ESMUC |

**Hard milestone**: dashboard alpha on real data + first Tier-3 cross-regime result, before status meeting five.

**Takeaway line**: this iteration was "make E(t) real"; the next is "make E(t) discriminate between regimes".

---

## Slide 7: Retrospective output (rubric §4)

**Kicker**: RETROSPECTIVE

**Visual**: three card columns: "What worked" / "What went wrong" / "Known limitations".

**What worked**:
- One reviewable artefact per work package per iteration.
- Documentation updated at every milestone; project state is readable from three files.

**What went wrong**:
- ESMUC and ChoralSynth not yet in Tier-2. ChoralSynth is openly licensed on Zenodo and scheduled for next iteration; ESMUC requires a license (open question).
- Half of the Tier-1 videos are screen captures without visible singers. Future curation will filter on singer visibility, not only NMP regime.

**Known limitations**:
- V(t) is absent from current E(t) values; Dagstuhl has no video. The composite reallocates weight until multimodal data exists.
- All five E(t) pieces are zero-latency studio recordings. Cross-regime variation arrives with Tier-3.
- p < 0.001 means 0 of 200 permutations exceeded the observed value.

**Takeaway line**: all retrospective items are documented in sprint3_results.md.

---

## Slide 8: Problems and questions (rubric §5)

**Kicker**: PROBLEMS / QUESTIONS

**Visual**: two question cards, large type, nothing else.

1. **To Prof. Hacker, ESMUC dataset access**: do you have institutional access to the ESMUC multitrack dataset? ChoralSynth is openly licensed on Zenodo and we will download it ourselves; ESMUC is the only dataset where we need support.
2. **To the coordinators, cluster access (nice-to-have, not a blocker)**: is CPU time available on a Bamberg or HSLU cluster? The planned next-iteration scope runs overnight on our laptops. Cluster access would let us run denser jitter grids and finer analysis windows, strengthening the H1 robustness checks.

Thank you.
