---
{
  "module": "Zeta23/XiPrime/QuarticWindow/ModWindow.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/QuarticWindow/ModWindow.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/QuarticWindow/ModWindow.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/XiPrime/QuarticWindow/ModWindow.lean — a MODULATED ramp taper is an admissible window.

Generic once-and-for-all version of Zeta23/ThmD/Window.lean + BridgeD.lean's `admWindow_phiD`: for the tree's ramp
taper φ = Taper.phi ϱ L w and a modulating factor f : ℝ → ℝ that is even, nonnegative, ≤ 1 and nonincreasing on
the core [0, L/2], C² on a neighbourhood of [−L/2, L/2], with |f′| ≤ A/L and |f″| ≤ B/L² on [−L/2, L/2], the window
    φ_f(u) := f(u) · φ(u)
satisfies Zeta23.AdmWindow (φ_f) L w (cMod ϱ A B), cMod := cRho ϱ + A + A² + B (needs 1 ≤ w, 8w ≤ L).  The ξ′
profile windows P.phiV v T (Zeta23/XiPrime/Defs.lean) are the case f u = √(max 0 (v(u/L))) (Quartic.lean); ThmD's
Montgomery–Taylor window is the case f u = √(cos(√2λu/L)).
Mechanism: evenness/support/monotonicity give ‖φ_f′‖₁ = 2φ_f(0) ≤ 2 and ‖(φ_f²)′‖₁ ≤ 2 (total variation of a
unimodal function); the product rule and the taper's own norms ‖φ′‖₁ = 2, ‖φ″‖₁ = 2‖ϱ″‖₁/w, ‖(φ²)′‖₁ = 2,
‖(φ²)″‖₁ ≤ cRho/w (Zeta23/Taper/Norms.lean) give the second-derivative norms, the factor's derivatives costing only
A/L, B/L² ≤ A/(8w), B/(64w²).
-/
```

### `ModFactor`

 hypotheses on a modulating factor (already in the u-variable, i.e. f u = m(u/L)). 

### `phiM`

 the modulated window φ_f := f · φ. 

### `cMod`

 its window constant. 

 ### pointwise / support facts 

### `phiM_contDiff`

 φ_f is C² (f is C² near the core; beyond the core φ_f vanishes identically). 

### `phi_antitoneOn`

 the ramp taper is nonincreasing on [0, ∞). 

### `phiM_antitoneOn`

 φ_f is nonincreasing on [0, ∞). 

 ### total variation of a unimodal function 

### `integral_abs_deriv_le_two`

 an even C¹ function, nonincreasing on [0,∞), with values ≤ 1 and support in [−M, M], has ∫|f'| ≤ 2. 

 ### first-derivative norms 

 ### second derivatives of products (the factor C² only near the core) 

### `deriv2_mul_eq`

 product rule, twice, on an open set where both factors are C². 

### `deriv_mul_eq`

 first product rule on the open set. 

### `deriv2_eq_zero_of_eqOn`

 a function vanishing on an open set has vanishing first and second derivatives there. 

### `integrable_abs_of_cs`

 integrability of |h| for a continuous compactly supported h. 

### `integral_abs_deriv2_mul_le`

 **‖(F·G)″‖₁ ≤ B′‖G‖₁ + 2A′‖G′‖₁ + ‖G″‖₁** for G ∈ C_c²[−L/2, L/2] and F C² near [−L/2, L/2] with
|F| ≤ 1, |F′| ≤ A′, |F″| ≤ B′ there. 

 ### the L¹ size of the taper and its square 

 ### second-derivative norms of φ_f and φ_f² 

### `ModFactor.abs_le_one`

 |f| ≤ 1 on the core. 

### `integral_abs_deriv2_phiM_le`

 **‖φ_f″‖₁ ≤ cMod/w.** 

### `phiM_sq_eq`

 φ_f² as a product of the squared factor and the squared taper. 

### `integral_abs_deriv2_phiM_sq_le`

 **‖(φ_f²)″‖₁ ≤ cMod/w.** 

 ### the admissible-window instance 

### `admWindow_phiM`

 **A modulated ramp taper is an admissible window.** 
