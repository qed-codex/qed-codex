---
{
  "module": "ThreeSumApsp/Util/CountingSort.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Util/CountingSort.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Util/CountingSort.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The pure side of counting sort

`N` items `0, …, N - 1` have keys `kf 0, …, kf (N - 1)`.  A stable sort by key puts item `j` at the
place `sortPos kf N j`: the number of items with a smaller key plus the number of earlier items with
the same key.

This is a bijection of `{0, …, N - 1}` (`eq_of_sortPos_eq`, `exists_sortPos_eq`) that is increasing
for the order "smaller key, or same key and earlier" (`sortPos_lt_sortPos_iff`).


### `cntEq`

 The number of items `i < j` with key `t`. 

### `cntLt`

 The number of items `i < j` with a key smaller than `t`. 

### `sortPos`

 The place of item `j` after a stable sort of the items `0, …, N - 1` by key. 

### `cntEq_succ`

 One more item: it is counted if its key is `t`. 

### `cntLt_succ_right`

 One more item: it is counted if its key is below `t`. 

### `cntLt_succ_left`

 Keys below `t + 1` are keys below `t` or equal to `t`. 

### `cntLt_mono_left`

 A larger bound counts more keys. 

### `cntLt_le`

 At most all items are counted. 

### `cntLt_congr`

 The number of keys below `s` among the first `m` items depends on these items only. 

### `cntLt_of_forall_lt`

 If all keys are below `K`, all items are counted. 

### `cntEq_lt_of_lt`

 Item `j` is itself one of the `N` items with its key. 

### `sortPos_lt_cntLt_succ`

 The place of an item lies before the places of the larger keys. 

### `sortPos_lt`

 The places are below `N`. 

### `sortPos_lt_sortPos`

 A smaller key comes first; among equal keys the earlier item comes first. 

### `sortPos_lt_sortPos_iff`

 The order of the places is the order "smaller key, or same key and earlier". 

### `eq_of_sortPos_eq`

 Different items get different places. 

### `exists_sortPos_eq`

 Every place is taken. 
