---
{
  "module": "OAI/Computability/VPVNP/SubpartyEmbedding.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SubpartyEmbedding.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SubpartyEmbedding.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Trivial legs outside a subset of parties

Section 2.2 of *VP and VNP differ over every field* restricts a spectral
point to a smaller party set, with a one-dimensional leg at every remaining
party. The embedding preserves products and restrictions. The embedded
direct sum is a restriction of the full-party direct sum.


### `trivialExtension`

 Extend a tensor to the disjoint union of its parties with a new set, giving each new party
a one-dimensional leg. 

### `applyLocal_trivialExtension`

 Local maps supported on the old parties act on the original tensor. 

### `trivialExtension_restricts`

 Local restrictions extend to the larger set of parties. 

### `trivialExtension_product`

 Extension commutes with the tensor product after identifying singleton factors. 

### `trivialExtension_directSum`

 Merging the two singleton blocks at each outside party produces the
embedded direct sum on the old parties. 
