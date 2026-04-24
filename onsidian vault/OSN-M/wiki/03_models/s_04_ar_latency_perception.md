---
title: S-04 AR Latency Perception
type: source
alchemy_stage: nigredo
tags: [ar, xr, latency, perception, drumming, deep_read]
ingested_date: 2026-04-23
last_deep_read: 2026-04-24
source_count: 1
related: ["[[p_09_how_late]]", "[[minimum_noticeable_delay]]", "[[attention_focus_shift]]", "[[deep_read_audit]]"]
team_take: Full 9-page ISMAR paper. P-09 is the 2-page VRW workshop abstract of the SAME study. S-04 is the canonical source; P-09 subset should cite S-04 for all numerics.
---

# S-04 Studying the Effects of Network Latency on Audio-Visual Perception During an AR Musical Task

**Citation**: Hopkins, T., Weng, S. C.-C., Vanukuru, R., Wenzel, E., Banic, A., Gross, M. D., Do, E. Y.-L. (2022). *2022 IEEE International Symposium on Mixed and Augmented Reality (ISMAR)*, pp. 26 to 34. [DOI:10.1109/ISMAR55827.2022.00016](https://doi.org/10.1109/ISMAR55827.2022.00016). Full 9-page paper.
**Affiliations**: ATLAS Institute, University of Colorado Boulder (Hopkins, Weng, Vanukuru, Wenzel, Gross, Do); Interactive Realities Lab, University of Wyoming (Banic).
**Collaboration**: Ericsson Research acknowledged.
**raw path**: `raw/02_secondary_sources/Studying_the_Effects_of_Network_Latency_on_Audio-Visual_Perception_During_an_AR_Musical_Task.pdf`

## 1. Relationship to P-09

S-04 and [[p_09_how_late]] are **the same study**. P-09 is the 2-page IEEE VRW 2022 workshop abstract; S-04 is the **full 9-page ISMAR 2022 paper**. Same design, same n, same equipment, same F-statistics. S-04 adds qualitative analysis, MIDI tempo variability, focus-shifting test, and limitations section.

**Any citation of P-09's numerics should cite S-04 as the canonical source.**

## 2. Design (identical to P-09, §4)

- 2 × 8 within-subjects: Tasks (Mimic, Improvise) × Latencies (0, 20, 40, 80, 160, 320, 640, 1200 ms)
- Balanced Latin Squares
- **n = 24** participants (university students)
- Stimulus: prerecorded remote drummer at 90 BPM
- **Inter-beat gap**: **667 ms** (correct; P-09 digest said "750 ms" which is an error — 90 BPM → 667 ms)
- Each task 12 s (4 bars × 4 beats)
- 16 tasks per participant (2 tasks × 8 latencies)
- Session ~45 min

**Apparatus**: Nreal Light AR headset, Qualysis 18-camera mocap, Ableton Live 11, Mixamo humanoid avatar, Unity 2020.2.2f1, electronic drum pad.

## 3. Raw Data Block (full set)

**Subjective scales** (1-7) [§4.5]:

1. Delay amount (1=no delay, 7=max delay)
2. Tolerance (1=intolerable, 7=very tolerable / not noticeable)
3. Focus (1=sound, 4=neutral, 7=animation)

| Measure | Statistic | Value | Source |
| :--- | :--- | :--- | :--- |
| Delay perception RM-ANOVA | F(7, 161) | **9.74** | [§5.1.1] |
| Delay perception p | p | **< .001** | [§5.1.1] |
| Delay perception η²_p | η²_p | **0.30** | [§5.1.1] |
| Tolerance RM-ANOVA | F(7, 161) | **9.94** | [§5.1.2] |
| Tolerance p | p | **< .001** | [§5.1.2] |
| Tolerance η²_p | η²_p | **0.30** | [§5.1.2] |
| **Task × Latency interaction (delay)** | F(7, 161) | **2.61** | [§5.1.1] |
| Task × Latency interaction p | p | **.014** | [§5.1.1] |
| Task × Latency interaction η²_p | η²_p | **0.10** | [§5.1.1] |
| Focus (sound vs. animation) RM-ANOVA | F(7, 161) | 9.94 | [§5.1.3] |
| Focus p | p | **> .001 (n.s.)** | [§5.1.3] |

**Task × Latency interaction interpretation** [§5.1.1]: At 160 ms, Improvise reported more noticeable delay than Mimic. At 640-1200 ms, the pattern reverses — Improvise reports LESS noticeable delay. Authors attribute this to cognitive loading during improvisation distracting from delay perception.

**Focus finding** [§5.1.3]: NO significant shift from animation to sound as delay increases. Participants did not shift focus. Mean ~ 4 (neutral). Authors acknowledge this contradicts their hypothesis that focus would shift to sound at high latency.

**MIDI tempo variability** [§5.2]: 3 participants (P3, P16, P24) dropped due to MIDI drum mechanical errors. Linear regression on variance-vs-latency: positive trend lines for most participants, **no significant line fit** due to high variability. No significant objective tempo disruption with increasing latency.

## 4. Limitations (stated, §7)

**Stated explicitly**:

- "Internal validity prioritized over external applicability."
- Remote musician was **simulated (prerecorded)**, not live. Future: real participants on both sides.
- Longer and more natural tasks needed; familiar music; real-time collaboration.
- **Musical experience not stratified**. Novices vs. experienced musicians have different expectations; stratified study would clarify.
- **No gaze tracking**. AR headset eye-tracking could corroborate focus self-report.
- 1200 ms upper limit confounded by 667 ms inter-beat interval (delay nearly 2 full cycles out; "poses a limit for understanding an upper threshold for delay tolerance with regularly spaced drum beats"). Irregular rhythms might reveal upper threshold.

**Implicit**:

- n = 24, all university students, single institution. Demographic narrow.
- AR rendering pipeline latency (Nreal Light) not isolated from injected network latency.
- "Delay tolerance scores never drop below 4 (neutral)" is framed as "tolerable even at 1200 ms" but this is an artifact of the cycle confound, not a genuine tolerance.
- No objective coordination metric (no onset sync, no PLV).
- Subjective self-report only.

## 5. Relevance to Project 8 E(t)

**S-04 is load-bearing for**:

- **160 to 320 ms minimum noticeable delay** threshold in [[latency_thresholds]] and [[audio_visual_mismatch]]. Use S-04 (not P-09) as primary citation since S-04 is the full paper.
- **320 ms tolerance decline threshold** — subjective tolerance drops at 320 ms.
- **[[attention_focus_shift]]**: the finding that focus does NOT shift to sound at high latency contradicts the prior digest framing. Should be corrected.
- **Task-dependent sensitivity**: cognitive loading of improvisation reduces delay perception above 640 ms. Not directly applicable to choir singing (which is not improvisation in most cases) but methodologically interesting.

**S-04 is NOT**:

- Evidence for "audio is clear then tolerable" — that is not what the paper claims. Delay scores rise significantly at 320 ms regardless of audio clarity.
- Evidence that AR visuals can use lower priority than audio — the paper does NOT compare AR to raw video latency thresholds. That comparison is from a different literature (Rottondi 2016, Zoom 150 ms figure).
- Evidence that "human brain's Sensory Integration Window for AR animation is wider than for raw video or audio" — S-04 does not compare AR to video. This claim is Project-8 extrapolation.
- Evidence applicable to choir singing — dyadic drumming, single tempo, short trials.

## 6. Corrections Logged Against Prior Digest

See [[deep_read_audit]] for full table. Summary:

| Issue | Prior claim | Corrected reading |
| :--- | :--- | :--- |
| Missing P-09 relationship | (not stated) | S-04 and P-09 are the same study. S-04 is the full paper; P-09 is the 2-page abstract. Canonical numerics should cite S-04. |
| "Experience remains 'tolerable' (score > 4/7) even at high delays, as long as the audio is clear" | — | Authors themselves caveat: tolerance at 1200 ms is **artifact of cyclic rhythm** (delay = ~2 inter-beat intervals, participants cannot distinguish). "The audio is clear" condition is not what preserves tolerance — the cycle confound does [§6]. |
| **"During Improvisation... players noticed the delay less because they prioritized audio-musical interaction over visual cues"** | — | Partially correct. Paper says cognitive loading of improvisation distracts from delay perception at 640-1200 ms. But at 160 ms Improvise noticed delay MORE than Mimic [§5.1.1]. Interaction is non-monotonic, not a simple "audio priority" story. |
| "Suggests that in a multi-modal NMP system, we can afford a lower packet priority for visual skeletal data compared to audio" | — | **Over-reach**. S-04 does NOT compare packet-priority schemes. Focus-shift test was non-significant (F p > .001). Paper reports that AR latency tolerance is higher than raw-video tolerance cited in prior literature, but does not validate a priority scheme. |
| Missing focus-shift non-significance | (implied but not stated) | Focus-shift hypothesis was NOT supported: F(7,161)=9.94, p > .001, mean ~ 4 (neutral). Participants did NOT shift focus to audio as delay increased [§5.1.3]. Contradicts prior digest implication. |
| Missing MIDI tempo analysis | (not stated) | Tempo variability regression yielded no significant line fit; 3 participants dropped for mechanical errors [§5.2]. Objective coordination not disrupted at tested latencies. |
| Missing task-by-latency interaction | (not stated) | Task × Latency interaction significant F(7,161)=2.61, p=.014, η²=0.10. Non-monotonic pattern [§5.1.1]. |
| Missing Ericsson Research collaboration | (not stated) | Industry acknowledgment; future implications for 5G-AR integration. |
