# 2026-07-27 MON — KR-OPEN WAKE: first LIVE-TICK open read (prior wakes data-gapped) + H3 two-path, rates leg gapped

**WORKFLOW: KR-OPEN WAKE (scheduled Routine, time-sensitive leg of `meta/good-morning-protocol.md`). Escorted-instrument discipline — every reading below is hand-decomposed and NOT acted on. NO POSITION ACTION (user-gated, Rule #8). Full 3-leg scan, prose-deadline sweep and quota check #3 held for the user's "good morning" (screenshots cannot ride a Routine).**

**Session state at fire:** UTC 2026-07-27 00:24, KST 09:24 Mon — KRX ~24 min into the session. Repo verified `behind: 0 / ahead: 0`, `is-shallow: false` (checked, not read off the banner — per the 07-26 stale-base finding). No user wake today → full time-sensitive leg, not increment-only.

---

## 1. DETERMINISTIC READS (orchestrator-fetched, no agent, no recall)

**Method:** EODHD real-time + EOD endpoints (`meta/data-access.md` §Keyed APIs) and FRED `DGS10`. Every percentage below is **computed** from the two adjacent closes shown, not quoted from a source. Quote timestamp on the KR block = **2026-07-27 00:06Z = 09:06 KST**, i.e. six minutes after the 09:00 KST open — a genuine live tick.

### 1.1 KR open vs Friday (EODHD real-time + EOD, T1-machine) — ⚠️ **RETRACTED AND REPLACED 2026-07-27, see §1.1-R below. The original table is preserved verbatim for audit; DO NOT CITE IT.**

> **SUPERSEDED — original text, retained only as the error record:**
>
> | Instrument | Thu 07-23 close | Fri 07-24 close | Mon 07-27 open-tick | Fri move | Mon vs Fri | Friday retraced |
> |---|---|---|---|---|---|---|
> | KOSPI (`KS11.INDX`) | 7,096.8901 | 6,690.6201 | 6,730.9102 | **−5.72%** | **+0.60%** | **9.9%** |
> | SK Hynix (`000660.KO`) | ₩1,919,000 | ₩1,759,000 | ₩1,772,000 | **−8.34%** | **+0.74%** | **8.1%** |
> | Samsung Elec (`005930.KO`) | ₩270,000 | ₩249,500 | ₩254,500 | **−7.59%** | **+2.00%** | **24.4%** |

### 1.1-R CORRECTED — official opening auction + settled close (EODHD EOD OHLC, recomputed 2026-07-27 post-session)

**How the error was found:** an independent fresh-session audit, commissioned on `main` with a binding no-circularity rule (`meta/redteam/2026-07-27-fresh-session-verification-commission.md`), refuted the KOSPI leg of claim 5. I re-fetched and confirmed it against the settled daily OHLC. **The audit is correct; the original table was wrong on all three names, in the same direction.**

| Instrument | Fri 07-24 close | **Mon OPEN (auction)** | Mon vs Fri **at open** | **Friday retraced at open** | Mon LOW | Mon CLOSE | Mon vs Fri **on close** |
|---|---|---|---|---|---|---|---|
| KOSPI (`KS11.INDX`) | 6,690.6201 | **6,806.27** | **+1.73%** | **28.5%** | 6,557.39 (**−1.99%**) | 6,755.75 | **+0.97%** |
| SK Hynix (`000660.KO`) | ₩1,759,000 | **₩1,814,000** | **+3.13%** | **34.4%** | ₩1,707,000 (**−2.96%**) | ₩1,816,000 | **+3.24%** |
| Samsung Elec (`005930.KO`) | ₩249,500 | **₩257,000** | **+3.01%** | **36.6%** | ₩246,000 (**−1.40%**) | ₩254,000 | **+1.80%** |

**Magnitude of the error:** published +0.60 / +0.74 / +2.00 against true +1.73 / +3.13 / +3.01 — understated by **2.87× / 4.23× / 1.50×**. Retracement understated by **2.9× / 4.2× / 1.5×**. All three in the same direction.

**Root cause — the same failure class booked three times this week.** The figure was an **EODHD real-time snapshot taken at 00:06Z**, which I labelled `open-tick` and then fed into a metric that is defined on the **official opening auction** ("Friday retraced"). `meta/data-access.md` already carries the warning for this exact endpoint — *"`.KO` real-time feed can lag ... cross-check timestamp field ALWAYS"* — and I did check the timestamp, which is precisely why it passed: **the timestamp was live, the price basis was not.** A live timestamp is not proof of an auction print. This is **L44 instance 4** (a number without its basis), and the first of the four that **propagated** rather than being caught at intake.

**Why nothing caught it:** every number was real, vendor-sourced, correctly cited, and internally consistent with its own `change_p` field — so anti-fabrication passed it, as it must. Citation-grounding cannot check a basis.

**⚠️ Internal contradiction the file itself contained and never reconciled:** §6.4 below, written later the same session, carries **Samsung at 257,000 (+3.0%)** — the *correct* opening auction — and describes a "gap-up → fade" shape. §1.1 and §6.4 disagreed by a full percentage point on the same print, in the same file, and I did not notice. **§6.4's qualitative read was right and is now confirmed by the settled tape** (KOSPI opened at its high of 6,806.27 and faded); §1.1's quantitative table was wrong.

**What the corrected tape actually says — and it is a different session than the one I described.** Not a "weak bounce". All three names **gapped up ~1.7–3.1%, sold through Friday's close to a NEW low** (KOSPI −1.99%, SKHY −2.96%, Samsung −1.40% vs Friday), then **closed green** (+0.97 / +3.24 / +1.80%). That is a violent two-way reversal, not a shallow bid. The "bounce is weak, retraces only 9.9%" read is **withdrawn**.

**What does NOT change:** the H3 Path A/B discrimination (§1.2) is a rates computation, untouched. The SKHY add gate remains the 2026-07-29 print. No falsifier fires on any held name. No position action.

Internal consistency checked: each vendor-reported `change_p` reproduces from its own `close`/`previousClose` pair to 3 d.p. Friday's KOSPI move computes to −5.7239%; the corpus carries **−5.73%** (`meta/day-state.md`, addendum #8) — agreement within rounding, so this is the same event, independently re-measured.

**Friday intraday shape (EODHD EOD OHLC):** KOSPI `O=7,000.7798 / H=7,000.7798 / L=6,650.4102 / C=6,690.6201` — **opened at the high and sold all session**, closing near the low. SK Hynix `O=1,894,000 / H=1,894,000 / L=1,752,000` and Samsung `O=266,000 / H=266,500 / L=247,000` show the same open-at-high distribution shape. Consistent with the on-file "검은 금요일" account (sell sidecar 11:23:49).

### 1.2 H3 Path A/B discriminator — rates (FRED `DGS10`, T1)

| Date | 10Y | Direction |
|---|---|---|
| 2026-07-17 | 4.55% | — |
| 2026-07-20 | 4.60% | ↑ |
| 2026-07-21 | 4.63% | ↑ |
| 2026-07-22 | 4.67% | ↑ |
| 2026-07-23 | **4.71%** | ↑ |

**5-session delta = +16bp (computed).** Per the I-2 instrument block (five-calls addendum #3): Path B requires **10Y falling ≥15bp/5d**; observed is **+16bp in the opposite direction**. → **Path B NOT MET. Path A MET.** Clean discrimination, no judgement call required.

**🚨 DATA GAP, and it is the load-bearing one:** FRED's most recent `DGS10` observation is **2026-07-23**. **Friday 2026-07-24 is not yet published** — and 07-24 is precisely the session of both the KR rout and the reported Brent pullback. So Path A is confirmed **through Thursday only**; the Friday rates leg is **DATA-GAPPED**. The H3 read must not be closed on a rates print that does not yet exist.

### 1.3 USDKRW (EODHD `KRW.FOREX`, T1-machine) — Path-B cluster input

| Date | USDKRW | Δ |
|---|---|---|
| 2026-07-20 | 1,475.90 | — |
| 2026-07-21 | 1,481.64 | +0.39% |
| 2026-07-22 | 1,477.40 | −0.29% |
| 2026-07-23 | 1,475.63 | −0.12% |
| 2026-07-24 | **1,459.57** | **−1.09%** |

Above the 1,450 Path-B threshold all week **by level**, but **falling** — and falling hardest on the rout day itself.

---

## 2. ESCORTED DECOMPOSITION (hand-decomposed, NOT acted on)

**Reading #5 in the escort sequence** (see §5 numbering note).

**(a) The bounce is weak — this is the primary read.** Friday's damage was −5.72% / −8.34% / −7.59%; today's open retraces only **9.9% / 8.1% / 24.4%** of it (computed, §1.1). The comparison that matters is the **07-20 episode**, where the same complex recovered **+5.76% KOSPI / +10.88% SKH** in a single session and that violent snap-back was what adjudicated the flow scare toward H1 (`meta/day-state.md`). **Today's open is stabilisation, not that.** A weak bounce is compatible with either "sellers exhausted, no buyers yet" or "distribution resuming after a pause" — the open alone cannot separate them. **The full-day flow print, not the open, is the discriminator.** 🟡 DIRECTIONAL.

**(b) Samsung is retracing ~3× harder than SK Hynix** (24.4% vs 8.1%, computed). Candidate mechanism (my model, **UNVERIFIED**): SKH carries a binary two sessions out — **Q2 print Wed 2026-07-29** — and event risk suppresses the bounce in the name with the pending catalyst. Alternative explanations not excluded: index/ETF mechanics, differing foreign ownership, or Samsung-specific news. Flagged as a hypothesis to test against the full-day per-name flow attribution, **not** as a finding. 🔴 SPECULATIVE.

**(c) ⚠️ CROSS-ASSET DIVERGENCE — the won strengthened while foreigners sold.** On file (addendum #8): foreigners swung **+2.14조 → −3.28조** on Friday, ~5.4조, concentrated in SKH and Samsung. Yet USDKRW **fell 1.09%** the same session (§1.3) — the won **strengthened**. Genuine foreign capital flight requires repatriation, which mechanically **weakens** the won. It did the opposite. Candidate readings, none confirmed: (i) selling was FX-hedged, so no spot conversion; (ii) proceeds were not repatriated but parked in KRW; (iii) offsetting flows (exporter conversion, official smoothing) dominated the day. **This weakens — it does not refute — the "foreign capital flight" framing of Friday, and it is exactly the class of divergence the I-2 block was amended to catch.** 🟡 DIRECTIONAL.

**(d) H3 gate + the pre-registered de-escalation trigger.** ⚠️ **THIS PARAGRAPH IS SUPERSEDED BY §6.1 — the $90.47 premise was a benchmark error; the trigger did NOT fire. Retained to show the reasoning as it stood pre-verification.** Addendum #8 registered verbatim: *"De-escalation trigger: Brent settle <$95 → H3 gate un-breach review."* The corpus carries 07-23 settle **$100.69** (settle-confirmed breach) and a 07-24 pullback to **~$90.47**. If that pullback is confirmed **on a settle basis**, the de-escalation trigger **FIRES** and an H3 gate un-breach review is owed. **Not adjudicated in this artifact** — Brent is not machine-reachable on the current EODHD tier (see §4) and the energy leg had not returned at write time. 🔴 PENDING.

**(e) Escalation trigger status.** Addendum #8: *"foreign net-sell persisting ≥3 KR sessions → H3 to ~35 and H1 flow-leg formally downgraded."* Friday = **session 1**. Today is the **session-2 read**. **Not yet at the 3-session threshold**, and today's flow print is what determines whether the count advances. No re-weight is warranted on an open tick.

**NO POSITION ACTION. No falsifier fired on any held name. Wed 2026-07-29 SK Hynix Q2 print remains the sole adjudicator of the conditional €3-5k SKHY add.**

---

## 3. Current five-calls state (unchanged by this reading)

**H1 60 / H2 12 / H3 28** (addendum #8, 2026-07-24). **No re-weight from an opening tick** — the instrument spec puts the discriminator in the full-day flow attribution, not the open.

---

## 4. Instrument/data-access findings (route to `meta/data-access.md`)

- **EODHD `/api/intraday` → HTTP 403** on both `KS11.INDX` and `000660.KO`. The opening-auction sell-concentration pattern (an I-3 primary input) is **not machine-reachable** on this tier; it must come from the KR press leg.
- **EODHD commodities → HTTP 403** on `BZ.COMM` / `BRN.COMM` / `CO.COMM` / `BZ=F.COMM`. **Brent has no deterministic route here** — the H3 gate, the single most consequential macro threshold the harness tracks, depends on agent-fetched T2 press. Worth a named gap entry.
- **✅ NEW CAPABILITY CONFIRMED:** EODHD `/api/real-time` **does** serve KRX same-day intraday quotes during KR hours (verified 00:06Z ≈ 09:06 KST). Prior KR-open wakes on 07-21/22/23/24 were all logged **DATA-GAPPED at this hour**. This is the first live-tick KR open the routine has obtained, and it removes the contamination ceiling those wakes carried. **Contradicts the standing `data-access.md` note that `.KO` "can lag to T-1 EOD outside KR hours"** — the correct statement is that it lags outside KR hours and is live *inside* them.

## 5. Escort-sequence numbering anomaly (housekeeping)

Escorted readings on file are labelled **#1** (2026-07-20), **#2** (2026-07-21), **#4** (2026-07-22). **There is no #3.** Either a reading was skipped or #4 is mislabelled. This artifact is the 5th escorted reading by count; labelled **#5 by position, not by the broken sequence**. The I-2/I-3 blocks specify escort for the *first 3* readings — by count that period has lapsed, but the Routine directs escorted discipline on any reading, so it is applied here regardless.

## 6. AGENT LEGS RETURNED — 2 agents (~232k tokens, 89 tool-uses)

### 6.1 🚨 CORRECTION #1 — THE BRENT GATE WAS NEVER UN-BREACHED. My error, propagated twice.

**On file (WRONG):** my 07-25 EOD artifact and the 07-26 clock both state Brent "pulled back to ~$90.47 on 07-24" i.e. **below** the $95 gate. That drove the day-state line *"Brent settled back below the $95 gate."*

**Verified today (T2, triangulated across ≥3 independent outlets):**

| Date | Brent SETTLE | vs $95 gate | Source |
|---|---|---|---|
| 2026-07-23 (Thu) | **$100.69** | ABOVE | [CNBC](https://www.cnbc.com/2026/07/23/oil-prices-today-wti-brent-trump-iran-hormuz.html) |
| 2026-07-24 (Fri) | **$96.78** | **ABOVE** | [CNBC](https://www.cnbc.com/2026/07/24/oil-price-trump-hormuz-red-sea-iran-war.html); Forbes independently $97.24; Bloomberg "~$97" |

**WTI settled $88.62–89.31 on 07-24.** The "$90.47" I booked matches neither Brent nor WTI exactly but sits in WTI's neighbourhood, and appears in **no** Brent-specific source. Origin: the 07-25 Leg-B sweep reported it as bare *"crude ~$90.47"* — grade **T2/T3 aggregated** — and **I resolved that ambiguous "crude" to Brent without checking which benchmark.** That is the error.

**CONSEQUENCE — this inverts a pre-registered adjudication.** Addendum #8 registered: *"De-escalation trigger: Brent settle <$95 → H3 gate un-breach review."* On the corrected settle, **the trigger did NOT fire. The H3 gate has remained SETTLE-BREACHED continuously since 07-23.** The 07-25 and 07-26 day-state entries claiming otherwise are struck below.

**Lesson (candidate, N=1):** *"crude" is not a benchmark.* Brent and WTI ran ~$8 apart on the very day in question, and the house gate is Brent-specific. Any oil figure entering the H3 instrument must carry its benchmark name explicitly or be rejected. Same family as L42 (an after-hours quote is not an outcome) — a number of the right magnitude attached to the wrong instrument passes every fabrication check.

### 6.2 🚨 CORRECTION #2 — the KR leveraged-ETF measure was PULLED FORWARD to July 31

I booked "effective **Aug 5**" into `companies/SKHY/thesis.md` and day-state on 07-25. **FSC moved both dates up to 2026-07-31** (deposit ₩10M→₩30M *and* the collateral-securities exclusion, originally ~Aug 19) per its 2026-07-24 announcement — reportedly at presidential pressure, faster than industry system-build timelines allowed ([한국일보](https://www.hankookilbo.com/news/article/A2026072409490001383), [FSC](https://www.fsc.go.kr/no010101/87403), T1/T2).

**The overhang window is 4 days out, not 9** — and it now lands **two days after** Wednesday's SK Hynix print, inside the same week. Cascaded below.

### 6.3 KR flow leg — the discriminator is DATA-GAPPED, and that is the honest answer

- **Today's 투자자별 foreign/retail/institutional split: DATA-GAPPED.** KRX's portal is JS-rendered/unreachable to this session; press has not published a same-day flow print 29 min into the session. **전기전자 sector attribution: DATA-GAPPED for both 07-24 and 07-27.**
- **Friday 07-24 baseline (confirmed, T2):** 개인 retail **+5.1783조** net buy / 외국인 foreign **−3.2685조** net sell / 기관 institutional **−1.9513조** net sell ([EBN](https://www.ebn.co.kr/news/articleView.html?idxno=1717719)). Matches addendum #8's ~−3.28조 to 4 d.p.
- **반대매매 latest daily print: DATA-GAPPED.** On file: July cumulative 3,442억; single-day record 1,422억 on 07-09; June daily average 52.7억 vs 26.2억 in March. No print dated near Friday's crash — which, on the T+2 lag, is exactly the forced-supply read that matters today.
- **KOSPI200 futures basis + overnight offshore gap: DATA-GAPPED both legs.** ⚠️ **Framing note that supersedes part of the I-3 spec:** KRX moved its night session **off CME/EUREX linkage to an in-house night system as of 2025-06-09**, so *"overnight CME/EUREX gap"* as written in the instrument block may no longer name a real instrument. Flagged for I-3 revision.
- **KOFIA margin balance:** 37.3조 end-June (from 32.9조 end-March). **No July print retrievable.** Contamination is now *worse* than modelled — the regulatory date moved inside the window, so any move this week is front-running, not sentiment. Secondary-only, as specified.

### 6.4 Live KR tape — the open FADED, and that changes the read

| | Prev close | Open | High | Low | 09:29 KST | Δ |
|---|---|---|---|---|---|---|
| SK Hynix | 1,759,000 | **1,814,000 (+3.1%)** | 1,816,000 | **1,745,000 (−0.8%)** | 1,771,000 | +0.68% |
| Samsung | 249,500 | **257,000 (+3.0%)** | 258,500 | **250,500 (+0.4%)** | 254,000 | +1.80% |

Index at 09:27 KST: **KOSPI 6,772.25 (+1.22%)**, **KOSDAQ 773.73 (+3.41%)** ([Naver Finance](https://finance.naver.com/sise/sise_index.naver?code=KOSPI), T2; arithmetic cross-checked against Friday closes, both reconcile exactly).

**Both names gapped up ~3% and were sold into — SK Hynix round-tripped the entire gap and traded NEGATIVE before stabilising.** This is a **gap-up → fade → stabilise** pattern, not a bought open. It materially qualifies my 09:06 read in §2(a): the index level improved from the (⚠️ erroneous, see §1.1-R) +0.60% read to +1.22% over the first half-hour — **the true opening auction was +1.73%, so the index in fact FADED from the open rather than improving; §6.4's gap-up→fade shape was right and its stated direction of travel was wrong** — but the *shape* underneath is distribution into strength at the single-name level, in exactly the two names foreigners sold on Friday.

### 6.5 H3 two-path — rates leg now covered, verdict A-LEANING/MIXED

- **10Y = 4.69% on 07-24** (T2, relayed via dshort/Advisor Perspectives — **not** a direct FRED fetch; FRED still has no 07-24 observation). Rose 5 consecutive sessions to a post-Jan-2025 high, then **paused ~2bp lower on Friday** (4.71% 07-23 → 4.69% 07-24). **Path B still NOT met** (requires −15bp/5d).
- **Confound flagged by the agent, and it matters:** part of the yield rise is attributed to a **new tariff package**, not oil alone. The Path-A mechanism ("inflation-from-oil") is therefore **not cleanly isolated**.
- **Risk-off cluster absent:** VIX **18.70** (from 16.64 on 07-22) — elevated, not panic, and far below the >35 Path-B class. S&P 500 **+0.05%** Friday. Gold **~$4,052–4,057**, little changed. Mid-week even produced a risk-ON tech rally with oil *and* yields both up.
- **VERDICT: Path A-leaning/MIXED — NOT the textbook Path A the corpus has been carrying.** Yields rule out B, but no genuine risk-off stress is present and the yield driver is confounded by tariffs.

### 6.6 Non-Brent dashboard — ≥3 of 5 elevated → escalation-review threshold MET

I-2 spec: *"2-of-5 elevated → H3 escalation review at any Brent level."*

| Leg | Reading | Elevated? |
|---|---|---|
| Brent–Dubai EFS | **$13.22** (07-23), highest since 2026-05-04 | ✅ |
| JKM | **$21.03/MMBtu** (07-20), +32.6% MoM / +75.5% YoY | ✅ |
| Hull war-risk | **7.5–10% of hull value** (Hormuz) vs 1–3% pre-crisis; Red Sea >1%, up to 3% Saudi-linked. $100M tanker ≈ $3–10M/voyage vs ~$250k pre-crisis ([Insurance Journal](https://www.insurancejournal.com/news/international/2026/07/23/878788.htm)) | ✅ |
| VLCC | PG→China **$77.96/mt** (07-22). *Daily-earnings figure DATE-UNCERTAIN — may be March-2026 vintage recycled; excluded per Rule #12* | ⚠️ partial |
| Hormuz transits | **15/day** (IMF PortWatch, last published 07-19) vs **88/day** pre-crisis | ✅ |

**Threshold met several times over. Kill-condition NOT met** (spec: Hormuz >15/day sustained 30d **and** Brent <$80 — transits are *at* 15 and Brent is nowhere near $80).

### 6.7 Weekend geopolitics — escalation PEAKED, then reversed

- **Sat 07-25 ~01:17 UTC:** Houthi missiles/drones struck Aramco's **Jizan** (400kbpd refinery, fire) and **Yanbu**; first direct Houthi strike on Saudi oil infrastructure since 2022; maritime "embargo" declared on Saudi Red Sea/Bab el-Mandeb exports. Brent spot ~$100 ([Al Jazeera](https://www.aljazeera.com/news/2026/7/26/new-front-in-us-iran-war-escalates-as-houthis-fire-at-saudi-oil-facilities), T2).
- **Sun 07-26:** US and Iran held fire a 2nd consecutive day; Iran–Oman talks in Tehran on Hormuz transit ([NPR](https://www.npr.org/2026/07/26/g-s1-135593/us-pauses-attacks-iran-second-day-tehran), T2).
- **Mon 07-27 (live):** Iran signalled it will hold fire while the US pause holds → **Brent ~$92 spot, −4.9% intraday** ([CNBC](https://www.cnbc.com/2026/07/27/oil-price-wti-brent-slide-as-iran-reportedly-may-halt-attacks.html), T2). **SPOT, not a settle.**
- No US "massive attack" was executed; the 07-24 "locked and loaded" posture was superseded by the pause.

---

## 7. ADJUDICATION (escorted — decomposed, NOT acted on)

**H3 gate: BREACHED, continuously, since 07-23.** Most recent settle $96.78 (07-24) is **above** $95. The de-escalation trigger **did not fire** — my prior claim that it had was the benchmark error in §6.1.

**But the direction of travel has reversed hard.** Escalation peaked Saturday (Jizan/Yanbu, spot ~$100); a US–Iran pause has since driven Brent to ~$92 spot. **If today's settle prints <$95, the de-escalation trigger fires for real** — that is the next scheduled adjudication, and it lands tonight.

**Escalation trigger (foreign net-sell ≥3 KR sessions): CANNOT BE EVALUATED.** Friday = session 1. Today's flow print is data-gapped at this hour. The count does not advance on an unmeasured session, and **I will not infer foreign direction from price** — that inference is precisely what the I-3 re-basing was built to forbid.

**Joint state — the two macro legs are now pulling in opposite directions:**

| Leg | Direction | Status |
|---|---|---|
| Oil/geopolitics | **De-escalating** (pause, spot −4.9%) | gate still breached on settle, may un-breach tonight |
| Non-Brent dashboard | **Still elevated** (≥3/5) | escalation-review threshold met — the plumbing has not normalised with the headline |
| KR flows | **Unknown** (data-gapped) | Friday's flip unresolved into session 2 |
| KR tape shape | **Gap-up then faded** | distribution into strength in both held-tracked names |

**The dashboard-vs-Brent divergence is the sharpest thing in this reading.** Brent is falling on a diplomatic pause while freight, war-risk, EFS and Hormuz transits remain at crisis levels — i.e. the *physical* disruption has not cleared even as the *price* de-escalates. That is exactly the asymmetry the non-Brent dashboard was added to catch, and it argues against treating a sub-$95 settle tonight as an all-clear.

**NO RE-WEIGHT. H1 60 / H2 12 / H3 28 stand** (addendum #8). The instrument spec puts the discriminator in the full-day flow attribution and the settle — neither exists yet. Re-weighting on an open tick plus a spot quote would be exactly the premature-adjudication failure the escort protocol exists to prevent.

**NO POSITION ACTION (user-gated, Rule #8). No falsifier fired on any held name. Wed 07-29 SK Hynix Q2 remains the sole adjudicator of the conditional €3-5k SKHY add** — consensus on file today: 매출 84.17조 / 영업이익 64.24조, +278.6%/+597.4% YoY, OP margin 76.3% vs 71.5% Q1 (FnGuide via [파이낸셜뉴스](https://www.fnnews.com/news/202607270530350900), T2). Samsung segment detail Thu 07-30.

## 8. Cascade executed (Rule #10)
`meta/day-state.md` (both the 07-25 and 07-26 H3 carry lines struck + corrected; ETF date corrected) · `companies/SKHY/thesis.md` (ETF date Aug-5 → Jul-31) · `predictions/2026-07-17-regime-read-preregistration-five-calls.md` (addendum #9: gate correction, no re-weight) · `meta/data-access.md` (three route findings) · `predictions/lessons.md` (L43 candidate — benchmark discipline).
