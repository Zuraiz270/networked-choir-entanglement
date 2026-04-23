# Migration to Master Prompt Architecture & Search Delegation

You are absolutely right. The current `onsidian vault` setup relies on an "alchemical" framework (Nigredo/Albedo/Citrinitas/Rubedo) that directly contradicts the strict directory architecture mandated in section 2 of `osn_master_prompt.md`.

To fully comply with your Master Prompt, we must purge the idiosyncratic folder structure and rebuild the canonical `osn-wiki/` architecture from scratch, driven exclusively by the new literature you will source.

## User Review Required

> [!WARNING]
> This plan will eventually **deprecate and replace** the current `onsidian vault/OSN-M/` directory. All concepts and entities currently stored there will be synthesized and rewritten into the flat and structured `osn-wiki/` outline defined below. 

Currently, I have curated the targeted search packets for you below. Please review these keywords. Once you approve, you can begin searching for and downloading the raw PDFs. After you provide the validated literature, we will execute the migration.

## Proposed Changes

### 1. Keyword Strategist — Search Packets

Here are the strict, targeted search queries designed to gather the modern (2024–2026) literature needed to rebuild our evidence matrix. Please use these on IEEE Xplore, ACM DL, and Google Scholar.

#### Packet 1: Networked Music Performance & Latency (H1 / Tier 3)
*Focus: Isolating audio coordination under extreme latency, specifically comparing Zoom-class to SoundJack-class limits.*
* **Queries:**
  * `"networked music performance" AND "packet loss" AND ("latency" OR "synchronization")` (filter: ≥ 2024)
  * `"online choir" AND "latency threshold" AND "coordination"` (filter: ≥ 2024)
  * `"SoundJack" OR "Jamulus" AND "music performance" AND "delay"` (filter: ≥ 2024)

#### Packet 2: Visual Entanglement & Honest Signals (H3 / Tier 1)
*Focus: Measuring non-verbal coordination (sway, breathing) using computer vision.*
* **Queries:**
  * `"pose estimation" AND "music ensemble" AND "synchronization"` (filter: ≥ 2024)
  * `"respiration rate" OR "breathing" AND "computer vision" AND "choir"` (filter: ≥ 2024)
  * `"MediaPipe" AND "kinematic" AND "music" AND "coordination"` (filter: ≥ 2024)

#### Packet 3: Network Science & Causality in Music (H2 / WP3)
*Focus: Modeling onset delays as a directed graph to show causality/influence.*
* **Queries:**
  * `"Granger causality" AND "music performance" AND "ensemble"` (filter: ≥ 2024)
  * `"network analysis" AND "musical coordination" AND "onset"` (filter: ≥ 2024)
  * `"transfer entropy" AND "synchronization" AND "music"` (filter: ≥ 2024)

#### Packet 4: Data Sourcing & GDPR (Legal/EBSE baseline)
*Focus: Defending the use of YouTube scraped data and biometric extraction.*
* **Queries:**
  * `"GDPR" AND "facial landmarks" AND "biometric"` (filter: ≥ 2024)
  * `"text and data mining" AND "copyright exception" AND "research"` (filter: ≥ 2024)

### 2. File Architecture Migration

When you have provided the PDFs in `raw/01_primary_sources/` and `raw/02_secondary_sources/`, we will spin up the exact mandatory structure:

#### [NEW] `osn-wiki/`
The new root folder for all knowledge, matching `osn_master_prompt.md`.

#### [NEW] `osn-wiki/index.md`
The master mapping document indexing all literature.

#### [NEW] `osn-wiki/wiki/`
We will populate the 7 mandatory categories:
* `00_overview/` (Glossary & High-level summary of the NMP/Choir problem)
* `01_project/` (Roadmaps, grades, timelines translated from PROJECT_GUIDE.md)
* `02_research_questions/` (H1, H2, H3 explicitly defined)
* `03_models/` (Separated into primary & secondary sources)
* `04_datasets/` (Tier 0, 1, 2, 3 data strategy, separated by source type)
* `05_metrics/` (The E(t) functional definition)
* `06_failure_modes/` (The Limitations register migrated here)

#### [MODIFY] `PROJECT_GUIDE.md`
Will be refreshed to reference the new paths and evidence matrix.

#### [DELETE] `onsidian vault/` (Deferred)
Once the migration is complete and we confirm zero data-loss, we will remove the old alchemical framework completely.

## Open Questions

1. Do these search packets cover the precise technical angles you want to research for the "Entanglement in Online Choirs" domain? 
2. Shall I create the empty folder skeleton for `osn-wiki/` now so you know exactly where to drop the PDFs?

## Verification Plan

1. You will download the PDFs and place them into the newly built `osn-wiki/raw/01_primary_sources/` and `02_secondary_sources/`.
2. I will read the directory to confirm acquisition.
3. We will then iterate through the papers to rebuild `PAPER_LINKS.md` and populate the `osn-wiki/wiki/` subfolders natively.
