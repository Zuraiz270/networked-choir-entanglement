# May 21 Status Meeting III, Q&A Prep

**Private prep document.** Anticipates likely questions from Prof. Hacker, Prof. Gloor, and the coordinators (Janine, Simon, Peter). Organised by theme.

---

## Theme 1: The Slippage

### Q-S1: "Why did Sprint 2 slip across the board?"

**Short answer**: the timeline assumed parallel team execution. In practice it became serial single-executor work, and a serial path through the same scope takes proportionally longer.

**Longer answer if pressed**:

- Original Sprint-2 plan distributed WP1, WP2, WP3, WP4 across four team members.
- Effective allocation collapsed to one executor in week 1. Other team members continued chapter-team obligations.
- Rather than fake parallelism, we rescoped Sprint 3 to match real throughput.
- Sprint 3 dates already reflect the rescoped pace, not the optimistic original.

**Do NOT**: blame teammates by name. Frame as a planning error, not a personnel issue.

### Q-S2: "Are we still on track for the Jul 31 final paper?"

Yes — slippage is on the Build phase, not Synthesise. Three-week buffer between Jul 7 paper draft v1 and Jul 31 submission absorbs further slip. If E(t) results come in by Jun 30 we have 4 weeks for writing, which is sufficient for an 8–12 page paper.

### Q-S3: "How will you make up the lost time?"

We are not making it up — we are absorbing it into the rescoped Sprint 3. The original plan over-promised on parallel velocity. The rescope is realistic. If the rescope holds, we hit Jul 31. The risk we are managing is *further* slip in Sprint 3, not the slip that already happened.

---

## Theme 2: Technical Status

### Q-T1: "Is the YouTube DSP blocker resolved?"

No — it is *acknowledged and architected around*, not resolved.

- Mixed-stereo YouTube audio cannot yield per-singer features using current open-source DSP (librosa pyin is monophonic; Demucs separates instruments not vocal stacks).
- We accepted this in Apr-17 plan v2.1 and the Apr 30 deck. Tier-1 YouTube is visual-only now.
- All per-singer audio features and Granger networks come from Tier-2 multitrack (Dagstuhl ChoirSet) and Tier-3 controlled latency injection.
- This was not a regression in Sprint 2; it was a design decision before Sprint 2 started.

### Q-T2: "Why Dagstuhl and not also ESMUC / ChoralSynth?"

Dagstuhl is verified-accessible (Zenodo, CC-BY-4.0, MD5 in hand). ESMUC and ChoralSynth were listed in the Apr-17 plan as candidates, but their access status is unverified. We started with the dataset we could definitely get, and we will add the others if the licences and download paths check out.

This is also Q-T2 to throw to Hacker: does she have direct access to ESMUC / ChoralSynth materials?

### Q-T3: "Show us the A(t) figure"

If figure is in the deck: walk through the two singer tracks, the cross-correlation peak, and what the peak position tells us about who is leading whom in this single quartet sample. Caveat: this is n=1, not yet a statistical claim.

If figure is not in the deck: "The figure is in `data/figures/` — happy to share-screen if useful. We chose to keep slide 3 light to leave room for the rescope discussion."

### Q-T4: "What is your validation strategy for E(t)?"

H1, H2, H3 *are* the validation. They are pre-registered hypotheses with effect-size and p-value targets:

- H1: Cohen's d ≥ 0.5 on ≥2 of 3 sub-scores between low-latency and high-latency regimes
- H2: topology metrics differ at p < 0.05 vs 200-permutation null
- H3: visual features add ΔR² ≥ 0.10 over audio alone

A null result is publishable and informative — it bounds the claim that E(t) discriminates latency regimes.

---

## Theme 3: GDPR / Legal

### Q-L1: "What is the DPIA status?"

Outline filed with Bamberg DPO this morning. Full document due before Jun 14 large-scale extraction. DPIA covers FaceMesh landmarks under Art. 9(2)(j) research exception + Art. 89 safeguards (pseudonymisation, aggregation, raw-mp4 deletion within 72h).

