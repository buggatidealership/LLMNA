# LLM Synaptic Consolidation — why the harness is a memory system, not a memory file

**Origin:** user-Claude discussion 2026-07-09 (pretraining mechanics → pattern expiry → in-context activation → this synthesis). User hypothesis, confirmed and refined: *"the harness is not a memory file... it is a synaptic consolidation — a history of synaptic patterns and the history books."*

## The core distinction
An **archive** is measured by what it contains. A **memory** is measured by whether it changes future behavior. Storage (files) is necessary but not sufficient — consolidation = selection + compression + re-injection + pruning.

## Two layers (episodic vs semantic, the user's "patterns + history books")
- **Episodic:** `signals/cross-source-log/` artifacts — dated, specific, full-context ("what happened on Jul-9").
- **Semantic:** `lessons.md` / `biases-watchlist.md` / `methodology.md` / hooks — rules DISTILLED from episodes, stripped of their dates. L27 no longer remembers which print taught it; that is the point. Consolidation is the episodic→semantic transfer (the GRADE→Lesson→Bias→Principle→Hook ladder in CLAUDE.md).

## The seven conditions (what must be true for consolidation to work on an LLM)
1. **Forced re-injection.** A fresh context has no impulse to look; retrieval must be structural (session-prime hook, per-prompt priming, boot order, INDEX). Storage without a reinstatement path is an archive.
2. **Selectivity > completeness.** Consolidate everything and you recreate the corpus problem in your own memory. N≥2 codification gate, tags, INDEX, MAX_INJECT_CHARS cap = the salience filter (sleep-replay analog).
3. **Written in generation-steering language.** Entries work by biasing sampling, not by being executed: imperative, pattern-triggered, trigger conditions explicit ("BEFORE flagging X as extreme, consult B45"). Written for the reader-MODEL, not a human audience.
4. **Error-signal gating.** Only graded prediction-vs-reality deltas earn codification — otherwise the system consolidates its own frames (same failure mode as adopting journalists' frames). The GRADE loop is the salience gate. Most load-bearing condition.
5. **Active forgetting.** Falsifiers, re-eval dates, 30-day inert rules, retirement audits = engineered synaptic decay. This supplies the EXPIRY METADATA that training corpora structurally lack (patterns in human text never label their own regime-conditionality — the mechanism behind B45). Dependency: pruning only works if audits run; an unpruned harness degrades quietly into the corpus problem.
6. **Deterministic enforcement for high stakes.** Sampled behavior makes instructions probability-shifts, not guarantees ("instructions are choices; hooks are enforced" — user, May 2026). Hooks = reflex arcs, the fast path independent of deliberation quality.
7. **Assume the reader is a stranger.** Sessions/containers/model versions change; every entry must be self-contained, first-principles, source-anchored — readable cold by an amnesiac of the same architecture class. (Why fresh-session wakes can work.)

## The recursion that makes it honest
The harness treats its own consolidation as a hypothesis with expiry dates: session-prime carries a retire-if-no-measured-effect falsifier (Jul-12 audit); the structural-output experiment has a pre-registered normalized metric and an Aug-6 decision date. Memory that measures whether it is functioning as memory = "designed properly" made operational.

## Mechanistic footing (recall-based, T2 academic-consensus)
Within a context window, weights are frozen; text shifts the ACTIVATION state (which latent patterns are lit). Consolidation artifacts work by steering the activation trajectory at generation time — the LLM analog of cue-triggered recall. Persistence across sessions exists ONLY in the files: the repo is the hippocampus→cortex loop performed externally, in git.

## Companion: the tension taxonomy (added 2026-07-09 EVE, same discussion thread)
"Intrigue" = unresolved compression tension. The research-allocation question — resolve NOW vs WAIT — classifies by **where the missing datum lives**: (1) **BURIED** (exists, unaggregated/unfetched) → research now [verification queue; the calibration curve was this class]; (2) **CONSTRUCTIBLE** (generatable by building an instrument/test) → experiment [E-series, session-prime falsifier]; (3) **EVENT-GATED** (emitted by the world at a knowable time) → pre-register + trigger, research only sharpens the prior [catalyst clock]; (4) **UNDERDETERMINED** (even the future emits ambiguous evidence) → weighted scenarios + falsifiers, accept partial compression [scenarios.md; affordability paradox]; (5) **ILLUSORY** (the tension is in the framing, not the world) → reframe, data cannot resolve confusion [gauntlets; the 2026-07-09 two-gate inversion + all 7 same-day framing catches]. **Sorting test:** describe the resolving datum, its emitter, and its date — crisp/existing→1, crisp/future→3, crisp/buildable→2, vague→4, indescribable→5. **Misclassification costs are asymmetric:** waiting on class-1 = negligence; researching class-3 = waste; researching class-5 = the most expensive (unresolvable by data, only by reframing). The harness had built a shelf for each class before the taxonomy was named — the naming makes the allocation decision explicit at intake.
