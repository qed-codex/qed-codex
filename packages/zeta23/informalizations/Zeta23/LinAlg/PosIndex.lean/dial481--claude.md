---
{
  "module": "Zeta23/LinAlg/PosIndex.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/LinAlg/PosIndex.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/LinAlg/PosIndex.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

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


# Positive index of a Hermitian matrix

For a Hermitian matrix `A` over `𝕜 = ℝ` or `ℂ`, the *positive index*
`n₊(A)` is the number of strictly positive eigenvalues. By Sylvester's law
of inertia this equals the maximal dimension of a subspace on which the
Hermitian form `x ↦ xᴴ A x` is positive definite.

This file defines `posIndex` via the eigenvalue count, together with the
real-valued trace `rtrace` and squared Frobenius norm `frobSq` needed for
the rank–trace inequality (paper §3, `lem:ranktrace`).


### `posIndex`

 The positive index `n₊(A)` of a Hermitian matrix: the number of strictly
positive eigenvalues. Equivalently (Sylvester's law of inertia), the maximal
dimension of a subspace on which the form `x ↦ xᴴAx` is positive definite. 

### `negIndex`

 The negative index `n₋(A)`: the number of strictly negative eigenvalues. 

### `posIndexAbove`

 The thresholded positive index `n₊^θ(A)`: the number of eigenvalues
strictly above `θ`. `posIndexAbove hA 0 = posIndex hA`. 

### `posIndex_eq_rank_of_posSemidef`

 For a PSD Hermitian matrix the positive index is the rank (every nonzero
eigenvalue is positive). 

### `rtrace`

 Real part of the trace. For a Hermitian matrix this is the full trace,
since the trace of a Hermitian matrix is real. 

### `frobSq`

 Squared Frobenius norm, `‖A‖_F² = Re tr(AᴴA) = ∑ᵢⱼ |Aᵢⱼ|²`. 

### `eigEquiv`

 The canonical equivalence `Fin (card n) ≃ n` under which
`eigenvalues (e k) = eigenvalues₀ k`. 

### `sum_eigenvalues_reindex`

 Any sum over `n` of a function of the eigenvalues equals the corresponding
sum over `Fin (card n)` of the function applied to `eigenvalues₀`. 

### `frobSq_hermitian_eq_sum_sq_eigenvalues`

 For a Hermitian matrix, `‖A‖_F² = ∑ᵢ λᵢ²` (sum of squared eigenvalues). 
