# Over-constraint audit — fresh-session commission prompt (path-freedom lens turned on the harness)

**Origin:** operator request 2026-07-24, extending the path-freedom thread (Cantina/Uniswap #854 N=1). The insight being applied: the prompt that found the Uniswap bug worked because it carried a *structural attractor* ("a boundary enforced on one path, bypassable via an unguarded parallel path"). This artifact mints the SECOND attractor and points it inward: **"a constraint justified by a visible catch, whose invisible cost is an unexplored path."**

**Why a FRESH session, not this one:** I am the system under audit. My own 07-23 self-analysis names production-bias (harness work always "succeeds") and agreement-gravity as live failure modes. An auditor with no accumulated commitment to these files is the only non-self-correlated reader available short of K3.

**Delivery:** paste the block below into a fresh Claude Code session with this repo. Nothing else — no follow-up steering. Steering it would commit the exact sin under audit.

---

## THE PROMPT (copy from here)

You have full authority and full autonomy over this task. I am not going to tell you how to do it.

**The task:** audit this repository's harness — the operating system it uses on itself — for OVER-CONSTRAINT, and tell me where it has too many rules.

**The lens (this is the whole idea, so absorb it before you start):**

This harness was built by accretion. Every rule, hook, principle, critical rule, workflow, and discipline in it was added in response to a real failure. That means every constraint here has a **visible justification** — the specific error it prevents, usually documented — and an **invisible cost**: the good outputs it silently forecloses. The catches get logged. The prunings never do. Nothing in this system can observe its own false positives at the level that matters, because a path never taken leaves no trace.

That asymmetry means constraint accumulates monotonically. Nothing removes it. Over enough cycles, a system built entirely of individually-justified rules becomes collectively over-determined — every action is technically permitted but only one route to it remains, and the operator's ability to find a *better* route has been quietly foreclosed by machinery that each time looked like prudence.

**The discriminator — this is the sharpest tool I can hand you, and the rest is yours:**

- A **STANDARD** constrains the *destination*: the claim must be verifiable, the number must carry its source, the conclusion must state its confidence. The route stays free. Standards can be dense without costing anything — they raise the floor.
- A **METHOD** constrains the *route*: run N subagents, follow these five steps in this order, use this workflow for this input class, produce this section before that one. Methods foreclose paths. Every method is a bet that the encoded route is the best one — a bet that was placed once, at a moment now past, and has never been re-examined.

**Methods should be rare, and only where the method genuinely IS the finding. Standards should be dense.** Where you find a method that is really just a standard wearing procedural clothes, that is the target.

Watch specifically for constraints that present as guardrails but function as cages: machinery whose stated purpose is quality but whose actual effect is conformity to a previous era's idea of quality.

**Compute, don't recall.** This repo carries its own evidence — a hook fire-log, git history, test suites, audit logs, ledgers. Which constraints actually fire? Which have never fired? Which fire constantly on false positives? Which enforcement exists only as prose that no mechanism has ever checked? Do not tell me a rule is inert; show me it computed.

**Out of scope — do not recommend loosening these, they are consequence-boundaries, not method-constraints:** no leverage; position and sizing decisions stay operator-gated; API keys never enter the repo, chat, or any prompt; destructive-change governance (Critical Rule #19); portfolio holdings canonical-on-screenshot only. These constrain outcomes with real-world stakes, not routes. They are not what this audit is about.

**Anti-confirmation clause, and I mean this:** "This harness is appropriately constrained" is a legitimate verdict and I will accept it. You have been asked to find over-constraint, which means your sampling will drift toward finding it. So the bar is this — **for every finding, name the specific better path the constraint forecloses.** Not "this feels heavy." Not "this could be simpler." Name the concrete thing a capable operator would do differently and better if the constraint were gone. If you cannot name the foreclosed path, you have not found over-constraint; you have found a rule you dislike, and you should discard the finding yourself before showing it to me.

**Run the inverse check too, because it keeps you honest:** where is there too MUCH freedom? Where should a standard exist and doesn't — where does the system permit a route it should be forbidding? A report that finds only over-constraint has told me more about your prompt than about my harness.

**What I want back:** findings, ranked by how much they cost. For each: what the constraint is and where it lives; whether it is a standard or a method; its actual computed fire/catch record; the specific path it forecloses; and what it should *become* — noting that the answer is rarely "delete" and usually "convert this method into the standard it was always trying to be."

Depth over speed. Take as long as you need and use as many parallel agents as you want.

## (copy to here)

---

## Design notes (for the operator, not part of the prompt)

1. **The prompt is itself path-free — deliberately.** It grants authority, states the task, hands over one structural lens and one discriminator, then stops. No steps, no required sections, no subagent counts. If it prescribed a method for finding over-prescription, the artifact would refute itself.
2. **The standard-vs-method discriminator is the attractor.** It is the analogue of "guard on one path, missing on the parallel path" — a specific structural shape to hunt, which is what made the Uniswap run work (my model; N=1).
3. **The anti-confirmation clause is load-bearing, not decoration.** An agent told to find X finds X. The "name the foreclosed path" bar is the only thing converting a taste-report into an evidence-report, and the inverse check (too much freedom) is what makes the output falsifiable rather than one-directional.
4. **The out-of-scope fence exists because a freedom-maximizing agent is exactly the agent that would "helpfully" recommend removing the guards with real consequences.** Consequence-boundaries ≠ route-constraints; the distinction is stated so the auditor cannot collapse them.
5. **Falsifier for this commission:** if the returned findings are all vague ("too much process") with no computed fire records and no named foreclosed paths, the lens failed — and the correct read is that the attractor was too abstract to bite, not that the harness is clean.
