# May 21 Status Meeting III, Q&A Prep

**Private prep document for Hammad** (presenter). Anticipates likely questions from Prof. Hacker, Prof. Gloor, and the coordinators (Janine, Simon, Peter). Three new categories below (Hacker-flavored, Gloor-flavored, General) added 2026-05-21 with technical depth; older thematic Q&A retained at the bottom.

Each question has 3 layers:

- **Short answer**: one sentence Hammad can read aloud cold and sound competent
- **Backup detail**: 2 to 3 sentences with concrete numbers if asked to elaborate
- **If pressed**: deepest defensible answer with project-specific data

If Hammad blanks on a deep technical question, the escape hatch is always: *"I'll check with the team and follow up by email."* Better than guessing wrong.

---

## Category 1: Hacker-flavored (network science, trust, engagement)

### Q-H1: Why Granger causality and not transfer entropy or mutual information?

**Short answer**: Granger gives us a parametric significance test that statsmodels supports out of the box, plus a clean lag interpretation.

**Backup detail**: Mutual information is symmetric so it can't give direction, which is the whole point of "who-leads-whom". Transfer entropy is directional but non-parametric, slower to compute, and harder to justify a null model for. Granger's F-statistic plus circular-shift null is the best tradeoff for our sample sizes and explains-itself to reviewers.

**If pressed**: We are running standard Granger as primary with ordinal-pattern Granger (Zanin 2021) as a robustness check in Sprint 3. If the two variants disagree on the directionality of a given edge in more than 10 percent of pieces, that is a finding in itself and we will report it.

### Q-H2: What's the null model and why circular-shift?

**Short answer**: 200-shuffle circular shift, which preserves within-stream autocorrelation that an i.i.d. shuffle would destroy.

**Backup detail**: i.i.d. shuffling on RMS envelopes would inflate the apparent significance because real choir audio has strong autocorrelation at the syllable scale. Circular shift slides one stream relative to the other by a random offset, so within-stream structure stays intact and only cross-stream timing is broken.

**If pressed**: We compute the empirical p-value as the fraction of shuffled F-statistics that exceed the observed F. With 200 shuffles, the smallest reportable p_null is 0.005, which is sufficient for our p < 0.05 threshold. Sprint 3 increases shuffles to 500 for the full corpus.

### Q-H3: Why is graph density 0.92 meaningful and not just an artifact of small N?

**Short answer**: For 4 nodes there are 12 possible directed edges. 11 came back significant against the null, so density is high because the null model rejects most random shuffles, not because the test is loose.

**Backup detail**: This recording is an in-person co-located quartet with no network latency. We expect everyone to listen to everyone, so a dense graph is the predicted outcome. The interesting question is what the density becomes for Zoom-only choir performances. We hypothesize density drops as latency rises, which is part of H2.

**If pressed**: We will report density distributions across multiple pieces, not single-piece point estimates. With 5 pieces in Sprint 3 we get a mean and CI. With the full Tier-2 corpus we get statistical power for the H2 comparison.

### Q-H4: Why eigenvector centrality for the most-central voice?

**Short answer**: Eigenvector centrality captures "influence on influencers", which matches the musical intuition that the soprano sets the temporal anchor for the whole quartet.

**Backup detail**: Degree centrality would just count edges and ignore weight; betweenness centrality measures structural brokering, which is not what we want here. Eigenvector accounts for the recursive structure of influence and works well on weighted directed graphs like ours.

**If pressed**: For Sprint 3 we will compute all 4 standard centrality measures (degree, betweenness, closeness, eigenvector) and report which one most consistently picks out the lead voice as judged by the score. If they disagree, that is a finding.

### Q-H5: How will you compare influence graphs across pieces of different lengths?

**Short answer**: Per-edge significance is length-invariant once we normalize for the number of windows. The graph metrics we report (density, modularity, centrality) are scale-invariant.

**Backup detail**: We run Granger in sliding windows of 10 seconds with 5-second overlap. Number of windows scales with piece length, but we report metric averages and CIs, not raw F-sums. Edge weights are normalized to maximum F per piece before cross-piece comparison.

**If pressed**: Different pieces also have different intrinsic structures (homophonic vs polyphonic), so we will stratify the cross-piece comparison by piece-type. This is in the Sprint 3 plan but we have not surfaced it on the slide.