### Q-L2: "Are you sure §60d UrhG covers your YouTube use?"

For DE-jurisdiction work, yes — §60d UrhG plus EU DSM 2019/790 Art. 3 grant statutory TDM rights on lawfully accessible sources for non-commercial scientific research, overriding platform ToS.

Open question we are escalating to Bamberg legal: whether the right survives arXiv deposit (US-jurisdiction repository). Falls under our problems list on slide 7.

### Q-L3: "What if a singer in a YouTube video asks to be removed?"

Right to erasure under Art. 17 GDPR applies. Our process: raw mp4 deleted within 72h of feature extraction anyway, so the only retained data per video is aggregate features keyed by anonymised `singer_01` IDs. Re-identification from those features is not feasible without the source video. We commit to removing any singer-level feature row on written request to the project email.

---

## Theme 4: Team and Process

### Q-P1: "Is your team functional?"

Yes. Sprint 2 had a coordination issue, not a team issue. The team is taking the retrospective seriously, the one process change on slide 5 came from that conversation, and we are committing to it.

### Q-P2: "Is Zuraiz doing all the work?"

Honest answer: I am the primary executor on the technical implementation right now, by mutual agreement within the team during Sprint 2. Other members contribute to presentations, retrospective input, and the Virtual Mirror. We are revisiting allocation in Sprint 3 based on the retro.

**Do NOT** call other team members out by name. Frame this as an internal allocation, not a performance issue.

### Q-P3: "Why was no one in Sprint 2 video meetings?"

Frame: weekly syncs continued (Wednesday 30-min team sync per Way-of-Working slide). Spinning up parallel WP work proved harder than expected; we under-estimated the ramp-up cost on first-time scientific Python work.

---

## Theme 5: Virtual Mirror

### Q-M1: "What does your team's archetype mean for your project work?"

Reference the SC Chat / Symbiont archetypes from Apr 30 deck (Tree Hugger / 3 Ants / 1 Capybara). If May-21 SC results confirm: tight-knit collaborators with one steady-pace coordinator. Risk pattern for Ant-dominated teams is over-deferral to a single coordinator, which matches the Sprint-2 single-executor pattern we observed. The retro action is to redistribute deliberately.

If May-21 SC results contradict: report the contradiction openly and ask what changed in the chat patterns vs the chapter-team baseline.

### Q-M2: "Did SC Chat / Symbiont work as expected this time?"

If yes: "Same protocol as block course, smooth run." If access issues: "We had to {fallback method}, results below should be treated as preliminary." (See risks section of plan: fallback is manual NetworkX on pandas-parsed WhatsApp export.)

---

## Theme 6: Coordination Questions for the Room

These are the three questions on slide 7, restated for our own reference:

1. **To Prof. Hacker**: Do you have access to ESMUC or ChoralSynth Tier-2 multitrack data beyond Dagstuhl?
2. **To both supervisors**: Influence-graph visual aesthetic preference — minimalist matplotlib or polished Cytoscape/Gephi?
3. **To coordinators**: Is the Jul 23 final presentation in-person at Bamberg, or remote?

---

## Things to NOT bring up unprompted

- Internal team allocation debates by name
- Specific dollar/euro figures (this is a course project, not a grant)
- Comparisons to the COIN sibling team's progress
- Personal opinions on supervisors' research framings (Honest Signals vs other coordination theories)

---

## Cheat sheet: numbers at fingertips

- **Tier-2 size**: 5.1 GB Dagstuhl
- **Tier-1 corpus**: {COUNT, fill after T2} videos
- **WP1 deps installed**: librosa 0.10.2, numpy 1.26.4, scipy 1.13.1
- **Repo commits since Apr 30**: {COUNT, fill before meeting}
- **E(t) hypothesis thresholds**: Cohen's d ≥ 0.5; p < 0.05 vs 200-perm null; ΔR² ≥ 0.10
- **DPIA filing date**: 2026-05-21
- **Next milestone**: VS#4 on Jun 11
