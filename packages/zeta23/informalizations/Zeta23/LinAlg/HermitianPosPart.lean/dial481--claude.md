---
{
  "module": "Zeta23/LinAlg/HermitianPosPart.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/LinAlg/HermitianPosPart.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/LinAlg/HermitianPosPart.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

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


# Positive and negative parts of a Hermitian matrix

For a Hermitian matrix `Q` with spectral decomposition `Q = U diag(λ) Uᴴ`,
define `Q₊ := U diag(λ⁺) Uᴴ` and `Q₋ := U diag(λ⁻) Uᴴ` where
`λ⁺ = max(λ,0)`, `λ⁻ = max(−λ,0)`.

Then `Q = Q₊ − Q₋`, both are PSD, `Q₊ Q₋ = 0`, and `rank Q₊ = n₊(Q)`.

This is equivalent to the CFC `Q⁺`/`Q⁻` via `Matrix.IsHermitian.cfc_eq`, but
the direct spectral construction keeps the eigenvalue bookkeeping explicit,
which is what the rank–trace proof needs.


### `specMap`

 Apply a real function to a Hermitian matrix via its spectral decomposition:
`specMap hA f := U diag(f ∘ λ) Uᴴ`. (This is `Matrix.IsHermitian.cfc`, reproduced
here to keep imports light and bookkeeping explicit.) 

### `hermForm_specMap`

 The Hermitian form `xᴴ(specMap hA f)x` in eigenbasis coordinates:
setting `c := Uᴴx`, we have `Re(xᴴ(specMap hA f)x) = ∑ᵢ f(λᵢ)·‖cᵢ‖²`. 

### `rtrace_specMap`

 The real-valued trace of `specMap hA f` is `∑ᵢ f(λᵢ)`. 

### `frobSq_specMap`

 The squared Frobenius norm of `specMap hA f` is `∑ᵢ f(λᵢ)²`. 

### `rank_specMap`

 The rank of `specMap hA f` is the number of `i` with `f(λᵢ) ≠ 0`. 

### `specMap_posSemidef`

 `specMap hA f` is PSD whenever `f(λᵢ) ≥ 0` for all `i`. 

### `hermPosPart`

 Positive part `A₊ := U diag(λ⁺) Uᴴ`. 

### `hermNegPart`

 Negative part `A₋ := U diag(λ⁻) Uᴴ`. 
