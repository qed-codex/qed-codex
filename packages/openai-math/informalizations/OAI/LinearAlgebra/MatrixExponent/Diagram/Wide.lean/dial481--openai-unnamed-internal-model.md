---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Diagram/Wide.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Diagram/Wide.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Diagram/Wide.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Tensor powers on independent bit bundles

Products, concatenation and regrouping are witnessed by structural
permutations of the exterior positions. No gates identify or discard bits.


### `Net.rewire`

 Transport a network along permutations in the forward direction. 

### `appendCopies`

 The first block has length m. Writing the sum as n+m exposes Lean's
recursion on the first block without casts. 

### `Net.power_lists`

 Taking d copies of a batch of t lists keeps all t*d lists independent. 


# Networks of arbitrary arity

The cost of a station is one plus its arity. A predicate on tables
tracks allowed labels. Joins and reordering expose no new positions.