### Q-H6: What sample size do you need for H2 statistical power?

**Short answer**: Per the Apr-17 plan, we need at least 5 pieces per regime to get a Cohen's d power of 0.8 at alpha 0.05.

**Backup detail**: H2 compares topology metrics between low-latency and high-latency regimes. The Tier-3 controlled latency injection lets us get matched-piece comparisons, which is more powerful than between-piece. Sprint 3 produces 5 Dagstuhl pieces in their natural state; Tier-3 then injects 4 latency regimes per piece, giving us 20 paired comparisons.

**If pressed**: This is the strongest case for Tier-3 controlled injection. Natural YouTube comparisons confound piece, performers, and latency. Tier-3 isolates latency as the only varying factor, dramatically reducing the sample size needed for the same effect.

### Q-H7: Is COP-GC just standard Granger with extra steps?

**Short answer**: No, COP-GC is non-parametric and handles non-linear dependencies that linear Granger misses.

**Backup detail**: Zanin 2021 shows that standard linear Granger underestimates causal strength when the true dynamics are non-linear, which is common in musical timing. COP-GC bins the time series into ordinal patterns and computes the predictive information transfer on those. It costs more compute but catches dependencies the linear test misses.

**If pressed**: For Sprint 3 we run both variants on the same 5 pieces and report the rank-order correlation between their edge weights. If r > 0.7 we recommend standard Granger going forward (faster, well-known). If r < 0.7 we keep both and report both.

---

## Category 2: Gloor-flavored (alchemical pipeline, Honest Signals, COIN)

### Q-G1: How does your alchemical-stage diagram map to Pentland's Honest Signals?

**Short answer**: The Citrinitas stage operationalizes Pentland's four honest signals (influence, mimicry, activity, consistency) on choir-specific time series, then aggregates them into V(t).

**Backup detail**: Pentland defines honest signals as unconscious behavioral cues that predict outcomes regardless of conscious content. For choir we map them as follows: influence = Granger-causal direction (N(t)); mimicry = pose synchrony between singers (part of V(t)); activity = motion intensity from MediaPipe (V(t)); consistency = stability of body posture over time (V(t)).

**If pressed**: We are using Pentland's framework as the theoretical anchor for V(t), but the operationalization is novel for music-domain data. The paper will be explicit about which mappings are direct and which are adaptations. The relevant section is in PROJECT_GUIDE.md §11.1.

### Q-G2: What COIN archetype did the team get from the Virtual Mirror?

**Short answer**: All 4 human members classified as Tree Hugger on the primary archetype, which matches our self-stated conscientious stance in the team brief.

**Backup detail**: Tree Hugger in the SocialCompass framework signals conscientiousness, sustainability orientation, and ethical care. For us that aligns with the design choices we already made: no self-recording, public-only YouTube under §60d UrhG, DPIA filed before extraction, mp4 deletion after feature extraction.

**If pressed**: Secondary archetypes spread across Fatherlander, Nerd (38-44%), and Spiritualist. The Nerd score range is tight which suggests the team has similar problem-solving styles. Lower-scoring archetypes are not reported by SC Chat Analyzer because the sample size of 5 participants is small for fine-grained discrimination.

### Q-G3: Where do Honest Signals show up in V(t) specifically?

**Short answer**: Three derived features per singer per frame: shoulder rise (breathing proxy), head sway (postural engagement), and trunk lean (intentional motion).

**Backup detail**: MediaPipe Pose gives us 33 keypoints with x/y/z/visibility. We pick a subset: nose, shoulders, hips. From those we compute shoulder rise as the vertical midpoint of left and right shoulders (a proxy for breath); head sway as the horizontal nose position relative to shoulder midpoint; and trunk lean as the angle of the shoulder-to-hip line vs vertical. These are the Pentland mimicry and consistency axes adapted for choir context.

**If pressed**: The breath proxy specifically maps to Pentland's "activity" signal, the body sway maps to "mimicry" when computed pairwise between singers, and head stability over time maps to "consistency". The Sprint 3 calibration study quantifies how reliably MediaPipe captures these compared to OpenPose.

### Q-G4: How does the Citrinitas-to-Rubedo transition manifest in the dashboard?

**Short answer**: The dashboard timeline shows A(t), V(t), N(t), and E(t) as four lines. Citrinitas is the per-pair coupling curves emerging; Rubedo is the composite E(t) that integrates them into one score plus the regime-contrast comparison.

