---
{
  "module": "OAI/Computability/VPVNP/RankQueryStackGramEngine.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryStackGramEngine.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryStackGramEngine.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The fixed Schur determinant machine for weighted Gram coefficients

A concrete scalar reader for the input matrix is the only matrix-dependent
subroutine. The Schur interpreter, the Gram index calculation, the two field
products and the continuation stack all have fixed finite controls.


### `actionsWith`

 Build the Gram evaluator actions using the supplied signed scalar-read callbacks. 

### `actions`

 Instantiate the Gram evaluator actions with the scalar routine built from a Macaulay entry
reader. 

### `machine`

 Assemble the stack machine that evaluates Gram queries using the supplied Macaulay entry
reader. 

### `contractsWith`

 Install all five engine callbacks on one finite bank. The matrix-entry
reader can be reused for different query degrees and both child directions. 
