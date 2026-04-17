# Wiki Log

Append-only chronological record of all wiki operations. Parseable via `grep "^## \[" log.md | tail -5`.

Verb taxonomy: `ingest` · `query` · `lint` · `promote` · `schema`. See [`../CLAUDE.md`](../CLAUDE.md) §7.

---

## [2026-04-16] schema | bootstrap

Initial wiki schema written. Establishes the LLM Wiki pattern for SNA-OSN-M with the alchemical four-stage lifecycle (Nigredo → Albedo → Citrinitas → Rubedo), frontmatter schema, INGEST / QUERY / LINT operations, and Rules 1 & 2.

**Pages touched**: CREATED `CLAUDE.md`.

---

## [2026-04-16] ingest | info.txt

First content ingest. Source: `raw/info.txt` — two admission / block-course emails from Prof. Janine Hacker (Uni Bamberg), April 2026. Establishes the SNA-OSN-M seminar structure (partners, dates, ECTS, team roster, chapter assignment).

**Pages touched** (5 content + 2 meta):
- CREATED [[info_txt]] (Nigredo)
- CREATED [[Project_Overview]] (Rubedo)
- CREATED [[Team_Profile]] (Albedo)
- CREATED [[Janine_Hacker]] (Albedo)
- CREATED [[Peter_Gloor]] (Albedo)
- CREATED [[index]]
- CREATED [[log]] (this file)

**Rule 1**: 5 content pages ✓
**Ingest counter**: 1/5.

---

## [2026-04-16] ingest | Chapter_14_Upgraded_Presentation.pptx

Source: `raw/Chapter_14_Upgraded_Presentation.pptx` (20 slides). Confirms chapter title "Data as Prima Materia", Part V: The Convergence. Reveals Zuraiz's slides 15–20 are partially templated (Slide 16 has unfilled placeholders requiring the team's actual tool data). Urgent: must be filled before 12:30 CET presentation.

**Pages touched** (4 content + 2 meta):
- CREATED [[chapter_14_presentation]] (Nigredo)
- CREATED [[socialcompass_tools]] (Citrinitas — concept page triggered by cross-tool references in slides)
- UPDATED [[Team_Profile]] (Albedo — artifact status corrected: pptx now in raw/)
- UPDATED [[Project_Overview]] (Rubedo — chapter title confirmed, presentation slot added)
- UPDATED [[index]]
- UPDATED [[log]]

**Rule 1**: 4 content pages ✓
**Ingest counter**: 2/5.

---

## [2026-04-16] ingest | CyberneticAlchemy_Seminar_SignUp2.xlsx

Source: `raw/CyberneticAlchemy_Seminar_SignUp2.xlsx`. Contains chapter sign-up table, instructor session planner, and complete SocialCompass profiles for ~25 students. Critical data: full four-tool results for all three Tree Hugger team members, cohort-wide pattern (Capybara dominance, Tree Hugger network position), iteration schedule, and instructor live prompt for Chapter 14.

**Key corrections**: Hammad Anwar's Symbiont is **Capybara** (not Ant as implied by original prompt). Name corrected: "Hassan Ahmed" (XLSX official) vs. "Hassaan Ahmad" (info.txt). Hammad's response latency = 1.99 hours (slowest of three).

**Pages touched** (3 content + 2 meta):
- CREATED [[seminar_signup]] (Nigredo)
- UPDATED [[Team_Profile]] (Albedo — full 4-tool data table for all 3 members)
- UPDATED [[Project_Overview]] (Rubedo — iteration schedule added, open questions closed)
- UPDATED [[index]]
- UPDATED [[log]]

**Rule 1**: 3 content pages ✓
**Ingest counter**: 3/5.

---

## [2026-04-16] ingest | Tips for groupwork_COINs25.pptx

Source: `raw/Tips for groupwork_COINs25.pptx`. Group-work guidance and communication recording protocol from the COINs seminar. Lower priority for presentation prep; adds iteration schedule confirmation and Scrum process detail.

**Pages touched** (2 content + 2 meta):
- CREATED [[tips_groupwork]] (Nigredo)
- UPDATED [[Project_Overview]] (Rubedo — iteration schedule cross-referenced)
- UPDATED [[index]]
- UPDATED [[log]]

**Rule 1**: 2 content pages (below minimum — acceptable: tips_groupwork is a thin source; merged supplementary data into existing pages rather than creating orphans) ⚠️
**Ingest counter**: 4/5 — **LINT REQUIRED ON NEXT INGEST.**

---

## [2026-04-16] NOTE | Cybernetic_Alchemy_Complete.pdf

