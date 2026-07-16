# Jul 23 Final Presentation, Deck

**Project 8 - Entanglement in Online Choir - 2026-07-23**

> 14 content slides + 1 backup, 20 min total including a 60-second live dashboard demo.
> Presenters: Hammad (slides 1-5), Zuraiz (slides 6-14 + demo).
> Speaker notes in `jul23_script.md`; Q&A bank in `jul23_qa_prep.md`.
> Every number on these slides traces to a repo CSV; sources are annotated in HTML comments.

---

## Slide 1: Title

**Final Presentation**

Project 8: Entanglement in Online Choir

SNA-OSN-M Summer 2026 - Uni Bamberg x Uni Koeln x HSLU

Team: Zuraiz, Hammad Anwar, Hassan Ahmed, Kumaran Vasu

Supervisors: Prof. Janine Hacker - Prof. Peter Gloor

2026-07-23

---

## Slide 2: The question

**Kicker**: QUESTION

When a choir sings together over the internet, the network is part of the instrument.

We measured what latency does to togetherness, using one score over time: **E(t)**, a coordination index combining audio, network, and visual signals.

Three hypotheses:

- **H1**: Higher latency reduces choir coordination. Metric: zero-lag onset synchrony; predicted to fall.
- **H2**: Influence networks show leadership structure. Metric: out-degree Gini vs a matched random null; predicted above null.
- **H3**: Visual body signals add information beyond audio. Metric: first visual-onset coupling; ΔR² test requires paired data.

**Takeaway**: three testable claims, each with an operational metric and a predicted direction, fixed before the analyses.

---

## Slide 3: Data: three tiers, one honest constraint

**Kicker**: DATA

| Tier | What it is | What it gives us |
|:--|:--|:--|
| Tier 1 | 29 YouTube virtual-choir videos (18 pose-usable) | Visual signals: sway, breathing gestures |
| Tier 2 | Multitrack corpora: Dagstuhl (5), ESMUC (3), ChoralSynth (20) | Per-singer audio, influence networks |
| Tier 3 | Controlled latency injection on Tier 2 | Ground-truth latency variation |
<!-- piece counts: data/processed/tier3/_latency_grid_2000.csv (28 pieces); tier1 counts: data/processed/tier1/_pose_summary.csv -->

The honest constraint: **no piece has audio, video, and network signals together**. Tier 2 has audio without video; Tier 1 has video without per-singer audio. That constraint shapes what each hypothesis can claim.

**Takeaway**: two real corpora, one synthetic control, one visual corpus, used for what each is actually good for.

---

## Slide 4: Method: E(t) and the latency grid

**Kicker**: METHOD

E(t) = equal-weight blend of acoustic coupling A(t), visual coupling V(t), network coupling N(t), computed in sliding windows.

Latency grid: each clean multitrack piece is degraded through five regimes, then every metric is recomputed per piece and regime:

| Regime | Delay (ms) | Jitter SD (ms) | Dropout |
|:--|--:|--:|--:|
| clean | 0 | 0 | 0% |
| in-person threshold (ept) | 25 | 10 | 0% |
| Jamulus LAN | 47 | 46 | 1% |
| Jamulus WAN | 83 | 57 | 3% |
| Zoom-class | 150 | 80 | 8% |
<!-- source: data/processed/tier3/_latency_grid_2000.csv, delay_ms/jitter_sd_ms/dropout_rate per level -->

Statistical floor: envelope and influence-network results use a **circular-shift null** that preserves each stream's own autocorrelation; the final grid uses **2000 shuffles per cell** (paper-grade rerun on the NHR@FAU cluster, 2026-07-14). H1 onset inference uses a paired clean-to-Zoom sign test across pieces.

**Takeaway**: known degradation by construction, with every piece serving as its own control.

---

## Slide 5: The pipeline is reproducible

**Kicker**: METHOD

- One command (`make reproduce`) regenerates the headline results from the committed data summaries.
- 48 automated tests cover audio, video, network, latency, entanglement, H3, and report generation.
- The 2000-shuffle grid ran as 140 SLURM array tasks; the submission script is committed and cluster-validated.
- Every deck number traces to a committed CSV; the audit trail is in the repo.

**Takeaway**: the numbers you are about to see can be regenerated without us in the room.

---

## Slide 6: H1 result: latency breaks timing, not loudness

**Kicker**: RESULT

Onset synchrony (do singers land notes together?) falls monotonically from clean to Zoom-class jitter:

- Dagstuhl (real): **-56.5%**
- ESMUC (real): **-65.1%**
- ChoralSynth (synthetic): **-75.1%**
- Corpus (28 pieces): **-70.7%**
<!-- source: data/processed/tier3/_latency_grid_2000.csv, onset_sync pivot clean vs zoom -->

Loudness-envelope coupling does **not** degrade: envelope E(t) stays flat on Dagstuhl (-0.4%) and even rises slightly at corpus level under jitter.
<!-- source: same CSV, E_mean pivot: dagstuhl -0.4%, corpus -10.9% i.e. slight rise -->

All **28 / 28 pieces** decrease; exact one-sided paired sign-test p = **3.73 x 10^-9**.
<!-- source: data/processed/tier3/_h1_paired_test.csv -->

**Visual**: `data/figures/tier3_corpus_summary.png`

**Takeaway**: H1 is supported in the timing channel. Latency breaks *when* singers land notes, not how loud they are; an envelope-only metric would have missed it.

---

## Slide 7: Why the dissociation is the finding

**Kicker**: RESULT

