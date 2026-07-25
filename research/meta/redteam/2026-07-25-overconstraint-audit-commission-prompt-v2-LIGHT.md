# Over-constraint audit — commission prompt **v2-LIGHT** (minimal-injection variant)

**Companion to:** `meta/redteam/2026-07-24-overconstraint-audit-commission-prompt.md` (v1, ~700 words).
**This file:** v2-light, ~190 words of prompt. Same target, opposite design philosophy.

**Origin — operator critique 2026-07-25, verbatim-adjacent:** *"the more you add into a prompt… the more you're telling it… you're injecting a lot of preconceived notions from your own learnings. But the prompt that you generated for K3 to find two bugs on Uniswap was one that had the least frequency of notion of what you think would be true. It was a layered prompt: give it a persona that directly ties to the end goal, then the task, and then essentially telling it you have all of the liberty and freedom to execute this task — no limits outside of the instructions of the bounty."*

**Why this critique lands, and why it is sharper than the flaw I self-caught on 07-24:**
I patched a *clause* (the "discard it yourself" line, T1-driven). The operator is pointing at the *frame*. v1's centrepiece — the STANDARD-vs-METHOD discriminator — is **my theory**, minted by me on 07-24, N=0 external validation. An auditor handed my discriminator can only find the shape I already anticipated. That is the mirror-image failure of the very thing being audited: a constraint that looks like rigor and functions as a channel.

