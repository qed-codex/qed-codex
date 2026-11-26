---
{
  "module": "Zeta23/LinAlg/Sylvester.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/LinAlg/Sylvester.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/LinAlg/Sylvester.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

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


# Sylvester's law of inertia for Hermitian matrices (subspace bound)

We prove the key inequality: any subspace `W ⊆ 𝕜ⁿ` on which the Hermitian
form `x ↦ Re(xᴴAx)` is positive definite has dimension at most
`posIndex hA`.

The proof is short: `A = A₊ − A₋` with both parts PSD (`HermitianPosPart`).
If `A₊ · x = 0` for `x ∈ W ∖ {0}`, then `xᴴAx = −xᴴA₋x ≤ 0`, contradicting
positive-definiteness on `W`. So `(A₊ *ᵥ ·)|_W` is injective, hence
`dim W ≤ rank A₊ = posIndex hA`.

This is the engine behind `lem:inertia`: pulling back a Hermitian form
cannot increase its positive index.


### `hermForm`

 The Hermitian form `x ↦ Re(star x ⬝ (A *ᵥ x))` associated to a matrix. 

### `PosDefOn`

 `W` is a subspace on which `hermForm A` is positive definite. 

### `hermForm_nonneg_of_posSemidef`

 `hermForm A x ≥ 0` when `A` is PSD. 

### `finrank_le_posIndex_of_posDefOn`

 **Sylvester's inequality (hard direction)**: any subspace on which the
Hermitian form is positive definite has dimension at most `posIndex hA`.

This is the subspace characterization of `n₊` that makes `lem:inertia`
trivial. 

### `posDefOn_range_hermPosPart`

 **Sylvester's inequality (easy direction)**: the Hermitian form is
positive definite on `range A₊`, which has dimension `posIndex hA`.

For `z = A₊ · y ∈ range A₊`, the eigenbasis coordinates `c := Uᴴz` satisfy
`cᵢ = λᵢ⁺ · (Uᴴy)ᵢ`, so `cᵢ = 0` whenever `λᵢ ≤ 0`. Hence
`zᴴAz = ∑ᵢ λᵢ|cᵢ|² = ∑_{λᵢ>0} λᵢ|cᵢ|²`, each term ≥ 0; and `z ≠ 0 ⟹ c ≠ 0`
(U unitary) forces some positive term. 

### `hermForm_one`

 `hermForm I x = ∑ᵢ ‖xᵢ‖²` (the squared `ℓ²` norm). 

### `sum_normSq_unitary_mulVec`

 `∑ᵢ ‖cᵢ‖²` is preserved by the unitary change of variables `c = Uᴴx`. 

### `hermForm_le_of_eigenvalues_le`

 `hermForm A x ≤ θ · ‖x‖²` whenever every eigenvalue of `A` is `≤ θ`.
Equivalently, `A ⪯ θ·I`. 

### `hermForm_gt_on_range_truncPos`

 **Generalized easy Sylvester direction**: on `range(specMap hA (·−θ)⁺)`,
the form satisfies `hermForm A x > θ · ‖x‖²` for `x ≠ 0`. The dimension of
this range is `posIndexAbove hA θ` (via `rank_specMap`).

The proof is identical to `posDefOn_range_hermPosPart` (which is the `θ=0`
case) with `λᵢ > 0` replaced by `λᵢ > θ`. 

### `finrank_range_hermPosPart`

 The dimension of `range A₊` is `posIndex hA`. 

### `posIndex_eq_max_finrank_posDefOn`

 **Sylvester's law of inertia (subspace characterization)**. 
