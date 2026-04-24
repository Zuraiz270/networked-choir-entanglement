---
title: Handedness Bias
type: concept
alchemy_stage: citrinitas
tags: [failure_modes, metrics, symmetry]
ingested_date: 2026-04-23
source_count: 1
related: ["[[p_20_mediapipe_preprocessing]]", "[[conductor_perceptual_bottleneck]]"]
---

# Handedness Bias

Handedness Bias is a failure mode in gesture analysis where a model fails to recognize the "same" motion because it is performed by the opposite hand (left vs. right).

## Consequences in NMP
- **Correlation Failure:** A right-handed conductor and a left-handed soloist might be perfectly in sync, but a simple coordinate-based correlation metric would show them as "anti-correlated" because their hands are moving in opposite directions in the image plane.
- **Cluster Isolation:** Left-handed performers will form their own separate cluster in UMAP/PCA visualizations, making it difficult to identify group-wide entrainment patterns.

## Mitigation (P-20)
- **Automatic Dominant Hand Detection:** Using average velocity and maximum vertical height to identify the "Lead" hand.
- **Vertical Flipping:** Mirroring the coordinate system ($x' = 1 - x$) for left-dominant performers to project all data into a "Right-Dominant" latent space.
