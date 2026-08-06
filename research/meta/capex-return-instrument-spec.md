# INSTRUMENT SPEC — hyperscaler capex→return, and why the obvious version cannot be built

**Created:** 2026-08-06, on operator question: *"What must be true for you to close that gap? For you to run a deep analysis on hyperscaler CapEx to ROI?"*
**Status:** 🟢 **N5 RUN 2026-08-06 — see `signals/cross-source-log/2026-08-06-thu-circularity-the-operator-aimed-at-microsoft-and-the-answer-is-amazon.md`. The pre-registered failure mode below FIRED ON THE FIRST RUN and produced the artifact's headline finding (48% of Amazon's backlog owed by two counterparties Amazon funded $68B into). N1 confirmed permanently blocked. N3 and N4 confirmed as real distortions with T1 magnitudes.** Original spec text preserved below unedited. Conditions N1–N5 below state what must be true; three of the five are blocked by **disclosure**, not by access.
**Parent frame:** `signals/cross-source-log/2026-08-06-thu-legC-wsj-16-screenshot-batch...md` §6 (growth-quality repricing) · `2026-08-06-thu-pltr-...md` §10 (the 4th-order leg that makes this the live question).

---

## The finding that comes before the analysis

**The gap is not a fetch problem. It is a disclosure problem.** I said I would not estimate the numerator to fill the hole; the reason is stronger than caution:

> **No hyperscaler discloses "AI revenue" as a line item.** There is no reported quantity whose ratio to capex would be the return on AI capex. Any published "hyperscaler AI ROI" number is therefore built on an analyst-constructed numerator, and the construction — not the data — determines the answer.

That is why the figure is quoted so confidently and so variously. **The honest move is to change the numerator to something that IS disclosed**, which is N2 below.

## N1 — A NUMERATOR THAT EXISTS

**Blocked as stated.** What is actually disclosed, per company:

| | disclosed | usable as an AI-return numerator? |
|---|---|---|
| Microsoft | Microsoft Cloud revenue; Azure growth % | partial — Azure is not all AI, and the AI contribution split was not consistently disclosed |
| Alphabet | Google Cloud revenue + backlog | partial — same mixing problem |
| Amazon | AWS revenue + backlog | partial — same |
| Meta | **nothing separable.** AI return shows up inside ad revenue and engagement | **no** — structurally unattributable |

**Meta is the proof that the direct ratio cannot be built cohort-wide.** A company can spend $135–145B and have *no* line where the return could appear. Any cohort-level ratio that includes Meta is smuggling in an estimate.

## N2 — THE SUBSTITUTION THAT MAKES IT BUILDABLE: capex → BACKLOG, not capex → revenue

**Remaining performance obligation (RPO) / backlog IS disclosed** by Microsoft Commercial, Google Cloud and AWS, with growth rates and (sometimes) weighted-average recognition periods.

**Backlog is the better instrument anyway, for three reasons:**
1. **It is forward-looking.** Capex spent today should show up as contracted future revenue before it shows up as recognised revenue. Revenue lags; backlog does not.
2. **It is the same instrument already built one layer down.** The PLTR trace (§10) established that **bookings-vs-revenue** is the check nobody runs on the application layer. Applying the identical check to the infrastructure layer makes it **one instrument across two rungs of the chain**, not two ad-hoc metrics.
3. **It is a RELATION, not a presence check** — the class the 2026-08-05 N1 audit found this harness has almost none of.

**⇒ The instrument becomes: Δcapex(t) vs Δbacklog(t) — and, crucially, backlog growth vs revenue growth, which is the leading indicator.**

## N3 — COMPARABLE DENOMINATORS (a basis condition, and it bites hard)

**Cash-flow-statement capex materially understates total commitment.** The corpus already carries the motivating specimen: Principle #51's second example is capex-line blindness when **Microsoft moved $132.5bn into leases** — a structure that does not appear as purchases of property and equipment.

**Condition: capex must be defined as purchases of PP&E + finance leases + disclosed commitments, consistently, per company.** A ratio built on the cash-flow line alone compares four companies that are each drawing the boundary somewhere different. That is a **basis mismatch (L58) at the denominator**, and it is the single most likely way this analysis produces a confident wrong answer.

## N4 — DEPRECIATION-LIFE NORMALISATION (the quiet one)

Capex hits earnings as **depreciation over the assumed useful life**. Extending the assumed life of servers and network gear **raises reported returns without anything real changing.**

**Condition: the assumed useful life must be read out of each 10-K, per company, per period, and any change normalised out before periods are compared.** If one company extended server life from 5 to 6 years mid-window, its apparent return improves by construction.

**Blind-check:** *distinguishes "the capex is earning more" from "the capex is being expensed slower" · reads on the useful-life disclosure and the stated EPS impact · **goes blind if** a company changes the life estimate and quantifies the impact only in aggregate across asset classes, which is common.*

## N5 — RELATED-PARTY REVENUE STRIPPED OUT — the operator's circularity point, and the one that could void the whole ratio

**Operator, 2026-08-06:** *"with Microsoft, it seemed like a large order of their AI revenue came from OpenAI, which then brings back the circular financing narrative… which adds fragility."*

