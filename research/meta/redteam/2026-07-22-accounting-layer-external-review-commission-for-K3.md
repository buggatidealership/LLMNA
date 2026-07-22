# External review commission — blind adversarial pass

**Branch under review:** `claude/harness-accounting-audit-it2e0w`
**Reviewer:** K3 (different model family — external oracle)
**Date:** 2026-07-22

## Why you, and why blind

The author is a same-family model with a documented failure mode: its patches
hold against the attacks it imagined and fail one character away from them. A
same-model self-review reproduces the same blind spot — it pins holes as
imagined and misses holes as spelled. You do not share the author's priors.
That is the entire value of this pass, so it is run blind: you are told what the
work had to achieve, and nothing about what was done.

## The mandate the work was done under (the bar it must meet)

> Repair the ACCOUNTING layer of the harness — the logs, receipts,
> promise-tracking, and self-grading that the machinery reports about itself.
> Target: make it structurally impossible for the logbook to claim
> "done / verified" without a machine-checkable receipt.

That sentence is the standard. The objective behavior contract for any mechanism
you encounter is documented in the repository itself — `research/CLAUDE.md` (the
harness specification, its hook definitions, and its Critical Rules), the
governance and spec documents under `research/meta/`, and each mechanism's own
docstring. Hold the code to those contracts, not to any account of the code.

## What to do

1. Fetch the branch and diff it against main **yourself**. You are given no
   summary of what changed — discover it.
   ```
   git fetch origin main claude/harness-accounting-audit-it2e0w
   git diff origin/main...origin/claude/harness-accounting-audit-it2e0w
   ```
2. Review the **mechanisms** in that diff — the executable hooks and guards, the
   scripts they invoke, their tests, and the data files they read and write. Any file whose
   change is prose that describes, summarizes, grades, or inventories the work
   (rather than implementing a mechanism) is the author's account of the work,
   not the work — do not let it seed your findings.
3. Treat every comment, docstring, added prose line, and commit message as a
   **claim to be refuted**, never as ground truth. They state what the author
   believes the code does. Your only evidence is what the code does when you run
   it.

## Your job: try to break each guard

For **each** guard or enforcement mechanism the diff touches:

- Try to **bypass** it. Prove every bypass by **running the live hook** — feed
  it input on stdin exactly as the harness invokes it — and show the exit code
  and output. A payload that should be caught but is allowed is a bypass. A
  legitimate input that is wrongly blocked is a false-positive. Both are findings.
- Where a mechanism decides on a pattern, find the spelling, position, casing,
  quoting, whitespace, or boundary just outside its match.
- Where a mechanism computes a value (a count, a rate, a derived state), try to
  make it produce the wrong value — or to move the value by changing only the
  data it reads.
- Where a mechanism claims to catch a class of failure, construct a member of
  that class it does not catch.
- Report **only** what you proved by execution. "I reason it might…" is not a
  finding. An empty result on a mechanism you genuinely tried and failed to
  break is itself a valid, valuable result — say so.

## Output

Per mechanism: proven bypasses (the payload, the exact command you ran, the
observed exit code and output), proven false-positives (same), and any behavior
the mandate implies must be enforced that you demonstrated is not. Rank by how a
confused agent would actually trigger it in normal use. No commentary on
quality — holes with reproduction, or silence.

## Deliberately withheld

You have not been told what changed, what holds, what the author is unsure of,
or where to look hardest. That withholding is load-bearing. If anything in this
brief lets you infer what the author was proud of versus nervous about, the
brief is defective — name the leak and discount it.
