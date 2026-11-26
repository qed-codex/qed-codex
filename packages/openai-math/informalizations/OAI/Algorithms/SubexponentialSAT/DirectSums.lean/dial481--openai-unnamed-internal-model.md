---
{
  "module": "OAI/Algorithms/SubexponentialSAT/DirectSums.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/DirectSums.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/DirectSums.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Coordinate embeddings and packed direct sums

Extension by zero realizes copies of a local subspace on pairwise disjoint
blocks. The actual embedding is injective, so its range has the sum of the
local dimensions. No runtime claim is made for these algebraic constructions.


### `extendLinear`

 Extend a coordinate vector by zero along an injective coordinate map. 

### `finrank_map_extendLinear`

 In particular, a coordinate embedding preserves the dimension of every
local subspace; extra ambient coordinates are identically zero. 

### `sum_extendLinear_mul`

 Extending the row and pairing with an arbitrary ambient vector is the
same as first restricting the vector to the embedded coordinates. 

### `sum_extendLinear_mul_hom`

 The pairing identity allows the local vector and the row to be over
different fields, through the supplied coefficient homomorphism. 

### `blockCoordinates`

 Forget each local subspace proof and uncurry the block coordinates. 

### `packedLinear`

 Place one vector from the local subspace into each disjoint block. 

### `packedSubspace`

 The actual ambient direct sum, represented as a subspace of all coordinates. 

### `blockEmbedding`

 The coordinate embedding of one block inside a packed family. 

### `packed_annihilation`

 A local annihilating row remains annihilating after extension into any
one block. Coefficients may be in a larger ring than the vector space. 

### `packedEquiv`

 Explicit linear equivalence with the finite product of local spaces. 

### `packedSupport`

 Transport of a local coordinate support into all packed blocks. 

### `packedSupportFinset`

 Finite-set form of the transported support used by the layout interface. 

### `packed_quarter_dimension`

 The manuscript's full-block proportion and three-quarter coverage imply
the required quarter-dimensional ambient subspace. 

### `packed_twentyone_sixtyfour_dimension`

 The quantitative bound before weakening it to a quarter. 

### `completeBlocks_quarter_dimension`

 Direct specialization to the complete blocks constructed by BlockPacking. 
