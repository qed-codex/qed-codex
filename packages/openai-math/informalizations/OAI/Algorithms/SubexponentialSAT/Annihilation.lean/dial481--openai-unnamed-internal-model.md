---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Annihilation.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Annihilation.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Annihilation.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Annihilation of the incidence-specific row paths

Section 5.3 is a finite linear-algebra statement once the row evaluations and
matrix support property are known.  This file proves that statement for actual
matrices and vectors, and specializes it to the universal type block.  It does
not assume the annihilation conclusion as a hypothesis.


### `extendRow`

 Extend a row indexed by a subset by zero on its complement. 

### `extendRow_dotProduct`

 Zero extension preserves the sum pairing with a restricted vector. 

### `extendRow_eq_zero_outside`

 A row supported on `Y` stays supported on `Y` after zero extension. 

### `annihilates_of_head_outside`

 If the selected coordinate is off the active side, all terms vanish.
Only correction values on the active side and inside `Y` need to be specified. 

### `annihilates_of_head_inside`

 On the active side, the correction agrees with a negative matrix row.
The support hypothesis supplies all omitted correction coordinates. 

### `typeBlock_annihilation`

 The two head cases of Section 5.3 for the actual universal type indices.
The matrix support implication and interpolated correction values remain
explicit hypotheses; the conclusion is the required row annihilation. 

### `map_fixedVector`

 A fixed-vector equation survives a coefficient ring homomorphism. No
injectivity or extra equations on the original vector are needed. 

### `universalPrescription`

 The prescribed values of the correction polynomials from Section 5.3.
The matrix is the actual projector construction, over the base field `F`.
The homomorphism permits the interpolation polynomial to live over `E`. 

### `universalRow`

 The actual incidence row polynomial on the universal type block. 

### `universalRow_origin`

 The row starts at the coordinate-selection row, including its diagonal. 

### `universalRow_degree`

 At most R interpolation constraints are imposed on each correction. 

### `universalRow_annihilates_of_fixed`

 Concrete row annihilation from support and the selected slot's fixed-vector
equation. The matrix support theorem discharges the Y-sparsity obligation. 

### `universalSpace`

 The full base-field subspace, imposing every slot's fixed-vector equation. 

### `mem_universalSpace`

 Membership exposes the concrete support and matrix equations. 

### `universalRow_annihilates`

 Section 5.3, instantiated to the actual matrix, actual interpolated row,
and actual base-field fixed subspace. No annihilation or support hypothesis
remains: only membership in that independently defined subspace is required. 
