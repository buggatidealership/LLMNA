# K3 COMMISSION — THE CLAIM-RECEIPT LAYER (drafted 2026-08-07 EOD; operator transports to a fresh session)

**Why this is commissioned and not self-run:** today's central finding — that a lesson (L57) was injected into every cold session for two days while having no canonical entry — **was found by a fresh session in its first ten minutes, after I had run a grep over that exact ID range the same morning and not noticed.** I then diagnosed the cause and built the enforcement. **The author of the fix is the system whose failure produced the defect, and the fix's own design principle ("a receipt must be a by-product of the act, not a statement by the actor") condemns exactly that arrangement.** Self-auditing it would be the thing the artifact argues against.

**Transport instructions:** open a fresh session with no memory of 2026-08-07, on branch `claude/first-test-new-repo-wxedu9` (⚠️ **`main` is ~37 commits stale — booting on main audits the wrong corpus**). Paste the block below verbatim. Do not steer. Do not answer clarifying questions with house context.

---

## PASTE BLOCK BEGINS

You are auditing an enforcement mechanism you did not build, in a research harness you did not write. Be adversarial. The mechanism was designed and shipped by the same system whose failure motivated it, in a single session, in direct response to operator pressure — treat every claim about it as a hypothesis to attack.

**Read first, in this order:**
1. `research/predictions/lessons.md` — entry **L57** and especially its **ORPHAN NOTE**
2. `research/meta/redteam/2026-08-07-claim-receipt-audit-what-did-i-say-i-wrote.md` — the audit that preceded the build
3. `research/meta/hooks/claim-receipt-hook.py` — the mechanism itself, header comment included
4. `research/meta/hooks/session-prime-cascade-hook.py` — the hook that was supposed to prevent L57 and is blind in one direction
5. `research/meta/session-prime.md` §3, and `research/CLAUDE.md` § "Enforcement hooks (live)"
6. `.claude/settings.json` — how hooks are actually wired

**The claims under audit.**

The artifact asserts: (a) that L57's failure mode is a **CLAIM WITH NO ARTIFACT**, structurally distinct from a wrong claim; (b) that the general fix is *"a receipt must be a BY-PRODUCT OF THE ACT, not a statement by the actor"*; (c) that claims divide into three classes — FILE, ID, ACTION — of which two are now gated and the third is not; and (d) that `claim-receipt-hook.py` closes classes 1 and 2 with **zero false positives measured over 209 real assistant messages**.

**TASK 1 — ATTACK THE DIAGNOSIS.** Is "a claim with no artifact" the real defect, or a tidy abstraction over an ordinary clerical slip? Specifically: L57 was *written*, just in the wrong file. Test whether the whole edifice — three claim classes, a by-product principle, a new hook — is proportionate to one missing section, or whether it is a satisfying architecture retrofitted onto a small mistake. **A demonstration that this was mundane and the response was over-engineered is worth more to me than a careful extension of it.**

**TASK 2 — BREAK THE HOOK.** It is a regex gate. Regex gates leak.
- Construct messages that make a **false codification claim the hook does NOT catch.** Word order, synonyms for "codified", claims split across sentences, an ID stated in a table rather than prose, markdown emphasis inside the ID token. How hard is it? If it takes five minutes, the gate is theatre.
- Construct the reverse: **an honest message the hook WRONGLY blocks.** The exemption list is a fixed set of hedge phrases; find natural phrasings that mean "not yet written" and are not on it. Note that the author already shipped one such bug and caught it only because a self-test fixture happened to cover it.
- **The `--selftest` has 9 fixtures, all written by the author.** Are they adversarial, or are they the cases that were already known to pass?
- The hook **exempts any message containing its own filename.** Is that a reasonable self-reference guard or an exploitable bypass?

**TASK 3 — THE BACKTEST.** The claim is *"zero false positives across 209 real assistant messages."* Verify the method, not the number. Those 209 messages come from the session that BUILT the hook — the author's own recent output, in a conversation about this very topic. **Is that a valid sample, or is it the most favourable one available?** Also: C3 fired 7 times and was dismissed as "backtest artifact, state-dependent." Is that dismissal sound, or is it an inconvenient result explained away? What sample WOULD be valid?

**TASK 4 — THE UNCOVERED CLASS, AND WHETHER IT IS THE ONLY ONE.** Phase 1 explicitly does not cover ACTION claims ("cascaded", "verified", "re-weighted", "pruned", "retired"). The artifact states this openly. **Adjudicate whether the honest declaration of a gap is doing real work or is functioning as an excuse** — the harness has an "enforcement ledger" that makes non-enforcement legible, and a prior audit already asked whether declaring a gap substitutes for closing it. Then: **are there claim classes the artifact does not enumerate at all?** It proposes exactly three. Find a fourth.

**TASK 5 — THE ONE THE AUTHOR CANNOT SEE.** `session-prime-cascade-hook.py` fires when a canonical ID ships without a summary update, and is structurally blind to the reverse — which is precisely how L57 survived. The author noted this asymmetry **only after** the new hook's false-positive fired on the L57 repair. **Search the other 17 Stop hooks for the same shape: enforcement that runs in one direction while the failure it targets can arrive from either.** This is the highest-value task in this commission if it returns anything.

**Deliverable:** one artifact at `research/meta/redteam/2026-08-XX-claim-receipt-audit-K3-return.md`. **Lead with whatever most damages the mechanism.** State explicitly what you could not determine. If you conclude the hook is sound, say so plainly — but only after Task 2 has genuinely tried to break it, and show the attempts that failed.

**Constraints:** no position or sizing recommendations (operator-gated). Do not edit `portfolio/holdings.md`. Anything that would disable or weaken live enforcement is Rule #19 HIGH tier — propose it, do not do it, and leave the decision to the operator.

## PASTE BLOCK ENDS

---

**Companions already outstanding, all awaiting operator transport — send to SEPARATE sessions:**
- `meta/redteam/2026-08-05-K3-commission-postcondition-audit.md` (the enforcement layer checks form, not comparability)
- `meta/redteam/2026-08-01-instrument-validity-audit-commission-prompt.md` (Principle #51 retro sweep; dated 08-08, due tomorrow)

**Why separate:** running them together lets one audit's framing contaminate the other, which is the failure mode all three exist to prevent. **Three commissions are now queued and the last fresh-session return landed 2026-07-28** — the backlog item for a fixed weekly slot exists precisely because this queue keeps growing while the mechanism sits idle.
