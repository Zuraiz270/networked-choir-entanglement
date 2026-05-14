
# Apr 30 Status Meeting II, Speaker Script

**Project 8 · Entanglement in Online Choir · 2026-04-30 · 14:00 CET**

> Companion to [apr30_deck.md](apr30_deck.md). One presenter (Zuraiz). The Q&A prep bank, terminology cheat sheet, and presenter doubts live in [apr30_qa_prep.md](apr30_qa_prep.md). The deck follows Prof. Gloor's Apr 14 email rubric: Team, Goals (Scope), Dataset Strategy, Project Plan, Next Iteration, Way of Working.

---

## T-30 minute checklist

- [ ] Deck open and on the right screen (rendered version, not raw markdown).
- [ ] Backup PDF of the deck on a USB stick or local folder.
- [ ] Camera on, mic tested. Battery above 50% or charger plugged in.
- [ ] [apr30_qa_prep.md](apr30_qa_prep.md) open in another tab for Q&A reference.
- [ ] [PROJECT_GUIDE.md](PROJECT_GUIDE.md) open in a third tab (you may reference the data tiers, formula caveat, or limitations).
- [ ] Glass of water within reach. Phone on silent.
- [ ] Read the closing line out loud once before joining the call.

## Tone

Confident, not cocky. You have done the homework. Acknowledge what is missing, and frame open questions as asks for input rather than gaps. Their feedback today is the deliverable, not your slides.

You are presenting to two senior researchers in a 15-minute slot. Land at 7 to 8 minutes spoken; the rest is theirs.

---

## Slide 1: Title (0:00 to 0:30)

> "Good afternoon. Project 8, Entanglement in Online Choir. I am Zuraiz, presenting on behalf of the team. We are four members from Uni Bamberg. Our supervisors are Prof. Hacker on the Bamberg side and Prof. Gloor as COIN seminar lead. Thank you for the meeting slot."

Move quickly. Do not dwell on the title slide.

## Slide 2: The Team (0:30 to 1:10)

> "Our team has four members, all M.Sc. students at Uni Bamberg."

Gesture at the 4 portraits left to right.

> "Three of us, Hammad, Hassan, and myself, came from the chapter team. Kumaran joined at the project signup."

Then point at the archetype bars.

> "The archetype bars are here because the May 21 Virtual Mirror asks us to analyse our own team communication. For today, the important point is simply that the team is complete, role allocation is stable, and the self-analysis deliverable is already planned."

Do not dwell on the archetype percentages unless asked. The scientific contribution is the choir dataset and measurement strategy, not our team profile.

## Slide 3: Goals (Scope) (1:10 to 2:50)

This is the most important slide for credibility. Slow down.

> "Our research question is simple. When a choir sings together over the internet, can we put a number on how well coordinated they are? This question comes from a gap between two literatures. NMP studies tell us a lot about latency and tool quality, while coordination research tells us a lot about group flow, but choirs give us something unusually concrete: an acoustic outcome that can be measured in milliseconds."

Pause one beat.

> "We are building a proposed number for that: E(t), the Entanglement Index. It combines audio synchrony, body movement, and a network of who influences whom."

Then be explicit about provenance.

> "The formula is not copied directly from an online-choir paper. The term and high-level idea come from Prof. Gloor's entanglement work on team communication, and the visual part is grounded in Pentland's Honest Signals. But the original entanglement formula was validated on email rhythms over 7-day windows, not continuous music streams. So our choir version is a domain adaptation, and H1, H2, and H3 are the validation tests."

Point at the three hypotheses.

> "We have framed three falsifiable hypotheses. H1 says low-latency tools like Jamulus or SoundJack score higher on E(t) than high-latency tools like Zoom. H2 says the influence network changes shape with latency, from democratic at low latency to leader-dominated at high latency. H3 says adding body-movement signals on top of audio improves the metric by at least 10 percentage points of explained variance."

> "Either outcome is publishable. A null result tells the field that the latency dichotomy is too crude or our metric is mis-specified. A positive result gives the field its first quantitative coordination meter."

Brief eye contact with both supervisors.

## Slide 4: Dataset Strategy (2:50 to 4:15)

This is likely to draw Prof. Gloor's attention. Keep it concrete: what we have, what we will collect, and what each tier can and cannot prove.

If you feel confused, remember this one line before speaking: **Tier 1 is real-world but messy; Tier 2 is clean but academic; Tier 3 is controlled and experimental.**

