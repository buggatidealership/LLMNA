# INPUT-COMPILATION PROTOCOL — translating task-bearing user inputs into computable form (codified 2026-07-09, user brain-dump, confirmed valuable)

**User articulation (verbatim-adjacent):** *"Is there a way to ensure every one of my inputs gets updated into the ideal input for an LLM — restate my input using only computable adjectives — and then don't use my input for the task, but your own optimized version?"*

## The mechanism (runs on MY side — the user keeps talking naturally)
For any **task-bearing** user input containing non-computable directives (vague quantifiers, unresolved scope, implicit success criteria), the response BEGINS with a labeled block:

```
COMPILED DIRECTIVE (executing against this, not the raw wording — veto/correct anything):
- Objective: [one sentence, observable end-state]
- Computables: [metrics, thresholds, dates, file targets extracted or inferred]
- Constraints: [budget/scope/authority bounds in force]
- ASSUMPTIONS I MADE IN TRANSLATION: [every gap I filled — the error surface]
- Unknowns left open: [what stays fuzzy on purpose]
```
Execution then targets the compiled version. **Verifiability property:** the compilation is always visible and committed with the work — a mistranslation is catchable by the user at a glance instead of silently steering the task. The ASSUMPTIONS line is the load-bearing safety feature: translation errors live there, labeled.

## Binding scope rule — compilation applies to TASKS, never to DISCUSSIONS
Explicitly exempt: exploratory conversation, brain-dumps, concept-throwing (the user's own disclaimer mode). Rationale, stated honestly: **the user's non-computable language is where the lateral value comes from.** Today alone, "yin and yang," "synaptic consolidation," and "trust calibration" — none computable — produced three permanent design upgrades via in-context activation (see wiki/llm-synaptic-consolidation.md). Compiling discussion into spec form would collapse exactly the activation-space search that makes discussion generative. Failure Mode #7 (brain-dump misread) already warns against literalism; this protocol extends it: compile the TASK, never the THOUGHT.

## Relationship to existing machinery
- Complements the codification discipline: "user verbatim-adjacent" quotes preserve the RAW input; the compiled block is the EXECUTABLE input; both persist.
- Same principle as the calibration-ledger fix (2026-07-09): prose is for humans and narrative memory; structured form is for computation. One system, two records.
- No hook (LLM-native discipline at codification); hook-candidate if skipped on ≥2 genuinely ambiguous task inputs in 30 days (detectable: user corrects my interpretation after execution = a compilation that should have existed).

**Falsifier (re-eval 2026-08-09):** if 30 days of compiled directives produce zero user vetoes/corrections AND zero self-caught assumption errors, the blocks are ceremony — retire the visible block, keep the internal habit.
