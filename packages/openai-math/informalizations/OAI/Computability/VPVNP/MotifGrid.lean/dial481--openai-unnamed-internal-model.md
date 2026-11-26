---
{
  "module": "OAI/Computability/VPVNP/MotifGrid.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MotifGrid.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MotifGrid.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Rational width grids for a fixed wire motif

In Theorem 6.1 of *VP and VNP differ over every field*, the spectral distances
on the demand and supply edges obey a weighted quadratic inequality. The
width grids below work simultaneously for every distance pattern satisfying
that inequality. All entries have one common denominator.


### `widthNorm`

 Width norm for edges with positive masses `p`. 

### `distanceEnergy`

 Squared distance in the dual weighted norm. 

### `wireValue`

 Logarithmic spectral value of a collection of wires. 

### `wireValue_le`

 Weighted Cauchy–Schwarz for the primal width norm and dual distance norm. 

### `norm_sq`

 Squaring the width norm recovers its weighted energy. 

### `coordinate_le`

 A single edge contributes at most the full width norm. 

### `norm_mono`

 The width norm is monotone on nonnegative widths. 

### `widthNorm_round_le`

 Coordinatewise upward rounding by at most `ε` increases the norm by at most
`ε` times the width norm of the all-ones vector. 

### `boxGrid`

 One finite box of vectors on a common rational mesh. 

### `maximizer`

 Optimal supply widths at dual distances `d`. 

### `realWidths`

 Cast a rational width vector into the real weighted space. 

### `StrictGrids`

 The two finite grids, their common denominator, and their approximation and
comparison properties. The supply witness may depend on the spectral point. 

### `StrictGrids.denominator`

 Positive integer giving the common mesh size through its reciprocal on both rational
  grids. 

### `StrictGrids.demands`

 Finite rational demand-width vectors that cover every nonnegative demand of weighted norm
  at most one by coordinatewise rounding up. 

### `StrictGrids.supplies`

 Finite rational supply-width vectors of weighted norm at most the supply radius, among
  which strict domination is witnessed. 

### `exists_strict_grids`

 Uniform finite rational approximation in the first part of Theorem 6.1.
The grid is independent of the demand widths and of the spectral point. 

### `widthNorm_scale`

 Scaling all widths by a nonnegative factor scales their norm by that factor. 

### `wireValue_scale`

 Scaling all widths scales the logarithmic wire value. 

### `demandWidths`

 Demand bit widths when the base scale is `t * G.denominator`. 

### `supplyWidths`

 Supply bit widths on the same base scale. 

### `supplyWidths_norm_le`

 The finite supply list has the required integral norm bound at every multiple. 

### `integer_strict`

 At any positive multiple of the mesh denominator the integer widths retain
strict comparison. The supply index is chosen after the two distance patterns. 

### `exists_large_scale`

 Multiples of the common denominator can exceed any prescribed base size. 
