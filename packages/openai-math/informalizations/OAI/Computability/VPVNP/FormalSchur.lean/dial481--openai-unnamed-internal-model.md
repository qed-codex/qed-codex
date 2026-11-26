---
{
  "module": "OAI/Computability/VPVNP/FormalSchur.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/FormalSchur.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/FormalSchur.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Formal Schur factors of the reverse characteristic polynomial

Appendix D.2 of *VP and VNP differ over every field* factors `det (1 - uM)`
over formal power series by successively deleting the first row and column.
The geometric inverse of a trailing matrix pencil has the powers of that
matrix as its coefficients.


### `formalPencil`

 The power-series matrix pencil whose inverse encodes all matrix powers. 

### `formalResolvent`

 The entrywise series of powers of the matrix. 

### `pencilInvertible`

 Invertibility witness for the formal matrix pencil, with its formal resolvent as the
inverse. 

### `coeff_formalPencil_inv`

 Every coefficient of the inverse pencil is an entry of a finite matrix power. 

### `headFactor`

 The Schur complement obtained by deleting the first row and column. 

### `peelFactors`

 Evaluate a local rule on each trailing submatrix by repeatedly dropping the first index. 

### `suffixIndex`

 Place the indices of the trailing principal submatrix in the full matrix. 

### `coeff_headFactor`

 The degree-zero and degree-one terms of a Schur factor come from the diagonal.
Each higher coefficient queries exactly one power of the trailing matrix. 

### `charpolyRev_eq_schurProduct`

 Every factor of the reverse characteristic polynomial is obtained by a direct
index shift to the trailing principal submatrix beginning at the given row. 
