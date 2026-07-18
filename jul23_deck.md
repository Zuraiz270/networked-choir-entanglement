# Jul 23 Final Presentation, Deck

**Project 8 - Entanglement in Online Choir - 2026-07-23**

> 17 presentation slides + 2 backup slides, 10-12 minutes plus 3 minutes Q&A.
> Presenters: Hammad (slides 1-8), Zuraiz (slides 9-17 + demo).
> Speaker notes in `jul23_script.md`; Q&A bank in `jul23_qa_prep.md`.
> Every numerical claim traces to a committed CSV.

---

## Slide 1: Title

**Measuring Coordination in Online Choirs**

Project 8: Entanglement in Online Choir

Team: Zuraiz, Hammad Anwar, Hassan Ahmed, Kumaran Vasu

Supervisors: Prof. Janine Hacker and Prof. Peter Gloor

2026-07-23

---

## Slide 2: Goals and hypotheses

**Goal**: measure how network conditions affect choir coordination and build a reproducible system for inspecting acoustic, visual, and influence-network signals.

- **H1**: Higher latency reduces choir coordination. Primary outcome: zero-lag onset synchrony.
- **H2**: Choir influence networks show leadership structure. Outcome: out-degree Gini versus matched random graphs.
- **H3**: Visual body signals add information beyond audio. Full test: audio-only versus audio-plus-visual prediction.

**Takeaway**: the hypotheses and directions were declared at project start; operational metrics were refined in documented, dated revisions.

---

## Slide 3: Related work and research gap

- **Entanglement**: temporal alignment has been measured in organizational communication networks.
- **Honest Signals**: activity, consistency, influence, and mimicry can reveal group coordination.
- **Choir and NMP research**: multitrack corpora and latency studies provide audio evidence, but not one integrated acoustic, visual, and influence measure.

**Research gap**: adapt these ideas to singing, test the operational measures against controlled network degradation, and state where the available data cannot support a claim.

---

## Slide 4: Whole-project structure

**Visual**: `data/figures/project_structure.png`

The project links three data tiers to audio, video, and network pipelines, then to H1, H2, H3, the dashboard, and the final research outputs.

**Takeaway**: every result has a visible path from source data to tested claim.

---

## Slide 5: Data and the multimodal constraint

| Tier | Material | Main use |
|:--|:--|:--|
| Tier 1 | 29 virtual-choir videos; 18 pose-usable | Visual extraction and exploratory H3 |
| Tier 2 | Dagstuhl 5, ESMUC 3, ChoralSynth 20 | Per-singer audio and H2 networks |
| Tier 3 | Five controlled degradation regimes on 28 pieces | H1 latency experiment |

No piece has synchronized per-singer audio and per-singer video. Tier 1 has video with mixed audio; Tier 2 has per-singer audio without video.

**Takeaway**: each dataset is used only for the claims it can support.

---

## Slide 6: Method and controlled latency grid

E(t) combines available acoustic A(t), visual V(t), and network N(t) coordination components.

| Regime | Delay | Jitter SD | Dropout |
|:--|--:|--:|--:|
| Clean | 0 ms | 0 ms | 0% |
| In-person threshold | 25 ms | 10 ms | 0% |
| Jamulus LAN | 47 ms | 46 ms | 1% |
| Jamulus WAN | 83 ms | 57 ms | 3% |
| Zoom-class | 150 ms | 80 ms | 8% |

The same piece appears in every regime. Envelope and network analyses use 2,000 circular shifts per cell; H1 onset inference uses the paired clean-to-Zoom sign test.

---

## Slide 7: Work process

- Four connected work packages: acoustic/integration, visual extraction, influence networks, and dashboard/report integration.
- Each iteration ended in a reviewable schema, result table, test, figure, or presentation artifact.
- Reproducibility was built into the workflow through seeded scripts, committed summaries, and independent audits.
- Virtual Mirror result: high shared meaning, low emotional exchange, medium relationship intensity; the team adopted a short weekly asynchronous check-in.

**Takeaway**: clear ownership plus explicit review gates kept the work packages connected.

---

## Slide 8: Reproducibility

- `make reproduce` regenerates report-stage statistics, figures, and the PDF from committed summaries.
- 50 automated tests cover audio, video, network, latency, entanglement, dashboard consistency, figure definitions, H3, and report generation.
- The final 2,000-shuffle grid contains 140 complete cells from a committed SLURM protocol.
- Every deck number traces to a committed CSV.

**Takeaway**: the results can be audited without relying on the presentation.

---

## Slide 9: H1 result, latency breaks timing

Dataset-level onset synchrony decreases from clean to the Zoom-class regime, where delay, jitter, and dropout co-vary:

- Dagstuhl: **-56.5%**
- ESMUC: **-65.1%**
- ChoralSynth: **-75.1%**
- Corpus: **-70.7%**

