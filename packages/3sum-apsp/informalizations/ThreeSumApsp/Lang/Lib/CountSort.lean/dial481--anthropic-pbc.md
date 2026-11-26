---
{
  "module": "ThreeSumApsp/Lang/Lib/CountSort.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Lang/Lib/CountSort.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Lang/Lib/CountSort.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Counting sort of a list of items by a key that is read through the item

countSort(n, src, dst, key, stride, off, nb, cnt) sorts the n items at src stably by their keys and
writes them to dst.  The key of the item x is the number in the cell key + x · stride + off, a
natural number below nb.  cnt is a scratch area of nb + 1 cells, of arbitrary content on entry; on
exit cnt[t] is the number of items with a key below t, which is where bucket t starts.

The routine has five phases, each of them one loop:
* `csZero` sets the cells of cnt to 0 (`csZero_ends`);
* `csCount` counts the items with key t in cnt[t + 1] (`csCount_ends`);
* `csPrefix` adds up, so that cnt[t] is the start of bucket t (`csPrefix_ends`);
* `csPlace` writes each item to the next free place of its bucket, which it reads from cnt and moves
  on by one (`csPlace_ends`);
* `csShift` moves the contents of cnt up by one cell, so that cnt[t] is again the start of bucket t
  (`csShift_ends`).

Each phase has an invariant, a structure about the memory, with two lemmas: `start` says that it
holds before the first round, and `succ` says what a round does to the memory.  Three numbers
describe the memory, where kf j is the key of item number j: `cntLt kf t n` is the number of items
with a key below t, the start of bucket t; `cntEq kf t i` is the number of items before item number
i with key t; and `sortPos kf n j`, their sum at t = kf j and i = j, is the place of item number j.
What is assumed is `CountSort.Pre`, what is achieved is `CountSort.Post`, and the result is
`countSort_meets`.


 ## The program 

### `Len`

 The local variables of countSort: the arguments n (Len), src, dst, key (Keys), stride, off
(Offset), nb (Buckets), cnt; the counter of the loops (Idx); the address of a cell of cnt (Cell); a
place in dst (Place). 

### `csKey`

 The key of item number i, where i is the value of the counter:
mem[key + src[i] · stride + off]. 

### `csZero`

 cnt[t] := 0 for t ≤ nb. 

### `csCount`

 cnt[(key of item i) + 1] += 1 for i < n. 

### `csPrefix`

 cnt[t + 1] += cnt[t] for t < nb. 

### `csPlace`

 dst[cnt[key of item i]] := item i, cnt[key of item i] += 1, for i < n. 

### `csShift`

 cnt[t] := cnt[t - 1] for t = nb, …, 1, and cnt[0] := 0. 

### `countSortBody`

 countSort(n, src, dst, key, stride, off, nb, cnt). 

 ## What is assumed, and the state between the phases 

### `Args`

 The arguments of countSort. 

### `Args.n`

 the number of items 

### `Args.src`

 where the items stand 

### `Args.dst`

 where the sorted items go 

### `Args.key`

 the key of the item x is in the cell key + x · stride + off 

### `Args.stride`

 see key 

### `Args.off`

 see key 

### `Args.nb`

 all keys are below nb 

### `Args.cnt`

 nb + 1 cells of scratch space 

### `Args.keyCell`

 The cell that holds the key of the item x. 

### `Args.state`

 A state of countSort: the arguments, the counter i, the scratch variables c and p, and the
memory. 

### `Args.Same`

 Only dst and cnt have changed. 

### `CountSort.Pre`

 What countSort assumes: where the arrays lie, that what is read is not overwritten, and what the
items (it) and their keys (kf) are. 

### `CountSort.Post`

 What countSort achieves: item number j stands at dst[sortPos kf n j], cnt[t] is the number of
items with a key below t, and nothing else has changed. 

### `CountSort.Pre.item`

 The items are still there after writing to dst and cnt. 

### `csKey_gives`

 Reading the key of item number i: the expression stays within the limits and gives kf i. 

### `CsState`

 The state between two phases, and before a round of a phase: the counter is i, only dst and cnt
have changed since the start, and R holds of the memory. 

### `CsState.imp`

 A weaker fact about the memory. 

### `Ends.csFor`

 **The loop rule for the phases.**  The loop has m rounds, the value of hi.  The body is a block
that keeps the arguments and the counter.  R j holds of the memory before round j; afterwards the
counter is m and R m holds. 

 ## The first phase: the counters are set to 0 

### `CsZeroed`

 The first j cells of cnt are 0. 

### `CsZeroed.succ`

 One more cell is set to 0. 

### `csZero_ends`

 `csZero`: the nb + 1 cells of cnt are 0 afterwards. 

 ## The second phase: the sizes of the buckets 

### `CsCounted`

 The items before item number i have been counted: the cell t + 1 of cnt holds the number of
those with key t, and the cell 0 holds 0. 

### `CsCounted.start`

 Nothing has been counted yet, and all cells are 0. 

### `CsCounted.succ`

 Item number i is counted. 

### `csCount_ends`

 `csCount`: cnt[t + 1] is the number of items with key t afterwards. 

 ## The third phase: the starts of the buckets 

### `CsSummed`

 The first r sizes have been added up: the cells t ≤ r of cnt hold the starts of their buckets,
and a cell t + 1 after them still holds the size of bucket t. 

### `CsSummed.start`

 What `csCount` leaves: the cell 0 holds 0, the start of bucket 0, and the others the sizes. 

### `CsSummed.succ`

 The cell r + 1 receives the start of bucket r + 1. 

### `csPrefix_ends`

 `csPrefix`: cnt[t] is the number of items with a key below t afterwards. 

 ## The fourth phase: the items go to their places 

### `CsPlaced`

 The items before item number i have been placed: they stand at their places in dst, and the
cell t of cnt holds the next free place of bucket t. 

### `CsPlaced.start`

 What `csPrefix` leaves: no item has been placed, and the next free places are the starts. 

### `CsPlaced.succ`

 **Item number i is placed**: it is written to its place, and the next free place of its bucket
moves on. 

### `csPlace_ends`

 `csPlace`: item number j is written to dst[sortPos kf n j], and cnt[t] moves on to the start of
bucket t + 1. 

 ## The fifth phase: the contents of cnt move up by one cell 

### `CsShifted`

 While the contents of cnt move up, with the counter at s: the items stand at their places, the
cells after s of cnt hold the starts of their buckets, and the cells before s still the starts of
the next buckets.  Nothing is said about the cell s: the next write goes there. 

### `CsShifted.start`

 What `csPlace` leaves, with the counter at nb: every bucket is full, so that its next free place
is the start of the next bucket. 

### `CsShifted.placed_update`

 A write to a cell of cnt leaves the items at their places. 

### `CsShifted.succ`

 The cell s + 1 receives what the cell s holds. 

### `CsShifted.last`

 The cell 0 of cnt is set to 0, the start of bucket 0. 

### `csShift_ends`

 `csShift`: from cnt[t] = start of bucket t + 1 to cnt[t] = start of bucket t. 

 ## The routine 

### `countSortTime`

 The time of countSort, for n items and keys below nb. 

### `countSort_meets`

 **countSort** sorts the items stably by their keys: the five phases, one after the other. 
