---
title: NMP on the Edge
type: concept
alchemy_stage: citrinitas
tags: [hardware, edge_computing, architecture, jacktrip]
ingested_date: 2026-04-23
source_count: 1
related: ["[[p_07_jacktrip_framework]]", "[[nmp_architecture]]"]
---

# NMP on the Edge

"NMP on the Edge" refers to the use of low-power, localized computing devices (e.g., Raspberry Pi, Jetson Nano) at the "edge" of the network to handle real-time audio/video processing, rather than relying on centralized cloud servers.

## Advantages
- **Latency Reduction:** Processing occurs at the user's location, eliminating the "Cloud Hop" (sending data to a server and back).
- **Sustainability:** Lower power consumption than high-end workstations.
- **Accessibility:** Enables professional-grade synchronization (sub-30ms) on inexpensive $50-$100 hardware.

## Implementation in JackTrip
JackTrip Virtual Studio uses a customized Linux kernel on a Raspberry Pi to achieve deterministic, low-jitter audio routing, making it the primary platform for high-entanglement research in underserved regions.
