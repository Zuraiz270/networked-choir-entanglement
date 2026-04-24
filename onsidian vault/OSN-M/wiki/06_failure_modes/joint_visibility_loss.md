---
title: Joint Visibility Loss
type: concept
alchemy_stage: citrinitas
tags: [failure_modes, computer_vision, occlusion]
ingested_date: 2026-04-23
source_count: 1
related: ["[[p_03_blazepose_tracking]]", "[[human_object_occlusion]]"]
---

# Joint Visibility Loss

Joint Visibility Loss is a state where a pose estimation model cannot directly see a joint (due to occlusion) and must choose between "dropping" the point or "hallucinating" its position.

## Detection (P-03)
BlazePose includes a dedicated **Visibility Head** in its neural network. For each of the 33 keypoints, it outputs a score:
- **1.0:** Joint is clearly visible.
- **0.5:** Joint is occluded but position is inferred from context (e.g., shoulder visible, elbow occluded, wrist visible).
- **0.0:** Joint is missing or prediction is untrustworthy.

## Impact on E(t)
If we calculate synchrony using only visible joints, we introduce "Metric Jitter" as singers move behind objects.
- **Mitigation:** We only include joints in the $V(t)$ calculation if their visibility score is $> 0.7$.
- **Temporal Filling:** If a joint is temporarily lost (visibility < 0.5), we use the **Hierarchical Motion Dynamics** (P-19) to interpolate its position based on previous acceleration data until the visibility head recovers.
