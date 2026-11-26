---
{
  "module": "Zeta23/ThmE/CountByIntegralChi.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmE/CountByIntegralChi.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmE/CountByIntegralChi.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/ThmE/CountByIntegralChi.lean — the zero count of L(s,χ) as a contour integral
(χ-analogue of Zeta23/RvM/CountByIntegral.lean).

Λ_sym(s,χ) := q^{s/2}·Λ(s,χ) (Λ = Mathlib's completedLFunction χ, which omits the conductor power):
for primitive χ mod q > 1, Λ_sym is entire, satisfies
Λ_sym(1−s,χ) = W(χ)·Λ_sym(s,χ⁻¹) (W = rootNumber χ ≠ 0), its zeros are exactly the nontrivial zeros
of L(s,χ) (Λ = γ·L on Re s > 0 with γ ≠ 0 [SeamL], L ≠ 0 on Re s ≥ 1 [Mathlib], and the FE for
Re s ≤ 0), with the same analytic orders on the strip. Hence, for heights T₁ ≤ T₂ (ANY sign — no pole)
avoiding the ordinates of zeros,
    (1/2πi) ∮_{∂([−1,2]×[T₁,T₂])} Λ_sym'/Λ_sym = N_χ(T₁,T₂)        (Zeta23.Analytic.rectangleIntegral'_mul_logDeriv).
-/
```

 ## Λ_sym 

### `completedLSym`

 Λ_sym(s,χ) := q^{s/2} · Λ(s,χ) — the symmetrically normalised completed L-function. 

### `completedLSym_one_sub`

 **Functional equation for Λ_sym**: Λ_sym(1−w,χ) = W(χ)·Λ_sym(w,χ⁻¹). 

 ## Zeros and orders of Λ and Λ_sym 

### `completedLFunction_eq_zero_iff`

 The zeros of Λ(·,χ) are exactly the nontrivial zeros of L(·,χ) (primitive χ mod q > 1). 

### `analyticOrderNatAt_completedLFunction`

 On Re ρ > 0 the analytic order of Λ(·,χ) equals zeroMultL χ ρ. 

### `analyticOrderNatAt_completedLSym`

 On Re ρ > 0 the analytic order of Λ_sym(·,χ) equals zeroMultL χ ρ. 

### `logDeriv_completedLSym_split`

 **Bridge for the Γ-side (GammaSideChi).** On Re s > 0 with L(s,χ) ≠ 0:
logDeriv Λ_sym(s,χ) = logDeriv L(s,χ) + logDeriv (z ↦ q^{z/2}·γ_χ(z)) (s). 

 ## The count 

### `rectangleIntegral'_logDeriv_completedLSym_eq_NcountL`

 **N_χ(T₁,T₂) as a contour integral.** For T₁ ≤ T₂ (any sign) with no nontrivial zero of
L(·,χ) of ordinate T₁ or T₂:  (1/2πi)∮_{∂([−1,2]×[T₁,T₂])} Λ_sym'/Λ_sym = NcountL χ T₁ T₂. 
