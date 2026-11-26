---
{
  "module": "proof/rates/ClauseBound/Alg/CertGridG.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Alg/CertGridG.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Alg/CertGridG.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Certificates for the grid

Polynomial time (PolyT) for the network `gridF P` of one term on a p × d grid and for the numbers
that one level computes from a step of the schedule. The sides p and d, the
parameter h of the pieces, the label length and the pad are data in unary; the flag «columns
merged», the pattern and the queries are data too. The pieces enter only through
their own certificates `P.Keeps`.

* `stCertGrid`: the lengths of the states and labels of `gridF P` are given in unary, its weights
  and factors are polynomial-time (the interface statement `StCertGrid P`).
* `stCertLam`: the label length one level down is given in unary (`StCertLam P`).
* For the certificates of a whole level: `capG_unary`, `priceG_unary`, `totalG_unary`,
  `capSum_unary`, `ubarG_unary`, `lamNextG_unary`, and `cnt_unary`, `cap_unary` for the
  pieces with h and the length of the strings as numbers in unary.
* Closure lemmas: the square root (`sqrt_polyT`, two binary digits at a time), the largest of
  finitely many numbers (`sup_range_polyT`), a chunk of a word whose chunks may be
  empty (`chunkAt_polyT`), and a product whose factors are only needed for small indices
  (`prodL_polyT_min`).

The chunks of a label may have the length 0 here, so the number of a chunk has to be given in unary.
In the product over the pairs of nodes of two parts the index j is therefore
replaced by min j m², which changes no factor of the product. 

 ### More closure lemmas for numbers given in unary 

### `unary_congr`

 «Given in unary» passes to a function with the same values. 

### `unary_ite`

 A case distinction between two numbers given in unary is given in unary. 

### `unary_mod`

 The remainder of a number given in unary is given in unary. 

### `unary_max`

 The larger of two numbers given in unary is given in unary. 

### `unary_min`

 The smaller of two numbers given in unary is given in unary. 

### `unary_min_right`

 The smaller of any number and a number given in unary is given in unary. 

### `c2_unary`

 g(g − 1)/2 is given in unary if g is. 

### `c2_polyT`

 g(g − 1)/2 is polynomial-time. 

### `tri_unary`

 The number of the pair a < b is given in unary if a and b are. 

### `prodL_min`

 A product over j < n only needs its factors for j ≤ n. 

### `prodL_polyT_min`

 A product over j < n is polynomial-time if its factors are for indices given in unary. 

### `chunkAt_polyT`

 A chunk of a word, for lengths that are polynomial-time and a chunk number given in unary. 

 ### Positions in the words of the p × d grid 

### `nRectG_unary`

 The number of rectangles is given in unary if p and d are. 

### `nRectG_polyT`

 The number of rectangles is polynomial-time. 

### `nParts_unary`

 The number of parts is given in unary if p and d are. 

### `nMemb_unary`

 The number of nodes of a part is given in unary if p and d are. 

### `nParts_polyT`

 The number of parts is polynomial-time. 

### `nMemb_polyT`

 The number of nodes of a part is polynomial-time. 

### `nodeG_polyT`

 The position of a node of a part is polynomial-time. 

### `rectIxG_polyT`

 The number of a rectangle is polynomial-time. 

### `heG_polyT`

 A half-edge in the word of a state is polynomial-time. 

### `chkG_polyT`

 The test of the edges inside a part is polynomial-time, for p and d in unary. 

### `gridW_polyT`

 The weight of a part is polynomial-time, for p and d in unary. 

 ### The square root, and the largest of finitely many numbers 

### `sqrt_eq_ite`

 The square root of m from that of m / 4. 

### `foldr_sqrt`

 The square root, two binary digits of the number at a time. 

### `sqrt_polyT`

 The square root is polynomial-time. 

### `sqrt_unary`

 The square root of a number given in unary is given in unary. 

### `sup_range_eq_foldl`

 The largest of f 0, …, f (n − 1) as a fold. 

### `sup_range_polyT`

 The largest of f 0, …, f (n − 1) is polynomial-time, for n in unary. 

### `sup_range_unary`

 The largest of f 0, …, f (n − 1) is given in unary if n and the numbers are. 

 ### The parts of a step 

### `K_unary`

 K is given in unary. 

### `p_unary`

 p is given in unary. 

### `d_unary`

 d is given in unary. 

### `D_unary`

 D is given in unary. 

### `h_unary`

 h is given in unary. 

### `a_unary`

 a is given in unary. 

### `b_unary`

 b is given in unary. 

### `thin_polyT`

 The flag «thin» is polynomial-time. 

### `Nof_unary`

 N = (pd)²λ is given in unary. 

 ### The arithmetic of one level, for any numbers 

### `ubarG_aux`

 The formula of the bound for U, for any numbers given in unary. 

### `lamNextG_aux`

 The formula of the label length one level down, for any numbers given in unary. 

 ### The pieces 

### `cnt_unary`

 The number of pieces is given in unary if h and the length of the strings are. 

### `cap_unary`

 The number of bits through which a piece factors is given in unary. 

### `digG_polyT`

 The digit of a pattern at a rectangle. 

### `lenG_unary`

 The length of the chunk of a rectangle is given in unary. 

### `capG_unary`

 The length of the labels of two parts is given in unary. 

### `priceG_unary`

 What the rectangles cost is given in unary. 

### `totalG_unary`

 U of the network of a pattern is given in unary. 

### `rectG`

 The factor of the rectangle of the nodes i < i' of the two parts in `gridFf`. 

### `rectG_polyT`

 The factor of a rectangle is polynomial-time, for the numbers of the two nodes in unary. 

### `itemG_polyT`

 One factor of the product in `gridFf` is polynomial-time, for a number j given in unary. 

### `gridFf_polyT`

 The factor of two parts is polynomial-time, for p, d, h and the label length in unary. 

### `gridF_keeps`

 The network of one term keeps polynomial time: lengths in unary, weights and factors
polynomial-time. 

 ### One level 

### `capSum_unary`

 The largest sum of the two numbers of bits of a piece is given in unary. 

### `ubarG_unary`

 The bound for U of the networks that are rebalanced is given in unary. 

### `lamNextG_unary`

 The label length one level down is given in unary. 

### `stCertGrid`

 The network of one term on a p × d grid keeps polynomial time, for pieces that do. 

### `stCertLam`

 The label length one level down is given in unary, for pieces that keep polynomial time. 
