---
{
  "module": "ThreeSumApsp/Lang/Lib/Seg.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Lang/Lib/Seg.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Lang/Lib/Seg.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Segments of the memory

Seg μ a l says that the cells a, a + 1, …, a + l.length - 1 of the memory μ hold the list l.
SegN is Seg for a list of natural numbers, MatAt for a matrix written row by row, VecAt for a vector
of indices.  The file has the lemmas for reading a cell of a segment, writing into it, writing
elsewhere, and for cutting and joining segments.  Each of the four predicates has its lemma `keep`,
which carries it to a later memory.


### `Seg`

 The cells a, a + 1, … of the memory μ hold the list l. 

### `readSeg`

 The list held by the n cells from address a. 

### `Seg.get`

 Reading a cell of a segment. 

### `Seg.getD`

 Reading a cell of a segment, with a default value for the list. 

### `Seg.eq_readSeg`

 A segment determines its list. 

### `Seg.congr`

 A segment only depends on its own cells. 

### `Seg.keep`

 A segment stays where it is if its cells do not change.  By the default proof of `hs`, the term
`h.keep` carries `h` to a later memory across the steps whose promises are in the context. 

### `Seg.update_in`

 Writing into a segment. 

### `Seg.update_out`

 Writing outside a segment. 

### `Seg.snoc`

 Writing just after a segment makes it longer. 

### `Seg.of_sameOn`

 A segment all of whose cells are kept. 

### `SameOutside.mono`

 A larger region may change. 

### `SameOutside.update`

 Writing inside the region. 

### `SameOutside2.update`

 Writing into one of the two regions. 

### `Seg.of_sameOutside`

 A segment that does not meet the region is kept. 

### `SegN`

 The cells a, a + 1, … hold a list of natural numbers. 

### `SegN.read`

 Reading a cell of a segment of natural numbers. 

### `SegN.getElem`

 Reading a cell of a segment of natural numbers, with the proof that the index is in range. 

### `SegN.snoc`

 Writing just after a segment of natural numbers makes it longer. 

### `SegN.take_succ`

 One more entry of a list of natural numbers is written behind its first k entries. 

### `SegN.drop_take`

 A piece of a segment of natural numbers: w cells from the place lo on. 

### `SegN.keep`

 A segment of natural numbers stays where it is if its cells do not change. 

### `SegN.of_sameOutside`

 A segment of natural numbers that does not meet the region is kept. 

### `MatAt`

 The cells from a on hold the matrix A, row by row. 

### `MatAt.congr`

 A matrix stays where it is if its cells do not change. 

### `MatAt.keep`

 A matrix stays where it is if its cells do not change. 

### `MatAt.congr_below`

 A matrix that lies below e is still there in a memory that agrees below e. 

### `VecAt`

 The cells from a on hold the indices I 0, I 1, …. 

### `vecAt_of_seg`

 A vector of indices that has been written as a list. 

### `VecAt.keep`

 A vector of indices stays where it is if its cells do not change. 
