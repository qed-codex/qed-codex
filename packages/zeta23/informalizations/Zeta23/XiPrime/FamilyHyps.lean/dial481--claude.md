---
{
  "module": "Zeta23/XiPrime/FamilyHyps.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/FamilyHyps.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/FamilyHyps.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/XiPrime/FamilyHyps.lean — the explicit formula's window-regularity class FamilyHyps (ExplicitFormula.lean §7)
for GENERAL taper families (discharges the last binder of the _flat_std and _quartic ξ′ headlines).

  theorem familyHyps_flat {P : Params} (hP : P.Valid) (hlam : P.lam < 1) : FamilyHyps (fun _ => P)
  (familyHyps_atV for φ_v = √(v(u/L))·φ is in Zeta23/XiPrime/FamilyHypsV.lean, importing §1 below.)

FamilyHyps asks, from some T₀ on: φ_T is C³, tsupport φ_T ⊆ [−L/2, L/2], even, |φ_T| ≤ 1, and ‖φ_T^{(j)}‖_{L¹} ≤ C
for j = 1,2,3 with C independent of T.  For the ramp taper φ(u) = ϱ((L/2−|u|)/w) with a C³ profile ϱ (ϱ ≡ 0 on
(−∞,0], ≡ 1 on [1,∞)) the derivatives φ^{(j)}, 1 ≤ j ≤ 3, live on the two ramps of width w and are bounded by
B·w^{−j}, B := a bound for |ϱ′|,|ϱ″|,|ϱ‴| (continuous, supported in [0,1]), so ‖φ^{(j)}‖₁ ≤ 2B·w^{1−j} ≤ 2B: this is
the Zeta23/Taper/GevreyRamps.lean argument (product form φ = f₊·f₋, mixed Leibniz terms vanish) run at
regularity C³ instead of C^∞ — §1–§2 below.  For φ_v = √(v(u/L))·φ (§3) the factor g(u) = h(u/L), h := √v, is C³ on
a neighbourhood |u| < L(½+η) of the support (v > 0 on [−½,½] ⇒ on [−½−2η, ½+2η]) with |g^{(i)}| ≤ H·L^{−i}, so
Leibniz gives ‖φ_v^{(j)}‖₁ ≤ H·(L·L^{−j} + 2^j·2B) ≤ H(1 + 16B) uniformly in T (L ≥ 1).
-/
```

 ## §1. C³ ramp calculus for a TaperProfile 

### `iteratedDeriv_eq_zero`

 for 1 ≤ i ≤ 3 the i-th derivative of a C³ profile vanishes off (0,1). 

### `exists_deriv_bound`

 a uniform bound for |ϱ^{(i)}|, 1 ≤ i ≤ 3. 

### `abs_iteratedDeriv_fP_le`

 ramp majorants. 

### `iteratedDeriv_fP_mul_fM_eq_zero`

 mixed Leibniz terms vanish (open ramps disjoint when 2w ≤ L). 

### `abs_iteratedDeriv_phi_le`

 |φ^{(k)}| ≤ |f₊^{(k)}| + |f₋^{(k)}|, 1 ≤ k ≤ 3. 

### `abs_iteratedDeriv_phi_le_indicator`

 pointwise ramp majorant for φ^{(k)}. 

### `integral_abs_iteratedDeriv_phi_le`

 **‖φ^{(k)}‖_{L¹} ≤ 2B·w^{1−k}** for 1 ≤ k ≤ 3 (2w ≤ L). 

 ## §2. FamilyHyps for the flat family of ANY valid parameter set 

### `hasCompactSupport_iteratedDeriv'`

 derivatives of every order of a compactly supported function are compactly supported. 

### `familyHyps_flat`

 **FamilyHyps for the flat family** T ↦ P, for every valid P with λ < 1 (any C³ taper profile, any w ≥ 1). 
