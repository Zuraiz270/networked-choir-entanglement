---
title: Larynx Microphones (Throat Mics)
type: concept
alchemy_stage: citrinitas
tags: [hardware, f0, mir, choral]
ingested_date: 2026-04-23
source_count: 1
related: ["[[p_01_dagstuhl_choirset]]", "[[nmp_hardware_requirements]]"]
---

# Larynx Microphones (Throat Mics)

Larynx Microphones (LRX) are contact microphones attached to the skin of the throat. They detect the bio-acoustic vibrations of the vocal folds rather than the acoustic sound pressure waves in the air.

## Benefits for Research (DCS / P-01)
- **Zero Crosstalk:** Unlike headset or handheld mics, LRX does not pick up sound from other singers, even in loud, dense choir settings.
- **Clean F0 Trajectories:** Algorithms like CREPE or pYIN achieve much higher Raw Pitch Accuracy (RPA) on LRX signals because the fundamental frequency is physically isolated.
- **Privacy:** As they don't capture the vocal tract (articulation/vowels) clearly, they are less "identifiable" as speech, potentially aiding in GDPR-compliant audio research.

## Limitations
- **Poor Timbre:** They lack the high-frequency information needed for vowel recognition or aesthetic listening. They are purely "analysis" signals.

## Use in SNA-OSN-M
For our Tier 3 (Controlled Experiment) data, we will attempt to acquire LRX-style ground truth for pitch synchronization to compare against the noisier YouTube-mined $A(t)$ data.
