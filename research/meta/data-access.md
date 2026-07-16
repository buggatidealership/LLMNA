# DATA ACCESS REGISTRY — the fact layer (canonical; every session reads this before fetching data)

**Born 2026-07-16 (API go-live day).** This file is the single source of truth for what hard-data access exists, how to use it, and what's still gapped. Update in the SAME COMMIT as any access change. Pointer lives in CLAUDE.md §File Layout.

## Epistemic frame (methodology #43b/3e, facts-first)
FACTS come from the sources below, computed and arithmetic-checked — never from press wording. Press/analyst text = data about EXPECTATIONS (the bar) + discovery of non-API facts. An agent tape claim that contradicts an API print is dead on arrival.

## Keyed APIs (env vars in the cloud environment; NEVER echo values — read via os.environ only)

| Env var | Service | Verified | Serves | Limits / gotchas |
|---|---|---|---|---|
| `FINNHUB_API_KEY` | finnhub.io | 2026-07-16 live-call | US earnings calendar (1,500 entries tested), quotes | **/stock/eps-estimate PREMIUM-GATED (403)** — do not use; calendar-embedded estimate fields untested |
| `EODHD_API_TOKEN` | eodhd.com | 2026-07-16 live (KRX + exchanges-list) | **Deterministic closes: KRX (.KO) verified same-day; KOSDAQ .KQ, Taiwan .TW/.TWO also in list**; US tickers | **20 calls/day**; ~1yr history; **TOKYO NOT COVERED on this tier** (exchanges-list: 70 exchanges, Japan absent — the 6981.TSE 404 was coverage, not suffix); token in old-session remote rigs may be stale (401) |
| `FRED_API_KEY` | fred.stlouisfed.org | 2026-07-16 live (DGS10) | Macro/rates series (funding-node financial rung) | generous limits |
| `DART_API_KEY` | opendart.fss.or.kr | 2026-07-16 live (status 000) | Korean official filings — SKHY primaries | individual-tier daily cap |
| `FMP_API_KEY` | financialmodelingprep.com | 2026-07-16 live | **US analyst estimates + earnings calendar (blowout input #1)** | **`/stable/` endpoints ONLY** — `/api/v3/` returns 403 "Legacy Endpoint" for post-Aug-2025 keys; fields renamed (`epsAvg`, `revenueAvg`); ~250 calls/day |
| `ALPHAVANTAGE_API_KEY` | alphavantage.co | 2026-07-16 live | `EARNINGS_ESTIMATES` incl. **7/30/60/90-day revision history (blowout input #2)** | **25 calls/day, 1/sec**; returns HTTP 200 on errors — check body for "Error Message"/"Information" |
| `EDINET_API_KEY` | disclosure2.edinet-fsa.go.jp | NOT YET OBTAINED (parked) | JP official filings | signup needs MFA + pop-ups via the viewing-site login flow |
| (queued) `ECOS_API_KEY` | ecos.bok.or.kr | — | KR official macro incl. margin-loan/credit series | user signup pending |

## Keyless clients (in-repo tools at `meta/tools/` — work in EVERY container immediately, incl. agents)

| Tool | Source | Verified | Serves |
|---|---|---|---|
| `edgar_client.py` | SEC EDGAR (data.sec.gov + Archives) | 2026-07-16 live (TSM 6-K stream; SKHY final-ADR 6-K parse = first productive catch) | US/foreign-issuer filings at filing grade; CIK map for 12 tracked names; compliant UA + ≤6.7 req/s throttle. FTS endpoint shape unverified. |
| `twse_client.py` | TWSE openapi + TPEx openapi | 2026-07-16 live (2330/2383/2408 closes; **EMC June monthly revenue +120.7% YoY**; TUC 6274 same-day close) | Taiwan daily closes + **monthly revenue prints (blowout input #5)** for the CCL cluster + Nanya DRAM tell; TPEx serves SAME-DAY closes; occasional IncompleteRead → built-in retry |

## Standing gaps (no free route — do not chase)
**JP daily tape (Murata/SUMCO/Kioxia): NO keyless machine route** — EODHD tier lacks Tokyo; Stooq is JS-challenge-walled; J-Quants free tier delayed (recall-based). Stays agent-fetched w/ date-pins; candidates: EODHD paid tier, J-Quants verify. · DRAM/NAND spot+contract (TrendForce/DRAMeXchange, paid — most valuable paid upgrade for the memory book) · KR/JP consensus (FnGuide/QUICK — user screenshot batches remain the route) · options flow (paid) · KOFIA 반대매매 (portal, agent-fetched) · KOFIA freesis raw (403s agents).

## Disciplines (binding)
1. **NEVER-ECHO:** key values never printed/logged/committed; fetch scripts read os.environ; test agents report presence/length/status only.
2. **Vendor data is an input, not truth:** consensus figures cross-check against filed actuals (EDGAR/DART) before entering any pre-registration bar (origin: MU FY26 consensus 8.4×-in-3yr sanity flag, 2026-07-16).
3. **Quota budgeting:** EODHD 20/day (tape fetch ≈6-8), AV 25/day — batch, don't poll.
4. **Env-var propagation is EVENTUALLY-CONSISTENT, not strictly boot-time** (2026-07-16 empirical: a long-running session's container picked up 4 newly-added keys mid-day). Verify presence by running `bash meta/tools/setup.sh` + reading /tmp/llmna-boot-status.txt — never assume either way.
5. **Boot status file:** the cloud environment's Setup-script field runs `meta/tools/setup.sh` at container start → `/tmp/llmna-boot-status.txt` (key presence + keyless-endpoint reachability + repo HEAD). Read it at wake instead of re-testing.

## Falsifier / re-eval
Monthly audit: any registry row not exercised in 30 days gets flagged; any gotcha proven wrong gets corrected here (not in day-state). If this file drifts from reality (a session hits a documented-as-working endpoint that fails), fixing THIS FILE is part of the fix.
