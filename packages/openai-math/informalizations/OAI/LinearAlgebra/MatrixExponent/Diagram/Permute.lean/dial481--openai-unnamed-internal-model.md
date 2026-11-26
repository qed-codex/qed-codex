---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Diagram/Permute.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Diagram/Permute.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Diagram/Permute.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Reindexing individual wire positions

An arbitrary bijection of the exterior positions is a structural rewiring.
We pull out the requested bits one at a time, keeping track of the positions
of all remaining bits.


### `extract`

 Extract the requested bundle, retaining the remaining positions indexed by `α`. 
