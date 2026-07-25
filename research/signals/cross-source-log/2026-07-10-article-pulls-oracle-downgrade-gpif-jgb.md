# 2026-07-10 — ARTICLE-PULL DELIVERY (good-morning wake #1, Leg C upgrade pass)

**Channel:** user WSJ subscription, article-body screenshots (6) delivered ~08:5x UTC in response to the two ranked pull requests from the wake-#1 synthesis. Per `meta/good-morning-protocol.md` §Leg C: article bodies upgrade items from T2-headline-layer → **T1 publisher for facts stated in the body**. FACT/FRAME/OPINION separation applied per §Human-authorship discipline. Rule #16 verifiers fired (2× Opus, parallel): Oracle-downgrade corroboration + GPIF/JGB corroboration w/ native-JP search. Verdicts appended below on return.

---

## PULL 1 — "Oracle Gets Credit Rating Downgrade" (WSJ, Sam Goldfarb, 2026-07-09 22:10 ET)

### FACTS (T1 WSJ article body)
- **S&P Global Ratings downgraded Oracle BBB → BBB− on Thursday 2026-07-09** — one notch above speculative grade. AGENCY=S&P; NOTCHES=1; now at the IG floor.
- **Stated reason is EXPLICITLY AI capex:** Oracle's "growing AI infrastructure business is diluting its strong business risk profile"; S&P had "underestimated the scale of the investments required to expand the AI business and its impact on our overall view of Oracle's creditworthiness."
- Credit transmission (modest): spread on Oracle 5.7% 2036 bonds 1.75pp (Wed) → 1.84pp (per MarketAxess) = **+9bp**.
- Equity transmission (near-nil): ORCL +2.7% to $144.22 on the day; slipped from ~$146 intraday post-announcement — the downgrade cost ~1.2% intraday and the stock still closed up.

### FRAME (author's, not booked)
"Inching closer to 'junk' territory" — a trajectory frame. The FACT is one notch above IG floor; whether junk is the path depends on the OUTLOOK (not stated in the visible body — verifier assigned).

### Routing
- **`sector/ai-funding-shock-node.md`** — this is the node's first RATING-AGENCY canary: an IG major downgraded WITH AI capex as the stated cause. Distinct from the neocloud canary basket (CoreWeave/NBIS class) — this is the HYPERSCALER-tier affordability leg showing up in an agency action. Cascaded same commit (new tell + canary row).
- Weekend deep-work item #1 (funding-shock) now has a live datum, not just framework.
- **Muted-transmission read (my model):** +9bp spread / equity up on the day = the market treats BBB− as priced; the node does NOT fire on this alone — it fires if (a) outlook negative + second agency follows, or (b) spreads widen through the ~130bp+ regime already logged in bottlenecks.

## PULL 2 — "Japan Wants GPIF to Boost Domestic Investments" (WSJ, Ronnie Harui, 2026-07-10 02:32 ET)

### FACTS (T1 WSJ article body)
- FM Katayama, Friday: "We are looking to pursue measures to encourage pension funds, including the GPIF, to make further investments in Japanese financial assets." GPIF ≈ **$1.8T AUM**.
- Market reaction (Tokyo Jul-10): **USD/JPY 161.57** (from 162.38 late Thu NY, yen +0.5%); JGB **5Y −4.5bp → 1.985%; 10Y −11bp → 2.77%; 40Y −8.5bp → 3.950%**; **Nikkei +1.4% → 68,695.73**.
- Intervention context: market intervention-watch level ~**¥163**; Japan FX reserves >**$1T**.

### FRAME / OPINION (labeled, not booked)
- Masahiko Loo (State Street, named strategist = T2 opinion): remarks "constructive for both JGBs and the yen over the medium to long term"; "smart policy signal" given questions about MOF's remaining FX-intervention firepower; encouraging domestic capital home = "more durable and structural way to support the yen" than intervention. → Logged as analyst-grade color for the module's transmission map, NOT as a triangulated read.
- Note the FRAME: the headline says "Japan Wants GPIF to Boost Domestic Investments" — the FACT layer is one minister's statement of intent ("looking to pursue measures"). JAWBONING vs MECHANISM distinction assigned to the verifier: no legal mechanism, allocation target, or date appears in the body.

### Routing
- **`sector/jgb-yen-sensitivity-module.md` — BUILT v1 this commit** (top register priority, recurrence 3, CLASS-1 auto-resolve grant). Article body supplies the seed levels + the policy-lever taxonomy.
- `meta/absence-question-register.md` JGB row → status BUILT (monitoring continues inside the module).
- Both held theses already carry the Jul-10 yen-flip cross-ref from wake #1 — no new thesis delta from the body beyond harder numbers (10Y −11bp vs the −10bp booked from the tape scan; module carries the exact figure).

## BONUS — WSJ market wrap screenshot (Caitlin McCabe + Corrie Driebusch, 2026-07-09 EOD)
- **SK Hynix ADR $149 / $26.5bn** ("people familiar") — independent T1-publisher confirmation of yesterday's CONFIRMED-FINAL grade. No delta.
- PHLX Semi +3.1% Thursday, led by ARM/Micron/Marvell — "investors revive AI trade."
- Geopolitics (complement channel): US-Iran exchanged fire, US struck 90 military targets, Trump says Iran "seeking a deal"; oil slipped; 10Y UST broke a 7-day rising-yield streak. → day-state context line; no thesis routing (non-AI, but rates-relevant as risk-appetite backdrop).

