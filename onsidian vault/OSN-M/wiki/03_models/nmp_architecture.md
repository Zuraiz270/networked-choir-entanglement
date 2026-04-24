---
title: NMP Architecture Models
type: concept
alchemy_stage: citrinitas
tags: [architecture, nmp, jamulus, soundjack]
ingested_date: 2026-04-23
source_count: 1
related: ["[[p_11_chamber_choir]]", "[[latency_thresholds]]"]
---

# Networked Music Performance (NMP) Architectures

Designing a successful NMP architecture requires moving away from the paradigms of standard videoconferencing tools (like Zoom or Teams) which are optimized for speech clarity and sequential talking, rather than synchronous multi-source audio.

## Architectural Tiers
Based on real-world deployments (e.g., [[p_11_chamber_choir]]), NMP systems generally fall into three tiers:

### Tier 1: The Conferencing Baseline (High Latency)
- **Tools**: Zoom, MS Teams, Google Meet.
- **Characteristics**: High latency (300-1000ms), heavy DSP (noise cancellation, echo suppression), speaker-highlighting.
- **Viability**: Completely unviable for synchronous ensemble performance. Used only for solo feedback or passive listening.

### Tier 2: The Distributed NMP (Medium Latency)
- **Tools**: Jamulus, SoundJack (home setups).
- **Characteristics**: Uncompressed or lightly compressed audio, ASIO/CoreAudio low-latency drivers, wired Ethernet connection. 
- **Latency**: 50-135ms.
- **Viability**: Allows for basic rhythmic synchronization, but fine tempo variations and visual conducting are often impossible without a metronome or piano backing track.

### Tier 3: The Local/Dedicated NMP (Low Latency + Video)
- **Tools**: Professional interfaces, dedicated LAN/WAN, low-latency video streams (e.g., custom Jitsi or WebRTC implementations).
- **Characteristics**: Sub-85ms audio latency, sub-100ms video latency for the conductor.
- **Viability**: Closest approximation to in-person rehearsal. Allows for *tutti a'cappella* singing and visual tempo control (rubato, fermatas).

## Asymmetric Deployment
A common pattern in amateur/university ensembles is the asymmetric or "gateway" architecture, where core members use a strict low-latency setup (Tier 2/3) while a one-way audio feed is bridged to a Tier 1 platform for passive listeners who lack the necessary hardware.
