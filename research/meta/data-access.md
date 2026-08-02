# DATA ACCESS REGISTRY — the fact layer (canonical; every session reads this before fetching data)

**Born 2026-07-16 (API go-live day).** This file is the single source of truth for what hard-data access exists, how to use it, and what's still gapped. Update in the SAME COMMIT as any access change. Pointer lives in CLAUDE.md §File Layout.

## Epistemic frame (methodology #43b/3e, facts-first)
FACTS come from the sources below, computed and arithmetic-checked — never from press wording. Press/analyst text = data about EXPECTATIONS (the bar) + discovery of non-API facts. An agent tape claim that contradicts an API print is dead on arrival.

## Keyed APIs (env vars in the cloud environment; NEVER echo values — read via os.environ only)

| Env var | Service | Verified | Serves | Limits / gotchas |
|---|---|---|---|---|
| `FINNHUB_API_KEY` | finnhub.io | 2026-07-17 news endpoints LIVE (`/news` 100 items minutes-latency; `/company-news` per-ticker) + 07-16 calendar/quotes | US earnings calendar, quotes, **real-time headline layer (roadmap track 2 DELIVERED)** | **/stock/eps-estimate PREMIUM-GATED (403)** — do not use; calendar-embedded estimate fields untested |
| `EODHD_API_TOKEN` | eodhd.com | 2026-07-17 indices verified | **Deterministic closes: KRX (.KO); KOSDAQ .KQ; Taiwan .TW/.TWO**; US tickers; **INDICES incl. N225.INDX + TWII.INDX + KS11.INDX — same-day live (07-17 verified). The JP/TW INDEX layer is covered even though Tokyo single stocks are not** | **20 calls/day**; ~1yr history; **TOKYO single stocks NOT covered** (exchanges-list: 70 exchanges, Japan absent); `.KO` real-time feed can lag to T-1 EOD outside KR hours (07-17 observed) — cross-check timestamp field ALWAYS |
| `FRED_API_KEY` | fred.stlouisfed.org | 2026-07-16 live (DGS10) | Macro/rates series (funding-node financial rung) | generous limits |
| `DART_API_KEY` | opendart.fss.or.kr | 2026-07-16 live (status 000) | Korean official filings — SKHY primaries | individual-tier daily cap |
| `FMP_API_KEY` | financialmodelingprep.com | 2026-07-17 QUARTERLY estimates verified (NOW 2026-06-30 row: revAvg/epsAvg + high/low bands) | **US analyst estimates incl. per-quarter bands + earnings calendar (blowout input #1)** | **`/stable/` endpoints ONLY** — `/api/v3/` 403 "Legacy Endpoint"; fields renamed (`epsAvg`, `revenueAvg`); `period=quarter` returns FURTHEST-out rows first — fetch `limit=40` and filter by date locally; EPS basis (GAAP vs non-GAAP) unpinned — verify vs company-reported at first grade; **`epsEstimated` = FMP-specific consensus snapshot, finer precision than press medians — beat/miss counts VENDOR-FRAGILE (8-13pt swing on BR-1, 07-18): always publish strict + robust(|Δ|≤$0.01) variants**; ~250 calls/day |
| `ALPHAVANTAGE_API_KEY` | alphavantage.co | 2026-07-16 live | `EARNINGS_ESTIMATES` incl. **7/30/60/90-day revision history (blowout input #2)** | **25 calls/day, 1/sec**; returns HTTP 200 on errors — check body for "Error Message"/"Information" |
| `EDINET_API_KEY` | disclosure2.edinet-fsa.go.jp | NOT YET OBTAINED (parked) | JP official filings | signup needs MFA + pop-ups via the viewing-site login flow |
| (queued) `ECOS_API_KEY` | ecos.bok.or.kr | — | KR official macro incl. margin-loan/credit series | user signup pending |

## Keyless clients (in-repo tools at `meta/tools/` — work in EVERY container immediately, incl. agents)

| Tool | Source | Verified | Serves |
|---|---|---|---|
| `edgar_client.py` | SEC EDGAR (data.sec.gov + Archives) | 2026-07-16 live (TSM 6-K stream; SKHY final-ADR 6-K parse = first productive catch) | US/foreign-issuer filings at filing grade; CIK map for 12 tracked names; compliant UA + ≤6.7 req/s throttle. FTS endpoint shape unverified. |
|  `twse_client.py` | TWSE openapi + TPEx openapi | 2026-07-16 live (2330/2383/2408 closes; **EMC June monthly revenue +120.7% YoY**; TUC 6274 same-day close) | Taiwan daily closes + **monthly revenue prints (blowout input #5)** for the CCL cluster + Nanya DRAM tell; TPEx serves SAME-DAY closes; **TWSE STOCK_DAY_ALL serves T-1 until TW late-afternoon publish (07-17 13:00 CEST observed: still Jul-16 rows) — for same-day TW index use TWII.INDX on EODHD**; occasional IncompleteRead → built-in retry |

## Standing gaps (no free route — do not chase)
**JP daily tape (Murata/SUMCO/Kioxia): NO keyless machine route** — EODHD tier lacks Tokyo; Stooq is JS-challenge-walled; J-Quants free tier delayed (recall-based). Stays agent-fetched w/ date-pins; candidates: EODHD paid tier, J-Quants verify. · DRAM/NAND spot+contract (TrendForce/DRAMeXchange, paid — most valuable paid upgrade for the memory book) · KR/JP consensus (FnGuide/QUICK — user screenshot batches remain the route) · options flow (paid) · KOFIA 반대매매 (portal, agent-fetched) · KOFIA freesis raw (403s agents).

## Retrieval-infra fix — WebFetch 403 ≠ site-blocked (added 2026-07-20, discovered in the CXL 4-round verification arc)
**The subagent WebFetch tool gets HTTP 403 on many sites (zdnet.co.kr, sedaily.com, x.com, thelec.kr, naver) — but this is a BOT-BLOCK on WebFetch's user-agent, NOT the site being unreachable.** Proven 2026-07-20: `curl -sS -A "Mozilla/5.0 …Chrome…" https://zdnet.co.kr` returns **HTTP 200** where every agent WebFetch returned 403. **CONSEQUENCE (this session's cost): 4 verification rounds / 6 agents concluded a real Korean-trade-press claim was "fabricated/unverifiable" when the source was reachable all along via curl.** BINDING FIX:
- Before concluding "source not found / can't verify / likely fabricated" on a KR/JP/paywalled outlet, **the ORCHESTRATOR (main loop, Bash) must retry with `curl -sS --max-time 20 -A "<browser-UA>" <url>`** — Bash curl is NOT subject to the WebFetch UA block. Section/listing pages work (`zdnet.co.kr/news/?lstcode=0050` = chip section); article pages work (`/view/?no=<id>`); their JS `/search/` endpoint returns a 647-byte shell (not curl-renderable — navigate section pages or an external index instead).
- **"Unreachable ≠ fabricated" (L39 refinement):** a retrieval failure via one tool is NOT evidence a source doesn't exist. Diagnose the RETRIEVAL LAYER (proxy status via `curl "$HTTPS_PROXY/__agentproxy/status"`; curl-UA fallback) BEFORE assigning a fabricated/unverified verdict.
- Agents cannot run this fallback reliably (their WebFetch is UA-blocked and Bash-curl availability varies) → the ORCHESTRATOR owns the curl-fallback step. Candidate: a `meta/tools/fetch_kr.py` browser-UA curl wrapper agents can shell out to.
- **FIRST END-TO-END PAYOFF (2026-07-20):** in the Samsung–Nvidia NAND/CMX INGEST, both agents got 403 on `thelec.kr` #28871 (direct AND via r.jina.ai) — the single load-bearing source for the molybdenum-generation-sequencing question. Orchestrator ran `curl -sS --max-time 25 -A "Mozilla/5.0…Chrome…"` → **HTTP 200, 123KB**; title + body extracted, and the question RESOLVED: moly was first applied at **V9 (2024-07-02)**, NOT "from V10 (2026)" as the brief claimed — an inversion + a 2-yr temporal-staleness catch that the curl-fallback made, and that would otherwise have been logged as "unverifiable." **This validates the fix: the binding constraint on ~6 prior CXL-round agents was retrieval-layer UA-blocking, not source absence.** Reusable one-liner: `curl -sS --max-time 25 -A "<browser-UA>" "https://www.thelec.kr/news/articleView.html?idxno=<ID>"` then parse `itemprop="articleBody"`.

## Disciplines (binding)
1. **NEVER-ECHO:** key values never printed/logged/committed; fetch scripts read os.environ; test agents report presence/length/status only.
2. **Vendor data is an input, not truth:** consensus figures cross-check against filed actuals (EDGAR/DART) before entering any pre-registration bar (origin: MU FY26 consensus 8.4×-in-3yr sanity flag, 2026-07-16).
3. **Quota budgeting:** EODHD 20/day (tape fetch ≈6-8), AV 25/day — batch, don't poll.
4. **Env-var propagation is EVENTUALLY-CONSISTENT, not strictly boot-time** (2026-07-16 empirical: a long-running session's container picked up 4 newly-added keys mid-day). Verify presence by running `bash meta/tools/setup.sh` + reading /tmp/llmna-boot-status.txt — never assume either way.
5. **Boot status file:** the cloud environment's Setup-script field runs `meta/tools/setup.sh` at container start → `/tmp/llmna-boot-status.txt` (key presence + keyless-endpoint reachability + repo HEAD). Read it at wake instead of re-testing.

## ROADMAP — user directive 2026-07-16 EVE: two new tracks ("you must get access to ETF/fund flows + institutional money flows, and minutes-latency news headlines")
| Track | Route | Cost | Status |
|---|---|---|---|
| Flows/institutional | **PLAN + first wires LIVE 2026-07-17 — see `meta/flows-positioning-acquisition-plan.md` (canonical).** TWSE T86 per-stock foreign/inst flows WIRED (`twse_client.t86_institutional`, keyless, T+0) · CFTC COT free-verified (deafut.txt) · JPX investor-type weekly reachable (xls) · KRX investor-type 403s containers (Open-API signup = user option; agent-bridge T2 meanwhile) · 13F via edgar_client (Aug sweep) · ICI/AAII/NAAIM monthly context · paid flows products ALL deferred/skip per plan (evidence-gated) | free | **DELIVERED (partial) — COT + JPX wires queued next wake** |
| Real-time headlines | **Finnhub /news + /company-news — LIVE, verified 2026-07-17** (general feed ~minutes latency; per-ticker 3-day window returned 127 IBM items) · GDELT 2.0 keyless (**429 rate-limited on 07-17 first try — flaky, retry with backoff, not load-bearing**) · wire RSS | free | **DELIVERED — wake protocol now includes a Finnhub headline pull** |
Rationale (user hypothesis, booked): human pattern-matching binds on ingestion; the system's doesn't — but pattern-capacity scales the false-pattern rate too, so every new data track feeds PRE-REGISTERED tells (tripwires, node tells), never free-form pattern hunting. Discriminating-signal ranking for competing-scenario resolution: flows/positioning > forward prices (spreads live via FRED; options gapped) > supply-chain leading indicators (TW monthlies live) > surveys.

## Falsifier / re-eval
Monthly audit: any registry row not exercised in 30 days gets flagged; any gotcha proven wrong gets corrected here (not in day-state). If this file drifts from reality (a session hits a documented-as-working endpoint that fails), fixing THIS FILE is part of the fix.


## Route findings — 2026-07-27 KR-open wake (per `signals/cross-source-log/2026-07-27-mon-kr-open-wake-escorted-reading-live-tick.md` §4)
- **✅ NEW: EODHD `/api/real-time` DOES serve KRX same-day live quotes during KR hours** — verified 00:06Z ≈ 09:06 KST, six minutes after the open, on `KS11.INDX` / `000660.KO` / `005930.KO`. Every KR-open wake 07-21→07-24 logged DATA-GAPPED at this hour; this removes that contamination ceiling. **Corrects the standing `.KO` note:** the feed lags to T-1 *outside* KR hours and is live *inside* them — state it that way.
- **❌ EODHD `/api/intraday` → HTTP 403** (`KS11.INDX`, `000660.KO`). Opening-auction sell-concentration (an I-3 primary input) is NOT machine-reachable on this tier.
- **❌ EODHD commodities → HTTP 403** on `BZ.COMM` / `BRN.COMM` / `CO.COMM` / `BZ=F.COMM`. **Brent has no deterministic route.** The single most consequential macro threshold the harness tracks depends entirely on agent-fetched T2 press — which is exactly how the L43 benchmark error entered. **Highest-value paid-data upgrade candidate after DRAM/NAND contract pricing.**
- **⚠️ FRED publication lag is load-bearing:** `DGS10` had no 07-24 observation as of 07-27 00:30Z. When a gate turns on a rates *direction*, check FRED's latest observation date before concluding — the most recent session is routinely absent.
- **KRX 투자자별 portal + KOSPI200 futures basis: unreachable** (JS-shell, not a clean 403). Naver Finance's polling API **was** reachable via curl + browser-UA and returned internally-consistent live quotes — currently the most reliable same-day KR channel.

## [2026-07-28] COMMODITIES GAP PARTIALLY CLOSED + KR FLOW GAP NAMED (per `signals/cross-source-log/2026-07-28-tue-kr-open-wake-selloff-resumes-vendor-prevclose-defect.md` §3.2, §4)

**✅ Brent/WTI route FOUND (FRED, keyed, T1) — but bounded:** `DCOILBRENTEU` (Brent Europe) and `DCOILWTICO` (WTI Cushing) are served by the existing `FRED_API_KEY`. **Two hard limits, both basis/latency, both binding:**
1. **BASIS: these are daily SPOT FOB series, NOT futures settles.** The H3 gate is defined on a Brent **settle**. Per L43 the two are different instruments and must not be substituted. Using FRED spot to adjudicate a settle-defined gate is the exact error class already booked twice.
2. **LAG: ~6 business days.** On 2026-07-28 the latest observation was **2026-07-20**. Useless for a same-day gate.
**⇒ Verdict: usable RETROSPECTIVELY for named-benchmark oil history; NEVER for a same-day threshold read.** EODHD remains 404/422 on every Brent symbol tried (`BZ.COMM`, `BRN.COMM`, `CO.COMM`, `BZ=F`, `BRENT.COMM`); `BZUSD.FOREX` resolves but returns `"NA"` on all fields.
**Open tension recorded, not resolved:** FRED Brent spot ran $81.23 (07-16) → $86.99 (07-20) while the corpus carries Brent futures settle **$96.78 on 07-24** (T2 ×3). That implies ~+11% in four sessions — plausible on the reported run toward $100, but the series are not interchangeable and this is flagged for the next clean adjudication rather than reconciled by assumption.

**❌ NAMED GAP — KR flow instruments have NO keyed route, and one of them gates a pre-registered trigger:**
| Instrument | Purpose | Consequence of the gap |
|---|---|---|
| **KRX 투자자별 investor-type flows** | **Pre-registered escalation trigger: foreign net-sell ≥3 consecutive sessions** | **The trigger is UNREADABLE — not "not fired." Those are different states and must be logged differently** |
| 반대매매 daily stats | Retail forced-liquidation read | H3-cluster input unavailable |
| KOSPI200 futures basis + overnight CME/EUREX gap | Gapped-in vs sold-in-session discrimination | Cannot separate overnight from intraday supply |
| KOFIA margin balance | Policy-contaminated SECONDARY only | — |
| Dubai EFS / JKM / war-risk premia | Non-Brent 2-of-5 dashboard | Escalation review cannot run |
**Fix candidate:** KRX OpenAPI and/or the queued `ECOS_API_KEY` (BOK, already listed as user-signup-pending). **Until then, any wake artifact must record the escalation trigger as UNREADABLE rather than silently omitting it.**

**⚠️ VENDOR DEFECT, dated and reproducible:** EODHD **real-time INDEX** feeds (`KS11.INDX`, `KQ11.INDX`) returned a **STALE `previousClose`** on 2026-07-28 00:05Z — carrying the 07-24 close rather than 07-27. Single-stock `.KO` feeds carried the correct prior close. **The vendor's own `change_p` was therefore wrong by −0.92pp on KOSPI and −2.14pp on KOSDAQ.** **Standing rule from this: NEVER read `change_p`; always compute from the tick against a close verified out of the EOD series.**


## 2026-07-28 EOD route notes (per the EOD Leg-B verification run)
- **EODHD Korean singles: use `.KO` suffix** — `000660.KO` / `005930.KO` returned clean EOD series tonight while `.KS` returned HTTPError (route drift vs earlier sessions; `.KRX` also errors). Indices unaffected (`KS11.INDX` fine). Verify suffix per session; compute deltas from the EOD series per the standing change_p ban.
- **Brent still has NO machine route**: `BZ.COMM` HTTPError on EODHD; FRED `DCOILBRENTEU` spot-FOB ~6-day lag. Settle-defined gates (H3) adjudicate on press-named settles, basis-stamped, until a futures-settle route is registered.
- **Credit/CDS gap (NEW, flagged by the 07-28 absence question):** no route for CDS levels or corporate bond spreads — TC-2 rung 3 now has traded-price marks (NVDA CDS, DC-bond yields) the harness cannot machine-read. Candidate sources to evaluate: FRED HY/IG OAS series (ICE BofA) as coarse proxy; issue-level data likely needs a paid route.
- **2026-07-29 EODHD same-day EOD-row defect (N+1 of the vendor-basis family):** the KS11.INDX EOD row for the CURRENT session printed 5,538.15 while the real-time endpoint and press both said 5,663.24 — the EOD row was mid-update at fetch. **Standing rule extension: never read a same-day EOD row; use real-time computed vs the verified prior close intra-day, and only trust the EOD row from T+1.**

## 2026-07-30 route additions (agent-A verified)
- **Treasury.gov daily yield-curve CSV (home.treasury.gov): T1 full par curve, SAME-DAY 3:30pm ET official — closes the FRED DGS10 T+1 lag gap.** Prefer for all UST tenors.
- CBOE delayed-quote JSON `cdn.cboe.com/api/global/delayed_quotes/quotes/_VIX.json` = keyless T1 VIX.
- CNBC `quote.cnbc.com/.../restQuote/...&exthrs=1` = keyless indices + after-hours + futures.
- UA-block list extended: cnbc.com, federalreserve.gov 403 on WebFetch, 200 on curl with browser UA. Meta IR Cloudflare-walled → use EDGAR 8-K Ex-99.1 (CIK 0001326801).
- CME Settlements endpoint 403 (no direct fed-funds futures route; FedWatch remains T2-derivative).
- **EODHD daily quota is REAL: 19/20 consumed 2026-07-30 by a 12-ticker batch + wake fetches. Finnhub `/quote` is unmetered at tier and matched EODHD to the cent on 12/12 US names — default US singles to Finnhub, reserve EODHD for KR/JP/indices.**

## 2026-07-31 — EODHD INDEX DEFECT: NOT CONFINED TO `prevClose` (N+1, new field)
Confirmed on **both** KR indices simultaneously at the 07-31 KR-open wake: `KS11.INDX` returned `prevClose` **5,663.24** and `KQ11.INDX` returned **662.68** — both are the **T-2 (07-29)** closes, not 07-30 (5,593.56 / 644.78). Single stocks were correct in the same call. **NEW this instance: the `open` field is ALSO corrupt** — KS11 returned `open` 5,657.79 for a session that had already printed 6,386.05. **Rule: on EODHD INDEX symbols, treat `prevClose`, `open`, and any derived `change_p` as untrusted; recompute every index % change off an independently verified close.** Singles (`.KO`/`.KQ`) remain reliable. Companion to the same-day-EOD-row defect already logged.

## 2026-07-31 — FRED OIL SERIES: DEMOTE TO CONTEXT-ONLY FOR THE H3 GATE
`DCOILBRENTEU` carries a persistent **~$2+ wedge** vs press front-month and publishes 3 business days late (07-27 print = $91.82 while press reported Brent below $90 the same day). It also printed **$105.32 (07-23)** and **$100.31 (07-24)** — levels the front-month press record does not corroborate. **The $95 H3 gate must be adjudicated on press-settle basis with a mandatory as-of date (addendum #10 declared-cut rule), NOT on FRED.** FRED oil retained for trend context only. FRED rate series (`DGS2/5/10/30`) remain T1-reliable, publishing T+1.

## 2026-07-31 — PROXY 403 WALL: THE HARNESS IS STRUCTURALLY CAPPED AT T2 FOR MARKET DATA
Across three research legs, WebFetch returned **HTTP 403 on the large majority of financial-press and exchange domains**: CNBC, Forbes, TradingEconomics, OilPrice, Fortune, Lloyd's List, Bloomberg, Businesskorea, fnnews, asiae, mt.co.kr, etoday, sedaily, hankyung, finance.naver.com, finance.daum.net, news.samsung.com, thelec.kr, investing.com, newsis.com. `data.krx.co.kr` additionally requires **POST/JS** (MDCSTAT024) and cannot be reached by simple fetch. **Consequence: figures route through WebSearch summaries (T2) rather than direct-source reads, so T1 tier is frequently unobtainable even when a T1 document exists.** Also: Finnhub `forex/rates` returns 403 (not entitled on this key) and Finnhub does not serve `^SOX`/`^GSPC`/`^IXIC` (HTTP 200, null payload) — use SOXX/SMH/SPY/QQQ ETF proxies and say so. **This is an infrastructure constraint, not a research failure — record it as a tier ceiling rather than re-discovering it each wake.**

## 2026-07-31 — 🔴 NEW VENDOR DEFECT: FMP `changePercent` IS NOT CLOSE-VS-PRIOR-CLOSE
**FMP's `changePercent` field computes `(close − open) / open`, NOT close vs the PRIOR close.** Verified 2026-07-31 on META 07-23: FMP reported **−0.380%**; the true close-to-close change is **−3.360%** — a **2.980pp error on a single row**, and the error equals the overnight gap, so it is largest exactly when a print has moved the stock. **Any corpus figure sourced from that field is wrong by the overnight gap.**
**RULE: drop `changePercent` on ingest from FMP, as we already do for EODHD `change_p`. Compute every percent change ourselves from two verified closes.** Same defect family, different vendor — the family now has **three** members (EODHD index `prevClose`/`open`/`low`, EODHD same-day EOD row, FMP `changePercent`). **Treat any vendor-supplied percent-change field as untrusted by default; the burden is on the vendor to prove the basis, not on us to assume it.**

## 2026-07-31 — EXTENDED-HOURS HISTORY IS NOT MACHINE-RETRIEVABLE (structural gap, not a one-off)
No route available to this harness returns **historical** after-hours prints. Finnhub `/quote` serves only the live tick; the CNBC `exthrs=1` route serves *tonight's* extended session, not a prior date's. **Consequence: every after-hours reaction figure in the corpus is T2 press or a carry-forward — none is T1.** This is the structural weak leg of the earnings reaction ledger and it will recur every quarter until a paid extended-hours route is added. **Record AH reactions as a RANGE (`ah_lo`/`ah_hi`) rather than a point wherever press figures disagree — they usually do, because they sample different moments of the same evening.**

## 2026-08-02 — NEW DEFECT: FRED `BAMLH0A0HYM2` (ICE BofA HY OAS) silently truncated to ~3 years

**Route ADDED (the flagged material gap is closed):** credit spreads are now reachable at T1 via FRED `BAMLH0A0HYM2`. Reading 2026-07-30 = **2.84% (284bps)**. Companion series verified same session: `DGS10` (UST 10Y, 4.68% 07-30) and `DEXJPUS` (JPY/USD, 163.71 07-24 — note DEXJPUS lags ~1 week).

**⚠️ DEFECT — the series returns only from 2023-08-01 regardless of `observation_start`.** Requested 2001-08-02 → got 2023-08-01. Re-requested 1990-01-01 → still 2023-08-01. `count=787`, `limit=100000`, `offset=0`, so it is not pagination.

**Why this is dangerous rather than merely limiting:** the call succeeds, returns a clean series, and the values are entirely plausible. Only a sanity check on the *extremes* exposes it — a 25-year HY OAS maximum of 461bps is impossible (the series exceeded 2,000bps in 2008). **I computed and nearly reported a "25-year percentile" that was actually a 3-year percentile.** Same shape as the EODHD index-field corruption: the failure is in the metadata, not the numbers, so value-level inspection passes it.

**Blind-check (#51):** distinguishes "spreads are historically tight" from "spreads are tight versus a truncated window" · reads on **the first observation date returned**, not on the values · **goes blind if a caller checks only the values** — which is exactly how the first pass failed, because the values looked reasonable in isolation.

**OPERATING RULE:** any percentile, "richest since", or "tightest in N years" claim from a FRED series MUST print the actual first-observation date alongside the claim. Do not state a window length that was requested rather than returned.

**Consequence for tonight's read:** the correctly-labelled figure is **284bps = tightest 24.7% of the LAST THREE YEARS**, 3y median 310bps, 3y min 259bps, **25bps of room to the 3-year low**. Any longer-horizon credit percentile is currently **UNOBTAINABLE at T1** in this harness — treat multi-decade credit claims from press as unverifiable, not as corroborated.
