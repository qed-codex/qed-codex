---
{
  "module": "proof/rates/ClauseBound/Rec/Tail.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Rec/Tail.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Rec/Tail.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Hoeffding's lemma on two points

`two_point_le`, in the namespace `ClauseBound.Rec.Tail`: p·e^{θ(1−p)} + (1−p)·e^{−θp} ≤ e^{θ²/8} for
0 ≤ p ≤ 1. This is Hoeffding's lemma for a random variable with values in {0, 1}.
It is taken from Mathlib's sub-Gaussian bound for a random variable with values in [0, 1], applied
to the measure with mass p at 1 and mass 1 − p at 0. 

### `two_point_le`

 Hoeffding's lemma on two points: p·e^{θ(1−p)} + (1−p)·e^{−θp} ≤ e^{θ²/8} for 0 ≤ p ≤ 1. 
