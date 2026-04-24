---
title: Attention Focus Shift
type: concept
alchemy_stage: citrinitas
tags: [perception, psychology, audio-visual]
ingested_date: 2026-04-23
source_count: 1
related: ["[[s_04_ar_latency_perception]]", "[[vocal_entrainment]]"]
---

# Attention Focus Shift

Attention Focus Shift is the psychological phenomenon where a performer redirects their cognitive resources from one sensory modality (e.g., Visual) to another (e.g., Audio) when the former becomes unreliable or distracting.

## In Networked Music
In low-latency conditions, performers utilize both **Ear Coupling** (audio) and **Eye Coupling** (visual cues, gestures) to synchronize. 

As network latency increases:
1. **The Distraction Phase (~320ms):** The visual animation lag becomes "noticeable" and starts to distract from the musical task.
2. **The Audio-Only Phase (>320ms):** The performer "tunes out" the visuals and relies almost exclusively on the audio stream to maintain rhythm.

## Significance for Dashboard Design
Our dashboard must visualize when this shift occurs. If $E_v$ (Visual Coupling) drops significantly but $E_a$ (Audio Coupling) remains stable, the "Entanglement" is still present but has moved to a purely auditory state.
