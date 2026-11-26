---
{
  "module": "proof/rates/ClauseBound/Alg/Need.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Alg/Need.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Alg/Need.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The exponent of a pad that suffices for all levels (`StNeedG`)

`FitsG P F …` lists what the descent through a schedule needs of the length F of the pad: one
inequality «… ≤ F» for every loop and every state. `needG P …` is the largest of
the exponents of these inequalities and of the label length and the numbers of binary digits of B
and of the number of nodes (these three are there for the computation of `needG` under a
bound). Here: a pad of length at least 2^needG satisfies all the inequalities (`fitsG_of_le`,
`stNeedG`). 

### `le_of_size_le`

 A number with at most n binary digits is at most F if 2^n ≤ F. 

### `pow_le_of_le`

 2^a ≤ F if a ≤ n and 2^n ≤ F. 

### `pow_le_two_pow_size`

 K^p ≤ 2^(p · number of binary digits of K). 

### `fitsG_of_le`

 The budgets hold for every pad of length at least 2^n, as soon as n is at least `needG`. 

### `stNeedG`

 `StNeedG`: a pad of length at least 2^needG suffices for all levels. 
