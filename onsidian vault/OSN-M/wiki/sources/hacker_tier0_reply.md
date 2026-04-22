---
title: "Prof. Hacker Tier-0 Reply — 5 YouTube URLs + ChoirAtHome Tools PDF"
type: source
alchemy_stage: nigredo
tags: [tier-0, hacker, youtube, jamulus, soundjack, nmp, project-8, data-sourcing]
ingested_date: 2026-04-22
source_count: 1
related: ["[[Project_8_MOC]]", "[[data_sourcing_policy]]", "[[Janine_Hacker]]", "[[limitations_register]]"]
team_take: ""
---

# Hacker Tier-0 Reply — URL List Received

**Source**: `raw/email_hacker_tier0_reply.txt` (email received 2026-04-22 06:06 CET)
**Manifest**: `raw/hacker_url_list.csv` (5 entries, Tier-0 schema)

**Resolution**: Watch-list item **W1 (L-D-1)** — **RESOLVED**. Reply received 2 hours 54 minutes before the 09:00 CET go/no-go deadline. No escalation needed.

---

## 1. The Five Videos

| # | Video ID | Title | Regime Label | Hacker Flag |
|:--|:--|:--|:--|:--|
| 1 | `isIV1XsKCgQ` | London City Voices singing "Toxic" live over Jamulus | **NMP-Jamulus** | — |
| 2 | `YiUJM6f8YpQ` | London City Voices - Jamulus & Zoom rehearsal | **NMP-Jamulus + Zoom** | — |
| 3 | `zp1qLCckgLk` | Karen Richardson — Jamulus World Jam — "Somebody To Love" (Queen) 13/06/2020 | **NMP-Jamulus** | — |
| 4 | `m811fZiPyaQ` | Jamulus Choral Festival (live stream) | **NMP-Jamulus** | — |
| 5 | `xPNu9TX-sgY` | Jul, jul, strålande jul — A cappella | **SUSPECT-POST-PRODUCED** | Hacker: *"seems to be a performance that has been edited, at least to me, singers are 'too much in sync'"* |

### Key observations

- **4 of 5 are Jamulus** (NMP low-latency) — this is gold for the project. Provides natural NMP-class references for Tier 1 visual analysis.
- **Video 2 explicitly shows Jamulus + Zoom side-by-side** — a direct within-performance comparison of the two regimes. Potentially the single most valuable video in the corpus.
- **Video 4 is a live stream** (Jamulus Choral Festival) — long-form; contains multiple choirs/ensembles performing live over Jamulus. Rich source.
- **Video 5 flagged by Hacker herself as post-produced** — aligns precisely with our **L-A-4** (post-synchronised virtual choirs) and **L-B-10** (fake-composite detection). Sets `post_aligned_flag = suspected` per mitigation strategy. **Validates our §3.3 exclusion criteria.**

---

## 2. Guidance from Hacker

1. **Search strategy**: use NMP tool names as search queries — "Jamulus", "SoundJack", etc. This directly extends `data_sourcing_policy.md` §3.1 query design.
2. **Live vs edited**: she says recognising live recordings "shouldn't be too hard" — endorses our §3.3 exclusion criteria approach. The fact she flagged Video 5 shows she shares the methodological concern.
3. **ChoirAtHome Tools PDF**: `https://choirathome.com/wp-content/uploads/2023/07/R2.2_ChoirAtHome_Tools.pdf` — a research deliverable from the **Choir@Home** project (*"Online Choirs: How to carry out virtual choir rehearsals with the help of digital tools"*). **This is a new primary source to acquire** — likely contains a taxonomy of NMP tools with latency characteristics.
4. **Status report expected**: she's "looking forward to your first status report" — confirms Iteration 2 report due **2026-04-24**.

---

## 3. Actionable Next Steps

1. **Download all 5 videos** via yt-dlp → populate `raw/youtube/<video_id>/` per directory discipline.
2. **Download ChoirAtHome Tools PDF** → `raw/R2.2_ChoirAtHome_Tools.pdf` → INGEST as new source.
3. **Expand Tier-1 search queries** per Hacker's guidance — add to [[data_sourcing_policy]] §3.1:
   - `"Jamulus choir"` / `"Jamulus rehearsal"` / `"Jamulus concert"`
   - `"SoundJack choir"` / `"SoundJack rehearsal"`
   - `"JackTrip choir"` / `"Sonobus choir"`
   - `"low-latency choir"` / `"online rehearsal live"`
4. **Run initial visual inspection** on Video 2 (Jamulus+Zoom) — could serve as flagship demo for Apr 30 deck.
5. **Prepare Iteration 2 status report** (due 2026-04-24) — Hacker explicitly requested it.

---

## 4. Impact on PAPER_LINKS.md

New source to add:

| ID | Citation | URL | Type | Status |
|:--|:--|:--|:--|:--|
| S-10 | Choir@Home Project. *R2.2 ChoirAtHome Tools.* 2023. | [PDF](https://choirathome.com/wp-content/uploads/2023/07/R2.2_ChoirAtHome_Tools.pdf) | S | ⬜ TO ACQUIRE |

---

## Open Questions

1. Video 4 (`m811fZiPyaQ`) is a live stream — how long is it? May need to extract specific performance segments rather than process the full stream.
2. Does the ChoirAtHome Tools PDF contain latency measurements for Jamulus/SoundJack that could inform our Tier-3 regime parameters (improving on Carôt & Werner 2007)?

## Backlinks

- [[Project_8_MOC]] (Rubedo parent)
- [[data_sourcing_policy]] (Citrinitas — Tier-0 update)
- [[Janine_Hacker]] (Albedo — relationship update)
- [[limitations_register]] (W1 L-D-1 resolved)