**Backup detail**: In the wireframe we have, the top panels show the raw video with pose overlay (Albedo from Nigredo). The middle shows the per-pair coupling timelines (Citrinitas patterns emerging). The bottom shows the E(t) composite line and the network animation (Rubedo, the magnum opus).

**If pressed**: The "transition" is meant to be readable in the visualization itself. A reviewer should be able to point at any moment in the video and see how raw motion data became a coordination score. That readability is the design goal, and the alchemical framing is the structure we used to organize the panels.

### Q-G5: Why (A+V+N)/3 and not weighted?

**Short answer**: Equal weighting is the honest baseline because we have no prior data telling us which signal matters most. Sprint 3 fits the weights from data.

**Backup detail**: A weighted composite requires either (a) theoretical priors which we don't have for music, or (b) empirical fits which require labeled coordination outcomes. We don't have ground-truth coordination labels, so we start with the equal-weight composite as the unbiased baseline. H3 explicitly tests whether the visual signal adds explanatory power on top of audio alone, and the result of that test informs whether weighting V higher is justified.

**If pressed**: There is an argument for weighting A higher because musicians are trained to coordinate on audio cues first. We are open to revisiting after H3 results, and the paper will include a sensitivity analysis with several weighting schemes.

---

## Category 3: General (any reviewer / supervisor)

### Q-X1: Why did Sprint 2 dates slip 9-17 days?

**Short answer**: The timeline assumed parallel WP execution; in practice Sprint 2 ran serially because all four work packages share the same Tier-2 data dependency, and the Tier-2 download was bandwidth-limited.

**Backup detail**: Tier-2 Dagstuhl was the prerequisite for WP1 audio (which is the input to WP3 network). At our connection bandwidth the 5.1 GB download took an hour with retries. Until Tier-2 landed May 17, downstream work was blocked. We could have re-scoped Sprint 2 mid-sprint around May 8 when this became clear, but we waited until the May-21 deadline forced it. The retro on slide 8 captures this and commits to mid-sprint re-scoping going forward.

**If pressed**: The slip was on intermediate dates, not the Sprint 2 boundary. All milestones landed before today. The overall scope actually expanded compared to the original Sprint 2 plan (WP2, WP3, WP4 milestones originally scheduled for May 22 and May 31 were pulled forward and shipped in draft form). The slip is in dates, not deliverables.

### Q-X2: What's the contingency if MediaPipe doesn't validate against OpenPose?

**Short answer**: We fall back to OpenPose for the full Tier-1 corpus. The Sprint-3 calibration study is the decision trigger.

**Backup detail**: The calibration study computes Pearson correlation of head-sway between MediaPipe and OpenPose on 3 randomly sampled videos. If r ≥ 0.70 we keep MediaPipe (faster, cleaner Python integration). If r < 0.70 we switch to OpenPose for the production pipeline. OpenPose is the published reference for body keypoint extraction in HCI research, so the fallback is defensible.

**If pressed**: This is Risk R3 in the original PROJECT_GUIDE. OpenPose requires Docker which adds infrastructure complexity, which is why we prefer MediaPipe by default. The fallback decision is binary and triggered by a quantitative threshold, not subjective preference.

### Q-X3: GDPR / DPIA status and timeline?

**Short answer**: DPIA outline filed with the Bamberg DPO this morning. Full document due before June 14, which is when large-scale extraction starts.

**Backup detail**: GDPR Art. 9(2)(j) gives us the research exception for processing biometric data (face landmarks, pose keypoints). Combined with §60d UrhG (German text-and-data-mining right) and EU DSM 2019/790 Art. 3, we have the legal basis for Tier-1 YouTube extraction. The DPIA covers data categories, retention (mp4 deleted after feature extraction), and pseudonymisation (singer_NN IDs, no names).

**If pressed**: One open jurisdictional question we are escalating: whether §60d UrhG covers arXiv deposit, given arXiv is US-hosted. Bamberg legal desk is reviewing. Worst case we move the deposit to a DE-hosted preprint server.

### Q-X4: Why YouTube and Dagstuhl, not self-recorded data?

**Short answer**: Self-recording was explicitly forbidden at project outset for three reasons: ethics overhead, self-selection bias (we are not trained singers), and original scope constraint.

