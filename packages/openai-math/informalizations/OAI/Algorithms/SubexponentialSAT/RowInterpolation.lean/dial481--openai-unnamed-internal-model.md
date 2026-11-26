---
{
  "module": "OAI/Algorithms/SubexponentialSAT/RowInterpolation.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/RowInterpolation.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/RowInterpolation.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Row correction polynomials

The interpolation construction in Section 5.3. A finite set of nonzero
nodes is augmented by the node zero, where the correction is prescribed
to vanish. The resulting actual Lagrange polynomial has degree at most
the number of nonzero constraints.


### `augmentedNode`

 The extra `none` index denotes the node zero. 

### `augmentedValue`

 The value of a correction at the extra node is zero. 

### `correctionPolynomial`

 An explicit Lagrange correction with an additional zero constraint. 

### `exists_correctionPolynomial`

 Existence follows from the actual polynomial above, not an interpolation axiom. 

### `columnCorrection`

 Corrections are constructed only on selected columns and are zero elsewhere. 

### `rowPath`

 Add a correction row to the constant coordinate-selection row. 

### `rowPath_eval_zero`

 The formula includes the diagonal correction when `u` is a selected column. 

### `interpolatedRowPath`

 The row path using the actual finite-node correction construction. 

### `agreementPositions`

 Exactly the interpolation positions where a column is on the active side. 

### `correctionColumns`

 The set `Y` of columns with at most `R` active interpolation positions. 

### `universalCorrection`

 The actual family of correction polynomials on a universal type block. 

### `universalRowPath`

 The polynomial row starting at type `u` and following its incidence slot `i`. 

### `universalRowPath_coeff_zero`

 Coefficientwise lifting can preserve the starting coordinate row exactly. 
