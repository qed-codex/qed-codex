---
{
  "module": "proof/rates/ClauseBound/Alg/CertLevel.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Alg/CertLevel.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Alg/CertLevel.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Certificates: one level and all levels

Polynomial time (`PolyT`) in the pad and the data, for any pieces with certificates, of

* `expandG`, one level on a p × d grid (`stCertExpandG`), from the certificates of the network of a
  term, of the label length one level down, of the evaluation by enumeration and
  of the rebalancing;
* `solveG`, all levels, brute force at the bottom and the final division (`stCertSolveG`), from the
  certificates of one level, of the label length and of brute force;
* `needC`, the exponent of a pad that suffices, computed under a bound (`stCertNeedC`), from the
  certificate of the label length.

All numbers of a step are given in unary, and so is the label length. The state of the loop of
`needC` holds the current number of nodes in binary, while the length of the word of
an instance has that number in an exponent. The numbers of nodes that occur are those of the steps
and the first one, so their sum M is given in unary; the certificate is proved
for the loop in which the number of nodes in the state is cut off at M (`needCut`), and the cut-off
changes nothing (`needCut_eq`). 

 ### Division of an integer by a natural number 

### `ediv_natCast`

 The quotient, rounded down, in terms of quotients of natural numbers. 

### `divZ_polyT`

 Division of an integer by a natural number is polynomial-time. 

 ### The numbers of a step 

### `K_unary`

 The numbers of a step are given in unary. 

### `c2_unary`

 The number of pairs is given in unary. 

### `nRectG_unary`

 The number of rectangles of a step is given in unary. 

 ### The numbers of the pieces 

### `cnt_unary`

 The number of pieces is given in unary. 

### `d_polyT`

 The factor d of the pieces. 

### `cap_unary`

 The number of bits through which a piece factors is given in unary. 

### `dpow_polyT`

 The factor d^R of a step. 

### `nPat_polyT`

 The number of patterns. 

### `dig_polyT`

 A digit of a pattern. 

### `sumDig_polyT`

 The sum of the digits of a pattern. 

### `priceG_polyT`

 What the rectangles cost. 

### `totalG_polyT`

 The total U of the network of a pattern. 

### `colSide_polyT`

 The choice of the side. 

 ### One level 

### `gctx_polyT`

 The context of the network of a pattern. 

### `atOnce_polyT`

 Is the term of a pattern evaluated at once? 

### `lamNextG_unary`

 The label length one level down is given in unary. 

### `childG_polyT`

 The child of one pattern. 

### `expandG_polyT`

 One level. 

### `stCertExpandG`

 One level is polynomial-time in the pad, the step and the instance. 

 ### All levels 

### `stepG_polyT`

 One round of the descent. 

### `descendG_polyT`

 The descent through all levels. 

### `stCertSolveG`

 All levels, brute force at the bottom and the division are polynomial-time in the pad, K₀ in
unary, the schedule and the instance. 

 ### The square root of a number given in unary 

### `countP_le_range`

 Among 0, …, N − 1 there are min N (k + 1) numbers that are at most k. 

### `sqrt_eq_countP`

 The square root, rounded down, by counting. 

### `sqrt_polyT`

 The square root of a number given in unary is polynomial-time. 

 ### The numbers in the exponent 

### `ebarG_polyT`

 The bound for the column networks that are evaluated by enumeration. 

### `instLen_polyT`

 The length of the word of an instance, for K and the label length in unary. 

### `PnG_polyT`

 P of the networks that are rebalanced. 

### `quo_polyT`

 2p/K. 

### `bits_polyT`

 The bound for the number of bits of the values of the pieces. 

### `need_polyT`

 The exponent that the loops inside the pieces need. 

### `bNextG_polyT`

 The bound for the bit length of the entries one level down. 

### `Nof_polyT`

 N = (pd)²λ. 

 ### The exponent, computed under a bound 

### `zNext_polyT`

 The bound for the number of bits of the sum and the factor. 

### `needState_polyT`

 The exponent for the state of the descent. 

### `needLoops_polyT`

 The exponents for the loops of one step. 

### `needStep_polyT`

 One step of the computation of the exponent, if the number of nodes in the state is given in
unary. 

### `needFin_polyT`

 The end of that computation, if the number of nodes in the state is given in unary. 

### `measOption`

 The length of the word of an optional value can be computed in polynomial time. 

### `clip`

 The state with the number of nodes cut off at M. 

### `clip_eq`

 A state whose number of nodes is at most M is not changed. 

### `fold_clip`

 If no number of nodes exceeds M, the cut-off changes nothing in a loop that writes the number of
nodes of the step into the state, and the number of nodes in the result is
at most M. 

### `needCut`

 The computation of the exponent under a bound, with the numbers of nodes cut off at M. 

### `needCut_eq`

 With M the sum of all numbers of nodes, the cut-off changes nothing. 

### `clip_polyT`

 The state, cut off, is polynomial-time. 

### `clip_unary`

 The number of nodes in a state that is cut off at a number in unary is given in unary. 

### `needCut_polyT`

 The computation with the cut-off is polynomial-time. 

### `stCertNeedC`

 The exponent under a bound is polynomial-time in the bound, the three numbers in unary and the
schedule. 
