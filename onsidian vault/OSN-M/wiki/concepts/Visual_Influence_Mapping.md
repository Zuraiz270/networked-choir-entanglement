---
title: Visual Influence Mapping
type: concept
alchemy_stage: citrinitas
tags: [metrics, computer-vision, influence, granger-causality]
ingested_date: 2026-04-23
source_count: 3
related: ["[[p_21_granger_representation_learning]]", "[[p_22_augmented_granger_causality]]", "[[granger_influence_index]]"]
team_take: "The visual counterpart to acoustic causality. This mapping allows us to see the 'silent leaders' in a choir section."
---

# Visual Influence Mapping

**Visual Influence Mapping** is the process of using computer vision (MediaPipe) and directed graph modeling to identify who is leading whom in a visual choral environment.

## Methodology
1. **Pose Extraction**: Extract trunk-sway and head-yaw time-series for every visible singer.
2. **Causality Testing**: Run Granger causality tests on the pose derivatives (velocity/acceleration) to check for time-lagged correlations.
3. **Graph Construction**: Create a directed graph where edges represent significant influence (X precedes Y).

## Significance
This mapping fulfills the stakeholder requirement from **[[Janine_Hacker]]** to visualize the topology of leadership and trust in virtual teams. It distinguishes between a "democratic" ensemble (dense, reciprocal links) and a "hierarchical" one (one-to-many links from a central node).

## Related
- [[p_21_granger_representation_learning]]
- [[p_22_augmented_granger_causality]]
- [[granger_influence_index]]
