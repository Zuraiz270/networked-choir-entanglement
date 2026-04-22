---
title: Project 8 — Networked Choir Entanglement Platform (Map of Content)
type: synthesis
alchemy_stage: rubedo
tags: [project-8, entanglement, choir, moc, coins-2026, tree-huggers]
ingested_date: 2026-04-17
source_count: 3
related: ["[[Project_Overview]]", "[[Project_Phase_Roster]]", "[[Team_Profile]]", "[[Janine_Hacker]]", "[[Peter_Gloor]]", "[[Kumaran_Vasu]]", "[[entanglement_index]]", "[[data_sourcing_policy]]", "[[hacker_tier0_reply]]"]
team_take: Tree Huggers' conscientious stance directly shapes §5 policy — no human subjects, no self-recording, GDPR-by-default, public artefacts only.
---

# Project 8 — Networked Choir Entanglement Platform (MOC)

**Role**: Rubedo **map-of-content** for the Tree Huggers + Kumaran project-phase deliverable. This is the single wiki entry point for anything concerning Project 8. All other Project-8 pages backlink here.

**Project**: *"Entanglement in Online Choir"* — measuring multi-modal coordination in distributed choirs under Zoom-class vs SoundJack-class latency regimes.

**Team**: [[Team_Profile]] (Zuraiz · Hammad Anwar · Hassan Ahmed · [[Kumaran_Vasu]]).
**Supervisor**: [[Janine_Hacker]] (Uni Bamberg · Chair of IS / Social Networks).
**Second grader**: [[Peter_Gloor]] (Uni Köln / ex-MIT · COINs · Cybernetic Alchemy).
**Scope**: 24 ECTS (6 × 4). **Target**: A+. **Final**: 2026-07-17.
**Canonical team guide**: `PROJECT_GUIDE.md` at repo root — v1.0, dated 2026-04-18 (supersedes v2.1 `implementation_plan.md`, now retired; all technical reference material preserved in `PROJECT_GUIDE.md` §11 Appendix).

> **Start here** → `PROJECT_GUIDE.md`. Team-facing master document; sections 1–10 are readable by any teammate in one sitting (~20 min); §11 is the technical appendix (formulas, EBSE evidence trails, pinned versions).

---

## The scientific question

Do online choirs exhibit **measurable multi-modal entanglement** — coupled acoustic, visual, and social-network signals — and does this coupling discriminate between **Zoom-class** (150–400 ms RTT) and **SoundJack-class** (20–60 ms RTT) regimes?

## The three hypotheses (tier-mapped, v2.1)

