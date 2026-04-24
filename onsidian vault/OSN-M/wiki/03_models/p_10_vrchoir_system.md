---
title: P-10 VRChoir System
type: source
alchemy_stage: nigredo
tags: [nmp, choir, virtual_reality, unity, jamulus, deep_read]
ingested_date: 2026-04-23
last_deep_read: 2026-04-24
source_count: 1
related: ["[[vr_avatar_presence]]", "[[conductor_perceptual_bottleneck]]", "[[p_11_chamber_choir]]", "[[deep_read_audit]]"]
team_take: Small 2-page VRW workshop abstract. n=11 total, single song, median geographic distance 0.29 km — not a real remote test. Qualitative only, no statistics. Confirms conductor-latency-bottleneck pattern seen in P-11.
---

# P-10 VRChoir: Exploring Remote Choir Rehearsals via Virtual Reality

**Citation**: Di, T., Medeiros, D., Sousa, M., Grossman, T. (2023). In *2023 IEEE Conference on Virtual Reality and 3D User Interfaces Abstracts and Workshops (VRW)*, pp. 895 to 896. [DOI:10.1109/VRW58643.2023.00290](https://doi.org/10.1109/VRW58643.2023.00290). **2-page workshop abstract.**
**Affiliations**: Department of Computer Science, University of Toronto; School of Computing Science, University of Glasgow.
**raw path**: `raw/01_primary_sources/VRChoir_Exploring_Remote_Choir_Rehearsals_via_Virtual_Reality.pdf`

## 1. System (§2)

- Unity + Photon PUN multiplayer networking
- Oculus Quest 2 headsets
- Full-body 3D avatars with inverse kinematics (IK) on controller hands
- Virtual concert hall with music panel (score, title, composer, menu)
- **Jamulus** for audio transmission (external, separate from VR)
- No facial expression capture; no hand tracking (controllers only)

## 2. Evaluation

- **9 singers** (5M / 4F) + **2 professional conductors** (C1, C2; 7-8 years conducting experience)
- 3 groups total (2-3 singers + 1 conductor each)
- Song: **Amazing Grace** (single song, iterated until conductor satisfied)
- 6-point Likert survey + semi-structured interviews
- Usability (SEQ), co-presence, attention, info understanding

**Geographic distances from moderator** [§2]: most within **1 km**, **median = 0.29 km**. Exceptions: C2 at 22.11 km, S9 at 500.95 km. **This is not a true long-distance remote test** — most participants in same local network.

## 3. Raw Data Block (§3.2, Fig. 2, Likert medians)

Results reported as 6-point Likert medians + IQR. **No inferential statistics.**

| Item | Singers | Conductors |
| :--- | :--- | :--- |
| Q1.1 Enjoyment (singers only) | high | — |
| Q1.2 Ability to focus on tasks | high | **M = 3, IQR = 1** (low; attributed to audio latency) |
| Q1.3 SEQ task difficulty | high | — |
| Q2.1 Co-presence with conductor | strong | — |
| Q2.2 Co-presence with other singers | strong (C2: low due to internet latency) | — |
| Q3.1 Easy to pay attention | M = 6 | M = 6 |
| Q3.2 Remain focused | M = 6 | M = 6 |
| Q4 Non-verbal info fidelity | higher than conductors | low (C2: VR controllers inadequate for formal performance) |

## 4. Qualitative Findings (§3.2)

- S4: "makes me able to see others more realistically. I like the feeling and atmosphere of the people around me."
- C1: VRChoir "really brought back the sense of togetherness compared to Zoom."
- **C2 complaint**: VR controllers "inadequate for formal choral performances and more advanced choral rehearsals."
- **C2 suggestion**: "avatar should show facial expression" — "facial expression plays a vital role in conveying the message of the conductor."
- **Conductor-latency sensitivity**: both conductors reported higher latency impact than singers.

## 5. Limitations

**Stated** [§4]:

- Future work: scale to larger studies, direct Zoom comparison, improve technological limitations.
- Authors acknowledge: "starting point for more effective remote music rehearsals" (tentative framing).

**Implicit**:

- **Workshop abstract, 2 pages.** Not full peer-reviewed paper.
- **n = 11 total** (9 singers + 2 conductors) across 3 groups. Small.
- **Amazing Grace only** (simple, familiar, easy). Generalization to complex choral repertoire untested.
- **Median participant distance 0.29 km** — participants effectively co-located on same LAN. Not a genuine remote-rehearsal test.
- No quantitative inferential statistics; Likert medians + IQR only.
- VR controllers (not hand tracking), no facial expressions on avatars — critical limitations for conducting fidelity acknowledged by C2.
- No direct Zoom-comparison trial (only participant recall of prior Zoom experience).
- No objective coordination metric (onset sync, intonation, PLV).
- Jamulus performance assumed, not measured in this study.
- Oculus Quest 2-specific; other headsets untested.

## 6. Relevance to Project 8 E(t)

**P-10 is useful for**:

- **Conductor-latency-sensitivity**: confirms the [[conductor_perceptual_bottleneck]] pattern observed in [[p_11_chamber_choir]]. Conductors report latency impact more than singers (M=3 vs high).
- **VR-as-alternative-to-Zoom framing**: provides qualitative evidence that VR avatars can restore "sense of togetherness." Small-n qualitative only.
- **Jamulus-as-audio-backbone** precedent: VRChoir architecturally separates audio (Jamulus) from video (VR), same pattern as P-11 Jamulus@Univ.
- **Missing-affordances findings**: hand-tracking (vs controllers) and facial-expression rendering identified as critical for conducting — useful for Project 8 Tier-3 design speculation.

**P-10 is NOT**:

- A statistically validated comparison (Likert medians, n=11, no inferential tests).
- Evidence that VR improves objective musical coordination. Paper measures co-presence and enjoyment, not synchrony.
- A true remote-distance test (participants were mostly co-located).
- Source of any specific "Visual Gaze Index V_g(t)" formulation — that is Project-8 speculation.
- Evidence that specific latency threshold causes conducting collapse. Paper reports the pattern qualitatively; no latency numbers logged for conductor condition.

## 7. Corrections Logged Against Prior Digest

See [[deep_read_audit]] for full table. Summary:

| Issue | Prior claim | Corrected reading |
| :--- | :--- | :--- |
| Missing 2-page-abstract caveat | "In IEEE VR 2023" | 2-page workshop abstract, not full peer-reviewed paper. VRW pp. 895-896 [title page]. |
| Missing n | (not stated) | n = 11 (9 singers + 2 conductors); 3 groups [§3]. |
| **Missing geographic co-location caveat** | — | Median distance 0.29 km. Most participants effectively on same local network. Not a genuine remote test [§2]. |
| "Latency Sensitivity: The conductor's ability to maintain the tempo is highly sensitive to even minor network jitter, more so than the singers" | — | Correct pattern but **not quantified**. Likert Q1.2 M=3 for conductors vs. high for singers. No objective tempo measurement [§3.2]. |
| Missing "Amazing Grace single song" | "Synchronized with Jamulus for real-time audio" | One song, repeated iterations. Not representative of complex repertoire [§3.1]. |
| "Significant increase in Co-presence compared to Zoom" | — | Comparison is implicit (participant recall of Zoom), no direct Zoom baseline in experiment. Authors flag direct Zoom comparison as future work [§4]. |
| "E(t) should include a Visual Gaze Index V_g(t)" | — | Project-8 extrapolation. P-10 does not propose or measure gaze indices; it uses co-presence and attention Likert ratings [§3.1]. Moved to §6 as labeled extrapolation. |
| Missing VR-controller limitations | (implied) | C2 explicit: controllers "inadequate for formal choral performances." Hand tracking and facial expression flagged as critical future additions [§3.2, §4]. |