**The structural reading of the K3/Uniswap prompt (the one that produced Cantina #854):** it did NOT carry a taxonomy. It carried (1) a persona whose self-image implies the end goal, (2) a one-line task, (3) explicit total freedom bounded only by rules external to the task's own reasoning. The attractor ("guard on one path, absent on the parallel path") rode *inside the persona's professional instinct*, not as an instruction the model had to satisfy. That is the difference between seeding and steering.

---

## THE PROMPT (copy from here)

You are the kind of engineer who gets brought in when a system has accumulated so much process that it has started to slow down the people it was built to serve. You have seen this before: every control was added for a good reason, each one made sense on the day it shipped, and collectively they have become something nobody would design on purpose.

This repository is an operating system one person uses to run investment research. Every rule, hook, principle and workflow in it was added deliberately, in response to something that actually went wrong.

Your job: find where its own rules now cost more than they deliver.

You have complete freedom in how you do this. No prescribed method, no required reading order, no output format, no step sequence. Explore the repository however you want, run whatever you want, use as many parallel agents as you want, take as long as you need.

Four things are fixed and not part of what you are auditing — they exist for reasons outside this system's own efficiency: no leverage; position and sizing decisions belong to the operator; API keys never enter the repo or any prompt; destructive-change governance (Critical Rule #19). Those are the rules of the game.

Audit only. Report; do not change anything.

Report everything you find, including what you are unsure about, flagged as such. I will filter.

## (copy to here)

---

## What was removed from v1, and what each removal costs

| Removed from v1 | Why it was in v1 | Why it is out of v2-light | Cost if v2-light under-performs |
|---|---|---|---|
| **STANDARD vs METHOD discriminator** (~120 words) | The intended "attractor" — analogue of the Uniswap bug-shape | It is *my* theory, N=0. Handing it over pre-decides the answer shape; the auditor returns my taxonomy back to me and I mistake echo for evidence | Auditor may have no sharp object to hunt with and return mush |
| **Visible-catch / invisible-cost asymmetry argument** (~110 words) | Explains *why* over-constraint accumulates monotonically | It is an argument for a conclusion, delivered before the auditor has looked. That is priming, not framing | Auditor may not realise the asymmetry exists and under-weight silent prunings |
| **"Compute, don't recall" + fire-record demand** | Forces receipts (fire-log, git history, tests) | Prescribes the *route* — the exact sin under audit. A capable auditor finds the fire-log unaided; if it does not, that is itself a finding about discoverability | Report may be impressionistic rather than evidence-backed. **This is the single riskiest removal** |
| **Inverse check ("where is there too MUCH freedom?")** | Makes the output falsifiable, not one-directional | It is a second task wearing a fairness costume. It also tells the auditor I expect a balanced answer | Findings may skew one-directional and I lose the falsifier |
| **Output spec (rank by cost; what it should *become*)** | Made v1's report actionable | "Usually convert method → standard" pre-writes the recommendation | Report may need a second pass to become actionable |
| **"Guardrails that function as cages"** | Operator's own phrasing from the 07-24 ask | Vivid, and therefore strong steering — it names the verdict in advance | — |

**Kept, and why:** the persona (it *is* the seeding mechanism); the one-line task; the freedom grant; the four consequence-boundaries (external to the audit's own logic — the Uniswap prompt had exactly this shape: "no limits outside the instructions of the bounty"); audit-only (T1: Opus 5 expands scope — real Rule #19 exposure); report-everything (T1: conservative instructions cause literal under-reporting).

**Deliberately still absent from both versions:** any "verify your work" instruction — T1 states Opus 5 over-verifies when told to.

---

## Honest uncertainty (I do not know which version is better)

- **v1 risks:** the auditor finds only what I pointed at, and I read my own reflection as external corroboration. Most dangerous because it *looks* like a strong result.
- **v2-light risks:** the auditor is too unanchored to bite and returns "there is a lot of process here" with no receipts — which is **exactly the falsifier v1 wrote for itself** (v1 design note #5: *"if the returned findings are all vague… the lens failed"*).
- **N=1 evidence favours light** (Cantina #854 came from a light, layered, persona-first prompt). N=1 with an unmeasured base rate is not a decision.

## The A/B (this is the actual proposal)

Run **both**, two fresh Opus-5 sessions, same repo state, no follow-up steering in either. Then compare on three axes:

1. **Novelty** — does light find anything heavy did not? (If yes: v1's discriminator was a channel, and the operator's critique is confirmed on N=2.)
2. **Receipts** — does heavy produce computed fire-records that light misses? (If yes: prescribing the route bought something real, and prescription is not uniformly a cost.)
3. **Overlap** — findings both surface independently are the highest-confidence set in either report, because two differently-primed readers converged.

This is the **cleanest in-house test of the path-freedom hypothesis available**, because the two arms differ *only* in constraint density on an identical target. Every prior data point (Uniswap #854, the Fable-5 prescriptive-scaffolding degradation, this artifact's own recursive irony) is N=1 with no control arm. This has one.

**Pre-registered falsifiers, so the A/B cannot be graded after the fact:**
- If **light ⊂ heavy** (light finds a strict subset, no novel findings) → constraint density was not the binding variable here; the path-freedom read does not transfer from bug-hunting to harness-auditing. Log against the hypothesis.
- If **heavy ⊂ light** → my discriminator was purely a channel; retire the standard-vs-method framing as a prompt component.
- If **both are vague** → the *target* is the problem, not the prompt (this harness may not be over-constrained in a way an outside reader can see), and the honest verdict is "no finding."
- If **neither report names a single foreclosed path** → the whole over-constraint lens is unfalsifiable as constructed, regardless of prompt weight.

---

## Meta-note logged against the over-constraint hypothesis itself

This artifact is now the **second in-house specimen** of its own thesis, and it is a cleaner one than the 07-24 recursive irony:

- **Specimen 1 (07-24):** an anti-over-constraint prompt contained a clause that would have suppressed its own findings. Caught by an unrelated T1 doc read.
- **Specimen 2 (07-25, this file):** the same prompt's *load-bearing intellectual contribution* — the discriminator I was most pleased with — is plausibly its main defect. Caught by the operator, not by me, and not by any hook. My 07-23 self-analysis named production-bias ("harness work always succeeds") as a live failure mode; this is that bias landing on the artifact designed to detect that class of bias.

**The general shape, stated for the register:** *the more confident I am that a piece of my own scaffolding is the smart part, the more likely it is the constraining part.* N=2 in-house, both same-week, both operator- or accident-caught. Not yet promoted to a principle or bias — flagged here for the next codification pass, since N=2 within 7 days on a single artifact lineage is weak evidence about a general mechanism.