Source: `raw/Cybernetic_Alchemy_Complete.pdf`. **NOT YET INGESTED** — markitdown extraction timed out (file too large for automated full-text extraction). Requires targeted page-range read using `Read` tool with `pages=` once Chapter 14 page range is known. Scheduled for a future INGEST.

---

## [2026-04-16] ingest | presentation_deliverables.md

Source: `raw/presentation_deliverables.md` (team-authored). Zuraiz's final 10-min speaking script for Chapter 14 slides 15–20 + Q&A prep (3 canned responses) + timing cheat sheet. Fills the pptx template's placeholders with live Tree Huggers 4-tool data and introduces 5 net-new claims: cohort-wide Sad/Neutral Perceptiface as context artifact (not personality); HireVue as the real-world Nigredo→Rubedo failure exemplar; Löhnert & Sova cohort quotes on Capybara saturation; ">1 year WhatsApp chat" scope qualifier; Hammad's 2-hour latency reframed as an open judgment call.

**Pages touched** (5 content + 2 meta):
- CREATED [[presentation_deliverables]] (Nigredo)
- UPDATED [[chapter_14_presentation]] (Nigredo — Slide 15/16 Open Questions closed; cross-ref added)
- UPDATED [[Team_Profile]] (Albedo — artifact added; Zuraiz label Open Question closed; source_count 4→5)
- UPDATED [[socialcompass_tools]] (Citrinitas — Capybara Puzzle sharpened with cohort quotes; Perceptiface context-effect promoted to cited claim; source_count 3→4)
- UPDATED [[Project_Overview]] (Rubedo — 12:30 slot marked delivered; source_count 4→5)
- UPDATED [[index]]
- UPDATED [[log]]

**Rule 1**: 5 content pages ✓
**Ingest counter**: 5/5 — **LINT REQUIRED AFTER NEXT INGEST.**

---

## [2026-04-16] ingest | SignUpSheet4ProjectsCOINs_26.xlsx

Source: `raw/SignUpSheet4ProjectsCOINs_26.xlsx` (53 KB, 2 sheets). Post-block-course project sign-up — distinct from the chapter-phase [[seminar_signup]]. Reveals the 10-topic cohort map, institutional distribution (Köln dominates plant/animal/agent; Bamberg clusters on human-team topics), and critically: **Tree Huggers carried over to the project phase intact**, with [[Kumaran_Vasu]] joining as 4th member. Their project topic = **"Entanglement in Online Choir"**. Sheet 2 = 17-email waitlist (purpose unclear; flagged as Open Question).

**Pages touched** (4 content + 2 meta):
- CREATED [[signup_sheet_projects]] (Nigredo — full 10-topic table, waitlist verbatim)
- CREATED [[Project_Phase_Roster]] (Rubedo — cohort-wide synthesis + our team detail)
- CREATED [[Kumaran_Vasu]] (Albedo — new 4th team member, no SocialCompass data yet)
- UPDATED [[Team_Profile]] (Albedo — new "Project Phase" section; composition Open Question closed; source_count 5→6)
- UPDATED [[Project_Overview]] (Rubedo — "Our Project" section added; team-formation Open Question closed; source_count 5→6)
- UPDATED [[index]]
- UPDATED [[log]]

**Rule 1**: 4 content pages ✓
**Ingest counter**: 6/5 — **LINT OVERDUE, RUNNING NOW.**

---

## [2026-04-16] lint

First LINT pass triggered by ingest counter reaching 6/5 (overdue from 5/5). Scope: all 13 wiki content pages + `index.md` + `log.md`.

### Findings

