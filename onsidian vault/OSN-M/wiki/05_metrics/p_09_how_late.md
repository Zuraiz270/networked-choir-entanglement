---
title: P-09 How Late is Too Late?
type: source
alchemy_stage: nigredo
tags: [latency, perception, ar, synchronization, deep_read]
ingested_date: 2026-04-23
last_deep_read: 2026-04-23
source_count: 1
related: ["[[latency_thresholds]]", "[[audio_visual_mismatch]]", "[[deep_read_audit]]"]
team_take: Confirms 160-320 ms noticeable-delay range for drumming in AR (n=24, single session). Paper's "no upper tolerance limit" claim is undermined by its own cyclic-rhythm confound and should not be cited at face value.
---

# P-09 How Late is Too Late? Effects of Network Latency on Audio-Visual Perception During AR Remote Musical Collaboration

**Citation**: Hopkins, T., Weng, S. C.-C., Vanukuru, R., Wenzel, E., Banic, A., Do, E. Y.-L. (2022). *2022 IEEE Conference on Virtual Reality and 3D User Interfaces Abstracts and Workshops (VRW)*, 686 to 687. [DOI:10.1109/VRW55335.2022.00194](https://doi.org/10.1109/VRW55335.2022.00194). ATLAS Institute (CU Boulder) + Interactive Realities Lab (U Wyoming). **2-page workshop abstract** (not full paper).
**raw path**: `raw/01_primary_sources/How_Late_is_Too_Late_Effects_of_Network_Latency_on_Audio-Visual_Perception_During_AR_Remote_Musical_Collaboration.pdf`

## 1. Design

- **2 × 8 within-subjects factorial** [p. 686, §2]
  - Factor 1 (Task): Mimic, Improvise
  - Factor 2 (Latency): 0, 20, 40, 80, 160, 320, 640, 1200 ms
- Balanced Latin Squares across conditions to control ordering [p. 686, §2]
- **n = 24** participants [p. 686, §2]
- Stimulus: pre-recorded remote drummer at **90 BPM** (750 ms between hits), 4/4 time
- Mimic: strict 4/4. Improvise: free-form at 90 BPM [p. 686, §2]

## 2. Apparatus

- **Nreal Light** AR headset [p. 686, §2]
- 18-camera **Qualisys** motion capture [p. 686, §2]
- Electronic drum pad
- Ableton DAW (audio recording)
- Mixamo humanoid avatar
- Unity 2020.2.2f1 [p. 686, §2]

## 3. Raw Data Block

| Measure | Statistic | Value | Source |
| :--- | :--- | :--- | :--- |
| Subjective delay (1-7 scale), RM-ANOVA | F(7, 161) | **9.74** | [p. 687, §3] |
| Subjective delay, p-value | p | **< .001** | [p. 687, §3] |
| Subjective delay, partial η² | η²_p | **0.30** | [p. 687, §3] |
| Delay tolerance (1-7 scale), RM-ANOVA | F(7, 161) | **9.94** | [p. 687, §3] |
| Delay tolerance, p-value | p | **< .001** | [p. 687, §3] |
| Delay tolerance, partial η² | η²_p | **0.30** | [p. 687, §3] |
| Mauchly's sphericity violation | — | **None** across RM-ANOVAs | [p. 687, §3] |
| Post-hoc | — | LSD tests | [p. 687, §3] |

**LSD group structure** (both analyses): {0, 20, 40, 80, 160 ms} significantly smaller than {320, 640, 1200 ms} [p. 687, §3].

## 4. Key Findings

- **Minimum noticeable delay**: between **160 and 320 ms** [p. 687, §3]. Paper's own phrasing: "higher than 160ms and possibly less than 320ms."
- **Tolerance threshold**: significant decline at **320 ms** [p. 687, §3]. At this level participants' tolerance scores drop below the neutral midpoint (4) of the 1-7 scale.
- **Upper tolerance limit**: **[NOT-DETERMINED]**. Paper claims "no upper limit to audio-visual delay tolerance" [p. 686, Abstract], but the same section admits that at **1200 ms** the delay exceeds nearly one full inter-hit interval (750 ms), confounding within-cycle vs. cross-cycle perception [p. 687, §3]: "a player will not be able to distinguish the discrepancy in delay between cycles." The no-upper-limit claim is therefore an experimental artefact of the 90 BPM rhythm, not an empirical result.

## 5. Limitations

**Stated** [p. 687, §3]:

- Further studies "needed to understand audio-visual delay tolerance upper limits" with irregular rhythms.
- Musical experience was not controlled as a covariate; flagged as future work.
- Future studies to investigate the 160 to 320 ms range more precisely.

**Implicit (binding on any citation)**:

- Workshop abstract (2 pages), not full peer-reviewed paper.
- Single tempo (90 BPM), single meter (4/4).
- Subjective self-report only; no objective performance outcome.
- Pre-recorded partner; no bidirectional live interaction.
- AR rendering pipeline latency (Nreal Light) is not separated from the injected network latency conditions.
- "No upper limit" is contradicted by the authors' own cyclic-confound note; must not be cited at face value.

## 6. Relevance to Project 8 E(t)

Project 8 uses P-09 as the primary evidence for the **320 ms audio-visual mismatch threshold** in [[latency_thresholds]]. This citation is sound for:

- Drumming in AR at 90 BPM with a drum-pad interface.
- Subjective audio-visual mismatch perception (not interpersonal coordination metrics).

This citation does **not** extend to:

- Choral singing (sustained tones, no percussive attack).
- Real-time bidirectional ensembles.
- Objective performance metrics (timing accuracy, onset synchronization).

Any Project-8 claim that V(t) should be "penalized more heavily above 320 ms" is an **extrapolation** from P-09's subjective-perception result to an objective metric definition. Flag as such in any paper or methods section.

## 7. Corrections Logged Against Prior Digest

See [[deep_read_audit]] for full table. Summary:

| Issue | Prior claim | Corrected reading |
| :--- | :--- | :--- |
| Missing statistics | "significantly noticing delay" | F(7,161)=9.74, p<.001, η²=0.30 (delay); F(7,161)=9.94, p<.001, η²=0.30 (tolerance) [p. 687]. |
| Missing n | (not stated) | n = 24, 2×8 within-subjects, Balanced Latin Squares [p. 686]. |
| Missing apparatus | "AR" | Nreal Light + 18-camera Qualisys mocap + Ableton + Mixamo + Unity [p. 686]. |
| "Cyclic Masking" (new term coined by prior digest) | "makes the delay harder to quantify subjectively but still disruptive" | Paper says the cycle confound undermines the upper-threshold measurement itself at 1200 ms, not that disruption persists. The "no upper limit" abstract claim is thus an artefact. Prior digest's over-interpretation removed. |
| Missing workshop-abstract caveat | Treated as full research paper | 2-page IEEE VRW workshop abstract; subjective self-report only; pre-recorded partner; single tempo. |
| "Relevance to E(t)" projected Project-8 V(t) weighting policy | "Our V(t) index should be weighted to penalize synchronization failures more heavily once they cross the 320ms boundary" | Moved to explicit Project-8 extrapolation label in §6. |
