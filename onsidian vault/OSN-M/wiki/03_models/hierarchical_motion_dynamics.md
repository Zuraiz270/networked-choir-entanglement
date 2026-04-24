---
title: Hierarchical Motion Dynamics
type: concept
alchemy_stage: citrinitas
tags: [mocap, physics, ml]
ingested_date: 2026-04-23
source_count: 1
related: ["[[p_19_viopose_4d]]", "[[phase_locking_value]]"]
---

# Hierarchical Motion Dynamics

Hierarchical Motion Dynamics is a modeling approach where a neural network's layers are explicitly mapped to the physical derivatives of motion.

## Structure (P-19)
1. **$a(t)$ (Acceleration):** Encoded from high-frequency audio features (transients, bow speed).
2. **$v(t)$ (Velocity):** Calculated by integrating $a(t)$ and refined by temporal visual features.
3. **$p(t)$ (Pose):** The final joint coordinates $X, Y, Z$.

## Advantages
- **Temporal Smoothness:** By integrating acceleration, the model avoids the "jitter" common in frame-by-frame 2D pose estimators like MediaPipe.
- **Occlusion Robustness:** If $p(t)$ is occluded, the model relies on the stable $a(t)$ signal from the audio to "hallucinate" the most likely joint trajectory.

## Choral Application
We map this to the **Choral Attack Pattern**. The sharp increase in audio envelope (Acceleration) serves as the prior for the "Opening of the Mouth" (Pose). This allows us to maintain synchronization metrics even during video frame drops.
