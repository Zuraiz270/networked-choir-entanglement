---
title: Breathing Desync
type: concept
alchemy_stage: citrinitas
tags: [failure_modes, choir, performance_errors]
ingested_date: 2026-04-23
source_count: 1
related: ["[[respiratory_synchrony]]", "[[p_16_structured_light_respiration]]"]
---

# Breathing Desync

Breathing Desync is a failure mode where singers fail to align their inhalation/exhalation cycles with the musical structure or with the rest of the ensemble.

## Visual Indicators
- **Staggered Chest Rise:** Visible in MoCap data as non-aligned peaks in the $Z$-axis of the torso.
- **Mouth-Breathing Mismatch:** Taking a breath in the middle of a word or phrase, detected by the AVSR system (P-05) as a break in the linguistic flow.

## Technical Cause
In NMP, breathing desync is often caused by **Visual Lag**. If a singer sees the conductor's "inhale" gesture 300ms late, their own inhalation will be late, causing a cascade of rhythmic errors in the subsequent vocal phrase.
