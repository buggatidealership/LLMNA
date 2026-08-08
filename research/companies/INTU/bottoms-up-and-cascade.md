# INTU — BOTTOMS-UP UNIT MODEL, MACRO ANCHOR, AND N-TH ORDER CASCADE

**Created 2026-08-08.** Written because three Stop hooks fired on the first version of the INTU thesis — `bottoms-up-hook` (forward projection without unit economics), `nth-order-cascade-hook` (causal reasoning stopping at 1st order), `macro-anchor-hook` (position-relevant output without a dated first-principles anchor). All three were correct: the thesis carried a multiple argument and a scenario map but **no unit model, no cascade, and no macro frame**. This file supplies them. Companion to `thesis.md` / `facts.md` / `interpretations.md`.

---

## 0. MACRO ANCHOR — first-principles read as of 2026-08-08 (Critical Rule #15 / Workflow #9 step 1)

**The layer being entered is new to this corpus.** Before 2026-08-08 there were zero files on Intuit and effectively zero on enterprise/SMB software as an investable layer — the corpus is a semiconductor and AI-infrastructure corpus. This section exists so the company work below is not floating on pre-training.

**Date-anchored state of the layer (research-verified 2026-08-08, tiers marked):**

| Fact | Tier |
|---|---|
| S&P 500 closed at a record **7,757.64** on 2026-08-07 | 🟢 T1 — EODHD `GSPC.INDX`, fetched this session; cross-confirmed by CNBC |
| Nasdaq **+5.2% in the week to 2026-08-07** on a snap-back in chip stocks; July payrolls printed a surprise **decline**, pushing rate expectations toward "on hold" | 🟡 T2 — press, 2026-08-07 |
| 2026 has run as a **value/cyclical-over-growth year**: energy, staples, materials and industrials led while Information Technology lagged YTD | 🟡 T2 — multiple secondary aggregations; the precise sector figures did NOT reconcile against index arithmetic when I checked them, so **direction only, magnitudes discarded** |
| **February 2026 "SaaS-pocalypse":** the S&P software & services complex shed roughly **$1 trillion** of market value from late January on agentic-AI disruption fear. Adobe, Salesforce and ServiceNow each −25–30% YTD; Intuit −50%; CoStar −59% | 🟡 T2 — press, cross-referenced across three outlets |
| Capital rotated **into** AI-capex winners in the same window — SanDisk +505%, Dell +248%, Micron +223% | 🟡 T2 |

**First-principles statement derived from the above (not from pre-training):** 2026 is the year the market began **pricing agentic AI as a transfer of value, not just a creation of it** — bidding the suppliers of AI capacity and selling the incumbent owners of knowledge-work workflows, as a single paired trade. The paired-trade structure is the macro fact. Intuit is not a stock-specific de-rating; it is a **position in the short leg of the market's largest active thematic.**

**Tie-together (mandatory B46 contradiction check):** does anything in the Intuit micro-detail contradict this macro read, or contradict a credible institutional signal? **Yes, one thing, and it is surfaced rather than buried.** The macro read says the market is selling incumbent workflow owners. Intuit's own management responded by announcing an **$8B buyback authorisation and a 15% dividend increase in the same release as a 17% headcount reduction** — i.e. the largest insider-adjacent capital commitment in the company's recent history, taken *into* the de-rating. That is a credible institutional signal pointing the other way from the tape. Per Critical Rule #15, when micro contradicts a credible institutional signal the **framing** is what is incomplete. The resolution adopted in `thesis.md` — that the market is pricing Bear A (displacement) while Bear B (price-carried decay) is what is actually happening — is that reframing. **Counter-signal that cuts the other way and is recorded for symmetry: there has been no insider open-market buying** with the stock down 58%. Buybacks are the company's money; Form-4 purchases would be management's. Only one of those two signals is present.

---

## 1. BOTTOMS-UP UNIT MODEL (methodology principle #1 — build from units × price, compare to the outside view LAST)

Every input tagged **DISCLOSED** (Intuit primary), **DERIVED** (computed here), or **(my model)**.

### Step 1 — back the unit base out of disclosed revenue

**DISCLOSED** (Q3 FY26 press release): QBO Accounting revenue rose **$234M, or 22%**, in Q3 FY26.

```
DERIVED:  prior-year Q3 = 234 / 0.22          = $1,064M
          Q3 FY26       = 1,064 + 234          = $1,298M
          annualised run-rate (QBO is non-seasonal, unlike TurboTax) = $5,191M
```

### Step 2 — implied subscriber base at disclosed list prices

