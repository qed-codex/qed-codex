---
{
  "module": "Zeta23/Taper/GevreyRamps.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/Taper/GevreyRamps.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/Taper/GevreyRamps.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/Taper/GevreyRamps.lean — Gevrey ramp lemma:
for a Gevrey-s profile ϱ (`Taper.GevreyProfile s A B ϱ`), the concrete taper
φ(u) = ϱ((L/2 − |u|)/w) is C^∞ and ‖φ^{(k)}‖_{L¹} ≤ 2B·w·(A/w)^k·k^{sk} for every k ≥ 1.
Route: the product form φ = f₊·f₋ with f_±(u) = ϱ((L/2 ∓ u)/w) (Taper.phi_eq_mul, needs 2w ≤ L);
ϱ^{(i)} (i ≥ 1) vanishes off (0,1) (closure argument at the two endpoints), so in the Leibniz
expansion only i = 0 and i = k survive and |φ^{(k)}| ≤ |f₊^{(k)}| + |f₋^{(k)}|; each is
w^{−k}|ϱ^{(k)}| ∘ (affine), bounded by w^{−k}BA^k k^{sk} on a ramp of length w and 0 elsewhere.
Produces the interface `Params.GevreyPhiBound` (Zeta23/Taper/GevreyPhi.lean).
-/
```

### `GevreyProfile.iteratedDeriv_eq_zero`

 for `i ≥ 1`, the `i`-th derivative of a profile vanishes off the open unit interval. 

### `GevreyProfile.abs_iteratedDeriv_le_indicator`

 pointwise majorant: `|ϱ^{(k)}(x)| ≤ B A^k k^{sk} · 1_{(0,1)}(x)` for `k ≥ 1`. 

### `iteratedDeriv_ofReal_comp`

 `iteratedDeriv` commutes with the coercion ℝ → ℂ for smooth functions. 

### `fP`

 the two one-sided ramps `f_±(u) = ϱ((L/2 ∓ u)/w)`. 

### `abs_iteratedDeriv_fP_le`

 ramp majorants: `|f₊^{(k)}(u)| ≤ w^{−k}BA^k k^{sk}·1_{(L/2−w, L/2)}(u)` and symmetrically. 

### `iteratedDeriv_fP_mul_fM_eq_zero`

 mixed Leibniz terms vanish: for `1 ≤ i`, `1 ≤ j` and `2w ≤ L`,
`f₊^{(i)}(u)·f₋^{(j)}(u) = 0` (the open ramps are disjoint). 

### `abs_iteratedDeriv_phi_le`

 **|φ^{(k)}| ≤ |f₊^{(k)}| + |f₋^{(k)}|** for `k ≥ 1`. 

### `integral_abs_iteratedDeriv_phi_le`

 **Gevrey ramp lemma**: `‖φ^{(k)}‖_{L¹} ≤ 2B·w·(A/w)^k·k^{sk}` (`k ≥ 1`, `2w ≤ L`). 

### `Params.gevreyPhiBound_of_profile`

 **Gevrey ramp lemma, in the `Params.GevreyPhiBound` interface**: a Gevrey-s profile makes
`P.phi T` a C^∞ window with ‖φ^{(k)}‖₁ ≤ 2B·w·(A/w)^k·k^{sk}. 
