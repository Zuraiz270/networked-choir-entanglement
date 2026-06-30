# Measuring Coordination in Online Choirs: an Entanglement Index and the Latency Signature of Ensemble Timing

**Report draft v1 (internal seminar report)** · SNA-OSN-M Summer 2026 · Uni Bamberg × Uni Köln × HSLU
Lead author: Zuraiz. Co-authors: Hammad Anwar, Hassan Ahmed, Kumaran Vasu.
Supervisors: Prof. Janine Hacker (Uni Bamberg), Prof. Peter Gloor (Köln / ex-MIT).
Draft date: 2026-06-30. Status: v1, for the Jul-9 review. All numbers trace to files under `data/processed/`.

---

## Abstract

When choirs perform over the internet, network latency degrades coordination, but the field lacks a quantitative measure of how much, and of what. We define an Entanglement Index E(t) that combines audio coupling, visual coupling, and influence-network coherence into a single coordination score, and we test three hypotheses on a corpus of 28 multitrack pieces across three datasets (two real human, one synthetic) plus 29 networked-performance videos. Our central finding is a dissociation: simulated network jitter sharply degrades the timing of note attacks (zero-lag onset synchrony falls 57 to 76 percent from clean to Zoom-class latency, across all 28 pieces and all three datasets), while loudness-envelope coupling is left almost untouched. A naive envelope-based metric would have concluded, wrongly, that latency does not matter. We further show that real human choir influence networks carry weak but statistically significant leadership structure that is absent in synthetic renderings. We report two hypotheses (visual contribution, latency-driven leadership) as currently untestable with available data, and we are explicit about the limitation that our latency is injected into pre-recorded audio rather than recorded live under latency.

---

## 1. Introduction

During COVID, choirs moved online and immediately hit a wall: singing together over Zoom "felt wrong" in a way that low-latency tools such as Jamulus and SoundJack only partly fixed. Networked Music Performance (NMP) tool makers design by intuition, music educators plan by anecdote, and researchers cannot compare one setup to another, because there is no number for how well a remote ensemble is actually coordinating.

We build that number. Choirs are a good testbed because coordination is acoustically measurable: two singers either attack a note together or they do not, and the recording shows it in milliseconds.

