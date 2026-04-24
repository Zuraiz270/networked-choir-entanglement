---
title: Intonation Cost (IC)
type: concept
alchemy_stage: citrinitas
tags: [metrics, intonation, f0, choral]
ingested_date: 2026-04-23
source_count: 1
related: ["[[p_01_dagstuhl_choirset]]", "[[entanglement_index]]"]
---

# Intonation Cost (IC)

Intonation Cost (IC) is a metric used to quantify the distance between an ensemble's local frequency content and an ideal 12-tone equal-tempered (12-TET) grid or a just-intonation scale.

## Calculation
1. Extract F0 and harmonic partials for each voice.
2. Compute a "grid-shift" parameter to account for global intonation drift.
3. Measure the remaining distance (error) for each singer.
4. Scale to a range of [0, 1].

## In Online Choirs
IC typically spikes during:
- **Chromatic Passages:** Where half-step movements are prone to over/under-shooting.
- **High-Latency Conditions:** Where performers cannot hear their partners' micro-intonation adjustments, leading to individual drift that isn't compensated for by the group.

## Impact on E(t)
A high IC in the absence of high latency suggests a failure of "Ear Coupling." A high IC *caused* by latency is a primary component of our Entanglement breakdown model.
