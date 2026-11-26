---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Spectral/Semiring.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Spectral/Semiring.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Spectral/Semiring.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Coefficient tensors on a finite set of named sites

We store a finite sum of pure tensors. Restriction acts by a local matrix
on every summand and compares the resulting coefficient arrays. It need
not preserve the chosen decomposition. Every array has a coordinate
expansion, and two expansions of the same array restrict to each other.


### `Restricts.pullback`

 Copying or selecting local coordinates is a restriction. 

### `restricts_iff`

 Formula independent of the chosen expansions of both arrays. 


# Direct sums and products of restrictions

Use block diagonal matrices for sums and Kronecker products for products.
The identities concern coefficient arrays and require no termwise
correspondence between the decompositions.


### `extend`

 Equality of coefficient arrays survives extending the factors by zero. 


# Semiring laws up to mutual restriction

Each identity reindexes the terms and the coordinates at every site by
the same sum or product equivalence.



# The restriction semiring on a fixed finite set of sites


### `Tensor`

 Coefficient tensors modulo mutual local linear restriction. 


# Finite coefficient tables

The product of local coordinate selectors is a weighted Kronecker delta.
It suffices to put the weight at one site.


### `ofTable`

 Coordinate expansion of any finite array as a sum of pure tensors. 

### `restricts_one`

 Selecting a nonzero coefficient and scaling by its inverse recovers the unit. 
