---
title: Human-Object Occlusion
type: concept
alchemy_stage: citrinitas
tags: [failure_modes, mocap, computer_vision]
ingested_date: 2026-04-23
source_count: 1
related: ["[[p_18_audio_guided_mocap]]", "[[attention_focus_shift]]"]
---

# Human-Object Occlusion

Human-Object Occlusion is a primary failure mode in markerless motion capture where the instrument (or another performer) physically blocks the camera's view of a joint.

## Specific Challenges in NMP
1. **Instrument Occlusion:** The cello/violin body blocking the left hand. In choirs, this is often the **Music Stand** or a **Sheet Music Folder** blocking the larynx or mouth.
2. **Self-Occlusion:** The performer's own torso or arms blocking the camera during expressive movements.
3. **Depth Ambiguity:** 2D pose estimators struggling to determine if a hand is *on* the instrument or *behind* it.

## Mitigation (P-18)
- **Multi-View Integration:** Using up to 23 cameras to ensure at least 4 clear views of every joint.
- **Audio Constraints:** Using the sound as a "non-visual sensor" that is immune to physical occlusion.
