---
title: Pitch Salience Map
type: concept
alchemy_stage: citrinitas
tags: [audio_processing, visualization, metrics]
ingested_date: 2026-04-23
source_count: 1
related: ["[[p_02_multi_f0_cnn]]", "[[vocal_entrainment]]"]
---

# Pitch Salience Map

A Pitch Salience Map is a time-frequency representation where each bin represents the probability (or energy) of a specific fundamental frequency (F0) being present.

## Construction (P-02)
- **HCQT Basis:** The map is built by summing harmonic energy across multiple octaves, centered on the fundamental.
- **Phase Refinement:** Phase differentials are used to "sharpen" the peaks, moving beyond the coarse resolution of standard STFT bins.

## Use in Entanglement
In our platform, we visualize the **Collective Salience Map**.
- **Cohesion:** If the salience peaks of all singers overlap perfectly at the target pitch, the map shows a single, bright "entanglement line."
- **Friction:** If singers are out of tune or out of sync, the map shows "blurred" or "split" peaks, indicating a breakdown in auditory entanglement.
