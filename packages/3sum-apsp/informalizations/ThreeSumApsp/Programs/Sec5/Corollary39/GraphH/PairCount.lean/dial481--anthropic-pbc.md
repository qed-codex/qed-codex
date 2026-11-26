---
{
  "module": "ThreeSumApsp/Programs/Sec5/Corollary39/GraphH/PairCount.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec5/Corollary39/GraphH/PairCount.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec5/Corollary39/GraphH/PairCount.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Corollary 39 in the light language: the number of pairs of parts

The three lists of pairs of parts together have (k choose 2) pairs: every pair of parts is counted
in exactly one of the three weight matrices of H.


### `add_choose_two`

 The pairs in a union of a and b elements: within the first set, across, and within the second
set. 

### `length_filter_lt`

 The number of indices above j. 

### `length_upper`

 The number of pairs j < j' below m. 

### `length_pairsH`

 The number of pairs of parts that contribute to the weight matrix number i of H. 

### `lenH_eq_choose`

 Every pair of parts is counted once. 
