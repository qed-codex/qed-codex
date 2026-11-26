---
{
  "module": "OAI/Computability/VPVNP/CompressorShrinkABSliceWindow.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkABSliceWindow.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkABSliceWindow.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native AB visits in the fixed shrinking script

The AB section starts after the thirty-six demand and selection visits and
the twelve resident-list visits. Its scalar expressions read the current
level header before the scratch region. Every source stage therefore uses
the operands evaluated from its own chronological input memory.


### `preceding`

 The shrinking visits preceding the AB intersection window, including term selection and
construction of the resident lists. 

### `abWindow`

 The contiguous window of AB intersection visits in the fixed script for this shrinking
substep. 

### `ab_header_walk`

 A guarded whole-level run produces the precise operand and execution
contract of every member of the script window. 
