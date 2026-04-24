---
title: S-02 Entanglement Metric for Team Flow
type: source
alchemy_stage: nigredo
tags: [entanglement, metrics, team-flow, sna, email, deep_read]
ingested_date: 2026-04-23
last_deep_read: 2026-04-23
source_count: 1
related: ["[[entanglement_index]]", "[[Peter_Gloor]]", "[[deep_read_audit]]"]
team_take: Definitional source for E(t), validated on email (n≤113, 7-day windows). Not validated on music or real-time bodily coupling. Any Project-8 use is an adaptation across a domain boundary.
---

# S-02 'Entanglement' - A new dynamic metric to measure team flow

**Citation**: Gloor, P.A., Zylka, M.P., Fronzetti Colladon, A., Makai, M. (2022). *Social Networks* 70, 100 to 111. [DOI:10.1016/j.socnet.2021.11.010](https://doi.org/10.1016/j.socnet.2021.11.010). Elsevier. 12 pages.
**Authors & affiliations**: Peter A. Gloor (MIT Center for Collective Intelligence); Matthäus P. Zylka (Uni Bamberg); Andrea Fronzetti Colladon (Uni Perugia); Marton Makai (Galaxyadvisors AG).
**raw path**: `raw/02_secondary_sources/'Entanglement' – A new dynamic metric to measure team flow.pdf`

## 1. Claim (author's words)

The paper introduces "entanglement" as a metric that "calculates the Euclidean distance among team members' social network metrics timeseries" to measure communication synchronization in online social networks, validated on four email case studies [p. 100, Abstract]. The authors explicitly disclaim causality: "we can only speculate about what is causing the entanglement effect" and "social entanglement is an indicator of behavior, with no definitive claims about cause and causality" [p. 100, Abstract; p. 109, Conclusion].

## 2. Raw Formulas (exact, p. 102 to 103)

Activity entanglement between x and y over time window T:

$$E_A(x_T, y_T) = \frac{C_D(x_T) \cdot C_D(y_T)}{d(A(x_T), A(y_T))} \quad \text{(Eq. 2)}$$

Betweenness entanglement:

$$E_B(x_T, y_T) = \frac{C_D(x_T) \cdot C_D(y_T)}{d(C_B(x_T), C_B(y_T))} \quad \text{(Eq. 4)}$$

Group betweenness entanglement (individual x vs. aggregated group rhythm):

$$E_{GB}(x_T) = \frac{C_{GB,T}}{d(C_B(x_T), C_{GB,T})} \quad \text{(Eq. 7)}$$

where $C_D$ = degree centrality, $C_B$ = normalized betweenness centrality (Freeman 1977, Brandes 2001), $C_{GB}$ = Freeman's group betweenness centralization (Eq. 5), $A$ = communication activity (count of messages sent in window), and $d(\cdot, \cdot)$ = Euclidean distance of two timeseries.

Gini coefficient of $E_{GB}$ (inequality across actors, Eq. 8):

$$G(E_{GB}) = \frac{\sum_{i=1}^{n} \sum_{j=1}^{n} |E_{GB}(x_i) - E_{GB}(x_j)|}{2 n^2 \cdot \overline{E_{GB}}}$$

**Time window**: 7 days, chosen per Gloor (2017) because "this has been shown to deliver the best results for this type of organizational e-mail data" [p. 104, §Data collection]. Not independently justified for other data types.

## 3. Raw Data Block

| Case | Sample | Finding | Statistic | Source |
| :--- | :--- | :--- | :--- | :--- |
| A: Healthcare innovation teams | 53 employees, 11 teams, 1 year | SD of $E_A$ correlates with team performance | Pearson r = **.615**, p = **.045** | [p. 105, §Case A] |
| A: Healthcare innovation teams | same | SD of $E_A$ correlates with learning behavior | Pearson r = **.707**, p = **.015** | [p. 105, §Case A] |
| B: Executive turnover | 113 senior executives, 8 months email | Gini $E_A$: leavers M=.457 SD=.070 vs. stayers M=.488 SD=.059 | t(111) = **−2.513**, p = **.013** | [p. 106, §Case B] |
| B: Executive turnover | same | CatBoost classifier, Monte-Carlo CV, 300 splits, 75/25 train/test | Accuracy **80.25%**, AUC **0.81** | [p. 106, §Case B] |
| C: Individual performance | 81 managers, 2015 year-end review (15 low-performers) | Gini $E_B$: top M=.508 SD=.061 vs. low M=.469 SD=.028 | t(79) = **2.432**, p = **.017** | [p. 107, §Case C] |
| C: Individual performance | same | Gini $E_B$ in logistic regression Model 5 | p < **.10** only; improves McFadden pseudo-R² from .2314 to .2803 | [p. 107, §Case C, Table 5] |
| C: Individual performance | same | CatBoost classifier, same CV procedure | Accuracy **74.73%**, AUC **0.68** | [p. 107, §Case C] |
| D: Customer satisfaction (NPS) | 13 teams, 82 managers | Gini group $E_{GB}$ vs. customer NPS | Pearson r = **.522**, p = **.002** | [p. 107, §Case D] |
| D: Customer satisfaction | N=34 (repeated measures), 13 groups | Multilevel model, adding Gini $E_{GB}$ reduces L2 variance by **30.56%** | Intraclass correlation **0.7604** | [p. 107 to 108, §Case D, Table 6] |

## 4. Method Details

- **Data source**: email corpora from four different organizations. No music, no audio, no body-signal data, no real-time interaction.
- **Tool**: Condor (free for academic use, [ickn.org/ckntools.html](http://www.ickn.org/ckntools.html)) and Griffin [p. 104, §Data collection].
- **Preprocessing**: emails normalized for time zones; nudges (pings before reply), average response time (ART), contribution index (sent vs. received balance), and reach-2 measured alongside [p. 104].
- **ML**: CatBoost (Prokhorenkova et al. 2018) for leaver and top-performer prediction; SHAP (Lundberg & Lee 2017) for feature-importance attribution [p. 106 to 107, §Case B, §Case C].

## 5. Limitations (paper §Discussion, p. 109 to 110)

**Stated**:

- "Our analysis is limited to the contexts of the case studies and the available datasets. It will be important to replicate our analysis in organizations of different industries, also considering different job descriptions and hierarchical positions." [p. 109]
- No definitive causal claims; entanglement is "an indicator of behavior, with no definitive claims about cause and causality" [p. 100, p. 109].
- Other SNA metrics (group centrality, emotion-weighted edges) could extend the definition [p. 110].
- Smart-wearables data (heart rate, body movement) flagged as "future studies" but not attempted here [p. 110].

**Implicit (binding on any downstream citation)**:

- **Domain is email, not music.** Musical, neural, and body-signal synchronization are cited as theoretical motivation (§Theoretical background) but are **not empirical content of this paper**.
- **Temporal resolution is 7-day windows.** Not tested at sub-second (onset) or sub-minute (breath-cycle) resolution.
- Sample sizes are modest: n=53 (A), n=113 (B), n=81 (C), n=82 across 13 teams (D). Each case is a single organization.
- All four studies are correlational / observational, not causal. Controlling for confounds (team-level effects, job-role effects, rank effects) is partial.

## 6. Relevance to Project 8 E(t) (explicit adaptation, not direct application)

Project 8 borrows the **term** and the **conceptual frame** (synchronization of timeseries measured via distance, individual-vs-group flow) but operates across a domain boundary:

| Axis | S-02 (this paper) | Project 8 E(t) |
| :--- | :--- | :--- |
| Data | Email message counts | Audio onsets, pitch F0, body pose timeseries, Granger causality graph |
| Time resolution | 7 days | Seconds to sub-second |
| Actors | Email accounts | Singers |
| Synchrony mechanism | Communication activity patterns | Acoustic and bodily coupling |
| Coupling metric | Euclidean distance of centrality timeseries | A(t), V(t), N(t) composite |
| Validated | Yes (4 case studies, email) | Not yet (Project 8 is the validation) |

The Project 8 formula $E(t) = (A(t) + V(t) + N(t)) / 3$ does **not** inherit S-02's Euclidean-distance-of-centrality structure. It inherits only the name and the intuition that team flow is measurable as a composite coordination signal. Any claim that "entanglement is proven to predict performance in online choirs" by citation of S-02 is an **over-reach**: S-02 proves this for email knowledge work, not music.

## 7. Corrections Logged Against Prior Digest

See [[deep_read_audit]] for the full corrections table. Summary:

| Issue | Prior claim | Corrected reading |
| :--- | :--- | :--- |
| Missing exact formulas | (none given) | Eqs. 2, 4, 5, 7, 8 now cited verbatim. |
| Missing statistical results | "positively correlates with team performance" | r=.615 p=.045 (A), r=.707 p=.015 (A), t=-2.513 p=.013 (B), t=2.432 p=.017 (C), r=.522 p=.002 (D). Effect sizes matter for whether this is a weak or strong predictor. |
| Missing sample sizes | (not stated) | n=53, 113, 81, 82 in four studies. All modest. |
| Missing domain caveat | Treats paper as generic "synchronization" result | Validated on **email only**, 7-day windows, knowledge-work context. Not on music, not on real-time, not on body signals. |
| "Team Flow/Virtual Mirror: we will also apply this concept to our own team's WhatsApp..." | — | Moved to [[entanglement_index]] as a Project-8 extrapolation, explicitly labeled. |
| Missing author list | "Gloor et al. (2022)" | Gloor (MIT), Zylka (Uni Bamberg), Fronzetti Colladon (Uni Perugia), Makai (Galaxyadvisors). Zylka is at our home institution. |
