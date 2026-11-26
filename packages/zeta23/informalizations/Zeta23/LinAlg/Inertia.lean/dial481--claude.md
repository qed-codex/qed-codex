---
{
  "module": "Zeta23/LinAlg/Inertia.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/LinAlg/Inertia.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/LinAlg/Inertia.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

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


# Inertia under pull-back (paper §3, `lem:inertia`)

For a Hermitian form `Q` on `ℂᵐ` and a linear map `𝒜 : U → ℂᵐ`, the positive
index of the pulled-back form `Q ∘ 𝒜` is at most the positive index of `Q`.

## Matrix formulation

If `Q : Matrix m m 𝕜` is Hermitian and `B : Matrix m d 𝕜` represents a linear
map `𝕜ᵈ → 𝕜ᵐ`, then `BᴴQB` is the matrix of the pulled-back form on `𝕜ᵈ`,
and `n₊(BᴴQB) ≤ n₊(Q)`.

## Proof

Via the subspace characterization of `posIndex` (`Sylvester.lean`):
- Let `Vp := range (BᴴQB)₊`, which has dimension `posIndex h(BᴴQB)` and on
  which `BᴴQB` is positive definite (`posDefOn_range_hermPosPart`).
- For `x ∈ Vp ∖ {0}`: `(Bx)ᴴQ(Bx) = xᴴ(BᴴQB)x > 0`, so `Bx ≠ 0`; hence
  `B|_{Vp}` is injective.
- `B(Vp) ⊆ 𝕜ᵐ` has dimension `= dim Vp` and `Q` is positive definite on it.
- By `finrank_le_posIndex_of_posDefOn hQ`, `dim B(Vp) ≤ posIndex hQ`.


### `posIndex_conj_le`

 **Inertia under pull-back** (paper `lem:inertia`, matrix form).
For Hermitian `Q` and any matrix `B`, the pulled-back form `BᴴQB` has
positive index at most that of `Q`. 

### `posIndex_add_le`

 **Subadditivity of the positive index** (paper §3, after `lem:inertia`).
`n₊(Q₁ + Q₂) ≤ n₊(Q₁) + n₊(Q₂)`. 
