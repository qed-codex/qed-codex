---
{
  "module": "proof/rates/ClauseBound/Part/Rec.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Part/Rec.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Part/Rec.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # A recurrence for the number of partitions

Taking k copies of the part v away is a bijection from the partitions of E in which v occurs at
least k times to the partitions of E − kv (`card_count_ge`).
Summing the parts of all partitions of E in two ways then gives E·p(E) = Σ_{v ≥ 1} Σ_{k ≥ 1, kv ≤ E}
v·p(E − kv) (`mul_p_eq`): a partition in which v occurs c times
contributes c·v, and c is the number of k ≥ 1 with k ≤ c. 

### `p_zero`

 p(0) = 1. 

### `p_pos`

 p(E) ≥ 1. 

### `card_count_ge`

 The partitions of E in which the part v occurs at least k times are as many as the partitions of
E − kv. 

### `p_mono`

 p is monotone. 

### `mul_p_eq`

 E·p(E) = Σ_{v ≥ 1} Σ_{k ≥ 1, kv ≤ E} v·p(E − kv). 
