# 2026-08-02 (Sun) — EOD FULL PATH: the credit gap is filled at T1, a held-name falsifier gets touched from an unexpected direction, and my own percentile computation was wrong by 22 years

**Workflow:** EOD CONDITIONAL SYNTHESIS → FULL PATH (condition computed: zero commits since 16:00Z; last session activity 11:33Z)
**Legs:** grade sweep (booked separately, `5c9ee10`) · ONE Leg-B unanchored discovery agent · escorted verification of every item touching a held name · docket close

---

## TL;DR

🟢 **The flagged material data gap is closed at T1.** `meta/day-state.md` 07-31 recorded *"No credit-spread/CDS route is now a MATERIAL gap — highest-value data upgrade available."* FRED `BAMLH0A0HYM2` serves it: **HY OAS 284bps at 2026-07-30**.

🔴 **But my first percentile computation was wrong, and the error was 22 years wide.** I computed a "25-year percentile," and the series this route actually returns **starts 2023-08-01**. The window was three years. **New data-access defect booked.**

🟡 **A held-name falsifier gets touched from a direction nothing in the harness was watching.** MURATA's FY3/27 raise leans on a yen tailwind the T1 短信 named explicitly (「操業度益や円安」). The yen has weakened **a further +2.65%** past the Q1 exit rate — and that tailwind is now the declared target of **coordinated** US-Japan intervention. The unanchored agent surfaced the intervention; it could not make this link, because by design it does not know what we hold.

🟢 **Two structurally new, dated, in-window items:** Korea FSC single-stock leveraged-ETF tightening **effective 2026-08-05**, and Japan MOF intervention totals due **08-03 to 08-07**.

---

## §1 — The credit gap: filled, then corrected

The sweep returned HY OAS at "281-284bps… among the tightest 5% of readings over 25 years… vs long-run median ~450bps" (T2 commentary).

