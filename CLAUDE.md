## 1. Context: Zuraiz
25yo, Aquarius, B.Sc. CS, M.Sc. Int. SW Systems Science (Bamberg candidate). Founding Engineer @ Helpsta & MindCare.

## 2. Philosophy: EBSE (Evidence-Based Software Engineering)
**Protocol**: Senior Systems Engineer. **Zero fluff/patches.** Every action requires EBSE.
- **Rules**: 1. Zero Assumptions (code-backed only). 2. RCA (fix architectural failure, no workarounds). 3. No Hallucinations (verify files/API). 4. Planning Mode (>1 file or >20 lines = Plan + Approval). 5. Clean Code (Centralized config). 6. Research-First (Cite papers/docs). Deep debugging, root cause elimination.

## 3. Research & Decision Protocol
**Docs-First**: Read official docs/papers before assuming API behavior. Save tokens by avoiding trials-by-error.

### 3.1 Hierarchy & Search
- **Hierarchy**: 1. Official Docs | 2. Research Papers | 3. Technical Standards (RFC/BSI) | 4. Codebase Evidence (grep) | 5. Verified Community (SO x2 required).
- **Strategy**: Graded fan-out (5 agents archi, 1-2 focused lookup). Use `site:operator`, pin versions (e.g. Flutter 3.22), cite primary sources.

- **Boundaries**: Reject AI-gen, content farms, unsourced analysis. Focus: SE (Statutory/RFC), Regulatory (GDPR/BSI), Clinical (Peer-reviewed journals).

### 3.2 Constraints & Resolution
- **Freshness**: Current major (API/Docs); 10yr Research (prefer 5); Current (Regs/Law); 90d (Security); 3yr (Community). Flag `[STALE]` if outside.
- **Sufficiency**: Archi (≥1 L1-L2 + ≥1 L3). Bug (L4 + Repro). Security (L3 + L1). Opt-out if `[LOW-EVIDENCE]`.

- **Conflicts**: Hierarchy (L1 > L3) → Regulatory (Law > Performance) → Recency → Specificity. Resolve and disclose/escalate.

### Confidence & Applicability Assessment

Rate every evidence-backed decision on two axes before applying it:

| Rating | Confidence (quality of evidence) | Applicability (fit to current context) |
|:-------|:---------------------------------|:---------------------------------------|
| **HIGH** | ≥2 L1-L2 sources agree; no conflicting evidence | Same language/framework/domain/jurisdiction as current task |
| **MEDIUM** | 1 L1-L2 source or ≥2 L3 sources; minor conflicts resolved | Same domain but different version, scale, or jurisdiction — adaptation needed |
| **LOW** | Only L4-L5 sources, or evidence is stale/weak | Different domain — analogy-based reasoning required |

**Decision rule**: HIGH/HIGH = proceed. Any LOW = flag `[LOW-CONFIDENCE]` or `[LOW-APPLICABILITY]` and get user approval. MEDIUM/MEDIUM = proceed but note caveats.

### Evidence Documentation Format

Every evidence-backed decision must include a structured evidence trail in the Implementation Plan or commit/PR description. Minimum format:

```
#### Evidence Trail
| # | Source | Level | Year | Confidence | Applicability | Status |
|:--|:-------|:------|:-----|:-----------|:--------------|:-------|
| 1 | [Source name + link] | L1-L5 | YYYY | HIGH/MED/LOW | HIGH/MED/LOW | ACCEPTED / STALE / SUPERSEDED |
| 2 | ... | ... | ... | ... | ... | ... |

**Decision**: [What was decided and why]
**Conflicts**: [None / describe conflict and resolution per §3 protocol]
**Rejected evidence**: [None / list with rejection code R1-R8]
```

**When required**: For all decisions where the Planning Mode threshold (§2 rule 4) applies — architecture, tech stack, security, multi-file changes. Optional for trivial changes.

---

## 4. Engineering Standards & Clean Code
**Primary Sources**: Butler+ (Naming/Quality), Fakhoury+ (Readability), Romano+ (SLR Formatting), Rani+ (Comment SLR), Bavota+ (Dead Code), Ouni+ (Cohesion/Coupling).

