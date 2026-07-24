# Recursive learning post-pretraining — first principles (wiki primer)

**Origin:** user question 2026-07-12 (Sunday): *"how can an [LLM] post-pretraining learn recursively? define it in layman terms and from first principles."* Companion to `wiki/llm-synaptic-consolidation.md` (dual-process appendix) and `meta/methodology.md` (question-generation inventory, constraint-differential search, Principle #43).

## 1. First principles
Learning = past experience changing future behavior. An LLM has exactly three substrates where experience can live:
1. **Weights** — the frozen "brain" from pre-training; the model cannot modify its own weights (lab-only lever).
2. **Context** — what is in the window right now; powerful but evaporates at session end.
3. **Environment** — files, hooks, prompts, tools; persistent AND self-editable.

Therefore all post-pretraining learning is an **environment loop**: output changes the files → files change what future sessions read → behavior changes. It becomes **recursive** when the loop improves the loop itself — the output of learning becomes the input to more learning.

## 2. The recursion ladder
| Level | What improves | Layman version | Harness instance |
|---|---|---|---|
| 0 | nothing persists | goldfish | a session without the repo |
| 1 | what the system knows | diary of facts + mistakes | `predictions/lessons.md`, calibration ledger |
| 2 | how it thinks | mistakes compressed into enforced rules | biases (B45 etc.), 19 live hooks |
| 3 | how it learns | rules that audit/retire/improve the rules | falsifiers + re-eval dates on every codification; audit days; `session-prime-cascade-hook.py` (a rule about maintaining the rule file, built 2026-07-12); prompt-library learning from its own prompts |
| 4 | the weights themselves | model retrains on its own experience | NOT available to this system; lab research territory (self-generated training data, continual learning, self-play) — also where the serious safety debates live |

**Memento analogy:** a brilliant amnesiac with a perfect notebook. The person never changes; but if the notebook contains instructions for improving the notebook, the person+notebook SYSTEM learns recursively while the brain stays frozen.

## 3. The three structural limits (first principles)
1. **The keyhole:** everything learned must re-enter through the context window as text each session — hence session-prime size caps, INDEX-first retrieval, compression discipline. Learning capacity is bounded by retrieval design, not storage.
2. **The feedback signal is everything:** recursion AMPLIFIES whatever grades it. Graded against reality (prints, prices, resolved predictions) → errors compound away. Graded against the system's own opinion of its output → errors compound in (model-collapse analog; the "taint" risk). A recursive loop without external ground truth spirals confidently. This is WHY every codification carries a falsifier and every prediction resolves against the tape.
3. **The ceiling (Principle #43):** environment loops can only CONFIGURE latent weight-level capability, never create it. Level 3 maximizes deployment of a fixed brain; only Level 4 raises the brain — and that lever is not ours.

## 4. Relation to neighboring wiki concepts
- `llm-synaptic-consolidation.md`: hooks = System-1 automation (Level-2 artifacts); context = System-2 (Level-1 substrate); consolidation = moving learnings down the ladder's cost curve.
- Constraint-differential search (methodology): Level-3 activity — searching for improvements a human designer wouldn't think to make.
- Who-caught-it ratio / gradeable-fraction metrics: the instrumentation that keeps the Level-2/3 loop honest (limit #2).

**Fluidity metadata:** codified 2026-07-12 (N=1 user-question origin; primer, not a codified principle). Re-eval with wiki sweep; falsifier: if this page is never referenced by a future artifact within 90 days, fold into llm-synaptic-consolidation.md as an appendix.
