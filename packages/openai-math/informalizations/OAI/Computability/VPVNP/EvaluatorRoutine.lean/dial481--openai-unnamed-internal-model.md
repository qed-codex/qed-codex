---
{
  "module": "OAI/Computability/VPVNP/EvaluatorRoutine.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorRoutine.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorRoutine.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Composition of time-bounded evaluator routines

A routine realizes a transition when any continuation with a reserved amount
of fuel returns the prescribed count on the resulting states. This permits
different branches to use different numbers of instructions.


### `Realizes`

 The caller reserves `extra` instructions after the routine's per-path
bound `B`. Its count on each encoded output determines the whole transition. 

### `Realizes.of_runs`

 A deterministic prefix spends its actual cost and preserves one branch. 

### `Realizes.of_delay`

 Bounded delays on a finite family of outcomes establish a transition
whose multiplicity is their ordinary sum. 
