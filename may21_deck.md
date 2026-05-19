# May 21 Status Meeting III, Deck

**Project 8 · Entanglement in Online Choir · 2026-05-21 · 14:00 CET**

> Format: 7 slides for a 10-minute presentation (target 9 minutes spoken), per the May-14 email from Janine/Simon/Peter. Email rubric covered: goals + plan recap (slide 2), last-iteration progress (slide 3), next-iteration plan (slide 4), retrospective (slide 5), virtual mirror (slide 6), problems/questions (slide 7). Speaker notes live in [may21_script.md](may21_script.md). The Q&A prep bank is in [may21_qa_prep.md](may21_qa_prep.md).

---

## Slide 1: Title

**Status Meeting III**

Project 8: Entanglement in Online Choir

SNA-OSN-M Summer 2026 · Uni Bamberg × Uni Köln × HSLU

Presented by Zuraiz, on behalf of the team

Supervisors: Prof. Janine Hacker (Uni Bamberg), Prof. Peter Gloor (MIT/Köln)
Coordinators: Janine, Simon, Peter

---

## Slide 2: Recap — Goals and Plan

**Visual**: split layout. Left: research question one-liner + E(t) formula sketch. Right: 3-phase timeline strip from Apr 16 to Jul 31, with VS#3 marker.

**Research question**: When a choir sings together over the internet, can we put a number on how well coordinated they are?

**E(t)** — composite Entanglement Index combining:

- **A(t)** audio synchrony (pitch + onset alignment)
- **V(t)** visual coupling (body sway + mouth opening, MediaPipe)
- **N(t)** network topology (Granger-causal "who leads whom")

**Three hypotheses (unchanged since Apr 30)**:

1. H1: low-latency tools (Jamulus, SoundJack) score higher on E(t) than high-latency (Zoom).
2. H2: influence-network topology shifts from democratic to leader-dominated as latency rises.
3. H3: visual signals add ≥10 percentage points of explained variance over audio alone.

**Plan recap**: 3 phases — Scope (done, Apr 16-30), Build (May 1-Jul 7, **we are here**), Synthesise (Jul 8-31).

---

## Slide 3: Last Iteration — What Shipped, What Slipped

**Visual**: tabular shipped list with four inline figures from `data/figures/`:
- `wp1_satb_coupling.png` (Sprint 2 audio)
- `wp2_visual_features.png` (Sprint 2 video)
- `wp3_influence_graph.png` (Hacker flagship, draft)
- `wp4_alchemical_stages.png` (Gloor flagship, draft)

**Sprint 2 window**: Apr 30 → May 21 (3 weeks).

**Shipped ✓ across all four work packages**:

| Item | Status |
|:---|:---|
| Tier-2 Dagstuhl ChoirSet on disk (5.1 GB, MD5 `82b95faa…` verified against Zenodo) | ✓ done 2026-05-17 |
| Tier-1 YouTube corpus validated (N=29, includes 4 Hacker Tier-0 seeds re-confirmed; Zoom-only stratum supplemented from 2 to 9 via Perplexity + yt-dlp search) | ✓ done 2026-05-19 |
| WP1 audio: pipeline end-to-end on Quartet A Take 02 (SATB, 143 s, 4 singers); pairwise A(t) coupling 0.72-0.77 between adjacent voices | ✓ done 2026-05-17 |
| WP2 video: MediaPipe Pose + FaceMesh + derived features extracted from a Tier-1 SoundJack rehearsal (595 frames, 79.5% pose detection); calibration note at `wp2_calibration_sprint2.md` | ✓ done 2026-05-17 |
| WP3 network: Granger influence graph on Dagstuhl SATB; 11/12 directed edges significant at p_null < 0.05, density 0.92, Soprano most-central. First draft of Hacker's flagship figure | ✓ done 2026-05-17 |
| WP4 dashboard: wireframe + design doc at `frontend/wireframe.md`; first draft of Gloor's alchemical-stage flagship figure | ✓ done 2026-05-17 |
| Smoke tests: 15/15 pass (WP1 audio 4, WP2 video 4, WP3 network 4, scaffold canary 3); ruff clean; mypy strict clean | ✓ done 2026-05-17 |
| DPIA outline filed with Bamberg DPO | ✓ done 2026-05-21 |

**Slipped ⚠**:

