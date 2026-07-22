# AGENTIC-DAU GENERAL BASKET — DRAFT (2026-07-22)

**STATUS: DRAFT — not yet reviewed/committed by primary session.** Built per `meta/todo.md` 2026-07-15 item ("AGENTIC-DAU runway instrument"), completing the GENERAL basket (coding / enterprise / consumer) alongside the two already-built vertical modules: `meta/education-ai-adoption-instrument.md` (2026-07-14) and `meta/lab-scaffolding-usage-instrument.md` (2026-07-14). Labels reused from those modules: **CUM** = cumulative/ever-tried counter · **SEAT** = paid/provisioned seat (not usage) · **ACT** = active (DAU/WAU/MAU-class) · **ARR** = revenue-only proxy (no user count attached). Tiers: 🟢 T1-vendor (company-disclosed) · 🟡 T2 (press/independent panel) · 🔴 T3 (secondary-aggregator/derived, low-confidence). All derived haircuts carry **(my model)**.

**TL;DR:** Across all three verticals, the SAME split the education and scaffold modules already found holds again: genuine daily-active usage is thinly disclosed and, where visible, runs far below headline "user" counts — except in a handful of metered, professional daily-use products (Cursor, Claude Code) where revenue-per-active is extremely high. Coding is the strongest pillar (real $-per-DAU evidence). Enterprise is the weakest — almost no vendor discloses actual usage depth, only ARR/deals/seats. Consumer is bimodal: ChatGPT's own DAU/MAU ratio can't even be computed (stale WAU), and the one "clean" ratio in the whole dataset (Meta AI 40M DAU / 1.2B MAU) turns out to be a **stale-number-paired-with-fresh-denominator laundering artifact** (DAU figure traces to Aug 2024, MAU is Jan 2026) — the exact "refresh-silence tell" the education module flagged (PC-candidate, see that file's header). 🟡 DIRECTIONAL — the runway read is partial support, not confirmation.

---

## A. CODING vertical

### A1. Tracking series (latest disclosed datapoint)

| Product | Metric | Value | As-of | Tier | Source |
|---|---|---|---|---|---|
| GitHub Copilot | Cumulative all-time users | >20M (spokesperson-confirmed "all-time," NOT active) | 2025-07-30 | 🟢 T1-vendor (CUM) | [TechCrunch](https://techcrunch.com/2025/07/30/github-copilot-crosses-20-million-all-time-users/) |
| GitHub Copilot | Paid subscribers | 4.7M (+75% YoY) | 2026-01-28 (FY26 Q2) | 🟢 T1-filing (SEAT) | MSFT FY26-Q2 earnings (cited via `meta/lab-scaffolding-usage-instrument.md` §1 — mlq.ai; github.blog Octoverse) |
| GitHub Copilot (agent) | Agent-authored PRs vs total merged PR flow | ~1.2M PRs/mo vs 43.2M merged — low-single-digit % of PR flow | 2026-01 | 🟡 T1-via-T2 (ACT proxy) | mlq.ai; github.blog Octoverse (per `meta/lab-scaffolding-usage-instrument.md` §1) |
| Cursor (Anysphere) | Daily active users | >1M | 2026 (unrefreshed exact date not disclosed) | 🟢 T1-vendor (ACT, vendor-claimed) | [getpanto.ai](https://www.getpanto.ai/blog/cursor-ai-statistics) |
| Cursor | Monthly active users | >7M; >50,000 paying teams | 2026 | 🟢 T1-vendor (ACT/SEAT, vendor-claimed) | [getpanto.ai](https://www.getpanto.ai/blog/cursor-ai-statistics) |
| Cursor | ARR | ~$2.0B (crossed $1.0B Nov 2025) | 2026-02 | 🟢 T1-vendor (ARR) | [letsdatascience.com](https://letsdatascience.com/blog/cursor-hit-2-billion-in-revenue-then-it-told-developers-to-stop-coding) |
| Claude Code (Anthropic) | Weekly active users | ~2M (±50%, wide press spread) | 2026-05 | 🟡 T2, never official | cryptobriefing.com (per `meta/lab-scaffolding-usage-instrument.md` §1) |
| Claude Code | Metered revenue (usage-priced ≈ usage) | >$2.5B run-rate | 2026-02 | 🟢 T1 (official floor, ~5mo stale) | saastr.com (per scaffold module) |
| Claude Code | Share of public GitHub commits | ~4% (undercounts via squash-merges) | early-2026 | 🟡 T1/T2, validity B+ | anthropic.com/economic-index |
| OpenAI Codex + ChatGPT Work | Combined active users | 6M (Jul-12) → 7M (Jul-13) → 8M (Jul-14) → 10M reported to Bloomberg ahead of Jul-21 announcement | 2026-07-12→21 | 🟡 T2, **launch-surge, ambiguous "active" window, Codex/ChatGPT-Work NOT separated** | [thenewstack.io](https://thenewstack.io/gpt-5-6-codex-user-surge/); [constellationr.com](https://www.constellationr.com/insights/news/openai-touts-broadening-codex-usage-5-million-weekly-active-users) |
| Windsurf (post-Cognition acquisition) | Revenue run-rate | $492M (Cognition combined, incl. Devin) | 2026-05 | 🟡 T2-press | [luka.to](https://luka.to/blog/windsurf-codeium-billion-dollar-ai-ide) |
| Windsurf (pre-acquisition, as Codeium) | ARR / active developers | $82M ARR (Jul 2025); 800K active developers (early 2025) | 2025-02→07, **stale >12mo** | 🟡 T2-press | sacra.com; luka.to |

### A2. Activation-haircut question — CODING

**Directly-disclosed ratio (rare in this dataset):** Cursor's own vendor claims put DAU (>1M) against MAU (>7M) — an implied **~14% DAU/MAU** (🟢 T1-vendor, both sides same vendor, dates not pinned to same month so treat as approximate). GitHub's paid-conversion (4.7M paid / 20M cumulative ever-tried) gives a **~23.5%** "ever-tried-to-paid" ratio (🟢 T1, but this measures conversion-to-paid, not daily activity — a different haircut than DAU/MAU).

**Haircut prior (my model): ~15–25% of disclosed cumulative/seat-class coding-tool users are genuine regular actives**, anchored on Cursor's self-disclosed 14% DAU/MAU as a floor and GitHub's 23.5% paid-conversion as a ceiling-adjacent proxy. This sits ABOVE the education module's 15% prior — rationale: coding assistants are professional daily-use tools embedded in a work habit (compile/test feedback loop), not institution-provisioned add-ons, so the activation floor is structurally higher. **Caveat: GitHub Copilot itself — the largest named "user" base (20M cumulative) — has ZERO disclosed DAU or WAU number, only a vague "10x YoY" DAU-growth claim with no base** (see A3 falsifier #1), so the 15-25% prior is anchored on Cursor/Claude Code, not on the single largest-headline product in the vertical.

### A3. Falsifiers / staleness triggers — CODING

1. If Microsoft/GitHub discloses an absolute DAU number for GitHub Copilot (not just unattributed "up 10x YoY" language) implying >35% of the 20M cumulative base is genuinely daily-active — the 15-25% haircut prior is too conservative for the largest coding product.
2. If Cursor's or Cognition's ARR growth decelerates sharply (e.g., below 50% QoQ) while vendor-claimed DAU stays flat or keeps climbing — DAU claims have decoupled from paying usage and should be downweighted to 🔴 T3 marketing-artifact status.
3. If the OpenAI Codex+ChatGPT Work "10M combined actives" figure (a ~1M/day growth rate over 9 days, per thenewstack.io) does NOT decelerate to a normal adoption curve within 60 days — treat the whole series as launch-promotional noise, not a genuine activation datapoint.

---

## B. ENTERPRISE vertical

### B1. Tracking series (latest disclosed datapoint)

| Product | Metric | Value | As-of | Tier | Source |
|---|---|---|---|---|---|
| Microsoft 365 Copilot | Paid seats | >20M (of ~450M M365 commercial seats = ~4.4% attach) | 2026-04-29 | 🟢 T1-vendor (SEAT) | [TechCrunch](https://techcrunch.com/2026/04/29/microsoft-says-it-has-over-20m-paid-copilot-users-and-they-really-are-using-it/); [nojitter.com](https://www.nojitter.com/) (via `meta/lab-scaffolding-usage-instrument.md` §1) |
| M365 Copilot | Daily active users (enterprise) | "up 10x YoY" — **no absolute base disclosed** | 2026-01-28 (FY26 Q2) | 🟢 T1-vendor (ACT, base-free) | [windowslatest.com](https://www.windowslatest.com/2026/02/02/microsoft-says-ms-365-copilot-is-now-a-daily-habit-copilot-for-consumers-daily-users-up-3x-after-telling-everybody-to-use-it/) |
| M365 Copilot | Conversations per user | doubled YoY | 2026-01-28 | 🟢 T1-vendor (intensity) | windowslatest.com |
| Salesforce Agentforce | ARR / deals | $800M ARR FY26 (+169% YoY); 29,000 deals | FY26 close (~2026-01/02) | 🟢 T1-filing (ARR) | [futurumgroup.com](https://futurumgroup.com/insights/salesforce-q3-fy-2026-ai-agents-data-360-lift-bookings-and-fy26-outlook/); [salesforceben.com](https://www.salesforceben.com/agentforce-customers-are-doubling-down-60-of-q4-bookings-came-from-expansions/) |
| Salesforce Agentforce | % of Salesforce customer base that has adopted at all | ~5.3% (analyst estimate, NOT vendor-disclosed) | 2026 | 🔴 T3 (Stifel estimate) | via [techhq.com](https://techhq.com/news/salesforce-agentforce-enterprise-agentic-ai/) / finance.yahoo.com Agentforce adoption coverage |
| Salesforce Agentforce | Accounts-in-production growth | +70% QoQ | 2026 | 🟡 T2-press (ACT proxy, no absolute count) | nojitter.com |
| ServiceNow AI Agents | Usage metric | Metered internally in "assists" — **no external DAU/seat/customer-count disclosure found** | 2026 | GAP | servicenow.com product pages (no usage disclosure) |
| Glean | ARR | $300M (tripled from $100M in 15 months) | 2026-05-28 | 🟢 T1-vendor (ARR) | [enterprisedna.co](https://enterprisedna.co/resources/news/glean-300m-arr-enterprise-ai-search-2026/) |
| Glean | Agent actions | >100M annually; tokens 20T/yr, doubling QoQ | 2026 (ARR-doubling point, ~9mo into 2026) | 🟢 T1-vendor (ACT proxy, no user count) | futurumgroup.com; agentmarketcap.ai |

### B2. Activation-haircut question — ENTERPRISE

**No enterprise vendor in this sample discloses a genuine seat-to-daily-active ratio.** The only directly computable haircut is MSFT's seat-ATTACH rate: 20M paid Copilot seats / 450M M365 commercial seats = **~4.4%** (🟢 T1) — but this measures who BOUGHT a seat, not who uses it daily; MSFT's own "10x YoY DAU" claim has no base, so a true activation ratio cannot be computed even for the best-disclosed enterprise product.

**Reused evidence from the scaffold module (same underlying enterprise-agent population, applicable here):** Bain survey — 97% executive-claimed AI use vs 52% employee-reported use (~2x self-report inflation); Menlo Ventures — only 16% of nominal "agent" deployments are true autonomous agents (rest are simpler automations mislabeled); MIT NANDA — 90% of personal AI use is vanilla chat vs 40% official-sanctioned use (per `meta/lab-scaffolding-usage-instrument.md` §3 Chain C). Independently, `wiki/agentic-ai-enterprise.md` finds production-deployment rate across enterprise agentic pilots generally runs **11–25%** of started pilots (Agentic AI Institute, 2026), with 88% of a separate 847-deployment sample failing to reach production at all (Medium study).

**Haircut prior (my model): ~10-15% of disclosed enterprise "agent seats/deals/customers" translate into genuine sustained production usage.** Anchored on the 11-25% production-deployment-rate midpoint from the enterprise-wide agentic literature (not vendor-specific), NOT on MSFT's 4.4% seat-attach (a different, non-comparable denominator — seat-attach already excludes non-buyers, whereas the 11-25% figure describes what happens AFTER a pilot starts). This is LOWER than both education (15%) and coding (15-25%) — rationale: enterprise rollout requires organizational workflow redesign, not individual tool adoption, and the Menlo/Bain evidence shows enterprises both mislabel simple automations as "agents" and over-report usage internally.

### B3. Falsifiers / staleness triggers — ENTERPRISE

1. If Microsoft's next earnings call (~Oct 2026, FY26 Q4 or FY27 Q1) discloses an absolute DAU number for M365 Copilot (not just "10x YoY") — first real activation datapoint for the largest-seat enterprise product; would directly test the 10-15% prior.
2. If ServiceNow or Salesforce discloses a genuine active-agent/DAU-class metric (not ARR, deals, or bookings) — breaks the current pattern that NO enterprise vendor in this sample discloses usage depth; single highest-value disclosure this vertical could produce.

---

## C. CONSUMER vertical

### C1. Tracking series (latest disclosed datapoint)

| Product | Metric | Value | As-of | Tier | Source |
|---|---|---|---|---|---|
| ChatGPT | Weekly active users | 900M (last official figure, **~5.5 months stale** as of 2026-07-22) | 2026-02 | 🟢 T1-vendor (ACT, stale) | [TechCrunch](https://techcrunch.com/) coverage / OpenAI blog (per `meta/education-ai-adoption-instrument.md` §1D cross-reference) |
| ChatGPT | Monthly active users | crossed 1B ("fastest app in history" to the mark) | 2026-06 | 🟡 T2-independent (Sensor Tower via Reuters, NOT T1) | per prior harness convention (education module §1D) |
| Gemini app | Monthly active users | 350M (Apr'25) → 650M (Q3'25) → 750M (Q4'25) → 900M+ (2026 I/O) | 2026-05 | 🟢 T1-vendor (ACT, MAU only — **no DAU ever disclosed**) | [TechCrunch](https://techcrunch.com/2026/02/04/googles-gemini-app-has-surpassed-750m-monthly-active-users/); Google I/O 2026 keynote |
| Gemini "AI Mode" | Monthly active users (US+India) | >100M | 2026 | 🟢 T1-vendor (ACT) | Google I/O / blog.google coverage |
| Meta AI | Monthly active users | 1.2B (+20% vs 1B in Oct 2025) | 2026-01 (Q1'26) | 🟢 T1-vendor (ACT) | demandsage.com; Meta Q1'26 disclosure coverage |
| Meta AI | Daily active users | ~40M — **traces to a 2024-08 origin figure (The Information), NOT re-disclosed in 2026** | reported as "2026" by aggregators but underlying figure dates to 2024-08 | 🔴 T3 **STALE, mismatched-denominator laundering** | [threads.com/@meta.ai](https://www.threads.com/@meta.ai/post/DYR8h5HAcHf/); underlying origin per secondary-aggregator cross-check |
| Perplexity | Monthly active users, "across all products" | >230M | 2026-03 | 🟡 T2 (margen.net citing unspecified vendor disclosure) | margen.net |
| Perplexity | Monthly active users, "core+agent products" | >100M | 2026-04 | 🟡 T2 (FT/Sacra) | Financial Times, cited via Sacra |
| Perplexity | Monthly active users, core-search-only | ~30M | 2025-04, **>12mo stale** | 🟡 T2 | per prior cross-source convention |

### C2. Activation-haircut question — CONSUMER

**No clean same-vendor, same-period DAU/MAU ratio exists for the two largest consumer assistants (ChatGPT, Gemini).** ChatGPT's WAU (900M) is 5.5 months stale and cannot be validly ratioed against the June-2026 MAU (1B, and itself a T2 non-vendor Sensor Tower figure) — the two numbers are from different measurement methodologies AND different dates. Gemini has published MAU at four points across 14 months but has **never once disclosed a DAU figure** — this matches the exact "refresh-silence tell" the education module identified (vendors publish the series that flatters, freeze the one that doesn't).

**Meta AI's "40M DAU / 1.2B MAU ≈ 3.3%" ratio, widely repeated by 2026 secondary aggregators as if current, is itself a laundering artifact**: the 40M DAU figure traces to an August-2024 report (The Information), never re-disclosed since, while the 1.2B MAU figure is January-2026. Pairing them produces a superficially "clean" ratio that is actually comparing a 17-month-old numerator to a current denominator — precisely the pattern flagged as PC-candidate ("refresh-silence tell") in the education module header. **This is downgraded to 🔴 T3 and should NOT be used as a load-bearing haircut anchor**, though directionally it is still suggestive that ambient/embedded assistants (Meta AI inside WhatsApp) show much lower daily-habitual conversion than sought-out standalone assistants.

**Haircut prior (my model, LOW CONFIDENCE): consumer-assistant genuine daily-habitual use is plausibly bimodal — likely >50% WAU/MAU for the standalone, sought-out leaders (ChatGPT; inferred, not measurable from current disclosures) vs low-single-digit % for assistants ambiently embedded in a messaging app (Meta AI; direction only, not the specific 3.3% figure, which is stale-paired).** This is the widest, least-confident haircut band in the entire GENERAL basket — a genuine data gap, not a resolved finding.

### C3. Falsifiers / staleness triggers — CONSUMER

1. If OpenAI refreshes the 900M WAU figure with a same-definition number dated within the current quarter — first chance to compute a real, non-stale ChatGPT WAU/MAU ratio; would resolve whether ChatGPT is actually the highest-conversion consumer product in the basket.
2. If Meta discloses a FRESH (2026-dated) DAU figure for Meta AI — either confirms the ~3-4% ambient-embedding read (if DAU stayed roughly flat while MAU tripled, ratio falls further) or overturns it (if DAU grew proportionally, the "ambient = low engagement" read breaks).
3. If Perplexity stops switching its MAU denominator (core-search-only vs core+agents vs all-products) across two consecutive disclosures — resolves the current definitional-creep flag; continued denominator-switching confirms a bearish "laundering" tell matching the education module's Gauth/Photomath pattern.

---

## D. SYNTHESIS — rolling GENERAL basket + education + scaffold into ONE runway read

**The cross-vertical pattern is now confirmed at N=3 (education, scaffold, GENERAL-basket coding/enterprise/consumer) — the SAME split recurs everywhere it's checked:**

1. **User-count evidence is thin, stale, or self-contradictory almost everywhere it matters most.** GitHub Copilot (20M cumulative, largest coding "user" base) has no DAU. Gemini (900M+ MAU, second-largest consumer assistant) has never disclosed DAU. ServiceNow (an enterprise AI-agent platform vendor) discloses zero usage metrics externally. Meta AI's apparent DAU/MAU "clean ratio" is a stale-paired laundering artifact once traced to its origin. This mirrors the education module's core finding almost exactly ("companies disclose the series that flatters and freeze the ones that don't") and the scaffold module's finding that most labs disclose CREATED-counters, not usage.

2. **Where genuine activity IS visible, it is concentrated in a small number of metered, professional, daily-habit products — and the revenue-per-active is extremely high.** Cursor: ~$2.0B ARR / >1M DAU ≈ **~$2,000/DAU/year** (🟡 T1-vendor both sides, my derivation). Claude Code: ~$2.5B run-rate / ~2M WAU ≈ **~$1,250/WAU/year** (🟡, both T1-adjacent per scaffold module). This is the single strongest piece of evidence FOR the capex-justifying-demand thesis in the entire three-module dataset — it is TOKEN/REVENUE-intensity evidence, not raw user-count evidence, exactly matching the scaffold module's Chain D finding that "penetration is LOW by users (3-8%), HIGH by tokens/dollars (30-55%)."

3. **Enterprise remains the weakest, least-disclosed link across ALL THREE modules now** — education's lab/teacher verticals (CSU: zero usage data on 500K seats; Khanmigo: 15% activation), the scaffold module's enterprise chain (7-10% "heavyweight" scaffold attach, my model), and now this basket's enterprise vertical (MSFT 4.4% seat-attach with no DAU base; ServiceNow zero disclosure; Salesforce ~5.3% customer-adoption per Stifel T3 estimate). Three independent verticals, same institutional-provisioning pattern: low disclosed activation where an organization (not an individual) makes the purchase decision.

4. **Consumer is the pivotal, unresolved swing factor for the runway question.** ChatGPT's 900M WAU (if it held or grew) would be, in absolute terms, the single largest piece of evidence that AI usage is genuinely mass-scale and durable — but it is 5.5 months stale and cannot currently be checked against a same-period MAU. This is the highest-value single disclosure the entire GENERAL basket is waiting on (falsifier C3.1).

**Runway verdict (🟡 DIRECTIONAL, not resolved):** Genuine agentic/AI daily-active usage growth provides **partial, not full, support** for the current AI-infra capex trajectory. The strongest evidence is intensity-based (tokens/revenue per active user, concentrated in a handful of coding products) rather than breadth-based (raw DAU growth across the installed base) — this is a **fragile** support structure: it holds if per-user intensity keeps compounding (agentic tasks running ~15x the token cost of chat, per the scaffold module's Chain D), but breaks if intensity growth stalls at the same time user-count growth plateaus. The three-module dataset has not yet found a single vertical where BOTH breadth (user count) AND depth (per-user intensity) are simultaneously well-disclosed and both growing — that combination, if it appeared, would be the strongest possible confirming signal; its absence is itself the finding.

**Biggest structural data gap across the whole instrument:** no lab or major platform (OpenAI, Google, Microsoft enterprise-Copilot, ServiceNow, Salesforce) currently discloses a same-period DAU-to-MAU or DAU-to-seat ratio for its flagship product. Every haircut prior in this file (and in the two prior modules) is therefore a cross-product proxy (Cursor/Claude Code standing in for coding broadly; production-deployment-rate literature standing in for enterprise broadly), not a same-vendor measured ratio — the instrument's honest state is "directional, proxy-based," not "measured."

## E. Instrument design note (feeds monthly AGENTIC-DAU cadence)

Recommended monthly-scan series (mirrors education module §4 / scaffold module §5 format): (1) GitHub/MSFT Copilot next DAU disclosure (any absolute base) — highest-value single miss in the coding vertical; (2) Cursor/Cognition ARR deceleration vs DAU-claim divergence; (3) MSFT M365 Copilot next earnings DAU base; (4) ServiceNow/Salesforce first genuine usage-depth disclosure (currently zero across the entire enterprise vertical); (5) OpenAI ChatGPT WAU refresh (5.5mo overdue as of this writing); (6) Gemini DAU — watch for a first-ever disclosure; (7) Meta AI DAU refresh — watch for a 2026-dated (non-2024-laundered) figure. Cadence: monthly scan, ~20-30 min, per the education/scaffold instruments' existing cadence discipline.

---

**Position implication: NO ACTION (instrument build)**
