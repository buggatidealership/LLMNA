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