**DISCLOSED** (`quickbooks.intuit.com/pricing`, fetched 2026-08-08, post the Aug-1 increase): Simple Start **$38**/mo · Essentials **$85** · Plus **$140** · Advanced **$340**.

**(my model)** tier mix 42 / 26 / 26 / 6 → blended list **$95/mo = $1,138/yr**.

| effective-vs-list realisation | implied ARPC | implied subscribers |
|---|---|---|
| 50% | $569/yr | **9.12M** |
| 60% | $683/yr | **7.60M** |
| 70% | $797/yr | **6.52M** |

**Read:** 6.5–9.1M brackets Intuit's last-disclosed QBO base (~8–9M, **recall-based — verify before sizing**; Intuit stopped disclosing it, which is precisely why thesis falsifier **F1 carries a blind-check**). The model is **internally consistent** with disclosed revenue and disclosed list prices. It is **not** independent confirmation of the base.

### Step 3 — the revenue FLOOR from the installed base alone (the capacity-gate analogue)

The binding constraint here is not customer acquisition. It is **whether the installed base survives a 41–70% list-price increase.** So build the floor from price alone, assuming **zero net new subscribers**.

**DERIVED:** revenue-weighted blended list increase = **+40.6%**.
At ~8M subscribers, **each $10/month of realised price = 8e6 × $10 × 12 = $960M/yr.** The Aug-1 increase moved blended list by ~$38/month.

| realisation × churn | QBO Accounting revenue | vs run-rate |
|---|---|---|
| 30% × 0% | $5,822M | **+12.2%** |
| 30% × 5% | $5,531M | **+6.6%** |
| **30% × 10%** | **$5,240M** | **+1.0%** ← the churn level that kills it |
| 45% × 5% | $5,831M | +12.3% |
| 60% × 5% | $6,131M | +18.1% |

**This is the whole investment question reduced to one number: churn.** At 30% realisation, the thesis needs churn below ~10% for the installed base alone to hold revenue flat. Falsifier F1 (QBO Accounting growth <18%) is the observable proxy, because Intuit will not give us churn directly.

### Step 4 — TurboTax, and an inconsistency I am not going to smooth

**DISCLOSED:** total online units **−2%** · paying units **+2%** · ARPU **+11%** · pay-nothing customers 8M → 7M · TurboTax Live **$2.8B, +36%**, customers +38%.

```
NAIVE BUILD:  paying units +2%  ×  ARPU +11%  =  +13.2%
DISCLOSED  :  FY26 TurboTax revenue guide $5.277-5.282B  =  ~+7%
⚠️ GAP OF ~6 POINTS. UNRECONCILED.
```

Most likely explanation is that ARPU is quoted on a different base than paying units (mix), but **I cannot close it from disclosed data and I am not going to assume it away.** The gap is itself a reason the **Aug-25 print matters**: it is where the decomposition gets restated.

**DERIVED:** non-Live DIY TurboTax = 5,280 − 2,800 = **$2,480M**.
**Read:** the genuinely LLM-substitutable part — pure DIY tax software — is now **~$2.5B, about 12% of company revenue.** Goldman's rhetorical anchor ("$0.12 per return vs $162") attacks that 12%. It does not touch the 88%.

### Step 5 — FY27 revenue built from the parts, THEN compared to the outside view

| Segment | FY26e $M *(my model allocation)* | low g | high g | Driver |
|---|---|---|---|---|
| Global Business Solutions | 13,000 | 13% | 16% | QBO price realisation + IES/Advanced ~+38% |
| Consumer (TurboTax) | 5,280 | 4% | 8% | Live +36% offsetting DIY unit decline ~−2% |
| Credit Karma | 2,400 | 8% | 15% | decelerated +23% → +15% through FY26 |
| ProTax | 750 | 2% | 5% | flat-to-low-single |

**BOTTOMS-UP FY27 REVENUE = $23,538M – $24,330M = +10.2% to +13.9%** vs FY26's $21,357M.

⚠️ The FY26 segment bases are **(my model)** allocations of the guided $21,357M total, anchored on disclosed Q3 segment revenue and disclosed FY growth guides. They are not filed segment splits.

