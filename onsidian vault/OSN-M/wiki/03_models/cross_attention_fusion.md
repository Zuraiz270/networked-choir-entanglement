---
title: Cross-Attention Fusion
type: concept
alchemy_stage: citrinitas
tags: [ml, multimodal, attention]
ingested_date: 2026-04-23
source_count: 1
related: ["[[p_05_mlca_avsr_fusion]]", "[[attention_focus_shift]]"]
---

# Cross-Attention Fusion

Cross-Attention Fusion is a mechanism where the information from one modality (e.g., Audio) is used to "query" the relevant features in another modality (e.g., Visual).

## Mechanism
1. **Audio-Query ($Q_a$):** "What was the singer doing with their voice at time $t$?"
2. **Visual-Key/Value ($K_v, V_v$):** "What were the lips doing at time $t$?"
3. **Alignment:** The model calculates a weight (attention map) that aligns the vocal burst with the lip opening, effectively "denoising" the audio signal using the visual ground truth.

## Significance for "Entanglement"
In our index, Cross-Attention represents the **Inter-Modality Coupling**. A high attention weight between audio and visual streams indicates that the performer is "congruent." If the attention map becomes sparse or chaotic, it signals a **Perceptual Mismatch**, which negatively impacts the group's collective entanglement.
