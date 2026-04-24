---
title: P-03 BlazePose Tracking
type: source
alchemy_stage: nigredo
tags: [mocap, computer_vision, mediapipe, real_time, mobile_ai, deep_read]
ingested_date: 2026-04-23
last_deep_read: 2026-04-24
source_count: 1
related: ["[[on_device_inference]]", "[[joint_visibility_loss]]", "[[p_20_mediapipe_preprocessing]]", "[[deep_read_audit]]"]
team_take: Foundation of MediaPipe Pose. 33-keypoint topology, mobile-optimized. Face-detector-as-person-detector assumes head is always visible — a direct constraint for choir singers looking down at music folders.
---

# P-03 BlazePose: On-device Real-time Body Pose Tracking

**Citation**: Bazarevsky, V., Grishchenko, I., Raveendran, K., Zhu, T., Zhang, F., Grundmann, M. (2020). arXiv:2006.10204 [cs.CV]. CVPR Workshop 2020.
**Affiliations**: Google Research, Mountain View, CA.
**raw path**: `raw/01_primary_sources/On-device Real-time Body Pose Tracking. Google AI Blog, CVPR Workshop.pdf`

## 1. Architecture

Detector-tracker pipeline [§2.1, Fig. 1]:

1. **Face detector** (BlazeFace) as person-detector proxy. Assumes head is visible. Outputs: mid-hip point, person circle size, incline angle [§2.2].
2. **Pose tracker**: 33-keypoint regression with combined heatmap+offset+regression head [§2.5, Fig. 4].

**Training trick**: heatmap and offset losses used only during training, removed for inference. Heatmap supervises the regression encoder's internal embedding [§2.5].

**Alignment preprocessing** [§2.6]: rotates/scales/translates so midpoint-between-hips is image center, with 10% scale+shift augmentation for tracker stability.

## 2. Raw Data Block

| Field | Value | Source |
| :--- | :--- | :--- |
| Keypoint count | **33** (superset of BlazeFace + BlazePalm + COCO) | [§2.3, App. A] |
| BlazePose Full | **6.9 MFlop, 3.5M params** | [§3] |
| BlazePose Lite | **2.7 MFlop, 1.3M params** | [§3] |
| BlazePose Full FPS on Pixel 2 | **102** | [§3, Table 1] |
| BlazePose Lite FPS on Pixel 2 | **312** | [§3, Table 1] |
| OpenPose body-only FPS (20-core Intel i9-7900X) | **0.41** | [§3, Table 1] |
| BlazePose Full PCK@0.2 AR dataset | **84.1** | [§3, Table 1] |
| BlazePose Full PCK@0.2 Yoga/Fitness | **84.5** | [§3, Table 1] |
| BlazePose Lite PCK@0.2 AR | **79.6** | [§3, Table 1] |
| BlazePose Lite PCK@0.2 Yoga/Fitness | **77.6** | [§3, Table 1] |
| OpenPose PCK@0.2 AR | 87.8 | [§3, Table 1] |
| OpenPose PCK@0.2 Yoga/Fitness | 83.4 | [§3, Table 1] |
| Human annotator baseline | **97.2** (re-annotation Pearson-like agreement) | [§3] |
| Speedup vs. OpenPose | **25× to 75×** | [§3] |

**Training data** [§2.4]: 60K single-or-few-people images in common poses + 25K single-person fitness images = **85K total**. All human-annotated. Occlusion-simulating augmentation (random colored rectangles).

**Evaluation** [§3]: Two in-house annotated datasets (1000 images each, 1-2 people per image): AR dataset (wild poses) + Yoga/Fitness. Mapped to MS COCO 17-point subset for comparison with OpenPose. Metric: PCK@0.2 (2D Euclidean error within 20% of torso size).

## 3. 33 Keypoints (App. A)

Head (0-10): nose, eyes (inner/outer/center), ears, mouth corners.
Upper body (11-22): shoulders, elbows, wrists, hands (pinky, index, thumb knuckles).
Lower body (23-32): hips, knees, ankles, heels, foot index.

Topology is richer than OpenPose (25 kpts) and Kinect (26 kpts) on hands/feet; sparser on face.

## 4. Limitations

**Implicit (paper has no formal §Limitations)**:

