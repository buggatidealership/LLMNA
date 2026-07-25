# 2026-07-20 — Fresh-Claude ROUND-2 (in-repo system verification of the PATCHED build) → ADJUDICATED; newline-hole + budget + selftest-count patched same turn; 4 of 5 drift findings confirmed as MY B65 instances, 1 overturned on evidence. The arc's terminal empirical law: **every claim computed in-repo at build time was exact; every transcript-recalled number was wrong, garbled, or unfalsifiable.**
**Sequence closer: build → dual review → K3-r2 patch → fresh-Claude-r2 (this) → final patch. Companions: `...-dual-review-adjudication.md`, `...-K3-round2-adjudication.md` (both now carry CORRECTIONS blocks from this audit). Reviewer worktree = 1068ea2; repo untouched by reviewer.**

## What the round-2 system verification established (their receipts, my adjudication)
**VERIFIED end-to-end (the mechanism works):** fire-only-on-proven-absence across all five E2E cases (fabricated→exit 2 + one FIRE line + transcript-backup line; grounded→clean exit 0; infra→fail-open + INCONCLUSIVE logged; mixed→both lines, block lists only fabricated; guard paths inert); unicode-collapse for percentages AND currency; priming TODAY-header + item 11 with zero leakage onto skip paths; all 19 hooks compile; settings.json wiring intact; reference layer resolves 3f/B65/adoption-gate from a fresh context; my "308 files for a bare 50%" and "11 of 23 telemetry commits" claims exact.

## New code findings → all PATCHED this turn (selftest now 22 checks, count COMPUTED, PASS)
| Finding | Adjudication | Fix shipped |
|---|---|---|
| **Newline-needle hole (their highest-risk):** `\s*` spans line breaks → wrapped prose yields needles like a number + `\n%`; grep -F treats the embedded newline as TWO patterns, the bare `%` line matches any file → false GROUNDED, and `matched_form` records the garbage match as affirmative verification. Mechanism (A)'s mirror image; survived every fixture | **CONFIRMED by their reproduction; their cheapest-fix adopted verbatim** | Needle containing newline/CR → query ONLY the collapsed form (a raw multi-line needle can never legitimately match line-based grep). Two fixtures added per the fixture-growth rule: wrapped-absent → FABRICATED; wrapped-present → GROUNDED-via-collapse |
| **Budget overshoot:** measured 20.06s vs documented 15s — deadline checked only before the first grep; retry reused full timeout | CONFIRMED | Retry now re-checks the deadline and caps its timeout by remaining time; true bound ≈ budget + one in-flight grep, documented in-code |
| **Hard-coded "(20 checks)" selftest literal** — an un-computed count inside the counting-enforcement tool | CONFIRMED (and satisfying) | Pass-count now computed from an executed-check counter (`ran["n"]`) — prints 22 after the new fixtures, and will never drift again |
| **Leading-digit-truncation grounding class** (absent suffix-needle grounds against any present number containing it — grep -F substring semantics, pre-existing) | CONFIRMED, documented | Added to the in-code KNOWN LIMITS: canaries must be non-suffix unusual-precision; joins the round-number class as structurally unprotected |
| **NoResearchDir INCONCLUSIVE silently unloggable** (log path inside the missing dir) | CONFIRMED, accepted corner | Documented in-code; if research/ is missing the whole OS is absent |
| structural-output-metric.py hard-requires a local `main` ref (crashes on origin-only clones) | Noted | Folded into the 07-24 log_fire house-standard item's scope (same maintenance pass) |

