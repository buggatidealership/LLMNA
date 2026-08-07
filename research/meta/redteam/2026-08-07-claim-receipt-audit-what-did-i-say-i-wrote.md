# CLAIM-RECEIPT AUDIT — "what have you said you wrote, that you didn't write?"

**Operator question, 2026-08-07, immediately after the L57 orphan was found:** *"What type of mechanism needs to exist… so that anything you claim has been written IS written? Which takes the question: what have you said you have written, but didn't write?"*

**Answer discipline:** the question is computable, so it was computed, not described.

---

## 1. THE DESIGN PRINCIPLE THE L57 CASE EXPOSES

> **A receipt must be a BY-PRODUCT OF THE ACT, not a statement by the actor.**

Git is a receipt for a file write because *the write produces it* — I cannot claim a commit that isn't there. **"I codified L57" produces nothing.** It is a statement by the same party whose reliability is in question, and there is no artifact whose existence depends on it being true. That is the entire hole, and it is why L57 could be **injected into every cold session for two days** while existing nowhere canonical.

**Corollary that ranks the work:** for each class of claim, find the thing the ACT itself produces. Where nothing is produced, the claim is unverifiable *in principle* and the fix is to change the act so that it produces something — not to add a reminder to be careful.

---

## 2. THREE CLASSES OF CLAIM, AND WHAT ACTUALLY CHECKS EACH

| class | the claim | the by-product that could verify it | status |
|---|---|---|---|
| **A — FILE** | *"written to `meta/foo.md`"* | the filesystem | 🟢 **RUN 2026-08-07** (§3) |
| **B — ID** | *"L57 / B66 / TC-19 codified"* | the ID's presence in its canonical file | 🟢 **RUN 2026-08-07** (§4) — this is the class L57 lived in |
| **C — ACTION** | *"cascaded / booked / registered / re-weighted / verified"* | **NOTHING EXISTS** | 🔴 **UNCOVERED — this is the receipts hook, P1, 14 days overdue** |

🔴 **The L57 failure was invisible to class A by construction.** L57 was never claimed as a *file*, so no path-existence check could ever have found it. **One class of check cannot cover another class of claim** — and the reason the hole survived is that the harness had a partial instrument and treated it as a general one.

---

## 3. CLASS A RESULT — file references that do not resolve

Swept every backticked in-repo `.md` reference across the corpus: **1,356 distinct references, 67 unresolved raw → 23 after excluding `…`-abbreviated display references** (which are typographic, not claims).

🟢 **THE CORPUS SCORES WELL, AND BETTER THAN I EXPECTED.** Of the 23, the overwhelming majority carry an **explicit unwritten marker at the point of reference**:

| specimen | wording at the reference |
|---|---|
| `companies/AMBA/thesis.md` | *"— this synthesis **(to be created)**"* |
| `meta/structural-winners-cohort.md` | *"see … **(when written)** OR refer to chat transcript 2026-06-09"* |
| `wiki/robotics-primer.md` (6 files) | *"**Phase 3** — `sector/robotics-stack-map.md`"* — a declared roadmap |
| `wiki/README.md` (3 primers) | a **planned-entries table**, labelled as such |
| `meta/redteam/2026-08-XX-…-K3-return.md` | a future deliverable, `XX` in the filename |
| `meta/tier-cascade-log.md` | `path/to/file.md` — a template placeholder |

**⇒ The "(to be created)" discipline is real and holding.** A plan is not a false claim; an unhedged citation is.

🔴 **The genuine exceptions — 2:**
1. **`meta/network-allowlist-recommendation.md`** — cited as a deliverable in the standing operator checklist. **Already self-flagged in `day-state.md` 2026-07-27:** *"this file was never written — the recommendation exists only as this checklist line."* Caught previously, still unresolved.
2. **`nvda-n1x-unbiased-money-flow-analysis.md`** — cited **bare, in `predictions/lessons.md`**, with no hedge. A lesson citing an artifact that does not exist. **The worst of the two, because lessons.md is a canonical file that other things cite.**

---

## 4. CLASS B RESULT — ID reconciliation across every namespace

Set difference: IDs **cited** in `session-prime.md` / `day-state.md` / `CLAUDE.md` vs IDs **present** in each canonical file.

| namespace | canonical | cited | orphans |
|---|---|---|---|
| **L** lessons | 60 | 35 | **NONE** (L57 was the sole orphan; fixed 2026-08-07) |
| **B** biases | 59 | 32 | **NONE** |
| **TC** triangulation | 19 | 17 | **NONE** |
| **P#** principles | 46 | 44 | **NONE** — raw run flagged #4/#5/#8/#19; verified as **Critical Rule** references, which the regex cannot distinguish from Principles. **Instrument artifact.** |
| **PC** patterns | 13 | 10 | **NONE** — raw run flagged PC-16; `CLAUDE.md` documents `[PC-16 skipped]`. **Declared gap, not an orphan.** |

🟢 **ZERO true orphans across all five namespaces.** L57 was the only one and it is closed.

⚠️ **Both raw hits were instrument artifacts, and both were checked before being reported** — the same discipline that saved the Korea attribution this morning. Had they been reported raw, this artifact would have claimed 6 orphans where there are none. **An audit that miscounts in the alarming direction damages trust exactly as much as one that misses.**

---

## 5. WHAT IS STILL UNCOVERED, AND IT IS THE LARGEST CLASS

**Class C — action claims — has no by-product and therefore no check.** Every one of these is currently believed on my word alone:

- *"cascaded to the affected theses"* (Critical Rule #10)
- *"booked to the todo"* · *"registered a falsifier"* · *"re-weighted H1/H2/H3"*
- *"verified"* / *"the verifier returned X"*
- *"pruned"* · *"retired"* · *"re-specced"*

**This is the RECEIPTS HOOK — already specified, P1, and 14 days overdue** (`meta/todo.md`; K3 proposal adjudicated 2026-07-20). The K3-Swarm amendment already carries the correct frame and it is exactly the L57 lesson stated in advance:

> **"A header/status line is a PROMISE, not a receipt."** (G-07)

**Design consequence, registered here:** the hook cannot work by scanning prose for the word "cascaded." It must **pair each action-claim class with a repo-observable postcondition** and check the postcondition — e.g. *"cascaded to N theses"* ⇒ those N `thesis.md` files appear in the same commit's diff. Where no postcondition can be defined, **the claim must not be made in that form.**

**Blind-check (#51):** *distinguishes "the act happened" from "the act was narrated" · reads on an artifact whose existence does not depend on my say-so (diff contents, file presence, ID set membership) · **goes blind if** the claim class has no observable by-product — which is precisely class C, and is why the fix is to change the ACT so it emits one, not to add a check over the narration.*

---

## 6. HONEST SCOREBOARD

| | result |
|---|---|
| Classes checkable today | **2 of 3** |
| Class A unresolved refs | 23, of which **21 explicitly hedged**, **2 real** |
| Class B orphans | **0** (after L57's repair; 2 raw hits were instrument artifacts) |
| Class C coverage | **0%** — no mechanism exists |
| Found by me vs by others | L57 and the INDEX staleness were both found by a **fresh session**; the 2 class-A gaps were found by **this sweep**; `network-allowlist` was self-caught 07-27 |

**The pattern holds and is now N=4 on the week: I find these by EXECUTING a check, never by RE-READING my own work.** The receipts hook is the same insight applied to the one class where execution currently has nothing to execute against.
