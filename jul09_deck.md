# Jul 9 Status Meeting VI, Deck

**Project 8 - Entanglement in Online Choir - 2026-07-09 - 14:00-16:00 CET**

> 9 slides, 8-10 min spoken. Presenter: Zuraiz, with team support. Speaker notes in `jul09_script.md`; Q&A bank in `jul09_qa_prep.md`. This is the final status meeting before the Jul 23 final presentation.

---

## Slide 1: Title

**Status Meeting VI**

Project 8: Entanglement in Online Choir

SNA-OSN-M Summer 2026 - Uni Bamberg x Uni Koeln x HSLU

Presented by Zuraiz, on behalf of the team

Supervisors: Prof. Janine Hacker - Prof. Peter Gloor

2026-07-09 - 14:00 CET

---

## Slide 2: Goals and plan

**Kicker**: RECAP

We are measuring how well online choirs coordinate when singers are not in the same room.

Our metric is **E(t)**: one coordination score over time from audio, network, and visual signals.

Project questions:

- **H1**: Does higher latency reduce choir coordination?
- **H2**: Do influence networks show leadership structure?
- **H3**: Do visual and body signals add information beyond audio?
- **Plan**: use verified datasets, write the report, and prepare a final dashboard demo.

**Takeaway**: Today we connect the project goal to the latest results and the final-presentation plan.

---

## Slide 3: Progress during the last iteration

**Kicker**: PROGRESS

Since Status Meeting V, we completed the Jul-9 report checkpoint.

What was done:

- Report draft v1 now writes up the H1 result.
- H1 is ready to use in the report as the main timing result.
- H2 has a cleaner interpretation: weak leadership signal in human choir networks.
- H3 remains open because the needed paired audio-video data is unavailable.
- Status VI slides, script, and Q&A notes are prepared.

**Takeaway**: the work moved from finding results to preparing the final presentation and report.

---

## Slide 4: Report draft v1 is ready for review

**Kicker**: PROGRESS

**Report draft v1 is ready for review** (`report_draft_v1.md`, 2026-06-30).

It contains:

- Abstract, hypotheses, data, methods, results, limitations, conclusion.
- H1 as the headline result.
- H2 as a measured leadership signal in human datasets.
- H3 as an open data-availability limitation.

**Claim status in the draft**:

| Claim | Status |
|:--|:--|
| H1 latency | Supported in the onset-timing channel |
| H2 leadership | Partially supported in human datasets |
| H3 visual contribution | Open, paired audio-video data unavailable |

**Takeaway**: the Jul-9 report milestone from Status Meeting V is met.

---

## Slide 5: H1 result summary

**Kicker**: RESULT

The H1 result is a timing dissociation:

- **Onset synchrony falls strongly** as jitter rises.
- **Loudness-envelope coupling stays almost flat**.
- Therefore latency breaks **when singers land notes**, not how loud they are.

Cross-dataset drop from clean to Zoom-class jitter:

- Dagstuhl: **57%** drop.
- ESMUC: **66%** drop.
- ChoralSynth: **76%** drop.

**Visual**: `data/figures/tier3_corpus_summary.png`

**Takeaway**: an envelope-only metric would have missed the real latency effect.

---

## Slide 6: H2 result summary

**Kicker**: RESULT

The original H2 asked whether networks become more leader-dominated as latency rises. This cannot be tested cleanly with injected delay on pre-recorded audio.

**Definition (operational, answering the Status-V question)**: leader dominance = **out-degree centralization of the directed influence graph**, measured as the **Gini coefficient of node out-degree**. 0 = every singer exerts equal outgoing influence (democratic); toward 1 = one singer Granger-causes the others without following back (a leader). Test: observed Gini vs 1000 random graphs of identical size and density. Observed corpus mean 0.154 vs null 0.139.

**Current H2 result**:

Clean human choir influence networks show weak leadership structure above a density-matched random null.

Evidence:

- Dagstuhl: 3 / 5 pieces significant.
- ESMUC: 2 / 3 pieces significant.
- ChoralSynth: 2 / 20 pieces significant, approximately chance.

**Takeaway**: leadership appears as a human coordination signal, not a synthetic-rendering artifact.

---

## Slide 7: Dashboard alpha uses real outputs

**Kicker**: PROGRESS

Dashboard alpha is real-data based:

- E(t) timeline from the real entanglement pipeline.
- Influence graph from real Granger GEXF.
- Pose overlay from real MediaPipe parquet.
- Metadata shows which signals each piece actually has.

**Visual**: `data/figures/wp4_dashboard_realdata.png`

This screenshot shows the current real-data dashboard alpha. It is included here to discuss the final demo plan, not as a new result.

Demo structure:

- Audio/network example: shows E(t) and influence graph.
- Video/pose example: shows video playback and pose overlay.

**Takeaway**: the final demo can be clear and honest even though no current piece has all three signals.

---

## Slide 8: Plan for the next iteration

**Kicker**: NEXT

The next iteration is the final presentation and report phase.

| Track | Plan |
|:--|:--|
| Final presentation | Build the 20-minute Jul-23 deck and demo narration |
| Report | Convert draft v1 into the final 10-20 page seminar report |
| Reproducibility | Run final checks and regenerate headline figures |
| Dashboard | Prepare the presentation laptop and rehearse the demo path |
| Limitations | Present H3 and latency-driven H2 as open questions for future data |

**Takeaway**: the remaining work is final packaging, verification, and rehearsal.

---

## Slide 9: What we need to align before the final presentation

**Kicker**: ALIGNMENT

Output from the retrospective:

- Null results were kept and explained instead of removed.
- The constant-delay result led to the stronger jitter/onset analysis.
- Dataset claims now trace to project files and generated outputs.

Final presentation structure:

- Project problem and goal.
- Research question and hypotheses.
- Method and datasets.
- Results and interpretation.
- Implementation: dashboard and reproducibility.
- Limitations and next steps.

Questions for feedback:

- **Final structure**: research question, hypotheses, method, results, implementation, limitations, next steps.
- **Main focus points**: which parts should receive the most attention in the final presentation?
- **Dashboard format**: is a dashboard screenshot enough, or should we show the dashboard live?

Thank you.
