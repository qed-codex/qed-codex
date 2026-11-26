---
{
  "module": "Zeta23/MV/Duality.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/MV/Duality.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/MV/Duality.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# MV step 4 — spectral reduction: `eigen_bound` ⇒ `MVDiag 13` ⇒ `∃ C, MVHilbert C`

With `k_{rs} := √δ_r √δ_s/(λ_r − λ_s)` (0 on the diagonal; real antisymmetric) the matrix
`M := i·K` is Hermitian.  Every eigen-pair `(ν, v)` of `M` (unit `v`, from Mathlib's
`Matrix.IsHermitian.eigenvectorBasis`) satisfies the eigen-relation of `eigen_bound` with `μ := −ν`,
so `|ν| ≤ 13` for all eigenvalues (step 3).  Expanding in the eigenbasis
(`y* M y = Σ_i ν_i |(U*y)_i|²`, `Σ_i |(U*y)_i|² = Σ_i |y_i|²`) gives `|y* M y| ≤ 13 ‖y‖²`;
substituting `y_r := x_r/√δ_r` lands exactly on `MVDiag 13` (the literature / diagonal form of the
Montgomery–Vaughan weighted Hilbert inequality, Zeta23/MV.lean), and polarization
`exists_MVHilbert_of_diag` yields the bilinear H-MV of `Hypotheses.lean`.


### `EigenBound`

 The conclusion of step 3 (`Zeta23.MV.eigen_bound`, Eigen.lean) as a `Prop` with a general
constant: every solution of the normalized eigen-relation with a unit vector has `|μ| ≤ C`. 

### `kfun`

 The normalized kernel `k_{rs} = √δ_r √δ_s/(freq r − freq s)`, `0` on the diagonal. 

### `Mmat`

 `M := i·K`, a Hermitian complex matrix. 

### `star_dotProduct_self`

 `star v ⬝ᵥ v = Σ ‖v_i‖²` (as a complex number). 

### `star_dotProduct_mulVec_eq`

 Spectral expansion of the Hermitian form, complex-valued:
`x* A x = Σ_i ν_i ‖(U* x)_i‖²` with `U` the eigenvector unitary. 

### `sum_norm_sq_unitary`

 `Σ ‖(U* x)_i‖² = Σ ‖x_i‖²` for the eigenvector unitary `U`. 

### `abs_eigenvalue_le`

 Every eigenvalue of `M = iK` has absolute value `≤ C` (step 3 + Mathlib eigenbasis). 

### `norm_form_le`

 The Hermitian form of `M` is bounded by `C ‖y‖²`. 

### `mvDiag_of_eigenBound`

 **Spectral reduction**: an eigenvalue bound `EigenBound C` gives `MVDiag C` — the
Montgomery–Vaughan weighted Hilbert inequality (diagonal / literature form, Zeta23/MV.lean). 

### `mvHilbert_of_eigenBound`

 … hence the bilinear H-MV of `Hypotheses.lean` with constant `2C` (polarization). 