| # | Check | Result | Action |
|:--|:---|:---|:---|
| 1 | Contradictions | Reconciled: script says "about 25 students" — seminar_signup log entry says "~25 students". Consistent. | none |
| 2 | Stale temporal phrasing | `Project_Overview.md:41` said "Day 2 — today" | **Fixed**: stripped "— today" marker, kept date anchor `2026-04-16`. |
| 3 | Orphan pages | All 13 pages have ≥1 incoming wikilink. | none |
| 4 | Dangling wikilinks | All 15 unique `[[targets]]` resolve to existing `.md` files (13 content + `index` + `log`). | none |
| 5 | Unmade concept pages | **HireVue / emotion-AI-in-hiring** now referenced in [[presentation_deliverables]] + [[chapter_14_presentation]] — meets the ≥2-source threshold for a Citrinitas page (`wiki/concepts/emotion_ai_in_practice.md`). | **PROPOSED** — not created (YAGNI until Zuraiz approves). |
| 6 | Data gaps | (a) [[Kumaran_Vasu]] lacks SocialCompass data; (b) `Cybernetic_Alchemy_Complete.pdf` still not ingested; (c) Sheet 2 of [[signup_sheet_projects]] semantics unclear (17 unplaced emails). | Captured as Open Questions on respective pages. |
| 7 | Frontmatter integrity | All 13 content pages have valid `alchemy_stage` (2 rubedo · 4 albedo · 1 citrinitas · 6 nigredo). All have `type`, `ingested_date`, `source_count`. | none |
| 8 | Index coverage | All 13 content `.md` files listed in `index.md` exactly once. `index.md` and `log.md` correctly exempted. | none |
| 9 | Resolved Open Questions | Closed across Team_Profile (Symbiont label · project-team composition), Project_Overview (final-team formation), chapter_14_presentation (Slide 15 content · Slide 16 placeholders). Moved to `## Closed` sections per new convention. | none |
| 10 | Schema check | Wiki now has all four alchemical stages populated (2 rubedo + 4 albedo + 1 citrinitas + 6 nigredo). Directory `wiki/concepts/` materialized (1 page). | none |

### Outstanding / Deferred

- Ingest `Cybernetic_Alchemy_Complete.pdf` (targeted page-range read — wait for Chapter 14 page numbers).
- Decide on `emotion_ai_in_practice.md` concept page (HireVue + chapter 14 cross-link) — requires Zuraiz's approval.
- Track Kumaran Vasu completing the four-tool suite before Iteration 2 (2026-04-24) for data completeness.
- Verify Sheet 2 waitlist purpose next time the team talks to [[Janine_Hacker]] or [[Peter_Gloor]].

**Ingest counter**: reset → 0/5.

---

## [2026-04-17] ingest | implementation_plan.md v2.1 (Project 8 deep plan)

Source: repo-root `implementation_plan.md` — 24-ECTS deep implementation plan for Project 8 (*Entanglement in Online Choir*), v2.1 authored 2026-04-17 by Zuraiz + LLM. Seeds the vault graph with Project-8-specific pages so every future ingest (Cybernetic Alchemy PDF, Dagstuhl digest, Hacker URL list, etc.) has stable Rubedo/Citrinitas anchors to backlink into.

Key content seeded:

- **Rubedo MOC** for Project 8: hypotheses (H1/H2/H3 tier-mapped), 4 work packages, alchemical pipeline mapping, milestone table (Apr 30 Hacker+Gloor meeting; Jul 17 final).
- **E(t) Citrinitas page**: formula decomposition A(t)/V(t)/N(t) + null-model protocol + DSP reality-check (v2.1 correction — mixed-stereo YouTube cannot yield per-singer pairwise audio features; Demucs separates instrument classes, pyin is monophonic).
- **Data-sourcing policy Citrinitas page**: three-tier architecture · Tier-0/1/2/3 scientific roles · legal basis (§60d UrhG, EU DSM Art. 3, GDPR Art. 6/89) · prohibited practices (no self-recording preserved).

**Pages touched** (3 content + 2 meta):

- CREATED [[Project_8_MOC]] (Rubedo)
- CREATED [[entanglement_index]] (Citrinitas)
- CREATED [[data_sourcing_policy]] (Citrinitas)
- UPDATED [[index]] (3 new entries · last-updated 2026-04-17 · counter 1/5)
- UPDATED [[log]] (this file)

**Rule 1**: 3 content pages ✓
**Rule 2**: LINT counter 1/5 (reset at previous LINT 2026-04-16).
**Ingest counter**: 1/5.

**Evidence-trail note**: the five top architectural decisions underpinning the v2.1 plan (yt-dlp vs YouTube Data API · MediaPipe vs OpenPose · librosa pyin vs CREPE · Granger vs transfer entropy · uv vs poetry/conda) live in `implementation_plan.md` §8 with full L1–L5 source tables and Confidence/Applicability ratings per global `CLAUDE.md` §3. Not duplicated in the wiki (YAGNI — single source of truth is the plan file; wiki concept pages link back to it).

**Deferred**:

- Ingest `raw/Cybernetic_Alchemy_Complete.pdf` → 4 expected wiki pages ([[honest_signals]], [[coin_framework]], [[Alex_Pentland]], `cybernetic_alchemy_complete_pdf.md`). Scheduled 2026-04-18.
- Create [[hacker_url_list]] on receipt (blocked: email sent 2026-04-17; go/no-go 2026-04-22 09:00 CET).
- [[Kumaran_Vasu]] SocialCompass backfill (tracked in plan §6 WP2 onboarding).
