---
{
  "module": "proof/rates/PaddedDescent/F/ArithWalk.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/ArithWalk.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/ArithWalk.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 The number of leaves of the sparsification tree for clauses of width k, as a power of two with a
natural exponent: the bound of the sparsification lemma on the number of leaves is at most
2^(⌊n/2^s⌋+1) for the threshold τ = tauOf s, as soon as s ≥ s0K k. The estimate of the sum of
binomial coefficients is `WidthK.stLeafCount`. 

### `sum_choose_le_two_pow`

 The bound of the sparsification lemma for the number of leaves, for width k and s ≥ s0K k, is at
most 2^(⌊n/2^s⌋+1). 
