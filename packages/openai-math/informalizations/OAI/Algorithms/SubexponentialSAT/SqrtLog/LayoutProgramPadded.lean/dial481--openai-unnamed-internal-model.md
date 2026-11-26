---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutProgramPadded.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutProgramPadded.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutProgramPadded.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 A computable integer row for every incidence position. Inactive covered
positions and non-head uncovered positions are zero. Active rows are precisely
the raw block constraints, with repetitions and zero padding permitted. 

### `paddedEntry`

 This definition uses the executable packing lookup and scalar numerator.
The arbitrary finite equivalence used by the semantic layout is absent. 

### `paddedConstraint_cover`

 Every old raw constraint has an actual incidence position representing it. 

### `paddedConstraint_shape`

 Every emitted row is either zero or one of the old raw constraints. 
