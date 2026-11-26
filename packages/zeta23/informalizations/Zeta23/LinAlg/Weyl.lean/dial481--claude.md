---
{
  "module": "Zeta23/LinAlg/Weyl.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/LinAlg/Weyl.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/LinAlg/Weyl.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

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


# Weyl's inequality and the thresholded Cauchy–Schwarz count

Paper §3, `lem:weyl` and `lem:CS`. These are the remaining two linear-algebra
tools (beyond `lem:inertia` and `lem:ranktrace`); they are needed for
Theorems B and C (simple zeros, distinct zeros) but not for Theorem A (2/3 on
the critical line).


### `weyl_posIndexAbove_le`

 **Weyl's eigenvalue perturbation inequality** (the paper's [lem:weyl], §3).
If `A, E` are Hermitian and `θ ≥ ‖E‖_op`, then `n₊^θ(A + E) ≤ n₊(A)`.

Proof in the paper: with eigenvalues in decreasing order, `λᵢ(A+E) ≤ λᵢ(A) + ‖E‖`
(Courant–Fischer). Hence `λᵢ(A+E) > θ ≥ ‖E‖` forces `λᵢ(A) > 0`.

That is the paper's proof. The Lean proof instead takes W := the range of the spectral truncation
(t − θ)⁺ of A + E (so dim W = n₊^θ(A+E)), shows that the Hermitian form of A is positive definite on W
(that of A + E exceeds θ‖x‖² there while that of E is at most θ‖x‖²), and concludes with the subspace
characterization of the positive index (`finrank_le_posIndex_of_posDefOn`, Sylvester.lean); the
hypothesis is stated as |λᵢ(E)| ≤ θ for every eigenvalue of E.
The operator norm `‖E‖_op` is
`Matrix.instNormedRing` (the `linftyOpNorm`), which for Hermitian matrices
equals `max |λᵢ|`. 

### `cauchySchwarz_count`

 **Thresholded Cauchy–Schwarz count** (the paper's [lem:CS], §3).
For Hermitian `R` with `tr R > θ · d`,
  `n₊^θ(R) ≥ (tr R − θd)² / tr(R²)`.

Proof: With `S := ∑_{λᵢ > θ} λᵢ`, note `S ≥ tr R − θd > 0` (negative
eigenvalues only help). By Cauchy–Schwarz, `S² ≤ n₊^θ(R) · ∑_{λᵢ>θ} λᵢ²
≤ n₊^θ(R) · tr(R²)`.

This is a pure real-eigenvalue statement; the proof is Cauchy–Schwarz on the
eigenvalues above the threshold. 
