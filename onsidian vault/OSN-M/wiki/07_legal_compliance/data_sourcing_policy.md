---
title: Data Sourcing Policy
type: synthesis
alchemy_stage: rubedo
tags: [policy, legal, gdpr, tdm, youtube]
ingested_date: 2026-04-23
source_count: 3
related: ["[[p_17_copyright_tdm]]", "[[fair_use_tdm]]", "[[lawful_access_prerequisite]]"]
team_take: "Our shield against legal and ethical risk. By following §60d UrhG and Art. 9(2)(j) GDPR, we ensure our research is academically defensible."
---

# Data Sourcing Policy

This document defines the strict legal and ethical boundaries for acquiring and processing choir data for the SNA-OSN-M project.

## 1. Copyright & TDM (§60d UrhG)
Under German Law (§60d UrhG) and EU Directive 2019/790 (Art. 3), we have the right to perform Text and Data Mining on lawfully accessible sources (YouTube, academic repos) for non-commercial research.
- **Rule**: We do not redistribute raw media.
- **Rule**: We delete mp4 files after feature extraction.

## 2. Privacy & GDPR (Art. 9)
Biometric data (FaceMesh landmarks) is processed under the **Research Exception (Art. 9(2)(j) GDPR)** and **Art. 89 safeguards**.
- **Anonymization**: Extracted landmarks are pseudonymized and aggregate.
- **DPIA**: A Data Protection Impact Assessment was originally planned. Per Status Meeting III (2026-05-21, see [[status_meeting_3_outcome]]), supervisors confirmed that DPIA / DPO sign-off is NOT required for the semester-project scope (publicly accessible YouTube videos, internal seminar report, no peer-reviewed paper). If publication scope changes later, DPIA becomes required again.

## 3. Tiered Data Strategy
- **Tier 1**: Public YouTube (Descriptive visual).
- **Tier 2**: Academic Multitrack (Ground truth).
- **Tier 3**: Controlled Latency Injection (Falsification test bed).

## Related
- [[p_17_copyright_tdm]]
- [[fair_use_tdm]]
- [[lawful_access_prerequisite]]
