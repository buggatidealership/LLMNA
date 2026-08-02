# Supervisor loop — operator proposal, evaluated and split (2026-08-02)

**Operator, verbatim-adjacent:** *"what if you just create a loop? And that agent's task is to ensure that every hook does what it's supposed to do and scans the harness with any remaining to-dos that are still open… you have to have a supervising agent whose only job is to ensure that the harness does the job it's supposed to do… I can verify the morning brief and the evening brief because I see them. But I can't see what's on the to-do list and what hasn't been done yet… Again, do not take what I say literally."*

---

## §1 — The diagnosis is right, and it is sharper than the proposal

The load-bearing sentence is not *"create a loop."* It is **"I can verify what I see; I can't see the to-do list."**

That is an **observability** gap, not an execution gap. The parts of the harness the operator sees (morning brief, EOD close, chat output) are checked by a human every day. Everything else — 19 hooks, 87 to-dos, 155 detectors — is checked by **nobody**, because I am simultaneously the author, the executor, the auditor and the reporter.

**Computed 2026-08-02** (`meta/tools/harness_supervisor.py`), not asserted:

| | reading |
|---|---|
| Hooks wired into `settings.json` | **19/19** — wiring is not the problem |
| Hooks with a fire-log entry in ≤14d | 15 |
| Hooks that have **never** written a log entry | **4** |
| Open to-dos | 87 |
| **Past their date** | **64 (73%)** |
| Older than 30 days | 23 |
| P0 overdue | 3 (by 9, 5, 5 days) |
| Detector blind-check compliance | 0/155 |

**73% of the queue is late.** At that rate the date field carries almost no information — it is a wish-list wearing a schedule's clothes. This is the same accretion pathology the over-constraint audit found in the rule layer, now visible in the task layer: things get added, nothing gets removed.

## §2 — The finding that changes the design

**The first check the proposed supervisor would run is already broken, and it would have reported a confident falsehood.**

Four hooks have never written to the fire log: `session-start-hook`, `llm-native-priming-hook`, `borrowed-vs-firstprinciples-hook`, `analyst-pt-context-hook`.

A log-reading supervisor reports those as dead. **At least two of them provably run on every single turn** — `session-start-hook` produces the briefing at the top of every session and `llm-native-priming-hook` injects the discipline block into every prompt. They are not dead. **They are unobservable.**

So the instrument cannot distinguish:
- a hook that never fired, from
- a hook that fires constantly and doesn't log.

**Consequence for the design: a supervisor that READS logs is not a supervisor. It has to EXECUTE the hooks.** Otherwise it inherits every blind spot of the thing it is auditing, and — worse — reports high confidence while doing so. This is the same defect class as the KIOXIA unfireable falsifier and the `macro-anchor-hook` unmeasurable repair criterion, now found a third time, in the supervisor concept itself, before it was built.

## §3 — Where the proposal needs splitting: two jobs, opposite natures

The proposal bundles two tasks. They should not share an implementation, because they have opposite risk profiles.

| | **Job A — "does every hook fire?"** | **Job B — "execute the remaining to-dos"** |
|---|---|---|
| Nature | deterministic, mechanical | judgment-heavy, open-ended |
| Right tool | **a script / test suite** | an agent (or a human decision) |
| Cost | seconds | large |
| Risk of getting it wrong | near zero | can change live enforcement, positions, framework |
| Verifiable by operator | yes — one number | no — requires reading the work |

**Job A should NOT be an agent.** An agent that reads hook source and forms an opinion is *strictly less reliable* than thirty lines of Python that actually invoke the hook and check the exit code. Using a language model where a test suffices imports non-determinism into the one place the harness has none. That is a downgrade dressed as sophistication.

## §4 — Where I'd push back hardest: the auto-executor

The proposal's second half — *"if they haven't been done yet, let's just execute them"* — I am not building, for three reasons, ranked.

**1. It turns `todo.md` into a privilege-escalation channel.** *I write `todo.md`.* If an autonomous executor acts on whatever is in it, then anything I write into that file gets executed with no further gate. Today the file contains items whose scope includes modifying live enforcement hooks — a **Rule #19 HIGH** class requiring operator pre-approval. An executor that treats the queue as authority routes around the governance layer *by design*, and it does so invisibly, because the operator's stated problem is precisely that he can't see this file.

**2. A 73%-late, 26%-stale backlog should be TRIAGED before it is AUTOMATED.** 23 items are older than 30 days; the oldest are 73 days. Automating execution of a list that is substantially dead means spending real tokens completing work that was superseded weeks ago. **The first pass over this backlog should delete, not execute.** Automating it first locks in the accretion.

**3. Who supervises the supervisor.** If I can let 87 items rot, an agent I spawn — whose report I read and summarise — can also produce a plausible "all clear." A supervisor adds accountability *only* if its output is a **computed artifact the operator reads directly**, not a narrative I relay. That is why what shipped tonight prints a table and appends a dated ledger row, rather than writing me a report.

## §5 — What shipped tonight (read-only, no execution)

**`meta/tools/harness_supervisor.py`** — one command, one screen, writes nothing except an optional dated row:

- hook state (wired / live / silent / no-log) **with its blindness stated in the output itself**
- backlog age distribution, overdue P0s, and a separate count of >30d **triage candidates** (late ≠ dead)
- rolled-up #51 detector compliance
- a single VERDICT line

**`meta/supervisor-ledger.md`** — append-only dated readings. **A missing date row is itself a finding**: the gap is the evidence that the pass did not run. That is the same accountability shape as the blind-check ledger, and it is the only form of accountability available to a system whose sole reviewer is also its author.

Both new detectors in the supervisor carry **#51 blind-check lines** — the first entries in the NEW cohort, which means #51 now has a non-empty denominator and dogfoods on its own instrument.

## §6 — What I deliberately did NOT build, and what it would take

| Not built | Why | What it needs |
|---|---|---|
| **Execution probes** (fire each hook against a fixture, check exit code) | Hooks have side effects — they write to the fire log and some block Stop. Probing naively pollutes the very telemetry being measured. | The `LLMNA_PROBE` tagging convention already exists in 3 hook scripts (added by the 07-23 hardening). Extend it to all 19, then probe. **This is the single highest-value next step** — it is what converts the supervisor from log-reader to actual supervisor. |
| **Auto-executor** | §4 | Backlog triage first; then a *whitelist* of item classes safe to auto-run (recurring audits with deterministic procedures, no enforcement/position impact) — never "whatever is in the file". |
| **A scheduled Routine** | Cheap to add, but a recurring autonomous pass is a governance choice, not a technical one. | Operator's call. My recommendation: **weekly, read-only, notify only when the VERDICT line changes** — a daily run on a slow-moving state is noise, and noise is how a supervisor becomes ignored. |

## §7 — The honest limit

This does not fix the underlying problem, and I want that on the record rather than buried. **The supervisor makes the state visible. It does not make anyone act on it.** Three P0s are already visible, surfaced loudly at the top of every single session by `session-start-hook`, and they are still 9, 5 and 5 days overdue. Visibility was never the binding constraint on those.

So the honest prediction (my model): a read-only supervisor is **necessary and not sufficient**. It closes the operator's stated gap — *"I can't see it"* — and it will not by itself close the backlog. The thing that would actually close the backlog is a **forcing function**: a rule that a to-do past N days is auto-deleted unless explicitly renewed, which converts silence from "still open" into "dropped." That is a much more invasive change and it is the operator's decision, not mine.

**Falsifier for this whole artifact:** if the supervisor runs weekly for a month and the VERDICT line never changes, it is a mirror rather than an instrument — retire it and build the forcing function instead.
