---
title: Ordinal Synchrony Pattern
type: concept
alchemy_stage: citrinitas
tags: [metrics, patterns, non_linear]
ingested_date: 2026-04-23
source_count: 1
related: ["[[p_22_augmented_granger_causality]]", "[[pitch_salience_map]]"]
---

# Ordinal Synchrony Pattern (OSP)

The Ordinal Synchrony Pattern (OSP) is a metric that measures the similarity between the "Shapes" of two performers' data trajectories, regardless of their absolute values.

## How it Works (P-22)
- **Shape Encoding:** If Performer A goes Up-Down-Up and Performer B also goes Up-Down-Up, they have high OSP, even if A is singing a C4 and B is singing a G4.
- **Pattern Buffering:** We use a "Reservoir" of 10-20 random shapes (e.g., Rising, Falling, Peak, Trough). We track how often the choir members "land" on the same shape simultaneously.

## Implementation in SNA-OSN-M
OSP is used to detect **Stylistic Cohesion**.
- **Classical Choir:** High OSP indicates disciplined ensemble phrasing.
- **Jazz/Gospel:** High OSP during "Ad-libs" reveals the underlying non-linear entrainment that allows singers to improvise together without a conductor.
- **Failure Mode:** Low OSP combined with high $P(t)$ (Pitch Synchrony) indicates "Mechanical Singing" where people are hitting the notes but missing the "Soul" or "Groove" of the ensemble.
