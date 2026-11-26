---
{
  "module": "proof/rates/ClauseBound/Boson/HalfList.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Boson/HalfList.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Boson/HalfList.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The pieces made from partitions, with the partitions given as lists

A program writes a partition of h as a list of its parts in some order of its own. Here a string x
is encoded by a list ℓ(x) of positive integers with sum h, and different strings have
lists that differ as multisets. The pieces `ApcL` are defined from these lists in the same way as
the pieces A_s in the proof of Theorem B are defined from partitions.
`ApcL_col_eq` writes a piece as a sum, over i ≤ 2h and the monomials τ of weight 2h − s − i, of
products of a function of (x,u) and a function of (y,v), as in the column-wise
expansion in the proof of Theorem B. 

### `ApcL`

 The piece number s, for an encoding ℓ of the strings by lists of positive integers with sum h. 

### `ApcL_col_eq`

 The piece as a sum over i ≤ 2h and the monomials τ of weight 2h − s − i: one factor depends on
(x,u), the other on (y,v). 
