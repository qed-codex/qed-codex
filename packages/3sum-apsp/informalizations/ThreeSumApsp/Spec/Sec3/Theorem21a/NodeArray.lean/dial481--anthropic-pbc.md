---
{
  "module": "ThreeSumApsp/Spec/Sec3/Theorem21a/NodeArray.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Spec/Sec3/Theorem21a/NodeArray.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Spec/Sec3/Theorem21a/NodeArray.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The array of a node of the reduction after Chan and He, from lists

For Theorem 21(a), after [CH20, Theorem 5.1].  The one-array instance of a node of the reduction
from 3SUM to Convolution-3SUM (`ChanHe.Node.oneArray`) is
defined through the buckets of three finite sets.  A program has each set as a list without
repetitions, computes the list of the remainders (`keys`), and counts how often each remainder
occurs.  In these terms:

* the size of a bucket is the number of times its remainder occurs (`card_bucket`);
* a cell of `arr` holds the number with that remainder if the remainder occurs once
  (`arr_of_count_eq_one`), and the padding value otherwise (`arr_of_count_ne_one`, `arr_of_le`);
* the cells `4i`, `4i + 1`, `4i + 2`, `4i + 3` of `oneArray` hold a constant and cell `i` of the
  three arrays, each shifted (`oneArray_cells`).


### `keys`

 The remainders of the numbers of a list, as natural numbers. 

### `length_keys`

 Each number has one remainder. 

### `keys_lt`

 The remainders are below `M`. 

### `map_cast_keys`

 The list of the remainders, as integers. 

### `card_bucket`

 The size of a bucket is the number of times its remainder occurs in the list of the
remainders. 

### `arr_of_count_eq_one`

 A cell whose remainder occurs once holds the number with that remainder. 

### `arr_of_count_ne_one`

 A cell whose remainder does not occur exactly once holds the padding value. 

### `arr_of_le`

 The cells from `M` on hold the padding value. 

### `oneArray_cells`

 The four kinds of cells of the one-array instance of a node.  Here `6V + 4` is the number
`G = 3W + 1` for `W = 2V + 1`. 
