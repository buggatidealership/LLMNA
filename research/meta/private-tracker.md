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
- Status: Strong #2 to OpenAI in scale, but passed OpenAI in enterprise share by April 2026
- Public-market relevance: Compute customer (AMZN AWS, GOOG); Anthropic-Amazon partnership deep; Anthropic-AVGO custom Si partnership announced May 2026
- **2026-06-11 update (per `signals/cross-source-log/2026-06-11-june10-evening-brief-triage-b40-n9.md`):**
  - **MSFT restricted internal employee use of Fable 5** (removed from internal GitHub Copilot model picker) over the Mythos-class retention requirement — which **overrides existing ZDR agreements** (T1 Anthropic Help Center: 30-day retention all platforms, up to 2 years if classifier-flagged). MSFT simultaneously sells Fable 5 via Foundry = customer-balking, not competitor positioning (T2 Verge/Reuters).
  - Named-researcher false positives (Unutmaz/Jackson Lab, Verdon) + **Anthropic acknowledged safeguards too stringent** (T2 The Register).
  - **H2 enterprise-trust-tax: P~30% → P~45% (my model, Bayesian: 2nd hyperscaler + acknowledged false positives + ZDR-override).** Threshold to dominant: 3rd named enterprise restriction (P~60%+, my model, directional). Watch Forrester-style vendor-risk advisories converting into named policies.
- **2026-06-10 update (per `signals/cross-source-log/2026-06-10-morning-brief-6-claim-verification-anthropic-spacex-dc.md`):**
  - **Fable 5 + Mythos 5 launched June 9** (first public Mythos-class). System card (T1, 319pp) discloses **silent capability-degradation interventions** on frontier-LLM-development tasks (~0.03% traffic, <0.1% orgs; prompt modification/steering/PEFT, invisible at runtime). "Sabotage" claims UNSUPPORTED; cyber/bio/chem/distillation requests reroute to Opus 4.8, not refused. Enterprise-trust impact: H1 negligible P~60% / H2 slow-burn trust-tax P~30% / H3 escalation P~10% (my model).
  - **Bedrock first-breach:** Mythos-class invocation requires opt-in `provider_data_share` (prompts/completions to Anthropic, ≤30-day trust-safety retention, not training — T1 AWS docs). First crack in Bedrock's no-provider-sharing norm; narrow but precedent-setting.
  - **Comparative position vs OpenAI strengthening:** Anthropic technical wins now a NAMED OpenAI-collateral-risk factor (Bloomberg native-jp, SoftBank $6B margin-loan stall 2026-06-10); Google's $4.99 consumer price cut pressures OpenAI's consumer line while Anthropic stays enterprise-weighted. P~60% (my model) OpenAI-funding-stress hardens into Q3 narrative with Anthropic as relative beneficiary.
  - SpaceX $45B compute deal = GROUND (xAI Colossus, 220K NVDA GPUs, 300MW per 2026-06-07 verification file); orbital = "interest" only (T2). SpaceX IPO June 12.
