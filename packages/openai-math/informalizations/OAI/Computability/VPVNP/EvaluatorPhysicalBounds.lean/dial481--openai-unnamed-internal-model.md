---
{
  "module": "OAI/Computability/VPVNP/EvaluatorPhysicalBounds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorPhysicalBounds.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorPhysicalBounds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Literal tape clock and storage envelope of the evaluator

Compilation of the fixed stack bank costs quadratic time. Its simulated input
length is linear in the exponent width. The resulting exponent of the width
is a fixed four, independent of the advised matrices and their query times.


### `tapeTicks`

 Physical clock sufficient for all stack instructions on the named bank. 

### `packedCap`

 A per-stack height bounds the packed bank, including its delimiter cells. 

### `headRadius`

 Two heads may move to either side of their initial position. 

### `tapeTicks_le_exp_poly`

 Uniform in the exponent width. All other parameters, including the two
coordinate-call clocks, admit the indicated singly exponential bound. 

### `headRadius_le`

 Uniform polynomial storage, including the head window of the literal
machine. All coordinate reader storage is accounted for in workspace. 
