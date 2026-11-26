---
{
  "module": "Paper/ApproxRound.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/ApproxRound.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/ApproxRound.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The paper, appendix "Approximate computation": one round, and back to exact values


### `prop_approx_acc_round`

 **Paper: proof of Proposition prop:approx-acc, one round.** "So the new value lies in ∑_e λ^e(pv(z_e) + ε^r E[ε]) ⊆
(value of p) + εE[ε] ⊆ pv(z) + εE[ε]": the new program guesses e, cuts z_e, and lets the interpreter run D on all
pieces with the constants σ_r(κ′), where r exceeds the exponents of all λ^e. 

### `prop_approx_acc_round_num`

 **Paper: proof of Proposition prop:approx-acc, one round with numbers.** 

### `prop_approx_acc_next`

 **Paper: proof of Proposition prop:approx-acc, from one scale to the next.** An approximate accelerator at the scale `u ^ H` gives
one at the scale `(u ^ α) ^ H`; its constants are rescaled copies of the given ones. 

### `prop_approx_acc_exact`

 **Paper: proof of Proposition prop:approx-acc, back to exact values.** "Its value is the coefficient of ε⁰ in the
value of D, that is, pv(z) on plain instances": the coefficients of the powers are new constants with B = 1. 
