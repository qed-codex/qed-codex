---
{
  "module": "OAI/Computability/VPVNP/EvaluatorUniformBounds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorUniformBounds.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorUniformBounds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Length-uniform bounds for the fixed evaluator table

All query, advice and scalar parameters can be bounded before the exponent
width is chosen. A single length envelope then bounds the physical clock,
advice length and tape window for every width, including widths selected by
the later diagonal construction.


### `lengthEnvelope`

 One numeric bound for the width-independent parameters at a length.
The entry query time is specified by its binary exponent. 

### `lengthEnvelope_mono`

 Width and storage bounds may be chosen uniformly over all fields and
slice models at a given length. 

### `uniform_window`

 Bound the two physical tapes including the original raw input and both
possible directions of head movement. 

### `exists_uniform_clock`

 Extract a single exponent and threshold from a length envelope before
choosing the width. The polynomial degree in the width is fixed. 
