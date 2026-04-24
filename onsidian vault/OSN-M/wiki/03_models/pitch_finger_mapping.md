---
title: Pitch-Finger Mapping
type: concept
alchemy_stage: citrinitas
tags: [mocap, acoustics, geometry]
ingested_date: 2026-04-23
source_count: 1
related: ["[[p_18_audio_guided_mocap]]", "[[intonation_cost_ic]]"]
---

# Pitch-Finger Mapping

Pitch-Finger Mapping is the deterministic relationship between the frequency produced by a string instrument and the spatial location of the performer's finger on the string.

## Formula (P-18)
The fundamental relationship is:
$$P = \frac{F \cdot L_{fund}}{L_{vib}}$$
Where:
- $P$: Detected Pitch (Frequency).
- $F$: Fundamental Frequency of the open string.
- $L_{fund}$: Full length of the string (Nut to Bridge).
- $L_{vib}$: Vibrating Length (the distance from the bridge to the finger).

## Use Case in SNA-OSN-M
In a choral context, we adapt this to **Vocal Tract Mapping**. By analyzing the F0 and Formants ($F_1, F_2$), we can estimate the mouth aperture and tongue position. If the visual tracking (MediaPipe) shows a closed mouth while the audio shows a high-frequency vowel, we can trigger a **Modality Conflict** flag in $E(t)$.
