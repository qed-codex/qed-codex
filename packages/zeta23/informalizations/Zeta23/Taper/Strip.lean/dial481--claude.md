---
{
  "module": "Zeta23/Taper/Strip.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/Taper/Strip.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/Taper/Strip.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23 — Taper/Strip.lean.
[eq:hfbound] specialized to `f = φ`, `Λ_f = L/2` (as consumed by [prop:tail]):
"`|φ̂(r − iy)| ≤ e^{L/4} ‖φ''‖₁ |r − iy|⁻²`" for `|y| ≤ 1/2`.
All three statements are proved here from the general-`f` bounds in Zeta23/Poisson/PaperFT.lean,
and are consumed via `Zeta23.Params.norm_phiHat_*`.
Reference: the paper, §2.1 [eq:hfbound], §4 [prop:tail].
-/
```

### `phiC_contDiff`

 `u ↦ (φ u : ℂ)` is `C³`. 

### `deriv_ofReal_comp`

 `deriv` commutes with the coercion `ℝ → ℂ` for differentiable functions. 

### `norm_phiHat_mul_sq_le`

 [eq:hfbound] for φ: `‖φ̂(z)‖ · ‖z‖² ≤ e^{|Im z|·L/2} · C₁` for all complex `z`,
`C₁ = ‖φ''‖₁`. 

### `integral_phi_le`

 `∫ φ ≤ L` (since `0 ≤ φ ≤ 1` and `supp φ ⊆ [−L/2, L/2]`). 

### `norm_phiHat_le`

 [eq:hfbound] for φ, 0-th order: `‖φ̂(z)‖ ≤ e^{|Im z|·L/2} · ‖φ‖₁ ≤ e^{|Im z| L/2} · L`. 

### `norm_phiHat_sub_I_mul_le`

 The form used in [prop:tail]: for real `r` and `|y| ≤ 1/2`, `z := r − iy ≠ 0`,
`‖φ̂(r − iy)‖ ≤ e^{L/4} C₁ / ‖r − iy‖²`. 
