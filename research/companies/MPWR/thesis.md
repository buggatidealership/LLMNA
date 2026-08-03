# MPWR (Monolithic Power Systems) — Thesis

**Last updated:** 2026-07-31
**Tier:** Watchlist
**Position target:** 0% (no entry)
**Anti-fragility:** 3/5 scenarios (preliminary — see below)

## TL;DR

The company that designed Vicor out of the H100 is now a **datacenter power company wearing an analog-diversified costume**: 38.8% of revenue and **93.1% of all YoY growth** is AI. It just printed a record quarter, raised its full-year AI growth *floor* from 85% to 130% mid-year on **lean channel inventory**, and committed its own capacity beyond $6B. It is on the watchlist as an **instrument** first — the cleanest per-socket read the harness has on whether hyperscaler capex is landing as units — and as a position candidate second.

## Why the folder exists (first ingest, 2026-07-31)

Mentioned in 11 corpus files since May 2026 and **never given a folder**, because every prior filing was peripheral (VICR's competitor / laptop PMIC / T9 consumer AI swap / IVR substitution *risk* to MURATA). The Q2'26 print re-bases it: this is a datacenter power name. Full analysis: `signals/cross-source-log/2026-07-31-fri-mpwr-recipient-side-capex-landing-test.md`.

## The Q2'26 print (T1, [SEC 8-K Ex-99.1](https://www.sec.gov/Archives/edgar/data/1280452/000162828026051029/mpwr-20260630xexx991.htm))

- Revenue **$980.6M** (+21.9% QoQ, +47.6% YoY) — record
- Enterprise Data **$380.6M** (+44.8% QoQ, **+164.3% YoY**), 38.8% of revenue
- Non-GAAP GM **55.6%**, non-GAAP EPS **$6.50**
- Q3 guide **$1,140–1,160M** (midpoint +17.3% QoQ)
- Days of inventory **140** (−17 QoQ); forward DOI **121** (−7); DSO **32** (−2)
- FY Enterprise Data growth floor raised **85% → 130%** (T2, call)
- Buyback authorization +$500M → $1B; capacity goal extended "significantly beyond $6B"

## Bull case (P=45%)

- Per-socket exposure to AI rack power with **content-per-system rising** as rack density rises (800V HVDC architecture: MPS is *already sampling* High Voltage AC-DC products, T1)
- Channel is lean, not stuffed — the balance sheet corroborates the demand claim on three independent axes (DOI trailing, DOI forward, DSO)
- SAM expansion in flight: initial DDR5 high-speed memory-component orders = a new socket class
- Self-funded capacity ahead of run-rate (~$6B goal vs ~$4.6B annualised) while simultaneously doubling the buyback — no capital-structure ask
- Expected return: +30–50% over 12–24 months **if** end-market growth (not share) is the driver

## Bear case (P=30%)

- **No AI gross-margin premium exists.** AI mix +17.1pt YoY moved gross margin +0.1pt. The buyer captures the component-layer surplus; MPS is a volume play, not a pricing play. Multiple compression risk is real at ~$1,426.
- **Share-gain confound:** an unknown and possibly large fraction of +164% is sockets taken from TI/ADI/Infineon, not market growth. Share gain is finite by construction; market growth is not.
- **Customer concentration undisclosed** in the 8-K. If Enterprise Data is one hyperscaler, the whole read narrows.
- The 800V architecture MPS is sampling into **reduces conversion stages per server** — the same architectural bypass that threatens discrete PMIC stacks can, at the limit, compress MPS's own content per box.
- Expected loss: −35–45% in an AI-capex digestion quarter, from a position of no valuation support

## Base case (P=25%)

Growth decelerates from +164% to a still-strong double-digit-to-50% range through 2027 as share gain saturates and end-market growth normalises; margin stays pinned at ~55.5%; the stock compounds with earnings but re-rates down.

## Falsifiers (mandatory)

1. **Enterprise Data growth falls below +130% YoY at the Q3'26 print (late Oct)** while forward days-of-inventory rises above 128 — that combination is channel congestion, and it would break the "capex is landing as units" read this folder exists to test. *(Instrument-validity checked: both quantities are disclosed quarterly at T1 by this issuer — this falsifier can actually fire, unlike the capex-cut falsifier retired in `meta/hyperscaler-reward-function-v2.md` §9.)*
2. **Non-GAAP gross margin falls below 54.5%** — would mean the buyer is now extracting surplus, not just capping it, and the volume thesis loses its earnings translation.
3. **A 10-Q reveals >40% of Enterprise Data revenue from a single customer** — the read-across value of this name as a market instrument collapses, and so does the bull case's diversification premise.

## Exposure to causal chains

- **T9 Consumer Hardware AI Swap** — **DEMOTED to secondary** as of 2026-07-31. Consumer is 5.8% of revenue and **−4.8% YoY**. The original 2026-06-06 filing rationale (AI-PC NPU power profile) is no longer the business.
- **Datacenter power / 800V HVDC cascade** (`signals/cross-source-log/2026-06-25-pm-integrated-synthesis-round6-trendforce-800v-hvdc-power-cascade.md`) — **PRIMARY drawer.** MPS is the named IVR substitution vector against both the MLCC count (MURATA) and discrete PMIC stacks.
- **Recipient/payer taxonomy** (`signals/events/2026-07-31-ai-complex-deleveraging-size-tested.md`) — **RECIPIENT.** Receives capex; carries no leverage exposure to the payer side.
- **VICR** — structural competitor; MPS has won the current generation (`companies/VICR/thesis.md`).
- **MURATA (held)** — MPS is the substitution risk to MLCC count per server via integrated voltage regulation; 800V AC-DC now *sampling*, revenue 2027-28.

## Position implication (Critical Rule #11)

**Position implication:** **NO ACTION — no entry — WATCHLIST retained with the drawer re-based from T9-consumer to datacenter-power.** Three gates: (a) the 07-31 tape faded 56% of the peak gain on a record beat, which is a poor entry regime for confirmed proof; (b) the share-gain-vs-end-market ambiguity is the whole thesis and is unresolved from this print; (c) no capacity in the book against the €160k reserve floor and the existing cohort. **Re-eval trigger: Q3'26 print (late Oct)** — falsifier #1 is the test.

## 🟡 2026-08-03 (Mon) T+2 — the entire print reaction is gone

Back-reference: `signals/cross-source-log/2026-08-03-mon-eod-kr-us-decoupling-12pp.md` §4.

| | |
|---|---|
| Pre-print close 07-30 | $1,316.18 |
| Print reaction 07-31 | $1,426.03 (+8.35%), intraday peak $1,568.21 (+19.15%) |
| **Close 08-03** | **$1,344.37 (−5.73%)** |
| **Cumulative vs pre-print** | **+2.14%** — **0.1% of the peak gain retained** |

A record quarter, a full-year Enterprise Data growth **floor raised 85%→130%**, and a doubled buyback — **effectively the entire move surrendered in two sessions**, on a day when the US AI complex was broadly *up* (QQQ +1.76%, NVDA +2.93%, SNDK +6.03%). So this is not tape-wide risk-off; it is name-specific give-back.

**This strengthens the 07-31 read rather than weakening it.** That artifact called the fade *"the highest-proof / lowest-ask cell we have observed this cycle"* and read it as a statement about the marginal buyer's price rather than the fundamental. Two more sessions of give-back against a rising cohort is further evidence for exactly that: **confirmed proof is not being paid for at these levels.**

**No falsifier is touched.** All three registered falsifiers key to the Q3'26 print — Enterprise Data growth ≥130%, forward days-of-inventory ≤125, non-GAAP gross margin ≥54.5%, and the 10-Q customer-concentration disclosure. **A price move touches none of them**, which is by construction: they were written to be instrument-valid against reported quantities, not against the tape.

**Position implication:** **NO ACTION — no entry — WATCHLIST unchanged.** The gate was never price; it is the unresolved share-gain-versus-end-market ambiguity (H-C 40%), and a cheaper entry does not resolve it. Re-eval stays the Q3'26 print. 🟡
