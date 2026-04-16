# SNA-OSN-M Wiki — Schema & Operating Protocol

This file governs how the LLM maintains this vault. It is the "IDE config" for the LLM Wiki pattern applied to the SNA-OSN-M seminar (Uni Bamberg × Uni Köln × HSLU, Summer 2026).

Zuraiz's **global** CLAUDE.md (EBSE protocol) applies on top — every wiki operation must honor its §2 rules (zero assumptions, RCA, no hallucinations, planning threshold, clean code, research-first).

---

## 1. Identity

- **The vault**: an LLM Wiki for SNA-OSN-M, modeled on Karpathy's pattern (lineage: Vannevar Bush, *As We May Think*, 1945).
- **You (the LLM)**: the wiki maintainer. You read `raw/`, write `wiki/`, and keep this `CLAUDE.md` current.
- **Zuraiz**: the curator. Sources, direction, questions.
- **Team**: Zuraiz + Hassaan Ahmad + Hammad Anwar ("Tree Huggers", conscientious stance). Epistemic lens optionally surfaced in the `team_take` frontmatter field.

---

## 2. Architecture

Three layers:

1. **`raw/`** — immutable source repository. PDFs, emails, presentations, xlsx, transcripts. **You never modify these files.** Only read.
2. **`wiki/`** — LLM-owned synthesis layer. Markdown pages you create, maintain, cross-link, and update on every operation.
3. **`CLAUDE.md`** — this schema. Co-evolved with Zuraiz over time. You may propose updates but only write after explicit approval; log a `schema` entry in `log.md` when you do.

Do not touch `.obsidian/` (tool config) or `Welcome.md` (default placeholder, not a wiki page).

---

## 3. Alchemical Lifecycle

Every wiki page is tagged with one of four alchemical stages, inspired by Gloor's *Cybernetic Alchemy*. Required in YAML frontmatter as `alchemy_stage: <stage>`.

| Stage | Color | Directory | Meaning |
|:---|:---|:---|:---|
| **Nigredo** | black | `wiki/sources/` | Prima materia · raw digest · one page per source file |
| **Albedo** | white | `wiki/entities/` | Purification · named entities (people, orgs, places, artifacts) |
| **Citrinitas** | yellow | `wiki/concepts/` (*) | Illumination · cross-source concepts, frameworks, themes |
| **Rubedo** | red | `wiki/` root | Magnum opus · top-level synthesis (project overviews, final wisdom) |

(*) `wiki/concepts/` materializes only when the first concept page is needed — YAGNI until then.

A page's stage is not permanent — you may promote pages (Nigredo→Albedo→Citrinitas→Rubedo) as synthesis deepens. Log promotions in `log.md` with a `promote` verb entry.

---

## 4. Frontmatter Schema

Required on every wiki page (except `index.md` and `log.md`, which have no frontmatter):

```yaml
---
title: <human-readable title>
type: source | entity | concept | synthesis
alchemy_stage: nigredo | albedo | citrinitas | rubedo
tags: [<kebab-case>, ...]
ingested_date: YYYY-MM-DD
source_count: <int>     # number of raw/ files supporting this page
related: ["[[Page_A]]", "[[Page_B]]", ...]
team_take: <optional 1-line Tree-Hugger perspective>
---
```

---

## 5. Operations

Three verbs. Exactly one per turn unless Zuraiz specifies otherwise.

### 5.1 INGEST

Bringing a new source into the wiki.

1. Confirm the source is in `raw/`. If not, copy it in first (preserving original).
2. Read the source in full. PDFs: use Read with `pages=...` for >10 pages. pptx/xlsx: extract text with the appropriate tool (anthropic-skills:pptx / anthropic-skills:xlsx).
3. Briefly summarize key takeaways to Zuraiz **in chat** before touching files.
4. **Write or update**, in order:
   1. `wiki/sources/<source_name>.md` — the digest (Nigredo).
   2. All affected entity pages — create new / update existing (Albedo).
   3. All affected concept pages (Citrinitas) — create only if a genuine concept emerges across ≥2 sources.
   4. All affected synthesis pages (Rubedo) — usually `Project_Overview.md`, sometimes `Team_Profile.md`.
   5. `wiki/index.md` — add new page entries; bump `source_count`s.
   6. `wiki/log.md` — append the ingest entry (see §7).
5. **Rule 1 — touch ≥3–5 pages per ingest.** If the source is too narrow to justify 3 pages, either (a) fold it into an existing source's digest, or (b) defer ingest until more context exists.

### 5.2 QUERY

Answering a question from the wiki.