> "The dataset strategy has three tiers plus one seed set. The seed set is Tier 0: five Jamulus or Choir@Home URLs from Prof. Hacker. We already have those. They are not the main dataset and we should not pretend they are. Their job is to show us what good candidate videos look like and to guide our YouTube search terms and inclusion rules."

Point at Tier 1.

> "Tier 1 is the real-world dataset: 20 to 30 public YouTube virtual-choir videos, hand-curated by May 15. With this tier, we extract what we can see: body movement, mouth opening, visible synchrony, and some ensemble-level audio descriptors. This tier is useful for H3, the question of whether visual signals add anything. But it is not enough for per-singer audio or who-leads-whom analysis, because YouTube gives us a finished mixed stereo track. We cannot reliably separate singer 1, singer 2, and singer 3 from that final mix."

Point at Tier 2.

> "Tier 2 is the clean audio dataset: academic multitrack recordings such as Dagstuhl ChoirSet, ESMUC, and ChoralSynth. Here each singer has a separate track, so now we can measure individual pitch, onset timing, pairwise synchrony, and Granger causality. This is the tier that makes A(t), N(t), and the directed influence graph possible."

Point at Tier 3.

> "Tier 3 is not a new external dataset. We create it from Tier 2. We take the clean multitrack recordings and artificially add low-latency conditions, Zoom-class latency, jitter, and packet loss. Then we recompute E(t). This is our cleanest H1 test because we know the exact latency profile we injected. On YouTube, we usually do not know the true network conditions."

End with the guardrail.

> "We are not self-recording and not recruiting choirs in this project phase. That avoids ethics overhead and keeps the dataset strategy reproducible: public videos, published datasets, manifest, hashes, derived features."

If they ask for it in one sentence, say:

> "Tier 0 gives seed examples, Tier 1 gives real-world video for visual coordination, Tier 2 gives clean per-singer audio for audio and network analysis, and Tier 3 gives controlled latency experiments to test whether E(t) distinguishes Zoom-class from low-latency conditions."

## Slide 5: Overall Project Plan (4:15 to 5:15)

> "We split the 14 weeks from kick-off to final paper into three phases. Phase 1, scope and scaffold, ran from April 16 to today. Phase 2, build and analyse, runs May 1 to July 7. Phase 3, synthesise, runs July 8 to July 31."

Point at the status meeting calendar.

> "Seven status meetings, including today. The next one, on May 21, is the Mirror Session. Final presentation on July 23, paper due July 31."

Walk the milestone table top to bottom, but do not read every row.

> "Phase 1 closes today with the research question, hypotheses, data tiers, and repo scaffold in place. The important honest status is: we have seed URLs, but we have not yet collected the analysis corpus or extracted features. That starts in Phase 2."

Pause.

> "Zero feature code yet. The audio pipeline lands May 8. We are on schedule. No critical blockers."

This slide is the credibility slide. The credibility comes from being precise, not from listing how much homework was done.

## Slide 6: Plan for the Next Iteration (5:15 to 6:30)

> "Sprint 2 runs from today, April 30, to the next status meeting on May 21. Three weeks. Four work packages, each ending in a defined deliverable."

Walk the table top to bottom.

> "First, the audio pipeline. We pull the academic multitrack datasets, Dagstuhl ChoirSet, ESMUC, and ChoralSynth, to disk; run pitch tracking and onset detection. Output: per-singer feature parquet for five pieces by May 8."

> "Second, the video pipeline. We run MediaPipe Pose and FaceMesh on the first ten YouTube virtual-choir videos and calibrate against a published pose ground truth. Output: pose parquet plus a one-page calibration note by May 22."

> "Third, the curated YouTube corpus and GDPR. Hand-curate 20 to 30 virtual-choir videos with no post-production edits. File the GDPR DPIA outline with the Bamberg data-protection officer, because face-mesh landmarks count as biometric data under Article 9. Output: corpus manifest with SHA-256 hashes by May 15, DPIA outline by May 21."

> "Fourth, the Virtual Mirror, which is the seminar requirement for May 21. We export our team WhatsApp chat, run it through SocialCompass, and classify the team archetype with all four members. Output: mirror write-up presented at VS#3."

Dataset-specific phrasing if asked "what exactly happens next":

> "In the next phase, we first put Tier 2 on disk and build a manifest. Then we curate Tier 1 manually, with inclusion and rejection reasons. Once Tier 2 is usable, we create Tier 3 by injecting latency and jitter into those clean tracks. Only after that do we compute the full E(t) pipeline."

## Slide 7: Way of Working (6:30 to 7:20)

