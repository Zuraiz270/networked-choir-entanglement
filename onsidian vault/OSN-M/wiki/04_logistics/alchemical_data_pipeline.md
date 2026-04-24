---
title: Alchemical Data Pipeline
type: concept
alchemy_stage: albedo
tags: [logistics, architecture, workflow]
ingested_date: 2026-04-23
source_count: 1
related: ["[[s_01_cybernetic_alchemy]]", "[[pose_standardization]]"]
---

# Alchemical Data Pipeline

The Alchemical Data Pipeline is the technical workflow used by the OSN-M platform to transform raw video/audio into actionable social insights.

## Visualization (The Magnum Opus)

```mermaid
graph TD
    subgraph Nigredo ["Nigredo (Blackness)"]
        A[Raw 5G Streams] --> B[YouTube Scraping]
        B --> C[MP4 Storage]
    end

    subgraph Albedo ["Albedo (Whiteness)"]
        C --> D[MediaPipe Extraction]
        D --> E[Multi-F0 Extraction]
        E --> F[Preprocessing/Scaling]
    end

    subgraph Citrinitas ["Citrinitas (Yellowness)"]
        F --> G[Granger Causality]
        G --> H[Ordinal Patterns]
        H --> I[E(t) Entanglement Index]
    end

    subgraph Rubedo ["Rubedo (Redness)"]
        I --> J[VR/XR Dashboard]
        J --> K[Directed Influence Graph]
        K --> L["'The Stone' (E=1.0)"]
    end

    style Nigredo fill:#333,stroke:#fff,color:#fff
    style Albedo fill:#fff,stroke:#333,color:#333
    style Citrinitas fill:#ffd700,stroke:#333,color:#333
    style Rubedo fill:#b22222,stroke:#fff,color:#fff
```

## Stages (The "Great Work")
- **Nigredo (Ingestion):** Capturing RAW 5G streams from performers (P-15).
- **Albedo (Refining):** Preprocessing MediaPipe data (P-20), normalizing pitch (P-02), and handling occlusions (P-03).
- **Citrinitas (Analysis):** Calculating Granger Influence (P-21) and Ordinal Patterns (P-22) to find the "Stone" (The Index).
- **Rubedo (Visualization):** Projecting the Entanglement Map back to the singers via the VR/XR interface (P-23/P-10).

## Objective
The goal is to reach **"The Stone" ($E=1.0$)**, where the network latency is perfectly masked by the collective entrainment of the performers.
