---
title: Pose Standardization
type: concept
alchemy_stage: citrinitas
tags: [computer_vision, normalization, geometry]
ingested_date: 2026-04-23
source_count: 1
related: ["[[p_20_mediapipe_preprocessing]]", "[[p_14_husync]]"]
---

# Pose Standardization

Pose Standardization is the process of removing extrinsic noise (camera distance, morphology, orientation) from skeletal tracking data to isolate the intrinsic motion.

## Standard Workflow (P-20)
1. **Origin Translation:** Shifting the coordinate system so the Neck (Body) or Wrist (Hand) is at $(0,0,0)$.
2. **Morphological Scaling:** Dividing all joint vectors by a stable anchor (e.g., Shoulder-to-Shoulder width).
3. **Handedness Alignment:** Vertically flipping $X$-coordinates to ensure the "Action Hand" is always on the same side for similarity analysis.

## Impact on SNA-OSN-M
Without standardization, our synchronization metrics would be biased by the "loudest" visual signal (the singer closest to the camera). Standardization ensures that every performer's contribution to the **Visual Coupling Index $V(t)$** is weighted equally based on their relative effort, not their physical size or distance.
