---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Rectangle/Model.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Rectangle/Model.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Rectangle/Model.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The arithmetic exponent for rectangular products

The side lengths are ordered as rows, columns, inner dimension. The
straight-line circuit rules are shared with the square model.


### `benchmark`

 The benchmark on the cone where the last coordinate is smallest. 

### `U`

 Evaluate the benchmark with a smallest side placed last. Division by
zero in the real-valued formula returns zero on a coordinate plane. 

### `Rigidity`

 The part of the rectangular rigidity dichotomy used in Corollary 1.2.
An active shape is one where the benchmark exceeds every pair sum. 
