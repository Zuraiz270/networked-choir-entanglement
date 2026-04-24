---
title: Granger Influence Index
type: concept
alchemy_stage: citrinitas
tags: [metrics, causality, network_science]
ingested_date: 2026-04-23
source_count: 1
related: ["[[p_21_granger_representation_learning]]", "[[entanglement_index]]"]
---

# Granger Influence Index (GII)

The Granger Influence Index (GII) is a directed metric that quantifies the degree to which one node in a networked choir drives the behavior of another.

## Mathematical Basis
$GII_{A \to B}$ is the improvement in predicting the future of Node B's state ($S_B(t+1)$) when Node A's history ($S_A(t-k \dots t)$) is included in the model, compared to using only Node B's history.

## Interpretation
- **GII > 0:** Node A is a "Leader." Their timing and expression are being mimicked by Node B.
- **GII $\approx$ 0:** Nodes A and B are independent or merely following a common external signal (e.g., a metronome).

## Choral Application
We use GII to detect **Sub-Network Capture**. In high-latency conditions, a choir often fragments into small "islands of synchrony" where local influence is high but global entanglement is low. The GII allows the dashboard to visualize these hidden power structures.
