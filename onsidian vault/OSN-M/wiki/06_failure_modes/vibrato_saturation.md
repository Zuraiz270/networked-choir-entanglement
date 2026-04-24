---
title: Vibrato Saturation
type: concept
alchemy_stage: citrinitas
tags: [failure_modes, signal_processing, vibration]
ingested_date: 2026-04-23
source_count: 1
related: ["[[p_19_viopose_4d]]", "[[hanging_note_inference]]"]
---

# Vibrato Saturation

Vibrato Saturation is a failure mode in visual pose estimation where high-frequency, low-amplitude oscillations (like a violinist's vibrato or a singer's vocal tremor) are "smoothed out" or lost by standard temporal filters.

## Causes
- **Low Sampling Rate:** Webcams at 30fps cannot capture 10-12Hz vibrato cycles without significant aliasing.
- **Temporal Loss Functions:** Standard training targets (like MPJPE) penalize jitter, unintentionally forcing the model to ignore valid sub-millimeter musical movements.

## Detection (P-19)
The VioPose system detects vibrato by identifying "Micro-Acceleration Bursts" in the audio stream. If the audio confirms a pitch fluctuation, the model "un-smooths" the visual pose to allow for the ~10mm oscillations.

## Impact on E(t)
Vibrato is a key feature of **Aesthetic Entrainment**. If the system fails to track the shared vibrato rate among choir members, the Entanglement Index $E(t)$ will underestimate the group's cohesive quality.
