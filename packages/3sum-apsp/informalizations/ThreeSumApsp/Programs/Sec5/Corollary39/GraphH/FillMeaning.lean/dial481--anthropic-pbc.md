---
{
  "module": "ThreeSumApsp/Programs/Sec5/Corollary39/GraphH/FillMeaning.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec5/Corollary39/GraphH/FillMeaning.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec5/Corollary39/GraphH/FillMeaning.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Corollary 39 in the light language: from the memory to the graph H

Proof of Corollary 39: "every edge of a k-clique is counted exactly once over the three edges of its
triangle". The program adds up cells of the memory over a list of pairs of numbers of parts, for a
choice of vertices that two odometers run through.  This file says what these sums are.  The list of
the program has the pairs of parts of the weight of an edge of H, the smaller part first (`pairsN`,
`pairsN_valid`).  If the weights of G stand in the memory (`WeightsAt`), the sum over this list is
the sum of the weights of G (`memSum_eq_pairSum`), and it is at most the number of pairs times the
bound on the weights (`memSum_abs_le`).  The choices that the odometers run through while one of the
three matrices is filled are the cliques given by four numbers (`choiceAt_AB`, `choiceAt_BC`,
`choiceAt_AC`, `withDigits_fixed`).


 ## The list of pairs in the text of the program 

### `pairsN`

 The pairs of parts as pairs of numbers, for the text of the program, each with the smaller part
first: the program reads the weight between two parts p < q in the block (p, q) only. 

### `length_pairsN`

 The list of pairs, written with natural numbers, is as long as the list of pairs. 

### `pairsH_ne`

 The two parts of a pair are different. 

### `pairsN_valid`

 The pairs are pairs of two parts, the smaller one first. 

 ## The sums 

### `WeightsAt`

 The weights of the graph G stand at g, in the blocks (p, q) with p < q.  Nothing is said about
the other blocks. 

### `memSum_eq_pairSum`

 What sumPairs computes is the sum of the weights of G. 

### `memSum_congr_vf`

 memSum only looks at the parts below kk. 

### `memSum_abs_le`

 A sum of |L| weights is at most |L| U in absolute value. 

 ## The choices that the odometers run through 

### `ChoiceIs.congr`

 Only the choices in the k parts matter. 

### `choiceAt_AB`

 The choices of vertices while the matrix between the groups 0 and 1 is filled. 

### `choiceAt_BC`

 The choices of vertices while the matrix between the groups 1 and 2 is filled. 

### `choiceAt_AC`

 The choices of vertices while the matrix between the groups 0 and 2 is filled. 

### `withDigits_fixed`

 If all cells hold 0 and the digits of F in base n are written to the cells of the fixed
vertices, the choice of vertices is vtx k n F 0 0 0. 
