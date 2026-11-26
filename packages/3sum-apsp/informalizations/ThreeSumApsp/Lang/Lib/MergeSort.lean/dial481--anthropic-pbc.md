---
{
  "module": "ThreeSumApsp/Lang/Lib/MergeSort.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Lang/Lib/MergeSort.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Lang/Lib/MergeSort.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Merge sort

sort(n, a, fr) sorts the n cells from a in place, in ascending order (`sort_meets`).  It is the
recursive merge sort: sort the first ⌈n/2⌉ cells, sort the rest, merge the two halves into the n
cells from the free pointer fr, and copy them back.  It calls half, merge and copy.

The proof is an induction on n.  `body_ends` treats the body of the procedure, given that the
procedure sorts the lists of half the length, and `join_ends` its last two calls; `sorted_merge`
says that what the four calls leave is a sorted permutation of the list.  The number of steps,
`sortTime n`, is of the order n log n (`clog_split`, `time_split`), and the calls are nested
⌈log₂ n⌉ + 1 deep.  Numbers are only compared and copied, so their size does not matter.


### `Len`

 The local variables of sort: the arguments n, a and fr; h = ⌈n/2⌉; and a local that takes the
results of the calls, which are not used. 

### `sortJoin`

 The two sorted halves are merged into the cells from fr and copied back. 

### `sortBody`

 sort(n, a, fr).  The parameters are the procedure numbers of sort itself, half, merge and
copy. 

### `sortTime`

 The time of sort. 

### `clog_split`

 The recursion for n ⌈log₂ n⌉. 

### `Procs`

 The program holds the four procedures. 

### `time_split`

 The recursion for the number of steps. 

### `Sorted`

 What sort leaves: a sorted permutation of the list L at a; of the cells below fr only those of
the list may have changed. 

### `sorted_refl`

 A list of at most one number is sorted. 

### `sorted_merge`

 The two halves are sorted one after the other, merged into the cells from fr, and copied
back. 

### `join_ends`

 Two lists, one after the other in the memory, are merged into the cells from fr and copied
back. 

### `body_ends`

 The body of sort, given that the procedure sorts the lists of at most half the length, rounded
up. 

### `_root_.Light.sort_meets`

 **sort(n, a, fr)** leaves a sorted permutation of the list at a.  Of the cells below fr only the
n cells from a may change; the n cells from fr are used. 
