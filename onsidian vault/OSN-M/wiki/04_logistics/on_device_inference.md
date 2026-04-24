---
title: On-Device Inference
type: concept
alchemy_stage: citrinitas
tags: [architecture, latency, edge_computing]
ingested_date: 2026-04-23
source_count: 1
related: ["[[p_03_blazepose_tracking]]", "[[symbolic_transmission]]"]
---

# On-Device Inference

On-Device Inference is a deployment strategy where machine learning models are executed directly on the user's local hardware (smartphone, laptop) rather than on a central server.

## Advantages in NMP
- **Zero Network Jitter for Extraction:** Pose estimation happens at the source. We don't need to send high-bandwidth RAW video to a server; we only send the lightweight 33-keypoint coordinates (30KB/s vs 5MB/s).
- **Privacy by Design:** Raw video never leaves the singer's device, adhering to strict GDPR/Fair-Use standards.
- **Battery Efficiency:** Models like BlazePose Lite are optimized for mobile NPU/GPU backends, allowing for hour-long rehearsal sessions without overheating.

## Role in SNA-OSN-M
By using on-device inference, we transform the "Networked Choir" into a **Distributed Sensor Network**. Each singer's node extracts their own synchrony features and only transmits the "Symbolic Motion" to the central dashboard, minimizing the impact of network congestion on the final $E(t)$ calculation.