**Comparison to the outside view, done last (principle #1, lesson L1):** sell-side FY27 consensus clusters **~+11–12%**, which sits **inside** my band rather than above it.

**⇒ I claim NO edge on the revenue line, and the thesis does not need one.** This is the important structural point: the argument in `thesis.md` is entirely about the **terminal multiple**. A bottoms-up build that merely *agrees* with consensus revenue is the correct supporting result — it removes the revenue line as a source of disagreement and isolates the disagreement where I actually claim it.

---

## 2. N-TH ORDER CASCADE (methodology principle #2 / Workflow #2 TRACE)

**Trigger:** agentic AI becomes reliable enough to execute bounded knowledge-work tasks end to end.

**1st order (P>80%)** — the price of standalone DIY workflow software falls. Vendors whose product *is* the workflow interface lose pricing power first. **Casualty:** pure-UI point tools; Intuit's ~$2.5B non-Live DIY TurboTax line; Adobe's creative-workflow core. **This is the order the market has priced, and the only one it has priced.**

**2nd order (P~60%)** — value migrates to whoever holds the **system of record plus the regulated money rails**, because an agent needs a ledger to write to and a licensed counterparty to move money through. **Beneficiary:** Intuit's Online Services — disclosed Q3 growth of +$160M split **money +$107M, payroll +$55M**; QBO Advanced + Intuit Enterprise Suite at ~+38%. **Casualty:** AI-native challengers who can do the *reasoning* but cannot be the *counterparty* — becoming a money transmitter in 50 states is a licensing problem, not a model problem.

**3rd order (P~40%)** — incumbents' cost-to-serve falls faster than their realised price, so **gross margins rise while growth slows**: the high-margin-utility end-state. Intuit's 9M FY26 operating margin already moved 30.6% → 31.6% while SBC fell 9.9% → 9.1% of revenue. **Beneficiary:** incumbents with owned distribution. **Casualty:** challengers who must *buy* distribution at full price into a market whose ASP is falling — the worst possible entry economics.

**4th order (P~20%)** — the accountant/advisor channel **re-intermediates** as the liability-bearing layer, because someone must carry the consequence when an agent gets payroll tax wrong. Intuit's ProTax + ProAdvisor network and TurboTax Live become *more* valuable, not less. **Weak corroboration already on the tape:** TurboTax Live customers **+38%** with retention **+2 points**; Accounting Today's 2026-07-27 headline runs *"Clients value human relationships over AI efficiencies."* **Casualty:** the disintermediate-the-accountant startups.

**Names whose exposure changed by this cascade:**

| Name | Direction | Order | Why |
|---|---|---|---|
| **INTU** | beneficiary at 2nd/3rd/4th, casualty at 1st | mixed | 12% of revenue is exposed at 1st order; ~88% sits at 2nd order or later |
| **ADBE** | casualty | 1st | Its core product is what generative models do natively. **This is the reasoning behind `interpretations.md` I4** — why Intuit over the cheaper de-rated name at ~10× forward. It is a contestable judgment, not a fact |
| **PLTR** *(held)* | beneficiary | 2nd | Sits on the same side of the 2nd-order migration — value accrues to the system of record. **Note the overlap honestly: INTU and PLTR are NOT opposite bets on this axis**, they are the incumbent and the challenger expression of the same 2nd-order claim |
| **AMZN** *(held)* | beneficiary | 2nd/3rd | Money rails + owned distribution |
| **NVDA** *(held)* | beneficiary | 1st | Long the capacity that makes the 1st order happen — i.e. **long the leg that shorts Intuit's 12%** |

**Portfolio read (joint-state, my model):** the honest finding is *not* that Intuit hedges the book. Adding INTU raises exposure to the 2nd-order "value accrues to the system of record" claim that **PLTR already expresses**, while adding a genuine short-leg position against the 1st-order claim that **NVDA expresses**. Realised daily correlation INTU↔PLTR is **+0.31** — the highest of the four, and consistent with this cascade reading rather than with the "uncorrelated diversifier" story. INTU↔NVDA is **+0.01**. Both numbers are computed in `facts.md` §6 and both are reported because the first one weakens the diversification case.

---

## 3. What this file changes about the thesis

Nothing in the conviction table. The bottoms-up build **agrees with consensus revenue**, which is the supporting result the multiple thesis needs, not a contradiction of it. What it adds is:

1. **A named binding variable — churn** — with the level (~10% at 30% price realisation) at which the installed-base floor collapses. This sharpens falsifier F1 from a revenue-growth threshold into a mechanism.
2. **A sized 1st-order exposure**: ~12% of company revenue, not the whole franchise.
3. **An unreconciled ~6-point gap** in the TurboTax unit build, flagged as an open item for the Aug-25 print.
4. **An honest correction to the portfolio story**: INTU is not orthogonal to PLTR on the mechanism (+0.31 correlation, same 2nd-order claim). It is orthogonal to NVDA (+0.01).
