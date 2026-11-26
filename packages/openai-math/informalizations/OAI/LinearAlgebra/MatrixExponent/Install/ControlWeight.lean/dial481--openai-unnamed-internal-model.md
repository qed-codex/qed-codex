---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Install/ControlWeight.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Install/ControlWeight.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Install/ControlWeight.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Selecting a network by a fixed number of control bits

Multiply one factor per control word. Inactive factors evaluate at a
fixed nonzero entry and divide by that entry. An identically zero table
only needs to test the control bits.


### `switch`

 The cost is linear in the payload width and the largest branch cost
when the number of control bits is fixed. 