- **2026-07-25 update (per `signals/cross-source-log/2026-07-25-opus5-vs-fable5-model-layer-deep-dive-4agent.md`, 4-agent deep dive):**
  - **Claude Opus 5 launched 2026-07-24** at $5/$25 per Mtok — **a price point unchanged since Opus 4.5 (Nov 2025)** across four model generations (T1 Anthropic pricing docs). "Half the price of Fable 5" ($10/$50) is a sibling comparison at a static price point, **NOT a price cut**. Realised saving is ~26% per task ($2.03 vs $2.75, Artificial Analysis via The Register), not 50%, because Opus 5 thinks by default and burns more tokens.
  - **Fable 5 / Mythos 5 are twins from one training run** (T1): Fable = public safety-gated GA; Mythos = same weights with cyber/bio safeguards lifted, invitation-only via **Project Glasswing**, not on claude.ai. Family hierarchy Mythos > Fable > Opus > Sonnet > Haiku. Both Opus 5 and Fable 5 sit at **ASL-3** — the 85%-fewer-cyber-classifier-interventions claim is operational friction, not RSP reclassification.
  - **TRUST-TAX THREAD PARTIALLY RESOLVES — H2 P~45% -> P~30% (my model).** Opus 5 ships with **NO data-retention requirement for general access** (T1 verbatim), whereas Fable 5 + Mythos 5 keep the 30-day Mythos-class policy that overrode ZDR and triggered the MSFT internal restriction in June. Anthropic **engineered around its own trust tax** rather than absorbing it. Mechanism confirmed material; revenue consequence now mitigated by a product route. The pre-registered "third named enterprise restriction" threshold is now less likely to be hit on the Fable line. Re-eval: do enterprise accounts migrate Fable->Opus 5, or leave?
  - **Capability:** Anthropic's own system card (193pp, T1) states plainly *"Claude Opus 5 is not more capable overall than our most capable general-access model, Claude Fable 5."* Opus 5 **loses** to Fable 5 on SWE-bench Pro (79.2 vs 80.0), DeepSWE (68.8 vs 69.7), FrontierCode (53.4 vs 53.5) and HLE-no-tools (56.3 vs 56.5). The "within 0.5%" marketing figure is scoped to **CursorBench 3.2 only**, which does not appear in the system card at all. GPQA/AIME/MMMU are absent from the entire card — benchmark comparability across labs is degrading by construction.
  - **Margins (the H1 answer):** SemiAnalysis models Anthropic inference gross margin **38% -> >70%** in ~1yr, explicitly attributed to a genuine cost breakthrough (Trainium + Nvidia software efficiency, Hopper->Blackwell, premium-tier mix) and **explicitly NOT** compression or subsidised land-grab (T2, direct fetch). This CONTRADICTS the margin-compression read logged 2026-07-24 — corrected.
  - **Business state (private-tracker figures above are STALE):** valuation **$965B** with confidential IPO filing **2026-06-01** (up from $350B Nov-2025, T2 N>=3); ARR ~$47B May-2026 from ~$9B end-2025 (T2 estimate, not a filing); enterprise-LLM share **40% vs OpenAI 27%** (Menlo Ventures Dec-2025, named methodology).
  - **Contracted compute (physical-layer reach):** AWS $100B+/10yr, up to 5GW Trainium (T1 2026-04-20); Google $200B/5yr, up to 1M TPUs, up to 5GW; NVDA up to $10B + 1GW; MSFT up to $5B + $30B Azure + 1GW.
  - **PC-14 escalation — export control applied to a MODEL:** US Commerce Dept restricted then cleared wider Mythos 5 access for "trusted partners" (Bloomberg 2026-06-26 + Fortune 2026-06-27, T2 N=2). The control surface has moved from silicon to weights-and-access. Separately, **White House OSTP Director Michael Kratsios accused Moonshot of covert distillation of Fable 5 on 2026-07-22** (T2 N>=4) + alleged GB300 smuggling via Thailand; Moonshot denied; independent researchers sceptical; **claim UNPROVEN in both directions**. The 25-company open-weight letter landed **two days later** — it is a RESPONSE, not an independent event. Note Fable 5 ships an **anti-distillation classifier** blocking third parties from distilling its outputs.

- Latest signals (2026-05-20, per [WSJ via Investing.com](https://za.investing.com/news/economy-news/anthropic-revenue-set-to-more-than-double-to-109-billion-in-q2-4293058) and [Sherwood News](https://sherwood.news/markets/anthropic-revenue-run-rate-30-billion-google-broadcom-partnership/)):
  - Q1 2026 revenue: $4.8B
  - Q2 2026 forecast revenue: $10.9B (~+127% q/q, ≈ "130% surge" per headline)
  - Q2 2026 forecast operating profit: **$559M — first ever** (includes training costs, excludes SBC)
  - Annual run rate: $30B (per Sherwood News)
  - Prior guidance had been: no profitability until 2028 at earliest
  - Caveat: may not stay profitable full year due to compute + training capex
  - Expanded partnerships announced: **Google + Broadcom** (the AVGO custom Si angle is the under-noticed detail)
- Watch: IPO progression (some sources hint at IPO timing acceleration); sovereign capital deal (likely Gulf state); Broadcom custom Si ramp; AWS Trainium volume consumption

### xAI
- Status: Musk-backed; large compute build (Colossus)
- Public-market relevance: NVDA customer; sovereign capital backing
- Watch: Compute scale; integration with X platform

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

## Semiconductor equipment startups

### xLight
- Status: Pat Gelsinger (ex-Intel CEO) startup; raised **$350M** (2026-07 round) to build the first American EUV lithography rival to ASML — 🟡 T3 Semi Doped newsletter relay of Startup Fortune, seen 2026-07-23; per `signals/cross-source-log/2026-07-23-semidoped-quicktakes-7item-newsletter-ingest.md`
- Public-market relevance: nominal ASML competitive-map entry; realistic threat horizon 10+ years (my model — EUV took ASML ~2 decades with an exclusive Zeiss optics chain; $350M funds a research program, not a toolchain). Strategic-signal value is US litho-sovereignty ambition (PC-14 thread), not near-term ASML thesis impact.
- Watch: national-security funding attach (CHIPS-II / DoD), optics-supplier partnerships, credible tool-architecture disclosure. No ASML thesis change unless government-scale capital commits.
- Added: 2026-07-23

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
