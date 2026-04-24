---
title: NMP Hardware Requirements
type: concept
alchemy_stage: citrinitas
tags: [nmp, logistics, hardware]
ingested_date: 2026-04-23
source_count: 1
related: ["[[s_03_choirathome_tools]]", "[[latency_thresholds]]"]
---

# NMP Hardware Requirements

The success of a Networked Music Performance is fundamentally limited by the user's hardware chain. S-03 identifies three non-negotiable requirements for low-latency synchronization:

## 1. External Audio Interface
- **Purpose:** Bypasses the high-latency internal sound chips of PCs/Macs. Uses specialized drivers (ASIO/CoreAudio) to process audio in <10ms.
- **Fail Case:** Using a built-in laptop mic/speakers adds 50-200ms of "hidden" processing latency.

## 2. Ethernet (LAN) Connection
- **Purpose:** Eliminates "Jitter" (variation in delay). WiFi introduces unpredictable packet bursts that cause audio artifacts ("crackling") and break synchronization.
- **Fail Case:** High-speed WiFi is still unsuitable for NMP due to packet collision/interference.

## 3. Closed-Back Headphones
- **Purpose:** Prevents feedback loops. If audio from collaborators leaks from speakers into the performer's microphone, it creates a "feedback scream" or an infinite echo.
- **Fail Case:** Using open speakers makes real-time duplex communication impossible.
