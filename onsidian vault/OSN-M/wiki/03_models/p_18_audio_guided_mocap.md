---
title: P-18 Audio-Guided MoCap
type: source
alchemy_stage: nigredo
tags: [mocap, multi_modal, string_performance, pose_estimation, audio_visual, deep_read]
ingested_date: 2026-04-23
last_deep_read: 2026-04-24
source_count: 1
related: ["[[pitch_finger_mapping]]", "[[cross_attention_fusion]]", "[[human_object_occlusion]]", "[[deep_read_audit]]"]
team_take: Very specific to string-instrument hand-string contact. 23-camera studio rig required — rules out application to Project 8 home/webcam scenarios. Useful for naming DWPose as SOTA (2023) and for methodological inspiration, not direct transfer.
---

# P-18 Audio Matters Too! Enhancing Markerless Motion Capture with Audio Signals for String Performance Capture

**Citation**: Jin, Y., Qiu, Z., Shi, Y., Sun, S., Wang, C., Pan, D., Zhao, J., Liang, Z., Wang, Y., Li, X., Yu, F., Yu, T., Dai, Q. (2024). *ACM Trans. Graph.* 43(4), Article 90, July 2024. [DOI:10.1145/3658235](https://doi.org/10.1145/3658235). CC-BY 4.0. 10 pages.
**Affiliations**: Central Conservatory of Music (Beijing), Tsinghua University, Weilan Tech. All Chinese.
**Code + dataset**: [Yitongishere/string_performance](https://github.com/Yitongishere/string_performance)
**raw path**: `raw/01_primary_sources/Audio Matters Too! Enhancing Markerless Motion Capture with AudioSignals for String Performance Capture.pdf`

## 1. Capture Setup (§3.1)

- **23 cameras** (violin) or **20 cameras** (cello) in cylindrical rig ~**4 m diameter**
- FLIR ORX-10G-245S8C, **2656×2300 @ 30 fps**, I/O synchronization
- Sony ICD-PX470 microphone, manual clap for A/V alignment
- Solid-colored curtains for background elimination

**Impossible for Project 8 home/webcam scenarios.** This is a research-studio setup.

## 2. Dataset: String Performance Dataset (SPD)

| Field | Value |
| :--- | :--- |
| Instruments | Cello + Violin |
| Performers | **9** (amateurs to professionals) |
| Pieces | **120** (scales, études, classical, pop) |
| Total duration | **> 3 hours** |
| Tuning standard | A4 = 440 Hz |
| Annotations | Body, Hands, Instrument, Bow |

**SPD is first large-scale multi-modal MoCap dataset for string performance with audio alignment.**

## 3. Method (§3)

- **Performer body**: DWPose [Yang et al. 2023], **133 keypoints** (body + hands + face). DWPose is named as SOTA surpassing both OpenPose and MediaPipe [§3.2].
- **Hand pose estimator (HPE)**: Custom model trained on InterHand2.6M + DARTset + BlurHand + HanCo. InterNet backbone modified to output 6D rotation representation. MANO hand model prior.
- **Fusion of DWPose + HPE**: inverse kinematics alignment at wrist, minimize Euclidean distance between hand joints.
- **Instrument**: Google TAPNet for keypoint tracking (nut, bridge) + geometric inference for strings.
- **Bow**: Custom YOLOv8 detector for frog and tip plate.
- **Audio guidance**: Audio pitch → hand-string contact point via vibrating-length formula (§4, Eq. 2). IK constrains fingertip to physical contact position.

## 4. Raw Data Block (Ablation, Table 2)

200 frames test set, 4-view manual 2D annotation → 3D ground truth via triangulation. Metric: MPJPE (mm), aligned at wrist.

| Method | MPJPE (whole hand) | MPJPE (note-playing finger) | Contact Deviation |
| :--- | :--- | :--- | :--- |
| DWPose (baseline, SOTA) | **17.00** | **16.14** | **22.40** |
| HPE w/o audio guidance | 15.27 (↓ 10.2%) | 14.95 (↓ 7.4%) | 16.06 (↓ 28.3%) |
| **HPE + Audio-guided (full)** | **14.93 (↓ 12.2%)** | **13.27 (↓ 17.8%)** | **5.19 (↓ 76.8%)** |

**Contact deviation** is the most improved metric: audio-guided approach reduces it by 76.8% vs. DWPose baseline. This is the load-bearing result of the paper.

## 5. Limitations

**Stated** [§5 Discussion]:

- **Polyphonic performance not supported** — method is monophonic only (assumes single note at a time).
- **Only left hand audio-guided**; right-hand / bow-holding pose underexplored.
- **30 fps** may limit fast-motion accuracy.
- Only pitch used from audio; volume and note duration not leveraged.
- Future: viola, double bass, monocular MoCap.

**Implicit**:

- **23-camera studio** rig — not deployable outside research lab.
- 9 performers, 2 instruments (violin, cello) — narrow domain.
- 3 hours of data, small for generalizable ML.
- Chinese performers + repertoire (classical + Chinese pop) — Western-choir generalization untested.
- No singing/vocal data.
- Contact-deviation metric assumes deterministic pitch-to-finger-position mapping (valid for fretless strings). **No analog for voice** — no fingertip to pull toward.
- DWPose as "SOTA" is 2023-vintage — newer methods may supersede.

## 6. Relevance to Project 8 E(t)

**P-18 is useful for**:

- **Naming DWPose as SOTA whole-body pose estimator (2023)**, surpassing MediaPipe. If Project 8 needs tighter pose accuracy than MediaPipe provides, DWPose is the reference.
- **Methodological inspiration**: the concept of "use audio pitch to constrain visual pose" is an interesting pattern. Whether it transfers to choral singing is unclear because there is no hand-string-contact equivalent for voice.
- **Acknowledgment of vision-based MoCap limits** for subtle musical gestures (paper's implicit critique of MediaPipe-only pipelines).

**P-18 is NOT**:

- Evidence that audio can refine **vocal / facial / head-motion** pose. Paper is about finger-to-string-contact specifically. **Voice has no geometric-contact analog**.
- Applicable to home/webcam choir scenarios (23-camera studio).
- A proof that "Audio is Ground Truth for spatial positioning" in a general sense — it is ground truth for fingertip-to-string contact via well-defined geometric mapping, which does not exist for voice.
- A source for "Mouth/Larynx tracking refinement using Vocal F0." F0 of the voice comes from vocal folds (inside the throat), not from a visible contact point. The analogy does not hold.

## 7. Corrections Logged Against Prior Digest

See [[deep_read_audit]] for full table. Summary:

| Issue | Prior claim | Corrected reading |
| :--- | :--- | :--- |
| Missing 23-camera studio constraint | "completely markerless" (true) | Markerless but **requires 23-camera cylindrical rig, 4 m diameter, FLIR cameras** [§3.1]. Not feasible for Project 8 webcam scenarios. |
| Missing exact MPJPE results | "Audio-Guided Position on the fingerboard" | DWPose 17.00 → HPE+Audio 14.93 mm (whole hand). Contact deviation: 22.40 → 5.19 mm (76.8% improvement) [Table 2]. |
| **"Just as it uses pitch to fix finger poses, we can use Vocal F0 to refine Mouth/Larynx tracking"** | — | **False analogy**. Hand-string contact has a **geometric mapping**: vibrating-length formula L = c × f gives exact fingertip position [§4, Eq. 2]. Voice F0 comes from the vocal folds (not visible, no geometric fingertip analog). Moving this claim to §6 as explicit disclaimer. |
| Missing polyphonic / monophonic caveat | (not stated) | Method is monophonic only. Polyphonic chords not supported [§5]. |
| Missing DWPose SOTA framing | "CREPE to extract high-accuracy pitch curves" | P-18 uses DWPose (not MediaPipe) and names it as SOTA surpassing MediaPipe/OpenPose [§3.2]. Relevant for Project 8's pose-estimator choice. |
| Missing 9-performer / 2-instrument caveat | "120 excerpts of cello and violin, 23 views, completely markerless" | Correct facts but missing context: 9 performers, Chinese, narrow repertoire. Generalization to voice/choir not supported. |
| Missing "pitch-only" audio caveat | (implied in pitch-finger model) | Only pitch used; volume, duration, attack dynamics not leveraged [§5]. Explicit future-work flag. |
