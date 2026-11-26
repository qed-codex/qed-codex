---
{
  "module": "Zeta23/ThmE/LGrowth.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmE/LGrowth.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmE/LGrowth.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/ThmE/LGrowth.lean — growth of L(s,χ) in vertical strips (input to
H-RvM(χ): the local count, Backlund's bound and the contour count all consume it; analogue of
Zeta23/RvM/ZetaGrowth.lean).

For a nontrivial character χ mod q the partial sums S(t) := Σ_{1≤k≤t} χ(k) are bounded by q, so Abel
summation gives the representation
    L(s,χ) = s ∫_1^∞ S(t) t^{−s−1} dt        (Re s > 0)
(Mathlib: LSeries_eq_mul_integral for Re s > 1 + LFunction_eq_LSeries; extended to Re s > 0 by
analytic continuation — the right side is holomorphic there and L(·,χ) is entire). Consequences:
 • `norm_LFunction_le_of_re_pos` : ‖L(s,χ)‖ ≤ q·‖s‖ / Re s  (Re s > 0);
 • `LFunction_growth_right` : ∃ A C, ∀ s, 0.15 ≤ Re s → ‖L(s,χ)‖ ≤ C·(|Im s|+3)^A (C depends on q);
 • `norm_LFunction_sub_one_le` : ‖L(s,χ) − 1‖ ≤ π²/6 − 1 on Re s ≥ 2, hence 1/3 ≤ ‖L(2+it,χ)‖ ≤ π²/6.
The continuation to Re s > 0 uses that the
Abel integral is a Mellin transform (Mathlib's mellin_differentiableAt_of_isBigO_rpow) + the identity theorem.
[Dav00 §§ 4, 16; Tit86 §2.1 analogue]
-/
```

 ## Partial sums of a nontrivial character 

### `sum_Ico_add_period_eq_zero`

 A full period of a nontrivial character sums to zero, from any starting point. 

### `norm_sum_Icc_le`

 Partial sums of a nontrivial character are bounded by the modulus:
‖Σ_{k=1}^{n} χ(k)‖ ≤ q. 

 ## The Abel integral as a Mellin transform; continuation to Re s > 0 

### `abelKernel`

 The Abel kernel: t ↦ 1_{t>1}·Σ_{1≤k≤t} χ(k). 

### `LFunction_eq_mul_integral`

 **Abel-summation representation on Re s > 0**:
L(s,χ) = s · ∫_1^∞ (Σ_{1≤k≤t} χ(k)) · t^{−(s+1)} dt. 

 ## Growth bounds 

### `norm_LFunction_le_of_re_pos`

 **Half-plane bound**: ‖L(s,χ)‖ ≤ q·‖s‖/Re s for Re s > 0. 

### `LFunction_linear_growth`

 δ-form, linear: for Re s ≥ δ > 0, ‖L(s,χ)‖ ≤ q·(1 + δ⁻¹)·(|Im s| + 1). 

### `LFunction_growth_right`

 **Polynomial (linear) growth to the right of σ = 0.15** (shape parallel to
Zeta23.RvM.zeta_growth_right; the constant depends on q; no condition at s = 1 — L(·,χ) is entire). 

 ## Re s ≥ 2 

### `norm_LFunction_sub_one_le`

 On Re s ≥ 2: ‖L(s,χ) − 1‖ ≤ π²/6 − 1 (Dirichlet series, |χ| ≤ 1). 

### `LFunction_lower_bound_two`

 Lower bound at the Jensen disc centre: 1/3 ≤ ‖L(s,χ)‖ for Re s ≥ 2. 

### `norm_LFunction_le_of_two_le_re`

 Upper bound on Re s ≥ 2: ‖L(s,χ)‖ ≤ π²/6. 

### `LFunction_growth_right_uniform`

 **q-uniform growth, absolute constants** (for the hybrid range): for every nontrivial χ mod q and
Re s ≥ 0.15, ‖L(s,χ)‖ ≤ 8·q·(|Im s| + 3). 
