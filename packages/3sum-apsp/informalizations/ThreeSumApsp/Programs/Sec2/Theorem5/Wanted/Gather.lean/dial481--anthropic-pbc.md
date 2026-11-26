---
{
  "module": "ThreeSumApsp/Programs/Sec2/Theorem5/Wanted/Gather.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec2/Theorem5/Wanted/Gather.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec2/Theorem5/Wanted/Gather.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Theorem 5 in the light language: gathering the codes in sorted order

Section 2.4.4: "sort the sets W_T", the wanted positions of each tile T.  Sorting produces a
permutation of the wanted positions.  The procedure gather(w, perm, src, dst) then copies their
codes into sorted order: dst[i] := src[perm[i]] for i < w.

gather_entry shows that a call ends within 20 (w + 1) steps, with dst[i] = src[π[i]] for the list π
at perm, and that no cell outside the w cells of dst has changed.  The proof is one loop with the
invariant GatherInv; each round reads two cells that are still as at the start and writes dst[i].


### `Len`

 The number w of cells. 

### `Perm`

 The permutation. 

### `Src`

 The array that is read. 

### `Dest`

 The array that is written. 

### `Pos`

 The counter i of the loop. 

### `gatherBody`

 gather(w, perm, src, dst): dst[i] := src[perm[i]] for i < w. 

### `GatherInv`

 The memory before round i: the first i cells of dst are filled, and no cell outside the w cells
of dst has changed. 

### `gather_entry`

 **gather**: a call ends within 20 (w + 1) steps with dst[i] = src[π[i]] for i < w, and no cell
outside the w cells of dst has changed. 
