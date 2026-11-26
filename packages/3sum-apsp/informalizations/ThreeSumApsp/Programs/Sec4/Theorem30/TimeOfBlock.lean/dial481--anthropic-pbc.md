---
{
  "module": "ThreeSumApsp/Programs/Sec4/Theorem30/TimeOfBlock.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/Theorem30/TimeOfBlock.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/Theorem30/TimeOfBlock.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Theorem 30 in the light language: the two routines against the expressions (8) and L ∑ α_d

Pure arithmetic, continued. Every summand of the time of the shared stage and of the length of the
shared block is at most a constant times `10^L`, or `N (L + 1)`, or the work for the bands
(`sharedShape_le`, `sharedEnd_sub_le`), and these three are within (8). With the tiles of the
previous file this gives the three bounds that leave these two files: the preprocessing takes
`O((8))` steps (`exists_tPreCore_le`), the block has `O((8))` cells (`exists_top_sub_le`), and a
query takes `O(L ∑_{d ≤ t} α_d)` steps (`exists_tQueryAt_le`).  The offline form uses them
elsewhere: its expression (9) is (8) plus |W| times the cost of a query (`Theorem30.cost9_eq`, with
the mathematics of Theorem 30), and `exists_tWantedCore_le`, beside the offline statement, puts the
two bounds together.


 ## The shared stage, in natural numbers 

### `succ_sq_le_ten_pow`

 `(L + 1)² ≤ 10^L`. 

### `SizeFacts`

 The facts about the sizes that the two estimates below use; T is `10^L` and S7 is `7^L`. 

### `sharedShape_le`

 The time of the shared stage: a part of order `10^L`, a part of order `N L`, and a part for each
band. 

### `sharedEnd_sub_le`

 The length of the shared block. 

 ## Within (8) 

### `N_mul_le_cost8`

 `N (L + 1)` is within three times (8), because `√K N₀ ≤ 7^L` and `(L + 1) 7^L ≤ 3 · 10^L`. 

### `N_mul_pow_le_cost8`

 `N 4^m` is within (8): it is at most the last term, because `√K N₀ 4^m ≤ K N₀ 4^m ≤ 7^L ≤ 10^L`.


### `within8_shared`

 The three quantities that bound the shared stage, together. 

### `within8_sharedShape`

 **The shared stage** runs within (8). 

### `exists_tPreCore_le`

 **The preprocessing** takes `O((8))` steps.  c is the constant of the shared stage. 

### `top_sub_eq`

 The length of the block, split into the shared block, the scratch strings, and the tries with
their roots. 

### `exists_top_sub_le`

 **The block** has `O((8))` cells. 

### `exists_tQueryAt_le`

 **A query** takes `O(L ∑_{d ≤ t} α_d)` steps. 
