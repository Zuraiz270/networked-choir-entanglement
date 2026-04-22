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

---

## [2026-04-18] promote | implementation_plan.md → PROJECT_GUIDE.md

Repo-root canonical document restructured from engineer-facing v2.1 `implementation_plan.md` (499 lines, dense, jargon-heavy, unstructured) into team-facing `PROJECT_GUIDE.md` v1.0. Trigger: Zuraiz rejected the v2.1 plan on 2026-04-18 as "very focused and unstructured, difficult even for a seasoned person, no structure, generic goals like 'impress the professors'." New doc is readable by non-DSP teammates (Kumaran, Hassan) in one sitting.

Structure of the new doc:

- §1 TL;DR · §2 Real Problem We're Solving · §3 Glossary (~30 terms with analogies) · §4 Where We Are Today · §5 Where We Need to Be · §6 Roadmap Week-by-Week · §7 Who Does What · §8 Three Data Sources · §9 What Could Go Wrong · §10 How We'll Know We Succeeded · §11 Technical Appendix (formulas · tier-gated feature catalog · directory discipline · EBSE evidence trails · verification smoke tests · DSP reality correction · vault integration · pinned stack versions).

No technical content dropped. All v2.1 formulas, feature catalogs, EBSE evidence trails, verification smoke tests, and DSP reality correction preserved verbatim in §11 Appendix. Presentation layer only.

**Pages touched** (0 content pages CREATED, 4 content pages UPDATED):

- UPDATED [[Project_8_MOC]] — replaced all `implementation_plan.md` pointers with `PROJECT_GUIDE.md` pointers; added "Start here →" banner after frontmatter.
- UPDATED [[entanglement_index]] — pointer updates (line 14, 67).
- UPDATED [[data_sourcing_policy]] — pointer update (line 14).
- UPDATED [[log]] (this file).

**Also at repo root**:

- CREATED `PROJECT_GUIDE.md` (new canonical team guide).
- CREATED `drafts/email_hacker_tier0_request.md` (rewritten brief email to Prof. Hacker: 62-word body, actionable subject, no DSP jargon — supersedes the over-technical first draft).
- DELETED `implementation_plan.md` (content preserved in `PROJECT_GUIDE.md` §11).

**Rule 1**: N/A (promotion, not ingest — no new sources).
**Rule 2**: LINT counter unchanged (1/5 after previous ingest).
**Evidence trail for this promotion**: user feedback on 2026-04-18 re: accessibility ("difficult even for a seasoned person", "no structure", "generic goals") + follow-up feedback on email ("unclear subject", "very hectic to read", "too much detail"). Saved as feedback memories `feedback_writing_style.md` and `feedback_email_tone.md` in the session memory directory. Applies to all future team-facing docs and academic emails on this project.

**Git commit plan** (not yet executed): atomic commit with Conventional Commits message `docs(guide): replace implementation_plan.md with team-facing PROJECT_GUIDE.md + add Hacker email draft`.

---

## [2026-04-18] lint | limitations_register_audit

Rigorous EBSE-grade audit of every threat to H1–H3 and Gates A–D for Project 8. Triggered by Zuraiz's request: *"evaluate, specify and eliminate all the limitations with rigorous effort and strategies — if you fail to tackle a limitation then give me relevant context and search queries to do it myself."* Scope: audio/DSP · computer vision · network-statistics · data sourcing · legal/GDPR · project reproducibility · stakeholder · integration. Output: **59 limitations** across 8 categories · 43 Mitigated · 6 Escalated · 4 Open · 1 Accepted · 5 Resolved. **17 items ★ newly-surfaced** beyond v1.0 `PROJECT_GUIDE.md` — incl. L-A-4 post-synchronisation editing artefact in virtual-choir videos, L-B-4 mouth-aperture lyric confound, L-C-5/C-7/C-8 statistical-power + multiple-hypothesis correction, L-E-1 FaceMesh-as-biometric under GDPR Art. 9, L-E-3 DPIA requirement, L-F-5 MediaPipe wheel smoke-test, L-G-2 Apr 30 deck. Each Escalated item carries ≥ 2-paragraph context + 3 verbatim search queries (Google Scholar / arXiv / legal DB) for Zuraiz to run himself. Pre-Apr-30 watch-list (§12.9): W1 L-D-1 Hacker URL list (2026-04-22 09:00 CET) · W2 L-F-5 MediaPipe smoke-test (2026-04-25) · W3 L-G-2 joint-deck draft (2026-04-25 draft / 2026-04-29 rehearsal).

**Pages touched** (5 content + 1 meta):

