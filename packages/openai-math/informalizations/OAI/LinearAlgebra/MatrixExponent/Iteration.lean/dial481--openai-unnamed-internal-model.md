---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Iteration.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Iteration.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Iteration.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Iterating compression at one list width 

### `absorb`

 The lower bound lets us absorb the additive term into the contraction at
*each* step. This avoids estimating a geometric sum at the last step. 

### `incompatible`

 Fix a number of iterations before choosing the width. The total number
of copies and the size per bit each cost at most an extra exponent of 1/40. 
