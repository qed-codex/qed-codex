---
{
  "module": "Zeta23/WeilEF/ZeroSummability.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/WeilEF/ZeroSummability.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/WeilEF/ZeroSummability.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 ### γ_ρ bookkeeping 

### `abs_gammaOf_im_lt`

 For a point of the open strip, |Im γ_ρ| < 1/2. 

### `abs_gammaOf_im_le`

 For a point of the closed strip, |Im γ_ρ| ≤ 1/2. 

 ### The weight series Σ_{n∈ℤ} log(|n|+3)/(1+n²) 

### `weight_le`

 log(|n| + 3)/(1 + n²) ≤ 4 |n|^{−3/2} for n ≠ 0. 

### `totalWeight`

 The total weight W := Σ'_{n∈ℤ} log(|n|+3)/(1+n²). 

 ### zero_sum_inv_sq 

### `key`

 unit-window key of an ordinate: n := ⌈y⌉ − 1, so that n < y ≤ n + 1. 

### `one_add_sq_ge`

 if n < y ≤ n+1 then 1 + y² ≥ (1 + n²)/4. 

 ### The generic theorems (any ZeroConfig with the local count) 

### `zero_sum_inv_sq_gen`

 **Σ_ρ m_ρ/(1+|γ_ρ|²) converges** for ANY zero configuration with a two-sided local count
N(t,t+1] ≤ A₀ log(|t|+3) (dyadic/unit-window summation of the local count). 

### `EF_zero_sum_summable_gen`

 The EF zero-side sum converges absolutely for every k ∈ C_c²(ℝ), for ANY zero configuration with
the local count (via [eq:hfbound]: ‖h(γ_ρ)‖ ≤ e^{Λ/2}‖k''‖₁/‖γ_ρ‖², |Im γ_ρ| < 1/2). 

 ### The ζ instances 

### `zero_sum_inv_sq`

 **Σ_ρ m_ρ/(1+|γ_ρ|²) converges** (dyadic/unit-window summation of the local count). 

 ### EF_zero_sum_summable 

### `EF_zero_sum_summable`

 The EF zero-side sum converges absolutely for every k ∈ C_c²(ℝ)
(via [eq:hfbound]: ‖h(γ_ρ)‖ ≤ e^{Λ/2}‖k''‖₁/‖γ_ρ‖², |Im γ_ρ| < 1/2) — EF_lit's Summable clause. 
