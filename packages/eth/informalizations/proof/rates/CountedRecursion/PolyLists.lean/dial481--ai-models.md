---
{
  "module": "proof/rates/CountedRecursion/PolyLists.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/PolyLists.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/PolyLists.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The numbers of the grid, jointly in the lists

The certificates of proof/rates/ClauseBound/Alg/CertGridG.lean for `digG`, `lenG`, `capG`, `priceG`,
`totalG` are for ONE family of pieces with certificates of its own (`P.Keeps`). In the recursion the
numbers |𝓘|, c^row_i, c^col_i are read from lists in the context (`listsAsPieces`), so the pieces
vary with the input. Here are the same certificates jointly in the lists. They hold on EVERY input
because `listsAsPieces` cuts each number at 2λ and λ is given in unary.

Besides: a chunk of a label for a chunk number that is NOT given in unary (`chunkL_polyT`). The loop
over the rectangles passes its counter j, in binary, to the computation of the chunk, and a
certificate must cover every j. The digits of the pattern y beyond its length are 0, so the lengths
of the chunks are constant from the place (number of binary digits of y) on, and the sum of the
first κ lengths is a sum of at most that many terms and a product. 

 ### The numbers 

### `capL_unary`

 c^row_i or c^col_i, cut at 2λ, is given in unary. 

### `digL_polyT`

 The digit of a pattern at a rectangle. 

### `lenL_unary`

 The length of the chunk of a rectangle is given in unary. 

### `capGL_unary`

 The length of the labels of two parts is given in unary. 

### `priceL_unary`

 What the rectangles cost is given in unary. 

### `totalL_unary`

 The total of the network of a pattern is given in unary. 

 ### A chunk whose number is given in binary 

### `digit_eq_zero`

 The digits of y beyond its length are 0. 

### `lenG_tail`

 From the place (number of binary digits of y) on, all chunks have the same length. 

### `sum_range_tail`

 The sum of the first κ of numbers that are constant from the place m on. 

### `dropTake_polyT`

 Drop and take, for a number of terms given in unary. 

### `chunkAt_polyT_tail`

 A chunk of a word, for lengths that are constant from a place given in unary on; the number of
the chunk may be given in binary. 

### `chunkL_polyT`

 The chunk of a rectangle in a label, jointly in the lists, for every number of a rectangle. 