**If a vendor supplies the capital its customer uses to buy from it, the resulting revenue is not a return on capex — it is the vendor's own money making a round trip and being booked once as an investment and once as revenue.** The ratio would then measure the size of the circle, not the size of the return.

This is not a Microsoft-specific question. The same structure is alleged across **Amazon↔Anthropic, Google↔Anthropic, Nvidia↔(OpenAI / CoreWeave / neoclouds), Oracle↔OpenAI**.

**Condition: vendor-financed revenue must be identified and removed — or, if it cannot be identified, the ratio must be reported with an explicit statement that its numerator includes an unquantified circular component.**

🔴 **STATUS: UNVERIFIED AND NOT ASSERTED.** The operator's magnitude claim about Microsoft/OpenAI is **plausible and load-bearing and I have not established it.** A verification pass is commissioned (2026-08-06). **Until it returns, no number is attached to this and the claim is not cascaded anywhere.** Recorded here so that if it later turns out to be wrong, the record shows it was carried as a hypothesis and not as a fact.

---

## What is runnable TODAY vs what is blocked

| condition | status | why |
|---|---|---|
| N1 direct AI-revenue numerator | **BLOCKED — permanently** | not disclosed; Meta structurally cannot disclose it |
| N2 capex→backlog substitution | **RUNNABLE** | RPO disclosed by MSFT / GOOGL / AMZN; EDGAR reachable and used successfully today for three other filers |
| N3 capex incl. finance leases | **RUNNABLE, laborious** | in the filings; requires per-company reading, not a screen |
| N4 useful-life normalisation | **RUNNABLE** | 10-K accounting-policy note |
| N5 related-party strip-out | **PENDING VERIFICATION** | may be partially undisclosed; if so, N5 becomes a stated caveat rather than an adjustment |

**⇒ Three of five are runnable now. The analysis that can honestly be built is `capex(incl. leases, life-normalised) → backlog`, carrying an explicit circularity caveat. The analysis everyone quotes — capex → AI revenue — cannot be built from disclosure by anyone, including the people quoting it.**

## Pre-registered failure mode of this instrument

**Backlog is not free of the same disease.** A vendor-financed customer signing a large multi-year commitment inflates backlog exactly as it inflates revenue, and *earlier*. **So N5 contaminates N2.** If the circularity is large, capex→backlog measures the circle sooner and more sensitively than capex→revenue does.

**That is not a reason to abandon the instrument — it is the instrument's most important reading.** A cohort where backlog growth is driven by counterparties the vendors themselves funded is a *detectable* state, and detecting it is worth more than the ratio.

**Blind-check on the whole instrument:** *distinguishes "AI capex is converting into contracted demand" from "AI capex is converting into vendor-financed commitments" · reads on backlog growth net of identified related-party commitments · **goes blind if** the cohort reports backlog only in aggregate with no counterparty concentration disclosure — which is the current state for at least some of the cohort, and is therefore the first thing to check rather than the last.*

## Re-eval

**2026-09-06**, or on the first hyperscaler quarter after this date, whichever is sooner. If N2 has not been run by then, this spec is a plan that did not become an instrument, and should be either executed or retired rather than carried.


---

## 2026-08-06 — RESULT OF THE FIRST RUN (appended; spec text above left unedited)

| condition | predicted | found |
|---|---|---|
| **N1** no AI-revenue numerator | blocked permanently | 🟢 **CONFIRMED.** Microsoft has no AI revenue line item and **stopped updating** even its run-rate proxy at Q4 FY26. The circulating "~70%" divides a T1 numerator by an extrapolated denominator. |
| **N2** capex→backlog | runnable | 🟢 **RUN.** And it produced the finding, not the ratio. |
| **N3** capex incl. leases | real distortion | 🟢 **CONFIRMED with magnitudes.** MSFT finance-lease additions **$24.6B on top of $115.9B** cash capex (17.5%); **$329.1B MSFT + ~$347B META uncommenced leases** in no capex table. Plus: Microsoft's "$15B capex cut" is a **lease reclassification**, not a cut. |
| **N4** useful-life normalisation | real distortion | 🟢 **CONFIRMED — and the common narrative is backwards.** Amazon **SHORTENED** server lives 6→5yrs (−$0.7B op income). MSFT and GOOGL made **no** server change. Only META extended. |
| **N5** related-party strip-out | could void the ratio | 🟢 **RUN.** Amazon **28.6%** vendor-financed vs Microsoft **5.2%** — the operator's premise aimed at the wrong company, and Microsoft's circularity claim is **refuted outright** ($11.9B funded cumulative vs $24.1B revenue in one year). |

**The pre-registered failure mode was the point.** The spec said N5 would contaminate N2 and that detecting a vendor-financed backlog would be worth more than the ratio. **It was detected at the first attempt, at 48%, from two T1 figures in a single 10-Q.**

**Instrument upgrade, registered:** the primary reading of N2 is no longer `Δcapex vs Δbacklog`. It is **`share of backlog owed by counterparties the vendor capitalised`** — with *"not disclosed"* scored as an attribute rather than left blank, since today only Amazon discloses both legs.

**Re-eval unchanged: 2026-09-06.** N2's full cohort run (MSFT/GOOGL/AMZN backlog vs life-normalised capex incl. leases) is still owed; what ran today was N5 plus the N3/N4 magnitudes.
