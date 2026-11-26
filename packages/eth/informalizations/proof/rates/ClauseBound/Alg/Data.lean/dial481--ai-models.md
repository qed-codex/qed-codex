---
{
  "module": "proof/rates/ClauseBound/Alg/Data.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Alg/Data.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Alg/Data.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The definitions, part 1: pieces as programs, the steps of a schedule, the network of one term on a p × d grid

Everything is a pure function of data and a pad, as in the namespace `PaddedDescent.F`. 

### `PQ`

 The argument of one factor of a piece: ((pad, column-wise?), (parameter h, index i), (first
string, second string, label θ)); λ is the length of the first string. 

### `PiecesF`

 Pieces as programs. The pieces for the strings of λ bits and the parameter h are numbered 0, …,
cnt h λ − 1. `cap tr h λ i` is the number of bits through which the piece number i
factors row-wise (tr = false) or column-wise (tr = true); `top` is the function of the first two
strings of that factorization, `bot` that of the other two. 

### `PiecesF.need`

 the pad that the loops inside top and bot need, as an exponent of 2 

### `PiecesF.bits`

 all values of the pieces and of top and bot have at most this many bits 

### `PiecesF.m`

 every cap is at most 2·m·λ (the paper has m = 1; code words that are easier to compute may
  need m = 2) 

### `bitsOf`

 A word of n bits as a function. 

### `PiecesF.Spec`

 What the grid needs of the pieces at (h, λ): they add up to d·[x = v][y = u]; top and bot
factorize them over all words of cap bits, when the pad is long enough; sizes. 

### `PiecesF.Keeps`

 The certificates of the pieces. 

### `Step`

 One step of a schedule, «p·d nodes → K nodes», all numbers in unary: ((K, p, d), (D, h), (thin?,
a, b)).
D: the grouping of the parts into the K groups is allowed the relative error 1/D. h: the parameter
of the pieces.
thin = false: both networks are rebalanced, the one with the smaller total is taken. thin = true: a
comparison that involves the sum of the values of ι and the numbers a and b decides between
evaluating the column network by enumeration
and rebalancing the row network. 

### `nRectG`

 The number of rectangles of the p × d grid. 

### `nParts`

 The number of parts (merged rows, or merged columns if tr) and the number of nodes of a part. 

### `nodeG`

 The position, among the p·d nodes of the instance, of the node number i of the part a: the node
in row r and column j has the position j + d·r. 

### `rectIxG`

 The number of the rectangle number κ of the pair of parts number q. 

### `heG`

 The half-edge from the node number x of a part towards the node at position u, in the word z of
a state of the part. 

### `GridCtx`

 ((pad, (p, d) in unary, tr, h in unary), (ℓ in unary, pattern y, table)). 

### `digG`

 ι at the rectangle number κ of the pair of parts number q: a digit of y in base cnt. 

### `lenG`

 The length of the chunk of that rectangle in a label. 

### `capG`

 The length of the labels of the parts a, b. 

### `chkG`

 The half-edges from a node to itself are 0…0 and the edges inside the part agree. 

### `gridW`

 The weight of a part. 

### `gridFf`

 The factor of the parts a = q.1.1 and b = q.1.2 on the side of a. 

### `gridF`

 The network of the term Z_ι with all rows (tr = false) or all columns (tr = true) merged. 

### `priceG`

 What the rectangles cost in the network of the pattern y (every rectangle counts twice). 

### `totalG`

 U of that network. 
