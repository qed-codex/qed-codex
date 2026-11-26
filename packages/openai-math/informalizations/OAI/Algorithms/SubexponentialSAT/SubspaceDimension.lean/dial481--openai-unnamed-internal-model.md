---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubspaceDimension.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubspaceDimension.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubspaceDimension.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Dimension of the universal fixed subspace

Collecting finitely many linear constraints into the product of their ranges
proves that their common kernel loses at most the sum of their ranks. We apply
this to restrictions of coordinate vectors followed by the map id - M.

All vector spaces in this file are over the same field; the result therefore
applies over the base field, without an extension-degree loss. The numerical
bounds are stated as inequalities of natural numbers with denominators cleared.


### `commonKernel`

 The vectors satisfying every constraint. 

### `finrank_le_commonKernel_add_sum_range`

 Codimension subadditivity, with the codimension written without subtraction.
No disjointness or independence between the constraints is required. 

### `codim_commonKernel_le_sum_range`

 The usual natural-number codimension formulation. 

### `coordinateRestriction`

 Restriction from a supported coordinate space to a smaller coordinate set. 

### `coordinateFixedSpace`

 Every slot's restricted vector is required to be fixed by its matrix. 

### `finrank_range_restricted_le`

 Applying a coordinate restriction before a constraint cannot increase rank. 

### `card_side_le_finrank_fixed_add_sum_defect`

 The universal-block dimension bound before inserting the numerical rank
estimate. The ambient dimension is exactly the size of the supported side. 

### `extendByZero`

 Realize the supported coordinate space inside the full coordinate space. 

### `supportedFixedSpace`

 The actual fixed subspace of full coordinate vectors, supported on S. 

### `sixteen_mul_sum_le`

 Summing the per-slot loss bound cancels the number of slots. This also
handles zero slots, where the sum is empty. 

### `fifteen_sixteenths_of_rank_budget`

 The stronger 15/16 bound, using only exact natural-number inequalities. 

### `seven_eighths_of_fifteen_sixteenths`

 Weakening 15/16 to the 7/8 proportion stated in (5.7). 

### `universalFixedSpace`

 The universal-block subspace K^B(t,g), as full coordinate vectors. 

### `universalFixedSpace_fifteen_sixteenths`

 The rank bound |J|/(8Δ), with |J| = |S|/2, gives the stronger 15/16
proportion. It is valid over the base field used to define M. 

### `universalFixedSpace_seven_eighths`

 Equation (5.7), with denominators cleared. 

### `universalFixedSpace_fifteen_thirtyseconds`

 Relative to the entire universal block of size N, the stronger bound is
15 N ≤ 32 dim K. The exact cardinality identities avoid natural division. 

### `universalFixedSpace_seven_sixteenths`

 The weaker full-block bound used by the packing argument. 
