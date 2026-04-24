---
title: Latency Spikes and Burst Errors
type: concept
alchemy_stage: citrinitas
tags: [failure_modes, latency, reliability, 5g]
ingested_date: 2026-04-23
source_count: 1
related: ["[[p_15_5g_iomt_analysis]]", "[[audio_visual_mismatch]]"]
---

# Latency Spikes and Burst Errors

Latency Spikes and Burst Errors are the two primary "hidden" failure modes in high-speed networks like 5G that disrupt musical synchronization.

## 1. Latency Spikes
Sudden, irregular increases in one-way delay (e.g., jumping from 20ms to 80ms). 
- **Cause:** Resource scheduling conflicts or Core Network interrogations.
- **Impact:** Causes "jitter" that forces the jitter buffer to drop packets, leading to audio glitches even if the average latency is low.

## 2. Burst Errors
The loss of many consecutive packets in a single time window.
- **Cause:** Temporary radio interference or physical obstruction (e.g., someone walking between the antenna and the performer).
- **Impact:** A burst of > 100ms (approx. 75 packets) is perceived as a "dropout" or "silence" that breaks the performer's sense of group flow, often leading to a restart of the musical phrase.

## Detection in E(t)
$E(t)$ must include a **Stability Penalty**. A session with 25ms average latency but 100ms spikes should have a lower entanglement score than a session with a constant 35ms latency.
