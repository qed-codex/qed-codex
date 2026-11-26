---
{
  "module": "proof/rates/CountedRecursion/GridLemmas.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/GridLemmas.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/GridLemmas.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The lists and the pieces

* `digG_congr`, `lenG_congr`, `capG_congr`, `priceG_congr`, `totalG_congr`: the plain functions of
  proof/rates/ClauseBound/Alg/Data.lean that give the numbers of the two networks of a pattern read
  only `cnt` and `cap` of the pieces, and `cap` only at numbers below `cnt`.
* `listsAgree : ListsAgree`: the numbers read from the lists that the solver has after its queries
  are those of the pieces; so the functions above agree on `listsAsPieces (listsOf D λ)` and
  `piecesOf D c`.
* Lemmas on the pieces of Definition 7 in the form `piecesOf D c`: sums over 𝓘 (`sum_indexAt`), the
  functions of the two pairs of strings (`top_piecesOf`, `bot_piecesOf`), and 𝓘 is not empty
  (`card_I_pos`). 

 ## The functions read only cnt and cap 

### `digG_congr`

 ι at a rectangle reads only the number of pieces. 

### `lenG_congr`

 The length of the chunk of a rectangle reads only `cnt` and `cap`. 

### `capG_congr`

 So does c_{a,a'}. 

### `priceG_congr`

 So does what the rectangles cost in a network. 

### `totalG_congr`

 So does the total U. 

 ## The lists 

### `getD_map_of_lt`

 The element number j of a list under a map. 

### `length_sortI`

 The list of 𝓘 has |𝓘| entries. 

### `indexAt_mem`

 The element number j < |𝓘| of 𝓘 is in 𝓘. 

### `listsAgree`

 **The numbers read from the lists are those of the pieces.** 

 ## Lemmas on the pieces in the form `piecesOf D c` 

### `sum_range_getD`

 A sum over the places of a list. 

### `sum_indexAt`

 A sum over 𝓘 is the sum over its places. 

### `toBits_bitsOf`

 A string written as a list and read again. 

### `fn_bitsOf`

 The functions of a factorization, called with strings written as lists. 

### `top_piecesOf`

 The function of the first pair of strings, in the form that this development uses. 

### `bot_piecesOf`

 The function of the second pair of strings, in the form that this development uses. 

### `card_I_pos`

 𝓘 is not empty. 