> "Three pillars. Cadence, sync, toolstack."

Walk left to right.

> "Cadence: 3-week sprints aligned to status meetings, each ending in a defined artefact, with a pre-VS review 1 to 2 days before. Sync: weekly 30-minute team meeting, daily async status posts, channels are WhatsApp and GitHub Issues, plus a weekly check-in with Prof. Hacker. Toolstack: Python, Git and GitHub Actions for CI, Markdown as the source of truth, method notes in Obsidian, and peer review through pull requests."

Pause.

> "One note: the team WhatsApp group, set up per Prof. Gloor's April 14 email instruction, is also our input data for the Virtual Mirror on May 21. So the way we communicate becomes the data we analyse on ourselves."

That last line is a nice callback for Gloor. Pause for one beat.

## Slide 8: Thank you (7:20 to 7:30)

> "That covers our team, scope, dataset strategy, project plan, next iteration, and way of working. Thank you for listening. I am happy to take your questions."

End there. Hold the silence for five seconds. Researchers process before they speak.

---

## Pacing variants

If you are running long, the Q&A is what matters. Do not steal time from it.

### 5-minute compressed (more Q&A, less talking)

| Slide | Action                                                                                          |
| :---- | :---------------------------------------------------------------------------------------------- |
| 1     | "Project 8, Entanglement in Online Choir. Four-person Bamberg team." 15 sec.        |
| 2     | "Team complete, roles stable, Virtual Mirror planned." 20 sec.                     |
| 3     | RQ origin + E(t) provenance + three hypotheses by name only. 75 sec.                |
| 4     | Dataset tiers: seed URLs, YouTube visual, multitrack audio/network, latency injection. 75 sec. |
| 5     | Three phases, today closes Phase 1, audio lands May 8. 40 sec.                      |
| 6     | Read the four work-package row labels and the first deliverable date of each. 40 sec. |
| 7     | "Three-week sprints, weekly Hacker check-in, GitHub/Markdown workflow." 25 sec.     |
| 8     | "Thank you. Questions?" 10 sec.                                                     |

### 7-minute standard (default)

Cover all 8 slides as written. Compress slide 5 to 45 seconds (the timeline is on screen, do not read it).

### 8-minute full

Cover all 8 slides as written. Most likely if Q&A is light or supervisors join late.

---

## Top 5 Q&A reminders (full bank in apr30_qa_prep.md)

1. **"What dataset are you using?"** Tier 0 seed URLs already received; Tier 1 YouTube for visual signals; Tier 2 academic multitrack for per-singer audio/network; Tier 3 latency injection for clean H1 ground truth. One line: real-world messy, clean academic, controlled experimental.
2. **"Is E(t) from a paper or made up?"** It is a proposed music-domain adaptation. Gloor's entanglement work gives the conceptual lineage; the original formula was email-based, so our A/V/N operationalisation must be validated by H1-H3.
3. **"Where did the research questions come from?"** From the literature gap: NMP studies latency/tools, coordination research studies group flow, choirs provide an objective acoustic outcome. Hacker's influence-graph lens and Gloor's Honest Signals/COIN lens shaped H2-H3.
4. **"Show me the directed influence graph."** It lives in WP3, due May 31 from Dagstuhl. We can send you the SVG the moment it lands.
5. **"What if results are null?"** Null is publishable. If H1 fails, the latency dichotomy is too crude. If H3 fails, the visual contribution is below our resolvable threshold at this sample size.

For anything you do not know: **"That is a good question and I have not tested it yet. Let me come back in the next iteration with a real answer rather than a guess."** Pull out a pen, write it down visibly. The act of writing it down signals respect.

---

## After the meeting (T+30 min)

- [ ] Write down every question they asked, in `onsidian vault/OSN-M/raw/apr30_meeting_notes.md`, before you forget.
- [ ] Send a 3-line follow-up email to both supervisors within 2 hours: thank them, list the asks they made of you with deadlines, attach the deck PDF.
- [ ] Append a `query` entry to `wiki/log.md` summarising decisions and follow-ups.
- [ ] Update `PROJECT_GUIDE.md` §4 status if the meeting changed any project state.
- [ ] If they assigned new work, add it to the next iteration deliverable list.

## A reminder

You have a defensible plan. The key today is to be precise about the dataset state: seed URLs are in hand, the real analysis corpus starts next, and the formula is a proposed adaptation that the project will test. Walk in with the frame that this meeting is the supervisors' input on the project, not the project succeeding or failing.
