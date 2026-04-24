---
title: Hanging Note Inference
type: concept
alchemy_stage: citrinitas
tags: [failure_modes, error_correction, midi]
ingested_date: 2026-04-23
source_count: 1
related: ["[[p_06_symbolic_nmp_framework]]", "[[latency_spikes_burst_errors]]"]
---

# Hanging Note Inference

"Hanging Notes" (or Stuck Notes) are a specific failure mode of symbolic transmission where a `Note-On` packet is received, but the corresponding `Note-Off` is lost due to network packet loss.

## Mitigation Strategy (P-06)
1. **Timeout Handlers:** Each active synth instance is assigned a maximum duration $\Delta t_{max}$. If no `Note-Off` is received within this window, the note is automatically released.
2. **State Dictionaries:** The synthesis server maintains a mapping of all active notes. A new `Note-On` for the same pitch can trigger a "Clean Up" of the previous orphaned note.
3. **Redundancy:** Symbolic streams are so small that the system can send each MIDI event multiple times (Forward Error Correction) without significant bandwidth impact.

## Role in E(t)
Hanging notes disrupt the **Musical Structure Index $M(t)$**. If a singer's voice "drones" indefinitely due to a network glitch, the group's entanglement score should reflect this structural breakdown.
