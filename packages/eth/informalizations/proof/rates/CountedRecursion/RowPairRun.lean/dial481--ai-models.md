---
{
  "module": "proof/rates/CountedRecursion/RowPairRun.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/RowPairRun.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/RowPairRun.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The procedure for Ψ_{a,a'}
`rowPair_within`: on settings z, z' of two rows a ≠ a', the procedure `rowPair` returns Ψ_{a,a'}(z,
z') of the network of the pattern within g²·(2^{cλ} + 3) operations; each A_i is one query to the
pieces, about strings of λ bits only.
«Ψ_{a,a'} is the product of the factors of the g straight edges between rows a and a' and of
A_{ι(q)}(x_q, y_q, u_q, v_q) over the g(g−1)/2 rectangles q with these two rows» (proof of
Proposition 3). The bound on the states is explicit. 

### `length_rectStrings`

 The four strings of a rectangle have λ bits. 

### `pieces_value`

 The pieces answer the question for A_i at four strings of λ bits. 

### `size_ordered`

 A query for Ψ put in order has the same size. 

### `pairLoop`

 The check and the loop of `rowPair`, after the query has been put in order. 

### `rowPair_eq`

 `rowPair` puts the query in order and runs the loop. 

### `pairItem`

 The factor number j of the loop. 

### `abs_pairItem_lt`

 It is below 2^{(2λ)^c} in absolute value. 

### `pairLoop_within`

 The check and the loop, run. 

### `rowPair_within`

 **The procedure for Ψ_{a,a'}.** 
