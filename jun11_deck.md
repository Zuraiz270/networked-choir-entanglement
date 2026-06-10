# Jun 11 Status Meeting IV, Deck

**Project 8 · Entanglement in Online Choir · 2026-06-11 · 14:00 CET**

> Format: 10 slides for a 10-minute presentation (target 9 minutes spoken). Speaker notes live in [jun11_script.md](jun11_script.md). Q&A prep bank in [jun11_qa_prep.md](jun11_qa_prep.md). Tone is strength-first: lead the Sprint-3 result on slide 3, surface limitations on slide 9 (not before).

---

## Slide 1: Title

**Status Meeting IV**

Project 8: Entanglement in Online Choir

SNA-OSN-M Summer 2026 · Uni Bamberg × Uni Köln × HSLU

Presented by Hassan Ahmed, on behalf of the team

Supervisors: Prof. Janine Hacker (Uni Bamberg), Prof. Peter Gloor (MIT/Köln)
Coordinators: Janine, Simon, Peter

---

## Slide 2: What we said we'd do, Sprint 3 plan recap

**Visual**: split layout. Left: the May-21 commitment list. Right: status column with ✓ marks.

Three weeks ago we committed to four core Sprint-3 deliverables plus two stretch items. Here is where each one stands.

| Sprint 3 deliverable | Status |
|:---|:---:|
| WP1 audio pipeline on all Dagstuhl pieces | shipped |
| WP2 pose extraction on 10 Tier-1 videos | shipped |
| WP3 Granger influence graph on 5 pieces + COP-GC | shipped |
| WP4 dashboard scaffold | shipped |
| E(t) end-to-end + null model | shipped (stretch) |
| WP3 full-corpus metrics | shipped (stretch) |

All six deliverables landed within the sprint window. Walking through each one next.

---

## Slide 3: Headline, E(t) works, all 5 pieces beat the null at p < 0.001

**Visual**: large `data/figures/et_corpus_comparison.png`. Five red dots (observed mean E(t)) sit clearly above five gray error bars (200-shuffle null 95% interval). Each red dot has `***` above it (p < 0.001).

The Entanglement Index computes end-to-end. We ran it on all five pieces with both audio and network signals. Every piece beats its null at p < 0.001.

The pattern is clean. Locus Iste sits at 0.74 to 0.80, Tu Pauper Es sits at 0.57 to 0.68. The split is by piece, not by ensemble size. A four-singer quartet of Locus Iste sits with the eight-singer full choir of Locus Iste, not with the quartet of Tu Pauper Es.

Reading: this is real coordination structure, not a statistical artifact. The number we have been promising since April is now operational and significantly above chance.

---

## Slide 4: What we shipped, WP1 audio scale

**Visual**: small `data/figures/wp1_satb_coupling.png` thumbnail (the Sprint-2 reference) + 4-row summary table from `data/processed/dagstuhl/_summary.csv` showing the per-piece coupling spread.

WP1 went from one piece in Sprint 2 to 25 in Sprint 3. Locus Iste plus Tu Pauper Es, every musical take in the Dagstuhl ChoirSet. 130 newly extracted singer parquets, 288 pairwise audio couplings.

The pipeline is resumable, prefers the dynamic microphone per singer, and writes a corpus-level summary CSV.

The cross-piece pattern is consistent with musical structure. Within-section pieces, like the basses singing alone, couple tightly at 0.78 to 0.87. Full-choir polyphonic pieces drop to 0.40 to 0.53. Sanity check passes.

---

## Slide 5: What we shipped, WP3 influence graph + COP-GC (Hacker flagship v2)

**Visual**: `data/figures/wp3_influence_graphs_5pieces.png` (2x3 grid).

WP3 went from one piece, one method to five pieces, two methods. Standard parametric Granger and the COP-GC ordinal-pattern variant from Zanin 2021 that we had promised since the implementation plan. Both methods produce a Gephi-compatible GEXF per piece.

The Sprint-2 Hacker flagship reproduces exactly: 11 of 12 significant edges, density 0.917, soprano leads.

The interesting finding is the method-divergence story. On Tu Pauper Es full choir, standard Granger flags 42 of 56 directed edges as significant. COP-GC flags 25. That gap is edges that depend on linear-magnitude structure rather than ordinal pattern structure. We carry both forward and let the contrast inform the discussion section.

---

## Slide 6: What we shipped, WP2 pose extraction on 10 Tier-1 videos

