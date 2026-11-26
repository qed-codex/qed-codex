---
{
  "module": "proof/threesat/Printed/Absorb.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/Printed/Absorb.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/Printed/Absorb.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # One constant for a polynomial bound

Definition 4 and Lemma 1 write their polynomial factors as C·(B + λ)^C and C₁·(P + B)^{C₁}, one
constant for factor and exponent. The theorems of this development give bounds of the form s +
a·y^a, where s and y are at most linear in x = B + λ. These lemmas put such a bound under Cc·x^Cc,
with a ≤ Cc, so that the bound on the time can be raised to the same constant. 

### `absorb`

 For all a and k there is Cc ≥ a with k·x + a·(k·x)^a ≤ Cc·x^Cc for all x ≥ 1. 

### `absorb_le`

 The same for any s and y that are at most k·x. 

### `absorb_time`

 A bound a·p·x^a on the time may be raised to Cc·p·x^Cc, for a ≤ Cc and x ≥ 1. 
