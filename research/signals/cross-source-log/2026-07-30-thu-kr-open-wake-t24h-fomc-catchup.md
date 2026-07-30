# 2026-07-30 THU — KR-open wake: T+24h reaction day + FOMC/US-close catch-up (last night's sweep was 529-blocked)

**WORKFLOW: KR-OPEN WAKE (W11 time-sensitive leg).** Sync clean (0 behind). Three Opus agents in flight: A = FOMC decision + US close attribution + MSFT/META prints (the carried gap); B = KR flows day-4 read + 반대매매 covering prints + call-transcript re-check; C = H3 dashboard day-3 (Wednesday Brent settle = the un-breach review's decisive datum).

## §1 TAPE (T1-machine EODHD, computed vs verified closes; same-day EOD rows NOT read per the 07-29 rule)

| Instrument | 07-30 09:25 KST | vs verified 07-29 close |
|---|---|---|
| KOSPI | open 5,681.77 (+0.33%) → **5,614.18 (−0.87%)** | 5,663.24 |
| KOSDAQ | open 654.72 (−1.20%) → 655.62 (−1.07%) | 662.68 |
| SK Hynix | open 1,361,000 (−2.86%) → **1,333,000 (−4.85%)** | 1,401,000 |
| Samsung | open 214,000 (+2.64%) → 207,250 (−0.60%) | 208,500 |

**US 07-29 closes (EOD T+1 rule satisfied, computed):** S&P **7,316.15 −1.52%** · NDX **27,192.31 −2.06%** · Dow **51,594.14 −2.19%**. ⚠️ **The Dow fell MORE than the S&P — the segment-scoped inversion (07-28/29 booking: US up-days ex-AI-infra) did NOT hold post-FOMC; Wednesday was market-wide. Attribution to agent A.** Vendor note: EODHD's finalized 07-28 US closes differ slightly from Tuesday's real-time prints (GSPC 7,428.78 final vs 7,435.69 RT) — settle-revision class, logged; deltas computed off the finalized series.

**T+24h reaction read (preliminary, grade pending agent data):** SKHY −9.61% (day 1) → −4.85% and falling (day 2) — the print morning's relief bounce (+4.45% high) fully reversed and extended; the reaction grade needs the FOMC/market-wide leg decomposed from the CXMT/idiosyncratic leg.

## §1b Rates leg (FRED T1-machine)
DGS10 series: 07-23 4.71 → 07-24 4.69 → 07-27 4.65 → **07-28 4.61** (FRED final; Tuesday press said 4.62 — settle-revision class, minor). 07-29 post-FOMC close not yet in FRED (T+1 lag) — agent C carries it.

## §2.1 H3 dashboard day-3 (agent C returned ~00:55Z) — AND THE JOINT REWEIGHT EXECUTES

### The decisive data (basis-labeled, settle-confirmed 2 outlets)
- **Brent Wednesday SETTLE $90.74, +7.9%** ([CNBC](https://www.cnbc.com/2026/07/29/oil-prices-today-brent-wti-iran-us-hormuz.html) + MarketScreener; arithmetic check: +$6.79 off the intraday 90.88 implies prior settle $84.09 = exact corpus match). WTI settle $84.46 +6.6%. **Three consecutive settles below the $95 gate ($88.36 / $84.09 / $90.74) — the gate is NOT breached, headroom $4.26 (4.7%) — but the direction has violently reversed.**
- **FOMC: HELD 3.50-3.75%, vote 9-3 — all three dissents FOR A HIKE** (Hammack, Kashkari, Logan; [CNBC](https://www.cnbc.com/2026/07/29/fed-rate-decision-july-2026.html) T1-adjacent). **30Y 5.201% = highest since July 2007**; 10Y 4.671% +7bp; 2Y −4bp (steepener); **Sept hike odds >57% post-decision** (CME FedWatch via CNBC). Warsh: higher rates "could become an appropriate policy response." Dots 3.6-4.1%.
- **US tape:** Dow −2.19% = **worst day since April 2025**; Nasdaq Composite −1.74%, >10% off ATH; **VIX 20.66 +13.45%** — the financial-calm leg of the divergence finally BROKE toward the physical leg. Gold overnight $4,078, touched $4,100 in Asia.
- **Physical dashboard EXTREME and fresh-confirmed:** Hormuz transits **78/week vs 174 two weeks prior** (Lloyd's List via USNI T2); **VLCC TD3C WS386.78 = $382,397/day TCE** (07-29); **Brent-Dubai EFS $13.22 highest since May 4** (07-23, stale 6d); JKM $21.43 +33.5% m/m (CFD proxy 🟡); war-risk ~5-10% hull (stale 6d). Iran: IRGC missiles at a US base in Jordan (intercepted); US+Saudi joint strikes on Iraqi militias; Houthis hit Yanbu-feeding pipeline; Trump "hitting them hard" rhetoric; Oman channel alive (Iran-administers-transit compromise floated) but no agreement.

### ⚖️ H3 JOINT REWEIGHT — EXECUTED (pre-registered consequence, both triggers now aligned; my-model weight layer, NOT a position action)
The two registered triggers no longer point opposite: the KR flow trigger FIRED at N=3 accelerating (07-29 booking), and the oil leg's un-breach premise is functionally dead — settles remain sub-95 (no gate breach) but Wednesday's +7.9% settle, the transit collapse, VLCC/EFS extremes, AND the rates path (30Y at a 19-year high, 3 hike dissents, Sept >57%) all load the H3 transmission (oil→rates→risk-off) in the SAME direction, with the US tape (Dow worst day since Apr-2025, VIX +13.45%) as the realized output. Per addendum #8's pre-registration (foreign net-sell ≥3 sessions → H3 ~35): **five-calls weights move H1 60 → 54 / H2 12 → 11 / H3 28 → 35 (my model)** — booked as five-calls ADDENDUM #12. Falsifier-side note per Rule #18: the strongest case AGAINST the reweight is that the Oman channel produces a transit agreement within days (gold/VIX would mean-revert and the KR flow could flip on relief) — if Brent settles <$85 for 2 consecutive sessions with a signed mechanism, review back down. **NO POSITION ACTION — user-gated; weights are the interpretive layer only.**

## §2.2 FOMC + US close catch-up (agent A returned ~01:20Z)

### ⚠️ PREMISE CORRECTION (T1, booked loudly): the Fed chair is KEVIN WARSH, not Powell — since May 2026; 07-29 was his second meeting. My agent-A prompt said "Powell presser" (recall-based error, mine). Corpus grep: `sector/where-we-are.md` carries no Powell reference (verified clean); future Fed items key on Warsh.

### FOMC substance (T1 federalreserve.gov + transcript PDF)
- Held 3.50-3.75%, 5th consecutive; **vote 9-3, all three dissents FOR +25bp** (Hammack/Kashkari/Logan) — first 3-same-direction dissent since Sept 2016 (T2). **Statement text near-verbatim identical to 06-17 (agent diffed both): the entire information content of the meeting is the vote split.** Non-SEP meeting, zero September guidance. IORB 3.65%; Desk buying T-bills to maintain ample reserves (= not QT).
- **Warsh verbatim, the harness-relevant quote:** *"The business capex boom... is driving up prices of **memory and logic chips** and associated A.I. infrastructure. Do those changes indicate a broader inflationary dynamic, or do we just focus on them because they are under the bright streetlight?"* — **memory pricing is now explicitly inside the Fed's inflation-discussion set.** Also: AI-related equipment/software capex "nearly 20 percent" 4-quarter growth; inter-meeting yield moves "top decile... in the last two decades."
- **September odds FELL, not rose: ~80% (07-27) → 54% post-decision (−26pp, directional — third-party FedWatch derivative; CME direct 403s).** T1 corroboration via the Treasury curve: front-end RALLIED (6M −10bp, 2Y −4bp) while 10Y +6bp / 30Y +11bp to **5.20% (2007 high)** — 2s10s 35→45bp, 2s30s 83→98bp (computed). **Joint read (🟡): a term-premium/credibility repricing, NOT a hawkish policy repricing — the hike dissents did not move September up.** ⟦Refines §2.1's "Sept >57%" line: level consistent, but the DIRECTION of the repricing was DOWN from 80%.⟧

### US attribution — Wednesday was a SEMIS ROUT, not a Fed day (correcting my §1 provisional "market-wide" read)
- **Concentration decisive (computed, 2-vendor cent-exact):** SOX **−5.33%** vs equal-weight RSP **−0.90%**; cap-weight fell 1.71× equal-weight; NYSE decliners only 1.43:1. Per-name: **MU −9.94%** (closed at low), SNDK −7.32%, MRVL −6.34%, AMD −5.51%, NVDA −3.55%, TSM −4.50%; **KLAC −10.80% ON A RAISED GUIDE** (→ anomaly register); **STX +2.29% the only memory-adjacent gainer** (HDD beat); GOOGL +0.90%. **The Dow's "worst day since Apr-2025" was its own members, not breadth — the segment-scoped inversion SURVIVES in refined form: epicenter memory/semis, ordinary tape beneath (equal-weight −0.90%).**
- Timing (T2 headline-stamps only, 5-min bars DATA-GAPPED): ~66% of the S&P loss and ~78% of the Dow's were on the tape BEFORE the 14:00 statement — do not grade the pre/post split.
- **SKHY ADR −2.60% close ($126.79) vs local −9.61% — the ADR/ordinary spread COMPRESSED**; CNBC ran "Is the SK Hynix ADR premium the market's latest bubble warning?" (T2). Feeds the venue-reconciliation item.

### MSFT / META (both Wed AMC, T1 releases/8-K) — the capex-tolerance fork made flesh
| | MSFT | META |
|---|---|---|
| Print | Rev $90.007B +0.7% vs cons; **EPS $4.74 +9.5%**; **Azure +43%** (cons 40.2%); RPO $678B +84% | Rev $60.801B −0.9% vs cons; **EPS $6.18 −16.0% MISS**; op margin 31% vs 43% PY (−12pp; $2.40B legal + $1.18B severance inside) |
| Capex | Q4 PP&E **$35.8B +109.6% YoY**; FY26 $115.9B +79.6%; FY27 "further growth" (~$175B on the new lease/life basis — NOT comparable to GAAP line); building useful-life 15→25yr | Q2 **$31.08B** incl. fin-leases; **FCF $784M** vs op-CF $31.9B; FY26 capex band low-end RAISED ($130-145B); expenses raised $165-169B |
| AH | **+8.88%** | **−7.45%** |
**Read (🟡, ties to TC-2 rung 3):** same capex direction, opposite equity outcome — the market is now pricing the FUNDING QUALITY of capex (FCF cover), which is TC-2's mechanism showing up in equity reaction, not just credit. Note MSFT booked a **$3.2B Anthropic gain** in the quarter. **AMZN + AAPL tonight (Thu AMC).**

### Adjudication: agent A's "contamination flag" on SKH net profit — REFUTED, our T1 stands
Agent A (which did not pull DART this pass) flagged "net profit ₩93.92tn > revenue = arithmetically impossible — do not ingest." **The on-file T1 DART filing (rcpNo 20260729800013) shows exactly NI ₩93.92T via pre-tax ₩122.71T including the ₩62.2T Kioxia disposal/valuation gain (composition solved 07-29) — unusual, not impossible; net margin 118% is booked WITH the non-operating caveat.** Kept as a clean example: plausibility heuristics lose to primary filings. Agent's "$96.78 07-24 settle unreconciled vs $89.57 now" — reconciled by the intervening corpus path (96.78 → 88.36 → 84.09 → 90.74 settles); no action.

### Other structural (24h)
1. **FCC bans imports of Chinese humanoid/quadruped robots AND power inverters** (07-29, Covered List; [CNN](https://www.cnn.com/2026/07/29/tech/us-china-robot-ban-intl-hnk) T2) — **the inverter clause is the underpriced half: DC + solar BOM item** → TC-13 rung candidate, bottlenecks review.
2. CXMT follow-on: US senators formally warn Apple against Chinese memory sourcing; Capitol Hill probe triggered (T2 — upgrades the 07-28 T3 probe item).
3. KLAC −10.80% on raised guidance → anomaly register (process-control WFE derating harder than memory on GOOD news — does not fit the China-competition story).

### Retrieval-layer wins (→ data-access.md)
**Treasury.gov daily yield-curve CSV = T1 full curve SAME-DAY (closes the FRED DGS10 T+1 gap)** · CBOE delayed-quote JSON = T1 VIX · CNBC restQuote = indices+AH+futures keyless · cnbc.com + federalreserve.gov 403 via WebFetch but 200 via curl browser-UA (UA-block list extended) · Meta primaries via EDGAR 8-K (IR site Cloudflare-walled) · CME settlements still 403 (FedWatch stays T2-derivative) · **⚠️ EODHD quota 19/20 consumed today — US singles via Finnhub (unmetered, cent-exact match on 12/12) for the rest of the session.**
