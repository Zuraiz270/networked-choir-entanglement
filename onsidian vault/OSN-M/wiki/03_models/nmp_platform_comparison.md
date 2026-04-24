---
title: NMP Platform Comparison
type: concept
alchemy_stage: citrinitas
tags: [nmp, architecture, tools, topology, deep_read]
ingested_date: 2026-04-23
last_deep_read: 2026-04-23
source_count: 2
related: ["[[s_03_choirathome_tools]]", "[[nmp_architecture]]", "[[p_12_exploiting_latency]]"]
---

# NMP Platform Comparison

Selecting an NMP platform is a trade-off between **latency**, **audio quality**, **topology**, and **user complexity**. Different systems place the trade-off in different places.

## Peer-to-Peer (P2P) vs. Client-Server

### P2P (e.g., SoundJack)

- **Advantages**: Lowest possible latency (no intermediate server hop). Direct coupling between participants.
- **Disadvantages**: Network complexity (NAT traversal, port forwarding). Aggregate bandwidth grows with N² (each pair of participants carries a direct stream).
- **E(t) impact**: High entanglement potential for small groups (N < 5).

### Client-Server (e.g., Jamulus, JackTrip)

- **Advantages**: Simplified connection setup. Bandwidth scales linearly with N (each client talks only to server). Server can handle mixing and clock reference.
- **Disadvantages**: Added latency of the server hop. Centralized point of failure.
- **E(t) impact**: Better for large choirs (N > 10), but coupling is "conducted" through the server's master clock rather than emerging directly between participants.

### Hub-and-Spoke with FTA Scheduling (e.g., [[p_12_exploiting_latency]] prototype, NINJAM, GDC)

- **Topology**: Central server routes all messages, maintains a master clock, logs performance data, and arbitrates or rejects invalid actions [[p_12_exploiting_latency]] [p. 4, §4.1].
- **Scheduling**: System imposes a tempo and uses the [[fake_time_approach]] to schedule message execution at multiples of one musical cycle, with total delay ≥ Λ. Jitter is absorbed inside the scheduled slot rather than minimized [[p_12_exploiting_latency]] [p. 2, §2.2.1; p. 4, §4.2].
- **Default latency budget**: Λ = 3500 ms [[p_12_exploiting_latency]] [p. 4, §4.2]. Max tempo ≈ 68 BPM at default parameters [p. 5, §4.6.1].
- **Tradeoff**: Tolerates extreme multi-second latency at the cost of rigid tempo, cyclical-music-only domain, and audio onsets that reflect software quantization rather than human entrainment.
- **E(t) impact**: A(t) is misleading inside an FTA envelope; V(t) and N(t) are the informative channels.

## "Music Modes" (Zoom, Teams) vs. Dedicated NMP

"Music mode" features in Zoom or Teams are designed for one-way broadcasting (teaching, lessons, recitals). They do not solve the bidirectional synchronization problem required for ensemble performance. They remain in the codec-optimization regime and do not address NMP's core constraint: end-to-end latency is bounded below by network physics, not by codec efficiency.

## Implications for Project 8

Project 8's three data tiers map onto three different NMP regimes:

- **Tier 1** (curated YouTube): post-hoc rendered content. Neither P2P, C/S, nor FTA is directly present; videos are stitched or rendered after the fact. Not a live-NMP regime.
- **Tier 2** (Jamulus, SoundJack multitrack): client-server and P2P low-latency regimes. A(t), V(t), N(t) are all physically meaningful; audio onsets reflect genuine human timing.
- **Tier 3** (controlled latency injection): synthetic manipulation of Tier-2 streams to map the coupling decay curve. FTA is not in use here; jitter and latency are directly measurable.

The [[p_12_exploiting_latency]] hub-and-spoke + FTA regime is not part of Project 8's experimental tiers. It is cited only as a boundary-condition reference.
