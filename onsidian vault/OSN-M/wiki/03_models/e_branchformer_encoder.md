---
title: E-Branchformer Encoder
type: concept
alchemy_stage: citrinitas
tags: [ml, architecture, transformer, branchformer]
ingested_date: 2026-04-23
source_count: 1
related: ["[[p_05_mlca_avsr_fusion]]"]
---

# E-Branchformer Encoder

The E-Branchformer is an "Enhanced" version of the Branchformer architecture, designed to capture local and global dependencies in sequential data (like audio and video) simultaneously.

## Architecture
- **Parallel Branches:** One branch uses a Convolutional module (local context), while the other uses a Self-Attention module (global context).
- **Enhanced Merging:** Uses a gated MLP or advanced fusion mechanism to combine the outputs of the two branches.
- **Superiority:** In AVSR tasks, it consistently outperforms Conformer and standard Transformer encoders by providing a more expressive representation of speech rhythms and lip motion.

## Application in SNA-OSN-M
We adopt the E-Branchformer as our reference model for processing **Head Motion Trajectories** and **Vocal F0 Envelopes**. Its ability to model both the "micro-jitters" (local) and the "musical phrase" (global) makes it ideal for calculating the Entanglement Index $E(t)$.
