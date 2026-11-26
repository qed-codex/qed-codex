---
{
  "module": "proof/rates/ClauseBound/Inst/HalfEnc.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Inst/HalfEnc.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Inst/HalfEnc.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The encoding of the strings by partitions

A string x of λ bits stands for the partition number x in the list of the partitions of h, which is
entry h of the table of the partitions of 0, …, W. If p(h) ≥ 2^λ and h ≤ W, that entry
exists: it is a list of positive parts with sum h that occurs in the flattened table (`encF_mem`,
`encF_ok`, `encF_mem_flatten`), and different strings stand for different partitions, also as
multisets (`encF_inj`). The flattened table has the three properties that the tables of matrices
need (`flatOK_allTab`). The last theorem, `stEnc`, collects the facts on the encoding for W = 4h. 

### `ofWord_bitsOf_lt`

 The number written by a string of λ bits is below 2^λ. 

### `ofWord_bitsOf_inj`

 Different strings write different numbers. 

### `ofWord_bitsOf_lt_length`

 The number written by a string is a position in the list of the partitions of h. 

### `encF_eq_getElem`

 The partition of a string is the entry at that position. 

### `encF_mem`

 The partition of a string is in the list of the partitions of h. 

### `encF_ok`

 The partition of a string has positive parts and the sum h. 

### `encF_mem_flatten`

 The partition of a string is in the flattened table. 

### `encF_inj`

 Different strings stand for different partitions, also as multisets. 

### `flatOK_allTab`

 The list of all partitions of 0, …, W, written as nonincreasing lists: different lists are
different multisets, erasing a part leads to a listed partition, and all sums are at most W. 

### `stEnc`

 The encoding with the table of the partitions of 0, …, 4h, in the form in which the
specification of the pieces uses it. 
