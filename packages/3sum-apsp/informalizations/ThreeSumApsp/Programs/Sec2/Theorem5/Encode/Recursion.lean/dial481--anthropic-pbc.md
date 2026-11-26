---
{
  "module": "ThreeSumApsp/Programs/Sec2/Theorem5/Encode/Recursion.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec2/Theorem5/Encode/Recursion.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec2/Theorem5/Encode/Recursion.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The encoding of an array by the recursion of Section 2.4.1

"To compute it, we run Full with b left out and without step (4)" (Section 2.4.1).  If L = 0 the
leaf stores its number.  Otherwise, for each term λ, step (2) writes A_λ to a scratch area and the
recursive call of step (3) encodes it into the part of the output that belongs to the leaves below
λ.  The language has no division, so the lengths 7^{L-1} and 10^{L-1} of the parts are read from two
tables of powers.

`encIdx` is what `encode` computes, in terms of positions in arrays.  `encode` writes it to the
output within `encTime L = O(10^L)` steps (`encTime_le`), using `scrSize L` scratch cells.  The
proof is by induction on `L`:

* the hypotheses of `encode` at level `L + 1` give those of `encStep` (`EncodePre.toStep`) and,
  after it, those of the recursive call (`EncodePre.toRec`);
* the two calls for the term `λ` fill the part of the output below `λ` (`TermsDone.step`,
  `encodeTerm_spec`);
* `encode_leaf` is the case `L = 0`, `encode_node` the loop over the ten terms, and `encode_spec`
  the induction.


### `Level`

 The local variables of encode: the arguments L, src, out, scr, tab, p7, p10; the lengths 7^{L-1}
and 10^{L-1}; the number of the term; the result of a call, which is not used. 

### `encodeTerm`

 The two calls for one term: step (2) into the scratch area, and step (3) from there into the
part of the output that belongs to the term. 

### `encodeBody`

 encode(L, src, out, scr, tab, p7, p10).  pS and pE are the numbers that the procedures encStep
and encode have in the program. 

 ## What encode computes, how much room and how much time it needs 

### `encSlice`

 The array A_lam of step (2), in terms of positions in arrays: a is the input array (7^{L+1}
numbers, seven slices of 7^L) and c the table of the coefficients (c (7 lam + s) is the coefficient
of slice number s in the term number lam). 

### `encIdx`

 What encode computes, in terms of positions in arrays: a is the input array (7^L numbers), c the
table of the coefficients, and i < 10^L the position of a leaf. 

### `encIdx_succ`

 The part of the encoding below the term number lam is the encoding of A_lam. 

### `scrSize`

 The number of scratch cells that encode uses: 7^{L-1} + ⋯ + 7 + 1. 

### `encTime`

 A bound on the number of steps of `encode`: at level `L + 1`, ten times the two calls for a
term, and 104 steps. 

### `tTerm`

 The time of the two calls for one term. 

### `cEncode`

 The constant of the running time of `encode`. 

### `encTime_le`

 The number of steps is `O(10^L)`.  The two further terms on the left make the induction go
through. 

 ## The hypotheses 

### `EncodeLayout`

 Where the arrays of `encode` lie: the three tables, then the output, the input and the scratch
area, one behind the other. 

### `EncodePre`

 The hypotheses of `encode`: the layout, what the cells hold, and how large the numbers are. 

### `EncodePost`

 What `encode` guarantees: the encoding is in `out`, and only the `10^L` cells of `out` and the
`scrSize L` cells of the scratch area have changed. 

### `EncodeLayout.places_succ`

 The layout at level `L + 1`, with the sizes in terms of `10^L`, `7^L` and `scrSize L`. 

### `sameOutside2_succ`

 What has not changed at level `L + 1`, with the sizes in terms of `10^L`, `7^L` and
`scrSize L`. 

### `EncodeLayout.toRec`

 The layout of the recursive call for the term number `lam`: it reads the first `7^L` cells of
the scratch area, writes the part of the output below the term, and has the rest of the scratch
area. 

### `V_nonneg`

 The bound `V` is not negative. 

### `toStep`

 In the course of `encode` at level `L + 1`, the hypotheses of `encStep` hold for every term. 

### `toRec`

 After `encStep` has written `A_lam` to the scratch area, the hypotheses of `encode` hold at
level `L` for the recursive call. 

 ## One term 

### `TermsDone`

 The memory before the round of the term number `lam`: the parts of the output below the earlier
terms are filled, and only the output and the scratch area have changed. 

### `TermsDone.step`

 The two calls for the term number `lam` fill the part of the output below it. 

### `Encode.locals`

 The list of the local variables at level L + 1. 

### `EncodeMeets`

 The specification of encode at level L, for a caller at depth d. 

### `encodeTerm_spec`

 **One term**: step (2) and step (3) fill the part of the output below the term number `lam`. 

 ## The recursion 

### `encode_leaf`

 **A leaf**: the number is copied. 

### `encode_node`

 **An inner vertex**: the two lengths are read from the tables, and the loop runs through the ten
terms. 

### `encode_spec`

 **encode** is correct and takes at most `encTime L` steps, in every program whose procedures
number pS and pE are encStep and encode.  It nests calls at most L deep. 