- UPDATED `PROJECT_GUIDE.md` (repo root — canonical §12 body, ~350 lines appended after §11.8: heat-map + 59 entries + watch-list + maintenance protocol).
- UPDATED [[Project_8_MOC]] (Rubedo — Risks section gains `PROJECT_GUIDE.md §12` pointer + [[limitations_register]] wikilink).
- UPDATED [[entanglement_index]] (Citrinitas — §7 Open Questions cross-refs L-B-1/L-B-3/L-C-1 + See-also footer).
- UPDATED [[data_sourcing_policy]] (Citrinitas — §9 Open Questions cross-refs L-D-5/L-C-3/L-E-2 + See-also footer).
- CREATED [[limitations_register]] (Citrinitas — `wiki/concepts/limitations_register.md`. Vault-graph surface for the canonical §12: totals · categories entry-points · pre-Apr-30 watch-list · ★ quick index · Escalated search-query packet index · coverage-completeness · backlinks).
- UPDATED [[log]] (this entry).

**Rule 1**: 5 content pages touched ✓ (exceeds minimum 3).
**Rule 2**: LINT counter bumped 1/5 → **2/5** (3 more INGESTs until next LINT).
**Ingest counter**: 2/5.

**Evidence trail**: single-source-of-truth body lives in `PROJECT_GUIDE.md §12`; vault pages are cross-reference surfaces only (YAGNI — no body duplication). Every Mitigated entry cites ≥ 1 concrete action + owner + ISO date. Every Escalated entry carries L1–L3 source pointer (ISMIR DOI · GDPR statute article · arXiv ID) + 3 verbatim search queries. Newly-surfaced items ★ annotated throughout.

**Deferred / downstream**:

- **Watch-list execution (Zuraiz)**: W1 Hacker email gate 2026-04-22 09:00 CET · W2 MediaPipe smoke-test by 2026-04-25 · W3 draft Apr 30 joint-deck by 2026-04-25.
- **DPIA** (L-E-3) draft + Bamberg DPO consult (L-E-1) before 2026-05-08 (WP1 + legal).
- **Escalated web-research** (L-A-3, L-B-3, L-E-1, L-E-2, L-D-5): Zuraiz to execute search packets over the next 2 weeks; findings append back to `PROJECT_GUIDE.md §12` as follow-up entries.
- **Paper §Threats-to-Validity**: curated subset of §12 drafted during paper skeleton phase (§6 2026-05-15 deliverable).

---

## [2026-04-19] schema | v2.2_scope_cut

Deliberate scope reduction on Project 8, approved by Zuraiz: *"the current plan is overambitious. Reduce YouTube dataset to 20 to 30 well-chosen videos, no post-produced stuff. Quality over quantity. Latency conclusions come from Tier 2 + Tier 3 only. E(t) stays simple. One figure per professor. GDPR on critical path. Simplify, validate early, scale only if time permits."* Prior state was v2.1 / PROJECT_GUIDE v1.0 targeting N = 150 Tier 1 videos with a full ablation matrix.

**Six concrete changes propagated into the docs:**

1. **Tier 1 dataset** cut from N = 150 to 20 to 30 hand-curated videos. Heavily edited / post-produced / virtual-composite content explicitly excluded (L-A-4, L-B-10 cross-refs).
2. **H1 / H2 test bed** carried by Tier 2 multitrack + Tier 3 controlled latency injection only. Tier 1 YouTube demoted to visual-feature sanity check for H3.
3. **E(t) frozen** at (1/3, 1/3, 1/3) weights. No regime-specific reweighting, no learned weights, no extra terms.
4. **Gate C deliverables** streamlined to exactly one flagship figure per professor (Hacker directed influence graph, Gloor alchemical Honest-Signals diagram). Additional visualisations go to paper appendix.
5. **GDPR promoted to pre-Apr-30 watch-list**: W4 L-E-1 (FaceMesh biometric position, 2026-04-29), W5 L-E-3 (DPIA outline, 2026-04-29). Original DPIA full draft still due 2026-05-08.
6. **R4 runtime risk** downgraded from MED to LOW. Expected Demucs end-to-end runtime at N = 30 drops from 12 to 25 h to 2 to 5 h on CPU. Compute-budget (L-F-8) rescoped from ~30 to 50 GPU-h to ~10 to 20 GPU-h.

**Pages touched** (5):

- UPDATED `PROJECT_GUIDE.md`: §1 TL;DR (N count + tier clarifier), §5 Claims (tier test-bed note), §6 milestone rows May 15 + Jun 30, §7/§10 Gate C flagship-figure clarifier, §8 Tier 1 header + post-prod exclusion, §9 R4 downgrade + v2.2 note, §11.2 feature-catalog legend + frozen-weights rule, §12.1 L-A-9 row rescope, §12.6 L-F-8 row rescope, §12.9 watch-list promoted to 5 items (W4 L-E-1, W5 L-E-3 added).
- UPDATED [[Project_8_MOC]]: H3 tier annotation updated, WP-table footer gains v2.2 dataset note, Risks section notes R4 downgrade.
- UPDATED [[data_sourcing_policy]]: Tier 1 N-target row updated, §3.3 exclusion criteria gains binding post-production rule.
- UPDATED [[entanglement_index]]: §1 Definition gains v2.2 frozen-weights rule note.
- UPDATED [[log]] (this entry).

