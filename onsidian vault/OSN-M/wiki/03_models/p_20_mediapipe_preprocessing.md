---
title: P-20 MediaPipe Preprocessing
type: source
alchemy_stage: nigredo
tags: [mediapipe, preprocessing, normalization, sign_language, dtw, deep_read]
ingested_date: 2026-04-23
last_deep_read: 2026-04-24
source_count: 1
related: ["[[pose_standardization]]", "[[handedness_bias]]", "[[phase_locking_value]]", "[[deep_read_audit]]"]
team_take: MediaPipe preprocessing pipeline for sign-language similarity analysis. Dominant-hand and handedness normalization techniques are potentially transferable, but sign language is highly articulated hand motion — choir-singer motion is much less demanding. Not a direct methodology fit.
---

# P-20 Preprocessing MediaPipe Joint Annotation for Sign Language Similarity Analysis

**Citation**: Manseri, K., Bigeard, S., Ouni, S. (2025). In *ACM International Conference on Intelligent Virtual Agents (IVA Adjunct '25)*, September 16-19, 2025, Berlin, Germany. 9 pages. [DOI:10.1145/3742886.3756716](https://doi.org/10.1145/3742886.3756716). CC-BY 4.0.
**Affiliation**: Université de Lorraine, CNRS, Inria, LORIA, Nancy, France.
**raw path**: `raw/01_primary_sources/Preprocessing MediaPipe Joint Annotation for Sign LanguageSimilarity Analysis.pdf`

## 1. Task & Datasets

**Task**: Sign-language similarity analysis — identify phonetically identical signs across languages without using glosses or metadata. DTW (Dynamic Time Warping) on preprocessed MediaPipe keypoints [§1].

**Datasets**:

| Dataset | Videos | Sign languages | Notes |
| :--- | :--- | :--- | :--- |
| Multilingual Sign Language WordNet (MSLW) | 10,321 | 6 (BSL, GSL, NGT, STS, PJM, DSGS) | Multiple signers + backgrounds per dataset |
| ASLLVD | 7,963 | ASL only | All right-handed signers |

## 2. Feature Set (§1)

**50 MediaPipe keypoints per frame** (2D only):

- 8 upper-body joints (nose, neck, shoulders, elbows, wrists)
- 21 landmarks per hand × 2 hands

No face-mesh, no lower body, no 3D.

## 3. Preprocessing Pipeline (§5)

**Step 1. Missing-keypoint interpolation** [§5.1, Zelinka & Kanis 2023]:

- Weighted average of corresponding keypoint in neighboring frames
- Weights based on MediaPipe confidence scores
- **Condition**: hand interpolated only if detected in > 10% of frames AND not perfectly immobile (non-real hands flagged and zeroed)

**Step 2. Dominant hand identification** [§5.2]:

- Primary: hand with higher average velocity (wrist displacement / frame)
- Fallback: if right-hand fastest, use maximum y-coordinate; higher hand = dominant
- Evaluation (Table 1): **1000 one-handed + 1000 two-handed per dataset** (WordNet had 50% left-handed signers; ASLLVD all right-handed)

**Step 3. Vertical flip** [§5.2.3]: If dominant = left, flip x-coordinate (x' = 1 - x) so dominant is always on left side.

**Step 4. Passive arm normalization** [§5.3]:

- Polar-to-Cartesian reconstruction: x1 = x0 + d·(-cos(angle)), y1 = y0 + d·sin(angle)
- d = average limb length from opposite side
- Angles set to mimic "natural resting position"

## 4. Raw Data Block (Table 1 — Dominant Hand Identification Accuracy)

| Sign type | WordNet | ASLLVD |
| :--- | :--- | :--- |
| One-handed | **0.99** | 0.97 |
| Two-handed | 0.93 | 0.90 |
| All | **0.96** | 0.94 |

Error sources [§5.2.2]:

- Inaccurate MediaPipe hand labels (most errors)
- Rapid non-dominant hands with similar configurations (two-handed)
- Non-dominant hand small movements at video start (Noema, BSL SignBank)

## 5. Limitations

**Stated** [§7, §5]:

- Some datasets (Noema, DSGS) authorised access only partial.
- "Non-real hand" threshold of 10% detection is heuristic; no rigorous evaluation.
- Passive-arm normalization uses arbitrary angles for resting position.

**Implicit (binding on Project 8 citation)**:

- **Sign language domain**: highly articulated hand motion; not directly comparable to choir singing (minimal hand motion, primarily head sway and mouth shape).
- **2D keypoints only** — no depth, no 3D pose.
- **MediaPipe-specific** — other pose estimators (OpenPose, DWPose, BlazePose) not tested.
- **Frontal view required** — close-up, single-signer, frontal framing. Choir video is multi-person, varying angles.
- **ASLLVD all right-handed** — method validation on handedness is partly asymmetric.
- **Dictionary-style videos** (cropped, similar length, similar framing) — not wild/noisy webcam input.
- Qualitative UMAP clustering is subjective assessment; no inferential significance tests on clustering improvement.
- **No quantitative "cpCER" metric** reported in the paper — prior digest claim of "+31% cpCER improvement" is not in the text (cpCER is a speech-recognition metric from P-05, not relevant here).

## 6. Relevance to Project 8 E(t)

**P-20 is useful for**:

- **MediaPipe preprocessing recipe**: Project 8's V(t) pipeline can adopt the confidence-weighted interpolation and non-real-hand flagging for subtle cases where MediaPipe drops frames.
- **[[handedness_bias]]**: relevant concept for any pose-comparison across signers.
- **[[pose_standardization]]**: direct methodology for normalizing keypoint coordinates across different body types and camera distances.
- Dominant-hand ID (velocity + height fallback) is a reasonable method if ever needed.

**P-20 is NOT**:

- Directly applicable to choir singing. Choir singers don't have a "dominant hand" in the signing sense; their hands mostly hold music folders or rest.
- A source for "+31% cpCER improvement" (prior digest claim). That is not in the paper. cpCER is a speech-recognition metric (from P-05).
- A source for "shoulder-anchor scaling" as a named technique in this paper. Scaling normalizations are mentioned only in related-work [§2.2, Fragkiadakis et al.; Boháček & Hrúz's wrist-bounding-box].
- A 3D pose source.

## 7. Corrections Logged Against Prior Digest

See [[deep_read_audit]] for full table. Summary:

| Issue | Prior claim | Corrected reading |
| :--- | :--- | :--- |
| **"+31% cpCER improvement in dictionary matching"** | — | **Fabricated**. cpCER is not used in P-20 — it is a speech-recognition metric from P-05. P-20 reports dominant-hand-identification accuracy (Table 1) and qualitative UMAP clustering improvement, not cpCER. |
| "Anchor-Based Scaling: Uses the shoulder-to-shoulder distance as a stable denominator" | — | **Not in P-20's own pipeline**. Shoulder scaling is mentioned only in related work (Fragkiadakis et al. [10]). P-20's novel contributions are dominant-hand ID + passive-arm normalization + interpolation, NOT shoulder-anchor scaling. |
| Missing dataset specifics | "Sign Language (SL) similarity" | 10,321 WordNet videos across 6 sign languages + 7,963 ASLLVD videos [§3]. |
| Missing exact dominant-hand accuracy | (not stated) | WordNet 0.96, ASLLVD 0.94 (all signs); 0.99/0.97 one-handed; 0.93/0.90 two-handed [Table 1]. |
| Missing 50-keypoint spec | "MediaPipe pose data" | 50 keypoints (8 upper body + 21×2 hands); 2D only [§1]. No face mesh, no lower body. |
| Domain transfer claim | "directly applicable to any gesture-heavy task like choral conducting or singing" | Over-reach. Sign language is highly articulated hand motion; choir singing is minimal hand motion + subtle head sway. Direct methodology transfer is limited; only the interpolation and handedness concepts apply broadly. |
| Missing polar-to-Cartesian formulation | "Passive Arm Normalization" | Eqs. 2-3: x1 = x0 + d·(-cos(angle)), y1 = y0 + d·sin(angle), with d = opposite-side limb length, arbitrary angles [§5.3]. |
| Missing 2D-only caveat | (not stated) | No depth information. Choir applications needing 3D head sway require different pipeline [§1]. |
