---
{
  "module": "Zeta23/ThmE/LocalCountChi.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmE/LocalCountChi.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmE/LocalCountChi.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
The two-sided local zero count for L(s,χ):
  N_χ(t, t+1] ≤ A₀ log(|t|+3)  for ALL real t  (A₀ depends on q through the growth constants) —
  derived from the q-uniform count `localCountChi_uniform_proof` (one absolute A₀, log(q(|t|+3))).
Route: halve by Zeta23.ZeroConfig.N_le_two_mul_half
(applied to LZeros), then ZerosBound on g(w) := L(c₀+1.9w,χ)/L(c₀,χ),
c₀ = 2+(t+½)i, r = .84, R = .95, with Zeta23.ThmE.LFunction_growth_right / LFunction_lower_bound_two;
L(·,χ) is entire for χ ≠ 1, so no pole bookkeeping and no |t| ≥ 4 split.
-/
```

### `gfunL`

 rescaled L: w ↦ L(c₀ + κ w, χ) · u. 

 ## The q-UNIFORM count (one absolute A₀ for every primitive χ mod q > 1) 

### `localCountChi_uniform_proof`

 **q-uniform local count**: ONE absolute A₀ with
N_χ(t,t+1] ≤ A₀·log(q(|t|+3)) for every primitive χ mod q > 1.  Same disc/ZerosBound argument as the ζ local
count, with the uniform linear growth ‖L(s,χ)‖ ≤ 8q(|Im s|+3) (LFunction_growth_right_uniform) so that log B
stays additive in log q. 

### `localCountChi`

 **Local count for L(s,χ)**, two-sided (per-χ constant; from the q-uniform count:
log(q(|t|+3)) = log q + log(|t|+3) ≤ (1 + log q)·log(|t|+3) as log(|t|+3) ≥ 1). 
