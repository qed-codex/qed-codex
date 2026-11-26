---
{
  "module": "proof/rates/ClauseBound/Alg/GridNet.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Alg/GridNet.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Alg/GridNet.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The network of one term on a grid with p rows and d columns, on words

The file follows proof/machines/StepMachines/Math/SideCodes.lean and SideNet.lean, which treat the
square grid and pieces made from single bits (Appendix H). Here the grid has p rows and d columns
and
the pieces are any `PiecesF`. A «part» is a row (tr = false) or a column (tr = true); there are
`nParts p d tr` parts with `nMemb p d tr` nodes each. The word of a state of a
part: for each of its nodes, the p·d half-edges that start there, in the order of the positions of
their other ends, ℓ bits each. A label of two parts: one block of ℓ bits for each
edge between nodes of the same number, then one chunk for each of their rectangles; the chunk of a
rectangle is any word of as many bits as its piece is charged.

`gridN` is the network; its value, its sizes and its total are computed here. 

 ### The grid 

### `gridE`

 The p·d nodes of the instance on the grid: (part, number in the part). 

### `gridE_symm_val`

 The position of a node of the grid among the p·d nodes of the instance. 

### `nodeG_lt`

 Positions are below p·d. 

### `nParts_mul_nMemb`

 There are p·d nodes. 

### `length_heG`

 A half-edge in the word of a state has ℓ bits. 

 ### The codes of the states 

### `nodeC`

 The code, on words of p·d·n bits, of the half-edges that start at one node. 

### `stC`

 The code of a state of a part. 

### `stC_dec`

 The state named by a word, read half-edge by half-edge. 

### `gridR`

 The instance on words, carried to the grid; to the transposed grid if tr. 

 ### The cuts and the network 

### `cutG`

 The piece number i, cut between the parts: the labels are all words of `cap` bits. 

### `cutsG`

 The cuts of the rectangles of the grid (of the transposed grid if tr) for the pattern y. 

### `gridNet`

 The network of the term, with states and labels as in `rowNet`, before they are written as
words. 

### `rectsC`

 The code of the labels of the rectangles of the parts a, b: their chunks one after the other,
every word being a label. 

### `gridNet_c_eq`

 The capacity (number of label bits) of the parts a < b. 

### `gridNet_Θ`

 The label set of the parts a < b: the edges between nodes of the same number, and a label for
each rectangle. 

### `gridNet_Θ_empty`

 Label sets are kept at a < b only. 

### `gridCl`

 The code of the labels of two parts. 

### `gridN`

 The network on words. 

### `gridN_c`

 The capacity of two parts is the length of their labels. 

### `gridN_lab`

 The labels of two parts are all words of that length. 

 ### Numbering the rectangles; patterns as numbers 

### `ixG`

 The number of a rectangle of the grid with p rows and d columns. 

### `ixG_bijOn`

 The rectangles are numbered 0, …, R − 1, each number once. 

### `card_Ω_eq`

 The number of rectangles. 

### `patG`

 The pattern written by the number y: a rectangle gets the digit of y in base n + 1 at its
number. 

### `sum_patG`

 Summing over the numbers y < (n+1)^R is summing over the patterns. 

### `sum_Ω_ixG`

 A sum over the rectangles is the sum over their numbers. 

### `sum_Ω_rectIxG`

 The same for the rectangles sorted by parts. 

 ### The terms 

### `gridR0`

 The instance on the grid with p rows and d columns. 

### `termZ`

 The term of the pattern written by y in base n + 1, for the pieces A. 

### `cross_eq`

 The function [x = v][y = u], `Pieces.cross`, agrees with `Cross.X`. 

### `ZW_mul_eq_sum`

 The identity D^|R|·Z = Σ_ι Z_ι of the proof of Theorem A(b), with D the multiplier of the pieces
and |R| the number of rectangles, on words. 

### `trA`

 A function of the four ends, read on the transposed grid if tr: transposing exchanges the ends y
and u. 

### `ZG_gridR`

 The sum over the grid, or over the transposed grid, is the term. 

### `abs_gridR_le`

 The bound 2^B on the instance at the queries that are asked passes to the grid. 

 ### Value, sizes and total of the network 

### `CutsOK`

 What is used of the pieces: the pieces A i, i < cnt, are factorized by the cuts, and everything
is bounded. 

### `digG_lt`

 A digit of a pattern is the number of a piece. 

### `value_gridN`

 Either network on words has the value of the term. 

### `abs_trA_le`

 The values of a piece read on the transposed grid. 

### `gridN_sized`

 The network on words has the size m·(parts·members²·ℓ), and values of at most members·B +
members²·bits bits. 

### `U_gridN`

 The total of the network. 

### `gridN_c_le`

 Two parts share at most members²·mℓ bits. 
