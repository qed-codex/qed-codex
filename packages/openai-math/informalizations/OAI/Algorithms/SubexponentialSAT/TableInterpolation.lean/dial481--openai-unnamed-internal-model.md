---
{
  "module": "OAI/Algorithms/SubexponentialSAT/TableInterpolation.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/TableInterpolation.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/TableInterpolation.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Exact table interpolation over a commutative ring

The usual Lagrange construction works whenever the differences of distinct
nodes are units. In particular it does not require a field, and preserves
table values in the whole coefficient ring, not only in a residue field.


### `UnitDifferences`

 The exact denominator hypothesis for Lagrange interpolation. 

### `UnitDifferences.map`

 Ring homomorphisms preserve the denominator hypothesis. 

### `invDiff`

 The inverse of a node difference; its value on the diagonal is unused. 

### `basisDivisor`

 Ring-valued version of the mathlib Lagrange basis divisor. 

### `basis`

 Lagrange basis for the finite node family. 

### `interpolate`

 The exact interpolant of a finite table in the coefficient ring. 

### `mvBasis`

 A Lagrange basis polynomial in one selected multivariate coordinate. 

### `gridBasis`

 The tensor product basis attached to a grid point. 

### `mvInterpolate`

 Tensor-product interpolation of a finite grid table. 

### `exists_integerLabelInterpolant`

 Specialization to literal integer representatives; agreement is in R itself. 

### `isUnit_natCast_primePower`

 Positive integers below p remain units modulo every power of the prime p. 

### `unitDifferences_zmod_integerLabels`

 Distinct integer representatives have unit differences modulo a prime power. 

### `unitDifferences_lambda_integerLabels`

 The specified integer labels have unit differences in the lifted ring Lambda. 

### `exists_lambda_tableInterpolant`

 Every table has an exact polynomial representation over the actual lifted ring. 