1. Read `wiki/index.md` first.
2. Open the candidate pages it points to.
3. Synthesize an answer using `[[wikilinks]]` as citations. Every factual claim must trace to a wiki page, which in turn traces to a `raw/` file.
4. When an answer yields a durable insight, offer to **file it back** as a new wiki page (concept or synthesis). Zuraiz approves explicitly.
5. Unknowns go in an `## Open Questions` section on the relevant page — not confabulated.

### 5.3 LINT

**Rule 2 — every 5 INGESTs, run a LINT.**

Checklist:

- [ ] **Contradictions**: any two pages make incompatible claims? Flag both, propose resolution.
- [ ] **Stale claims**: older pages superseded by newer sources? Update or mark `[STALE]`.
- [ ] **Orphan pages**: pages with zero incoming wikilinks? Either link them in or delete.
- [ ] **Dangling wikilinks**: `[[X]]` referenced but `X.md` missing? Create stub or remove link.
- [ ] **Unmade concept pages**: recurring ideas across ≥2 sources with no `concepts/` page? Propose creation.
- [ ] **Data gaps**: `## Open Questions` items a web search or new source could close.
- [ ] **Frontmatter integrity**: valid YAML, correct `alchemy_stage`, up-to-date `source_count`.
- [ ] **Index coverage**: every `.md` in `wiki/` (except `index.md`/`log.md`) listed in `index.md` exactly once.

Append `## [YYYY-MM-DD] lint` entry to `log.md` with findings and actions.

---

## 6. Naming & Wikilink Conventions

- **Synthesis & entity pages**: `Snake_Case.md` (e.g., `Peter_Gloor.md`, `Project_Overview.md`).
- **Source digests**: `snake_case.md` (lowercase, mirrors raw filename stem — `info.txt` → `info_txt.md`).
- **Intra-wiki references**: `[[Wikilinks]]` (bare name — Obsidian resolves across subfolders). Do **not** use markdown `[text](path)` for internal refs (the graph view misses these).
- **External refs**: markdown links with explicit URLs.
- **Folders**: `sources/`, `entities/`, (later) `concepts/`, (later) `assets/` for downloaded images.

---

## 7. Log Entry Format

Parseable via `grep "^## \[" log.md | tail -5`.

```markdown
## [YYYY-MM-DD] <verb> | <object>

<2–8 line summary>

**Pages touched**: list with CREATED / UPDATED prefix.
**Rule 1**: ≥3–5 pages ✓/✗
**Ingest counter**: N/5 until next LINT
```

`<verb>` ∈ { `ingest`, `query`, `lint`, `promote`, `schema` }. `schema` entries log changes to this `CLAUDE.md`.

---

## 8. Rules (Invariants)

1. **Rule 1** — every INGEST touches ≥3–5 wiki pages.
2. **Rule 2** — every 5 INGESTs, run a LINT.
3. **Raw is immutable** — `raw/*` is read-only. Original files preserved.
4. **No fabrication** — every claim cites a `raw/` file or another wiki page. Unknowns go in `## Open Questions`.
5. **Evidence hierarchy** (global EBSE §3): L1 Docs > L2 Research > L3 Standards > L4 Codebase > L5 Community ×2. Cite level when it matters.
6. **Wikilink hygiene** — no dangling `[[links]]`. Create the target page or drop the link.

---

## 9. Tree Hugger Lens

Team epistemic stance: *conscientious*. Use the optional `team_take` frontmatter line to surface the team's perspective on a source — especially those inviting value judgments (data ethics, platform harms, ecological costs of compute). Leave blank on neutral factual pages. **YAGNI**: do not manufacture takes.

---

## 10. EBSE Alignment (global CLAUDE.md)

All wiki operations obey the global protocol (EBSE §2):

- **Zero assumptions** — verify against `raw/` and existing wiki pages before asserting.
- **RCA over patch** — if a wiki claim is wrong, find the upstream source error; don't just overwrite.
- **No hallucinations** — verify file paths, dates, names against `raw/` before writing.
- **Planning threshold** — multi-file schema changes require a plan + approval.
- **Clean code** — centralized frontmatter schema; DRY; YAGNI on speculative scaffolding.
- **Research-first** — cite primary sources (L1–L2) over community synthesis.

Evidence trail (global §3) is **required** when an ingest introduces a non-trivial architectural or factual claim that contradicts earlier pages.

---

## 11. What is NOT the wiki

- `.obsidian/` — Obsidian tool config. Hands off.
- `Welcome.md` — Obsidian default placeholder. Do not link it from the wiki; leave as-is.
- Anything outside `OSN-M/` — out of scope. The parent folder is read-only reference staging, not part of the vault.
