---
{
  "module": "Zeta23/Taper/Norms.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/Taper/Norms.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/Taper/Norms.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 ### [eq:phinorms] 

### `deriv_nonneg_of_monotone`

 A monotone function has nonnegative derivative wherever it is differentiable. 

### `deriv_phi_pos`

 For u > 0, φ′(u) = −ϱ′((L/2 − u)/w)/w. 

### `integral_abs_deriv_eq_two`

 ∫ℝ |F′| = 2 for an even C¹ bump: F(0) = 1, F = 0 off [−L/2, L/2], F′ ≤ 0 on (0,∞). 

### `integral_abs_deriv_phi`

 [eq:phinorms]: "`‖φ'‖₁ = 2`". 

### `integral_abs_deriv_phi_sq`

 [eq:phinorms]: "`‖(φ²)'‖₁ = 2`". 

### `derivRho_zero_left`

 deriv ϱ vanishes left of 0 (ϱ is locally 0 there). 

### `derivRho_zero_right`

 deriv ϱ vanishes right of 1 (ϱ is locally 1 there). 

### `abs_deriv_phi_le`

 [eq:phinorms]: "`‖φ'‖_∞ = ‖ϱ'‖_∞ / w`" (we record `≤`, which is what is used). 

### `deriv2_phi_pos`

 For u > 0, φ″(u) = ϱ″((L/2 − u)/w)/w². 

### `integral_abs_eq_two_mul`

 Even-integrand reduction: ∫ℝ |G| = 2∫₀^{L/2} |G| for |G| even, G = 0 off [−L/2, L/2]. 

### `integral_abs_deriv2_phi`

 [eq:phinorms]: "`‖φ''‖₁ = 2‖ϱ''‖₁ / w`". 

### `integral_abs_deriv2_phi_sq_le`

 [eq:phinorms]: "`‖(φ²)''‖₁ ≤ c_ϱ / w`" (uses `w ≥ 1`). 

### `four_le_cRho`

 [eq:phinorms]: "`c_ϱ (≥ 4)`". 

### `C1_le`

 "Finally `C₁ ≤ 2‖ϱ''‖₁` as `w ≥ 1`" [prop:tail proof, last lines]. 

 ### [eq:abdef]: "`1 − 2w/L ≤ b ≤ a ≤ 1`" 