The project tests a binary that is publishable either way. **Either** latency is a hard ceiling on coordination (so NMP tools need new architectures), **or** human performers compensate through other channels such as visual cues (so Pentland's Honest Signals view gets a clean external test). This report's result speaks to the first horn: latency degrades coordination specifically in the timing channel.

### 1.1 Hypotheses (operationalized)

| # | Statement | Metric | Prediction | Status in this report |
|:--|:--|:--|:--|:--|
| **H1** | Higher network latency lowers coordination | E(t) and its sub-signals; zero-lag onset synchrony | synchrony decreases monotonically with injected jitter | **Supported** (in the onset-timing channel) |
| **H2** | Choir influence networks carry leadership structure | out-degree centralization (Gini of out-degree) vs density-matched random null | observed centralization > random | **Partially supported** (human datasets only); latency-driven version data-blocked |
| **H3** | Visual signals add coordination information beyond audio | delta-R^2 of V(t) over audio-only | visual adds >= 10 points | **Data-blocked** (no piece has audio and video together) |

---

## 2. Background

- **Latency thresholds.** The Ensemble Performance Threshold for synchronous playing is about 25 ms one-way (Chafe and colleagues, CCRMA hand-clapping studies); natural interaction needs under about 30 ms; consumer videoconferencing runs 100 to 150 ms. The only controlled measurement of inter-chorister timing in a choral-NMP system we found reports 47 +/- 46 ms (Jamulus LAN) and 83 +/- 57 ms (Jamulus WAN) (P-11). We treat round numbers like a "100 ms cliff" as design folklore, not measured thresholds; accordingly H1 is framed as regime discrimination, not cliff location.
- **Honest Signals.** Pentland treats micro-timing and synchrony as a core, largely involuntary channel of human coordination. Our finding that latency degrades attack timing specifically (rather than loudness) sits naturally in this frame.
- **Causality in ensembles.** Granger causality on per-singer onset or envelope series yields a directed "who-leads-whom" influence graph; we run both standard parametric Granger and the ordinal-pattern variant COP-GC (Zanin 2024), which captures non-linear couplings the parametric test misses.

---

## 3. Data

| Dataset | Type | Pieces used | License | Role |
|:--|:--|:--:|:--|:--|
| Dagstuhl ChoirSet | real, multitrack | 5 | CC BY 4.0 | Tier-2 audio + network |
| ESMUC Choir Dataset | real, multitrack | 3 | CC BY 4.0 | Tier-2 audio + network |
| ChoralSynth | synthetic, per-voice | 20 | CC BY-SA 4.0 | Tier-2 audio + network |
| Tier-1 YouTube | mixed-stereo video | 29 (18 pose-usable) | per-video | Tier-1 video + pose |

All Tier-2 archives were downloaded from Zenodo and verified against the upstream MD5 (provenance in `data/raw/_dataset_inventory.md` and `_dataset_checksums.csv`). On inspection ESMUC is 7 song-codes across full-take / section / excerpt settings (48 multitrack groups, 16 full-ensemble takes), not the "3 pieces" the source paper implies; we use full-ensemble takes. ChoralSynth audio is per-voice MP3, decoded via libsndfile. No piece in the corpus carries audio and video together, which is what blocks H3.

---

## 4. Methods

### 4.1 The Entanglement Index

E(t) is computed on a common time grid as the mean of the available sub-signals, so it is defined even when one is missing (which is the realistic case here):

- **A(t), audio coupling**: mean absolute windowed Pearson correlation of per-singer RMS envelopes over a 10 s sliding window.
- **V(t), visual coupling**: variance of pose-derived honest-signal features (shoulder rise, head sway, trunk lean) over the same window. Absent for audio-only datasets.
- **N(t), network coherence**: density of the Granger influence graph.
- **E(t) = mean(A, V, N)** over whichever signals are present (`src/choir_entanglement/entanglement.py`).

Significance uses a circular-shift null (200 shuffles), which preserves within-stream autocorrelation, unlike an i.i.d. shuffle.

### 4.2 Onset synchrony (the timing channel)

Because A(t) cross-correlation searches over lags, it is by design tolerant to a constant offset. To measure whether singers attack notes *at the same instant*, we add a zero-lag measure: each binary onset train is smoothed with a +/- tolerance box (about 70 ms, near the Ensemble Performance Threshold) and the two smoothed trains are compared by zero-lag Pearson correlation (`onset_synchrony` in `audio/coupling.py`). Unlike A(t), this cannot absorb a timing shift.

### 4.3 Tier-3 latency injection

We simulate NMP regimes by perturbing clean multitrack audio. The reference singer is held fixed and the others are delayed. We tested two manipulations:

1. **Constant delay** (a fixed per-regime offset).
2. **Jitter + dropout**: per-frame Gaussian jitter whose SD is taken from the measured P-11 inter-chorister timing SD (46 ms LAN, 57 ms WAN), plus packet-loss dropout, with packet-loss concealment (hold-last-value) before any Granger step.

The grid covers 5 regimes (clean, EPT 25 ms, Jamulus LAN, Jamulus WAN, Zoom 150 ms) over 28 pieces, 140 cells total (`scripts/tier3_latency_grid.py`, `data/processed/tier3/_latency_grid.csv`).

### 4.4 H2: leadership structure

For each clean piece we compare observed out-degree centralization (Gini of node out-degree in the Granger graph) against an Erdos-Renyi null with the same node and edge count (1000 draws), two-sided empirical p (`scripts/h2_centralization_test.py`).

---

## 5. Results

### 5.1 H1: latency degrades attack timing, not loudness (the headline)

The two manipulations told a two-step story, which we report in full because the dead end is itself informative:

1. **Constant delay does nothing to E(t).** The envelope coupling is lag-tolerant by design, so a constant shift slides inside its search window and is absorbed.
2. **Realistic jitter still leaves E(t) flat**, because a 10 s loudness envelope is physically robust to tens-of-ms timing noise.
3. **Zero-lag onset synchrony, by contrast, falls sharply and monotonically** with jitter, on every piece and in every dataset:

| Dataset | pieces | onset synchrony, clean | Zoom-class | drop |
|:--|:--:|:--:|:--:|:--:|
| Dagstuhl (real) | 5 | 0.287 | 0.124 | **-57%** |
| ESMUC (real) | 3 | 0.254 | 0.087 | **-66%** |
| ChoralSynth (synthetic) | 20 | 0.308 | 0.075 | **-76%** |

Loudness-envelope coupling moves by under 10 percent across the same range. The dissociation (`data/figures/tier3_corpus_summary.png`) is the contribution: **latency breaks *when* singers land notes, not *how loud* they are.** A loudness-only metric would have missed the effect entirely.

### 5.2 H2: weak leadership structure in human choirs, absent in synthetic

Across 28 clean pieces, observed out-degree centralization is modestly above the density-matched random null (mean Gini 0.154 vs 0.139). The effect concentrates in the **human** datasets:

| Dataset | obs Gini | null Gini | pieces significant (p<0.05) |
|:--|:--:|:--:|:--:|
| Dagstuhl | 0.064 | 0.052 | 3 / 5 |
| ESMUC | 0.109 | 0.082 | 2 / 3 |
| ChoralSynth | 0.184 | 0.169 | 2 / 20 |

So 5 of 8 real human pieces carry significant leadership structure, versus 2 of 20 synthetic pieces (at chance). The interpretation is clean: leadership is a human coordination phenomenon, weak but present, and machine-rendered voices do not reproduce it. We do **not** claim strong hierarchy; the effect is small.

### 5.3 H3: not testable with current data

H3 needs a piece with both audio and video. None exists in the corpus (Dagstuhl and ESMUC are audio-only; Tier-1 YouTube is video with mixed audio). The integration code is ready for V(t); the data is the blocker.

---

## 6. Discussion

The result favours the "latency is a hard ceiling" horn of the binary, but with a precise refinement: the ceiling acts on **attack timing**, the involuntary micro-timing channel that Honest Signals theory treats as central to coordination. This is also a methodological lesson, the choice of measure decides the conclusion: a lag-tolerant or envelope-based coordination metric is blind to exactly the degradation that matters.

On leadership (H2), real choirs are close to democratic in their mutual influence at zero latency, with only a weak leadership gradient, and synthetic choirs show none. Whether latency *intensifies* leadership (the original H2) is the question we cannot answer here, and Section 7 explains why.

---

## 7. Limitations (stated plainly)

1. **Latency is injected, not recorded live.** We perturb pre-coordinated studio audio. This models transmission delay but not a live singer's behavioural adaptation to hearing others late. The H1 effect should be read as "the timing structure that latency destroys," not as a measurement of live remote performance.
2. **The latency-driven version of H2 is untestable with this design.** Injecting a uniform delay cannot create a behavioural leader, and fixed-lag Granger spuriously connects delayed streams (graph density rises and centralization washes out). Testing it needs real low-vs-high-latency live recordings, or a delay-robust causality measure.
3. **H3 is data-blocked**: no multimodal (audio + video) piece.
4. **ChoralSynth is synthetic**: its coupling is weaker and its leadership absent, so it serves as a contrast corpus, not as primary human evidence.
5. **Significance null sizes**: the per-cell coordination null uses 200 shuffles, the grid uses 100; a paper-grade rerun would use 2000 (an overnight laptop run, no special hardware needed).

---

## 8. Conclusion and next steps

We deliver a working Entanglement Index and a clear, replicated H1 result: network jitter degrades choral attack-timing synchrony by 57 to 76 percent across three datasets, while leaving loudness coupling intact. We add a modest H2 finding (human-only leadership structure) and are explicit that the visual hypothesis and the latency-driven leadership question remain open for lack of the right data.

**Next:**
- First V(t) attempt for H3: pair pose onsets with audio onsets on the 18 pose-usable Tier-1 videos.
- Paper-grade rerun of H1 at 2000 shuffles.
- Pursue real latency-varied live recordings (the only way to test H2's latency form and H1 without the simulation caveat).

---

## Appendix: reproducibility

Every figure and number regenerates from committed code and data: H1 grid `scripts/tier3_latency_grid.py` -> `_latency_grid.csv`; H2 `scripts/h2_centralization_test.py` -> `_h2_centralization.csv`; figures via `scripts/tier3_corpus_figure.py`. Datasets are Zenodo downloads with MD5 recorded in `data/raw/_dataset_checksums.csv`. Test suite: 38 passing.
