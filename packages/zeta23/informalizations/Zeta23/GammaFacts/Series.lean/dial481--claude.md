---
{
  "module": "Zeta23/GammaFacts/Series.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/GammaFacts/Series.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/GammaFacts/Series.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/GammaFacts/Series.lean — the digamma partial-fraction series.

Target:  digamma z = −γ − 1/z + ∑'_{n≥0} (1/(n+1) − 1/(z+n+1))   for z ∈ ℂ_ℤ,
the Mathlib-missing piece needed for the remaining H-Γ fields
([eq:mufacts]; see Zeta23/GammaFacts.lean).  Route (modelled on Mathlib's
Analysis/SpecialFunctions/Trigonometric/Cotangent.lean, which does the same for
sin → cot):
  1. Weierstrass factors  1 + wTerm n z = (1 + z/(n+1))·e^{−z/(n+1)}, with
     ‖wTerm n z‖ ≤ 3(‖z‖/(n+1))² for n+1 ≥ ‖z‖  (M-test input);
  2. the finite identity  (GammaSeq z N)⁻¹ = z·e^{(H_N − log N)z}·∏_{n<N}(1+wTerm n z);
  3. N → ∞ (GammaSeq_tendsto_Gamma + tendsto_harmonic_sub_log):
       Γ(z)⁻¹ = z·e^{γz}·∏'_n (1 + wTerm n z)            [Weierstrass product]
  4. logDeriv via Complex.logDeriv_tprod_eq_tsum          [digamma series].
This file has steps 1–3; step 4 is `digamma_series` at the bottom.
-/
```

### `wTerm`

 Offset Weierstrass factor: `1 + wTerm n z = (1 + z/(n+1))·e^{−z/(n+1)}`. 

### `norm_wTerm_le`

 The quadratic tail bound for the Weierstrass factor. 

 ### The finite identity and the Weierstrass product 

### `inv_gammaSeq_eq`

 The finite identity: (GammaSeq z N)⁻¹ = z·e^{(H_N − log N)z}·∏_{n<N}(1 + wTerm n z). 

### `inv_gamma_eq_prod`

 **The Weierstrass product for 1/Γ** on the integer complement:
Γ(z)⁻¹ = z·e^{γz}·∏'ₙ (1 + z/(n+1))e^{−z/(n+1)}. 

### `logDeriv_one_add_wTerm`

 The logarithmic derivative of a single Weierstrass factor. 

### `summable_digamma_series`

 Summability of the digamma partial-fraction series. 

### `hasSum_digamma_series`

 **The digamma partial-fraction series, HasSum form**:
Σₙ (1/(n+1) − 1/(z+n+1)) converges to ψ(z) + γ + 1/z on the integer complement. 

### `digamma_series`

 **The digamma partial-fraction series** (paper [eq:mufacts]'s parenthetical, the
keystone for the remaining H-Γ fields):
ψ(z) = −γ − 1/z + Σ'ₙ (1/(n+1) − 1/(z+n+1)) for z off the integers. 
