# Instrument-validity audit — fresh-session commission prompt

**Origin:** nominated in the 2026-07-31 EOD docket after the same defect surfaced twice in twelve hours; **written 2026-08-01** after the 07-31 docket's own promise (*"paste block draft below"*) turned out to be a promise with nothing below it — a say-do gap caught by tonight's EOD condition check, and itself a specimen for the open P1 receipts hook (G-07: *a header or status line is a PROMISE, not a receipt*).

**Scope widened on 2026-08-01** by a third specimen found in the **enforcement layer** rather than the research layer. The original nomination was "audit every live falsifier." That is now too narrow: hook kill-criteria and repair criteria are detectors too, and at least one of them has the identical defect.

**Why a FRESH session, not this one:** I built every instrument under audit and I graded every failure that motivated the audit. My own hand-labelled FP specimen from 2026-08-01 carries the same declaration — a self-grade from the flagged party is the weakest form of this evidence. An auditor with no authorship stake is the only non-self-correlated reader available.

**Delivery:** paste the block below into a fresh Claude Code session with this repo. Nothing else — no follow-up steering.

**Length choice:** this is written in the LIGHT style established by `2026-07-25-overconstraint-audit-commission-prompt-v2-LIGHT.md`, after the operator's critique that the long form injects too many of my preconceived notions and pre-decides the answer shape. The three specimens below are given as *dated facts*, not as a theory of the defect — the auditor is expected to find its own shape, including the shape where I am wrong that these three are the same thing.

---

## THE PROMPT (copy from here)

You have full authority and full autonomy over this task. I am not going to tell you how to do it.

**The task:** this repository is a research operating system that runs on detectors — falsifiers attached to theses, kill criteria attached to codifications, repair criteria attached to enforcement hooks, triggers attached to predictions. Audit them for one property: **can the detector still detect?**

**Three dated specimens, given as facts rather than as a theory:**

1. **2026-07-31** — a falsifier written for the KIOXIA thesis could not fire inside its own resolution window. It was not wrong. It was unfireable.
2. **2026-07-31** — a falsifier keyed to "a hyperscaler cuts capex" went blind when Microsoft held capex guidance flat while adding $132.5bn of not-yet-commenced lease commitments in one quarter ($196.6bn → $329.1bn). The spending did not stop; it moved off the line the detector watches.
3. **2026-08-01** — the `macro-anchor-hook` carries a pre-registered repair criterion, *"if false-positive rate >30% → tighten exemption list."* Its log records the fire reason and never the triggering message, so the FP rate cannot be computed from the data the hook collects. The criterion has been un-adjudicable through two scheduled reviews.

Specimens 1 and 2 are research-layer. Specimen 3 is enforcement-layer. **Whether those are one defect or three unrelated things is your call, not mine** — I am the author of all three and I have an obvious interest in them being one tidy pattern.

**What I want back:** an inventory of live detectors in this repo, and for each one, whether it can still register the event it was built for. Where it cannot, say what changed — the world, the accounting, the instrument, or the detector's own logging. Rank by what it would cost us to keep trusting it.

**Compute, don't recall.** This repo carries its own evidence: `research/predictions/`, `research/companies/*/thesis.md` falsifier blocks, `research/meta/hooks/` with `meta/hook-fire-log.md`, `research/meta/methodology.md` fluidity metadata, git history. Do not tell me a detector is blind; show me it computed. Where the evidence needed to adjudicate does not exist in the repo, **that absence is itself a finding** — specimen 3 is exactly that case, and I would rather you find five more of those than force a verdict on thin data.

**Adversarial clause:** the strongest thing you can return is evidence that this audit is unnecessary — that the three specimens are unrelated, that the detector population is mostly healthy, and that a sweep would burn context for nothing. I will take that answer. Do not build a case for me.

**Out of scope:** no position or sizing recommendations. Do not modify any file under `research/portfolio/`. Live enforcement files (`research/meta/hooks/*.py`, `.claude/settings.json`) are **read-only for this audit** — propose changes, do not ship them; that is a Rule #19 gate the operator holds.

(copy to here)

---

## Pre-registered falsifier for this commission itself

- **POSITIVE:** the audit returns ≥1 blind detector I did not already know about, or credibly refutes the premise that specimens 1-3 share a mechanism.
- **NEGATIVE:** it returns a restatement of the three specimens I handed it plus generic advice. That means the prompt injected the answer and the specimens should have been withheld.
- **If NEGATIVE:** re-run once with the specimens removed entirely — task text only — and compare. That A/B is the same design as the 07-25 LIGHT-vs-long comparison and would give the harness a second datapoint on whether specimen-injection helps or contaminates.