**Escorted verification (Principle #43b — compute, don't accept):**

| | reading |
|---|---|
| HY OAS 2026-07-30 | **2.84% = 284bps** 🟢 T1 FRED `BAMLH0A0HYM2` |
| UST 10Y 2026-07-30 | 4.68% 🟢 T1 FRED `DGS10` |
| JPY/USD 2026-07-24 | 163.71 🟢 T1 FRED `DEXJPUS` |

**The level checks out at T1. The percentile does not, and neither did mine.**

My first pass requested `observation_start=2001-08-02`, got 787 observations, and computed *"tightest 24.7% of the last 25 years, 25-year median 310bps, max 461bps."* **A 25-year HY OAS maximum of 461bps is impossible** — the series exceeded 2,000bps in 2008. The mismatch is what exposed the defect: **the route returns data only from 2023-08-01 regardless of `observation_start`.** I re-requested from 1990 and still got 2023-08-01.

**Correctly labelled:**

| HY OAS, **3-year window only** (2023-08-01 → 2026-07-30, n=787) | |
|---|---|
| current | **284bps** |
| 3y median | 310bps |
| 3y min / max | **259bps** / 461bps |
| percentile | tightest **24.7%** of the last 3 years |
| room to the 3y low | **25bps** |
| room to the 3y median | +26bps |

**What survives, and what does not.** The agent's *direction* is right — credit is priced near the tight end of its recent range with far more room to widen than to tighten. The agent's *magnitude* claim — "tightest 5% of 25 years," "long-run median ~450bps" — is **UNVERIFIABLE at our tier** and must not enter the corpus as fact. Anyone quoting a multi-decade credit percentile from this harness is quoting three years of data wearing a longer label.

🟡 **The read that does survive:** at 284bps with **25bps of room to the 3-year low**, credit is expressing no stress at all in the same fortnight that a 4×-levered AI fund was margin-called, KOSPI printed its worst month on record, and a G7 tariff took effect. That asymmetry is real without needing a 25-year claim to support it.

### NEW DATA-ACCESS DEFECT (booked to `meta/data-access.md`)

> **FRED `BAMLH0A0HYM2` (ICE BofA HY OAS) returns only from 2023-08-01 on this route**, silently, regardless of `observation_start`. **Any percentile or "richest since" claim computed from it is capped at ~3 years.** This is the credit-route equivalent of the EODHD index-field corruption: the call succeeds, the numbers look plausible, and the window is wrong.
>
> **Blind-check:** distinguishes "spreads are historically tight" from "spreads are tight versus a truncated window" · reads on the first observation date returned, not on the values · **goes blind if a future caller checks only the values and not the range** — which is exactly how I got it wrong on the first pass, and the values alone looked entirely reasonable.

---

## §2 — 🟡 FALSIFIER TOUCH: MURATA (HELD), from a direction we were not watching

**The sweep's item #6 (T1/T2, [NHK](https://news.web.nhk/newsweb/na/na-k10015194291000) + [Nomura](https://www.nomura.co.jp/wealthstyle/article/0570/)):** Japan MOF/BOJ ran intermittent FX intervention 2026-07-30 → 08-01, described as **coordinated with US authorities**. Full totals due from MOF **2026-08-03 to 08-07** (the prior Apr-May round totalled ¥11.7tn).

**Why this lands on a held name — the link the unanchored agent structurally could not make:**

MURATA's Q1 FY3/27 print (graded 07-31) HIT its numbers while its **mechanism was wrong on 3 of 3 causal legs**. The T1 決算短信 attributed the result not to our thesis (April MLCC price hikes flowing through) but to **「操業度益や円安」 — utilisation gains and a weak yen** — with FX running **¥144.60 → ¥159.49 (+10.30% YoY)**, plausibly the entire beat. The FY3/27 guidance was then **RAISED** against our P(raise)=25%.

**So the FY raise rests substantially on a currency assumption.** Computed tonight:

```
Murata Q1 FX (T1 短信) : 144.60 -> 159.49   (+10.30% YoY yen weakness)
Latest DEXJPUS         : 163.71 (2026-07-24, T1 FRED)
vs Q1 exit 159.49      : +2.65%  -> yen WEAKER STILL
```

The tailwind has **extended, not faded** — which supports the raise. But it is now the **explicit declared target of coordinated intervention by two governments**, with the size of that intervention printing inside the next five days.

🟡 **This does not fire a falsifier tonight.** MURATA H3 (P=10%) is *"MISSES — FX/yen/capacity execution drag."* Nothing has missed. What has changed is that the **variance** around the FY raise is now policy-driven rather than demand-driven, and policy prints on a date we can put in the calendar.

**Position implication: HOLD — no size change — but the pending MURATA re-basing must now carry an FX leg it did not have.** The re-basing (due pre-Aug-6) was scoped to move the thesis off price-flow-through and onto volume/utilisation/datacenter-mix. Tonight adds a third input: **the FY raise's currency dependence, and the fact that the counterparty to that dependence is the Japanese and US treasuries.** A re-basing that lands without pricing the intervention risk would be re-basing onto two of three legs. 🟡

**SUMCO (HELD)** carries the same exposure structurally (JPY reporter, USD-denominated wafer contracts) and its **Q2 interim prints 08-06** — inside the MOF disclosure window. **Position implication: HOLD — no size change — FX now a named input to the 08-06 decision package.** 🟡

---

## §3 — Two structurally new, dated, in-window items

**Korea FSC single-stock leveraged-ETF tightening, effective 2026-08-05** (T2, [Bloomberg](https://www.bloomberg.com/news/articles/2026-07-16/south-korea-to-halt-new-listings-of-single-stock-leveraged-etfs) reported; new listings halted since 07-16). Minimum cash deposit ₩10m → ₩30m; minimum lot 1 → 20 units; mandatory education 2h → 3h; tracking-error tolerance 3% → 2%.

**Why structural:** the regulator is removing a volatility-amplification mechanism from **the two names that ARE the memory trade** (Samsung, SK Hynix). Our own 07-31 close artifact recorded that the KOSPI move was a positioning event, that *"디레버리징이 상당 부분 마무리됐다는 인식"* had become a named rally driver, and that **our positioning-flush read had become consensus and its edge was spent.** This is the mechanical follow-through: less structural leverage in the system going forward = **dampened beta in both directions** on those two names.

**2nd order (P~60%):** our 08-14 float-share test (Situational Awareness Q2 13F) gets *harder* to interpret, because from 08-05 the retail-leverage channel is materially different from the one that operated in July. **Comparing pre- and post-08-05 flow regimes without noting the rule change would be a basis error** — booking it now so the 08-14 read does not walk into it.

**Japan MOF intervention totals, 08-03 → 08-07** — see §2. Now a dated calendar item.

---

## §4 — What I am NOT ingesting, and why (Rule #18 / B40)

| Sweep claim | Verdict |
|---|---|
| HY OAS "tightest 5% of 25 years," "long-run median ~450bps" | **REJECTED as fact.** Unverifiable at our tier; our route holds 3 years. Direction retained, magnitude discarded. |
| SK Hynix "shares fell 9.6-12% on the print" | **CONFLICTS with our own T1 record (−5.64%).** Almost certainly a different basis or window. Not ingested — this is the exact B40.2 magnitude class, and the corpus figure was computed from a settled close. |
| Situational Awareness "$45B → ~$10B AUM," "4× leverage" | **NOT ingested as fact.** Our 07-31 size-test partial retraction established the 13F table value was 8.6-30% of the actual book and that **float share, not fund size, is the discriminator.** These are T2 press AUM figures of exactly the kind that retraction was about. **08-14 13F remains the only thing that settles it.** |
| Yen intervention "near 160/USD" | **Level imprecise** — T1 FRED has 163.71 on 07-24, i.e. already weaker than 160 a week earlier. Direction right, level wrong. Recorded with the correction. |
| Items #1, #2, #4, #5 generally | **Already in the corpus** from the 07-30/07-31 work. Corroborating, not new. #5's KOSPI 6,595.45 / +17.91% matches our T1 record exactly — a clean independent confirmation. |

**Honest note on the instrument:** roughly half of a 12-item unanchored sweep returned things we already held. That is not a failure — an unanchored agent cannot know what we know, and the independent corroboration of the KOSPI figure has real value. But it does mean the **marginal** yield of Leg B on a quiet weekend sat in items #3, #6, #8 and #12 — four of twelve.

---

## §5 — Lower-priority items retained without cascade

- **PJM capacity price $28.92 → $329.17/MW-day since 2024; Ohio manufacturer Belden Brick reports a 90% power-bill increase; OH/PA residential rates +9%/+14% YoY** (T2 Reuters/Insurance Journal, Fortune). **Why it matters:** first quantified, politically-visible real-economy cost of the buildout, creating a constituency actively opposed to further data-center siting. Routes to TC-13 / TC-3 as a **bypass-route risk to the "power is the next bottleneck, buy anything power-adjacent" consensus** — the risk is not power scarcity, it is *permission*. Not promoted; single-source-cluster.
- **China Politburo 07-30 pledged targeted, explicitly not large-scale, stimulus; 5th Plenum October** (T1/T2 Caixin, SCMP). 2nd order: no state-stimulus tailwind for CXMT/YMTC either — marginally reduces near-term competitive pressure on the memory names.
- **Canada 35% tariff effective 08-01** on non-USMCA-compliant goods; energy/potash at 10%.
- **US June payrolls +57K vs ~115K consensus, labour force −720K, participation 61.5%; July print 08-07.** A shrinking labour force with soft hiring is a **supply-side** signature — so a weak August print will not automatically mean demand is rolling over. Worth holding before the 08-07 read.
- **Rivian −9.6% on a beat** — ~60% of software/services revenue from the VW JV, core automotive at a −$36M gross loss. Cross-domain methodology specimen for earnings-quality decomposition; no position relevance.

---

## §6 — Coverage gaps (explicit, per Leg-B spec)

- **Corporate/deal news dated 08-01/08-02**: nothing surfaced. Agent flagged this as possibly a search-recall limitation rather than a true null — **not asserted as quiet.**
- **Regulatory/geopolitical beyond China/Korea/Canada**: nothing weekend-dated.
- **Fed speaker calendar for the week**: not surfaced.
- **No HTTP 403 encountered this sweep** — notable, given the standing proxy wall on financial-press domains. Recorded as a data point on the ceiling, not a claim that it has lifted.
