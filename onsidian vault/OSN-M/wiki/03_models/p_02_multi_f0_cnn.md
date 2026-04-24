---
title: P-02 Multi-F0 CNN
type: source
alchemy_stage: nigredo
tags: [mir, f0_estimation, cnn, choir, hcqt, phase_differentials, deep_read]
ingested_date: 2026-04-23
last_deep_read: 2026-04-23
source_count: 1
related: ["[[pitch_salience_map]]", "[[harmonic_collision]]", "[[entanglement_index]]", "[[p_01_dagstuhl_choirset]]", "[[deep_read_audit]]"]
team_take: SOTA multi-F0 for a cappella SATB as of 2020. Frame-wise only (no voice assignment), no per-singer output. Project 8 can use this for polyphonic mixture analysis but cannot extract per-singer F0 without separate multitrack (Tier 2).
---

# P-02 Multiple F0 Estimation in Vocal Ensembles using Convolutional Neural Networks

**Citation**: Cuesta, H., McFee, B., Gómez, E. (2020). In *Proceedings of the 21st International Society for Music Information Retrieval Conference (ISMIR)*, Montréal, Canada. arXiv:2009.04172. CC-BY 4.0.
**Affiliations**: UPF Music Technology Group, Barcelona; NYU MARL + Center for Data Science; European Commission JRC Seville.
**Code**: [helenacuesta/multif0-estimation-vocals](https://github.com/helenacuesta/multif0-estimation-vocals)
**raw path**: `raw/01_primary_sources/Multiple F0 Estimation in Vocal Ensembles using Convolutional Neural Networks.pdf`

## 1. Method (exact)

**Input**: Dual HCQT representation [§4.1]:

- HCQT magnitude (3D array H[h, t, f]): 60 bins/octave, 20 cents/bin, 6 octaves, f_min=32.7 Hz (C1), h ∈ {1, 2, 3, 4, 5}
- HCQT phase differentials (instantaneous-frequency refinement, Eq. 1)
- Sampling rate: 22050 Hz, hop size 256 samples

**Output**: 2D salience map with same time and frequency resolution as H[1]. Target: Gaussian-blurred binary activation, SD=1 in frequency, energy decay covering half a semitone.

**Three CNN architectures** [§4.3, Fig. 3]:

1. **Early/Shallow**: magnitude + phase concat after first 5×5 convs
2. **Early/Deep**: same as Early/Shallow + two additional 64-filter 3×3 layers
3. **Late/Deep**: magnitude and phase in separate branches through 70×3 convs, then concat, then shared head

**Training** [§4.3, end]:

- Loss: binary cross-entropy
- Optimizer: Adam lr=0.001, batch size 16
- 100 epochs max, early stopping after 25 non-improving validation epochs
- Input patch size: (360, 50) — frequency bins × time frames

## 2. Dataset

Aggregate of 5 multi-track polyphonic singing datasets [§3, Table 1]:

| Dataset | Songs | Singers | Voice layout | Public |
| :--- | :--- | :--- | :--- | :--- |
| **Choral Singing Dataset (CSD)** | 3 | 16 | 4S4A4T4B | Yes |
| **Dagstuhl ChoirSet (DCS)** | 2 | 13 | 2S2A4T5B | Yes (see [[p_01_dagstuhl_choirset]]) |
| **ESMUC Choir Dataset (ECS)** | 3 | 13 | 5S3A3T2B | **Proprietary** |
| **Bach Chorales** | 26 | SATB quartets | SATB | Commercial |
| **Barbershop Quartets** | 22 | Male quartets | Tenor/Lead/Baritone/Bass | Commercial |

**Augmentation**:

- Pitch-shift: -2 to +2 semitones per voice, re-mixed via PySox
- Reverb: Great Hall IR from Isophonics Room Impulse Response Dataset via MUDA

**Final dataset size**: **22,910 audio files**, 10 s to 3 min duration each.
**Split**: 75% / 10% / 15% train/val/test (17,184 / 2,291 / 3,435 files).

## 3. Raw Data Block (BSQ evaluation results, §5.2, Table 2)

Evaluated on Barbershop Quartets dataset (excluded from training in this experiment).

| Method | 100 cents F | 100 cents P | 100 cents R | 20 cents F | 20 cents P | 20 cents R |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| MSINGERS | **0.708** (.06) | 0.685 (.06) | 0.736 (.07) | **0.537** (.07) | 0.620 (.07) | 0.477 (.08) |
| VOCAL4-VA | **0.757** (.06) | — | — | **0.490** | — | — |
| **Late/Deep (this paper)** | **0.846** (.03) | 0.812 (.03) | 0.884 (.04) | **0.831** (.03) | 0.797 (.03) | 0.868 (.04) |

**Key finding**: Late/Deep drops only ~2% from 100 cents to 20 cents tolerance, while baselines drop 17% (MSINGERS) and 26% (VOCAL4-VA). Phase information explains the precision robustness.

**Experiment 3 generalization**:

- On Su et al. 2016 choir dataset (excluded from training): Late/Deep F=**0.704**, Su et al. F=**0.653**. P-02 wins [p. 5, §5.3].
- Reverb subset: training with reverb gives ~10% F-Score improvement over dry-only training.

## 4. Limitations

**Stated** [§6, §5.3]:

- "Further experiments with a larger amount of data are required to verify these findings." Particularly relevant for the Su et al. comparison (small test set).
- Post-processing for temporal continuity of F0 contours is future work.
- **No voice assignment**: model outputs multiple F0s per frame but does NOT identify which F0 belongs to which singer. This is flagged as future work.

**Implicit (binding on Project 8 citation)**:

- **Frame-wise only**: no per-singer F0 stream. Project 8 cannot extract per-singer pitch features from polyphonic mixes using P-02 alone; needs multitrack (Tier 2) to get per-singer F0.
- **Training data mixes SATB (CSD, DCS, ECS, BC) with TLBB (BSQ)** — voice-range generalization to non-standard ensembles is untested.
- **ESMUC is proprietary** — part of the training set cannot be independently reproduced without UPF license.
- **Single reverb IR** (Great Hall) — robustness to small-room, studio, or Zoom-compressed audio untested.
- **Only Western SATB + barbershop repertoire** — non-Western or contemporary choral styles untested.
- Reference F0 for training relies on pYIN or similar algorithms on close-up mics, not hand annotation. Any label noise propagates to the CNN.

## 5. Relevance to Project 8 E(t)

**P-02 is load-bearing for**:

- **Polyphonic mix pitch analysis**: when Project 8 analyzes a stereo mix (e.g., Tier 1 YouTube, some Tier 2 bounced mixes), P-02 provides the state-of-the-art multi-F0 salience output.
- **[[pitch_salience_map]]**: direct source for this concept page.
- **Robustness to reverb**: important for real-world Tier 1 and Tier 3 recordings.
- **[[harmonic_collision]]** failure mode: P-02's multi-F0 output will collapse when multiple singers hit overlapping partials; this is a known limitation the paper acknowledges indirectly (see "timbre similarity, strong harmonic relationships").

**P-02 is NOT**:

- A source for per-singer F0 tracking from a polyphonic mix. P-02 outputs a set of F0s per frame, unlabeled. Project 8 needs multitrack data for per-singer analysis.
- A voice-assignment solution. Separate downstream work needed (e.g., Schramm & Benetos 2017 VOCAL4-VA or McLeod et al. 2017 HMM-based assignment).
- A validator for vibrato/intonation-drift tracking specifically. The paper's focus is frame-wise F0 correctness, not temporal contour modeling.

## 6. Corrections Logged Against Prior Digest

See [[deep_read_audit]] for full table. Summary:

| Issue | Prior claim | Corrected reading |
| :--- | :--- | :--- |
| Missing F-Score numbers | "Significant performance boost over general-purpose multi-F0 models (like DeepSalience)" | Late/Deep: F=0.846 vs. MSINGERS 0.708 vs. VOCAL4-VA 0.757 at 100 cents. At 20 cents: 0.831 vs. 0.537 vs. 0.490 [p. 5, Table 2]. |
| Missing 20-cents robustness claim | "improving pitch resolution down to 20 cents" | Late/Deep drops only ~2% F-Score from 100 to 20 cents; baselines drop 17% and 26% [p. 5, §5.2]. This is the key selling point — direct quote. |
| Missing dataset aggregation detail | "Uses multi-track data (Dagstuhl ChoirSet, etc.) augmented with reverb and pitch-shifting" | 5 datasets (CSD, DCS, ECS, BC, BSQ) aggregated → 22,910 files, 75/10/15 split. ESMUC is proprietary [§3, Table 1]. |
| Missing "no voice assignment" caveat | "We can track the micro-fluctuations (vibrato, intonation drift) of each singer in an ensemble" | **P-02 does NOT output per-singer F0s**. It outputs frame-wise multi-F0 without voice assignment. Per-singer tracking requires multitrack (Tier 2) or downstream voice-assignment model [§6]. |
| Over-reach on "Vocal Entrainment dashboard basis" | "The cross-correlation of these salience trajectories forms the basis of the Vocal Entrainment component of our dashboard" | P-02 is frame-wise, not trajectory-level. Cross-correlating salience trajectories is Project-8 design, not P-02 finding. Moved to §5 as Project-8 plan. |
| Missing hardware/training specifics | "Late/Deep CNN" | HCQT 60 bins/oct, 5 harmonics, f_min=32.7 Hz, hop 256 @ 22050 Hz; BCE loss; Adam lr=0.001; batch 16; 100 epochs; early stop 25 [§4.1, §4.3]. |
| Missing proprietary-ESMUC caveat | (no mention) | ESMUC Choir Dataset is proprietary; training set not fully reproducible [§3]. |
