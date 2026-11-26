---
{
  "module": "NS1/OneCut.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/NS1/OneCut.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/NS1/OneCut.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Cuts one after the other

From one cut by any factor k ≤ v ^ 64 at the scale v, cuts down to v ^ H steps: the induction on the numbers of steps,
sizes and pieces.


### `OneCutAt`

 The hypothesis at one `v`. 

### `_root_.Paper.thm_cut_iterate`

 **Paper: Theorem thm:cut, the induction on (τ_i, s_i, P_i).** Cut by v^63 as long as the steps are many, and at last
once to v^H; sizes, pieces and time. 

### `le_lg_of_lg_pow_le`

 Powers of the logarithm that are at most `v` bound the exponent by the logarithm. 

### `polylog_loss_le`

 The iterated cuts lose at most `v`, if `(lg v) ^ (C₀ * α) ≤ v` for the constant `C₀` below. 
