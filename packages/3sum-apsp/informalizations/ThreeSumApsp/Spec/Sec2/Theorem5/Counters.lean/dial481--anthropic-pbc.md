---
{
  "module": "ThreeSumApsp/Spec/Sec2/Theorem5/Counters.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Spec/Sec2/Theorem5/Counters.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Spec/Sec2/Theorem5/Counters.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Quotients and remainders by counters

The word RAM has no division.  A program that runs through the rows `I = 0, 1, …, N - 1` of a matrix
can still know, for each row, its band, its block within the band and its offset within the block
(Section 2.3.4), that is `I / (K₀ N₀)`, `I / N₀ % K₀` and `I % N₀`: it keeps three counters and
steps them (`stepCtr`, `ctrAt_succ`).


### `Ctr`

 The band of a row, its block within the band, and its offset within the block. 

### `Ctr.band`

 The band of the row. 

### `Ctr.block`

 The block of the row within its band. 

### `Ctr.off`

 The offset of the row within its block. 

### `ctrAt`

 The band, block and offset of row `I`, for bands of `k₀` blocks of `n₀` rows. 

### `stepCtr`

 From the band, block and offset of a row to those of the next row: comparisons and additions of
1 only. 

### `ctrAt_succ`

 Stepping the counters of row `I` gives the counters of row `I + 1`. 
