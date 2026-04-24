---
title: Symbolic Transmission
type: concept
alchemy_stage: citrinitas
tags: [nmp, protocols, midi, osc]
ingested_date: 2026-04-23
source_count: 1
related: ["[[p_06_symbolic_nmp_framework]]", "[[nmp_architecture]]"]
---

# Symbolic Transmission

Symbolic Transmission is an NMP strategy that sends "instructions" (MIDI/OSC) rather than "sound waves" (PCM/Opus).

## Comparison

| Feature | Audio Streaming | Symbolic Transmission |
| :--- | :--- | :--- |
| **Payload** | Waveform Samples | Note-On/Off, Velocity, Pitch |
| **Bandwidth** | High (>64 kbps) | Ultra-Low (<1 kbps) |
| **Synthesis** | Remote (at source) | Local (at destination) |
| **Flexibility** | Static Timbre | Real-time timbre morphing at edge |

## Implementation in SNA-OSN-M
While our project focuses on *analyzing* choral audio, symbolic transmission serves as the "Ground Truth" or "Control Signal" in our experimental tests. By comparing a MIDI-driven virtual choir with a human recording, we can isolate **Human Jitter** from **Network Jitter**.
