---
title: P-14 huSync Model
type: source
alchemy_stage: nigredo
tags: [husync, pose_estimation, phase_locking_value, nmp, deep_read]
ingested_date: 2026-04-23
last_deep_read: 2026-04-23
source_count: 1
related: ["[[phase_locking_value]]", "[[musical_texture_effects]]", "[[deep_read_audit]]"]
team_take: Load-bearing for Project 8's V(t) and PLV framing. Strong statistics, but case study is 2 pieces from one ensemble with post-hoc video. AlphaPose v0.4 is older than the MediaPipe stack Project 8 will use.
---

# P-14 huSync - A Model and System for the Measure of Synchronization in Small Groups: A Case Study on Musical Joint Action

**Citation**: Sabharwal, S.R., Varlet, M., Breaden, M., Volpe, G., Camurri, A., Keller, P.E. (2022). *IEEE Access*, 10, 92357 to 92376. [DOI:10.1109/ACCESS.2022.3202959](https://doi.org/10.1109/ACCESS.2022.3202959). CC-BY-4.0.
**Institutions**: DIBRIS, University of Genoa (Italy); MARCS Institute, Western Sydney University (Australia); Center for Music in the Brain, Aarhus University & Royal Academy of Music Aarhus (Denmark).
**Funding**: EU H2020 EnTimeMent Project, Grant 824160.
**Ethics**: Western Sydney University Human Research Ethics Protocol H10487.
**raw path**: `raw/01_primary_sources/huSync_-_A_Model_and_System_for_the_Measure_of_Synchronization_in_Small_Groups_A_Case_Study_on_Musical_Joint_Action.pdf`

## 1. Method (exact)

**Pose estimation**: AlphaPose v0.4 [p. 92365, §V-C]. Head key-point = nose (key '0'). Distance-only (no velocity/acceleration derivatives because differentiation amplifies noise) [p. 92367, §VII-A].

**PLV formula** [p. 92359, Eq. 1]:

$$\text{PLV} = \frac{\left| \sum_{t=1}^{n} e^{i(\phi_1 - \phi_2)} \right|}{n}$$

where φ₁, φ₂ are phase angles of the two head-motion signals for a specific frequency bin, obtained via FFT. Range [0, 1]; 1 = perfect synchrony.

**Averaged PLV** [p. 92363, Eq. 3]: PLV computed per window × frequency bin, averaged across all frequency bins of interest.

**Processing parameters** [p. 92365, §V-C]:

- Sliding window size = **30** samples
- Step size = **5** samples
- Frequency cut-off = **10 Hz** (excludes DC component and bins above 11th)
- Savitzky-Golay filter evaluated but NOT applied (no material difference)
- Dataset divisibility constraint: total samples must be multiple of 5 (window step) AND 3 (start/middle/end trisection)

**Pair counts**: $C(n, 2) = n! / (2!(n-2)!)$. **6 pairs** for Borodin (n=4), **10 pairs** for Brahms (n=5) [p. 92365, §V-C].

## 2. Dataset

| Field | Value | Source |
| :--- | :--- | :--- |
| Ensemble | Omega Ensemble (professional chamber group, Australia) | [p. 92364, §V-A] |
| Venue | City Recital Hall, Sydney | [p. 92364, §V-A] |
| Concert date | 2017 | [p. 92364, §V-A] |
| Pieces | Brahms Clarinet Quintet B minor Op. 115 (1891) + Borodin String Quartet No. 1 A major (1874-79) | [p. 92364, §V-A] |
| Performers | Brahms: 5 (vln1, vln2, vla, vc, clarinet). Borodin: 4 (vln1, vln2, vla, vc) | [p. 92364 to 92365, §V-A] |
| Durations | Brahms 40 min 38 s; Borodin 39 min 13 s | [p. 92364, §V-A] |
| Video | Canon 1DX + 70 to 200 mm f/2.8L, 1920×1080 @ 25 fps, H.264 | [p. 92364, §V-A] |
| Audio | **Stereo mix only**, 16-bit, 48 kHz, Linear PCM (no multitrack) | [p. 92364, §V-A; p. 92366, §VI-B] |
| Annotation | ELAN tool, score-based musicological classification | [p. 92364 to 92365, §V-B] |
| Total selected phrases | **44** | [p. 92365, §VI] |
| Phrase criteria | ≥5 s per segment (start/middle/end trisection); all instruments playing; consistent instrument roles | [p. 92365, §V-B] |
| Texture levels | Binary: homophonic (melody + accompaniment, clear leader) vs. polyphonic (distributed leadership) | [p. 92365, §V-B] |

## 3. Raw Data Block (ANOVA results)

**Design**: ANOVA with Phrase Position (Start/Middle/End, within-subject) × Texture (Homophonic/Polyphonic, between-subject) × Pair (between-subject). Phrase duration included as covariate. Brahms and Borodin analyzed separately because of differing pair count. Ran in jamovi [p. 92365, §VI].

| Effect | Piece | Statistic | Value | p | Source |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Texture main effect | Brahms | F(1, 219) | **16.08** | **< 0.001** | [p. 92366, §VI-A] |
| Position × Texture | Brahms | F(2, 438) | **6.098** | **0.002** | [p. 92366, §VI-A] |
| Texture main effect | Borodin | F(1, 107) | **14.051** | **< 0.001** | [p. 92366, §VI-A] |
| Position × Texture | Borodin | F(2, 214) | **3.399** | **0.035** | [p. 92366, §VI-A] |
| Position main effect | both | — | n.s. | — | [p. 92366, §VI-A] |

**Direction of effect**: Polyphonic > Homophonic PLV throughout, with the gap largest at Start and Middle positions, compressing at End (polyphonic drops, homophonic rises at phrase endings).

## 4. Audio Cross-Validation (linear mixed effects)

**Model**: lmer in R. PLV ~ pulse_clarity + event_density + texture + phrase_position + (1 | piece). Arcsine transform on pulse clarity; log transform on event density. Audio features extracted via MIRtoolbox in MATLAB [p. 92366, §VI-B].

| Predictor | Likelihood-ratio test | Effect | Source |
| :--- | :--- | :--- | :--- |
| Event density | χ²(1) = **7.44**, p = **0.006** | β = **0.031**, SE = 0.011, t = 2.767, p = 0.006 | [p. 92366, §VI-B] |
| Pulse clarity | χ²(1) = 0.03, p = **0.884** | **[NOT-SIGNIFICANT]** | [p. 92366, §VI-B] |

Higher event density → higher PLV. Pulse clarity does not predict PLV.

## 5. Limitations

**Stated** [p. 92367 to 92368, §VII-A, §VIII-A, §VIII-B]:

- Video-based tracking has higher noise than marker-based MoCap, especially on velocity/acceleration derivatives (authors therefore used distance only).
- Figure-ground differentiation is critical for pose-estimation quality; small/distant/cluttered scenes (e.g., smaller venues, larger ensembles, audience heads in frame) "highly challenging."
- Seating position and camera angle influence detectable motion.
- Occlusions break down for multi-row ensembles (e.g., choirs). Multi-camera reconstruction proposed as future work.
- **No multitrack audio** — relied on indirect stereo-derived pulse clarity and event density. Per-instrument onset-level synchrony (the standard NMP audio metric) not available.
- Future work: Multi-Event Class Synchronization, Granger causality for leadership direction.

**Implicit (binding on any Project-8 citation)**:

- **n = 2 pieces, 1 ensemble, 1 session**. Generalization to other ensembles, genres, and cultural traditions is untested.
- Post-hoc analysis of existing concert video, not an experimental manipulation. No randomization, no controlled texture induction.
- **Head-only coupling** (nose key-point). Torso sway, hand motion, breathing, instrument-specific gestures all ignored.
- Binary texture classification (homophonic vs. polyphonic). Real musical texture space is richer; effect sizes on a coarser partition may over-state real-world discriminability.
- AlphaPose v0.4 (circa 2019 to 2021) is older than MediaPipe Pose (Project 8 stack). Results may not transfer directly.
- Musicological classification from score, not listener perception. Does not check whether listeners actually perceive the texture boundary as annotated.
- Borodin analysis has lower df (F(1, 107), F(2, 214)) than Brahms — fewer phrases and pairs, possibly underpowered for some contrasts.

## 6. Relevance to Project 8 E(t)

P-14 is **load-bearing** for:

- **[[phase_locking_value]]**: direct source for the PLV formula and parameter choices.
- **V(t) in E(t)**: establishes precedent for measuring visual coupling from head-motion video at ensemble scale.
- **[[musical_texture_effects]]**: evidence that texture (leadership distribution) modulates PLV.
- **[[breathing_desync]]** and related concepts: P-14 suggests PLV is sensitive to coordination demands at phrase endings.

P-14 is **NOT** evidence for:

- Choral applicability (paper is instrumental ensembles, no vocal data).
- Larger groups (paper limits at 4 to 5 performers; authors explicitly flag multi-row ensembles as future work with occlusion problems).
- Network-side latency (paper is co-located concert recordings, no network transmission).
- Real-time analysis (paper is post-hoc offline processing).
- Granger-causal leadership direction (paper lists this as future work, not demonstrated).
- MediaPipe-based pipelines (paper uses AlphaPose v0.4; Project 8 must validate MediaPipe against P-14's parameter choices).

## 7. Corrections Logged Against Prior Digest

See [[deep_read_audit]] for full table. Summary:

| Issue | Prior claim | Corrected reading |
| :--- | :--- | :--- |
| Missing F, p, effect sizes | "Synchronization (PLV) is significantly higher during polyphonic textures" | Brahms: F(1,219)=16.08 p<.001; Borodin: F(1,107)=14.051 p<.001. Interactions: Brahms F(2,438)=6.098 p=.002; Borodin F(2,214)=3.399 p=.035 [p. 92366]. |
| Phrase position claim oversimplified | "The difference in synchronization between polyphonic and homophonic textures is most pronounced at the beginning of musical phrases" | Effect is at Start AND Middle. Gap compresses at End because polyphonic **decreases** and homophonic **increases** at phrase endings [p. 92366]. Prior digest missed the directional asymmetry. |
| Missing dataset size | (not stated) | 44 phrases, 1 ensemble, 1 session, 2 pieces (Brahms + Borodin), 4 and 5 performers, 6 and 10 pairs [p. 92364 to 92365]. |
| Missing parameter details | "FFT" | Window=30, step=5, 10 Hz cut-off, Savitzky-Golay evaluated but unused, distance-only (no derivatives) [p. 92365]. |
| Missing multitrack-audio caveat | (no mention) | Paper has stereo mix only; cannot do per-instrument onset synchrony. Project 8 needs multitrack (Tier 2) to replicate beyond head-motion PLV [p. 92366, §VI-B]. |
| Missing pose-algorithm version | "AlphaPose" | AlphaPose v0.4. Project 8 uses MediaPipe; parameter transfer must be validated [p. 92365, §V-C]. |
| Missing audio cross-validation stats | "Auditory coordination ... visual coordination occurs at longer timescales" | Event density predicts PLV: χ²(1)=7.44 p=.006, β=.031 t=2.767. Pulse clarity does NOT: χ²(1)=.03 p=.884 [p. 92366, §VI-B]. |
| Missing Granger-causality future-work flag | (no mention) | Paper explicitly proposes Granger causality for leadership direction as future work [p. 92368, §VIII-B], directly supporting Project 8's N(t) network approach. |
