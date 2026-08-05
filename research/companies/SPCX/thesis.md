# SPCX (SpaceX, Nasdaq) — Thesis STUB

**Created:** 2026-08-05
**Tier:** Watchlist — **no thesis yet.** This file exists to end a filing defect, not to state a view.
**Position target:** 0% — not held, no entry package.
**Anti-fragility:** not scored.

## 🔴 Why this file was created: a retrieval failure, not a knowledge gap

On 2026-08-05 the operator shared WSJ headlines showing SpaceX reporting quarterly results and its shares falling. **I told him "my corpus has SpaceX as private." That was wrong.** The corpus knew, in two places:

- `meta/private-tracker.md` — *"SpaceX IPO June 12"* and *"SpaceX IPO'd Jun-12"*
- `meta/private-tracker.md` § `xAI → SpaceXAI` — a **2026-07-14 STATE REPAIR** block headed *"house record was STALE — entity is PUBLIC,"* naming **ticker SPCX**, the $135 offer, and the day-one tape

**A repair entry written three weeks ago, explicitly flagging this exact staleness, did not retrieve when the identical question arrived.** This is **L53 (retrieval-drawer)** — a fact that is filed but not indexed against incoming content is functionally not filed. It is the same failure as B40 catch #9, where a catch already in `biases-watchlist.md` failed to retrieve against a byte-identical headline.

**The structural defect:** a listed equity of ~$1.3-1.65tn was being tracked in the **privates ledger**, the one file no reader consults for a public company, while `companies/` held 100+ folders and not this one. **Fixed by this file's existence.**

## Facts on the record (2026-08-05, commissioned Opus verification, Critical Rule #16)

| | | Tier |
|---|---|---|
| Ticker / exchange | **SPCX / Nasdaq** | T1-indexed (EDGAR CIK 0001181412) |
| Listing | traditional IPO **2026-06-12** — not a direct listing, not a SPAC | T2 |
| Offer price | **$135.00** | T2 |
| Peak | **$225.64, 2026-06-16** | T3 |
| Structure | **xAI absorbed pre-IPO** (all-stock, announced 2026-02-02); rebranded "SpaceXAI" 2026-07-06. The listed entity carries Grok, X, the launch business and the compute/orbital-DC business | T1/T2 |

**Q2 2026 — first report as a public company (2026-08-04 AMC, call 16:30 ET):**

| | |
|---|---|
| Revenue | **$7.81bn (+92% YoY)** — AI $2.561bn (+247%) · Connectivity/Starlink $4.291bn (+66%) · Space $0.962bn (+29%) |
| Net loss | **$541m**, narrowed 46% from $1.008bn |
| **Total capex** | **$18.37bn**, >6× YoY, against ~$13.22bn expected — **a 39% overshoot** |
| **of which AI capex** | **$15.83bn** = **86.2%** of total capex |

**Computed here, stated by no source:** AI capex **6.2× the AI segment's own revenue**; total capex **2.35×** total revenue; AI capex **+105% sequential** (Q1 $7.723bn → Q2 $15.83bn) — **it doubled in one quarter**; H1-2026 AI capex **$23.55bn**.

🔴 **THE $15.8bn IS CAPITALISED, NOT EXPENSED.** The company's own line item is *"AI capital expenditures."* WSJ's "spent $15.8 billion on AI projects" is accurate as to period and amount but obscures that it lands on the balance sheet and reaches earnings through future D&A — **not in the $541m Q2 loss.** For any FCF or EPS bridge that distinction is the whole exercise.

## Open contradictions — flagged, NOT averaged

| Item | Conflict |
|---|---|
| **Amount raised / valuation** | Corpus (07-14, from SEC S-1 + pricing PDF): **~$86bn raised, ~$2.1tn day-one cap, "largest IPO in history."** 2026-08-05 verification: **~$75bn raised, ~$1.75tn implied.** Both cite primary sources. **UNRESOLVED — do not use either as a point estimate.** |
| **Shares outstanding / market cap** | Reported caps ($1.64tn, $1.651tn) do not reconcile with $1.75tn ÷ $135 ≈ 12.96bn shares. **Market cap carried as a BAND: ~$1.3-1.65tn.** |
| **Aggregator arithmetic** | "911.5m unlocking shares = 12% of total" — 911.5m ÷ 12.96bn is **7.0%**. T3 error. "~30% below IPO price" — actual **~12-15%**. ">50% off the high" — actual **~49%**. All three refuted by recomputation. |
| **"$1 trillion revenue"** | 🔴 **B40 STALE-RECYCLE.** The $1tn target was **already in the IPO prospectus (June 2026)**. The 08-04 news is a **pull-forward, 2031 → 2030**, with a hedged *"non-zero chance"* of 2029. WSJ presented a prospectus-vintage aspiration as fresh guidance and stripped both the year and the conditionality. **Management aspiration, not guidance.** Sell-side 2030: Goldman ~$470bn, Morgan Stanley ~$330bn — management's number is **~2.1× and ~3.0×** those. |

## Why this name matters to the harness even unheld

**A new gigawatt-class AI-capex buyer now exists OUTSIDE the hyperscaler set, and it discloses quarterly.** Every demand model in this corpus concentrates AI capex in ~5 named buyers. A sixth spending **$15.83bn a quarter and doubling sequentially** changes the shape of that model — and unlike OpenAI or Anthropic, **it files.** That is a new observable feed for the AI-funding-shock node and for every memory/accelerator demand read.

**Adjacency already live:** on the same call, President Shotwell said *"I anticipate us to be able to acquire quite a few of their customers because I think our service will be better."* VZ **−3.6%**, T **−2.7%**, TMUS **−2.4%** after hours.

## What is NOT established

- **No thesis.** No bull/bear/base, no P-weights, no anti-fragility score, no falsifiers. Writing them off one quarter and a stale corpus entry would be false precision.
- **No memory/HBM read-through** from this data.
- **08-06 lockup expiry (~911.5m insider shares, larger than the ~640m float)** is **forward risk, not a fact about the past.** Do not cascade it as an outcome. It is logged as an in-window market-structure event for the SNDK T+1 grade.
- Exact 08-04 and 08-05 closes: **UNPINNED.** Sources gave $108.37 / $114.53 / $118.14 / $125.33 / $135.27 — mutually irreconcilable. Confidence band only: **08-05 move −8% to −11%, price ~$100-115, below the $135 offer.**

## Falsifiers

None registered — **a thesis stub cannot carry falsifiers, and pretending otherwise is the failure Principle #51 exists to prevent.** The first real detector will be written when this file gets a view.

**Position implication: NO ACTION — 0% — not held; Watchlist, pre-thesis.** 🟡 The work owed is a proper thesis build, which requires reading the 10-Q (period 2026-06-30, EDGAR) directly — blocked this session by proxy 403 on sec.gov.
