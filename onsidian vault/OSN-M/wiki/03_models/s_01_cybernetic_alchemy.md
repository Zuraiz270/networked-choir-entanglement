---
title: S-01 Cybernetic Alchemy
type: source
alchemy_stage: rubedo
tags: [theory, mit_cci, cybernetics, alchemy, honest_signals, deep_read]
ingested_date: 2026-04-23
last_deep_read: 2026-04-23
source_count: 1
related: ["[[honest_signals_hierarchy]]", "[[alchemical_data_pipeline]]", "[[entanglement_index]]", "[[Peter_Gloor]]", "[[deep_read_audit]]"]
team_take: Source of the Project 8 vault's alchemical-stage terminology and honest-signals framing. Book (not peer-reviewed empirical paper), co-authored with Claude Sonnet (Anthropic). Most chapters concern plants/animals/bacteria — not directly relevant to Project 8. Chapter 14 "Data as Prima Materia" is the load-bearing section for us.
---

# S-01 Cybernetic Alchemy: From Paracelsus to Plant Sensors

**Citation**: Gloor, P. A. (2025). *Cybernetic Alchemy: From Paracelsus to Plant Sensors*. With Claude Sonnet (Anthropic) as AI Co-Author & Research Assistant. 16 chapters + Prologue + Epilogue. ~190 pages.
**Affiliations**: Research Affiliate, MIT System Design Management; Honorary Professor, University of Cologne; Chief Creative Officer, galaxyadvisors AG.
**AI co-authorship**: Explicitly acknowledged. Unusual authorship structure; not peer-reviewed as a standard journal article.
**raw path**: `raw/Cybernetic_Alchemy_Complete.pdf`

## 1. Core Argument

"Cybernetic alchemy" = practice of building instruments to read the **honest signals** that living organisms continuously broadcast, and developing the wisdom to interpret what those signals reveal [Prologue].

**Honest signals framework** [Prologue + Ch. 14]: every living organism — from bacteria coordinating through quorum sensing to humans leaking intent through vocal prosody — continuously broadcasts its inner state through measurable outputs that are "honest because they are costly to produce and difficult to fake." 22 years of research at MIT Center for Collective Intelligence.

## 2. Alchemical-ML Mapping (Ch. 14 "Data as Prima Materia")

This is the **only part of S-01 directly load-bearing for Project 8**. Gloor maps the classical alchemical stages onto the ML pipeline:

| Stage | Color | ML Pipeline Correspondence |
| :--- | :--- | :--- |
| **Nigredo** | Black | Data collection + preprocessing: filtering (50 Hz hum), normalization, segmentation (5-second epochs for bioelectric; frame-level for video), artifact rejection |
| **Albedo** | White | Feature extraction: mel-spectrograms, betweenness centrality, network density, oscillation frequencies, Symbiont archetype ratios, HRV, GSR |
| **Citrinitas** | Yellow | Model training: CNN (ResNet18), XGBoost, random forest, transformer. Continuous retraining for circadian rhythms. "The pattern was already in the material." |
| **Rubedo** | Red | **Interpretation by a human being** — "cannot be automated"; requires context, judgment, moral disposition |

[Ch. 14, p. 160 to 168 in extract, lines 5565 to 5747]

## 3. Four Guides (structural framework, Prologue)

1. **Paracelsus** (16th-c physician) → body broadcasts what mind conceals → Happimeter smartwatch (HRV + GSR)
2. **Rosenkreuzers** → nature is a readable book → Biolingo platform (23 researchers / 9 universities for plant bioelectrics)
3. **Douglas Adams** → the translation problem (question-finding is harder than answer-finding) → ML model training
4. **Isaac Asimov** → psychohistory as statistical prediction of collective behavior → SNA + communication-pattern mining

## 4. Instruments Named (§2 and throughout)

| Instrument | Domain | Used by Project 8? |
| :--- | :--- | :--- |
| **Happimeter** | HRV + GSR smartwatch | No (out of Project 8 scope) |
| **Perceptiface** | Facial micro-expression analyzer | No (out of scope) |
| **Symbiont Analyzer / SocialCompass** | WhatsApp → bee/ant/butterfly/capybara/leech archetypes | Yes (used in COINs seminar Phase 1, not Project 8 proper) |
| **Biolingo** | Plant bioelectric platform | No (out of scope) |
| **MoCo (Momentum Contrast)** | Animal behavior video | No (out of scope) |
| **AD8232 + ESP32** | Plant bioelectric hardware | No |

## 5. Structure

| Part | Chapters | Focus |
| :--- | :--- | :--- |
| I | 1-3 | Paracelsus + humans + honest signals |
| II | 4-7 | Rosenkreuzers + collaborative networks + Biolingo |
| III | 8-10 | Douglas Adams + translation problem + Symbiont Analyzer |
| IV | 11-13 | Asimov + honest signals hierarchy (humans → animals → plants → fungi → bacteria) |
| V | 14-16 | **Convergence**: 14 Data as Prima Materia, 15 Silent Signals, 16 Dew and Fire |

