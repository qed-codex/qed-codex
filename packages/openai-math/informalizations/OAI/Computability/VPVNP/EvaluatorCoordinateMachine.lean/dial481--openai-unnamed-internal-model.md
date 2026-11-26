---
{
  "module": "OAI/Computability/VPVNP/EvaluatorCoordinateMachine.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorCoordinateMachine.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorCoordinateMachine.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The binary evaluator from its two deterministic coordinate readers

The entire stack machine, including binary input decoding and terminal
branching, has fixed control as soon as its two entry readers are fixed.
The two coordinate-query contracts concern only the stored row and column
and the field element returned. The exponent width occurs only in the input,
radix conversion and digit traversal.


### `program`

 A single literal two-tape evaluator table built from the fixed entry
readers, independently of the ground field or exponent width at a given input. 

### `count_from_readers`

 Equation (8.2) for the actual bit-stack machine, assuming just correctness
and running times for the two deterministic coordinate-entry readers on the
advised matrix data. The scalar update and nondeterministic control are the
concrete programs of the preceding modules. 
