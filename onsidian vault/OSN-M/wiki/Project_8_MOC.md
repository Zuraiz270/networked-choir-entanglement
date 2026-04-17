---
title: Project 8 — Networked Choir Entanglement Platform (Map of Content)
type: synthesis
alchemy_stage: rubedo
tags: [project-8, entanglement, choir, moc, coins-2026, tree-huggers]
ingested_date: 2026-04-17
source_count: 2
related: ["[[Project_Overview]]", "[[Project_Phase_Roster]]", "[[Team_Profile]]", "[[Janine_Hacker]]", "[[Peter_Gloor]]", "[[Kumaran_Vasu]]", "[[entanglement_index]]", "[[data_sourcing_policy]]"]
team_take: Tree Huggers' conscientious stance directly shapes §5 policy — no human subjects, no self-recording, GDPR-by-default, public artefacts only.
---

# Project 8 — Networked Choir Entanglement Platform (MOC)

**Role**: Rubedo **map-of-content** for the Tree Huggers + Kumaran project-phase deliverable. This is the single wiki entry point for anything concerning Project 8. All other Project-8 pages backlink here.

**Project**: *"Entanglement in Online Choir"* — measuring multi-modal coordination in distributed choirs under Zoom-class vs SoundJack-class latency regimes.

**Team**: [[Team_Profile]] (Zuraiz · Hammad Anwar · Hassan Ahmed · [[Kumaran_Vasu]]).
**Supervisor**: [[Janine_Hacker]] (Uni Bamberg · Chair of IS / Social Networks).
**Second grader**: [[Peter_Gloor]] (Uni Köln / ex-MIT · COINs · Cybernetic Alchemy).
**Scope**: 24 ECTS (6 × 4). **Target**: A+. **Final**: 2026-07-17.
**Canonical plan**: `implementation_plan.md` at repo root — v2.1, dated 2026-04-17.

---

## The scientific question

Do online choirs exhibit **measurable multi-modal entanglement** — coupled acoustic, visual, and social-network signals — and does this coupling discriminate between **Zoom-class** (150–400 ms RTT) and **SoundJack-class** (20–60 ms RTT) regimes?

## The three hypotheses (tier-mapped, v2.1)

