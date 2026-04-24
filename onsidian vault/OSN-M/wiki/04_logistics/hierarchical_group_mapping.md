---
title: Hierarchical Group Mapping
type: concept
alchemy_stage: citrinitas
tags: [logistics, sda, choir_structure]
ingested_date: 2026-04-23
source_count: 1
related: ["[[p_21_granger_representation_learning]]", "[[pose_standardization]]"]
---

# Hierarchical Group Mapping

Hierarchical Group Mapping is the process of aggregating individual performer data into section-level metrics (e.g., Sopranos, Altos, Tenors, Basses).

## Technical Implementation (P-21)
Instead of simply averaging the pitch or pose of 4 singers to get a "Section Average," we use **MCCA (Multiset Canonical Correlation Analysis)**. This identifies the shared "Performance Signal" that defines the section's contribution to the ensemble, effectively filtering out individual errors or idiosyncratic movements.

## Benefits for OSN-M
- **Noise Reduction:** Reduces the impact of a single singer's network stutter on the group visualization.
- **Scalability:** The dashboard only needs to calculate 4x4 influence matrices (SATB) instead of NxN (Performer-to-Performer), significantly reducing computational overhead for large virtual choirs.