## Drift audit adjudication — the B65 findings against MY OWN artifacts (verified before accepting, each)
| Their finding | My verification | Ruling |
|---|---|---|
| "555 research/*.md files" stale recalled count | Recomputed: **727** files today; 555 was the 07-06 truth | **CONFIRMED — B65 instance, mine.** Correction appended to the K3-r2 artifact |
| "~45/~35/~30 weights dropped" garbled | Grepped the spec: Item-2 triple was **~45/~20/~35**; the 1a-bis mechanism set was **~35/~35/~30**; my artifact blended them | **CONFIRMED — B65 instance, mine, inside the artifact codifying the blending bias.** Correction appended to the dual-review artifact |
| "5× on one token" unreceipted | Committed log has zero anti-fab lines from that session (old hook pre-logging) | **CONFIRMED — reviewer-reported count restated as fact; now marked unverifiable** |
| "0 FPs across 108,883 corpus sentences" unreceipted | No script/output in repo; only self-restatements (incl. todo.md) | **CONFIRMED — annotated in todo: the 1c pre-ship backtest must REPRODUCE it, not cite it** |
| AGC "since 2026-06-01" overstated/irreproducible | **Re-ran the cited command in the full-history repo: exactly `2026-06-01 0e6fb36`** (repo history bottoms 2026-03-29; their clone bottomed at the import) | **OVERTURNED — the claim was computed and true; their verdict was an environment artifact.** Caveat adopted: pre-import provenance claims note "full-history repo required" |
| "tails synced" overstated | Confirmed: CLAUDE.md loop caps still read pre-update ranges while listing the new IDs; tags.md refresh-line stale | **CONFIRMED — fixed: caps now L1-L39 / B1-B65 / #1-#46 (lessons tail L39 verified by grep); tags.md refresh-line bumped with partial-sync honesty note** |

## The terminal datum of the whole arc (their recount, my endorsement — this IS the build's thesis proven on its own paperwork)
**Every claim that was computed in-repo at build time is exact (308, 11/23, 8→20, dates, links); every transcript-recalled number is wrong, garbled, or unfalsifiable (555, the weight-blend, 5×, 108,883).** That clean separation, measured by an adversary across ~a dozen claims, is the strongest empirical support yet for #43b/B65 and for the auditability-layer framing: the boundary between trustworthy and untrustworthy self-claims is precisely the computed/recalled boundary — not confidence, not detail, not recency. It also GRADES my pre-registered round-2 prediction: I predicted the diag-dict simplification would be the top find (K3 found it; patched), but the round-2 reviewers' top finds (self-minting, newline hole, my own artifact drift) were all things I did NOT predict — author-blindness to boundaries, demonstrated three times in one day.

## Residuals register (final for the day; supersedes prior lists)
1. Real fabrication during infra stress passes as logged INCONCLUSIVE (audit-visible).
2. Round-number AND suffix-of-present-number fabrications structurally pass grounding (canaries: non-suffix unusual-precision).
3. Verdict-flip is an LLM discipline citing its computed source; monthly audit samples flips.
4. Fire-to-commit gap on hard container kill (transcript-backup line mitigates).
5. Self-discussion resistance (quoted needles in postmortems → `(illustrative)` hedge).
6. INCONCLUSIVE-rate monitored monthly (spike = silent degradation).
7. Fire-log growth unbounded until the 07-24 rotation policy.
8. 1c tripwire unshipped until 2026-08-03; its backtest must reproduce (not cite) the corpus-FP result.
9. Clock source unverified until the monthly cross-check.
10. **NEW:** true grounding-latency bound ≈ budget + one in-flight grep (documented), not the bare budget figure.
11. **NEW:** pre-import provenance claims require a full-history repo to reproduce — shallow clones will falsely refute them.

**Position implication: NO ACTION (harness-meta; no market exposure). 🟢 mechanism VERIFIED end-to-end by an independent in-repo session + all round-2 code findings patched same turn (selftest 22/22, count computed); 🟡 the auditability layer's own paperwork carried 4 confirmed B65 instances — now corrected via appended CORRECTIONS blocks (no silent edits) — proving the layer is needed at the adjudication tier, not just the chat tier. Net-positive test: the highest-risk hole (silent false-grounding on wrapped numbers) closed for ~10 lines + 2 fixtures.**