**Visual**: `data/figures/wp2_visual_features_v2.png` (V(t) for ZKthfLPWBCQ, the best detection in batch).

WP2 went from one Tier-1 video in Sprint 2 to 10 in Sprint 3. Stratified across NMP regimes: four Jamulus, three Zoom-only, two SoundJack, one Jamulus+Zoom. Total runtime 2.3 minutes.

5 of 10 pass the 50% pose-detection floor. The 5 passing videos define our WP2 inclusion set for the H1 hypothesis test downstream.

The 5 failing videos are software-UI screen captures or dense low-resolution tile grids with no body in frame for MediaPipe to find. This matches the "try and iterate" guidance from Status Meeting III. It is a property of the input, not of the pipeline.

---

## Slide 7: What we shipped, WP4 dashboard scaffold + E(t) integration

**Visual**: `data/figures/wp4_dashboard_scaffold.png` (Playwright screenshot of the 4-panel layout running locally).

Two pieces in one slide.

Left: the WP4 dashboard. React 18 + Vite 5 + TypeScript strict, FastAPI 0.111 backend. Four panels: video placeholder, D3 force-directed influence graph, Plotly E(t) timeline, metadata strip. Runs against mock JSON right now, end-to-end verified with a Playwright screenshot.

Right: the E(t) integration module behind it. Takes A(t), V(t), N(t) parquets and produces the time-aligned E(t) timeline. 200-shuffle circular-shift null at the composite level. NaN-aware weight reallocation when one signal is missing, which is the realistic case in our corpus today.

23 of 23 tests pass.

---

## Slide 8: Sprint 4 plan, June 12 to June 25

**Visual**: same 4-track table style as the May-21 Sprint-3 plan slide.

Sprint 4 runs from tomorrow until Status Meeting V on June 25. Four parallel tracks plus one acquisition task.

| Track | Sprint 4 work |
|:---|:---|
| WP1 audio | per-window Granger to give us a time-varying N(t) signal |
| WP2 video | extract pose for the remaining Tier-1 videos, triaged by detection rate |
| WP3 network | Tier-3 latency injection: synthetic jitter on Dagstuhl audio, run E(t) at each regime |
| WP4 dashboard | swap mock JSON for real parquet readers; pose overlay on real video |
| Data | acquire ChoralSynth from Zenodo; pursue ESMUC access if Hacker confirms a path |

The Sprint-4 hard milestone is the dashboard alpha running on real data.

---

## Slide 9: Retrospective and four honest limitations

**Visual**: 2x2 box of the four limitations + small "what worked" panel.

What went well: we shipped six of six Sprint-3 deliverables, including the two pull-forward stretch items. The doc-update discipline kept TEAM_BRIEF, PROJECT_GUIDE, and the vault wiki in sync after every phase.

What did not: ESMUC + ChoralSynth not yet pulled into Tier-2. ESMUC needs a UPF license we have not pursued; ChoralSynth is openly licensed on Zenodo and is a Sprint-4 download, not a blocker.

**Four honest limitations** to flag explicitly so they are not Q&A surprises:

1. **V(t) is NaN in every current E(t).** Dagstuhl is audio-only. The integration code is ready for V(t) the moment a piece carries it.
2. **WP3 corpus is all Dagstuhl studio.** No NMP-regime variation in N(t) yet. Cross-regime is Sprint 4.
3. **WP2 detection is 50%.** The 5/10 pass rate is the explicit inclusion set, per Status-Meeting-III guidance.
4. **p_null reports as 0.0000.** Correct interpretation is p < 1/200, not literal zero. We can bump to 2000 shuffles if anyone wants a finer p-value.

---

## Slide 10: Open questions for the room

**Visual**: 3 numbered questions, large font, no other content.

1. **To Prof. Hacker**: do you have access to ESMUC multitrack data we could fold into Tier-2 alongside Dagstuhl? (ChoralSynth we can acquire ourselves; it's openly licensed on Zenodo at DOI 10.5281/zenodo.10137883.)
2. **To Prof. Gloor**: for the final paper figure, do you prefer matplotlib-clean or Gephi/Cytoscape SVG-polished for the alchemical-stage diagram?
3. **To the coordinators**: is there a path to compute time on the Bamberg or HSLU university cluster for the Sprint-4 Tier-3 latency-injection runs? Per-window Granger on the full corpus is the bottleneck and a cluster would unblock it.

Thank you. Questions.
