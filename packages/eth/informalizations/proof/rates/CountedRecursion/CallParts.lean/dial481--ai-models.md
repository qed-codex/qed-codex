---
{
  "module": "proof/rates/CountedRecursion/CallParts.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/CallParts.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/CallParts.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The parts of the context of a call

Plain facts about the data that the solver hands to a callee, with no machine and no mathematics of
the networks:
* the row network and the column network of the g × g grid have g nodes (`nParts_self`, in
  proof/rates/CountedRecursion/SquareGrid.lean);
* `rK_readyOf`, `rG_readyOf`, `nPatterns_readyOf`: what the solver holds at the level ℓ + 1 when the
  loop over the patterns begins: K_ℓ, g_ℓ and the number |𝓘|^{|ℛ|} of patterns; `total_direction`:
  the network that it takes has the smaller total;
* `answersOf_readTables`, `answersOf_some`, `fits_succ`: the tables read back from the oracle of a
  well-formed instance are its tables, on settings;
* `groupTables_mkParent`: the tables W̃ of the callee, written with the numbers of the parent. 

### `level_numbers`

 K_ℓ ≥ 2, K_ℓ ≤ g_ℓ, g_ℓ ≥ 2. 

 ### What the solver holds 

### `rK_readyOf`

 The K that the solver holds at the level ℓ + 1 is K_ℓ. 

### `rG_readyOf`

 The g that the solver holds at the level ℓ + 1 is g_ℓ. 

### `nPatterns_readyOf`

 The number of patterns is |𝓘|^{|ℛ|}. 

### `total_direction`

 «the network with the smaller total»: its total is the smaller of the two. 

 ### Tables and oracles 

### `answersOf_congr`

 The oracle reads the tables only on settings. 

### `answersOf_readTables`

 The oracle of the tables read back from an oracle of tables is that oracle. 

### `answersOf_some`

 An answer of the oracle: the query names a node and a setting, and the answer is the entry. 

### `fits_succ`

 A well-formed instance of the level ℓ + 1: λ, B ≥ 1, the tables read from its oracle are below
2^B on the settings of the clique on g_ℓ·g_ℓ nodes, and the oracle is the oracle of these tables. 

### `groupTables_mkParent`

 The tables W̃ of the callee, written with the numbers of the parent. 
