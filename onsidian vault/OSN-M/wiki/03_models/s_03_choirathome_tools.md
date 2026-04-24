---
title: S-03 Choir@Home Tools Survey
type: source
alchemy_stage: nigredo
tags: [nmp, benchmarks, choir, tools, deep_read, grey_literature]
ingested_date: 2026-04-23
last_deep_read: 2026-04-24
source_count: 1
related: ["[[nmp_platform_comparison]]", "[[nmp_hardware_requirements]]", "[[Janine_Hacker]]", "[[deep_read_audit]]"]
team_take: Project-deliverable brochure from Hacker's own Choir@Home ERASMUS+ project. Tactically useful for Apr 30 meeting context. Not a peer-reviewed source; marketing-style tool descriptions with no quantitative data.
---

# S-03 Choir@Home: Tools for a Stay-at-Home-Choir

**Document**: Choir@Home Project Report R2.2, "Tools for a Stay-at-Home-Choir: Software solutions for collaborative music-making." 8 pages, brochure format. No formal authorship line; **not peer-reviewed**.
**Project team**: Dr. Janine Hacker (University of Liechtenstein); Univ. Prof. Dr. Heike Henning (Mozarteum University Salzburg); Prof. Dr. Alexander Carôt (Anhalt University of Applied Sciences).
**Funding**: EU ERASMUS+ Key Action 2 (Cooperation Partnerships).
**Website**: [choirathome.com](https://choirathome.com/)
**raw path**: `raw/02_secondary_sources/R2.2_ChoirAtHome_Tools.pdf`

**Key context**: Janine Hacker is Project 8's own COINs seminar lead and one of the Apr-30-meeting professors. This report is her project's output — politically relevant for the meeting, not technically primary.

## 1. Scope

Two-part survey of software tools:

**Part 1 — Video conferencing systems**:

| Platform | Max participants (free) | Music Mode | Notes |
| :--- | :--- | :--- | :--- |
| Zoom | 1000 | Yes (Hi-Fi Music Mode) | Market leader, time limit on free |
| Microsoft Teams | 300 (paid) | Yes | Office 365 integration, partial music support |
| Skype | 100 | No | Microsoft since 2011 |
| Webex | 100 | Yes | Cisco, 50-min free limit |
| Jitsi Meet | 75 (35 recommended) | No | Open-source, no E2E encryption |
| Google Meet | 100 | No | 60-min free limit, Google account needed |

**Part 2 — Dedicated NMP (real-time music) tools**:

| Platform | License | Architecture | OS | Cost |
| :--- | :--- | :--- | :--- | :--- |
| **Jamulus** | Open-source (GPL) | P2P or own server | Windows/Mac/Linux/Android | Free |
| **Soundjack** | Closed-source | P2P primary | Windows/Mac/Linux | Free |
| **JamKazam** | Commercial | P2P or central server | Windows/Mac | $4.99 to $19.99/month |
| **ELK Live** | Beta (paid planned) | Proprietary cloud | MacOS (Windows in dev) | Free during beta |
| **JackTrip** | Open-source | P2P or client-server | Windows/Mac/Linux | Free; Virtual Studio paid from $8.25/mo |

## 2. Document Content (§Per-tool qualitative lists)

Each platform gets 1-page advantages/disadvantages bulleted list. No numeric benchmarks, no measured latencies, no jitter statistics, no user study.

**Tables on pages 4 and 7** aggregate:

- User-friendliness (+ to ++)
- Music Mode availability
- Recording capability
- Costs

## 3. Raw Data Block (what numbers ARE in the paper)

| Fact | Value | Source |
| :--- | :--- | :--- |
| Jamulus maximum free participants (public servers) | "public server capacities may be limited" — no number | [§Jamulus] |
| Jitsi Meet participant cap | 75 (35 recommended) | [§Jitsi] |
| Zoom participant cap | 1000 | [§Zoom] |
| Webex free-version time limit | 50 minutes | [§Webex] |
| Google Meet free-version time limit | 60 minutes | [§Google Meet] |
| Jamulus development year | 2006 | [§Jamulus] |
| Skype launch | 2003 | [§Skype] |

**All other "latency" and "quality" claims are qualitative adjectives** ("low", "high", "user-friendly") with no measurements.

## 4. Limitations

**Implicit (document is explicitly a project deliverable, not a research paper)**:

- **Not peer-reviewed**. Published as a Choir@Home project deliverable R2.2.
- **Marketing-style descriptions** based on official product websites (see Sources section on pp. 4, 7).
- **No measurements**: no latency, jitter, packet loss, or user-experience data.
- **No user study** or comparative evaluation.
- **Pricing likely outdated** (2023 prices; subject to change).
- **No engineering depth**: architectural trade-offs described qualitatively, not quantitatively.
- **No stated threshold** for "latency sufficient for music" — cited as background without defining.
- Written as educational outreach material for choir directors, not technical community.

## 5. Relevance to Project 8 E(t)

**S-03 is useful for**:

- **Tactical context for Apr 30 meeting**: Hacker's own project output. Useful to acknowledge in conversation with her.
- **Tier 2 platform-selection background**: confirms Jamulus + SoundJack + JackTrip as the canonical dedicated-NMP trio, matching [[nmp_platform_comparison]] categorization.
- **ELK Live and JamKazam** are lesser-known alternatives worth flagging for completeness.
- **Choir@Home project existence**: Hacker has been publishing on this topic; alignment exists.

**S-03 is NOT**:

- A primary source for latency benchmarks. [[p_11_chamber_choir]] and [[p_15_5g_iomt_analysis]] provide measured numbers; S-03 provides qualitative descriptors only.
- A source for "80% hardware dependency" — that figure is NOT in the paper (prior digest fabrication). The paper discusses hardware as "significant" without a percentage.
- A source for "audio-only or low-frame-rate video preserves bandwidth for synchronization data" — not in paper text.
- An authoritative engineering comparison of NMP tools.
- Appropriate to cite as a peer-reviewed authority.

## 6. Corrections Logged Against Prior Digest

See [[deep_read_audit]] for full table. Summary:

| Issue | Prior claim | Corrected reading |
| :--- | :--- | :--- |
| Missing "grey literature" caveat | "Source: Hacker, J., Henning, H., & Carôt, A. (2023). Choir@Home Project Report R2.2." (correct attribution) | Not peer-reviewed; project deliverable from ERASMUS+ grant. Marketing-style, not engineering study. |
| "Comparison of Dedicated NMP Tools" table with Latency ratings ("Low", "Extremely Low") | — | These ratings are **not in the paper**. Paper uses qualitative adjectives but does NOT rank tools by latency. Prior digest invented a comparative latency column. |
| **"Success is 80% dependent on hardware"** | — | **Fabricated**. No percentage in paper. Paper says hardware is "significant" without quantification [§Real-time music-making]. |
| "Audio-only or low-frame-rate video is preferred to preserve bandwidth for critical synchronization data" | — | Not in paper. No such statement in S-03 text. Possibly Project-8 extrapolation or misattributed to another source. |
| Missing Janine Hacker Project-8-context note | (not stated) | Hacker is Project 8's lead professor. S-03 is her own ERASMUS+ project deliverable. Tactically relevant context. |
| Missing "not peer-reviewed" | (not stated) | Project deliverable R2.2 of EU ERASMUS+ grant. Not journal/conference paper. |
| Best-For claims fabricated ("Large Ensembles", "Professional Chamber Music", etc.) | — | Paper does NOT make "best for" pairings between tool and use-case. Prior digest invented these. |
| "Network topology fundamentally changes the jitter profile" as S-03 finding | — | Paper does not discuss jitter profiles. It distinguishes P2P vs. server architecture but gives no jitter data. Project-8 extrapolation. |
