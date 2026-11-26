---
{
  "module": "Zeta23/PrimeSideA/CrossMuPCore.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/PrimeSideA/CrossMuPCore.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/PrimeSideA/CrossMuPCore.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Analytic core of [prop:cross] (i): the double integration by parts for `𝓜[u, cos(·y)]`

See `Zeta23/PrimeSideA/CrossMuP.lean` for the statement of [prop:cross](i) and the paper text.


### `setIntegral_sq_shift_le_left`

 `∫_S Φ(x−y)² dy ≤ ∫_ℝ Φ²`. 

### `setIntegral_Icc_eq_intervalIntegral`

 Icc-set-integral = interval integral (`T ≤ 2T`). 

### `Mform_eq_iter`

 Fubini for `𝓜` with the first variable outer:
`𝓜[u,v] = ∫_I u(τ) (∫_I Φ(τ−τ′)² v(τ′) dτ′) dτ`. 

### `setIntegral_sq_shift_le'`

 `∫_S Φ(y − c)² dy ≤ ∫_ℝ Φ²` (translation invariance, `Φ² ≥ 0`). 

### `outer_ibp`

 **IBP in `τ`** (§5.4 "integrating by parts in τ"), for fixed `τ′`:
`∫_T^{2T} u(τ)(Φ²)′(τ−τ′) dτ = u(2T)Φ(2T−τ′)² − u(T)Φ(T−τ′)² − ∫_T^{2T} u′(τ)Φ(τ−τ′)² dτ`. 

### `inner_ibp_phase`

 **IBP in `τ′`** (§5.4 "integrating by parts"), for fixed `τ`, `y ≠ 0` and a phase `θ`:
`∫_T^{2T} Φ(τ−τ′)² cos(τ′y+θ) dτ′ = [Φ(τ−τ′)² sin(τ′y+θ)/y]_T^{2T} + y⁻¹ ∫_T^{2T} (Φ²)′(τ−τ′) sin(τ′y+θ) dτ′`. 

### `abs_Mform_cos_phase_le`

 **The oscillatory bound** (§5.4: "`|∫_I m(τ′)cos(τ′y)dτ′| ≤ (2 sup|m| + ∫_I|m′|)/y`"), in the explicit,
phase-shifted form: if `Φ, u ∈ C¹`, `|u| ≤ B` and `|u′| ≤ D` on `I = [T,2T]`, `T ≥ 0`, `y ≠ 0`, then for every
phase `θ`, `|𝓜[u, cos(·y + θ)]| ≤ (4B + D·T)·(∫_ℝ Φ²)/|y|` (covers `sin` at `θ = −π/2`; used for the
complex-coefficient prime sums of Theorem E, where `Re(c·e^{−iτy}) = ‖c‖·cos(τy − arg c)`; the case `θ = 0` is
`abs_Mform_cos_le` below). 

### `abs_Mform_cos_le`

 **The oscillatory bound** (§5.4: "`|∫_I m(τ′)cos(τ′y)dτ′| ≤ (2 sup|m| + ∫_I|m′|)/y`"), here in
the explicit form: if `Φ, u ∈ C¹`, `|u| ≤ B` and `|u′| ≤ D` on `I = [T,2T]`, `T ≥ 0`, `y ≠ 0`, then
`|𝓜[u, cos(·y)]| ≤ (4B + D·T)·(∫_ℝ Φ²)/|y|` — the case `θ = 0` of `abs_Mform_cos_phase_le`. 
