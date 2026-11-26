---
{
  "module": "ThreeSumApsp/Lang/Lib/Merge.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Lang/Lib/Merge.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Lang/Lib/Merge.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Merging two segments

merge(a, na, b, nb, dst) writes the merge of the na cells from a and the nb cells from b to the na +
nb cells from dst, within `mergeTime (na + nb)` steps (`merge_meets`).  The model is `List.merge`:
the next output is the head of the first list unless the head of the second list is smaller.
Nothing is assumed about the order of the two lists.  Numbers are only compared and copied, so their
size does not matter.


 ## The pure side: one step of List.merge on the rests of two lists 

 ## The program 

### `ListA`

 The local variables of merge: the arguments a, na, b, nb, dst, and the numbers i and j of cells
already taken from the first and the second list. 

### `mergeTakeLeft`

 The next output is the head of the first list: dst[i + j] := a[i]; i := i + 1. 

### `mergeTakeRight`

 The next output is the head of the second list: dst[i + j] := b[j]; j := j + 1. 

### `mergeBody`

 merge(a, na, b, nb, dst). 

### `Pre`

 What merge assumes: the two lists lie in the memory, and the output region is within the memory
and meets neither of them. 

### `Inv`

 The state after i cells of the first list and j cells of the second have been taken: they stand,
merged, in the first i + j cells of dst, and no cell outside dst has changed. 

### `Taken`

 The invariant of the loop: t cells have been taken. 

### `takeLeft`

 dst[i + j] := a[i]; i := i + 1. 

### `takeRight`

 dst[i + j] := b[j]; j := j + 1. 

### `_root_.Light.mergeTime`

 The time of merge, for n = na + nb numbers. 

### `_root_.Light.merge_meets`

 **merge(a, na, b, nb, dst)** writes `List.merge` of the two lists to dst and changes nothing
else. 
