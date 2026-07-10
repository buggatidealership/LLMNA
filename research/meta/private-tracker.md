# Private AI Companies Tracker

**Last updated:** 2026-05-20

Names that matter to public-market thinking but don't have tickers. Track their actions because they shape demand and competitive dynamics for our universe.

## Frontier model providers

### OpenAI
- Status: Largest AI model provider; targeting Q4 2026 IPO at $800B–$1T valuation
- Public-market relevance: Compute customer (NVDA, MSFT Azure); Stargate consortium
- Latest signals: Going on-prem with enterprise consortium (Anthropic partnership)
- Watch: IPO progression; on-prem deal scale; partner shifts

### Anthropic
- Status: Strong #2 to OpenAI in scale, but passed OpenAI in enterprise share by April 2026; **IPO path OPENED — confidential draft S-1 filed 2026-06-01**
- Public-market relevance: Compute customer (AMZN AWS, GOOG); Anthropic-Amazon partnership deep; Anthropic-AVGO custom Si partnership announced May 2026
- **2026-06-01 STATE CHANGE (backfilled 2026-07-07 — event was never logged; caught via US Leg B re-surface + Rule #16/B63 adversarial verification):** Confidential draft S-1 filed with SEC (IPO path opened). T1 company-confirmed ([anthropic.com](https://www.anthropic.com/news/confidential-draft-s1-sec)) + CNBC/CNN/NPR/TechCrunch independent. FACT: filing itself; concurrent ~$65B Series H @ $965B valuation (T1/T2 reported); RRR ~$47B at filing (T2 CNBC). SPECULATION (T3, unconfirmed): Oct-2026 Nasdaq listing, >$60B raise, GS/JPM/MS leads, "$1T IPO" framing — company explicitly says shares/price/exchange/timing NOT set; confidential S-1 = option, not commitment. **Re-surfaced 2026-07-07 via Crunchbase H1 roundup = STALE-RECYCLE (B40/B61) — do not re-log as new.** B63 note: Anthropic-favorable item; adversarial pass run, core fact survived on company-confirmation tier.
- **2026-07-08 PM update — FABLE 5 EXPORT-CONTROL SUSPENSION RESOLVED (the parked outage flag; B63: negative, full weight; per `signals/cross-source-log/2026-07-08-morning-brief-b61-gauntlet-gpt56-fable5-sambanova-nand-check.md`):** verified timeline: Fable 5 launch Jun-9 → **SUSPENDED Jun-12 under US export controls** (Amazon researchers demonstrated a safeguard bypass producing exploit code; no real-time nationality check → pulled globally) → controls lifted Jun-30 → restored Jul-1 (**~18-19 days dark**) → paid-plan window (50% weekly-limit cap) extended to Jul-12 after backlash → then metered $10/$50 per Mtok; corporate customers shifted per-seat → metered (T1 anthropic.com + T2 Forbes/Register). **H2 enterprise-trust-tax P~45 → P~55 (my model)** — most severe datapoint yet (customers lost a production model mid-contract), though the pre-registered "3rd named ENTERPRISE restriction → P~60+" threshold is not technically met (government action ≠ enterprise policy). Launch-week collision: OpenAI GPT-5.6 Sol/Terra/Luna Jul-9 (Sol $5/$30, Terra $2.50/$15, Luna $1/$6 per Mtok, T1; Commerce-cleared), timed on Fable-5's metering transition (T3 "preemptive strike" framing). Watch: procurement language citing the suspension; multi-model failover clauses.
- **2026-07-08 update — CURSOR CONCENTRATION RISK + vertical-integration threat (B63: Anthropic-negative, ingested at full weight; per `signals/cross-source-log/2026-07-08-twitter-batch-spacexai-cursor-zhipu-chip-china-model-curbs-3agent.md`):** Cursor at peak accounted for **~40-50% of Anthropic revenue** (T2 36Kr/Analytics India Mag) as its single largest model buyer; Anthropic's own Claude Code hit ~$2.5bn annualized Feb-2026, overtaking Cursor (~$2.0-2.6bn ARR) — supplier turned competitor BEFORE SpaceX's $60bn Cursor acquisition (Jun-16). If the SpaceXAI in-house model (launch reportedly imminent, memo-tier) migrates Cursor traffic off Claude, the (formerly) largest external revenue channel shrinks while Claude Code substitutes — no reported figure on CURRENT Cursor→Anthropic volume; migration is inference, not reported fact. Watch: Cursor model-mix disclosures post-launch. Also 07-08: TC-15 core member via AVGO custom-Si (inference-silicon internalization cluster, N=4).
- **2026-06-11 update (per `signals/cross-source-log/2026-06-11-june10-evening-brief-triage-b40-n9.md`):**
  - **MSFT restricted internal employee use of Fable 5** (removed from internal GitHub Copilot model picker) over the Mythos-class retention requirement — which **overrides existing ZDR agreements** (T1 Anthropic Help Center: 30-day retention all platforms, up to 2 years if classifier-flagged). MSFT simultaneously sells Fable 5 via Foundry = customer-balking, not competitor positioning (T2 Verge/Reuters).
  - Named-researcher false positives (Unutmaz/Jackson Lab, Verdon) + **Anthropic acknowledged safeguards too stringent** (T2 The Register).
  - **H2 enterprise-trust-tax: P~30% → P~45% (my model, Bayesian: 2nd hyperscaler + acknowledged false positives + ZDR-override).** Threshold to dominant: 3rd named enterprise restriction (P~60%+, my model, directional). Watch Forrester-style vendor-risk advisories converting into named policies.
- **2026-06-10 update (per `signals/cross-source-log/2026-06-10-morning-brief-6-claim-verification-anthropic-spacex-dc.md`):**
  - **Fable 5 + Mythos 5 launched June 9** (first public Mythos-class). System card (T1, 319pp) discloses **silent capability-degradation interventions** on frontier-LLM-development tasks (~0.03% traffic, <0.1% orgs; prompt modification/steering/PEFT, invisible at runtime). "Sabotage" claims UNSUPPORTED; cyber/bio/chem/distillation requests reroute to Opus 4.8, not refused. Enterprise-trust impact: H1 negligible P~60% / H2 slow-burn trust-tax P~30% / H3 escalation P~10% (my model).
  - **Bedrock first-breach:** Mythos-class invocation requires opt-in `provider_data_share` (prompts/completions to Anthropic, ≤30-day trust-safety retention, not training — T1 AWS docs). First crack in Bedrock's no-provider-sharing norm; narrow but precedent-setting.
  - **Comparative position vs OpenAI strengthening:** Anthropic technical wins now a NAMED OpenAI-collateral-risk factor (Bloomberg native-jp, SoftBank $6B margin-loan stall 2026-06-10); Google's $4.99 consumer price cut pressures OpenAI's consumer line while Anthropic stays enterprise-weighted. P~60% (my model) OpenAI-funding-stress hardens into Q3 narrative with Anthropic as relative beneficiary.
  - SpaceX $45B compute deal = GROUND (xAI Colossus, 220K NVDA GPUs, 300MW per 2026-06-07 verification file); orbital = "interest" only (T2). SpaceX IPO June 12.
- Latest signals (2026-05-20, per [WSJ via Investing.com](https://za.investing.com/news/economy-news/anthropic-revenue-set-to-more-than-double-to-109-billion-in-q2-4293058) and [Sherwood News](https://sherwood.news/markets/anthropic-revenue-run-rate-30-billion-google-broadcom-partnership/)):
  - Q1 2026 revenue: $4.8B
  - Q2 2026 forecast revenue: $10.9B (~+127% q/q, ≈ "130% surge" per headline)
  - Q2 2026 forecast operating profit: **$559M — first ever** (includes training costs, excludes SBC)
  - Annual run rate: $30B (per Sherwood News)
  - Prior guidance had been: no profitability until 2028 at earliest
  - Caveat: may not stay profitable full year due to compute + training capex
  - Expanded partnerships announced: **Google + Broadcom** (the AVGO custom Si angle is the under-noticed detail)
- **2026-07-08 update:** GPT-5.6 **Sol/Terra/Luna** launching Jul-9 (T1 openai.com preview: tiers — Sol flagship $5/$30 per Mtok, Terra $2.50/$15, Luna $1/$6); launch **cleared by US Dept of Commerce after government review** (T2 VentureBeat; full-public vs widened-gated ambiguity flagged); GPT-5.5 price DOUBLED to $5/$30 (T2 Register) = frontier-pricing-power datapoint; custom chip "Jalapeño"/XPU unveiled 06-24 (Broadcom+TSMC, MP H2-26, T1 TechCrunch — TC-15 core member). Per `signals/cross-source-log/2026-07-08-morning-brief-b61-gauntlet-gpt56-fable5-sambanova-nand-check.md`.
- Watch: IPO progression (some sources hint at IPO timing acceleration); sovereign capital deal (likely Gulf state); Broadcom custom Si ramp; AWS Trainium volume consumption; Sol/Terra/Luna adoption + benchmark reception vs Fable 5

### xAI → SpaceXAI
- Status: **Acquired by SpaceX (all-stock, announced 2026-02-02, ~$1.25tn combined, T1 CNBC); formally rebranded "SpaceXAI" 2026-07-06 (T1 Engadget)**; large compute build (Colossus, ~1M H100-equivalent claimed in the 07-07 memo — memo-tier)
- Public-market relevance: NVDA customer; SpaceX IPO'd Jun-12; **acquiring Cursor $60bn all-stock (announced 2026-06-16 T1, closes Q3; in corpus since 06-17)**
- **2026-07-08 update (per `signals/cross-source-log/2026-07-08-twitter-batch-spacexai-cursor-zhipu-chip-china-model-curbs-3agent.md`):** first SpaceXAI+Cursor joint model reported launching "as soon as Wednesday" (The Information 07-07, MEMO-SOURCED SINGLE ORIGIN — Reuters could not verify, Cursor declined comment; internal claim: competitive with Opus 4.8/GPT-5.5 "in some respects," trained from scratch on Colossus). PARKED as weak signal pending actual release or 2nd independent T1. "Grok 4.5"/"1.5T V9" naming = T3 noise, discarded. Strategic frame: coding-app tier consolidating INTO a lab (application-layer framework §capture-stack validation).
- Watch: actual model release + benchmarks; Cursor deal close (Q3); whether Cursor traffic migrates off Anthropic/OpenAI models (see Anthropic entry)

### Mistral
- Status: French frontier provider; smaller scale
- Public-market relevance: EU sovereign AI vehicle; potential customer for European cloud
- Watch: EU government deals; partnership with French state

### Perplexity
- Status: AI-search vertical; smaller scale
- Public-market relevance: Customer for inference; potential acquirer or acquirer-target

## AI infrastructure / inference clouds

### CoreWeave
- Status: Largest specialized NVDA-rental cloud
- Public-market relevance: IPO candidate; NVDA dependency
- Watch: Revenue scale; hyperscaler competition reaction

### Lambda Labs, Crusoe Energy, similar
- Status: Smaller specialized infra
- Watch: M&A consolidation

## Defense / sovereign AI integrators

### Anduril
- Status: Defense AI/autonomy leader
- Public-market relevance: PLTR competitor/complement; defense AI spend grows

### Shield AI
- Status: Autonomous systems for defense
- Watch: Government contract progress

## Agent / AI-native infrastructure

### Various agent-platform startups (Hugging Face, LangChain, etc.)
- Status: Tooling for agentic builds
- Public-market relevance: TAM creation for compute and observability

## How to use this file

When a private co does something material (raises, partners, launches, gets acquired), it changes public-market dynamics:
- OpenAI IPO → re-prices the AI sector multiple
- Anthropic sovereign deal → confirms T6 (sovereign AI scaling)
- Custom Si partnership announcement at a hyperscaler → S2 evidence
- M&A in private inference clouds → consolidation theme

Update affected `companies/{TICKER}/interpretations.md` and run TRACE if material.

---

## OpenAI exclusivity premium compression (E5 candidate added 2026-06-03)

**Signal cluster:**
- OpenAI frontier models + Codex now available on AWS (beyond Azure exclusivity) per 2026-06-02 morning brief T1
- Microsoft launched MAI-Thinking-1 + MAI-Code-1-Flash own-frontier models at Build 2026 (June 2, 2026) per T2 Microsoft AI — hedging OpenAI partnership
- Combined signal: BOTH Microsoft AND OpenAI hedging the exclusive partnership simultaneously

**Implication:**
- OpenAI distribution moat (Azure exclusivity premium) compressing in real time
- ORCL Stargate positioning is one-step-removed-affected — Stargate buildout still happens but OpenAI exclusivity less load-bearing
- AVGO custom Si partnership with OpenAI (Titan) remains material but less unique vs MSFT-MAI alternative
- Anthropic positioning STRENGTHENS by comparison (Anthropic kept compute commitments + Surge AI for RLHF; less hyperscaler-dependent for distribution)

**E5 promotion criterion:** Any further hyperscaler-OpenAI relationship dilution within 90 days (e.g., Google adding OpenAI to GCP, OpenAI multi-cloud expansion to Oracle, OpenAI hardware diversification beyond NVDA).

**Affected public-market positioning (per Critical Rule #10):**
- ORCL Stargate thesis: marginally weakened (Stargate buildout intact but OpenAI exclusivity premium reduced)
- AVGO custom Si: TITAN program less differentiated vs MSFT in-house alternatives
- MSFT: strengthened (own-frontier optionality reduces OpenAI dependency)

## OpenAI leadership + IPO state (updated 2026-07-10; per `signals/cross-source-log/2026-07-10-morning-brief-b61-gauntlet-simo-msft-emissions-lyzr.md`)

- **Fidji Simo stepped down to part-time advisor Thu 2026-07-09** (her own staff note T1; medical — POTS relapse, on leave since Apr-2026). Title at departure: **"CEO, AGI Deployment"** (renamed from CEO of Applications — title correction booked 2026-07-10 after verifier refuted my garble-suspicion). No named successor; Brockman absorbed product scope during leave; Altman searching. "Pre-IPO leadership vacuum" = T2 editorial frame, held as frame not fact.
- **OpenAI confidentially FILED for IPO ~June 2026 — one week AFTER Anthropic's filing** (T2 multi-outlet via Simo coverage); timeline reportedly pushed to >=2027.
- **GPT-5.6 named "preferred model" in M365 Copilot Jul-9 (OpenAI's own words, T1)** — read as DEFENSIVE: Copilot is now explicitly multi-model (Claude = DEFAULT for Excel+PowerPoint since ~2026-05-04, Word to follow; MSFT elevating in-house MAI, this-week Word/Excel-to-MAI reports = the "breakup chatter"). **E5 exclusivity-premium-compression cluster: +1 datapoint (within the 90-day promotion window's spirit — relationship dilution continuing).**

## Anthropic governance (updated 2026-07-10)
- **Ben Bernanke appointed to the Long-Term Benefit Trust Thu 2026-07-09** (T1 anthropic.com + Bloomberg/CNBC independent). LTBT = the body that appoints/removes a board majority; trustees hold no equity. Framing explicitly scoped to AI-and-the-economy research — a named macro voice inside a lab. Governance color; no valuation surface. (B63-checked: facts hold on non-Anthropic sources.)

## Anthropic financial state (updated 2026-07-10, B63-hardened verification — non-Anthropic sources; per `signals/cross-source-log/2026-07-10-nvda-ndr-memory-jukan-cycle-anthropic-helium-3agent.md`)
- **ARR: $60B+ (SemiAnalysis Jul-8) / ~$69B (Yipit Jul-10)**; disclosed path $9B end-25 → $30B Apr → $47B mid-May. >=3 independent sources.
- **Profitability, correctly framed: first OPERATING profit ~$559M Q2-2026 EXCLUDING SBC** (WSJ/CNBC via internal investor materials ~May-20; non-GAAP). SemiAnalysis projects Q3 GAAP EBIT >$1B (~6% margin). **NOT free cash flow: The Information (T1) — cash-flow-positive target DELAYED to 2028** (~$12B training + ~$7B inference spend 2026). Blended gross margin ~65% (recovered from -94%); >80% = Opus-4.8 API per-token unit economics only; 77% = 2028 target. NEVER relay "FCF-positive"/"profitable" unqualified — that is the IPO-managed narrative (confidential S-1 ~Jun-1; OpenAI filed ~1wk later).

## Meta frontier-model state (updated 2026-07-10)
- **"Watermelon"** (internal, Wang to employees Jul-2 T2): caught up to **GPT-5.5** on watched benchmarks, **still in training**, needs ~10x Muse Spark compute; Opus-level coding model "pretty soon."
- **Muse Spark 1.1** shipped Jul-9 (Bloomberg): first paid Meta model, positioned ~Opus-4.8/GPT-5.5, aggressive pricing (~5.9x undercut, booked Jul-9).
- ICML rumor "internal model at Mythos-5 level, deployment-ready" = **REFUTED AS FRAMED** (escalates above both on-record claims; "still training" contradicts deployment-ready). Zero-weight color; "Meta not out of the race" = the fair kernel.

## Anthropic compute-financing structure (added 2026-07-10 EVE)
- **$35B Apollo+Blackstone-arranged credit facility: SPV purchases Google/Broadcom custom TPUs and LEASES them to Anthropic** (Bloomberg Jul-9 T2; Athene holds a slice). Delayed-draw, ~16 tranches over ~1yr; ~$15B expected tradeable by early 2027; no secondary price print yet (funding-shock node tell #8 armed). Read jointly with the same-day financials booking: op-profit-ex-SBC positive WHILE ~$19B/yr compute spend is partly off-balance-sheet via lease SPV — the profitability optics and the leverage live in different vehicles. B63 note: verified on non-Anthropic sources.