**Rule 1**: 5 content pages touched ✓ (exceeds minimum 3, though this is a schema entry not an INGEST).
**Rule 2**: LINT counter unchanged (schema entries do not advance the INGEST counter). Still **2/5**.

**Evidence trail**: the scope cut is a Zuraiz-authored decision, not externally sourced. Rationale logged to the persistent memory file `memory/project_scope_cut_v2_2.md` (not part of the vault). Downstream items deferred (paper §Threats-to-Validity still pulls from §12; Apr 30 deck still needs drafting; DPIA full draft still due 2026-05-08) are unchanged.

**Deferred / downstream (unchanged by v2.2):**

- W1 Hacker URL list go/no-go 2026-04-22 09:00 CET.
- W2 MediaPipe 0.10.14 × Py 3.11 × Win 11 smoke-test by 2026-04-25.
- W3 Apr 30 joint-deck draft 2026-04-25, rehearsal 2026-04-29.
- W4 FaceMesh biometric position drafted 2026-04-29 (new under v2.2).
- W5 DPIA outline 2026-04-29 + full DPIA by 2026-05-08 (promoted under v2.2).

---

## [2026-04-22] ingest | PAPER_LINKS.md (Init Task #2)

Execution of `osn_master_prompt.md` §3 Task 2: *"Create a single, hallucination-free bibliography matrix that links directly to the `raw/` PDFs."* This was the last remaining initialization task — Task 1 (`PROJECT_GUIDE.md`) completed 2026-04-18, Task 3 (wiki skeleton) completed 2026-04-16.

Created `PAPER_LINKS.md` at repo root with:

- **10 Primary sources** (peer-reviewed: Dagstuhl ChoirSet, Cuesta multi-f0, BlazePose, Pentland Honest Signals, Benjamini-Hochberg, Phipson-Smyth, G*Power, Daffern, Kortli, Cohen) — cross-referenced against `PROJECT_GUIDE.md` §11.4 evidence trails. No hallucinated DOIs.
- **9 Secondary sources** (Cybernetic Alchemy ✅ in raw, Cairns PhD, Carôt & Werner NMP, ESMUC Dataset, Patterson & Jack, Hilton, Geiger, Müller, Lancichinetti).
- **6 Course materials** in `raw/` — all verified present.
- **Acquisition priority queue** mapped to project milestones (Apr 30 → May 8 → May 22 → Jun 30).
- **5 Keyword Strategist search packets** (per `osn_master_prompt.md` §4) covering: NMP + choir coordination, pose estimation + breathing, network science in music, statistical methods, GDPR/legal.

**Pages touched** (2):
- CREATED `PAPER_LINKS.md` (repo root)
- UPDATED [[index]] (PAPER_LINKS.md entry added to Synthesis section; timestamp bumped to 2026-04-22)

**Rule 1**: 2 pages touched ⚠️ (below minimum 3 — justified: repo-root artefact per master prompt, not a standard `raw/` ingest).
**Ingest counter**: 3/5.

---

## [2026-04-22] ingest | hacker_tier0_reply

Received Hacker's reply at 06:06 CET — **3 hours before the 09:00 W1 go/no-go deadline.**
Source `raw/email_hacker_tier0_reply.txt` ingested. Created manifest at `raw/hacker_url_list.csv`.

**Content**:
- 5 YouTube URLs: 4× Jamulus (including a side-by-side Jamulus+Zoom comparison, incredibly valuable for our thesis), 1× flag for "post-produced" which validates our L-A-4 limitation.
- NMP search query guidance (Jamulus/SoundJack).
- New secondary source to acquire: `ChoirAtHome Tools PDF`.
- First status report expected by Iteration 2 (2026-04-24).

**Pages touched** (6):
- CREATED [[hacker_tier0_reply]] (Nigredo)
- UPDATED [[Janine_Hacker]] (Albedo — tier-0 open question closed; source_count bumped)
- UPDATED [[data_sourcing_policy]] (Citrinitas — W1 go/no-go resolved; new queries added; source_count bumped)
- UPDATED [[limitations_register]] (Citrinitas — W1 L-D-1 watch list item resolved)
- UPDATED [[Project_8_MOC]] (Rubedo — W1 open question closed; source_count bumped)
- UPDATED `PROJECT_GUIDE.md` (repo root — §12.4 + §12.9 W1 resolved)
- UPDATED [[index]] (hacker_tier0_reply added + timestamp)
- UPDATED [[log]] (this entry)

**Rule 1**: 6 pages touched ✓ (exceeds minimum 3).
**Ingest counter**: 4/5.

---
