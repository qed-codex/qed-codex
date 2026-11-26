---
{
  "module": "OAI/Computability/VPVNP/EvaluatorRoutineFrame.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorRoutineFrame.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorRoutineFrame.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Framing nondeterministic evaluator callbacks

Renaming a returning routine into a larger bank of stacks leaves every other
stack available to the scheduler. Each binary choice retains its two slots,
and the continuation receives the residual fuel on that particular path.


### `countFrom_onPorts`

 Exact continuation semantics on a disjoint set of named ports. 

### `count_onPorts`

 The entry point of a framed routine can be invoked from an arbitrary caller state. 
