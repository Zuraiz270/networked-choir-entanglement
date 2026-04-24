---
title: Non-Linear Causal Leakage
type: concept
alchemy_stage: citrinitas
tags: [failure_modes, causality, metrics]
ingested_date: 2026-04-23
source_count: 1
related: ["[[p_22_augmented_granger_causality]]", "[[granger_influence_index]]"]
---

# Non-Linear Causal Leakage

Non-Linear Causal Leakage is a failure mode in standard Network Analysis where influential nodes (Leaders) are missed because their influence is not expressed through direct linear correlation.

## The "Silent Leader" Problem
In a choir, a Lead Soprano might influence the ensemble's timing not by being "Louder" or "Earlier," but by the way she "Shapes" her vowels (P-22 logic). A linear Granger test ($GII$) will report 0 influence, leading to a false network map.

## Detection via OSPs
By augmenting the $GII$ with **Ordinal Patterns**, we can detect these "Silent Leaders."
- **Dashboard Warning:** "Non-linear Influence Detected: Section B is following Section A's phrasing pattern (OSP=0.85), despite low rhythmic correlation (GII=0.1)."
- **Strategic Value:** This ensures that our "Entanglement Index" captures the actual social hierarchy of the choir, not just the technical artifacts of the audio mix.
