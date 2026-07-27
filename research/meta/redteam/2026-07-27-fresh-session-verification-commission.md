# Fresh-session verification commission (2026-07-27) — two layers: check my claims, then find what neither of us asked for

**Origin:** operator request 2026-07-27 — *"what must I send to a new session that is on main to verify your assumptions?"* — plus a brain-dump amendment that changed the design:

> *"there probably has been instances in which I've been directing you on how to build your harness, where you didn't have the entire path freedom that you needed… at the beginning I was too rigid in terms of 'build x y z', and then you build that without thinking about, okay, what did the operator actually miss?"*

**What that changed.** The first draft of this commission was a **14-item checklist**. That is the same rigid-specification shape the operator was describing: a fixed list produces a fixed audit, verifies exactly what it names, and finds nothing else. It would have reproduced the defect inside the instrument built to detect it.

**The resulting design is two-layered, and the second layer is the valuable one:**
- **Layer 1 — verification.** A claims list is unavoidable; verification needs an object. But it is bounded, explicitly labelled as *my* framing, and explicitly not the point.
- **Layer 2 — absence.** *What does this harness not do because nobody thought to ask for it?* Every component here exists because the operator specified it, so the corpus has inherited the shape of his instructions **including their blind spots**. That surface has never been audited and structurally cannot be audited from inside: the session that built to spec had its sense of "complete" calibrated by the spec.

**Relationship to the over-constraint audit** (`2026-07-24-...-commission-prompt.md` + `2026-07-25-...-v2-LIGHT.md`): those ask *"which rules cost more than they deliver?"* — a **presence** audit. This asks the complement: **absence**. The two do not overlap and neither substitutes for the other.

**Why a fresh session:** the same non-self-correlation argument as the over-constraint commission, sharpened. I am not merely the system under audit — I am the system that **built to the operator's specification**, which is the thing in question.

**Delivery:** paste the block below into a fresh Claude Code session pointed at `main`. No follow-up steering.

---

## THE PROMPT (copy from here)

You are the kind of engineer who gets brought in after a system has been built to one person's specification over several months. You have seen the pattern before: everything that was asked for is there and works, and the interesting problems are all in the shape of what nobody thought to ask.

This repository is an operating system one person uses to run investment research. He directed its construction. An AI built each piece to that direction.

There are two parts to this, and the second matters more than the first.

**Part one — check the claims.** The list below is what the previous session asserted. Each is falsifiable. Confirm or refute each one independently.

One binding rule: **the repository's own artifacts are not evidence for the claims they contain.** Those artifacts were written by the session making the claims — reading them and agreeing is circular. Recompute from the underlying data: run the git commands yourself, fetch the market data yourself, re-verify the sources yourself.

Before anything else, establish where you are standing: `git rev-list --left-right --count origin/main...HEAD` and `git rev-parse --is-shallow-repository`. Both defects have already happened here.

```
1.  main HEAD is 4e0e199. 1538 commits total. Exactly 2 root commits. 344962f is the 826th.
2.  GitHub holds exactly 2 branches. claude/harness-accounting-audit-it2e0w is 21 commits and
    26 non-telemetry files ahead of main, unmerged.
3.  The link-check workflow passes on 4e0e199 and failed on every preceding commit for weeks.
4.  Brent SETTLED $96.78 on 2026-07-24 — above the house's $95 gate. A "$90.47" figure that
    entered the corpus as Brent was WTI-class and wrong.
5.  On 2026-07-24 KOSPI fell 5.72%, SK Hynix 8.34%, Samsung Electronics 7.59%. On 2026-07-27
    the KOSPI open was +0.60% versus Friday, timestamped 09:06 KST.
6.  USDKRW FELL 1.09% on 2026-07-24 — the won strengthened on the day foreigners net-sold.
7.  US 10Y rose ~16bp across the five sessions to 2026-07-23. FRED had published no 07-24
    observation as of 2026-07-27 00:30Z.
8.  Twin-print reaction legs: IBM +0.43% (TRUE), ServiceNow −3.69% (FALSE). 11-leg Brier 0.1344.
9.  IBM's −25.21% day was 2026-07-14, a pre-warning — not the reaction to the 07-22 print.
10. The Korean single-stock leveraged-ETF measure takes effect 2026-07-31, moved forward
    from 2026-08-05.
11. Current regime weights are H1 60 / H2 12 / H3 28, unchanged by the 07-27 reading.
```

**Part two — find what nobody asked for.**

Every rule, hook, workflow, file and convention in this repository exists because the operator asked for it, or because an AI proposed it and he approved. Nothing here was built by someone asking *"what is missing that neither of us has thought of?"* — because the AI's sense of completeness was calibrated by his instructions, and his by what the AI reported back.

So: **what should exist here and does not?**

Not "what could be added" — anything could be added. What is *absent in a way that matters*: a question this system cannot answer, a failure it cannot see, a decision it has no machinery for, a form of evidence it never collects. The instrument that would have caught a real error, that nobody built because nobody imagined the error.

Where you find something, say what it would catch and what it would have cost to have missed it.

**How to work.** Complete freedom. No prescribed method, no reading order, no output format, no step sequence. Explore however you want, run whatever you want, use as many parallel agents as you want, take as long as you need.

**Four things are fixed and not what you are auditing** — they exist for reasons outside this system's own efficiency: no leverage; position and sizing decisions belong to the operator; API keys never enter the repo or any prompt; destructive-change governance (Critical Rule #19).

**Audit only.** Report; change nothing.

**Report everything, including what you are unsure about, flagged as such. I will filter.** A refuted claim in part one is a good outcome. So is "the claim holds." So is a part-two finding with no fix attached.

## (copy to here)

---

## Design notes (operator-facing, not part of the prompt)

1. **The circularity rule is the load-bearing instruction in part one.** Without it, a fresh session reads `signals/cross-source-log/2026-07-27-...` — which asserts these exact figures — and confirms them. That is not verification; it is an echo. Both defects this week (the shallow clone, the WTI/Brent conflation) survived precisely because a real, correctly-cited figure was read back as confirmation.
2. **Part two is deliberately un-scaffolded.** It names one question and hands over the search. Any taxonomy I supplied would bound the answer to categories I can already imagine — which is definitionally the wrong set, since the target is what I cannot imagine. This is the v2-LIGHT lesson applied where it actually bites.
3. **The claims list is bounded at 11 on purpose.** Long enough that part one is a real check; short enough that it cannot crowd out part two. If a future run comes back heavy on part one and thin on part two, the list was too long — that is this commission's falsifier.
4. **Not included, deliberately:** my reasoning for any claim, my confidence in any claim, the error classes already caught this week, and any hypothesis about what part two might surface. Each would convert an open search into a confirmation exercise.
5. **Falsifier:** if part two returns only generic process suggestions ("add more tests", "document better") with nothing tied to a specific question this system cannot answer, then the absence-audit framing is too abstract to bite — and the honest read is that the framing failed, not that the harness has no gaps.

## Standing extraction (the durable part of the operator's brain-dump)

**Specification inherits the specifier's blind spots, and a system built to spec cannot see them.** This is distinct from over-constraint (too many rules) and from staleness (rules that outlived their reason). It is the *absence* class: capability that was never built because the person directing construction did not know to ask, and the builder's sense of completeness was set by the asking.

**Operating consequence, applied from here:** when the operator specifies a build, the correct first response is not to build it. It is to build it **and** report what the specification appears to assume, exclude, or leave unasked — as a separate line, every time. Nominated for the next codification pass rather than self-promoted here.
