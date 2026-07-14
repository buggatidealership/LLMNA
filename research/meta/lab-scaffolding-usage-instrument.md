# LAB SCAFFOLDING-USAGE INSTRUMENT (born 2026-07-14, user-commissioned 9-agent workflow ≈ 513k tokens; directive: "if the data is non existing, say so. if it is hard to compute, do it anyway using proxy data")

**What this is:** the usage-truth layer for frontier labs' user-specific agent scaffolding (custom GPTs, Projects, Memory, Skills, Gems, Copilot agents) — the layer the §6b debate turns on. Companion to `meta/education-ai-adoption-instrument.md` (vertical module #1); this is the SCAFFOLD module. The created-vs-used distinction is this file's registered-vs-active. Cadence per §5 series table; re-eval trigger: Anthropic S-1 publication (~Aug 2026) or next OpenAI Enterprise report, whichever first.
**Process note (failure-mode #7 instance, N=1):** first commissioning attempt was misread as edtech-app tracking — anchored on the concrete noun ("education") instead of the conversation thread (scaffolding); user-corrected same session. If this interpretation class recurs, graduate to a lesson.

# SCAFFOLDING-USAGE — First Reading
**Commissioned:** 2026-07-14 · Directive (verbatim-adjacent): *"frontier ai labs usage of their user specific agent scaffolding. if the data is non existing, say so. if it is hard to compute, do it anyway using proxy data."*
**Method note:** every claim carries [tier] + source; created-vs-used labels per the 20-row audit. 🟢 = T1 receipt · 🟡 = T2/my-model · 🔴 = speculative.

**TL;DR:** Only ONE true scaffold attach-rate exists in public (OpenAI: ~20% of Enterprise messages via Custom GPT/Project). Everything else labs publish about scaffolding is created-counters — hype artifacts, several frozen for 12–30 months. Doing the arithmetic anyway: user-weighted active scaffold penetration is ~3–8% of the combined user base, but token-weighted it is plausibly 30–55% — the scaffold layer is created-and-abandoned at consumer scale and alive-and-compounding in a small enterprise/agentic tail.

---

## 1. WHAT IS ACTUALLY KNOWN (the few real usage numbers)

### Genuine USAGE metrics (survive audit)

| Lab | Metric | Value | Tier/validity |
|---|---|---|---|
| OpenAI | **% of Enterprise messages via Custom GPT or Project** — the only message-level attach any lab has published | **~20%** @2025-12 | 🟢 T1 official report, validity A- (rank 1/20) — openai.com/index/the-state-of-enterprise-ai-2025-report/ |
| OpenAI | Consumer GPT attach (independent panel) | 2.7% ww / 4.1% US of ChatGPT web traffic @2024-01; 56.5M GPT visits/mo vs multi-billion total @2025-03 | 🟡 T2 Similarweb — similarweb.com/blog/insights/ai-news/chatgpt-custom-gpts/ |
| OpenAI | Codex WAU | ~5M @2026-06 (6x in 4 months — launch-surge-heavy; do NOT use the 6M headline, unconfirmed window/scope) | 🟡 T1-via-T2 — constellationr.com |
| Anthropic | Claude Code metered revenue (usage in dollars — usage-priced, so revenue ≈ usage) | **>$2.5B run-rate** @2026-02 (official floor, ~5mo stale); Sacra $8B = scenario only | 🟢 T1 (Feb) / 🔴 T3 (May) — saastr.com |
| Anthropic | Claude Code share of public GitHub commits — the dataset's only third-party-REPRODUCIBLE usage stat | ~4% @early-2026 (undercounts via squash-merges) | 🟡 T1/T2, validity B+ — anthropic.com/economic-index |
| Anthropic | Claude Code WAU | ~2M ±50% @2026-05 (press, never official; 4.2M figure is timeline-disproven T3 slop) | 🟡 T2 — cryptobriefing.com |
| Anthropic | Cowork task mix (the usable finding; 1.2M = sample size, NOT volume; 600K orgs = trial-breadth, ~2 sessions/org) | ~90% non-coding: 33.4% biz-ops / 16.4% content / 8.7% swdev (±5pp) @2026-07-07 | 🟡 T1-via-T2, validity B+ — venturebeat.com |
| Anthropic | Economic Index conversation mix | 52% augmentation / 45% automation @2025-11 data | 🟢 T1 research — anthropic.com/research/economic-index-june-2026-report |
| Google | Gemini Enterprise paid MAU growth | +40% QoQ @2026-04-29 — genuine active-paid disclosure but BASE-FREE; 8M seats = entitlement | 🟡 T1 earnings, validity B- — blog.google Q1'26 |
| Microsoft | M365 Copilot paid-seat attach | >20M seats vs 450M commercial = **~4.4% attach** @FY26-Q3 | 🟢 T1 earnings — nojitter.com |
| Microsoft | Copilot credit consumption (the ONLY MS agent-usage signal) | ~2x QoQ "as customers extend Copilot with custom agents" @FY26-Q3 | 🟡 T1-via-T2 spend proxy — alphastreet transcript |
| GitHub | Paid subs (renewal-gated) + agent output | 4.7M paid +75% YoY @2026-01; agent ~1.2M PRs/mo vs 43.2M merged = low-single-digit % of PR flow | 🟢 T1 — mlq.ai; github.blog Octoverse |
| Cross-lab | Ramp card-spend (behavioral, third-party) | Anthropic 34.4% vs OpenAI 32.3% of US businesses paying @2026-04/05 (adoption, not intensity) | 🟡 T2 panel, validity B — ramp.com/data/ai-index |
| Cross-lab | Agentic intensity | ~15x tokens per agentic task vs chat; reasoning share ~0%→>50% during 2025 | 🟡 T2 OpenRouter/a16z, dev-skewed — a16z.com/state-of-ai |

### CREATED-counters — label them and discard as usage
- OpenAI **3M GPTs created** @2024-01 — validity F, 30 months frozen, ~95% never published. Discard [T1-stale — openai.com/index/introducing-the-gpt-store/].
- Anthropic **500M+ artifacts** @2025-06 — auto-emitted model side-effects, validity D-, 13mo stale [T1/T2 — anthropic.com/news/artifacts].
- Microsoft **3M agents created FY25** (terminal disclosure, Jul 2025) + **Agent 365 "tens of millions" registered** (~1,000 agents/org 2mo post-preview = bulk auto-registration) — validity F [T1 earnings].
- GitHub Copilot **26M "users"** — spokesperson-CONFIRMED cumulative ever-tried, not active [T1, reclassified created-counter].
- Meta AI Studio **"hundreds of thousands"** characters, most private, ~18mo stale — validity F [T2].
- MCP **9,652 registry servers / "10,000+ active"** — supply-side; independent audit: only ~17% production-grade → **~1,600–2,000 real servers** [T3 audit — rapidclaw.dev].

---

## 2. WHAT DOES NOT EXIST (per directive: saying so plainly)

**OpenAI — no data has ever been disclosed for:** Memory adoption/opt-out % (default-on since Apr 2025 makes it near-meaningless anyway); Tasks usage (only per-tier caps); Operator/agent-mode WAU (sunset Aug 2025 with zero stats; T3 panel: ChatGPT Agent <1M weekly); Canvas usage; Connectors attach; consumer-side Projects. OpenAI's own NBER paper (1.5M conversations) and Signals Q1'26 never classify whether a conversation ran inside a scaffold — **the personalization layer is invisible in the lab's own usage research.**

**Anthropic — no data for:** Projects (nothing since Jun 2024 launch); Memory adoption %; Skills invocations/installs — and circulating "Skills Marketplace / 47% token reduction" stats are traceable only to SEO farms, **treat as fabricated**; Artifacts active usage (only created-counters); Connectors attach; Cowork distinct users/seats. The confidential **S-1 (public filing expected ~Aug 2026) is the single biggest upcoming T1 catalyst.**

**Google — no data for:** Gems — ZERO disclosures ever (created, active, or attach) since Aug 2024; absent from I/O 2026 and Q4'25/Q1'26 calls. Project Mariner shut down 2026-05-04 with no usage stats ever. Jules: quotas only. NotebookLM total (web+mobile) MAU never given as one number. Gemini memory/personalization %: nothing.

**Microsoft — retired/stale:** agents-created counter DROPPED after FY25 Q4; Copilot Studio 230K-orgs figure ~14 months stale; Copilot 150M MAU not refreshed after FY26 Q1, replaced by base-free ratios — metric rotation after the "empty agents" criticism is dodge-as-data. Copilot Workspace sunset with no numbers; no % of Copilot seats invoking agents, ever.

**Structural gaps (why nobody can measure this from outside):** no survey/panel publishes % of users using memory/projects/personalization at ANY lab; post-2024 feature-level panel measurement became impossible because Projects/Skills/Gems live behind app-internal routes with no URL paths (unlike 2024's `/g/` GPT paths Similarweb caught); nobody audits Anthropic's "active" MCP-server qualifier; **xAI/Grok, Mistral, DeepSeek scaffolds = open coverage gap, not verified nonexistence.**

---

## 3. PROXY COMPUTATION — the arithmetic done anyway

**Target:** % of lab users actively using persistent-personalization/scaffold features ("active scaffold penetration"), plus token-weighted share.

**Chain A — Enterprise attach (anchor):**
- Input: ~20% of Enterprise messages via GPT/Project [T1] on ~9M paying business seats [T1 DevDay/press].
- Assumption (my model): message-attach ≈ user-attach ±; Projects (a folder + instructions — barely a scaffold) likely majority of the 20% → heavyweight-scaffold share ~⅓–½ of it.
- → **Enterprise: 15–25% any-scaffold; ~7–10% heavyweight** 🟡.

**Chain B — Consumer attach:**
- Input: Similarweb 2.7–4.1% of ChatGPT traffic to GPTs [T2]; GPT visits FELL pre-Store; 56.5M/mo vs multi-billion total in 2025 implies ~1–2%.
- Assumption: consumer Projects/memory-as-chosen adds a little; memory default-on is ambient, not usage.
- → **Consumer: 2–4% active scaffold use** 🟡.

**Chain C — User-weighted blend:**
- Denominators: ChatGPT 900M WAU @2026-02-27 [T1]; business seats ~1% of that. Claude ~31M MAU (18.9M web + 12.5M mobile [T2/T3]); Gemini 900M+ [T1]; Copilot 150M stale [T1].
- Blend: 0.99 × (2–4%) + 0.01 × (15–25%) ≈ **2–4% for OpenAI-like bases**.
- Outlier: Anthropic — Claude Code ~2M WAU / ~31M MAU ≈ **~6–7% of the Claude base is heavyweight-agentic** (my model; both numbers T2) — the one lab where the scaffold tail is a visible share of the base.
- Haircuts from survey gaps [T3, use gaps not levels]: Bain exec-claim 97% vs employee-use 52% (≈2x inflation); Menlo: only 16% of "agent" deployments are true agents; MIT NANDA: 90% personal vanilla use vs 40% official — vanilla chat still dominates behavior.
- → **RANGE: user-weighted active scaffold penetration ≈ 3–8% across the major labs' combined bases** 🟡 (my model; upper end only if Copilot-seat and Claude Code cohorts are counted at full weight).

**Chain D — Token-weighted (intensity correction):**
- Input: agentic task ≈ 15x chat tokens [T2 OpenRouter/a16z].
- Arithmetic (my model): if p = scaffolded-user fraction, token share = 15p/(15p+(1−p)). p=3% → 32%; p=5% → 44%; p=8% → 57%.
- Cross-checks: reasoning-token share >50% late 2025 [T2]; Google tokens 7x YoY vs Gemini MAU ~2.25x → per-user intensity ~3x [T1-derived]; 4 of top-5 OpenRouter apps agentic [T2]; Claude Code $2.5B of Anthropic ~$14B ARR @Feb-2026 ≈ ~18% of revenue from one scaffold product [T1].
- → **RANGE: token/value-weighted scaffold share ≈ 30–55%** 🟡 (my model; dev-panel-skewed inputs, so treat the upper half cautiously).

**Bottom line of the computation:** penetration is LOW by users (3–8%), HIGH by tokens/dollars (30–55%). Both can't be summarized by one number — the distribution is the finding.

---

## 4. WHAT IT MEANS FOR 6b (hyperpersonalization vs scaffold)

1. **Consumer hyperpersonalization is mostly created-and-abandoned.** Every consumer-facing scaffold counter is a frozen creation metric (3M GPTs, 500M artifacts, Meta characters), consumer attach is ~2–4% [T2], and no lab will disclose memory/projects usage — vendor silence on flattering-metric-shaped questions is itself evidence of unflattering answers 🟡. The "personalization layer" as a consumer moat is, on current public evidence, NOT being used at scale.
2. **The scaffold thesis survives — relocated.** It lives in the enterprise workflow container (20% Enterprise message attach [T1], Copilot credits 2x QoQ [T1-via-T2]) and the agentic-developer tail (Claude Code $2.5B+ metered [T1], ~4% of public commits [T2], agent PRs low-single-digit % of GitHub flow [T1]).
3. **Investment translation (ties to T1/TC-8 token-consumption theme):** per-user intensity (3x/yr at Google, 15x per agentic task) is the compounding variable, not user counts. Scaffold-driven token demand is a tail-concentration story — bullish for inference infrastructure regardless of whether consumer personalization ever attaches 🟡.
4. **Default-on personalization (OpenAI memory Apr-2025, Claude free-tier Mar-2026) dissolves the question:** labs are making personalization ambient precisely because opt-in usage was low — "usage %" of memory is being defined out of existence 🔴 (inference).

---

## 5. TRACKING DESIGN — series that would detect scaffold-usage inflection

| # | Series | Source / cadence | A move means | Access |
|---|---|---|---|---|
| 1 | OpenAI Enterprise scaffold attach (the 20% figure) | openai.com State of Enterprise AI, ~annual | >25–30% = enterprise inflection; **non-refresh = negative tell**; demand GPT-vs-Project split | Free |
| 2 | **Anthropic S-1** (public ~Aug 2026) | SEC EDGAR, one-shot | First audited Claude Code/Cowork revenue & user decomposition — biggest single truth catalyst | Free |
| 3 | Claude Code share of public GitHub commits | Reproducible GitHub query (Co-Authored-By trailers), monthly | Sustained rise past ~6–8% = agent-authored code inflection; only third-party-verifiable series | Free (compute) |
| 4 | MSFT Copilot credit consumption QoQ + paid seats | Earnings calls, quarterly | Credits decelerating while seats grow = shelfware; credits >2x sustained = real agent pull | Free |
| 5 | Ramp AI Index — % firms paying per lab; push for spend-weighted | ramp.com, monthly | Spend-weighted Anthropic share rising = agentic revenue thesis confirmation | Free |
| 6 | OpenRouter token mix (agentic vs chat) | openrouter.ai rankings/blog, monthly | Agentic share crossing 50%+ of tokens = intensity thesis confirmed (panel dev-skewed) | Free |
| 7 | Anthropic Economic Index / Cowork reports | anthropic.com / claude.com blog, ~quarterly | Cowork biz-ops share + aug/auto ratio shifts; **claude.com primary 403'd — BROWSER-SESSION LIST** | ⚠️ Blocked |
| 8 | Similarweb ChatGPT/Claude feature-path traffic | similarweb.com, monthly | Mostly dead post-2024 (no URL paths) — keep as canary for any re-exposed paths; **full data paywalled — BROWSER-SESSION LIST** | ⚠️ Paywalled |

---

## 6. FALSIFIER FOR THIS READING

The reading claims: **consumer scaffold attach ~2–4% and stagnant; scaffold value concentrated in a 3–8%-of-users / 30–55%-of-tokens enterprise-agentic tail.** It is falsified if any of:
1. A lab discloses (T1) consumer memory/Projects/GPT attach **>15% of messages** — consumer personalization alive, reading's core dead-layer claim wrong.
2. OpenAI's next Enterprise report shows scaffold attach **falling below ~15%** — the "live enterprise container" half breaks; the whole scaffold layer, not just consumer, would be created-and-abandoned.
3. Anthropic S-1 shows Claude Code + agentic products **<10% of revenue** — the tail-concentration/dollar-weighted claim breaks (current basis: $2.5B of ~$14B @Feb-2026).
4. A credible panel/audit shows agentic token intensity **<5x** chat (vs 15x input) — the 30–55% token-weighted range collapses toward the user-weighted 3–8% and the intensity thesis (TC-8 linkage) needs rebuild.

Re-eval trigger: on S-1 publication (~Aug 2026) or next OpenAI Enterprise report, whichever first.