**Backup detail**: Self-recording would require IRB review, written consent management, and we would still get a sample of 4 untrained singers which would not generalize. Public YouTube gives us a large quantity of real-world choirs (hundreds of candidates), and academic multitrack datasets like Dagstuhl give us the ground-truth audio per-singer that YouTube cannot.

**If pressed**: Tier-3 controlled latency injection on the Tier-2 data is actually better science than natural YouTube comparisons. We know exactly what latency profile we injected, which gives us perfect ground truth. The natural YouTube data complements this as descriptive evidence and visual-signal sanity check.

### Q-X5: What if H1, H2, and H3 all fail?

**Short answer**: A negative result is a publishable finding. It bounds the claim that E(t) discriminates latency regimes.

**Backup detail**: We pre-registered the hypotheses with effect-size thresholds (Cohen's d ≥ 0.5; p < 0.05 vs null; ΔR² ≥ 0.10). If results fall below these, we report the failure honestly. That tells the field: with this specific metric formulation and this specific corpus, latency does NOT predict coordination as we hypothesized. That is informative for NMP tool design decisions.

**If pressed**: The COIN community has a strong tradition of reporting null results. Gloor's own work on the Honest Signals framework includes several failed transfers between domains. Honest negative reporting is part of the methodology.

### Q-X6: What's your reproducibility story?

**Short answer**: Every Tier-2 dataset is MD5-verified vs Zenodo. Every Tier-1 video has a SHA-256 in our manifest. Code dependencies are pinned in uv.lock, and feature outputs are parquet with schema metadata.

**Backup detail**: A future reader can clone the repo, run uv sync against uv.lock, re-download the same datasets, verify hashes, and re-run the pipeline. The fresh-clone smoke test runs in under 12 minutes cold cache on Windows 11. The reproducibility appendix of the paper will reference exact commit SHAs.

**If pressed**: We are following the ACM Artifact Review and Badging guidelines (artifacts available + artifacts evaluated). The repo will be deposited on Zenodo at paper submission with a DOI for citation. Long-term archival is not yet committed but is on the Sprint-6 todo list.

### Q-X7: How do the 4 team members divide work?

**Short answer**: Each member has a primary work package (audio, video, network, dashboard) plus shared responsibility for the paper and presentations.

**Backup detail**: WP1 audio and integration is led by one member, WP2 video by another, WP3 network by a third, WP4 dashboard and figures by the fourth. Sprint coordination is via WhatsApp (which the SC Chat Analyzer just confirmed is working well, as shown on slide 9). Presentations rotate between team members; today I'm presenting on behalf of the team.

**If pressed**: Sprint 2 was unusually serial because of the data dependency on Tier-2. Sprint 3 should re-parallelize naturally now that Tier-1 and Tier-2 are both on disk. The weekly 15-min Monday check-in is our process change to keep this from recurring.

### Q-X8: What's the publication venue?

**Short answer**: 8-12 page paper in IEEE or LNCS format, target submission July 31. Specific venue is still being decided by the team.

**Backup detail**: We are looking at COINs annual conference (the seminar's home venue), ISMIR (music information retrieval), and ACM CHI as candidate venues. The choice depends partly on whether our results are stronger on the network-science side (Hacker's pillar, COINs/ASONAM) or the human factors side (Gloor's pillar, CHI/CSCW).

**If pressed**: We are happy to follow supervisor guidance on venue. If both supervisors have a preference today, that helps us write toward the right reviewer audience.

### Q-X9: How will you handle Tier-1 videos that get taken down mid-project?

**Short answer**: We have SHA-256 hashes for all 29 videos and the mp4s are on disk for Sprint-3 processing. If YouTube takes one down, our processing can still complete; we report which videos were live at scrape time vs at re-verification.

**Backup detail**: We learned this lesson the hard way. The initial Perplexity scrape returned 24 URLs; 2 were taken down between scrape and validation. We documented them in the manifest with status `url-unavailable` for transparency. The supplementary curation rebuilt the Zoom stratum to 9 verified URLs, all of which we have SHA-256 hashed copies of.

**If pressed**: The paper will report the corpus state at scrape time and at processing time. If videos disappear between scrape and the paper deadline we will note it. This is consistent with how prior art on YouTube corpora handles temporal volatility.

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