All **28 of 28 pieces** decrease from clean to Zoom-class; exact one-sided sign-test p = **3.73 x 10^-9**.

Envelope coupling degrades an order of magnitude less: A(t) falls 7.9% on Dagstuhl and 11.9% at corpus level. The envelope-plus-network composite E(t) stays flat or rises because network density offsets the envelope decline.

**Visual**: `data/figures/tier3_corpus_summary.png`

---

## Slide 10: Why the measurement revision matters

The first constant-delay test used lag-tolerant envelope coupling and showed little effect. Its control exposed a mismatch between the manipulation and the metric.

- The null result was retained and explained.
- Zero-lag onset synchrony directly measures simultaneous note attacks.
- Timing falls 56% to 75%, while the pure envelope channel falls roughly 6% to 14% across corpora.
- The hypotheses stayed fixed; the operational metric revision is dated and reproducible.

**Takeaway**: measurement choice changes the conclusion, so the audit trail is part of the result.

---

## Slide 11: H2 result, limited leadership evidence

Leadership is measured as the Gini coefficient of out-degree in the Granger influence graph: 0 means equal outgoing influence; larger values mean influence is concentrated.

Observed corpus mean **0.162** versus matched-null mean **0.155**:

- Dagstuhl: **1 of 5** pieces significant.
- ESMUC: **1 of 3** pieces significant.
- ChoralSynth: **0 of 20** pieces significant.

**Visual**: `data/figures/wp3_flagship_LI_QuartetA_Take02_standard.png`

**Takeaway**: H2 has limited support in two human pieces; the corpus-level evidence is not significant and requires replication.

---

## Slide 12: H3 result, an informative null

Pose-derived motion was paired with the mixed-audio onset envelope over each video's first **60-72 s pose window** (the exact window is recorded per video), using maximum signed correlation within 2 seconds and 1,000 circular-shift nulls.

- 17 of 18 pose-usable videos were analyzable.
- **1 of 17** was significant at p < 0.05, consistent with chance.
- Median maximum-lag r = **0.068**.

**Visual**: `data/figures/h3_visual_onset.png`

**Takeaway**: the exploratory substitute is null; the full H3 comparison still requires synchronized per-singer audio and video.

---

## Slide 13: Live dashboard demonstration

60-second run on the presentation laptop:

1. Dagstuhl audio/network piece: E(t) timeline and influence graph.
2. Tier-1 video piece: playback with pose overlay.
3. Signal-availability metadata: which channels each piece actually contains.

The live dashboard uses the same envelope-only E(t) definition as the published report values.

---

## Slide 14: Limitations

- Injected latency models transmission, not live singer adaptation.
- Delay, jitter, and dropout co-vary across the five regimes, so their effects are not isolated.
- No item contains synchronized per-singer audio and video.
- H2 has only two individually significant pieces and no corpus-level significance.
- E(t) is a proposed music-domain adaptation, not yet externally validated against perceived performance quality.

---

## Slide 15: Main results and implementation

1. **H1 supported for timing**: all 28 pieces lose onset synchrony, with a 70.7% corpus mean drop.
2. **H2 limited**: two human pieces show significant centralization; the overall evidence remains weak.
3. **H3 exploratory null**: mixed audio plus one pose stream does not substitute for paired per-singer data.
4. **Implementation delivered**: reproducible analysis pipelines, tested dashboard, figures, final report, and presentation package.

---

## Slide 16: Possible extensions

- Record live latency-varied choir sessions to measure behavioral adaptation and latency-driven leadership.
- Build a synchronized per-singer audio-video corpus for the planned H3 incremental-validity test.
- Separate delay, jitter, and dropout in a factorial experiment.
- Validate E(t) against expert ratings, singer experience, and score-alignment errors.

---

## Slide 17: Retrospective and closing

**What worked well**

- Controls exposed the first metric mismatch instead of hiding it.
- Seeded scripts, tests, and audits made every final claim traceable.
- Instructor questions improved the operational definitions and limitation framing.

**What could improve**

- Secure suitable paired multimodal data earlier.
- Resolve cross-work-package dependencies before parallel implementation.
- Confirm final format and metric expectations earlier in the course.

Thank you. Questions are welcome.

---

## Slide 18: Backup, dashboard screenshot

**Visual**: `data/figures/wp4_dashboard_realdata.png`

Use only if the live dashboard cannot run.

---

## Slide 19: Backup, reproducibility protocol

- `make reproduce` rebuilds report-stage results and the final PDF.
- H1: exact paired sign test plus seeded bootstrap.
- H2: 1,000 matched random graphs per piece with plus-one p-values.
- H3: deterministic seeds and 1,000 circular shifts per video.
- Environment: Python 3.11.9 and locked dependencies.
