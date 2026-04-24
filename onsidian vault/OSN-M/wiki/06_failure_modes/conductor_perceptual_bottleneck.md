---
title: Conductor Perceptual Bottleneck
type: concept
alchemy_stage: citrinitas
tags: [failure_modes, choir, conducting, latency]
ingested_date: 2026-04-23
source_count: 1
related: ["[[p_10_vrchoir_system]]", "[[attention_focus_shift]]"]
---

# Conductor Perceptual Bottleneck

The "Conductor Perceptual Bottleneck" refers to the finding that choral conductors suffer more from NMP degradations (latency, low gesture fidelity) than the singers themselves.

## Causes
1. **High Temporal Precision:** Conductors lead the tempo. A 20ms audio lag is perceived by them as a "drag" on the entire ensemble.
2. **Gesture Fidelity:** Standard VR controllers (Quest 2) lack the finger-level resolution needed for nuanced choral expressions (e.g., cut-offs, dynamics).
3. **Facial Information Loss:** Choral conducting relies heavily on mouth shapes and eye contact, which are often absent or uncanny in current VR avatars.

## Project Mitigation
In the SNA-OSN-M dashboard, we must treat the **Conductor's Node** as the "Master Clock." We should prioritize bandwidth for the conductor's visual feed (Hand Tracking + Facial Rig) over the singers' feeds to ensure the group doesn't collapse into rhythmic chaos.
