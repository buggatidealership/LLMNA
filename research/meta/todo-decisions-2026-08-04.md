# Operator decisions — five gated to-do items, 2026-08-04

**Origin:** operator asked *"any items on the to do that can be deleted or need my input?"*, then *"let's go through them one by one, expand them in layman terms, and then we make decisions."* Five items were expanded and put to him. All five decided in one pass. Receipt for the 17 authorized deletions the day before: `meta/todo-deletions-2026-08-03.md`.

---

## The decisions

| # | Item | Age when decided | Decision |
|---|---|---|---|
| 1 | P0 quota-instrument forced binary | 7d overdue, measured 3× | **Branch (a) — fix the plumbing** |
| 2 | Workflow #11 autonomous day-loop | 33d stale, dead 26d | **Delete (superseded)** |
| 3 | Weekly competitive surveillance | user-gated 13d | **Go weekly** |
| 4 | DeGiro/N26 availability check | 22d | **Delete (superseded)** |
| 5 | P0 "DEEP-DIVE DEFERRALS + K3 REWORK" | 11d overdue | **Split** (no objection) |

---

## Two findings that changed two of the decisions

Both were computed while preparing the expansions. Neither had been noticed in the weeks the items sat open, and neither would have surfaced without someone asking for the items in plain terms.

### 1. The surveillance item's cost objection was arithmetically wrong, on its own figures

The item read *"4× cost vs monthly."* That is **4 passes, not 4× spend**:

| | |
|---|---|
| Weekly: 50–80k/week × 4.345 weeks | **217–348k/month** (midpoint ~282k) |
| Current monthly H2 bear-case | **~280k/month** |
| **Ratio** | **1.01× — a wash** |

The decision sat user-gated for 13 days on a cost concern **its own numbers never supported**, while its origin note records two displacement events (MRVL Trainium 3, SNDK MU 245TB ION) that surfaced post-hoc and would have surfaced 3–4 weeks earlier under the weekly cadence. The multiplication was available in the item the entire time.

**Failure class: instrument-validity — a real quantity (cost) measured with the wrong instrument (passes, not spend).** Same shape as every other significant finding this week.

### 2. The DeGiro item reinstated a rule the operator had abolished eight days earlier

`research/CLAUDE.md:42`:

> *"**Investability filter** (added 2026-05-28; **SUPERSEDED 2026-07-05 by user directive**): accessibility is NO LONGER a research gate… surface every name on merit."*

The item is dated **2026-07-13**. Its scope line: *"availability check **gates** whether they're worth a Workflow #9 thesis build."*

**Failure class: L53 (retrieval-drawer), applied to a directive rather than to a name.** The superseding line sits in `CLAUDE.md` and is read at every session start. It was never connected to the item being written, and not once in 22 days of re-reads. **A rule that is read but not indexed against new work is functionally not in force.**

---

## What shipped, per decision

**1 — quota, branch (a).** `predictions/grading-log.md` § "Wake-call registrations `[WAKE]`": convention + first two registrations, booked at booking time with P-provenance. The `[WAKE]` tag is the guard against branch (a)'s known risk (count inflating with low-stakes calls until 150 means nothing) — the quota is reported **both ways**, with and without wake rows, always alongside and never instead. The to-do is re-scoped from *measure the gap* to *measure compliance with the convention* (≥80% by 08-24). Audit entry appended to `meta/recurring-audit-log.md`.

*The first registration already earned it:* the 08-04 KR ETF-divergence call went in tagged **`⚠️ NO P STATED AT BOOKING`** — the wake artifact hedged in prose and never wrote a number. Recorded as-is, not back-filled. **An unfalsifiable hedge reads as caution and grades as nothing.**

**2 — Workflow #11.** To-do closed; `meta/workflow-11-autonomous-day-loop.md` marked **SUPERSEDED in place, not deleted** — it is the record of what was tried and how it failed. Superseded by the scheduled Routines, which are not session-scoped, which is the exact property whose absence killed it.

**3 — surveillance.** Cadence set to weekly, next pass 2026-08-05 then every Wednesday. Cost line corrected in the item itself. Blind-check added (it reads on the announcement channel only — it is blind to a design win disclosed at the customer's print, which is precisely how the MRVL loss surfaced). Kill criterion: 8 consecutive passes with zero Δ the monthly would have missed → revert.

**4 — DeGiro/N26.** To-do closed as superseded. All ~10 names migrated to `watchlist/candidates.md` as the REIA power / electrical-infrastructure cluster, **merit-ranked** with exchange tags as courtesy. The verified-unavailable results (Nanya 2408.TW; CXMT / Naura / AMEC / Piotech; direct KRX) are retained there so nobody re-derives them.

**5 — split.** G-19 cascade-hook changeset-window → its own **P1 dated 08-11** (the only sub-item that is a live hole in an enforcement hook; Rule #19 review-gated). Audit residue + suite RED + exit-path inventory → **P3 dated 09-01**. The K3 Q5 `stop_hook_active` blanket guard was **carved out and kept at P1** rather than downgraded — it is a LIVE-enforcement defect and does not belong in a triage pile.

---

## The thing worth carrying forward

**Three of these five items were not merely stale — they were wrong in a way that reading them would not reveal.** #3 carried arithmetic nobody had done. #4 enforced an abolished rule. #2 described infrastructure that had been dead for 26 days. In every case the item had been re-read many times, surfaced in briefings, and scored by the forced ranker — and the ranker cannot detect any of these, because **a wrong item and a right item look identical to a scoring function.**

The forced ranking answers *"which of these deserve attention?"* It has no opinion on *"is this item still true?"*, and this week says that is the more expensive question. A cheap partial answer: an item whose scope line contradicts a dated directive, or whose cost line contains an uncomputed multiplication, is mechanically detectable. Neither check exists.

**And the same pattern held one level down.** The `blocked-on-operator` component — shipped the day before to fix a real blind spot — scored the surveillance item +35 for being blocked on the operator **in the same edit that unblocked it**, because it cannot read tense. Found by running the tool on this session's own output. Patched (line-scoped, resolution-marker exclusion); classified explicitly as a false positive and **not** as the third structural blind spot that would retire the score under spec §4. See `meta/backlog-forced-ranking-spec.md` §7.
