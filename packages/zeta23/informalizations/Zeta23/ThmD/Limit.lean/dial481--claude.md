---
{
  "module": "Zeta23/ThmD/Limit.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmD/Limit.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmD/Limit.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/ThmD/Limit.lean — Theorem D endgame: the exact-constant limit.
 (L1) cRatio at the starred data IS c*_λ;
 (L2) the concrete window data converges: cRatio(λ₁(T), a_D(T), b_D(T), J_D(T)) → c*_λ as T → ∞;
 (L3) the λ → 1⁻ ε-step for the three Theorem-D rates (HD, 2c*−1, c*), by the Lipschitz bound.
-/
```

 ### (L1) the starred ratio 

 ### range facts 

### `vStar_nonneg_on`

 vStar is nonnegative on the unit window. 

### `jStar_nonneg`

 J* ≥ 0 (integral of a pointwise-nonnegative kernel). 

### `star_denom_pos`

 the denominator of the starred ratio is strictly positive. 

 ### (L3) the λ → 1⁻ ε-step 

### `eps_form_of_approx`

 generic form: if the target constant is approached from the left in the rate scale, the
ε-statement at every λ < 1 upgrades to the ε-statement at λ = 1. 

### `approx_of_continuousWithinAt`

 left-approximation at 1 from continuity within [0,1]: the `hg` hypothesis of `eps_form_of_approx`. 

### `eps_form_cStar`

 the c*-rate ε-step. 

### `eps_form_twoCStar`

 the (2c* − 1)-rate ε-step. 

### `eps_form_HD`

 the HD-rate ε-step (HD = 2 − 1/c*; c* 1 > 0 makes 1/c* continuous at 1 within [0,1]). 

 ### (L2) convergence of the concrete data 

### `tendsto_lam1`

 λ₁(T) → λ. 

### `tendsto_of_close`

 generic: data within C·w/L of a constant converges to it. 

### `tendsto_aD`

 the three concrete D-window moment limits, exported standalone. 

### `tendsto_cRatio_of`

 generic ratio limit: any λ₁-like sequence tending to λ and any data tending to the starred
moments give cRatio → c*_λ. 

### `tendsto_cRatio_concrete`

 **(L2)**: the concrete Montgomery–Taylor window ratio converges to c*_λ. 
