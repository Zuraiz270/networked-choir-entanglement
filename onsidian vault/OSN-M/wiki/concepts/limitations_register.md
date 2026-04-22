---
title: Limitations Register — auditable inventory of threats to H1–H3 and Gates A–D
type: concept
alchemy_stage: citrinitas
tags: [limitations, ebse, risks, gdpr, dsp, statistics, validation, project-8]
ingested_date: 2026-04-18
source_count: 3
related: ["[[Project_8_MOC]]", "[[entanglement_index]]", "[[data_sourcing_policy]]", "[[Janine_Hacker]]", "[[Peter_Gloor]]"]
team_take: Tree Huggers — documenting every failure mode in advance is the conscientious counterpart of claiming ambitious hypotheses. Transparent limitations + mitigations beat quiet hand-waving, always.
---

# Limitations Register

**Role**: Citrinitas synthesis page — the vault-graph surface for the auditable inventory of every DSP, statistical, legal, reproducibility, stakeholder, and integration limitation that can undermine Project 8. Body is canonical in `PROJECT_GUIDE.md` §12 (v1.0, 2026-04-18). This page links that canonical section into the Obsidian graph and carries the at-a-glance summary for LINT cycles.

**Owner**: Zuraiz (WP1).
**Review cadence**: each iteration-2+ status report; each §6 milestone gate.
**Canonical**: `PROJECT_GUIDE.md` §12.0–§12.10.

---

## 1. Totals

- **59** specified limitations across 8 categories (audio/DSP · CV · network-statistics · data-sourcing · legal/GDPR · reproducibility · stakeholder · integration).
- **43** Mitigated · **6** Escalated · **4** Open · **1** Accepted · **5** Resolved.
- **17** newly-surfaced beyond v1.0 PROJECT_GUIDE.md (★ items).

---

## 2. Categories — entry points

| Section | Canonical ref | Entries | Highest-impact IDs |
|:--|:--|:--|:--|
| Audio / DSP | `PROJECT_GUIDE.md` §12.1 | 10 | L-A-3 ★, L-A-4 ★, L-A-9 |
| Computer Vision | `PROJECT_GUIDE.md` §12.2 | 10 | L-B-3 ★, L-B-4 ★ |
| Network / Statistics | `PROJECT_GUIDE.md` §12.3 | 10 | L-C-5 ★, L-C-6, L-C-7 ★, L-C-8 ★ |
| Data Sourcing | `PROJECT_GUIDE.md` §12.4 | 8 | L-D-1, L-D-5 |
| Legal / GDPR | `PROJECT_GUIDE.md` §12.5 | 5 | L-E-1 ★, L-E-2, L-E-3 ★ |
| Project / Reproducibility | `PROJECT_GUIDE.md` §12.6 | 8 | L-F-5 ★ |
| Stakeholder | `PROJECT_GUIDE.md` §12.7 | 4 | L-G-2 ★ |
| Integration / Engineering | `PROJECT_GUIDE.md` §12.8 | 4 | L-H-1 ★ |

---

## 3. Pre-Apr-30 Watch List

Three items that must land before the 2026-04-30 14:00 CET Hacker + Gloor joint status meeting. Full criteria in `PROJECT_GUIDE.md` §12.9.

| # | ID | Title | Owner | Deadline |
|:--|:--|:--|:--|:--|
| W1 | L-D-1 | ~~Hacker URL list receipt or escalation~~ **RESOLVED** | Zuraiz | 2026-04-22 09:00 CET |
| W2 | L-F-5 | MediaPipe 0.10.14 × Py 3.11 × Win 11 smoke-test | Zuraiz | 2026-04-25 |
| W3 | L-G-2 | Apr 30 joint-deck draft | Zuraiz | 2026-04-25 (draft) · 2026-04-29 (rehearsal) |

---

## 4. Newly-surfaced (★) items — quick index

Items introduced on 2026-04-18, absent or materially under-specified in v1.0 `PROJECT_GUIDE.md`:

- **L-A-3** Cuesta 2020 multi-f0 per-voice accuracy unverified at scale — Escalated.
- **L-A-4** Virtual choirs are post-synchronised in production (editing artefact) — Mitigated.
- **L-A-10** Dagstuhl headset-mic cross-talk bleed — Mitigated.
- **L-B-3** MediaPipe validation covers limbs, not breath-frequency torso micro-sway — Escalated.
- **L-B-4** Mouth-aperture sync confounded by shared lyrics — Mitigated.
- **L-B-7** Lip-sync editing artefact (paired with L-A-4) — Mitigated.
- **L-B-10** Fake-composite "virtual choirs" (studio recording + visual comp) — Mitigated.
- **L-C-5** Cohen's d ≥ 0.5 target — formal power analysis drill-down — Mitigated.
- **L-C-7** 200-permutation null insufficient post-MHT — Mitigated (raise to 1000).
- **L-C-8** Multiple-hypothesis correction missing — Mitigated (Benjamini–Hochberg FDR).
- **L-D-4** SATB labels absent from YouTube metadata — Mitigated.
- **L-D-8** English-title filter biases cultural sample — Mitigated.
- **L-E-1** FaceMesh landmarks = biometric under GDPR Art. 9? — Escalated.
- **L-E-3** DPIA (Art. 35) not yet drafted — Mitigated.
- **L-F-4** Docker Desktop WSL2 GPU passthrough fragile on Win 11 — Mitigated.
- **L-F-5** MediaPipe 0.10.14 × Py 3.11 × Win 11 wheel not yet verified — Open.
- **L-F-8** Compute budget undisclosed (~30–50 GPU-h) — Mitigated.
- **L-G-2** Apr 30 joint-deck not started — Open.
- **L-H-1** Parquet schemas (WP2 → WP3) not specified — Open.
- **L-H-2** Dashboard live-demo feasibility (60 s claim) — Mitigated.

---

## 5. Escalated items — search-query packets

For the 6 Escalated entries, `PROJECT_GUIDE.md` §12 supplies the full 2-paragraph context plus 3 verbatim search queries each. Index:

- **L-A-3** (Cuesta multi-f0 accuracy) → §12.1
- **L-B-3** (MediaPipe breath-sway validity) → §12.2
- **L-D-1** (Hacker URL list) → §12.4 + §9 R1 cross-ref
- **L-D-5** (DUST dataset access) → §12.4
- **L-E-1** (FaceMesh biometric classification) → §12.5
- **L-E-2** (§60d UrhG foreign publication) → §12.5

---

## 6. Coverage against prior open questions

Every prior open question in the vault and in `PROJECT_GUIDE.md` §9 has been indexed — see `PROJECT_GUIDE.md` §12.0 Coverage-Completeness table. Exception: `entanglement_index.md` §7 Q1 (should `A_ens(t)` be reported alongside main E(t)?) is a **paper-drafting decision**, not a limitation, and is therefore out-of-register.

---

## Backlinks

- [[Project_8_MOC]] (Rubedo parent).
- [[entanglement_index]] — Open Questions §7 cross-ref L-B-1/L-B-3/L-C-1.
- [[data_sourcing_policy]] — Open Questions §9 cross-ref L-C-3/L-D-5/L-E-2.
- [[Janine_Hacker]] — empirical-rigor lens; Gate B scientific standards.
- [[Peter_Gloor]] — COINs / alchemical lens; Gate C stakeholder deliverable.
