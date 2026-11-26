---
{
  "module": "proof/rates/CountedRecursion/RowFactorRun.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/RowFactorRun.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/RowFactorRun.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The procedure for f_{a,a'}

`rowFactor_within`: on a setting z of the row a and a string θ of c_{a,a'} bits, the procedure
`rowFactor` returns f_{a,a'}(z, θ) of the network of the pattern within g²·(2^{cλ} + 3) operations:
the first gλ bits of θ are compared with the strings of z on the straight edges, and each rectangle
gives one query to the pieces, for the function of the first pair of strings if a < a' and of the
second if a > a', at the chunk of θ that belongs to the rectangle
(proof of Proposition 3: by the observations after Definition 1 and the first factorization in Lemma
2 (b), Ψ_{a,a'} factors through c_{a,a'} bits). It asks the pieces only about strings of λ bits. The
bound on the states is explicit. 

### `top_lists`

 The function of the first pair of strings, in the form of `piecesOf`, at strings given as lists. 

### `bot_lists`

 The function of the second pair of strings. 

### `pieces_factor`

 The pieces answer the question for a function of a factorization. 

### `factorDigit`

 The place in 𝓘 of the piece of the rectangle with the columns j / g < j % g. 

### `factorChunk`

 The chunk of θ that belongs to that rectangle. 

### `factorItem`

 The factor number j of the loop. 

### `length_factorChunk`

 The chunk of a rectangle has as many bits as its piece asks. 

### `abs_factorItem_lt`

 It is below 2^{(2λ)^c} in absolute value. 

### `gridFf_items`

 `ClauseBound.Alg.gridFf` for the pieces, as the check and the loop of `rowFactor`. 

### `rowFactor_within`

 **The procedure for f_{a,a'}.** 
