# FLOWS/POSITIONING ACQUISITION PLAN (2026-07-17, user directive: "what APIs optimize for the winning of the harness — state your definition of winning first")

## Definition of winning (stated before acting; the evaluation criterion for every row below)
Winning = **the calibration ledger compounding faster than the market prices the same insights**: (1) pre-registered calls whose graded hit-rate at claimed P-bands beats chance AND beats consensus (edge-vs-street per print); (2) converted into position decisions ahead of the price move, inside the envelope (no leverage; reserve floor; survivable drawdowns — compounding never interrupted); (3) error rates falling (user-caught + INPUT-layer failures declining monthly); (4) per unit of cost — token/euro spend must show measured yield in the cost-yield ledger. **A data source optimizes winning ONLY if it feeds a pre-registered tell that can change a graded call or a position decision.** Data that cannot change a decision is decoration.

## Why flows specifically (the gap this closes)
The Jul-17 regime-read pre-registration names the H1-kill signature: *margin balance shrinking while selling continues = informed selling, not forced*. Adjudicating that requires knowing WHO is selling — the exact dataset the registry lists as gap #1. Every row below is scored against the live tells it would feed: KOFIA H1/H2 discriminator, Jul-29 SKHY window, Jul-22 twin print, TC-18 falsifier watch, value-migration screen.

## The map (tested from this container 2026-07-17 — Verified column is empirical, not catalog)

| Source | Layer | Cadence | Cost | Verified today | Feeds which tell | Verdict |
|---|---|---|---|---|---|---|
| **TWSE T86 per-stock 三大法人 flows** | MICRO — daily foreign/institutional net buy per TW stock (2330/2408/3532/2383) | daily T+0 evening | FREE keyless | ✅ LIVE — `twse_client.t86_institutional()` built+tested; first datum: Jul-16 foreign net-sold all 4 tracked names (Nanya −21,931,962 sh) | TW memory-complex positioning; TC-18 demand-vs-flows cross-check | **WIRED TODAY** |
| **CFTC COT (incl. TFF disaggregation)** | MACRO — weekly futures positioning: NASDAQ-100/S&P leveraged-fund + asset-manager net | weekly (Fri, T+3) | FREE | ✅ LIVE — deafut.txt fetched, NASDAQ-100 rows parsed | The H2 "informed selling" adjudicator at index level: leveraged-fund net-length trend | **WIRE next wake** (fetch helper, trivial) |
| **JPX investor-type weekly + margin balance (信用残)** | MACRO/MESO — who bought/sold Tokyo (foreigners vs individuals) + JP margin stock | weekly (~Thu, T+4) | FREE | ✅ page reachable, 11 file links (xls) | Murata/SUMCO market-level flow attribution; JP margin = the KOFIA-equivalent for the JP book | **WIRE** (xls parse; weekly pull) |
| **KRX investor-type daily (foreign net buy per stock)** | MICRO — the SKHY-critical one | daily | FREE (portal 403s containers; official Open-API needs KR signup, or press-relay T2) | ❌ data.krx.co.kr 403 (expected) | Jul-20 reopen + Jul-29 window: is foreign money exiting or absorbing? | **USER ACTION option:** KRX Open-API signup (Korean forms, like DART) — else stays agent-fetched T2 from 연합인포맥스-class relays (workable, dated) |
| **KOFIA 신용융자/반대매매** | MESO — KR margin + forced sales (the #1 discriminator) | daily T+1/T+2 | FREE (portal walls agents) | prior artifacts; Jul-13 freshest | H1/H2 kill-signature direct | ECOS key (already queued, user) covers adjacent credit series; portal stays agent-bridged |
| FINRA short interest + Reg SHO daily files | MICRO US | bi-monthly / daily | FREE | not yet | US satellites (MU/NOW/IBM watch names) | wire at first US-name entry package |
| Nasdaq RTAT retail tracker (free tier) | MICRO US retail | daily T+1 | FREE (key signup) | not yet | retail-vs-institutional split on US names | low priority — book is Asia-heavy |
| ICI weekly fund flows + AAII + NAAIM | MACRO US sentiment/flows | weekly | FREE | not yet | regime overlay only | wire as monthly context pull, not a tell |
| 13F via edgar_client | MACRO/MICRO institutional | quarterly, 45d lag | FREE (built) | ✅ (client live) | Q2 season ~mid-Aug: who added/cut memory complex | already owned — schedule the Aug sweep |
| — PAID — | | | | | | |
| EPFR / Vanda (fund + retail flows) | MACRO gold standard | daily/weekly | institutional-priced (recall-based, way out of range) | — | — | **SKIP** — cost kills the cost-yield test |
| Ortex (short interest est.) | MICRO US | intraday | ~$50-100/mo (recall-based — verify if pursued) | — | US shorts | **DEFER** — Asia-heavy book, low yield now |
| SpotGamma / Unusual Whales (options/GEX) | MESO US day-level | daily | ~$50-150/mo (recall-based) | — | day-level swing mechanics | **DEFER, evidence-gated:** buy only after a graded miss where options-positioning would demonstrably have changed a call (that receipt doesn't exist yet); horizon mismatch with 6-24mo book |
| WhaleWisdom (13F aggregation) | convenience | quarterly | ~$500/yr (recall-based) | — | — | **SKIP** — redundant with our free EDGAR parse |
| EODHD paid tier (Tokyo singles) | tape, not flows | daily | ~$20-50/mo class (recall-based) | — | Murata/SUMCO exact closes (recurring conflict, again today) | flagged separately — tape gap, different track |
| TrendForce/DRAMeXchange | PRICING, not flows | daily/weekly | paid | — | memory contract/spot = the book's core variable | **still the #1 paid candidate overall** (registry, unchanged) — if ONE paid subscription ever happens, it's this, not a flows product |

## The holistic answer (macro + micro, one paragraph)
The flows gap is a **wiring problem, not a money problem**, because this book is Asian-listed and Asian exchanges publish daily investor-type flows OFFICIALLY and FREE — the opposite of the US, where flows are the paid layer. Concretely: TW micro flows are live as of today; index-level US leverage (COT) and JP weekly attribution are free wires away; the two KR sources (KRX investor-type, KOFIA margin) are the only ones needing either a Korean signup or the standing agent bridge. Paid flows products all fail the winning test today: either priced out (EPFR), redundant (WhaleWisdom), or aimed at a day-trading horizon we don't trade (GEX) — deferred behind an evidence gate, not rejected forever. Paid budget, if any, still belongs to memory PRICING (TrendForce) — the variable our core thesis actually runs on.

## Falsifier / re-eval (like everything)
If 30 days of wired flow data feeds zero graded calls and zero position decisions (check at the Aug-17 audit): the wiring was decoration — trim to the KOFIA discriminator alone. If a graded miss shows a paid source (GEX/Ortex) would have flipped the call: the evidence gate opens, buy it.
