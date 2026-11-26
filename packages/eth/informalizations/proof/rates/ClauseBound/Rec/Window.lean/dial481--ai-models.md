---
{
  "module": "proof/rates/ClauseBound/Rec/Window.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Rec/Window.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Rec/Window.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Signs and binomial coefficients

Two lemmas: for a natural number j, the sign written with a case distinction on the parity of j is
(−1)^j; and for an integer a of any sign, the binomial coefficient C(a, k) = a(a − 1)⋯(a − k + 1)/k!
(`Ring.choose`) satisfies |C(a, k)| ≤ 2^(|a| + k). 

### `ite_even_natCast`

 The sign written with a case distinction is the power of −1. 

### `abs_choose_le`

 |C(a, k)| ≤ 2^(|a| + k). 
