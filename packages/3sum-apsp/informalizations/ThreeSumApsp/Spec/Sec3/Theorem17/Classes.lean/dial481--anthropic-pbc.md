---
{
  "module": "ThreeSumApsp/Spec/Sec3/Theorem17/Classes.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Spec/Sec3/Theorem17/Classes.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Spec/Sec3/Theorem17/Classes.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The number of chunks, on lists and on sets of pairs (proof of Theorem 17)

The routines work with lists of places: `classIdx` lists the places `a n + b` of the pairs of a
class, and the table `chunkTab` has one entry for each chunk.  The paper's class `W_ϱ` is a set of
pairs (`residueClass`).  The map `(a, b) ↦ a n + b` is a bijection between the set and the list, so
both have the same number of elements (`length_classIdx_eq_card`), and the table has as many entries
as there are chunks "in all" (`length_chunkTab_eq_totalChunks`).  The instance is
`triOf n AB BC AC`, whose weights `w(a,b)` are read from the list `AB`, row by row.


### `length_classIdx_eq_card`

 The list of the places of a class has one entry for each pair of the class `W_ϱ`. 

### `length_chunkTab_eq_totalChunks`

 The table has one entry for each chunk. 
