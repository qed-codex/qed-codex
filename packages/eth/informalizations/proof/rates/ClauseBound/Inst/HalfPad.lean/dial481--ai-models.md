---
{
  "module": "proof/rates/ClauseBound/Inst/HalfPad.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Inst/HalfPad.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Inst/HalfPad.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The list of all partitions of 0, …, 4h, and the pad for the tables

The functions that read the tables of the operators take, besides their input, a pad. The flattened
table of the partitions of 0, …, W has Σ_{E ≤ W} p(E) members, which for W = 4h is the number
`deltaF h`. For a partition μ of h, the two lengths of the pad that suffice for the tables, `padOp`
(the table of the operators (t^μ)[·]) and `padKF` (the tables of the parts of a^μ), are at most
`padLen h`. So the two functions that read the tables give the entries of the matrices as soon as
the
pad has length at least `padLen h` (`stTopF`, `stBotF`), by the correctness of the tables for a
general list of monomials. 

### `length_flatten_allTab`

 The flattened table has Σ_{E ≤ W} p(E) members. 

### `deltaF_eq`

 deltaF h = Σ_{E ≤ 4h} p(E). 

### `length_flatten_allTab_four`

 The flattened table of the partitions of 0, …, 4h has deltaF h members. 

### `padOp_le_padKF`

 The pad for the table of a[·] is shorter than the pad for the tables of the parts of a^μ. 

### `padKF_le`

 The pad for the tables of the parts of a^μ, for W = 4h, the sum h and at most h parts. 

### `parts_of_mem`

 A partition μ of h in the list: at most h parts, each at most 4h. 

### `padKF_le_padLen`

 The pad of length padLen h suffices for the tables of the parts of a^μ, μ a partition of h. 

### `padOp_le_padLen`

 The pad of length padLen h suffices for the table of the operators (t^μ)[·], μ a partition of h. 

### `stTopF`

 With a pad of length padLen h, `topF` on the list of all partitions of 0, …, 4h gives the
entries of the matrix. 

### `stBotF`

 With a pad of length padLen h, `botF` on the list of all partitions of 0, …, 4h gives the
entries of the matrix. 
