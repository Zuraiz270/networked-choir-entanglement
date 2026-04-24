---
title: P-01 Dagstuhl ChoirSet
type: source
alchemy_stage: nigredo
tags: [dataset, choral, mir, f0, intonation, deep_read]
ingested_date: 2026-04-23
last_deep_read: 2026-04-23
source_count: 1
related: ["[[intonation_cost_ic]]", "[[larynx_microphones]]", "[[p_14_husync]]", "[[deep_read_audit]]"]
team_take: Gold-standard multitrack dataset for a cappella SATB. 13 amateur singers, 2 Western pieces, co-located (no network). Useful for audio baselines; NOT a source for network-latency or interpersonal-coordination research.
---

# P-01 Dagstuhl ChoirSet: A Multitrack Dataset for MIR Research on Choral Singing

**Citation**: Rosenzweig, S., Cuesta, H., Weiß, C., Scherbaum, F., Gómez, E., Müller, M. (2020). *Transactions of the International Society for Music Information Retrieval* 3(1), 98 to 110. [DOI:10.5334/tismir.48](https://doi.org/10.5334/tismir.48). Open access CC-BY 4.0. Submitted 14 Feb 2020, accepted 10 Jun 2020, published 29 Jul 2020.
**Affiliations**: International Audio Laboratories Erlangen (FAU + Fraunhofer IIS, DE); UPF Music Technology Group, Barcelona (ES); University of Potsdam (DE); Joint Research Centre, European Commission, Seville (ES).
**Funding**: DFG MU 2686/12-1 (Rosenzweig); FI Predoctoral Grant + H2020 TROMPA 770376 (Cuesta).
**Artifact locations**:

- Data: [Zenodo 10.5281/zenodo.3956666](https://doi.org/10.5281/zenodo.3956666)
- Web interface with score-following playback: audiolabs-erlangen.de/resources/MIR/2020-DagstuhlChoirSet
- Python toolbox: [helenacuesta/ChoirSet-Toolbox](https://github.com/helenacuesta/ChoirSet-Toolbox)

**raw path**: `raw/01_primary_sources/Dagstuhl ChoirSet A Multitrack Dataset for MIR Research on Choral Singing.pdf`

## 1. Dataset Content (exact)

Recorded at **Dagstuhl Seminar 19052** ("Computational Methods for Melody and Voice Processing in Music Recordings"), 2019. Seminar room, not concert hall.

| Field | Value | Source |
| :--- | :--- | :--- |
| Total singers | **13** (Dagstuhl participants, CC consent) | [p. 100, §3.1] |
| Full Choir composition | 2 sopranos, 2 altos, 4 tenors, 5 basses | [p. 100, §3.1] |
| Experience mix | Amateur-dominant: hobby to one professional with music degree | [p. 100, §3.1] |
| Rehearsal time | 3 sessions × ~1 hour | [p. 100, §3.1] |
| Pieces | Bruckner *Locus Iste* WAB 23 (Latin, ~3 min) + Hristov *Tebe Poem* (Bulgarian) + systematic exercises | [p. 100 to 101, §3.1] |
| Settings | Full Choir, Quartet A, Quartet B (different singer subsets) | [p. 100, §3.1] |
| Total takes | **81** | [p. 101, Table 2] |
| Total duration | **55 min 30 s** | [p. 101, Table 2] |

**Per-piece breakdown** [p. 101, Table 2]:

| Piece | Full Choir | Quartet A | Quartet B |
| :--- | :--- | :--- | :--- |
| Locus Iste | 3 takes / 07:22 | 7 takes / 16:26 | 6 takes / 14:02 |
| Tebe Poem | 5 takes / 05:27 | 2 takes / 02:30 | — |
| Exercises | 33 takes / 06:00 | 25 takes / 03:43 | — |

## 2. Recording Setup (exact)

**Microphones per singer** [p. 101 to 102, §3.2]:

- **DYN** (dynamic): Sennheiser MD421 II. 4 available.
- **HSM** (headset): DPA 4066F. 3 available.
- **LRX** (throat/larynx): Albrecht AE 38 S2a. 8 available.
- Room stereo (STM): Schoeps MSTC 64 U ORTF, ~3 m from singers.

At least one LRX + one DYN per SATB section; three singers had full DYN+HSM+LRX; others had 1-2.

**Signal chain** [p. 102, §3.2]:

- RME Fireface UFX + 2× RME Micstasy A/D converters
- Logic Pro X DAW
- Additional stereo reverb version using ChromaVerb, 2-second decay

**File format**:

- Mono WAV per track
- Sampling rate: **22050 Hz**
- Filename convention: `DCS_{Song}_{Setting}_Take{#}_{Voice}{#}_{Microphone}.{Suffix}` [p. 103, §3.3]

## 3. Annotations (exact)

**Beat annotations** [p. 103, §3.4]: Two-stage manual process via Sonic Visualiser. First-pass tapping, second-pass refinement by experienced annotator. CSV format with timestamp (s) + measure.beat float encoding (e.g., 1.250 = measure 1, beat 1.25).

**Score alignment** [p. 103, §3.5]: MIDI scores from CPDL aligned to STM signals via DTW (Ewert et al. 2009, Müller et al. 2004) using beat annotations as anchors. Exported to CSV via pretty_midi.

**F0 trajectories** [p. 103 to 104, §3.6]:

- Algorithms: **pYIN** (Mauch & Dixon 2014) via Vamp plugin; **CREPE** (Kim et al. 2018) via Python package
- pYIN: FFT 2048, hop 221 samples (~10 ms), HMM+Viterbi smoothing, negative F0 for unvoiced frames
- CREPE: full model capacity, Viterbi smoothing, hop 10 ms, input size 1024
- Output format: CSV with timestamp, F0 (Hz), and voicing probability/confidence

## 4. Raw Data Block (F0 Evaluation)

Validation: manual F0 annotations on 2 quartet recordings (saxophone sound engineer with 10+ years training, Tony tool) vs. algorithm output. Averaged over 8 LRX + 6 HSM + 8 DYN trajectories per algorithm. Metrics: Voicing Recall (VR), Voicing False Alarm (VFA), Raw Pitch Accuracy (RPA), Raw Chroma Accuracy (RCA), Overall Accuracy (OA). SD in brackets.

**pYIN** [p. 104, Table 4]:

| Mic | VR | VFA | RPA | RCA | OA |
| :--- | :--- | :--- | :--- | :--- | :--- |
| LRX | 0.99 (0.00) | 0.11 (0.06) | 0.95 (0.02) | 0.95 (0.01) | **0.93** (0.03) |
| HSM | 0.98 (0.01) | 0.33 (0.09) | 0.81 (0.10) | 0.91 (0.04) | 0.77 (0.08) |
| DYN | 0.99 (0.00) | 0.16 (0.11) | 0.93 (0.04) | 0.95 (0.01) | 0.90 (0.05) |

**CREPE** [p. 104, Table 5]:

| Mic | VR | VFA | RPA | RCA | OA |
| :--- | :--- | :--- | :--- | :--- | :--- |
| LRX | 0.96 (0.01) | 0.12 (0.02) | 0.96 (0.01) | 0.96 (0.01) | **0.93** (0.02) |
| HSM | 0.92 (0.02) | 0.32 (0.08) | 0.91 (0.01) | 0.91 (0.02) | 0.84 (0.02) |
| DYN | 0.93 (0.01) | 0.18 (0.07) | 0.93 (0.01) | 0.93 (0.01) | 0.90 (0.02) |

**Takeaways**: LRX is cleanest for F0 (OA 0.93 both algorithms). DYN close (OA 0.90). HSM worst (OA 0.77 pYIN, 0.84 CREPE) because vocal-tract loss + crosstalk. CREPE slightly better than pYIN on HSM; roughly equal on LRX and DYN.

## 5. Case Studies (paper's own demonstrations)

**Case 1: Intonation Cost (IC)** [p. 105 to 106, §5.1]: Applied Weiß et al. 2019 IC measure (12-TET grid shift minimization). Results across 6 takes of Quartet A + 5 takes of Quartet B show:

- Chromatic passages (measures 13-20 and 40-42 of Locus Iste) have higher IC for both quartets.
- Quartet B > Quartet A intonation quality on the final chord (measures 44-48).
- Demonstrates suitability of DCS for intonation-drift studies.

**Case 2: Multiple-F0 Estimation** [p. 106 to 107, §5.2]: Applied DeepSalience (Bittner et al. 2017) to three scenarios on Locus Iste Quartet A Take 3: DYN mix, STM, STM+reverb. Threshold 0.1. Findings:

- Best F-Score: DYN mix.
- Reverb decreases precision (false positives from temporal smearing). Recall unaffected.
- LRX pYIN trajectories used as reference (acknowledged as algorithmically derived, not hand-annotated).

## 6. Limitations

**Implicit (not stated explicitly but binding on any citation)**:

- **Co-located recording, no network**. P-01 is NOT a network-latency or NMP dataset. Any Project-8 claim citing DCS as NMP evidence is wrong.
- **No interpersonal coordination annotations**. No onset-synchrony, no phase-locking, no head-motion data. Only F0 and score alignment.
- **13 amateur singers, single session, single venue** (Dagstuhl seminar room). Not representative of professional choirs or diverse ensembles.
- **Western SATB only**. Two pieces (Bruckner + Hristov). No non-Western repertoire, no alternate tuning systems.
- **Only 3 singers had full DYN+HSM+LRX**. Many singers lack one or more close-up mics. Per-singer analysis coverage is non-uniform.
- **LRX throat attachment** may slightly alter natural vocal behavior; not quantified.
- **Balance of voice sections**: 2S/2A/4T/5B is imbalanced for SATB analysis. CSD (Cuesta et al. 2018) is more balanced for section-interaction studies.
- **F0 manual annotation validation** done on only **2 quartet recordings**, not the full dataset.

## 7. Relevance to Project 8 E(t)

**P-01 is load-bearing for**:

- **Audio baseline A(t)**: LRX signals provide clean per-singer F0 nearly free of crosstalk — gold standard for within-singer audio feature extraction.
- **Tier 2 benchmark**: DCS can serve as a co-located comparison baseline against which Jamulus/SoundJack-mediated performances (Project 8 Tier 2) can be compared for audio-coupling metrics.
- **Intonation drift failure mode**: chromatic-passage IC spikes documented in §5.1 inform [[intonation_cost_ic]].
- **Validation of F0 algorithms**: pYIN and CREPE performance benchmarks (Tables 4, 5) guide Project 8's algorithm choices.

**P-01 is NOT**:

- Evidence for network-latency effects.
- Evidence for interpersonal coordination or [[entanglement_index]] (no coordination annotations).
- Evidence for larger-ensemble behavior (N = 13).
- Evidence for MediaPipe-based visual analysis (no video data).

## 8. Corrections Logged Against Prior Digest

See [[deep_read_audit]] for full table. Summary:

| Issue | Prior claim | Corrected reading |
| :--- | :--- | :--- |
| Missing dataset counts and timing | "Multitrack dataset of a cappella choral music" | 13 singers, 81 takes, 55:30 total, 2 pieces + exercises, 3 settings, 3 hours rehearsal [p. 100 to 101]. |
| Missing F0 evaluation numbers | "Compares DYN (high crosstalk), HSM (medium), and LRX (low) for F0 estimation accuracy" | Exact OA: pYIN LRX=0.93, HSM=0.77, DYN=0.90; CREPE LRX=0.93, HSM=0.84, DYN=0.90 [p. 104, Tables 4-5]. HSM is worst, not medium. |
| Missing author affiliations | "Rosenzweig, S., et al. (2020)" | 6-author team: Erlangen Audio Labs + UPF MTG Barcelona + Univ. Potsdam + JRC EU Commission Seville. DFG + TROMPA funded. |
| Missing hardware specs | "Headset, Dynamic, and Larynx" | Sennheiser MD421 II (DYN), DPA 4066F (HSM), Albrecht AE 38 S2a (LRX), Schoeps MSTC 64 U (STM). RME Fireface UFX + Micstasy. Logic Pro X. 22050 Hz mono WAV [p. 101 to 102]. |
| **Missing "no network, no coordination annotations" caveat** | "Gold-standard dataset for our Audio Synchronization A(t) baseline" | DCS is co-located, no network, no onset/PLV/coordination annotations. Useful as audio-quality baseline only. Any claim about DCS-based network or entanglement evidence is misleading [p. 100, §3.1]. |
| "Identified intonation drift patterns in amateur choirs will serve as the primary failure mode for our Entanglement Index tests" | — | Over-reach. Case study 5.1 shows chromatic-passage IC elevation, not a validated "primary failure mode" for E(t). Moved to §7 as Project-8 application, not P-01 finding. |
| Missing open artifact links | (no mention) | Zenodo DOI, web interface, GitHub toolbox all cited. Project 8 should use the toolbox for DCS ingestion to ensure reproducibility. |
