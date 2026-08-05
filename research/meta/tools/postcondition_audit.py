#!/usr/bin/env python3
"""N1 — restate every Critical Rule as a POSTCONDITION and classify it.

The 2026-08-05 root-cause artifact (§11) claims the harness's defect is that
every discipline specifies an ACTION and none specifies a POSTCONDITION, and
proposes rewriting all of them. This script is that rewrite, held as data so the
tally is COMPUTED rather than narrated — the discipline of priming item 10/11,
applied to the audit of the priming items.

The classification that matters is NOT machine-vs-human. It is:

  PRESENCE  — the check passes when a TOKEN appears in the output. "Contains a
              Position implication line." "Contains a citation." "Contains a
              1st/2nd/3rd-order marker."
  RELATION  — the check passes when TWO THINGS IN THE OUTPUT AGREE. "The
              falsifier cited in the EXIT line is one of the falsifiers actually
              written in that thesis." "The two dates on a recycled signal
              differ." "Both operands of a comparison declare the same basis."

This distinction is the whole result. Every hook in the harness today is a
PRESENCE check. All 8 errors of 2026-08-05 were produced with every relevant
token present — cited numbers, tagged claims, correct form — and a false
relation underneath. A rewrite that converts 20 action-rules into 20 presence-
postconditions therefore changes nothing, which would FALSIFY N1 as stated.

Run: python3 research/meta/tools/postcondition_audit.py
     python3 research/meta/tools/postcondition_audit.py --md   (artifact table)
"""
import sys

# (rule, short title, postcondition, kind, checker, backing hook or "" )
#   kind:    PRESENCE | RELATION | UNCHECKABLE
#   checker: MACHINE | HUMAN | NONE
RULES = [
    ("1", "facts vs interpretations",
     "no line in any companies/*/facts.md contains an interpretive verb "
     "(means, suggests, implies, likely, bullish, bearish, I read)",
     "PRESENCE", "MACHINE", ""),

    ("2", "read lessons.md before predicting",
     "every predictions/*.md cites >=1 lesson ID, AND the cited lesson's "
     "subject matches the prediction's failure mode",
     "RELATION", "HUMAN", ""),

    ("3", "name the source of 'consensus'",
     "every consensus/street/analysts-expect claim has a named source within "
     "the same sentence",
     "PRESENCE", "MACHINE", ""),

    ("4", "TRACE on cross-domain events",
     "every signals/events/*.md carries 1st/2nd/3rd-order markers",
     "PRESENCE", "MACHINE", ""),
    ("4t", "TRACE — the trigger, not the form",
     "every event WITH cross-domain reach got a file at all (the decision to "
     "file is the rule; nothing observes events I never noticed)",
     "UNCHECKABLE", "NONE", ""),

    ("5", "bottlenecks.md last_review",
     "last_review in bottlenecks.md == the date of the commit that touched it",
     "RELATION", "MACHINE", ""),

    ("6", "segment-classify before triangulating",
     "every triangulation.md entry names the segment of each of its sources, "
     "AND all named segments are identical",
     "RELATION", "MACHINE", ""),

    ("7", "never fabricate numbers",
     "every numeral is cited, computed in-message, hedged, or exact-string "
     "grounded in the repo",
     "PRESENCE", "MACHINE", "anti-fabrication-hook"),
    ("7b", "L58 clause — never compare across bases",
     "both operands of every comparison declare the same basis (reference "
     "point, date, category, season, window, denominator incl. day count)",
     "RELATION", "HUMAN", ""),

    ("8", "no sell on macro without falsification",
     "every EXIT/TRIM names a falsifier that is literally present in that "
     "ticker's thesis.md falsifier block",
     "RELATION", "MACHINE", ""),

    ("9", "bypass-route thinking",
     "every binding-constraint claim is followed by a named bypass route or "
     "an explicit statement that none exists",
     "PRESENCE", "MACHINE", "bypass-route-hook"),

    ("10", "cascade cross-source synthesis",
     "every ticker named in a synthesis artifact has a back-reference to that "
     "artifact in its thesis.md within the SAME commit",
     "RELATION", "MACHINE", "cascade-enforcement-hook"),

    ("11", "thesis -> position translation",
     "every modified thesis.md ends with a Position implication line in the "
     "mandated form",
     "PRESENCE", "MACHINE", ""),
    ("11b", "the line must carry decision content",
     "the Position implication is not the 5th consecutive identical "
     "'HOLD — no size change' with rote rationale",
     "RELATION", "HUMAN", ""),

    ("12", "temporal freshness before cascade",
     "every T2/T3 signal states TWO dates — the aggregator's and the "
     "underlying primary claim's — and they are visibly distinct fields",
     "RELATION", "MACHINE", ""),

    ("13", "codification trigger",
     "when a chat-only output met a trigger, a file changed in the same turn",
     "UNCHECKABLE", "NONE", ""),

    ("13b", "blind-check on every detector",
     "every detector line in the corpus is followed by a Blind-check line "
     "carrying all three clauses (distinguishes / reads on / goes blind if)",
     "PRESENCE", "MACHINE", ""),

    ("14", "signal-density detection",
     "every new cross-source-log file either updates a TC-N entry or records "
     "the skip together with the search that justified it",
     "PRESENCE", "MACHINE", ""),

    ("15", "macro-first, research-vs-recall",
     "position-relevant output carries a date-anchored first-principles line "
     "and research-verified-vs-recall tags on load-bearing claims",
     "PRESENCE", "MACHINE", "macro-anchor-hook"),

    ("16", "always run verification subagents",
     "every commit that cascades external data has a matching same-commit "
     "entry in meta/subagent-cost-yield-ledger.md",
     "RELATION", "MACHINE", ""),

    ("17", "ensemble high-stakes calls",
     "every sizing-consequential number reports N and the observed spread, "
     "not a collapsed point estimate",
     "PRESENCE", "MACHINE", ""),

    ("18", "standing dissent mandate",
     "every thesis conclusion contains a falsifying-case section, or states "
     "that none was found, before the conclusion",
     "PRESENCE", "MACHINE", ""),
    ("18b", "and it must be the STRONGEST one",
     "the falsifying case argued is the strongest available, not the weakest "
     "one that is easy to dismiss",
     "UNCHECKABLE", "NONE", ""),

    ("19", "destructive-change governance",
     "no HIGH/CATASTROPHIC-tier operation reaches git without a matching "
     "OPERATOR_APPROVED token issued BEFORE the operation",
     "RELATION", "MACHINE", "git-guard-pretooluse"),
]


