---
{
  "module": "ThreeSumApsp/Spec/Sec3/Theorem21b/RepeatedSquaring.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Spec/Sec3/Theorem21b/RepeatedSquaring.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Spec/Sec3/Theorem21b/RepeatedSquaring.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Repeated squaring on lists of integers

For Theorem 21(b): if no closed walk has negative weight, then squaring the weight matrix `⌈log₂ n⌉`
times in the (min,+)-product yields the distance matrix, and all finite entries that occur have
absolute value at most `nU`, where `U` bounds the edge weights. The matrices of the repeated
squaring have entries that may be `+∞`, while a solver for the (min,+)-product works on integers.
Here `+∞` is written as the integer `3nU`.

* `squareList n U ADJ W t` is the list, row by row, after `t` rounds.  A round is a (min,+)-product
  of the list with itself, after which every entry above `nU` is set back to `3nU`.
* One round is right (`Encodes.square`): finite entries have absolute value at most `nU`, so a sum
  with an infinite term is at least `2nU`, and a finite sum is the sum of the two codes.
* By induction the list holds the matrix `minPlusSquares` of the repeated squaring, entry
  by entry (`encodes_squareList`), and after `⌈log₂ n⌉` rounds it holds the distances
  (`squareList_distances`).


 ## Entries that may be infinite, as integers 

### `Encodes`

 The list `L` holds, row by row, the matrix `D`, with `INF` for `+∞`: the code `d.untopD INF` of
an entry `d` is the number itself, or `INF` if `d = +∞`. 

### `clip`

 Every number above `thr` becomes `INF`. 

### `neg_le_untopD`

 A code is at least `-B` if `3B` stands for `+∞` and the numbers are bounded by `B`. 

### `two_mul_le_untopD_add_untopD`

 If a sum of two entries is `+∞`, then the two codes add up to at least `2B`. 

### `untopD_add_untopD_of_coe`

 If a sum of two entries is a number, then the two codes add up to this number. 

 ## The lists of the repeated squaring 

### `weightList`

 The weight matrix of the graph (0 on the diagonal), row by row, with `INF` where there is no
edge. 

### `squareList`

 The matrix after `t` squarings, row by row, with `3nU` for `+∞`. 

### `length_squareList`

 Each list of the repeated squaring has `n²` entries. 

### `encodes_weightList`

 The list of the weights holds the weight matrix of the graph. 

### `Encodes.square`

 **One round.**  If a list holds a matrix `D` whose finite entries are bounded by `B`, with `3B`
for `+∞`, and the finite entries of the (min,+)-product of `D` with itself are bounded by `B` too,
then the (min,+)-product of the list with itself, with every entry above `B` set to `3B`, holds that
product. 

### `edgeWeightsBoundedBy_graphOf`

 The edge weights of the graph read from lists are bounded if the list of the weights is. 

### `abs_minPlusSquares_le`

 For Theorem 21(b): the finite entries of the matrices of the repeated squaring have absolute
value at most `nU`. 

### `encodes_squareList`

 **Repeated squaring on lists.**  After `t` rounds the list holds the matrix after `t` squarings
(`minPlusSquares`). 

### `abs_squareList_le`

 The entries of the lists of the repeated squaring are bounded by `3nU`. 

### `squareList_distances`

 **The answer.**  After `⌈log₂ n⌉` rounds the list holds the distances: an entry is `3nU` if and
only if the distance is `+∞`, and it is the distance otherwise. 