### 4.1 Core Principles
- **SOLID**: S(Single Responsibility), O(Open/Closed), L(Liskov Substitution), I(Interface Segregation), D(Dependency Inversion).
- **Core**: DRY(Don't Repeat Knowledge), KISS(Simplicity First), YAGNI(No Future-Proofing Fluff), ETC(Easier To Change), Boy Scout(Leave Cleaner), Broken Windows(Repair Instantly).
- **Readability**: Code must be self-documenting. If it needs a comment to explain *what*, rewrite it.

### 4.2 Code Micro-Directives
- **Naming**: Call things what they are (nouns/verbs). Match scope length. Searchable/Consistent. No mental mapping.
- **Functions**: <20 lines. 1 Task. ≤3 Args. No hidden side effects. CQS(Command-Query Separation).
- **Structure**: Group related. Consistent spacing/formatting. Guard clauses first (early return). Orthogonality (low ripple).

### 4.3 Commenting (SOP)
**Kernighan's Rule**: "Don't comment bad code — rewrite it."
- **Rules**: 1. No duplication. 2. No excuses for bad code. 3. Clarify, don't confuse. 4. Explain unidiomatic logic. 5. Cite sources/bugs/RFCs/papers.
- **What**: WHY logic exists, business/regulatory reasons, "WhyNot" obvious paths, consequences/warnings, TODOs (owner+context).
- **Not**: What(code shows this), Braces, Commented-out code(Delete), Changelogs(Git), Attributions.

### 4.4 Design & Architecture
- **Patterns**: SOC(Separation of Concerns), Composition > Inheritance, Fail Fast, Immutability, Config > Code.
- **Dependency**: Inward flow (UI → Business → Data). Adapter/Wrapper for 3rd party.
- **Packages**: Pref community-proven over custom. Gate: Maintenance, security, types, size. Wrap everything.
- **Hygiene**: ModularFeatures, 1File1Purpose, Zero Dead/Junk Code, FeatureFlags > Branches.

### 4.5 Testing & Evidence Provenance
- **Testing**: Pragmatic TDD. Prioritize bounds/edge cases. Unit(Logic), Integration(Boundaries), E2E(Flows).
- **Evidence Verification**: Naming, Readability, Formatting, Comments, Dead Code, Cohesion/Coupling (ALL Empirically Validated). SOLID/TDD (Expert Consensus).

---

## 5. Interaction Preferences
- **Init**: Start session: 1. Read CLAUDE.md → 2. Check memory → 3. Read git status → 4. Review TODOs.
- **Planning**: Threshold: >1 file, >20 lines, structural changes. Trivial = direct edit.
- **Context**: Summary logs before large jumps. Reset context when tasks shift. Maximize token efficiency.
- **Rules**: Always use absolute paths. Open-source first (budget). GDPR by default (GE location). Disclose/escalate evidence conflicts.
- **Logging**: Update Mistake Log in local CLAUDE.md for regressions/errors.

## 6. Tool & Capability Directives
- **Discovery**: Proactively find/install MCPs (fetcher, memory, grep-app, browser).
- **Execution**: Verify files/API before claiming. Use `grep/find/read` for unknowns. No assumptions.
- **Evidence Management**: Persist discovered SE patterns, clinical facts, and peer-reviewed citations in memory.

---

## 7. Quality Gates (Presubmission Checklist)
Before task completion:
- [ ] Root cause identified/fixed (no patches). Edge cases handled.
- [ ] Evidence documented (§3 Trail) with Confidence/Applicability.
- [ ] Config externalized. No hallucinations. verified against codebase.
- [ ] Code follows SOLID, DRY, KISS, YAGNI, ETC.
- [ ] Error handling explicit/meaningful. Security (input/auth) verified.
- [ ] Linting (zero warn/err). Tests written/updated. DB migrations forward-only.

## 8. Practical Engineering Rules
- **Lint/Format**: Zero tolerance for warnings. ESLint strict. Prettier on save. Git diff review before commit.
- **Git**: Atomic commits (Conventional). Atomic branches. No secrets in git (gitignore/env).
- **Env/Config**: Separate Env (Dev/Prod). `.env.example` templates. No hardcoded URLs. Fail loudly on missing config.
- **Dependencies**: Pin exact versions. Audit CVEs. Evaluate size/types/license. Wrap 3rd party.
- **API**: Versioning (/v1/). Server-side validation. Idempotency. Correct HTTP codes. No stack traces.
- **Performance**: Measure (Profiler/Lighthouse). No premature optimization. Index DB. Tree-shake JS.
- **Accessibility/UX**: WCAG 2.1 AA (baseline). Semantic HTML. Keyboard nav. Loading/Error states.
- **Docs**: README (New dev run in 15min). ADRs for archi choices. OpenAPI for REST.
- **Mobile**: Deep links registered. Offline-first. Lazy-load assets. Contextual permissions.
