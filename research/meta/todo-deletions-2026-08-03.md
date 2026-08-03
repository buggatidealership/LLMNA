# Backlog triage — 17 deletions, operator-authorized 2026-08-03

**Authorization:** operator, verbatim — *"authorized deletion for the ones you suggested deletion for"*, against the Group A + Group C proposal presented the same turn. Group B (4 items) was RESCUED and re-dated, not deleted. Group D (2 items) awaits an operator decision and was left untouched.

**Why a receipt exists at all:** Rule #19 governs destructive change, and a 17-item removal is recoverable from git but not *legible* from git — the diff shows deletions, not the reasoning. This file is the reasoning.

## Group A — stale deep-dive queue (12)

Queued 2026-05-31 -> 2026-06-05, i.e. **before the July regime break**. Every one was surfaced under a demand-scarcity framing that has since been repriced: we now hold that capex dollars have decoupled from capex units, that there is no AI margin premium at the component layer (MPWR: AI mix +17.1pt -> gross margin +0.1pt), and that profit is concentrating into memory (Samsung DS = 99.7% of group OP). Researching these now would spend real budget on a two-month-old view of the world. **If any still matters it will resurface on merit — that is what the watchlist is for.**

- - [ ] **P2 / research / 2026-05-31** [INDP, AF, POS] — Deep dive: Synaptics (SYNA) edge AI candidate — Astra SR80 + Google Coral NPU
- - [ ] **P2 / research / 2026-05-31** [INDP, AF, POS] — Deep dive: Camtek (CAMT) HBM + advanced packaging inspection candidate
- - [ ] **P2 / research / 2026-05-31** [INDP, AF, POS] — Deep dive: Lattice Semiconductor (LSCC) REFRESH from May 27 thesis
- - [ ] **P2 / research / 2026-06-02** [INDP, AF, POS] — Mitsui Mining (5706.T) entry-trigger watch
- - [ ] **P2 / research / 2026-06-02** [INDP, AF, POS] — Furukawa Electric (5801.T) HVLP4 thesis
- - [ ] **P2 / research / 2026-06-02** [INDP, AF, POS] — Deep-dive: Advantest (6857.T) + Teradyne (TER) — SoC test duopoly
- - [ ] **P2 / research / 2026-06-02** [INDP, AF, POS] — Deep-dive: Alphawave Semi (AWE.L) — SerDes IP at high-speed interconnect layer + M&A status ver
- - [ ] **P2 / research / 2026-06-04** [INDP, AF, POS] — Deep-dive: Seagate (STX) + Western Digital (WDC) — NAND-supply-constraint bypass plays at HDD c
- - [ ] **P2 / research / 2026-06-04** [INDP, AF, POS] — Deep-dive: Pure Storage (PSTG) — AI-storage software bypass play
- - [ ] **P2 / research / 2026-06-05** [INDP, AF, POS, BOT] — Deep dive: BE Semiconductor Industries (BESI) — hybrid bonding equipment for 3D-stacked DR
- - [ ] **P2 / research / 2026-06-05** [INDP, AF, POS] — Deep dive: Nova Measuring (NVMI) — Israeli twin to Camtek
- - [ ] **P2 / research / 2026-06-05** [INDP, AF, POS] — Deep dive: Onto Innovation (ONTO) — architecture-of-tomorrow CAMT competitor

## Group C — superseded (5)

- **Both wiki primers (74d):** a hyperscaler-capex primer written today would teach the wrong thing — we have since established that the capex LINE is a broken measure (MSFT held capex flat while adding $132.5bn of lease commitments). Geopolitical primer: never started, no pull.
- **China sovereignty TRACE backfill (59d):** backfill of a two-month-old event.
- **Hidden-AI-apps standing items (32d):** the run COMPLETED and its falsifier FIRED. Residue only.
- **Oblivious-layer standing items (32d):** run COMPLETED 2026-07-02. Residue only.

- - [ ] **P3 / wiki / 2026-05-21** [INFRA] — Hyperscaler capex primer
- - [ ] **P3 / wiki / 2026-05-21** [INFRA] — Geopolitical AI primer
- - [ ] **P2 / research / 2026-06-05** [INDP] — Back-fill China sovereignty cluster TRACE event (verification catch 2026-05-28)
- - [ ] **P2 / research / 2026-07-02** [INDP, AF, DISC] — HIDDEN-AI-APPS post-run-#1 standing items (run COMPLETE, falsifier FIRED — see `signals/cross-
- - [ ] **P2 / research / 2026-07-02** [INDP, AF, BOT, DISC] — OBLIVIOUS-LAYER PROGRAM standing items post-run-#1 (run COMPLETE 2026-07-02, 10 agents): 

## What this does NOT fix

Deleting 17 items does not make the remaining dates mean anything. The structural finding from the 2026-08-02 supervisor build stands: **a 70%-late queue is a wish-list wearing a schedule's clothes**, and the durable fix is a forcing function (auto-delete past N days unless explicitly renewed, converting silence from "still open" into "dropped"), not a periodic manual purge. That remains the operator's call — `meta/redteam/2026-08-02-supervisor-loop-design.md` §7.

## Reconciliation — and a finding the count itself surfaced

| | |
|---|---|
| open before | **96** |
| deleted (Groups A + C, authorized) | **17** |
| rescued + re-dated (Group B) | **4** (headers replaced, items kept) |
| **open after** | **79** |
| past their date | 44 (59%) — down from 71% |
| stale >30d | **2** — down from 23 |

**The finding: 5 of the 79 open items are INVISIBLE to the parser that surfaces overdue work.**
Reconciling a loose header match (79) against the documented template (74) exposed five items
whose date field is not a date:

- `**P2 / harness / 2026-07-24→CARRIED**`
- `**P2 / research / open**`
- `**P1 / USER-ACTION / 2026-07-13**` (non-standard category)
- `**P1 / research / 2026-Q4**`
- `**P2 / research / 2026-06-25→2026-07-04**`

The session-start hook sorts and surfaces by parsed date. **An item with `open` or `2026-Q4` in
that field can never be flagged overdue, no matter how long it sits.** They are not lost — they
are unreachable by the only mechanism that would ever remind us of them.

**This is L53's class applied to the queue itself**: a correct entry, filed in a form nothing reads,
is functionally invisible. It was found only because a delete pass forced two independent counts of
the same file to be reconciled — the same way the 25-year/3-year credit percentile was found only
because an impossible maximum forced a second look. **Counting the same thing two ways is cheap and
keeps working.**