- **H1** — `[[entanglement_index]]` E(t) discriminates regimes at Cohen's d ≥ 0.5 on ≥ 2 sub-components. **Tested on Tier 3** (controlled latency injection on Tier 2 multitrack; paired within-piece design).
- **H2** — Granger-causal directed onset-graph topology (density, modularity, Burt's constraint) differs across regimes at p<0.05 vs 200-permutation null. **Tested on Tier 2 + Tier 3** (per-singer streams required).
- **H3** — Honest Signals (trunk-sway + breath synchrony, Pentland 2008) contribute ΔR² ≥ 0.10 to E(t) beyond audio-DTW alignment (hierarchical regression). **Tested on Tier 1 visual (N=150) + Tier 2 audio ground truth**.

See `implementation_plan.md` §1 for the full four-level goal tree (L1 research · L2 technical · L3 academic · L4 process).

## The four work packages

| WP | Owner | Pillar | Core artefact |
|:---|:---|:---|:---|
| **WP1** | Zuraiz (PI) | Audio ML · Integration · Paper | `choir_entanglement/{ingest,audio,latency_injection,integration}` + [[entanglement_index]] |
| **WP2** | [[Kumaran_Vasu]] | Computer Vision | `choir_entanglement/video/` · MediaPipe Pose + FaceMesh |
| **WP3** | Hammad Anwar | Network Science (Hacker pillar) | `choir_entanglement/network/` · Granger digraph + centrality + null model |
| **WP4** | Hassan Ahmed | Rubedo (Gloor pillar) | FastAPI + React dashboard · Honest-Signals alchemical diagram |

Cross-reference [[Team_Profile]] for SocialCompass archetypes (Capybara Hammad · Ant Hassan · Kumaran onboarding) and the rationale for matching people to pillars.

## Alchemical pipeline mapping

| Stage | Repo/vault dir | Pipeline action | Artefact class |
|:---|:---|:---|:---|
| **Nigredo** | `raw/youtube/<video_id>/` · `wiki/sources/` | yt-dlp + license capture | `.mp4` · `info.json` · `sha256.txt` |
| **Albedo** | `processed/<video_id>/` · `wiki/entities/` | Demucs stems · MediaPipe keypoints | `stems/*.wav` · `pose/*.parquet` |
| **Citrinitas** | `features/<video_id>.parquet` · `wiki/concepts/` | feature extraction + E(t) synthesis | [[entanglement_index]] · `*.parquet` |
| **Rubedo** | `results/` · `wiki/` root | paper + dashboard | `paper.pdf` · dashboard bundle |

This mirrors the vault schema in [`../CLAUDE.md`](../CLAUDE.md) §3.

## Key concept pages

- [[entanglement_index]] — operational definition of E(t) = (1/3)·A(t) + (1/3)·V(t) + (1/3)·N(t) · null-model z-scoring · DSP reality check.
- [[data_sourcing_policy]] — three-tier dataset strategy · legal basis (§60d UrhG · EU DSM Art. 3 · GDPR Art. 6+89) · prohibited practices.
- [[socialcompass_tools]] — team archetypes informing WP assignment.

## Immediate milestones (v2.1)

| Date | Deliverable | Owner |
|:---|:---|:---|
| **2026-04-17** | Hacker URL email sent · repo scaffold commit · this MOC | Zuraiz |
| **2026-04-18** | Cybernetic Alchemy PDF ingested → 4 wiki pages | Zuraiz |
| **2026-04-21** | Tier-0 URL list received **or** escalation | Zuraiz |
| **2026-04-24** | Iteration-2 report to Hacker | Zuraiz |
| **2026-04-30 14:00 CET** | **Hacker+Gloor status meeting · 5–10 min deck** | Zuraiz (presenter) |
| 2026-05-08 | Audio pipeline MVP (A1–A5) on Dagstuhl | Zuraiz |
| 2026-07-17 | **Final 20-min presentation** | all |

Full timeline: `implementation_plan.md` §7.

## Evaluation gates (all four must pass)

- **A — Methodological**: EBSE evidence trail on top-5 decisions · Dockerised `make reproduce` on fresh machine · BagIt validation.
- **B — Scientific**: Cohen's d ≥ 0.5 on ≥ 2 sub-indices · null-model |z| > 2 on ≥ 1 network metric · ≥ 1 honest negative result.
- **C — Stakeholder**: 1 Hacker deliverable (directed influence graph) + 1 Gloor deliverable (alchemical HS diagram).
- **D — Aesthetic**: 60 s dashboard demo · paper satisfies both professors.

## Open Questions

1. Does [[Janine_Hacker]] have a canonical Tier-0 YouTube URL list? — email sent 2026-04-17; go/no-go 2026-04-22 09:00 CET.
2. Will [[Kumaran_Vasu]] complete his SocialCompass backfill before 2026-05-01 onboarding-plan deadline?
3. DUST packet-loss dataset — access verification by 2026-04-24.
4. Cuesta 2020 multi-f0 SATB model — install friction (R10); tier-1 stretch only.

## Risks

See `implementation_plan.md` §10 for the full R1–R10 register. Highest-impact (I=H): R1 Tier-0 URL list absent · R4 audio pipeline >12 h on 150 videos · R7 paper bottleneck · R9 Tier-2 corpus too small for H1 statistical power.

## Backlinks

- Up: [[Project_Overview]] (seminar-level synthesis).
- Cohort context: [[Project_Phase_Roster]] (our topic in the 10-topic cohort map).
- Team: [[Team_Profile]] · [[Kumaran_Vasu]].
- Stakeholders: [[Janine_Hacker]] · [[Peter_Gloor]].
- Canonical plan: see `implementation_plan.md` at repository root (not a wiki page — too large; v2.1 authored 2026-04-17).
