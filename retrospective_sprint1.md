# Sprint 2 Retrospective (Apr 30 → May 21)

**Format**: async reflection across the team WhatsApp + structured write-up.
**Participants**: Zuraiz, Hammad Anwar, Hassaan Ahmed, Kumaran Vasu.

## What worked

- **Tight team coordination loop**. The SC Chat Analyzer pass on our WhatsApp confirmed our group's response cadence (Hassaan 3.5 min, Zuraiz 8.8 min) kept blockers from stalling longer than half a day on average. The group stayed close to the work without needing scheduled meetings.
- **Inclusion criteria for Tier-1 corpus survived first contact with reality**. The criteria we agreed on (no post-production, real-time NMP, multi-singer, video present) were strict enough that the curated set re-discovered 4 of Prof. Hacker's 5 Tier-0 seed URLs unprompted. That validated the prompt design before we spent download bandwidth.
- **WP1 audio numbers match musical theory on first run**. SATB voice ranges landed in expected ranges (Soprano 353 Hz, Alto 290, Tenor 203, Bass 131); adjacent-voice coupling 0.72-0.77 matches in-person quartet behaviour. We have confidence in the measurement stack going into Sprint 3.
- **Cross-WP coverage shipped**. All four work packages landed Sprint-2 milestones, including draft flagship figures for both supervisors (Hacker's directed influence graph, Gloor's alchemical-stage pipeline diagram).

## What didn't work, and the root cause

- **Intermediate dates slipped 9-17 days**. Root cause: the original Sprint-2 timeline assumed parallel execution across the four work packages; in practice Sprint 2 ran serially because most engineering tasks share the same data dependencies (Tier-2 had to land before audio extraction; audio parquets had to land before network analysis).
- **We caught the slip late**. We should have re-scoped Sprint 2 mid-sprint (around May 8) instead of waiting until the May-21 deadline forced an end-of-sprint compression.
- **Coordination is task-heavy, bond-light**. SC Chat Analyzer scored our WhatsApp HIGH-Meaning / LOW-Emotion / MEDIUM-Relationship. We are efficient on tasks but thin on team bonding, which slows blocker surfacing because nobody wants to break the substantive flow with a "stuck on X" message.

## One process change for Sprint 3

- **Weekly 15-minute team check-in on WhatsApp (Mondays)**. Light-touch, no meetings, just a structured async thread: each WP posts one line on "shipping this week", "stuck on X", "need from team". Goal: lift Relationship score, surface blockers earlier, reduce response-time variance.
