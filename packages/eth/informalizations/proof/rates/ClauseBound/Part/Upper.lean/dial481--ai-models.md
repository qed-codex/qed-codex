---
{
  "module": "proof/rates/ClauseBound/Part/Upper.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Part/Upper.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Part/Upper.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # p(E) ≤ exp(π·√(2E/3))

Induction on E through the recurrence E·p(E) = Σ_{v,k ≥ 1, kv ≤ E} v·p(E − kv), the method of Erdős.
Let c = π·√(2/3) and a = c/(2√E). By √(E − x) ≤ √E − x/(2√E) and the
induction hypothesis, p(E − kv) ≤ exp(c√E)·exp(−akv). For y > 0 we have Σ_{v ≥ 1} v·e^{−yv} =
e^{−y}/(1 − e^{−y})² ≤ 1/y², and Σ_{k ≥ 1} 1/(ak)² = (π²/6)/a² = E. 

### `cHR_pos`

 c = π·√(2/3) is positive. 

### `cHR_sq`

 c² = 2π²/3. 

### `sqrt_sub_le`

 √(n − x) ≤ √n − x/(2√n) for x ≤ n. 

### `exp_div_le`

 e^{−y}/(1 − e^{−y})² ≤ 1/y² for y > 0. 

### `sum_mul_exp_le`

 Σ_v v·e^{−yv} ≤ 1/y² over any finite set of v, for y > 0. 

### `sum_inv_sq_le`

 Σ_k 1/k² ≤ π²/6 over any finite set of k. 

### `p_le_exp`

 p(E) ≤ exp(π·√(2E/3)). 
