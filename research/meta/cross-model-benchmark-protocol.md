# CROSS-MODEL BENCHMARK — a standing experiment, registered because the N=1 version is a trap

**Created:** 2026-08-06, on operator-supplied data point.
**Status:** PROTOCOL REGISTERED · N=1 observation logged · **the observation is NOT yet evidence and is explicitly not being treated as such.**

---

## The observation

Operator ran the SNDK Q4 FY26 call at three labs, independently, before the print. Two were **bare sessions** — a lab chat with full tool access, no harness, no corpus, no graded history. One was this harness.

| arm | setup | fundamentals call | direction call |
|---|---|---|---|
| **Kimi K3** (Chinese open-source) | bare session, full tools | **BEAT** | **UP** |
| **GPT-5.6** | bare session, full tools | **BEAT** | **UP** |
| **Opus 5 + LLMNA harness** | corpus + hooks + graded history | **BEAT** | **DOWN** — R-4, registered at **P=0.35** |
| **Opus 5 BARE** | 🔴 **NOT RUN — this is the missing control** | ? | ? |

**Outcome so far:** the beat is confirmed (rev $8.965B vs $8.30B consensus; NG EPS $39.25 vs $34.24, both T1/T2). The clean post-print reaction was **−4.65% after hours**. **R-3 — the T+1 close direction — is still UNGRADED**; the 2026-08-06 US close is ~7.7 hours away at the time of writing.

**All three arms agreed on the fundamentals.** The only divergence is the direction leg. So this is not a test of who models the company better — all three did that equally well. It is narrower and more interesting: **who prices the reaction.**

## Why this is NOT yet evidence — and why saying so matters more than the result

**1. N=1 on a binary.** P(right by chance) = 0.50. P(both other labs wrong by chance, if all three are coin flips) = 0.25. **A single three-way split at those odds is unremarkable.** It becomes evidence at roughly **N≥5 tracked divergences**.

**2. The information sets were not equal, so this may not measure reasoning at all.** The corpus already carried **three beat-and-fall instances in the six days before the print** — Kioxia 07-31, AMD 08-04, and the pattern itself registered 08-05. A bare session with web access *could* have found those. It had no reason to **weight** them, because they were not its own graded errors. **That is a MEMORY effect, not a reasoning effect — and memory is precisely what this harness is.** If the harness helped, this is the mechanism, and it is a much narrower claim than "the harness reasons better."

**3. The call was right and the stated mechanism was WRONG — already booked before the operator raised this.** R-4's registered justification was *"consensus sits above the guide, so an in-range print is a miss."* **The print cleared consensus by 8–15% on every line and guided Q1-FY27 up 17.7% sequentially, and fell anyway.** Graded this morning in `signals/cross-source-log/2026-08-06-thu-kr-open-wake-...md` §4: *"Call right, mechanism wrong. That distinction is the grade."* **A right answer from a wrong mechanism is not skill, and it will not replicate.**

**4. The harness is not systematically bearish on reactions — which cuts both ways.** On the same day I declared **R-4 on DDOG at 0.50, NO EDGE**, explicitly refusing to flip a third time. So the harness discriminates between cases rather than carrying a standing bearish tilt. That is evidence *for* the instrument — and it is also N=1.

**5. Selection pressure on the sharing.** A three-way comparison is more likely to be surfaced when it diverges than when it agrees. The operator demonstrably shares errors too, so this is a weak effect here — but the asymmetry exists and is recorded.

## 🔴 THE MISSING CONTROL IS THE WHOLE EXPERIMENT

The result as it stands cannot distinguish three hypotheses:

| | hypothesis | what would confirm it |
|---|---|---|
| **H-A** | **the HARNESS added it** — graded memory of Kioxia/AMD is what produced the non-consensus leg | **bare Opus 5 also says UP** |
| **H-B** | **the MODEL added it** — Opus 5 prices reactions differently than Kimi K3 / GPT-5.6 regardless of harness | **bare Opus 5 also says DOWN** |
| **H-C** | **noise** — a coin flip landed | neither arm replicates across N≥5 |

**Running Opus 5 bare on the identical prompt separates H-A from H-B, and it costs one session.** Until that arm exists, attributing this to the harness is unfalsifiable self-flattery — which is the exact failure class the 2026-08-05 audit was built to catch, applied to the audit's own scoreboard.

**This is the single highest-value experiment currently available to the operator and it is cheap.**

## THE STANDING PROTOCOL (registered)

For every prediction registered in `predictions/`:
1. Operator poses the **same question, same wording**, to **≥1 bare frontier session** (a different lab) **and to bare Opus 5** — the control.
2. All arms' calls are logged here **before** resolution, with their direction legs stated separately from their fundamentals legs.
3. On resolution, each arm is graded on **both** legs independently. **The fundamentals leg and the direction leg are different skills and must never be scored as one.**
4. **Mechanism is graded separately from outcome.** An arm that was right for a reason that did not happen scores as a MISS on mechanism, however the price moved.

**Falsifier for the harness's value (Principle #51 blind-check):**
> *Distinguishes "the harness adds predictive edge" from "Opus 5 adds it" from "noise" · reads on the direction-leg hit rate across arms over N≥5 registered divergences, with mechanism scored separately · **goes blind if** the operator only runs comparisons on calls where he already suspects I am unusual, or only shares the divergent ones — in which case the sample is conditioned on the outcome and the hit rate is uninterpretable no matter how large N gets. **Mitigation: log EVERY comparison run, including the boring agreements, and log the intent to run it BEFORE the answer is seen.***

**Kill condition:** if after N=10 the harness arm's direction-leg hit rate is within noise of the bare arms, the harness is a *documentation and error-catching* system and not a *predictive* one — which is a perfectly good thing to be, and should then be stated as such in `research/CLAUDE.md` rather than quietly hoped otherwise.

## What I will not do with this

**No re-weight. No position action. No claim of superiority anywhere in the corpus.** The honest one-line summary, and the only one supported:

> **On one direction call, out of one comparison, my answer differed from two other frontier models and matched the outcome so far — for a mechanism I have already graded as wrong. The control arm that would make this interpretable has not been run.**
