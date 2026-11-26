---
{
  "module": "proof/threesat/Exits/Tested.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/Exits/Tested.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/Exits/Tested.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The points that are met, the leaves that are tested

Facts on the two list functions of proof/threesat/Exits/Defs.lean, with no machine in them.
`tested v ls` is the part of ls up to and including the first entry that passes v; `met f stop c xs`
is the part of xs that a loop sees which halts as soon as its accumulator passes `stop`.
For the two loops of Algorithm 1 that are left early, the loop over the formulas of line 2, in its
deciding form that stops at the first Φ with Count(Φ) > 0, and line 10 («try all groupings into K_ℓ
groups until one is good»), `met` is `tested`: `met_or` and `met_first`.
The rest says how `tested` behaves on a list put together from two, on a range of numbers, and under
a choice `sel` of the entries on which the test is run at all. 

 ### `tested` 

### `tested_nil`

 Nothing is tested in the empty list. 

### `tested_cons_of_pass`

 If the first entry passes, it alone is tested: «if … then return». 

### `tested_cons_of_fail`

 If the first entry fails, the search goes on behind it. 

### `tested_singleton`

 A single entry is tested, whatever the outcome. 

### `mem_of_mem_tested`

 What is tested lies in the list. 

### `tested_of_fail`

 If no entry passes, all are tested. 

### `tested_append_of_pass`

 If an entry of the first list passes, nothing of the second list is tested. 

### `tested_append_of_fail`

 If no entry of the first list passes, all of it is tested and the search goes on in the second
list. 

### `any_tested`

 Some tested entry passes if and only if some entry passes. 

### `reach_le`

 The search does not go beyond the range. 

### `tested_range`

 In the range 0, …, n − 1 the numbers below `reach` are tested: «try all … until one is good». 

 ### The test is run only on the entries that `sel` picks 

### `any_filterMap_sel`

 Some entry passes w if and only if some picked entry passes v. 

### `filterMap_tested`

 The picked entries among those tested by w are the picked entries tested by v. 

 ### `met` 

### `met_nil`

 No point is met on the empty orbit. 

### `met_cons_of_stop`

 If the accumulator passes `stop` after the first round, the loop is left. 

### `met_cons_of_go`

 If it does not, the loop goes on with the new accumulator. 

### `met_or`

 The loop of «if … then return»: the accumulator says whether some point has passed so far, and
the loop is left as soon as it says yes. The points met are those tested. 

### `foldl_or`

 The result of that loop. 

### `met_first`

 The loop of «try all … until one is good»: the accumulator holds the first good number, if one
has been seen, and the loop is left as soon as it holds one. The points met are those tested. 

### `foldl_first_tested`

 The result of that loop: the first good number of the whole list. 