- **Single-person use case** (§1, §2.2). Multi-person scenes require per-person detection pass.
- **Assumes head always visible**. Face-detector-as-person-detector breaks when head is occluded, tilted down, or out of frame. **Direct constraint for choir singers looking down at music folders or wearing masks**.
- **Training data bias**: 85K images, no breakdown of demographic, cultural, body-type diversity. Fitness-heavy (25K fitness + 60K "common poses").
- **PCK@0.2 threshold is lenient**: 20% of torso size for a typical adult ~10 cm error. Adequate for gesture recognition; **marginal for sub-cm head-sway sync metrics** that Project 8 may need.
- No temporal smoothing claims; frame-to-frame jitter not quantified in paper.
- Inference speed on Pixel 2 (2017 flagship); current phones faster, but also faster CPUs available for desktop processing.
- Heatmap branch discard = loss of multi-person generalization; cannot easily extend to multi-person without retraining.
- Per-point visibility classifier mentioned [§2.6] but no quantitative evaluation of its accuracy.

## 5. Relevance to Project 8 E(t)

**P-03 is load-bearing for**:

- **[[entanglement_index]] V(t) head-motion extraction pipeline**: MediaPipe Pose (Google's productionized BlazePose) is Project 8's default choice for per-singer pose tracking. 33-keypoint topology directly inherits.
- **Nose keypoint (index 0)**: matches [[p_14_husync]]'s AlphaPose nose-keypoint use for head-motion PLV. Project 8 can apply same PLV pipeline.
- **Mobile-first design**: supports decentralized Project 8 deployment scenarios (each singer's device runs pose locally).
- **[[joint_visibility_loss]]**: BlazePose has per-point visibility classifier but limited empirical validation in paper.

**P-03 is NOT**:

- Evidence of BlazePose accuracy on **choir singers** specifically (not in training set). Accuracy on subtle head-sway, breathing-related torso motion, or choir-specific postures untested.
- Evidence for sub-cm precision. PCK@0.2 implies ~10 cm error acceptable; Project 8's head-sway PLV analysis may need tighter.
- A multi-person tracker. For multi-singer video frames, need separate pipeline (e.g., YOLO-detector → BlazePose-per-crop).
- A source for the "Visibility Classifier hallucinates occluded joints" claim in prior digest — paper says classifier **flags** inaccurate predictions, not that it fills them in.

## 6. Corrections Logged Against Prior Digest

See [[deep_read_audit]] for full table. Summary:

| Issue | Prior claim | Corrected reading |
| :--- | :--- | :--- |
| "30+ FPS on mid-tier smartphones" understates | — | BlazePose Full = **102 FPS** on Pixel 2; Lite = **312 FPS** [§3, Table 1]. "30+" is the minimum from abstract language, actual is ~10× higher. |
| Missing exact PCK values | "Outperforms OpenPose in specific use cases (Yoga/Fitness)" | Full: 84.1/84.5 vs. OpenPose 87.8/83.4. BlazePose Full **loses on AR** (84.1 vs 87.8) but **wins on Yoga/Fitness** (84.5 vs 83.4) [Table 1]. Prior digest reversed the AR result. |
| Missing speedup figure | — | **25× to 75× faster** than OpenPose on mobile vs. 20-core desktop CPU [§3]. |
| Missing training data size | — | 85K images (60K common + 25K fitness), all human-annotated [§2.4]. |
| **"Visibility Classifier hallucinates breathing and posture joints behind the folder, maintaining continuity of our metrics"** | — | **Over-reach**. Paper says per-point visibility classifier "indicates whether a particular point is occluded and if the position prediction is deemed inaccurate" [§2.6]. It **flags** inaccuracy; it does not "hallucinate" accurate joints behind occlusions. Quantitative accuracy of the classifier is not reported. |
| Missing head-visibility-required caveat | (not stated) | BlazePose's face-detector-proxy requires head to be visible [§2.2]. Direct constraint for choir settings with music folders, lowered heads, or masks. |
| Missing PCK@0.2 metric caveat | (not stated) | PCK@0.2 = 20% of torso size error tolerance, ~10 cm for adults. Adequate for gestures, marginal for sub-cm head-sway PLV analysis [§3]. |