# Clauses that are a SECOND postcondition on an existing rule rather than a
# rule of their own. Enumerated, because it is not derivable from the ID.
SPLIT_IDS = {"4t", "7b", "11b", "18b"}


def main():
    md = "--md" in sys.argv
    kinds, checkers, hooked = {}, {}, 0
    for _, _, _, kind, checker, hook in RULES:
        kinds[kind] = kinds.get(kind, 0) + 1
        checkers[checker] = checkers.get(checker, 0) + 1
        if hook:
            hooked += 1

    if md:
        print("| Rule | Postcondition (the end-state, not the action) | Kind | Checkable by | Hook today |")
        print("|---|---|---|---|---|")
        for rid, title, post, kind, checker, hook in RULES:
            print(f"| **#{rid}** {title} | {post} | {kind} | {checker} | "
                  f"{hook or '—'} |")
        print()

    n = len(RULES)
    # Computed, not narrated: a split clause is one whose ID carries a letter
    # suffix. Writing "5 splits" by hand here would be exactly the item-11
    # failure this file audits — and the first draft did write 5, for 4.
    # NOT inferred from the ID. "13b" is a REAL Critical Rule (BLIND-CHECK);
    # "7b" is a split of rule 7. A letter suffix does not mean what it looks
    # like it means, and the first computed version of this line got the count
    # wrong for exactly that reason — L58 basis mismatch inside the counter.
    splits = [r[0] for r in RULES if r[0] in SPLIT_IDS]
    print(f"clauses audited: {n}  ({n - len(splits)} Critical Rules, {len(splits)} "
          f"split where the form and the substance are separately checkable: "
          f"{', '.join(splits)})")
    print("kind:    " + " · ".join(f"{k}={v} ({v/n:.0%})" for k, v in sorted(kinds.items())))
    print("checker: " + " · ".join(f"{k}={v} ({v/n:.0%})" for k, v in sorted(checkers.items())))
    print(f"backed by a hook today: {hooked}/{n} ({hooked/n:.0%})")

    # Cross the classification against the PROBE, not against the code. A hook
    # that exists but cannot be shown to fire is not enforcement.
    status = {}
    try:
        import json
        from pathlib import Path
        status = json.loads((Path(__file__).resolve().parents[2] / "meta" / "hooks"
                             / "enforcement-status.json").read_text())["hooks"]
    except Exception:
        print("(enforcement-status.json unreadable — hook verdicts omitted)")

    def verdict(h):
        return status.get(h, {}).get("verdict", "UNKNOWN")

    rel = [r for r in RULES if r[3] == "RELATION"]
    rel_hooked = [r for r in rel if r[5]]
    rel_live = [r for r in rel_hooked if verdict(r[5]) == "LIVE"]
    print()
    print(f"RELATION-form postconditions: {len(rel)}")
    print(f"  ...with a hook in code:        {len(rel_hooked)} "
          f"({', '.join(f'#{r[0]} {r[5]}={verdict(r[5])}' for r in rel_hooked) or 'none'})")
    print(f"  ...PROBE-VERIFIED enforcing:   {len(rel_live)} "
          f"({', '.join('#' + r[0] for r in rel_live) or 'NONE'})")
    pres_hooked = [r for r in RULES if r[3] == "PRESENCE" and r[5]]
    pres_live = [r for r in pres_hooked if verdict(r[5]) == "LIVE"]
    print(f"PRESENCE-form with a hook: {len(pres_hooked)} · probe-verified: "
          f"{len(pres_live)} ({', '.join('#' + r[0] for r in pres_live)})")
    print()
    print("The asymmetry above IS the result. Enforcement clusters on PRESENCE.")
    print("Every error of 2026-08-05 had the required tokens present and a false")
    print("RELATION underneath, which is why none of them tripped anything.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
