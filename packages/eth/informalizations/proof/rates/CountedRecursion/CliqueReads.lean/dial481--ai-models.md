---
{
  "module": "proof/rates/CountedRecursion/CliqueReads.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/CliqueReads.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/CliqueReads.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # What the value of a clique reads, and the value of a callee

* `clique_value_congr`: the value of the (K, λ)-clique reads its tables only on settings (strings of
  (K − 1)λ bits). `clique_readTables`: so tables that were made an oracle (`answersOf`) and read
  back (`readTables`) give the same value.
* `parentAt_readyOf`: the parent that the solver hands to a callee, written with the numbers of the
  level.
* `child_value`: the value that the specification gives to a callee is the value of the clique of
  the groups (`Value.groupClique`) of the network of its pattern, at the callee's label length.
* `Net.abs_value_le`: |Z| ≤ 2^{gP + g²B} for a network on [g] with parameters P, B. 

### `clique_value_congr`

 The value of a clique reads its tables only on settings. 

### `readTables_setting`

 Tables made an oracle and read back are the tables, on settings. 

### `clique_readTables`

 So they give the same value. 

### `unary_length_eq`

 A string of units is its length in unary. 

### `length_unary`

 The length of a number in unary. 

### `parentAt_readyOf`

 The parent that the solver hands to a callee at the level ℓ + 1: K = K_ℓ, g = g_ℓ, the solver's
λ and B, the lists of the pieces for λ, the direction, y and x. 

### `groupTables_value`

 The tables W̃, made an oracle and read back, give the value of the clique of the groups. 

### `child_value`

 **The value of a callee** with the parent (K, g, λ, B, the lists, tr, y, x) and the label length
L: the value of the (K, L)-clique of the groups of the grouping x of the network of the pattern y. 

### `Net.abs_value_le`

 A network on [g] with parameters P, B has |Z| ≤ 2^{gP + g²B}. 
