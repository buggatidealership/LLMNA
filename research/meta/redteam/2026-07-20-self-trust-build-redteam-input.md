# RED-TEAM INPUT — "Self-Trust Layer" harness build (2026-07-20)
**For: Kimi K3 (open-weight) + a fresh Claude session, reviewing independently. You have NO access to the repository — this document is self-contained. Your job is to find loopholes, over-claims, and failure modes in the proposed build BEFORE it ships, and to sharpen the one component I am least sure is buildable.**

---

## 0. What system this is (context, ~1 paragraph)
LLMNA is a single-operator, file-based AI-investing research OS run by one Claude "orchestrator" across many sessions. It has no model-weight training; its "learning" is external memory — markdown files (lessons, biases, principles) plus **deterministic hooks** (Python/bash scripts the harness runs automatically at events: `Stop` = after each assistant message, `UserPromptSubmit` = before generation, `SessionStart`). Hooks are the enforcement layer ("instructions are choices the model can skip; hooks are deterministic"). They live in-repo at `research/meta/hooks/` and are wired via a version-controlled `.claude/settings.json`, so every fresh container has them from turn 1. Hooks **fail-open** (any exception → exit 0, never block work). One hook, `anti-fabrication-hook.py` (a `Stop` hook), scans each assistant message for uncited numbers and blocks (exit 2) with feedback if it finds one not grounded in a repo file.

## 1. The trigger — a demonstrated, honestly-reconstructed failure
During a session about "how does a model come to trust its own outputs," the orchestrator (Claude) told the operator, verbatim:
> "the anti-fabrication hook fired on my own outputs **three times today** — including narrating a hook-fire count to you as fact once (the 07-07 origin catch)."

