---
{
  "module": "ThreeSumApsp/Util/StablePass.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Util/StablePass.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Util/StablePass.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# One stable pass of a radix sort, on lists

A stable counting sort moves the item at place `j` of a list `π` to place `sortPos kf n j`, where
`n` is the length of `π` and `kf j = keyAt kd π j` is the key of that item (`IsStablePass`).  The
new list is a rearrangement of `π` (`IsStablePass.perm`), and if `π` was sorted by `g`, the new list
is sorted by the pair (key, `g`) (`IsStablePass.sorted`).  This is the step of a radix sort that
starts with the least significant digit.


### `keyAt`

 The keys of the items of a list, by place. 

### `keyAt_eq`

 The key at a place of the list. 

### `IsStablePass`

 `π'` is the result of a stable pass on `π` by the key `kd`: it is as long as `π`, and the item
at place `j` of `π` stands at place `sortPos … j` of `π'`. 

### `IsStablePass.perm`

 A stable pass rearranges the list: the places `sortPos … j` are a permutation of the places. 

### `IsStablePass.sorted`

 After a stable pass by `kd` on a list sorted by `g`, the list is sorted by `kd · B + g`, if
`g < B`. 

### `cntLt_keyAt`

 The number of places with a key below `s` is the number of items with a key below `s`. 
