# 2026-08-07 FRI EOD — DISCOVERY: memory is pre-sold through 2027, SK Hynix commits $38B — and the held name it lands on has TWO thesis files

**Run:** EOD CONDITIONAL SYNTHESIS Routine, FULL PATH. One Leg-B unanchored discovery agent (company- and segment-agnostic, breadth-at-search/filter-at-digest).
**Segment classification (Rule #6 / Principle #29):** memory-and-storage (items 1–2), networking/advanced-packaging (3–4), infrastructure-financing + power-and-cooling (5–6).
**Status:** 🔴 **Items [2] and [5] are UNDER VERIFICATION at write time** — two verifiers fired in parallel per Rule #16. Nothing below is cascaded to a thesis until they return.

---

## TL;DR

Memory output for all of 2027 is reportedly pre-allocated with **Apple unable to secure a fourth DRAM supplier**; SK Hynix approved **~$38B for two new fabs today**. But the discovery's most useful output is not a market signal — **the L60 prior-read check found that a held position has two live thesis files, and the one the corpus mostly points at is not the one with the recent work.**

---

## 1. THE DISCOVERY ITEMS

| # | Mechanism | Tier | Status |
|---|---|---|---|
| 1 | **2027 DRAM/HBM output fully pre-allocated** — Samsung/SKH/Micron finished 2027 allocation talks early; **Apple reportedly failed to line up a 4th DRAM supplier** | T2/T3 (Digitimes-lineage) | plausible, not verified |
| 2 | **SK Hynix board approves KRW 54.3T (~$38B)** — Yongin "Y2" DRAM 35.2T + Cheongju "M17" NAND 19.1T; Yongin cluster timeline reportedly pulled **2045 → 2033** | claimed T1 board resolution | 🔴 **VERIFIER IN FLIGHT** |
| 3 | **FCC drafting ban on Chinese optical transceivers** — hits Zhongji Innolight (27% global share, 62% of Q1-26 revenue from US); Coherent/AOI/Lumentum rallied same day | T1/T2 Reuters-lineage | directional |
| 4 | **Japan tightens advanced-packaging tool licensing to China** | 🔴 **T3, Chinese financial press ONLY** | **NOT CONFIRMED — see §3** |
| 5 | **AI data-centre CMBS spreads widening**; 2 of last 3 deals repriced wider; "hyperscaler bond coverage ratios ~5× (Feb) → below 2× (Jul)" | T2 Bloomberg | 🔴 **VERIFIER IN FLIGHT** |
| 6 | **AI's spiky power draw physically degrading DC equipment** — some storage systems replaced after weeks | T2 Bloomberg, single-source | registered, not actioned |

**The agent's own strongest-disconfirming pick was [5]**, and it picked correctly: it is market-priced rather than vendor-reported, and its framing ("supply of debt is the risk, not defaults") makes it a cost-of-capital signal rather than a distress signal. That distinction is exactly the kind that gets flattened in transmission, which is why it went to a verifier.

---

## 2. 🟢 THE L60 CHECK EARNED ITS KEEP ON ITS FIRST SCHEDULED RUN

L60 was codified this morning: *before an external attribution enters an artifact, grep for our own prior read.* Run here as a matter of course, and it changed two readings:

**(a) The SK Hynix CEO "worst year in the industry's history" quote is ALREADY OURS.** The agent correctly flagged it as **not fresh (2026-07-10)** — and the corpus goes further: it was ingested **2026-07-12**, routed, and put through a **substance-validation run** (`2026-07-12-sun-eve-kwak-substance-validation-blockF.md`), then cascaded into `companies/SKHY/thesis.md`. **Item [1]'s "corroborating" quote is our own month-old datum arriving back as if it were support.** Treating it as independent corroboration would have double-counted a single source — the precise shape of the error the whole exercise exists to stop.

**(b) The data-centre debt theme is not new either.** `2026-07-23-thu-ai-brief-intake-1p65T-debt-...md` already carries a read on the financing stack. **Item [5] is a continuation with a fresh market-priced datum, not a discovery.** Registered as such.

**⇒ Two of six items were partially already-held.** Neither was wrong; both would have been over-weighted as new. **The check cost one grep.**

---

## 3. 🔴 ITEM [4] IS NOT ENTERING THE CORPUS

Japan/advanced-packaging licensing is sourced **only** to Chinese financial press (Eastmoney, 163.com, both 2026-08-03). The agent tried and failed to corroborate via METI, Reuters or Nikkei and **flagged it itself as the translation/attribution-garble pattern**.

**That is the same shape as this morning's refuted Korean "next-gen AI chip supply delay"** — single-language press, no primary source, a mechanism that would be very convenient if true. **Two instances in one day.** Logged here, cascaded nowhere, and if it is real a primary source will appear.

---

## 4. 🔴 THE STRUCTURAL FINDING — A HELD POSITION HAS TWO LIVE THESIS FILES

Surfaced only because the L60 check made me look up where SK Hynix knowledge actually lives before cascading into it.

| | `companies/HYNIX/` | `companies/SKHY/` |
|---|---|---|
| thesis.md size | **334 KB** | 89 KB |
| header "Last updated" | 2026-06-12 | 2026-07-11 |
| most recent dated entry | **2026-07-28** | 2026-07-27 |
| inbound references from the rest of the corpus | **183** | **22** |
| `INDEX.md` points to | ✅ this one | — |
| Position implication carried | **`HOLD (SKHY 37 ADS)`** | **`HOLD (37 ADS)`** |

🔴 **Both files carry position implications for the SAME live position — 37 ADS.** This is not a held/exited split and not two instruments: `HYNIX/thesis.md` line 21 states the SKHY position explicitly. **Both were written to within one day of each other in late July. Neither is canonical.**

**Why this matters more than it looks:** a Rule #10 cascade lands in whichever folder the session happens to pick. **The corpus points 183:22 at `HYNIX/`, while `holdings.md` names the position `SKHY`** — so the retrieval gradient and the position record point at different files. Work done in one is invisible from the other.

**Classification: L53 (retrieval-drawer error) at the FOLDER level, on a live position.** L53 governs a name filed under the wrong theme being functionally invisible; this is a name filed under two folders, where the more-referenced one is not the one named in holdings.

⚠️ **I first read this as "duplicate folders = defect," then checked whether it was a deliberate GDR-vs-ADS distinction — it is not, and the check is what established that.** Recording the sequence because the wrong read was the intuitive one.

**NOT resolved tonight.** Merging or retiring a 334 KB thesis file touches live position records and is **Rule #19 MEDIUM-to-HIGH** — it is booked for the operator, not executed at EOD by the party that found it.

**Blind-check (#51):** *distinguishes "one canonical thesis per position" from "two files that each look complete" · reads on the count of `companies/*/thesis.md` files carrying a Position-implication line for the same holdings row · **goes blind if** a folder stops being written to but keeps its inbound references, which makes it look retired while still being the retrieval target.*

---

## 5. WHAT THE AGENT LOOKED FOR AND DID NOT FIND (recorded — a negative result is information)

- No fresh (≤36h) EU capital/regulatory item — the 7-gigafactory tender is **8 days stale**, excluded.
- No fresh China-side regulatory response beyond stock reaction — MOFCOM draft consultation is FT-sourced ~07-21/22, **excluded as stale-recycle**.
- **No genuine demand-destruction or efficiency-compression signal in the window.** Worth stating plainly: the U8/B47 falsifier side produced nothing today.
- No FERC compliance filing yet against the ~2026-08-17 deadline from the June 18 order — **flagged for a dedicated sweep on/after 08-17.**

---

## 6. POSITION IMPLICATION

**Position implication: 🔴 NO ACTION** — no size change on any name — **the two items that could bear on a held position are both still under verification, one of the six is single-language and refused entry, and two were partially already in the corpus.** Weights held **H1 60 / H2 11 / H3 29**. Any sizing decision remains operator-gated regardless.

**Rule #10 cascade: DEFERRED, deliberately.** The correct target file for SK Hynix is ambiguous (§4), and cascading into the wrong one would be worse than not cascading — it would create a record that looks complete and is not. **Cascade executes once the verifiers return AND the folder question is resolved by the operator.**

**Signal density (Rule #14):** items 1–2 are same-segment (memory-and-storage) same-direction as the 2026-07-12 Kwak cluster — but per §2(a) that is the *same source lineage*, not a third independent signal. **No TC promotion. N is not incremented on a datum we already hold.**
