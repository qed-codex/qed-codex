---
{
  "module": "OAI/Computability/VPVNP/AffineSliceQuery.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/AffineSliceQuery.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/AffineSliceQuery.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Coefficient queries after prime reduction and affine slicing

A row lookup either asks for one original integer coefficient and casts it
to the base field, or reads the constant and linear coefficients of one of
the supplied affine cuts. This gives the scalar interface used by the
finite-slice coordinate queries of Appendix D.


### `AffineCut`

 One affine equation, represented by its coefficient words in the slice field. 

### `AffineCut.constant`

 Coefficient of the constant monomial in the affine slice equation over `K`. 

### `AffineCut.linear`

 Coefficient of each of the `t` coordinate variables in the affine slice equation. 

### `polynomial`

 The multivariate polynomial of the affine equation, obtained by adding its constant term to
the weighted sum of the coordinate variables. 

### `getCoeff`

 Read the coefficient of a cut at a numeric exponent tuple. 

### `slicedSystem`

 Base change the integer equations, followed by the affine slice equations. 

### `slicedQueryData`

 Numerical input for the indexed matrix algorithm after prime reduction. 
