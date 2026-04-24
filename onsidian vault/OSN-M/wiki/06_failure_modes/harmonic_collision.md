---
title: Harmonic Collision
type: concept
alchemy_stage: citrinitas
tags: [failure_modes, acoustics, signal_masking]
ingested_date: 2026-04-23
source_count: 1
related: ["[[p_02_multi_f0_cnn]]", "[[pitch_salience_map]]"]
---

# Harmonic Collision

Harmonic Collision is a failure mode in multi-F0 estimation where the harmonics of one source (e.g., a Bass singer) overlap perfectly with the fundamental of another source (e.g., a Soprano singing an octave higher).

## Technical Impact
- **Salience Ambiguity:** The CNN may misattribute the energy of the Soprano's F0 to the 2nd harmonic of the Bass, leading to a "missing" voice in the transcription.
- **Phase Interference:** If the two singers are slightly out of phase, their overlapping partials can cancel each other out, leading to "holes" in the pitch salience map.

## Mitigation (P-02)
P-02 mitigates this using **Deep Learning Priors**. The model is trained on SATB structures and learns that if a Bass is present, certain harmonic patterns are "expected," allowing it to better separate colliding frequencies through its multi-layer feature hierarchy.