| Item | Original | New | Why |
|:---|:---|:---|:---|
| Tier-2 dataset on disk | May 1 | May 17 | Slow bandwidth on 5.1 GB Zenodo fetch; required resume + retry |
| Audio pipeline first run | May 8 | May 17 | Blocked on Tier-2 download |
| Corpus curation | May 15 | May 17 | Sequenced after the audio pipeline to validate the legal-extraction loop first |

**The honest story**: Sprint-2 intermediate dates slipped 9-17 days but all milestones landed before May 21. WP2/3/4 deliverables originally scheduled for May 22 / May 31 were brought forward and shipped in draft form so this presentation has cross-WP coverage rather than only audio.

---

## Slide 4: Plan for the Next Iteration

**Visual**: 4-row table with phase colour stripe on the left, matching Apr 30 deck slide 6.

**Sprint 3: May 21 → Jun 11 (3 weeks, ending at VS#4)**

| Work Package | Next Step | Output | Due |
|:---|:---|:---|:---|
| **WP1 Audio** | Scale pipeline from 1 piece to all Dagstuhl pieces. Compute A(t) per piece, store as parquet. | A(t) feature parquet for 100% of Dagstuhl multitrack pieces | Jun 4 |
| **WP2 Video** | Run MediaPipe Pose + FaceMesh on first 10 Tier-1 YouTube videos. 1-page calibration note. | Per-singer pose parquet × 10 videos | Jun 11 |
| **WP3 Network** | Granger-causal influence graph on 5 Dagstuhl pieces. Standard GC + COP-GC variants. | Directed influence graph × 5 pieces | Jun 11 |
| **WP4 Legal/DPIA** | Convert DPIA outline to full document; Bamberg DPO sign-off before Jun-14 large-scale extraction. | Signed DPIA | Jun 11 |

**Critical-path notes**:

- Tier-3 (controlled latency injection) starts Jun 14 after WP1 + WP3 land.
- Per Apr-17 DSP-blocker finding, Tier-1 YouTube remains visual-only; no per-singer audio features will be attempted on mixed-stereo.

---

## Slide 5: Retrospective Output

**Visual**: 3-column "started / stopped / continued" board, populated from T5 retro call.

**Sprint 2 retrospective (held {DATE}, attendees: Zuraiz, Hammad, Hassan, Kumaran)**

**What worked**:

- {bullet from retro}
- {bullet from retro}

**What slipped and why**:

- {bullet from retro — root cause, not symptom}
- {bullet from retro}

**One process change for Sprint 3**:

- {single concrete change the team agreed on}

---

## Slide 6: Virtual Mirror Results

**Visual**: 2-up panel. Left: SocialCompass archetype bar chart for our team. Right: a network diagram of WhatsApp message flow.

**Method**: Team WhatsApp group exported {DATE}. Fed through SC Chat Analyzer + Symbiont per the introductory block course protocol.

**Findings (placeholder until T7 runs)**:

- **Team archetype**: {Bees / Ants / Butterflies / Capybaras / Leeches}
- **Communication topology**: {dense-democratic / star / fragmented}
- **Top contributors**: {names + message counts}
- **Reciprocity index**: {value}

**Interpretation**: {1-2 sentences on what this means for our own COIN dynamics, and what we'd change}

---

## Slide 7: Problems and Questions

**Visual**: 2-column layout. Left: open problems. Right: questions for the room.

**Open problems we are working on**:

1. **GDPR / DPIA turnaround**: DPO sign-off needed before Jun-14 large-scale extraction. Outline filed today.
2. **arXiv jurisdiction question**: §60d UrhG TDM right is DE-statutory; arXiv deposit is US-jurisdiction. Pending Bamberg legal-desk clarification.
3. **MediaPipe pose accuracy on micro-sway**: Apr-17 audit flagged this as unvalidated for choir use case. Calibration note (May 22, Sprint 3) will quantify error.
4. **Zoom-only stratum supplemented** (closed 2026-05-19): Originally thin at 2 verified videos; supplementary curation via Perplexity + yt-dlp search added 7 more, bringing the stratum to 9 (above the 3-5 target). H1 contrast now has adequate statistical power.

**Questions for the room**:

- Does Prof. Hacker have access to additional Tier-2 multitrack datasets (ESMUC / ChoralSynth) beyond Dagstuhl?
- For the directed-influence graph deliverable, preferred figure aesthetic — minimalist (matplotlib) or styled (Cytoscape)?
- Is the Jul 23 final presentation in-person or remote?

---

**Thank you. Open to your questions.**
