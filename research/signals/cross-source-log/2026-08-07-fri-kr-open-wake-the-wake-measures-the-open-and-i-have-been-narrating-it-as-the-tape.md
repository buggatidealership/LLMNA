# KR-OPEN WAKE 2026-08-07 FRI — the wake measures THE OPEN, and I have been narrating it as THE TAPE

**Fired:** ~09:24 KST / 00:24Z, Friday 2026-08-07. Routine, time-sensitive leg — INTRA-SESSION per L42-b.
**Sync:** clean, 0 behind / 25 ahead of `origin/main`. No prior operator wake → full leg.
**Segment classification (Critical Rule #6 / Principle #29):** memory-and-storage + chip-and-foundry, Korea cohort.

---

## TL;DR

Korea bounced at the open (+1.66% KOSPI, SK Hynix +2.74%, Samsung +3.47%) but is still deep in the hole from yesterday. **Three findings matter more than the tape, and the third is the worst.**

1. **This wake reads a 4-to-24-minute sample of a 6.5-hour session, and I have been writing it up as if it were the day.** Yesterday's wake said SK Hynix was down 4.26%; it closed down 10.37%. Samsung's error was **10×**. Every prior wake carries the same defect. (§2)
2. **The flow discriminators I could not read for six sessions became readable**, and they say foreign *and* institutional money sold the same two names together while retail bought the fall — the FRAGILE configuration ADDENDUM #8 pre-registered. **Counter: 1 of 3. No action.** (§4)
3. 🔴 **The story I flagged as "the first hard evidence for the operator's fab-gated thesis" was REFUTED — and I had the correct explanation in my own file 24 hours earlier and abandoned it.** There was no next-gen chip delay (no lineage across six Korean articles; the nearest real item is a 30-day-stale story about a server *rack*). There was no SOX crash (it was **−1.40%**, after **+6.55%**). The actual cause was the SanDisk/WDC guidance miss — **which my own 08-06 wake named as "the obvious candidate cause" before the Korean close.** I replaced a correct self-derived mechanism with an unsourced one because the unsourced one was more interesting and pointed at a live thesis. **The verifier requirement caught it; my judgement did not.** (§5)

---

## 1. THE TAPE — bounce, but the two-day shape is what matters

🔴 **VENDOR DEFECT, INSTANCE 6.** Both indices returned a `previousClose` of the **08-05** session — T-2, two sessions stale. All four single-stock prevCloses clean. **Index-only, as documented since 08-04.** Caught by the standing practice of checking every prevClose against our own T1 record before use; without it the headline would have been computed off the wrong base for a second consecutive month.

| | prior close (08-06, our T1 record) | 09:04 KST tick 08-07 | computed change |
|---|---|---|---|
| KOSPI | 6,296.38 | 6,401.21 | **+1.66%** |
| KOSDAQ | 801.67 | 810.11 | +1.05% |
| SK Hynix (000660) | 1,495,000 | 1,536,000 | **+2.74%** |
| Samsung Electronics (005930) | 230,500 | 238,500 | **+3.47%** |

**Two-day net, which is the honest frame:** SK Hynix is still **−7.91%** below its 08-05 close after today's bounce. A +2.74% open recovers roughly a quarter of a −10.37% day. **Reporting the bounce without the two-day net would be the basis error (L58) this artifact's §2 is about, committed in the same file that names it.**

---

## 2. 🔴 NEW HARNESS DEFECT — THE WAKE MEASURES THE OPEN AND I HAVE BEEN NARRATING IT AS THE TAPE

This is the finding of the session and it is about the instrument, not the market.

**The KR-OPEN WAKE fires at ~09:04–09:24 KST. The Korean session runs 09:00–15:30 KST.** The wake therefore samples the first **4 to 24 minutes** of a **390-minute** session — roughly **1% to 6%** of it — and I have consistently written that sample up in the register of a completed day.

**Measured on yesterday's own numbers:**

| | what the 09:07 KST wake read | what the session actually closed | understatement |
|---|---|---|---|
| SK Hynix | −4.26% | **−10.37%** | **2.4×** |
| KOSPI | −1.05% | **−4.58%** | **4.4×** |
| Samsung Electronics | −0.61% | **−6.30%** | **10.3×** |

**All three errors point the same way — the open UNDERSTATED the damage — and the error grows as the sample gets smaller relative to the move.** Samsung, which looked almost flat at the open, lost more than six percent.

**Classification: this is an L58 BASIS MISMATCH of the TENSE family.** The number is real and correctly computed; what it was measured *against* — a 24-minute window — was never stated, and every downstream sentence inherited the authority of a session close it never had. It is the same defect as the 08-06 "DDOG printed pre-market" error (a 04:07 ET statement about a 07:00 ET release) and the same as the SPCX and AMD headline-inheritance errors: **a correct quantity, reported on a basis the reader will assume is a different one.**

**Scope: every prior KR-OPEN WAKE carries it.** This is not a one-session slip; it is a property of where the Routine fires. I am not retro-editing prior artifacts — the record stands with this correction pointing at it.

**The repair, registered now:**
1. Every KR-OPEN WAKE number from here carries the literal tag **`(open, HH:MM KST — N minutes into a 390-minute session)`**. No exceptions, no "obvious from context."
2. Any wake claim about DIRECTION OR MAGNITUDE of a Korean session must be stated as **a reading of the open**, never of the day; the phrase "the tape" is retired from this Routine.
3. The prior session's CLOSE is fetched and reported alongside the open in every wake — which makes the two-day frame in §1 mandatory rather than a courtesy.

**Blind-check (Principle #51):** *distinguishes "the open is informative about the session" from "the open is a 6% sample I am rounding up to 100%" · reads on the open-vs-close divergence measured per session and accumulated · **goes blind if** a run of sessions happens to open near where it closes, which will make the tag look like pedantry exactly when the discipline is cheapest to drop.*

**What this does NOT do:** it does not make the wake worthless. The open is a genuine, timely, tradeable observation and it is often the first read anyone gets. **The defect was never the measurement — it was the label.** No position or weight moves on this finding; it changes how the readings are written, not what they say.

---

## 3. H3 — the current instrument, run for the 4th consecutive wake in place of the retired Brent gate

Per ADDENDUM #15 the Brent-95 gate is retired and the live H3 instrument is the **2s30s curve** (escalation) against **10y breakevens** (de-escalation).

| instrument | reading | observation date | distance to trigger |
|---|---|---|---|
| 2s30s spread | **99bp** (+1bp) | 2026-08-05 | **21bp** below the 120bp escalation trigger |
| 10y breakeven | **2.26%** | 2026-08-06 | 34bp below the 2.6% de-escalation trigger |

⚠️ **NOT SAME-CUT** — the curve reading is 08-05 and the breakeven is 08-06. Stated, not smoothed. Per the 08-03 FRED lesson, every value carries its returned observation date and the gap to today.

**Six sessions flat at 98–99bp.** The ratchet property registered in ADDENDUM #15 is unchanged and worth restating because it is the instrument's own defect: **escalation is 21bp away and reachable; de-escalation requires breakevens to rise to 2.6% when ADDENDUM #14's own argument is that they are anchored.** It is a one-sided instrument — it can tell me things are getting worse and structurally struggles to tell me they are getting better. Registered as a known limitation, not repaired today.

**WEIGHTS HELD: H1 60 / H2 11 / H3 29.** Nothing in this wake moves them.

⚠️ **4th consecutive wake carrying the retired Brent gate in the Routine prompt.** The prompt amendment requires the operator's UI and is now materially overdue; I am running the correct instrument and ignoring the prompt's stale clause each time, which works but is exactly the kind of undocumented workaround that survives until someone else runs the Routine.

---

## 4. 🟢 BREAKTHROUGH — THE I-3 FLOW DISCRIMINATORS WERE READABLE FOR THE FIRST TIME IN SIX SESSIONS

The 투자자별 (investor-type) close-basis flows have been "STILL OWED, not invented" in every day-state entry since 07-31. **Today the T2 Korean press carried them for the 08-06 close.**

| | foreign net | institutional net |
|---|---|---|
| SK Hynix | **−₩16,936억** (−₩1.69조) | −₩4,218억 |
| Samsung Electronics | −₩7,268억 | −₩2,776억 |

**Combined foreign + institutional net selling in the two names: ₩3.12조.**

**Retail bought the fall** — T2 headline 「외국인 1.7조 팔자에 개인 방어 역부족」 ("retail defence insufficient against foreign selling of ₩1.7조").

🔴 **This is the FRAGILE configuration as pre-registered in ADDENDUM #8:** foreign selling **and** institutional selling in the same names **and** retail absorbing. The distinction ADDENDUM #8 exists to draw is between foreign selling that institutions absorb (rotation, benign) and foreign selling that institutions join (distribution, fragile). **Today reads unambiguously as the second.** This is the same read the 08-03 sweep produced (foreign+institutional −₩4.77조 vs retail +₩4.65조) — so the configuration is now **N=2 within five sessions**, which is what ADDENDUM #8 asked for.

**매도 사이드카 (SELL sidecar) triggered 10:18 KST on 08-06** — KOSPI200 futures fell more than 5%, halting program trading. **First sidecar of August.**

**USDKRW 1,423.8, −0.7**, at the 15:30 KST onshore weekly close — the cut-stamp ADDENDUM #10 requires is satisfied. The won did essentially nothing on a −4.58% equity day, which is itself mildly informative: this was not a currency event.

**🟢 I-3 COUNTER: 1 of 3, starting 2026-08-06.** The escalation trigger requires 3. **Sessions before 08-06 CANNOT be back-filled** — the discriminator was unreadable, and treating "I could not measure it" as "it did not happen" is the exact move the counter exists to prevent. Two more readable FRAGILE sessions are required before anything escalates. **No position action, no re-weight.**

---

## 5. 🔴 THE ATTRIBUTED CAUSE — VERIFIER RETURNED **REFUTED ON BOTH LEGS**, AND THE WORST PART IS THAT I ALREADY HAD THE RIGHT ANSWER YESTERDAY

Korean press attributed the 08-06 crash to two things: **an overnight SOX crash**, and **「차세대 AI 반도체 공급 일정 연기 가능성」 — a possible delay in the NEXT-GENERATION AI CHIP SUPPLY SCHEDULE.** I flagged the second as T2 and commissioned a verifier before cascading it. **It returned REFUTED. So did the first.**

### 5.1 Leg (b) — the delay story: **REFUTED. No traceable lineage.**

The verifier checked **six Korean articles dated 08-06 KST individually** (헤럴드경제 10:07, 한국경제 11:19, mediawatch, MBC 15:52, 코리아리포트 18:50, plus one 403). **None mentions Rubin, HBM4, or a supply schedule.** The verifier could not find any Korean outlet that printed the phrase at all. Checking the four candidate chips separately:

| candidate | finding |
|---|---|
| Nvidia Rubin / Rubin Ultra | the only real delay story — and it is **stale by 30 days and about a RACK, not a chip**: the Kyber NVL144 slip to 2028 was SemiAnalysis reporting surfaced **2026-07-07** (서울경제, T2). The Rubin *GPU* thermal-lid/HBM4-qualification ramp issue was **RESOLVED pre-window** (KeyBanc; production ramping July 2026; target *raised*). |
| HBM4 at SK Hynix / Samsung / Micron | **no delay — the opposite.** See 5.3. |
| TSMC CoWoS / N2 | nothing in window. **NOT ESTABLISHED** — untested, not disproven. |
| hyperscaler accelerators (TPU / Trainium / Maia) | nothing in window. **NOT ESTABLISHED.** |

**Classification: B40 stale-recycle, textbook.** A 2026-07-07 third-party analyst item about a server rack, resurfacing as a 2026-08-06 causal driver about chips. That is the exact bias B40 was codified for, and it arrived wearing a different language.

### 5.2 Leg (a) — the "SOX crash": **REFUTED AS FRAMED. It was −1.40%.**

| session | SOX | move |
|---|---|---|
| 2026-08-03 | 11,430.4 | +1.05% |
| 2026-08-04 | 12,179.3 | **+6.55%** |
| 2026-08-05 | 12,008.9 | **−1.40%** |
| 2026-08-06 | 12,048.7 | **+0.33%** |

Two independent lineages agree (kr.investing.com historical series; 헤럴드경제 08-06 stating −1.40% and 「5거래일 만에 하락세로 돌아섰다」).

**Recomputed: SOX on 08-05 was still +5.06% above its 08-03 close.** A −1.40% day that gives back a fifth of the prior session's +6.55% is a **pullback, not a crash** — and **SOX ROSE +0.33% on 08-06, the day Korea fell 4.6%.** A −1.40% index print cannot mechanically produce SK Hynix −10.37%.

🔴 **I INHERITED THE WORD "CRASH" WITH NO NUMBER ATTACHED AND CARRIED IT INTO MY OWN ARTIFACT.** That is the same class as the SPCX and AMD headline-inheritance errors: **an adjective about a magnitude, propagated without its magnitude.** Registering the general form now — *any inherited index-move adjective (crash / plunge / tumble / rip) is unusable until a number is attached to it* — because this is now the third instance in four days and the first one where the adjective came in a foreign language, which made it harder to notice.

### 5.3 What actually happened — and 🔴 **I HAD IT RIGHT 24 HOURS EARLIER AND THEN ABANDONED IT**

The real transmission was **after-hours, and it does not appear in the 08-05 SOX close at all**: SanDisk and Western Digital reported after the US close on 08-05 — **beat on results, missed on forward guidance** (SNDK Sept-quarter revenue midpoint ~$10.55B vs ~$10.8B consensus). SNDK fell ~5% after-hours; WDC ~−14% and SNDK ~−8% subsequently. **Asia on 08-06 traded that after-hours shock.** The Korean press said so directly:

> 「반도체 업종 투자심리가 위축된 가운데 샌디스크가 실적 발표 이후 시간외거래에서 5%대 하락한 점도 국내 반도체주 투자심리에 부담을 준 것으로 풀이된다」 — 코리아리포트, 2026-08-06 18:50 KST (T2)

> 「AMD와 샌디스크 등 글로벌 인공지능 관련 기업들이 시장 예상치를 밑도는 향후 실적 전망을 내놓으면서」 — MBC 뉴스, 2026-08-06 15:52 KST (T2)

🔴 **AND MY OWN 08-06 WAKE ARTIFACT SAID EXACTLY THIS, IN WRITING, BEFORE THE CLOSE:**

> *"SK Hynix **−4.26%** against a KOSPI of −1.05% and a KOSDAQ of +0.38% is a **−3.2pp relative move in the single most SNDK-correlated name on the KR board**, hours after SanDisk beat every line and fell. The read-through is the obvious candidate cause."*
> — `2026-08-06-thu-kr-open-wake-h3-instrument-measured-first-time-and-it-is-a-ratchet.md`, line 145

**I had the correct mechanism, derived from first principles, from our own data, 24 hours before the press did — and this morning I replaced it with a press attribution that had no source, no company, no chip, and no lineage.** The substitution was not caused by new evidence. It was caused by the new story being **more interesting** and by its pointing at the operator's live fab-gated thesis.

**This is the single most important thing in this artifact, and it is worse than the §2 defect.** §2 is a labelling error. This is a **reasoning regression**: I moved from a correct, self-derived, cheaply-checkable mechanism to an unsourced one, in the direction of a hypothesis already on the table. §5 of the draft version of this same file contained a paragraph explaining that I was guarding against precisely this — *"an attractive mechanism that would confirm the operator's live thesis is exactly the one I am most likely to promote on thin evidence"* — and I wrote that paragraph **while calling the delay story "the first hard evidence bearing on the operator's fab-gated thesis."** **The guard was stated and the error was committed in the same section.** Hedging a claim is not the same as not making it.

**What saved it was not judgement. It was the mechanical rule that a T2 load-bearing claim gets a verifier before it cascades.** The claim never entered a thesis or a weight. **Process caught what reasoning did not** — which is the same conclusion the 08-05 correction ledger reached: I self-correct by EXECUTING, not by INSPECTING.

### 5.4 🔴 THE DIRECTION OF THE CORRECTION IS THE OPPOSITE OF WHAT I IMPLIED

This matters for anything downstream:

- **A supply-schedule delay** says the AI buildout is slipping on constraints. For memory that is **bullish-scarcity** — tight supply, firm pricing.
- **A demand-guidance reset** says AI memory demand is moderating from elevated expectations. For SK Hynix and Samsung margins that is **bearish**, and arguably **more bearish than a delay would have been.**

**I framed a bearish demand event as evidence for a supply-constraint thesis. Those are opposite readings of the same tape.** L58 applies at the level of the *mechanism*, not just the number: **the datum was real and I attached it to the wrong causal direction.**

### 5.4b What this does and does not do to the operator's fab-gated thesis

**It removes today's claimed support for it and supplies nothing against it.** The operator's argument — that the semis complex is booked out, fab-gated, and therefore trades on narrative — is **untouched by this correction**; it simply does not get 2026-08-06 as evidence. TSMC packaging and hyperscaler-accelerator schedules were **not examined** by this verification and remain genuinely open. **Absence of evidence in one window is not evidence against the thesis, and I am not converting my own overreach into a refutation of the operator.**

### 5.5 What SURVIVES the verification

The mechanical market facts largely hold and are **not** marked down:
- **매도 사이드카 at 10:18 KST on 08-06** — confirmed, first since 07-29 (한국경제).
- **SK Hynix −10.37%, Samsung −6.30%** — well-supported; lower figures circulating (−8.5%, "8%대") are intraday snapshots, flagged rather than averaged.
- **Heavy foreign net selling** — confirmed, press range ₩1.7–2.9조. §4's flow reading stands.
- **KOSPI −4.58%** — the verifier could not pin this from press (intraday prints only, band −4.0% to −4.6%). **We can, from our own two T1 fetches: 6,598.26 (08-05 close, recorded in yesterday's wake) → 6,296.38 (08-06 close, today's prevClose) = −4.575%.** This is a case where the corpus is better-sourced than the press, and the §2 defect table is unaffected.

🟢 **SK Hynix HBM4 is INDEPENDENTLY T1-REAFFIRMED AS ON-TRACK** and must not be marked down on the basis of the refuted claim: per the **SK hynix Q2 2026 earnings call, 2026-07-29 (T1, company)** — HBM4 mass-production shipment **began in Q2**, yields and quality "근접" to mature prior-gen HBM, and the company plans to **substantially expand HBM4 supply in H2**; HBM4E sampling complete, targeting 2027 production. **No delay language anywhere — a T1 reaffirmation eight days BEFORE the alleged delay narrative.** Had I cascaded the press story, I would have marked down a schedule the company had already confirmed on the record.

**Blind-check, re-specified after the refutation:** *distinguishes "a named company moved a named product's date" from "a market fell and the press supplied a reason afterwards" · reads on a company statement, filing, or call with a product name and a date attached · **goes blind if** the delay is communicated privately to customers only — but the correct handling of that case is to leave the question OPEN, not to accept an unsourced press attribution as its proxy, which is what I did.* The previous version of this blind-check made exactly that mistake: it treated absence of confirmation as weak confirmation.

---

## 6. WHAT IS STILL OWED (not invented, not papered over)

- **반대매매 (forced-liquidation) prints** — still not obtained.
- **KOSPI200 futures basis and the overnight CME/EUREX gap** — still dark, 5th consecutive session.
- ~~The delay-claim verification~~ — **RETURNED, REFUTED (§5).**
- **TSMC CoWoS/N2 and hyperscaler-accelerator schedules in the 08-04→08-06 window** — the verifier found no evidence either way and marked them **NOT ESTABLISHED, genuinely unexamined rather than disproven.** These are the two legs on which the operator's fab-gated thesis could still find support; carried as open, not closed.
- **One 08-06 Korean source (fnnews 202608061938253556) returned HTTP 403** and was not inspected. Stated rather than rounded to "all sources checked."
- **DDOG "first sequential RPO decline in years"** — T2 single-lineage, still not checked against the 10-Q.
- **ETF re-spec-or-retire** — was due 08-06, **now overdue**.
- **Quota check #4** — 5 days overdue.
- **Bare-Opus control arm** for the cross-model benchmark — cheapest outstanding high-value item.
- **Two Routine-prompt amendments requiring the operator's UI** — the EOD relative window, and the KR-OPEN retired Brent gate (§3, 4th consecutive wake).

---

## 7. POSITION IMPLICATION

**Position implication: NO ACTION** — no size change on any name.

Three findings, none of them a position trigger:
- **§2** is an instrument-labelling defect. It changes how wake readings are written, not what they say.
- **§4** is a FRAGILE flow configuration standing at **1 of the 3** readings its own pre-registered trigger requires, and the missing two cannot be back-filled.
- **§5** is a **refutation, not a signal.** The claim I flagged as potentially thesis-moving turned out to have no source; the corrected reading (a memory demand-guidance reset, not a supply delay) is **directionally bearish for the two Korean names** — but it arrives as a correction to my own error, not as new evidence, and one session of guidance reaction is not a thesis input. **SK Hynix's HBM4 schedule is T1-reaffirmed on-track and is explicitly NOT marked down.**

**Weights held H1 60 / H2 11 / H3 29.** Any sizing decision remains operator-gated regardless.

⚠️ **This section was left stale for one commit** (`bd9789b`) — it still read *"the one finding that could move a thesis is T2, unverified"* after §5 had already been rewritten to REFUTED. Corrected here rather than silently. **A summary section that outlives the analysis it summarises is the same displacement failure L60 was codified for this morning, pointed inward** — and it survived a full read-through of the file before commit.

---

**EODHD quota:** consumed this wake — logged against the daily allowance; quota check #4 remains overdue.
**Signal density (Critical Rule #14):** §4 FRAGILE-configuration reading is same-segment (memory-and-storage, Korea) and same-direction as the 2026-08-03 flow reading — **N=2 within 5 sessions.** Booked to the ADDENDUM #8 counter rather than opening a new TC cluster, since the existing pre-registered instrument already holds it.
