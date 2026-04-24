---
title: P-05 MLCA-AVSR Fusion
type: source
alchemy_stage: nigredo
tags: [ml, avsr, lip_reading, audio_visual, fusion, deep_read]
ingested_date: 2026-04-23
last_deep_read: 2026-04-24
source_count: 1
related: ["[[cross_attention_fusion]]", "[[e_branchformer_encoder]]", "[[vocal_entrainment]]", "[[deep_read_audit]]"]
team_take: Audio-visual SPEECH recognition (Chinese TV rooms), not singing. Methodologically adjacent to Project 8's audio-visual coupling pipeline but does NOT provide "reconstruct pitch from lip motion" capability — it improves speech-word error rate.
---

# P-05 MLCA-AVSR: Multi-Layer Cross Attention Fusion Based Audio-Visual Speech Recognition

**Citation**: Wang, H., Guo, P., Zhou, P., Xie, L. (2024). In *ICASSP 2024*, pp. 8150 to 8154. [DOI:10.1109/ICASSP48485.2024.10446769](https://doi.org/10.1109/ICASSP48485.2024.10446769).
**Affiliations**: ASLP@NPU, Northwestern Polytechnical University, Xi'an, China; Space AI, Li Auto.
**raw path**: `raw/01_primary_sources/MLCA-AVSR_Multi-Layer_Cross_Attention_Fusion_Based_Audio-Visual_Speech_Recognition.pdf`

## 1. Architecture (§2)

- Audio frontend: 2-layer conv down-sampling
- Visual frontend: **5-layer ResNet3D** on lip ROI (112×112 crops) [§3.1]
- Audio encoder: **24-layer E-Branchformer**, 256-dim, 4 heads, 1024-dim FFN
- Visual encoder: 9-layer E-Branchformer
- Decoder: 6 Transformer layers
- **Cross-attention modules at 3 intermediate positions** (CA1, CA2, CA3) plus final fusion
- Joint CTC/Attention training + Inter-CTC loss regularization
- Model size: **105.40M params** (MLCA full)

## 2. Dataset: MISP2022-AVSR

- **Chinese conversational corpus**, 141h audio+video from 34 real-home TV rooms
- Far/middle/near microphones; far/middle cameras
- Training 106h, Dev 3.09h, Eval 3.13h
- After augmentation (speed 0.9/1.0/1.1, MUSAN noise, pyroomacoustics RIRs): ~1,300h training
- Visual: lip ROIs cropped, 112×112

## 3. Raw Data Block

**Single-modality baselines** (E-Branchformer, CER% on Dev/Eval/Evalsd) [Table 1]:

- ASR (audio-only): **25.9 / 27.3 / 33.3**
- VSR (visual-only): **84.4 / 84.6 / 83.5** (lip-reading much worse than audio)

**Fusion comparison** (CER% Dev/Eval; cpCER% Evalsd) [Table 2]:

| Fusion | Params | Dev | Eval | Evalsd |
| :--- | :--- | :--- | :--- | :--- |
| Add | 110.05M | 24.6 | 26.5 | 32.5 |
| MLP | 111.63M | 24.9 | 26.6 | 32.8 |
| **MLCA (proposed)** | **105.40M** | **21.8** | **24.1** | **30.6** |

MLCA gives ~2.4 to 2.5% relative CER improvement over Add/MLP.

**MISP2022 top-systems comparison** (cpCER% Devsd/Evalsd) [Table 4]:

| System | Rank | Devsd | Evalsd |
| :--- | :--- | :--- | :--- |
| Channel AV-Fusion [Xu et al. 2022] | 1st | — | **29.58** |
| SLCA-AVSR (authors' previous) [Guo et al.] | 2nd | 29.73 | 33.74 |
| +ROVER | — | 28.13 | 31.21 |
| Conformer-AV | 3rd | 29.40 | 33.94 |
| +ROVER | — | 27.50 | 31.88 |
| **MLCA-AVSR (this work)** | — | **25.92** | **30.57** |
| **+ROVER** | — | **24.49** | **29.13** (new SOTA) |

**Ablation** (CA1/CA2/CA3 removal) [Table 3]:

- All three modules → 21.8/24.1/30.6 CER (best)
- Only CA1 retained → 22.7/24.9/31.1 (0.6% better than CA2-only)
- All three cross-attention modules improve; removing any degrades. Early fusion (CA1) particularly important.

## 4. Limitations

**Implicit (paper has no explicit §Limitations)**:

- **Chinese conversational speech**, not English, not music, not singing.
- **Far-field TV-room scenarios**, not NMP.
- **Lip ROIs only** (112×112 crops) — full body pose, head sway, breathing NOT included.
- Relies on **speaker diarization** (DER 9.43% on Dev); upstream errors propagate.
- **105M parameters**, no real-time inference claim, no mobile benchmark.
- Training used 1300h of augmented Chinese speech; not transferable to choral singing without retraining.
- ROVER ensemble for SOTA result requires multi-system fusion — computationally expensive.
- Word-error-rate metric (CER) measures speech transcription accuracy, not coordination.
- VSR (lip-reading only) CER is ~84% — visual stream alone is nearly useless for speech recognition; it **complements** audio, does not replace it.

## 5. Relevance to Project 8 E(t)

**P-05 is relevant for**:

- **Methodological precedent** for multi-level cross-attention audio-visual fusion. If Project 8 explores neural audio-visual coupling models (not currently in v2.2 scope), MLCA is a reference architecture.
- **E-Branchformer encoder** choice: supports Project 8's backbone decision if a transformer encoder is used.
- **Cross-attention fusion** as a feature-learning approach vs. simple concatenation/addition.

**P-05 is NOT**:

- A source for "reconstructing vocal timing and pitch from lip motion" (prior digest over-reach). VSR-only CER is **84-85%** — lip-reading alone is barely better than random for Chinese conversational speech [Table 1].
- A source for E(t) calculation under "Blind Audio" conditions. Paper is about speech transcription, not pitch / timing / coordination.
- Applicable to choral singing without major retraining. MISP2022 is Chinese conversational far-field, not singing.
- Real-time capable (no latency benchmark; 105M params heavy).
- Evidence that visual stream can rescue audio-degraded conditions for **coordination** metrics — only speech-recognition accuracy is measured.

## 6. Corrections Logged Against Prior Digest

See [[deep_read_audit]] for full table. Summary:

| Issue | Prior claim | Corrected reading |
| :--- | :--- | :--- |
| Missing CER numbers | "SOTA on MISP 2022-AVSR" | MLCA: 21.8/24.1/30.6 CER (Dev/Eval/Evalsd); with ROVER → 29.13% cpCER on Evalsd, beating MISP2022 1st by 0.45% [Tables 2, 4]. |
| Missing dataset specificity | "AVSR" | **Chinese conversational** TV-room speech (MISP2022). Lip ROIs 112×112. 141h corpus → 1300h after augmentation [§3]. |
| **"Reconstruct intended vocal timing and pitch from lip motion, maintaining E(t) even in Blind Audio conditions"** | — | **Over-reach**. VSR-only CER is **84.4% on Dev**; lip-reading alone is nearly useless without audio. MLCA improves speech TRANSCRIPTION accuracy by fusing A+V; it does NOT reconstruct audio from video [§3.3.1, Table 1]. |
| Missing domain caveat | "AVSR" used generically | Chinese far-field speech; NOT English, NOT music, NOT singing. Not directly applicable to choral NMP without retraining. |
| Missing model size / efficiency | "mathematical basis" | 105M parameters. No real-time or mobile benchmark. Not deployable for live NMP monitoring [§3.2]. |
| "Shallow cross-attention (early fusion) is particularly effective" | Correct | CA1-only retention is 0.6% CER better than CA2-only retention [§3.3.3], confirming early fusion helps. But all three CA modules together yield the best result. |
| "Our Multi-modal Synchronization Index" | — | No such construct in P-05. Project-8 extrapolation, moved to §5 as labeled application. |
