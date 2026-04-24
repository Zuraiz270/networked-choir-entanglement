---
title: Perceptual Delay Masking
type: concept
alchemy_stage: citrinitas
tags: [failure_modes, xr, perception]
ingested_date: 2026-04-23
source_count: 1
related: ["[[p_23_immersive_nmp_qoe]]", "[[minimum_noticeable_delay]]"]
---

# Perceptual Delay Masking

Perceptual Delay Masking is a phenomenon where the use of immersive visual representations (3D avatars, XR) reduces the user's awareness of network latency.

## Mechanism
- **MoCap Decoupling:** In a 2D video, every dropped packet is visible as a "stutter." In a 3D avatar system, the local engine can interpolate motion (Phase 7 implementation), masking minor jitter.
- **Focus Shift:** Immersive environments encourage a "Peripheral Vision" mode (P-23), which is less sensitive to the precise timing of pixel updates than the "Direct Gaze" mode used in 2D videoconferencing.

## Role in SNA-OSN-M
This concept justifies our focus on **Avatar-based Visualization**. By moving the choir into a virtual concert hall, we create a "Perceptual Buffer" that allows for a stable $E(t)$ even when the underlying 5G network (P-15) experience burst errors.