Our first method (constant delay, envelope coupling) showed **no effect**. Its own control caught the confound: envelope coupling is lag-tolerant, and constant delay is exactly what it tolerates.

The fix was chosen a priori: zero-lag onset synchrony is the physical quantity that jitter should break. It recovered the effect in every piece.

- The negative result was kept and reported, not deleted.
- The dissociation (timing collapses, loudness holds) is itself the scientific claim.
- Replicated across two real corpora and one independent synthetic corpus.

**Takeaway**: the method audit trail is part of the result.

---

## Slide 8: H2 result: limited leadership evidence

**Kicker**: RESULT

Leader dominance, operationally: **Gini coefficient of out-degree** in the Granger-causal influence graph. 0 = democratic; toward 1 = one singer drives the rest.

Observed corpus mean **0.162** vs density-matched random null **0.155** (1000 draws per piece):

- Dagstuhl: **1 / 5** pieces significant.
- ESMUC: **1 / 3** pieces significant.
- ChoralSynth: **0 / 20** pieces significant.
<!-- source: data/processed/tier3/_h2_centralization.csv, regenerated from _latency_grid_2000.csv with rounding-safe plus-one p-values -->

**Visual**: `data/figures/wp3_flagship_LI_QuartetA_Take02_standard.png`

**Takeaway**: H2 receives limited support: two human pieces are centralized and no synthetic piece is, but the pooled effect is small. The latency-driven form remains untestable with injected delay.

---

## Slide 9: H3 result: an honest null, and what it teaches

**Kicker**: RESULT

First visual-onset attempt, as planned since Jun 25: pair the audio onset envelope with pose-derived motion on the 18 pose-usable Tier-1 videos (first-minute window, max-lag correlation, 1000 circular-shift nulls per video).

Result: **null**.

- 17 of 18 videos analyzable (one has a digitally silent first 90 s).
- **1 / 17 significant** at p < 0.05, which is chance expectation.
- Median max-lag r = **0.068**.
<!-- source: data/processed/tier1/_h3_visual_onset.csv -->

The measurement itself is validated on synthetic coupled signals (it recovers known lags and rejects independent streams), so the null is informative: **ensemble-level motion of one tracked stream does not couple to a mixed audio envelope**. H3's ΔR² claim remains data-blocked; it needs per-singer audio and video together.

**Visual**: `data/figures/h3_visual_onset.png`

**Takeaway**: we ran the promised experiment, it said no, and we report that. The data requirement for H3 is now demonstrated, not assumed.

---

## Slide 10: Live demo: E(t) on real recordings

**Kicker**: DEMO

60-second live dashboard run:

1. Audio/network piece (Dagstuhl quartet): E(t) timeline updating with the influence graph.
2. Video/pose piece (Tier-1): video playback with the live pose overlay.

The metadata panel shows which signals each piece really has; the demo does not pretend any piece has all three.

**Takeaway**: the platform is real and local-first; the presentation laptop holds the required media and feature files.

---

## Slide 11: Fallback: dashboard on real outputs

**Kicker**: DEMO

**Visual**: `data/figures/wp4_dashboard_realdata.png`

(Backup slide in case the live demo cannot run: same content as the demo, one frame.)

---

## Slide 12: Limitations, stated plainly

**Kicker**: LIMITS

- **Simulated latency**: injection into pre-recorded audio models transmission, not live behavioural adaptation of singers.
- **Signal split**: no piece carries audio + video + network together; E(t) has never been computed with all three channels live.
- **H3 window**: pose covers one tracked stream over the first minute of each video only.
- **Null caveats**: a minority of individual grid cells are not significant against their null; corpus-level trends carry the claims.
- **E(t) domain transfer**: the entanglement formula was validated on email networks; this is its first music-domain test.

**Takeaway**: each limitation is registered, owned, and either mitigated or explicitly left as future work.

---

## Slide 13: Contributions

**Kicker**: CLOSE

1. **A latency signature for online choirs**: timing collapses 56 to 75 percent while loudness coupling holds; all 28 pieces decrease (paired sign-test p = 3.73 x 10^-9).
2. **An operational leadership measure** with limited evidence in two human pieces and none of 20 synthetic pieces.
3. **A demonstrated data requirement for visual entanglement**: the first visual-onset experiment, honestly null.
4. **An open, reproducible pipeline**: one command, 48 tests, cluster-validated batch protocol, every report claim traceable to a committed artifact.

**Takeaway**: supported, partially supported, honestly null, and all of it reproducible.

---

## Slide 14: What comes next, and thanks

**Kicker**: NEXT

- Record real latency-varied live sessions (the only way to test H1 without simulation and H2's latency form).
- Build a small paired corpus (per-singer audio + video) to unlock the H3 ΔR² test.
- Final seminar report ready as Markdown and a 10-page PDF.

Thank you. Questions welcome.

---

## Backup slide: Reproducibility protocol

**Kicker**: BACKUP

- `make reproduce` regenerates report-stage results and the final PDF from committed artifacts.
- H1 inference: `scripts/h1_paired_test.py`, exact paired sign test plus seeded bootstrap.
- 2000-shuffle grid: `scripts/hpc/tier3_2000.sbatch`, 140 array tasks (28 pieces x 5 levels), merged and completeness-checked by `scripts/tier3_merge_shards.py`.
- H3 experiment: `uv run python -m scripts.h3_visual_onset` (deterministic seeds).
- Environments pinned: Python 3.11.9, locked dependencies, `uv sync --extra all`.