## 6. Limitations

**Implicit** (no §Limitations section since this is a book, not an empirical paper):

- **Not a peer-reviewed journal article.** Claim-to-evidence ratio is much higher than a standard scientific paper.
- **AI co-authorship** acknowledged (Claude Sonnet), but no standard attribution methodology exists for this.
- **Most chapters concern non-human organisms** (plants, animals, bacteria, fungi). Only Ch. 14 (the alchemical-ML mapping) and parts of Ch. 11-13 (honest signals in human teams) are directly relevant to Project 8's human-choir domain.
- Claims about "Biological Resonance" and "Planetary Qi" are philosophical/metaphoric; they are not operationally defined as measurable constructs in the book.
- The "Vault opening" metaphor is rhetorical; no specific predictions are made that could be falsified.
- "22 years of research at MIT CCI" is cited but individual empirical studies within that corpus are not enumerated or meta-analyzed.
- The alchemical-stage → ML-pipeline mapping is a **metaphor-structure** (Gloor calls it "a structural correspondence, not a metaphor," [p. 5565-5573]), not an empirically derived methodology.
- Book rhetoric sometimes overstates: e.g., the opening Phänomena-visitor plant-detection vignette combines scientific facts (ECG, ML classification) with claims that blur into mysticism (plant "reading" visitor's "honest signals").

## 7. Relevance to Project 8 E(t)

**S-01 is load-bearing for**:

- **Alchemical-stage terminology** used throughout the Project 8 vault ([[Project_8_MOC]], wiki organization in 4 alchemical stages). This is a direct cite from Ch. 14.
- **[[honest_signals_hierarchy]]** concept — the multi-layer classification from team-level communication down to bodily signals.
- **[[alchemical_data_pipeline]]** concept — Gloor's own 4-stage framing.
- **Peter Gloor entity** page — his authorship and affiliation.
- **Meeting Prof. Gloor on Apr 30**: Project 8 should cite this book as the framing narrative supervisor-side, even though the empirical content we use comes from S-02 (Entanglement) and other primary sources.

**S-01 is NOT**:

- An empirical source for any Project-8 measurement or threshold.
- A source for the term "entanglement" as used in Project 8 — that comes from S-02 (Gloor et al. 2022 Social Networks paper).
- A source for "Planetary Qi" as an operationally defined entanglement metric — the term is philosophical in the book, not technical.
- Evidence for any specific ML architecture choice — it names CNN/XGBoost/RF/transformer but as examples, not comparisons.
- A validator for the entanglement index E(t) — S-01 describes the cybernetic-alchemy philosophy, not NMP-specific coordination metrics.

## 8. Corrections Logged Against Prior Digest

See [[deep_read_audit]] for full table. Summary:

| Issue | Prior claim | Corrected reading |
| :--- | :--- | :--- |
| Missing AI co-authorship | "Gloor, P.A. (2025)" | Co-authored with Claude Sonnet (Anthropic) as AI Co-Author. Explicit on title page. This is unusual authorship structure; peer-review status unclear. |
| "The project adopts Gloor's four-stage metabolic model" presented as fact | — | It is a **metaphor-structure** (Gloor: "a structural correspondence"), not an empirical model. Project 8 adoption is a methodological choice inspired by S-01, not an empirical validation of the mapping. |
| "Planetary Qi: The global network of entrainment between humans, plants, and machines" as defined concept | — | "Planetary Qi" is Ch. 13's title and a philosophical framing. **Not operationally defined** in the book as a measurable construct. Should not be cited as a Project-8 technical term. |
| "Honest Signals... measurements that cannot be faked" — correct framing | Correct | Honest signals are "costly to produce and difficult to fake" [Prologue]. |
| "Role in SNA-OSN-M: Operating Manual for our dashboard. It defines the Entanglement Index" | — | S-01 does NOT define the Entanglement Index. That's S-02 (Gloor et al. 2022 Social Networks). S-01 provides the **philosophical framing** (alchemical stages, honest signals hierarchy), not the mathematical definition. |
| Missing instrument catalog | (no mention) | Happimeter, Perceptiface, Symbiont Analyzer / SocialCompass, Biolingo, MoCo, AD8232+ESP32 are all described. Only Symbiont Analyzer is used in COINs Phase 1 (Project 8 Phase 0); others are out of Project 8 scope. |
| Missing "most of the book is non-human" caveat | (no mention) | Only Ch. 14 (Data as Prima Materia) and parts of Ch. 11-13 (honest signals in teams) are Project-8-relevant. Plant / animal / fungal / bacterial chapters are out of scope. |
| "The Vault: A metaphor for the hidden causal structures of nature that are now 'opening' through computational analysis" | — | Correct as rhetorical framing; not a defined technical term. |
