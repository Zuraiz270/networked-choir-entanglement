---
title: P-08 Videoconference Fluidity ML
type: source
alchemy_stage: nigredo
tags: [ml, fluidity, enjoyment, multimodal, video_conferencing, granger_causality, deep_read]
ingested_date: 2026-04-23
last_deep_read: 2026-04-23
source_count: 1
related: ["[[fluidity_and_enjoyment]]", "[[awkwardness_vs_rudeness]]", "[[granger_influence_index]]", "[[deep_read_audit]]"]
team_take: Strong methodological parallel to Project 8 (multimodal audio+video+GC ML), but domain is CONVERSATION not music. Body-motion Granger causality caveat: paper's 7-second window is acknowledged as too short for reliable GC.
---

# P-08 Multimodal Machine Learning Can Predict Videoconference Fluidity and Enjoyment

**Citation**: Chang, A., Akkaraju, V., Cogliano, R.M., Poeppel, D., Freeman, D. (2025). In *ICASSP 2025*. [DOI:10.1109/ICASSP49660.2025.10889480](https://doi.org/10.1109/ICASSP49660.2025.10889480).
**Affiliations**: New York University + Max Planck Society (Munich).
**Funding**: NYU Discovery Research Fund, NIDCD/NIH F32DC018205, Leon Levy Foundation, NYU HPC.
**raw path**: `raw/01_primary_sources/Multimodal_Machine_Learning_Can_Predict_Videoconference_Fluidity_and_Enjoyment.pdf`

## 1. Dataset

**RoomReader corpus** [Reverdy et al., LREC 2022] [§III-A-1]:

- 30 Zoom sessions, 4-5 participants each, 8-30 min each
- **~9 hours total**, **118 participants** (91 English native speakers)
- Collaborative quiz games + icebreakers (not music)

**Clip extraction** [§III-A-2]:

- RMS threshold 0.05 per speaker; silence = all below for 0.75 s; overlap = >1 simultaneous
- 1508 marked points each in silence and overlap categories
- **3,016 clips total** at -3 s to +4 s (7-s windows)

**Ratings** [§III-B]:

- **528 NYU student raters** (274F / 167M / 87 other), age 18-36 (median 20), 46% native English
- 5-point Likert on Fluidity and Enjoyment
- Reliability: Pearson r > 0.2 vs. consensus → 350 reliable raters
- Final: **2,992 clips** (rated by ≥4 reliable raters)
- Event classification: 810-996 clips per event type

**Binary threshold = 2.5** on Likert (authors verified robustness at threshold 3 as well).

## 2. Features

| Domain | Method | Output | Sampling |
| :--- | :--- | :--- | :--- |
| **Audio** | VGGish (128-dim), YAMNet (1024-dim), Wav2Vec2-base-960h (768-dim) | Embedding per window | 16 kHz audio, 0.96/0.48/1.00 s windows |
| **Face** | **OpenFace** 17 Action Units (blink, jaw drop, etc., lip suck excluded) | Per-participant AU time-series, averaged across participants | 60 Hz → 0.98-s window average |
| **Body motion** | MediaPipe webcam-to-participant distance → first derivative → Granger causality coupling via MVGC toolbox model order 12 (1.5 s) | Averaged pairwise GC | 60 Hz → 8 Hz |

## 3. Model

- scikit-learn 1.3, Python 3.8
- Logistic regression via SGDClassifier, balanced class weights
- 5-fold stratified group cross-validation (new sessions/participants held out)
- BayesianOptimization 600 iters on PCA var (50-99%), alpha (10⁻¹⁰ to 1), L1 ratio (0-1)
- Metrics: macro-averaged ROC-AUC, AP, BA, F1

## 4. Raw Data Block (Table I — 0 to 7 s features)

| Target | Feature set | ROC-AUC | AP | F1 | BA |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Fluidity | Face | .668 | .963 | .440 | .625 |
| Fluidity | VGGish | **.805** | .977 | .547 | .712 |
| Fluidity | VGGish+Face | .814 | .980 | .584 | .728 |
| Fluidity | **VGGish+Face+Body** | **.815** | .980 | .584 | .728 |
| Enjoyment | Face | .758 | .985 | .485 | .683 |
| Enjoyment | VGGish | .859 | .990 | .593 | .788 |
| Enjoyment | VGGish+Face | .873 | .992 | .573 | .788 |
| Enjoyment | **VGGish+Face+Body** | **.874** | .992 | .565 | .784 |

**Pre-event (0-3 s) features, Table II**: Fluidity AUC=.690, Enjoyment=.761. Big drop for audio-containing models (-.11 AUC), small drop (-.03) for face-only — authors conclude audio reflects dynamic changes, face reflects long-term state.

**Audio backbone comparison**: VGGish > Wav2Vec2 (Fluidity .815, Enjoyment .841) > YAMNet (.694, .789). Domain-general audio DNNs outperform speech-specific Wav2Vec2 for high-level Enjoyment [§V-A].

## 5. Event-Type Effects

Differences on Likert Fluidity [§III-B-4]:

- Backchanneling > Interruption: t(1841) = **21.5**, p < .001
- Backchanneling > Gap: t(1806) = **21.8**, p < .001
- Interruption vs. Gap: t(1653) = 1.5, p = .129 (n.s. for Fluidity)

Differences on Likert Enjoyment:

- Backchanneling > Interruption: t(1841) = 19.5, p < .001
- Backchanneling > Gap: t(1806) = 30.3, p < .001
- Interruption > Gap: t(1653) = **12.5, p < .001**

**Interpretation** (authors' [§III-B-4]): "Gaps are worse than interruptions for overall enjoyment, implying that awkwardness is more damaging than rudeness."

Fluidity × Enjoyment contingency: χ² = 758.13, p < .001. Related but not equivalent.

## 6. Granger Causality Sub-Finding

Body motion GC was **higher among high-Fluidity clips**: t(2990) = **2.29, p = .022** [§V-A, replicating authors' prior body-sway leadership work refs 17-20].

Body motion GC did **NOT differ** between high/low Enjoyment clips: t(2990) = 0.51, p = .607.

**Critical caveat** [§V-A, explicit authors' note]: "its potential to enhance model performance could be significantly increased by calculating it over minutes, as in previous studies, rather than the 7-second period used here." → GC on 7-s windows underestimates the signal.

## 7. Limitations

**Stated** [§VI]:

- RoomReader "protocol is carefully designed to provoke naturalistic behavior, this likely makes the dataset overly self-consistent, and so the generalizability of our model to broader videoconferencing contexts remains untested."
- Body-motion GC window (7 s) too short; minutes-long windows would likely perform better.

**Implicit (binding on Project 8 citation)**:

- Domain is **videoconference conversation**, not music. RoomReader has no singing or ensemble playing.
- NYU-student rater pool; demographic bias.
- Heavily imbalanced: 2,731 positive vs. 92 low-Fluidity+low-Enjoyment clips. Use of macro-averaged AUC and balanced-class weights partly mitigates.
- No network-condition manipulation; RoomReader's latency/jitter are whatever Zoom provided during collection.
- MediaPipe body motion from webcam only (upper body, face visible); full-body motion not captured.
- No latency-threshold study; cannot be cited for latency-perception claims.

## 8. Relevance to Project 8 E(t)

**P-08 is load-bearing for**:

- **Methodological parallel**: Project 8's E(t) pipeline (audio + pose + Granger network) is structurally analogous to P-08's VGGish + OpenFace + body-motion-GC. P-08 validates that multimodal ML from these domains can predict subjective coordination outcomes at ROC-AUC ~.87.
- **[[fluidity_and_enjoyment]]**: direct source. Project 8 can cite as precedent for fluidity prediction from multimodal features.
- **[[awkwardness_vs_rudeness]]**: gaps > interruptions as Enjoyment penalty (awkwardness > rudeness) is a well-sourced claim.
- **Audio embedding choice**: VGGish > Wav2Vec2 for high-level enjoyment suggests Project 8 should prefer domain-general audio embeddings if reusing transfer-learned features, not speech-specific.

**P-08 is NOT**:

- Evidence for musical coordination or choral entanglement. RoomReader is conversational, not musical.
- Evidence for latency thresholds (no latency manipulation).
- A validated real-time model (trained in batch).

## 9. Corrections Logged Against Prior Digest

See [[deep_read_audit]] for full table. Summary:

| Issue | Prior claim | Corrected reading |
| :--- | :--- | :--- |
| Missing dataset specifics | "RoomReader corpus" | 30 sessions, 118 participants, ~9 hours, 2,992 clips (7 s each) rated by 528 raters (350 reliable) [§III]. |
| Missing ROC-AUC per condition | "Achieved an ROC-AUC of 0.87" | Fluidity best .815 (VGGish+Face+Body); Enjoyment best .874; on 0-3 s pre-event features the gain drops to .690 / .761 [Table I, II]. The .87 figure is Enjoyment-best, not Fluidity. |
| Missing event-pair statistics | "Conversational gaps (>750ms) are more detrimental to user enjoyment than interruptions" | Backchanneling > Interruption > Gap for Enjoyment, with t-values 19.5, 30.3, 12.5 respectively (all p<.001). For Fluidity, Interruption ≈ Gap (n.s.) [§III-B-4]. |
| Missing body-motion-GC caveat | "Multimodal ML (audio, facial, body motion)" | Body motion contribution to model is **minimal** (AUC change <.01). Authors themselves say 7-s GC window is too short and "could be significantly increased by calculating over minutes" [§V-A]. |
| "Proving that high-level social outcomes can be predicted from low-level sensory data" | — | Over-reach. Paper generalizability "remains untested"; single-corpus validation; 2992/3016 highly self-consistent clips [§VI]. |
| Missing domain caveat | (no mention) | RoomReader is conversational, not musical. Any Project-8 claim extending P-08's .87 AUC to choral entanglement is a domain jump. |
| "Absence of awkward gaps indicates high collective entanglement" | — | P-08 analyzes conversational fluidity, not entanglement. The mapping to "collective entanglement" is Project-8 extrapolation. Moved to §8 as labeled application. |
| Missing VGGish > Wav2Vec2 finding | (no mention) | Domain-general audio DNNs outperform speech-specific ones for high-level Enjoyment prediction [§V-A]. Informs Project 8's audio-backbone choice. |
