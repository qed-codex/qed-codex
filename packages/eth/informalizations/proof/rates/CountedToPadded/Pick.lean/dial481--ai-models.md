---
{
  "module": "proof/rates/CountedToPadded/Pick.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedToPadded/Pick.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedToPadded/Pick.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The program that picks the level

Proof of `PickOfFacts` (Defs.lean). The list of the entries that `kf` finds is followed from ℓ = 0
upwards: after the first m numbers its last entry belongs to the largest ℓ < m with K_ℓ within the
bound. 

### `eq_unary`

 A list of units is its length in unary. 

### `take_unary`

 The first ℓ units of b are ℓ in unary, for ℓ within the length of b. 

### `add_two_le_K`

 K_ℓ ≥ ℓ + 2. 

### `cand`

 The entry for ℓ: (ℓ, (ℓ, K_ℓ)), all in unary, if `kf` finds K_ℓ within the bound b; else
nothing. 

### `cand_eq`

 The entry for ℓ within the length of b, by what `kf` computes. 

### `last_succ`

 The last entry among the first m + 1 numbers is that of m, if there is one, else the last among
the first m. 

### `last_spec`

 After the first m numbers: nothing, if no K_ℓ with ℓ < m is within the bound; else the entry of
the largest such ℓ. 

### `pickOf_eq`

 The program, written with `cand`. 

### `pickOfFacts`

 The program that picks the level is polynomial-time and returns the index of the largest level
within the bound. 