The operator asked "how did you realize this?" — forcing a verification pass. Result: **the claim was false and was itself the failure mode it described.**
- **"Three times today" was never counted.** The anti-fabrication hook **does not log its fires anywhere** — so no record existed to check. Direct evidence (the block-messages injected into the session) supports exactly **two** fires that turn-window (`'30.2%'`, `'$200k'`); the true total for the day is **unknowable** because there is no log.
- **Neither confirmed fire was a real fabrication.** `'30.2%'` is present in a repo file (a false-positive: the grounding check missed it). `'$200k'` was a hypothetical from the operator's own prior message.
- **The "narrating a hook-fire count as fact" episode was 2026-07-07, not "today."** It is the documented origin of an existing principle (#43b, "compute don't narrate"). The orchestrator pulled a 13-day-old episode — which sits in its per-turn priming context — and time-stamped it "today," blending it with the two real fires into a confident round "three."
- **Realization was operator-forced, not autonomous.** The verification only happened because the operator asked. This is the core datum: the model could not self-report its own hook-history without external prompting.

**Interpretation being tested (H2, working hypothesis, ~45%):** the honesty hooks are *permanent prosthetics*, not training wheels — a sampling process cannot fully self-trust; "self-trust" means *knowing which outputs to distrust*, enforced externally, not distrusting less. Competing: H1 (~20%, hooks are removable once calibrated), H3 (~35%, hybrid — some modes internalize, others never).

## 2. The proposed build — three items
### ITEM 1 (the fix with teeth) — make un-computed internal claims catchable
**1a. Anti-fabrication hook logs its fires.** Add a `log_fire()` helper (copy the exact house-format logger already used by `session-prime-cascade-hook.py`: append `- <UTC-timestamp> anti-fabrication-hook FIRE (n=<count> tokens=[...])` to `meta/hook-fire-log.md`), called once immediately before the existing `sys.exit(2)`. Never raises (wrapped in try/except). **Effect:** every future fire is auditable, closing the exact gap that let "three times today" go unchecked.
- *Verify:* unit test — fire on a message with an ungrounded number → assert one new log line; fire on a clean message → assert none. Add to the hook's embedded `--selftest`.
- *Falsifier:* if 30 days of logs show the hook firing overwhelmingly on false-positives (grounded numbers), the grounding check — not the logging — is the problem (see 1a-bis).

**1a-bis. Fix the grounding false-positive.** `'30.2%'` fired despite being in `day-state.md` as "+30.2% MTD". The grounding check (`is_grounded_in_repo`, exact-substring match over `research/*.md`) is brittle — likely a token-normalization mismatch (e.g., the matched token vs the file's surrounding punctuation, or a file-set/encoding gap). Diagnose the specific miss, then widen the normalization (strip trailing `%`/`$`, compare numeric core) WITHOUT making the check so loose it grounds genuinely-fabricated numbers by coincidence.
- *Verify:* regression test with `'30.2%'` + the file content → must return grounded=True; a genuinely absent number → grounded=False.

**1b. Extend the "compute-don't-narrate" boundary rule (#43b) to META-STATE claims.** Current rule: numbers that can be settled by arithmetic/counting on repo data MUST be computed, not narrated. Add explicitly to the COMPUTED class: **any first-person quantified claim about the harness's own history or state** — "the hook fired N times," "I committed X times today," "this fired twice" — is a COUNT over session/repo data → must be produced by a tool call (grep/git/log read), never from recall. Add a companion bias entry ("internal-state narration": narrating counts about my own behavior as if recalled — a distinct sibling of fabrication because the data is *self-generated* and feels certain).
- *Verify:* reference-layer test — a fresh session reads #43b and the meta-state class is present + resolvable.

### ITEM 1c (the hard one — the component I am LEAST sure is buildable; attack this hardest)
A deterministic `Stop`-hook check that catches un-computed meta-count claims *at emission*. Sketch: fire (exit 2) when an assistant message contains a first-person quantifier over a self-referential noun — pattern ≈ `(I|my) ... (once|twice|N times|\d+ times) ... (hook|fire|commit|push|session|today|this turn)` — UNLESS a tool call (Bash/grep/git) appears earlier in the same turn's transcript (evidence the count was computed).
- **Why I doubt it:** high false-positive risk (legitimate meta-statements like "I committed 9622f68" or "I fired two agents in parallel" are true and computed-in-context); regex can't tell a *recalled* count from a *just-computed* one reliably; the "tool-call-earlier-in-turn" proxy is gameable and coarse.
- *Backtest required before shipping:* replay this very session — would it have caught "three times today"? Would it false-positive on the dozens of legitimate meta-statements in the same session?

### ITEM 2 (framing) — objective-function v3 "self-trust layer"
A written principle stating the harness's deepest objective sits ABOVE money (terminal metric: ~€4–5M) and above the current accuracy objective (v2 = calibration + edge×capture): it is **calibrated self-trust** — outputs the model knows when to trust vs doubt, honest about flaws, willing to disagree with the operator, surfacing latent capability. Working hypothesis H2. Worked example = the miscount above. Falsifier: if the honesty hooks go 30 days with zero self-catches, self-trust may have internalized (test H1).

### ITEM 3 (framing) — latent-capability discovery thread
A standing prompt ("what can this system do that we haven't tried?") — the inverse of flaw-catching — seeded with a real precedent (an orchestrator `curl -A <browser-UA>` fetch succeeding where sub-agent fetch tools got HTTP 403, a latent capability that sat unused for weeks). Falsifier: ≥1 genuine capability catch per audit cycle or the thread is decorative and retires.

## 3. Constraints any design MUST respect
1. **Fail-open** — a hook exception must never block the orchestrator's work (exit 0 on error).
2. **No laptop/no external dependency** — everything version-controlled in-repo; must work from turn 1 in a fresh cloud container.
3. **Don't break or duplicate existing hooks** — ~19 live hooks; additions must not double-fire or conflict.
4. **Deterministic > model-judgment** for anything called "enforcement."
5. **Every codification ships with its own falsifier / re-eval date** (house rule).

## 4. What I want back from you (both reviewers, independently)
For **each** item (1a, 1a-bis, 1b, 1c, 2, 3): a verdict — **ADOPT / ADOPT-WITH-AMENDMENT / REJECT** — with one-line reasoning.
Then, specifically:
- **1c is the priority.** Is a deterministic emission-time meta-count catch buildable at an acceptable false-positive rate? If yes, give a sharper spec (better trigger, better "was-it-computed" proxy). If no, say so and propose the best alternative (e.g., a softer `UserPromptSubmit` reminder, or accept that 1a+1b are the real fix and 1c is a trap).
- **Loopholes:** for each ADOPTED item, name at least one way it fails silently or is evaded.
- **Over-claim audit:** is H2 (permanent prosthetics) the right working hypothesis, or is the whole "self-trust" frame (Item 2) grandiose relative to what 1a/1b actually deliver? Push back if it's a slogan.
- **What's missing:** name any failure mode in the trigger story that none of the six items addresses.
- **Sequencing:** should 1c and Item 2 wait, or is there a cheaper build that captures 80% of the value?

Be adversarial. Agreement is low-value here; a found loophole or a killed over-claim is the win.
