---
{
  "module": "Zeta23/LinAlg/VonNeumann.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/LinAlg/VonNeumann.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/LinAlg/VonNeumann.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
The linear algebra of §3 of the paper (Hermitian positive/negative parts, inertia, the positive index,
von Neumann's trace inequality, the rank–trace inequality, Weyl's perturbation bound). These seven files
were produced first, as a self-contained development (namespace `RHLinalg`) accompanying §3 of the paper —
like all Lean code in this repository, written by Claude, under the direction of the paper's authors — and are
incorporated here unchanged; they have no upstream outside this project (see README § Provenance and attribution).
-/
```


# Von Neumann's trace inequality

For Hermitian `A, B` with eigenvalues sorted in decreasing order
`a₀ ≥ a₁ ≥ …` and `b₀ ≥ b₁ ≥ …`,

  `Re tr(AB) ≤ ∑ᵢ aᵢ bᵢ`.

## Proof outline

Diagonalise `A = Uₐ Dₐ Uₐᴴ` and `B = Uᵦ Dᵦ Uᵦᴴ`. Setting `W := Uₐᴴ Uᵦ`
(unitary), a direct calculation gives

  `tr(AB) = tr(Dₐ W Dᵦ Wᴴ) = ∑ₖₗ aₖ · ‖Wₖₗ‖² · bₗ`.

The matrix `Sₖₗ := ‖Wₖₗ‖²` is doubly stochastic over `ℝ` (rows and columns
of a unitary matrix are unit vectors). By **Birkhoff–von Neumann**
(`exists_eq_sum_perm_of_mem_doublyStochastic`) every doubly stochastic
matrix is a convex combination of permutation matrices: `S = ∑_σ w_σ P_σ`.
For each permutation `σ`, `∑ₖ aₖ b_{σ k} ≤ ∑ₖ aₖ bₖ` by the **rearrangement
inequality** (`Monovary.sum_mul_comp_perm_le_sum_mul`), since both `a` and
`b` are antitone (hence monovary). Averaging over `σ` with weights `w_σ`
gives the result.


### `normSqMatrix`

 Entrywise squared-norm `‖Wᵢⱼ‖²` of a matrix, as a real matrix. 

### `normSqMatrix_mem_doublyStochastic_of_unitary`

 For a unitary matrix `W`, the entrywise-squared-norm matrix
`(i, j) ↦ ‖Wᵢⱼ‖²` is doubly stochastic over `ℝ`. 

### `re_trace_mul_eq_eigenvalue_bilinear`

 For Hermitian `A, B`, writing `W = Uₐᴴ Uᵦ` for the eigenvector unitaries,
`Re tr(AB) = ∑ₖₗ λₖ(A) · ‖Wₖₗ‖² · λₗ(B)`. 

### `_root_.Antitone.monovary_antitone`

 Two antitone functions on a linear order monovary. 

### `bilinear_doublyStochastic_le_of_monovary`

 The core combinatorial step: for `a, b : n → ℝ` that monovary and
`S` doubly stochastic, `∑ₖₗ aₖ Sₖₗ bₗ ≤ ∑ₖ aₖ bₖ`.

Proof: `∑ₖₗ aₖ Sₖₗ bₗ = ∑ₖ aₖ (S *ᵥ b)ₖ = a ⬝ (S *ᵥ b)`. By Birkhoff,
`S *ᵥ b = ∑_σ w_σ · (b ∘ σ)` (via `permMatrix_mulVec`). For each `σ`,
`∑ₖ aₖ b(σ k) ≤ ∑ₖ aₖ bₖ` by rearrangement. Average with weights `w_σ`. 

### `vonNeumann_trace_ineq`

 **Von Neumann's trace inequality** (Hermitian case). For Hermitian `A, B`
with eigenvalues sorted in decreasing order, `Re tr(AB) ≤ ∑ᵢ aᵢ bᵢ`. 
