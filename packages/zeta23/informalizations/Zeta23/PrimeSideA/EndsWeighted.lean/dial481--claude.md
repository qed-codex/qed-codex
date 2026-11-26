---
{
  "module": "Zeta23/PrimeSideA/EndsWeighted.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/PrimeSideA/EndsWeighted.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/PrimeSideA/EndsWeighted.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/PrimeSideA/EndsWeighted.lean

Substrate for the 𝓔₂ bound [lem:ends], shared with EndsNu.lean (the
1-D estimates N1/N2): log⁺/√ facts, pointwise ν-bounds from NuBound, integrability of the
ψ-weighted ν integrals, and the grid-domination lemmas reducing Σ_{k<d} ψ(τ−τ_k) to
Σ_{j<d} ψ(Δ + jh), Δ = dist(τ, I).
-/
```

### `psiA_shift_integrable`

 ψ(· − a) is integrable. 

### `integral_psiA_shift`

 ∫ ψ(τ − a) dτ = ∫ ψ. 

### `integrable_psiA_mul_sqrt`

 ψ(r)·√|r| is integrable (L·√|r| near 0, (c/w)|r|^(−3/2) at infinity). 

### `integrable_psiA_shift_mul_nu`

 ψ(· − a)·|ν| is integrable, for a ∈ [T, 2T]. 

### `sum_psiA_shift_left`

 Left grid domination: for τ ≤ T the distances to the grid points T + k·h are exactly
(T − τ) + k·h (evenness of ψ). 

### `sum_psiA_shift_right`

 Right grid domination: for 2T ≤ τ and grid points T + k·h ≤ 2T (k < d), after reflecting the
index the distances dominate (τ − 2T) + j·h (ψ antitone on [0,∞)). 
