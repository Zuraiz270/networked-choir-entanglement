---
title: Status Meeting III Outcome
type: synthesis
alchemy_stage: rubedo
tags: [seminar, status-meeting, decisions, dpia, publication-scope]
ingested_date: 2026-05-21
source_count: 1
related: ["[[Project_Overview]]", "[[data_sourcing_policy]]", "[[seminar_logistics]]", "[[Project_Phase_Roster]]"]
team_take: "DPIA dropped + paper scope reduced to semester report = Sprint 3 critical path simplified."
---

# Status Meeting III Outcome (2026-05-21)

Verbal post-meeting report from Kate, captured in `raw/status_meeting_3_notes.txt`.

## Headline

Both supervisors (Prof. Janine Hacker, Prof. Peter Gloor) satisfied with our presentation. Two consequential decisions came out of the Q&A that reshape Sprint 3 scope.

## Decision 1: DPIA / DPO sign-off NOT required

**Question asked** (slide 10): DPO sign-off pending, following up weekly until Jun-14 extraction deadline.

**Supervisor response**: We do not need DPO sign-off. YouTube videos are already publicly available. Legal status is a "gray area" but acceptable for our scope, which is a semester project with an internal seminar report, not an externally published research paper.

**Conditional**: if publication scope changes later (e.g., we decide to submit a peer-reviewed paper), DPIA becomes required again.

**Implication for Sprint 3**:
- WP4 "DPIA sign-off" deliverable is REMOVED from the critical path
- Tier-1 large-scale feature extraction on all 29 videos can proceed without waiting
- The arXiv jurisdiction question (logged in [[deep_read_audit]]) becomes moot

**Updates triggered**:
- [[data_sourcing_policy]] §2 amended
- Local docs (PROJECT_GUIDE.md, TEAM_BRIEF.md) updated

## Decision 2: MediaPipe calibration downgraded to "try and iterate"

**Question asked** (slide 10): MediaPipe pose accuracy on micro-sway unvalidated; Sprint-3 OpenPose comparison planned.

**Supervisor response**: Just try it. If it does not work, ask AI.

**Implication for Sprint 3**:
- The formal calibration study against OpenPose with Pearson-r ≥ 0.70 threshold downgrades to a lightweight empirical check
- We run MediaPipe on the 10 Tier-1 videos and assess output quality visually + numerically
- If results are noisy or wrong, we troubleshoot or substitute on the fly
- OpenPose fallback (originally tracked as Risk R3) becomes opt-in rather than mandatory

## Decision 3: Publication scope = semester report only

**Confirmed**: this is a semester project. Output is the internal seminar report, not a peer-reviewed paper.

**Out-of-scope items that drop**:
- DPIA / DPO sign-off (per Decision 1)
- arXiv jurisdiction question
- Publication-venue decisions (IEEE / LNCS / COINs / ISMIR / ACM CHI all unnecessary)
- DOI deposit and artifact evaluation badging

**In-scope items that remain**:
- Reproducibility hygiene (SHA-256 manifest, uv.lock, parquet schema) — still load-bearing for the report
- All 3 hypotheses (H1 latency, H2 topology, H3 visual signals) — still the report's claims
- Both flagship figures (Hacker's influence graph, Gloor's alchemical-stage diagram)
- Final 20-min presentation on Jul 23

## Items NOT addressed in the meeting

- Jul 23 final presentation logistics (in-person at Bamberg or remote on Zoom). Re-ask at Status Meeting IV (Jun 11).
- Specific Sprint-3 progress expectations beyond what we already proposed.
- Next-presenter rotation.

## Open Questions

- If we drop publication scope, does the reproducibility appendix still matter for the report grading? Probably yes (Hacker values rigor), but worth confirming.
- Does the team still want to keep paper-quality figure polish (Cytoscape SVG for July) given the lighter scope? Discuss with WP4 owner.
