# 2026-08-06 (Thu) EOD — two registered predictions resolved. 4 hits, 1 miss, 1 declared no-call — and the lesson is that the leg I won, I won on a mechanism the event refuted.

**Workflow:** EOD CONDITIONAL SYNTHESIS (Routine) → condition check → GRADE sweep (Workflow #5, 3-layer) → docket close.
**Condition check:** literal `--since="16:00"` = **0 commits**; relative `--since="6 hours ago"` = **0 commits**; all commits today = **13**, all landing **00:33Z–13:54Z**. **The evening was genuinely quiet** — so the full leg runs, and this is the **first session in three where the condition check and the intent AGREE**. The 08-04/08-05 defect (N=2) is now better characterised: it **under-reads a worked evening but reads a quiet one correctly.** The amendment is still owed but the fault is asymmetric, not general.
**Priority override:** the Routine specifies a discovery leg. **Two registered predictions resolved at today's close, which outranks discovery.** The discovery sweep is deferred and recorded here as deferred, not skipped.

---

## §1 — PRICE BASIS, ESTABLISHED BEFORE ANY GRADE

🔴 **First fetch was a trap and was caught.** The primary vendor returned quotes stamped **19:08Z = 15:08 ET — 52 minutes before the close.** Grading a "T+1 close" off those would have been the intraday-presented-as-close error the Brent verification caught this same morning. **Re-fetched from an independent vendor; both names settled at 20:03Z = 16:03 ET.**

| | 08-05 close (registered baseline) | **08-06 CLOSE** | close-to-close |
|---|---|---|---|
| **SNDK** | $1,350.50 | **$1,242.40** | **−8.00%** |
| **DDOG** | $283.17 | **$229.54** | **−18.94%** |

DDOG session high **$243.00**, low **$225.26** — the high sits **below** the $283.17 reference, so the session never traded up. ⚠️ **The registered blind-check requires gap / open-to-close / close-to-close recorded separately; the OPEN is not yet in hand and is owed before the DDOG write-up is final.**

## §2 — 🔴 SNDK: THE BASIS DECIDES R-2, AND IT DECIDES IT AGAINST ME

| basis | move | R-2 (\|move\| ≥ 10%, P=0.60) |
|---|---|---|
| **08-05 close — REGISTERED** ("Reaction baseline remains the 2026-08-05 close") | **−8.00%** | **MISS** |
| 08-04 close | −12.97% | would be a HIT |

**I grade on what was registered. R-2 is a MISS.** Selecting the other baseline after the fact is exactly the L58 error this entire week was about, and it would have been available, defensible-sounding, and wrong.

### The registered legs

| leg | P | claim | result |
|---|---|---|---|
| **R-1** | 0.70 | Q4 revenue AND NG EPS both beat consensus | **HIT** (+8.0% / +14.6%) |
| **R-2** | 0.60 | \|same-day move\| ≥ 10% | 🔴 **MISS** (−8.00%) |
| **R-3** | 0.52 | T+1 close direction NEGATIVE | **HIT** |
| **R-4** | **0.35** | beat BOTH lines → NEGATIVE close (the Kioxia shape) | **HIT** — the non-consensus call |
| R-3a | — | AH first print on the numbers | **HIT** (−4.65%, direction held to the close) |

## §3 — 3-LAYER GRADE (Workflow #5)

**INPUT — 🔴 FAILED, and measurably worst-in-class.** Revenue **−6.3%**, NG EPS **−14.6%**, FQ1 guide **−12.8%** — all three low, same direction. Scored today against two other frontier arms on the identical question: **mean absolute error GPT-5.6 2.18% / Kimi K3 4.98% / me 10.48%.** I was **4.8× worse than the best**. B45 fired on every line, in a week when B45 was named, banner-flagged, injected into every prompt, and explicitly anticipated in a neighbouring file.

**COMPUTATION — 🔴 FAILED on magnitude, in the opposite direction.** Too conservative on the fundamentals, too aggressive on the size of the reaction. Opposite errors inside one call.

**REASONING — 🟡 RIGHT CONCLUSION, REFUTED CHAIN.** R-4's registered justification was *"consensus sits above the guide, so an in-range print is a miss."* **The print cleared consensus by 8–15% on every line and guided +17.7% QoQ — and fell anyway.** The conclusion survived. The mechanism did not happen.

## §4 — 🔴 CANDIDATE LESSON L59 (the one this grade forces)

> **A correct direction call produced by a REFUTED mechanism is scored a MISS on the reasoning layer regardless of outcome, and must NOT update the P on the mechanism that produced it.**

**Why this needs to be a rule rather than a note:** the natural update from *"R-4 hit at 0.35"* is to raise confidence in consensus-above-guide reasoning — reasoning that was **falsified by the very event it predicted**. Without L59 the harness reinforces a chain the outcome disproved, and reinforces it **more strongly than an ordinary hit**, because the hit came at long odds. **This is the mechanism by which a lucky long-shot becomes a house rule.**

**Blind-check:** *distinguishes "the mechanism worked" from "the conclusion happened to land" · reads on whether the registered causal chain's own premises were true in the resolved event · **goes blind if** a prediction is registered without an explicit mechanism, since there is then nothing to falsify separately from the outcome.* **Mitigation, registered: no direction leg ships without a stated mechanism.**

## §5 — 🟢 A CANDIDATE BIAS BORN AND KILLED IN THE SAME SESSION

**Proposed:** *"under-model the company, over-model the drama"* — B45 conservatism on fundamentals plus aggression on reaction size, one bias with two faces.

**Tested immediately against DDOG's R-5, and REFUTED at N=2:**

| leg | claim | P | actual | result | my error |
|---|---|---|---|---|---|
| SNDK R-2 | \|move\| ≥ 10% | 0.60 | −8.00% | MISS | **OVER**-called magnitude |
| DDOG R-5 | \|move\| ≥ 10% | 0.60 | **−18.94%** | **HIT** | **UNDER**-called magnitude |

Same probability, same threshold, same week, **opposite errors**.

**⇒ My magnitude calls are not biased — they are NOISY.** That is a different defect requiring a different fix: **a directional bias gets a correction factor; noise gets a wider band or no call at all.** Merging the two would have applied a correction factor to a noisy quantity and made calibration **worse**.

**What survives is sharper:** B45 is **directional and consistent** (low, low, low, and low again against two independent arms). Magnitude is **not**. Keeping them separate is the finding.

**Registered:** the `|move| ≥ 10%` leg needs **N≥8** before its calibration is readable. Realised so far **1/2 against a stated 0.60**. Until then it is a call I make without evidence that I can make it, and it is labelled as such.

## §6 — 🟢 THE DECLARED NO-CALL, AND WHY IT WAS RIGHT

**DDOG R-4 was registered at 0.50 with "I have no skill on this leg" stated explicitly. The stock fell 18.94%.** Declaring no-edge cost a leg I would have won by flipping to DOWN a third time.

**That is correct behaviour, not a missed opportunity.** The alternative was flipping a direction call three times in twenty-four hours on no new information — which is how a process stops meaning anything. **A no-call that would have won is the strongest possible evidence the no-call rule is real rather than decorative**, and it should be cited whenever the rule feels expensive.

## §7 — 🟡 SECTOR DISPERSION AT THE SAME SESSION (15:08 ET intraday, stamped, directional only)

| | |
|---|---|
| **WDC** | **−11.82%** |
| **SNDK** | **−8.00%** (settled) |
| **DDOG** | **−18.94%** (settled) |
| AMD | +2.75% |
| MU | +0.38% |
| NVDA | +0.28% |
| PLTR | −1.95% |
| SPCX | +1.83% |

🔴 **WDC is the second memory/storage name down hard.** 🟢 **But AMD, NVDA and MU are all UP — compute did not follow memory.**

**That is dispersion INSIDE the complex, and it argues against a blanket "AI is being sold" read.** It is also the first same-session evidence bearing on the growth-quality frame registered this morning: **memory/storage — where the growth is price-driven — is being sold; compute, where it is volume-driven, is not.** N=1 session. **Registered as a test, not a conclusion**, and it is exactly the discriminator the frame predicted would matter.

## §8 — Carried, deferred, and owed

- **DDOG R-1 / R-2 / R-3 / O-3** — pending the reported figures; verifier commissioned this session.
- **DDOG open price** — owed, for the gap-vs-fade decomposition the blind-check requires.
- **Discovery leg** — DEFERRED (not skipped) in favour of the grade sweep. Recorded so the skip is auditable per Rule #14.
- **ETF re-spec-or-retire** — due today, **not run**. Now overdue.
- **Quota check #4** — 4 days overdue.
- **Bare-Opus-5 control** for the cross-model benchmark — still unrun; it is the single cheapest high-value item on the docket.
- **Routine-prompt amendments** (EOD relative window; KR-OPEN retired Brent gate) — still need the operator's UI.

**NO POSITION ACTION. NO RE-WEIGHT.** H1 60 / H2 11 / H3 29 (my model) stand. 🟡

---

## §9 — DDOG RESOLVED IN FULL (verifier returned post-write; T1 SEC 8-K, accession 0001628280-26-053829)

**Actuals:** revenue **$1,121.5M** (+35.6% YoY vs $826.76M; **+11.4% QoQ** vs $1,006.4M) · NG diluted EPS **$0.65** · NG operating income **$257.0M / 22.9%** · GAAP EPS **$0.12** · OCF $316M / FCF $279M.

⚠️ **GAAP net income ($44.6M) is ~8× GAAP operating income ($5.5M)** — the GAAP line is carried by interest income on a $5.0B cash pile, not operations. **GAAP operating margin is effectively zero.** Any read of "GAAP profitability improving" is describing interest income.

### My points vs actual — and B45 gets NARROWED

| line | registered | actual | error |
|---|---|---|---|
| Revenue | $1,108m | **$1,121.5m** | **−1.2%** |
| NG EPS | $0.64 | **$0.65** | **−1.5%** |
| FY guide top | ~$4.53bn | **$4.47bn** | +1.3% |

**On SNDK the same day I was −6.3% / −14.6%. Here, −1.2% / −1.5% — five to ten times better, same week, same harness.**

🟢 **That NARROWS B45 rather than confirming it.** B45 is not a constant conservatism tax; it binds hard on a **violent-price-cycle** name (memory, where the quarter is driven by a price spike) and barely at all on a **subscription-consumption** name. **Registered refinement: B45 is a MAGNITUDE-REGIME bias, not a general one — it should be applied where the underlying quantity is itself in a violent cycle, and not otherwise.** Applying it uniformly would have made the DDOG call worse.

### Registered legs

| leg | P | claim | result |
|---|---|---|---|
| **R-1** | 0.83 | Revenue > $1,078.575m | **HIT** — $1,121.5m, +4.0% vs the bar |
| **R-2** | 0.90 | NG EPS > $0.583 | **HIT** — $0.65, +12.1% |
| **R-3** | 0.93 | FY26 guide raised above $4.34bn | **HIT — and SUBSTANTIVE.** New top **$4.47bn = +$130m**, clearing the **$100m** substantive threshold I registered pre-print by $30m |
| **R-4** | 0.50 | same-day direction | **NO-CALL** (declared no edge); actual DOWN |
| **R-5** | 0.60 | \|same-day move\| ≥ 10% | **HIT** — −19.03% |
| **O-3** | 0.55 | beat lands BELOW the +2.72–4.82% historical band | 🔴 **MISS** — +3.98%, **inside** the band |

🔴 **O-3 was registered deliberately AGAINST my own point estimate.** My revenue point was right, so O-3 was wrong — **exactly the outcome I pre-stated would weaken L57** (a beat-streak measures the guidance gap, not the company). **Booked as such: L57 is WEAKENED by its own pre-registered test, not confirmed.** This is what registering a test against yourself is for.

### 🟢 THE BLIND-CHECK RESOLVES, AND THE TWO MEASURES HAVE OPPOSITE SIGNS

| | |
|---|---|
| **GAP** (prior close → open) | **−19.68%** |
| **OPEN-TO-CLOSE** | **+0.81%** |
| **CLOSE-TO-CLOSE** | **−19.03%** |

**103% of the loss was delivered before a share traded.** Shape: **gap-down with a net-positive session** — not a fade, not a slide. (Path detail: gap down → rally to $243.00 → fade to $229.29, so there *is* a fade-from-high inside the day, but open-to-close nets positive.)

**The registered blind-check demanded all three precisely because close-to-close alone can be true and misleading.** Here **close-to-close and open-to-close carry opposite signs.** Reporting either alone would have been accurate and wrong.

🟡 **Close carries a small unreconciled band:** $229.29 (quote page, corroborated by an intraday print) vs $230.38 (history table) ⇒ close-to-close **−19.03% to −18.64%**. **Stated, not averaged.** Sign and shape are robust to either.

🔴 **Headline-percentage forensics — a basis catch worth carrying.** Coverage quotes −14%, −16.96%, −17%, −17.3%, −18%, **−19.5%**, −21%. These are **not contradictions; they are different clock times and different bases.** −19.5% was pre-market. **−21% measures from the 08-05 intraday 52-week high ($292.72), not from a close.** **Only −19.03% is close-to-close.** Any digest saying "Datadog fell 21%" has silently switched to peak-to-close.

## §10 — 🔴 MY OWN NEW INSTRUMENT FAILS ITS FIRST TEST, AND I AM GRADING IT AS A FAILURE

This morning's PLTR trace (§10 of that artifact) registered: *"every AI-application name should be checked on bookings-vs-revenue, not revenue alone. This is a cheap check nobody is running."* **DDOG is the first application.**

| | YoY |
|---|---|
| RPO | **+43%** |
| Billings | **+38%** |
| Revenue | **+36%** |

**Backlog still outgrows revenue on BOTH measures. The relationship I predicted would break is intact. The instrument does not fire.**

What actually deteriorated is the **second derivative**: RPO growth **+51% → +43%**; RPO **fell sequentially for the first time in multiple years** (T2, **medium confidence, single reporting lineage — re-verify against the 10-Q before anything is built on it**); and the FY raise shrank from **~$240m (Q1) to ~$140m**.

> 🔴 **HONEST GRADE ON MY OWN FRAME: PARTIAL AT BEST.** I registered a **LEVEL** test. The evidence is a **RATE-OF-CHANGE** signal. **Those are not the same claim** — and calling the second a confirmation of the first would be **precisely the L59 error I codified four hours ago**: a conclusion landing while its stated mechanism did not hold. **The instrument needs re-specifying to the second derivative, or it needs to stay unfired.**

### What actually moved the stock — and it is neither of my hypotheses

Management disclosed that a **major longtime AI customer renewed a nine-figure deal across 17 products — and that its usage will DECLINE from Q3.** CEO: *"If you backed out our largest customer from our growth, you get pretty much the same growth rate as the rest of the business."*

**Q3 guide is the damage:** revenue **$1.135–1.145bn = +1.65% QoQ** against Q2's **+11.4%** — a ~9.8pp collapse in sequential growth, ~29% YoY vs 35.6%. **Implied Q4 ~$1,192m = +4.6% QoQ**, so the guided path is **+11.4% → +1.7% → +4.6%**: the Q3 trough is an anomaly, **consistent with a one-account step-down rather than secular decay.**

🔴 **The customer is NOT named by management. Identification as OpenAI is press inference (T3) and does NOT enter the corpus as fact.**

**Against both my hypotheses:** the renewal is a **commitment event happening simultaneously with a consumption cut** — that is optimisation/insourcing at one account, **not demand destruction**. 750+ AI customers, 31 >$1m, 8 >$10m: the cohort is **broadening** while the apex account shrinks. **The generalisable finding is the decoupling of COMMITMENT from CONSUMPTION**, which applies to every "AI-native cohort %" disclosure in the sector.

🔴 **And DDOG STOPPED DISCLOSING the AI-native cohort % in the quarter it mattered** — replaced by a non-comparable customer-count basis. **A disclosure change in the quarter a metric turns adverse is itself the signal**, and it is the literal "goes blind if" case for that entire line of analysis. Logged separately. *(A circulating "12%" figure is untraceable — **UNVERIFIED, do not propagate.**)*

**Slop netted:** one outlet claims management *"lowered revenue and EPS forecasts"* — **CONTRADICTED BY T1**, guidance was raised on every line. Two others recycle the **"revenue hits $1B"** milestone, which was **Q1 2026**. One headline says the stock **rose**.

**Position implication: NO ACTION — no size change — operator-gated.** 🟡 A beat-and-raise on every registered line, a one-account consumption step-down, and my own instrument failing to fire are three separate facts; none is a sizing input, and the concentration disclosure needs the 10-Q before it becomes one.
