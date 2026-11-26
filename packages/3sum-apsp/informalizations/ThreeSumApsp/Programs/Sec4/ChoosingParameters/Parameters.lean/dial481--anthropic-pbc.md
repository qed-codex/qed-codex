---
{
  "module": "ThreeSumApsp/Programs/Sec4/ChoosingParameters/Parameters.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/ChoosingParameters/Parameters.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/ChoosingParameters/Parameters.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Corollaries 26 and 31 in the light language: rational parameters in the program text

Proof of Corollary 26: "Setting up. Let m := ⌈log₄ D⌉, and pad the inner dimension to 4^m < 4D";
proof of Corollary 31: "with L := ⌈cm⌉ and t := ⌈θm⌉". A program is a finite text, so it can hold c
and θ only if they are rational: c = a/b and θ = p/q (`RatParams`). For real c and θ the statements
follow by approximation (`exists_ratParams`). Corollary 26 is the case c = 21, θ = 1/9, with the
threshold 60 (`ratParams26`).

This file has the parameters, what a structure at the free pointer fr consists of (`structEnd`,
`Ready31`), what the routines ask of the limits (`Lim31`), the query with its specification and its
proof (`QuerySpec31`, `query31_meets`), and the text and the specification of the preprocessing
(`pre31Body`, `PreSpec31`).


 ## Parameters 

### `RatParams`

 The parameters in the program text: c = a/b > 10, θ = p/q in (0, 0.9), and the threshold m₀ ≥ 1
below which queries compute inner products. 

### `RatParams.L`

 L = ⌈(a/b) m⌉. 

### `RatParams.t`

 t = ⌈(p/q) m⌉. 

### `RatParams.ten_le_L`

 10 m ≤ L. 

### `RatParams.t_le`

 t ≤ m. 

### `RatParams.am_le`

 a m ≤ b L. 

### `RatParams.pm_le`

 p m ≤ q m. 

### `parOf`

 The parameters of Theorem 30. 

### `switchOf31`

 The switching order. 

### `RatParams.Hyp`

 The hypotheses of Theorem 30 at these parameters. 

### `RatParams.preCost`

 The cost (8) of the preprocessing of Theorem 30 at these parameters. 

### `RatParams.queryCost`

 The cost L ∑ α_d of a query of Theorem 30 at these parameters. 

### `RatParams.blockEnd`

 The first address after the block of Theorem 30. 

### `structEnd`

 The first address that is not used. 

### `structEnd_small`

 Below the threshold a structure has three cells. 

### `structEnd_large`

 For m ≥ m₀ a structure ends with the block of Theorem 30. 

### `add_three_le_blockAt`

 The block of Theorem 30 begins after the first three cells. 

### `RatParams.blockAt_lt_blockEnd`

 The block of Theorem 30 is not empty. 

### `RatParams.scratch_in_block`

 The cells that a query of Theorem 30 writes lie in the block. 

### `add_three_le_structEnd`

 A structure has at least three cells. 

### `logFour_le_levels`

 m ≤ L. 

### `Built31`

 The data structure of Theorem 30 for the padded matrices has been built in the cells after fr.


### `Ready31`

 **The cells from fr on hold what a query needs.** 

### `Lim31`

 The limits that the two routines need. 

### `Lim31.mword`

 For the computation of L and t. 

### `Lim31.wordL`

 The numbers formed on the way to L fit in a word. 

### `Lim31.wordT`

 The numbers formed on the way to t fit in a word. 

### `Input31`

 **What both routines are given**: matrices X and Y with entries bounded by U, the addresses aX
and aY of their cells, which lie below the free pointer fr, and limits that suffice. 

 ## The query: the text is query31Body 

### `tQuery31`

 The time of a query. 

### `QuerySpec31`

 query31 returns the entry (XY)[I, J], keeps the structure ready, and changes only cells of the
structure behind its first three. 

### `Ready31.of_query`

 A query to the data structure of Theorem 30 changes only cells of its block, so that the
structure stays ready. 

### `query31_meets`

 query31 reads the flag and calls the query of Theorem 30 if it is 1 and the inner product
otherwise; it returns the entry (XY)[I, J] and keeps the structure ready. 

 ## The preprocessing: text and interface 

### `tCeilMul`

 The time of ceilMul: it counts up to ⌈a m / b⌉. 

### `CeilMulSpec`

 Procedure number pn returns ⌈a m / b⌉ on the argument m, and changes no cell. 

### `Size`

 The locals of pre31. The first five are its arguments N, D, aX, aY, fr. Then come m, 4^m, L, t,
the addresses of the padded matrices, the base address b0 of the block of Theorem 30, a result that
is not used, and the product N 4^m. 

### `prePad31`

 The first part of pre31 for m ≥ m₀: L, t, the addresses, and the padded matrices. 

### `preBuild31`

 The second part: the preprocessing of Theorem 30, the base address and the flag 1. 

### `preLarge31`

 The part of pre31 for m ≥ m₀. 

### `pre31Body`

 pre31(N, D, aX, aY, fr): m and 4^m; for m < m₀ the flag 0, for m ≥ m₀ preLarge31. 

### `tPre31`

 The time of the preprocessing; c is the constant of the shared stage. 

### `PreSpec31`

 pre31 prepares the cells from fr on, about which nothing is assumed, for queries to XY. 
