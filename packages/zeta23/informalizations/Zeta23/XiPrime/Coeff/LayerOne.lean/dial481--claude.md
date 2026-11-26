---
{
  "module": "Zeta23/XiPrime/Coeff/LayerOne.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Coeff/LayerOne.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Coeff/LayerOne.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/XiPrime/Coeff/LayerOne.lean — the ω = 1 (prime) layer of the diagonal law H3.

  sfPart Λs 1 y = Σ_{p ≤ e^y} ‖C(p;Λs)‖²/p = l²·(s²/2 − 4s³/3 + s⁴) + O(1+l),   s = y/l,
uniformly in 0 ≤ y ≤ l, for Re Λs = l/2, |Im Λs| ≤ 1, l ≥ 2.  Route: C(p;Λs) = −log p + Λs⁻¹(log p)²
(MainTerm's xiCoeff_prime), so ‖C(p)‖² = L² − 2·Re(Λs⁻¹)·L³ + ‖Λs‖⁻²·L⁴ (L = log p); the three prime sums
Σ(log p)^b/p = y^b/b + O((1+y)^{b−1}) (PrimeSums.prime_logpow_sum, b = 2,3,4); and the parameter
estimates Re(Λs⁻¹) = 2/l + O(l⁻³), ‖Λs‖⁻² = 4/l² + O(l⁻⁴) (Coeff/Param).
-/
```

### `norm_sq_prime_term`

 `‖−L + z·L²‖² = L² − 2·Re z·L³ + |z|²·L⁴` for real `L`. 

### `re_sq_add_im_sq_inv`

 `(Re Λ⁻¹)² + (Im Λ⁻¹)² = ‖Λ‖⁻²`. 

### `primeLogPowSum`

 the prime sums `S_b(y) := Σ_{p ≤ e^y, p prime} (log p)^b / p`. 

### `sfPart_one_eq`

 the ω = 1 layer in terms of the three prime sums. 

### `sfPart_one_asymp`

 **The ω = 1 layer of H3**: `sfPart Λs 1 y = l²(s²/2 − 4s³/3 + s⁴) + O(1+l)`, `s = y/l`, uniformly in
`0 ≤ y ≤ l`, for every `Λs` with `Re Λs = l/2`, `|Im Λs| ≤ 1`, `l ≥ 2`. 
