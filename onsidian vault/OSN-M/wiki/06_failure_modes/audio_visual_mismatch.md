---
title: Audio-Visual Mismatch
type: concept
alchemy_stage: citrinitas
tags: [latency, perception, ar, failure_modes, deep_read]
ingested_date: 2026-04-23
last_updated: 2026-04-24
source_count: 2
related: ["[[p_09_how_late]]", "[[s_04_ar_latency_perception]]", "[[latency_thresholds]]", "[[deep_read_audit]]"]
---

# Audio-Visual Mismatch

Audio-Visual Mismatch occurs in NMP when the auditory signal and the visual signal (pose, facial expression, or video) of a collaborator arrive at different times due to differing network processing loads.

> **Same-study note (2026-04-24):** [[p_09_how_late]] (IEEE VRW 2022 workshop abstract, 2 pages) and [[s_04_ar_latency_perception]] (ISMAR 2022 full paper, Hopkins et al.) are **the same study at two venues**. S-04 is the full report with F-statistics (Task × Latency interaction F=2.61, p=.014, η²=.10). The often-cited "1200 ms tolerance" is a **cyclic-rhythm-confound artifact** at the 1200 ms test condition, not a real perceptual ceiling on free-rhythm tasks. See [[latency_thresholds]] for the full provenance table.

## In AR Environments

Visual data typically requires significantly more processing than audio, leading to a "visual lag" even if the audio is real-time. S-04 (the full paper) reports that audio-visual desync becomes discretely perceptible above **320 ms**, with the 160-320 ms range producing a qualitative "smearing" perception.

## Theoretical Impact on Entanglement
If $A(t)$ (Audio Synchronization) is high but $V(t)$ (Visual Synchronization) lags by >320ms, the Entanglement Index $E(t)$ will show a "false positive" for coordination—the performers might sound in sync, but they are not visually coupled, leading to a fragile state that is prone to collapse if the tempo changes.
