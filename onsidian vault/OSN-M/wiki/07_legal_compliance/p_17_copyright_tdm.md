---
title: P-17 Copyright and TDM
type: source
alchemy_stage: nigredo
tags: [legal, copyright, tdm, compliance, deep_read]
ingested_date: 2026-04-23
last_deep_read: 2026-04-24
source_count: 1
related: ["[[fair_use_tdm]]", "[[lawful_access_prerequisite]]", "[[data_sourcing_policy]]", "[[deep_read_audit]]"]
team_take: China-perspective policy paper comparing US/Japan/EU TDM regimes. Does NOT address Germany's §60d UrhG (the actual Project 8 basis). Useful for confirming EU DSM Article 3 non-commercial-research requirement. Short conference paper, no case-law depth.
---

# P-17 Application of Copyright Exceptions under Text and Data Mining Technology

**Citation**: Wang, L., Wang, Y., Wang, C. (2024). In *Proc. 2nd International Conference on Intelligent Data Communication Technologies and Internet of Things (IDCIoT)*, pp. 1145 to 1148. [DOI:10.1109/IDCIOT59759.2024.10467650](https://doi.org/10.1109/IDCIOT59759.2024.10467650).
**Affiliations**: Nanjing University of Science and Technology (Intellectual Property Dept.); Nanjing University of Science and Technology (Sino-French College of Engineers); Northwestern Polytechnical University (Marine Science and Technology), Xi'an, China.
**raw path**: `raw/01_primary_sources/Application_of_Copyright_Exceptions_Under_Text_and_Data_Mining_Technology.pdf`

## 1. TDM Lifecycle (§II)

Three stages, each with distinct copyright-infringement risks [§III]:

| Stage | Description | Copyright risks |
| :--- | :--- | :--- |
| **Copying** | Crawl-based acquisition from web, databases, literature, social media, log files | Right of reproduction |
| **Extracting** | Preprocessing: tokenization, stop-word removal, stemming, standardization; PDF → XML transcoding | Right of adaptation / translation |
| **Recombining** | Integrate into patterns/trends/correlations; output visualization + reports | Right of information network dissemination (public communication) |

**Sui generis right** [§III-B]: Distinct from copyright. Protects databases where the owner has made "substantial investment in obtaining, verification or presentation." Explicitly cited: **EU Court of Justice 2004 ruling** — investment for creation of data is NOT protected, but investment for obtaining/presenting/verifying IS [p. 1147].

## 2. Jurisdictional Comparison (§IV, Table I)

| Country | Legal basis | Purpose | Commercial use |
| :--- | :--- | :--- | :--- |
| **US** | Judicial precedents (no statute) | Transformative use (fair use) | **Allowed** |
| **Japan** | Copyright Law Art. 30-4 (2018) | Not for personal enjoyment of thoughts/sentiments | **Banned** |
| **EU** | DSM Directive 2019 Arts. 3 and 4 | Scientific research, non-profit, public interest (Art. 3); other TDM of legally acquired works (Art. 4) | **Banned** (Art. 3); Art. 4 allows unless rightsholders explicitly opt out |

**EU DSM Article 3** [§IV-C, p. 1147]: Research organizations + cultural heritage institutions may copy/extract TDM of **legally acquired works** for scientific research, non-profit + public-interest objective.

**EU DSM Article 4** [§IV-C, p. 1147]: Member states should allow copying/extraction of legally obtained works/content for TDM. **Prerequisite: lawful access** to content. Commercial use not explicitly banned in Article 4 but rightsholders can reserve rights machine-readably.

**US fair-use factors** [§IV-A]: four-factor test — purpose and character, nature of work, amount/substantiality, market impact.

## 3. Chinese Policy Recommendations (§V)

The paper is primarily a **Chinese policy paper**, recommending China adopt TDM fair-use clauses modeled on EU/Japan:

- Add TDM fair-use clauses to China's existing 12 fair-use situations
- Subject: research institutions + public orgs + non-commercial actors (modeled on EU Art. 3)
- Non-commercial purpose required
- Legal-acquisition prerequisite
- Technical path: pre-screen data to exclude copyrighted content

## 4. Limitations

**Implicit** (paper has no explicit §Limitations):

- **China-focused policy paper**, not an empirical study.
- **Short conference paper** (4 pages), limited case-law depth.
- Does **NOT address Germany specifically**. Germany's **§60d UrhG** (statutory scientific-TDM exception, pre-dates EU DSM) is not mentioned. **This is the actual statutory basis Project 8 should cite**, not a general EU DSM reading.
- Does NOT address German DPA guidance on mixing TDM with GDPR Art. 6 and Art. 89 (research exception).
- Does NOT address non-text TDM specifically — audio, video, image TDM may have different fair-use considerations (e.g., moral rights, performer rights).
- US "fair use for commercial TDM" framing is over-simplified: judicial precedents (e.g., Authors Guild v. Google 2015) are nuanced, not blanket allowance.
- Published in a non-IP-focused venue (IoT/Data Communication conference). Not a top-tier IP law journal.

## 5. Relevance to Project 8 E(t)

**P-17 is useful for**:

- **EU DSM Article 3 framing**: research organizations conducting non-profit scientific TDM of legally-acquired works. Project 8 qualifies (Uni Bamberg + Uni Köln + HSLU research context).
- **"Lawful access" prerequisite**: any Project 8 TDM of YouTube must not circumvent technical protections. `yt-dlp` on publicly streaming videos is a grey area; scraping past paywalls is not allowed.
- **Three-stage analysis**: Project 8's pipeline (download → feature extract → aggregate analytics) maps to P-17's Copying / Extracting / Recombining.
- **Sui generis database-right caveat**: if YouTube's video corpus is considered a protected database (EU court interpretation), sui generis right may apply. This is a specific risk item for [[limitations_register]] L-E-2.

**P-17 is NOT**:

- The primary legal basis for Project 8. Germany's **§60d UrhG** (statutory TDM research exception enacted before EU DSM transposition) is the binding authority, not Wang et al.'s EU DSM summary.
- A source for Project 8's GDPR analysis — P-17 does not address personal-data / biometric-data dimensions of choral singers captured on video.
- A source for opt-out / reservation mechanics (EU DSM Art. 4 allows rightsholders to opt out via machine-readable signals; P-17 does not analyze this).
- A guide to how EU DSM transposes into DE / FR / IT law — national transpositions vary.
- A case-law-based study. The EU Court 2004 ruling cited is relevant to sui generis; other EU case law (e.g., Pelham, Funke Medien) not discussed.

## 6. Corrections Logged Against Prior Digest

See [[deep_read_audit]] for full table. Summary:

| Issue | Prior claim | Corrected reading |
| :--- | :--- | :--- |
| Missing China-focus caveat | "This paper analyzes... with a focus on establishing a framework for China" | **Correct in prior digest** — paper is Chinese policy recommendation, not an authoritative EU / DE analysis. Project 8 should not cite this as primary German-law guidance. |
| **Missing §60d UrhG absence** | (not stated) | P-17 does NOT mention Germany's §60d UrhG (statutory research-TDM exception). This is the actual binding law for Project 8. Prior digest treats P-17 as if it were a complete EU source, which it is not. |
| "Articles 3 & 4 provide exceptions for scientific research by non-profits, but require Lawful Access" | — | Correct but incomplete. Article 3 = non-profit public-interest research. Article 4 = broader (any TDM of lawfully-accessed content) but rightsholders can opt out via machine-readable reservations. Prior digest conflated the two. |
| **"Our 'transcoding' of video into skeletal landmarks (MediaPipe) and audio features (Librosa) falls under the 'Extracting' stage and is protected as long as we maintain Lawful Access"** | — | **Partially correct but glosses the performer-rights issue**. Video of identifiable singers → GDPR Art. 9 (biometric data from facial landmarks) + German performer rights (§73-§84 UrhG) are separate from copyright analysis. P-17 is copyright-only; Project 8 must separately address GDPR + performer rights. |
| Missing US case-law nuance | "Transformative use is generally allowed even for commercial entities" | Over-simplified. US fair-use is four-factor, case-by-case. Google Books (2015) was fair use; other cases have gone the other way. Not a blanket allowance. |
| Missing sui generis EU Court 2004 ruling | (not stated) | EU Court of Justice 2004 distinguished "investment in obtaining/presenting/verifying" (protected) from "investment in creation of data" (NOT protected). Relevant if YouTube's corpus counts as a protected database [§III-B]. |
| Missing short-paper / non-IP-venue caveat | (not stated) | 4-page conference paper in IoT/Data-Communication venue, not a top-tier IP law journal. Limited authority. |