- **H1** — `[[entanglement_index]]` E(t) discriminates regimes at Cohen's d ≥ 0.5 on ≥ 2 sub-components. **Tested on Tier 3** (controlled latency injection on Tier 2 multitrack; paired within-piece design).
- **H2** — Granger-causal directed onset-graph topology (density, modularity, Burt's constraint) differs across regimes at p<0.05 vs 200-permutation null. **Tested on Tier 2 + Tier 3** (per-singer streams required).
- **H3** — Honest Signals (trunk-sway + breath synchrony, Pentland 2008) contribute ΔR² ≥ 0.10 to E(t) beyond audio-DTW alignment (hierarchical regression). **Tested on Tier 1 visual (N = 20 to 30, hand-curated, v2.2 scope cut 2026-04-19) + Tier 2 audio ground truth**.

See `PROJECT_GUIDE.md` §5 for where-we-need-to-be (artefacts + hypothesis claims) and §11.1–§11.2 for the full formula decomposition + tier-gated feature catalog.

## The four work packages

| WP | Pillar | Core artefact |
|:---|:---|:---|
| **WP1** | Audio ML · Integration · Paper | `choir_entanglement/{ingest,audio,latency_injection,integration}` + [[entanglement_index]] |
| **WP2** | Computer Vision | `choir_entanglement/video/` · MediaPipe Pose + FaceMesh |
| **WP3** | Network Science (Hacker pillar) | `choir_entanglement/network/` · Granger digraph + centrality + null model |
| **WP4** | Rubedo (Gloor pillar) | FastAPI + React dashboard · Honest-Signals alchemical diagram |

**Dataset under v2.2 (2026-04-19):** Tier 1 is 20 to 30 hand-curated videos (no post-produced content); latency claims (H1, H2) come from Tier 2 multitrack plus Tier 3 controlled latency injection only. E(t) weights frozen at (1/3, 1/3, 1/3).

Full WP descriptions and stack per WP: see `PROJECT_GUIDE.md` §7.

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

| Date | Deliverable |
|:---|:---|
| **2026-04-17** | Hacker URL email sent · repo scaffold commit · this MOC |
| **2026-04-18** | Cybernetic Alchemy PDF ingested → 4 wiki pages |
| **2026-04-22** | Tier-0 URL list received (3 hrs early, 5 URLs) |
| **2026-04-24** | Iteration-2 report to Hacker |
| **2026-04-30 14:00 CET** | **Hacker+Gloor status meeting · 5–10 min deck** |
| 2026-05-08 | Audio pipeline MVP (A1–A5) on Dagstuhl |
| 2026-07-17 | **Final 20-min presentation** |

Full timeline: `PROJECT_GUIDE.md` §6.

## Evaluation gates (all four must pass)

- **A — Methodological**: EBSE evidence trail on top-5 decisions · Dockerised `make reproduce` on fresh machine · BagIt validation.
- **B — Scientific**: Cohen's d ≥ 0.5 on ≥ 2 sub-indices · null-model |z| > 2 on ≥ 1 network metric · ≥ 1 honest negative result.
- **C — Stakeholder**: 1 Hacker deliverable (directed influence graph) + 1 Gloor deliverable (alchemical HS diagram).
- **D — Aesthetic**: 60 s dashboard demo · paper satisfies both professors.

## Open Questions

1. DUST packet-loss dataset — access verification by 2026-04-24.
2. Cuesta 2020 multi-f0 SATB model — install friction (R10); tier-1 stretch only.

## Closed

1. ~~Does [[Janine_Hacker]] have a canonical Tier-0 YouTube URL list?~~ **YES** — received 2026-04-22. See [[hacker_tier0_reply]]. W1 (L-D-1) **RESOLVED**.

## Risks

See `PROJECT_GUIDE.md` §9 for the top-7 risks in plain language. Highest-impact: R1 Tier-0 URL list absent · R6 paper bottleneck. R4 audio runtime risk was downgraded from MED to LOW under v2.2 (20 to 30 videos, not 150). Additional risks (R8–R10: scope creep · Tier-2 corpus too small · Cuesta 2020 install friction) retained in `PROJECT_GUIDE.md` context where relevant.

**Full audit**: `PROJECT_GUIDE.md` §12 *Limitations Register* (added 2026-04-18) — 59 specified entries across audio/DSP · CV · network-statistics · data sourcing · legal/GDPR · reproducibility · stakeholder · integration; 17 newly-surfaced beyond v1.0 (★ items including L-A-4 post-synchronisation, L-B-4 mouth-aperture lyric confound, L-C-5/C-7/C-8 statistical-power + MHT, L-E-1 FaceMesh biometric, L-E-3 DPIA). Pre-Apr-30 watch-list (§12.9): W1 Hacker URL list (L-D-1) · W2 MediaPipe wheel smoke-test (L-F-5) · W3 Apr 30 deck draft (L-G-2). Vault-graph surface: [[limitations_register]].

## Backlinks

- Up: [[Project_Overview]] (seminar-level synthesis).
- Cohort context: [[Project_Phase_Roster]] (our topic in the 10-topic cohort map).
- Team: [[Team_Profile]] · [[Kumaran_Vasu]].
- Stakeholders: [[Janine_Hacker]] · [[Peter_Gloor]].
- Canonical team guide: see `PROJECT_GUIDE.md` at repository root (v1.0, 2026-04-18; replaced the earlier v2.1 `implementation_plan.md` — technical content preserved in §11 Appendix).
