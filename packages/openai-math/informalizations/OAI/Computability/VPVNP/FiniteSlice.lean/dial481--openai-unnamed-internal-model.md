---
{
  "module": "OAI/Computability/VPVNP/FiniteSlice.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/FiniteSlice.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/FiniteSlice.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The reduced algebra of a finite geometric slice

Section 8.2 of *VP and VNP differ over every field* takes the quotient of a polynomial
ring over a finite field by the ideal vanishing at all geometric points of a finite slice.
Evaluation embeds this reduced coordinate algebra in the functions on the slice. The
points can be defined over an extension field. Frobenius permutes the points and forces
the coefficients of every minimal linear dependence to descend to the base field.
This bounds the base-field dimension by the number of geometric points.


### `exists_algebraMap_eq_of_frobenius_fixed`

 A coordinate fixed by the cardinality Frobenius of the ground field descends to that field. 

### `linearIndependent_of_fixedField`

 A finite family of functions equivariant for a permutation of the arguments and
a field endomorphism is linearly independent over the extension whenever it is
linearly independent over the fixed field. 

### `finite_and_finrank_le_of_independence`

 A finite coordinate model preserving independence after extending scalars bounds
the dimension over the original field. 

### `CoordinateAlgebra`

 The reduced coordinate algebra over the base field of a set of extension-field points. 

### `coordinateLabel`

 The images of the polynomial variables in the slice algebra. 

### `sliceEvaluation`

 Evaluation of classes of base-field polynomials at all points of the slice. 

### `equation_eq_zero`

 Every original label equation holds in the reduced coordinate algebra. 

### `pointPerm`

 A field endomorphism fixing the coefficient field permutes the points of a finite slice. 

### `coordinateAlgebra_finite_finrank`

 Dimension bound for a finite slice defined by base-field equations.
The extension `E` may be the algebraic closure of `K`. 