---

## Rule #16 verifier verdicts (appended on return)

### Oracle/S&P verifier — RETURNED (Opus, ~23.6k, 15 tool uses). Yield: HIGH (framing catch).
- **Downgrade CONFIRMED-FRESH T1:** S&P Research Update "Oracle Corp. Downgraded To 'BBB-'" (spglobal.com id 3592347), Jul-9; long-term BBB→BBB−, short-term A-2→A-3. Independently echoed same-day (Investing.com/Yahoo, HNGN, AInvest).
- **⚠️ FRAMING CATCH — OUTLOOK = STABLE.** S&P went BBB/negative → BBB−/STABLE: the negative-outlook overhang RESOLVED into the notch cut. **Junk is NOT S&P's base path** — the WSJ "inching closer to junk" frame overstates trajectory. (S&P retains a could-cut-if-leverage-stays-elevated caveat.)
- **ONE-AGENCY EVENT, not a trend:** Moody's Baa2/NEGATIVE and Fitch BBB/stable — both one notch ABOVE S&P's new level, neither moved Jul-9. **Next domino = Moody's** (negative outlook): a Baa3 cut converts event → trend.
- **Hard credit numbers CONFIRMED T1 (via S&P):** total debt ~$160B; FY27 capex revised $60B → $90-95B; FY27 FOCF ~−$42B (was −$24B); adjusted leverage mid-4x FY27; **OpenAI ≈ half of remaining performance obligations, named a "key credit risk"; Oracle plans a $20B equity issuance this year to defend the rating.**
- Single-source (WSJ-only, do not book as confirmed): the 1.84/1.75pp MarketAxess spread figures; exact $144.22/$146 prints (+2.7% day move IS corroborated). "First AI-capex IG downgrade" superlative: NOT FOUND anywhere — never repeat as fact.
- Context on file elsewhere: hyperscaler IG-index weight ~doubled 2.2%→4.1% YoY to Apr-2026; no Jul-9-specific spillover into other AI issuers' spreads found.

### GPIF/JGB verifier — RETURNED (Opus, ~31.1k, 22 tool uses, native-JP parallel executed). Yield: HIGH (2 framing catches).
- **Katayama remarks CONFIRMED-FRESH T1** (Nikkei/Bloomberg JP/Reuters/Asahi, all Jul-10): forum = post-cabinet-meeting press conference (閣議後会見); JP verbatim matches WSJ translation; GPIF ¥293.4T ≈ $1.8T; current allocation domestic bonds 26.91% / foreign bonds 24.48% / domestic equity 23.81% / foreign equity 24.80% (Mar-end). Katayama also reaffirmed BOJ independence — WSJ omits.
- **Levels: USD/JPY CONFIRMED** (161.57 valid mid-session snapshot; intraday strongest ~161.29; prior NY ~162.40); **10Y CONFIRMED** (T1 −10bp → 2.775%, steepest one-day drop in a month; WSJ −11bp/2.77% = rounding); **Nikkei CONFIRMED** (close ~68,700 +1.5%, intraday +2%/69,300); 5Y 1.985% / 40Y 3.950% = PARTIAL (direction confirmed curve-wide, exact levels not independently pinned; JBTS 403-blocked). 40Y context: recently printed first-ever >4% — 3.95% = back below. NOTE: English T1 gave 20Y −11.5bp to 3.75% — different tenor, do not conflate.
- **⚠️ FRAMING CATCH 1 — JAWBONING, NO MECHANISM:** GPIF sits under **MHLW, not MOF**; allocation changes require a formal slow review; no legal instrument, no timeline, no target number; no GPIF response yet. Bloomberg JP: market "skeptical about sustainability" (「市場は持続性に懐疑的」). Do NOT model a GPIF domestic reweighting as a dated catalyst.
- **⚠️ FRAMING CATCH 2 — RETRACEMENT, NOT CLEAN RALLY:** Japanese T1 frames the remark as damage-control (財務相「火消し」) after a **骨太-方針 (economic-blueprint) JGB selloff** that stoked BOJ-independence/fiscal fears — Friday's bond rally is materially a retracement of that shock, not a standalone structural bond bull. Nikkei invokes a 2020 jawboning precedent. WSJ presents the move as pure GPIF reaction — incomplete frame.
- **Intervention corroborated:** Loo verbatim confirmed; zone refined to **163 break → stop-driven momentum toward 165**; intervention now "driven by speed and disorder rather than a fixed level." MOF reserves $1.31-1.37T (T1) after record ¥11.7T spent.
- Native URLs in verifier output (Nikkei ×3, Bloomberg JP ×3, Bloomberg EN, Reuters/Newsweek JP, Asahi, Japan Times, MOF, GPIF).

**Ledger:** 2 verifier fires this batch (Opus ×2, ~54.7k combined), both HIGH — 3 framing catches total (Oracle outlook-stable; GPIF jawboning-not-mechanism; GPIF retracement-context). Human-authorship discipline empirical count continues to earn its keep: both article bodies were factually accurate but FRAME-incomplete in the trajectory/causality layer.
