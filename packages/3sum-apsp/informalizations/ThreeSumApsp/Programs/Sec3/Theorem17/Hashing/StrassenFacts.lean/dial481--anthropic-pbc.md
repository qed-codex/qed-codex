---
{
  "module": "ThreeSumApsp/Programs/Sec3/Theorem17/Hashing/StrassenFacts.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem17/Hashing/StrassenFacts.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem17/Hashing/StrassenFacts.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Strassen's algorithm in seven uniform phases: the pure side

An entry of a matrix is a vector of `p` numbers, an element of the ring ℤ[x]/(x^p - 1), whose
product is `cconv p`; `vlinList s A B` is the list `A + s B`, which the routine vlin writes.  The
routine for Strassen's algorithm clears the four quarters of the result and then runs seven
phases.  A phase forms `S = A₁ + s_A A₂`, `T = B₁ + s_B B₂`, `M = S · T` (recursively) and adds
`s₁ M` and `s₂ M` to two quarters of the result; the signs are 1, -1 or 0.  This file has the facts
about lists that the proof about the routine uses:

* lengths (`length_vlinList`, `length_quarter`, `length_strassenList`);
* magnitudes: for operands bounded by `α` and `β`, all numbers that are formed at level `j` are
  bounded by `strassenBound p j α β = 16^j p α β` (`absLe_strassenList`);
* the seven phases give `strassenList` (`strassenList_succ_eq_phases`).


### `length_vlinList`

 The list that vlin writes is as long as its operands. 

### `vlinList_zero`

 With the sign 0 the first operand is kept. 

### `vlinList_zero_self`

 With the sign 0 and twice the same operand, the operand is kept. 

### `vlinList_zeros_left`

 Adding a list to zeros gives the list. 

### `_root_.ThreeSumApsp.AbsLe.vlinList`

 The bounds of the two operands add up. 

### `_root_.ThreeSumApsp.AbsLe.trans_le`

 A larger bound. 

### `absLe_zeros`

 Zeros are bounded by 0. 

### `length_quarter`

 A quarter of a list of 4 q numbers has q numbers. 

### `_root_.ThreeSumApsp.AbsLe.quarter`

 A bound for a list is a bound for its quarters. 

### `_root_.Light.Seg.quarter`

 A quarter of a segment is a segment. 

### `_root_.Light.ArrayAt.quarter`

 A quarter of an array of 4 q numbers is an array of q numbers. 

### `_root_.Light.ArrayAt.vlinList`

 The list A + s B, once it stands at dst, is an array, and the bounds of A and B add up. 

### `length_cconv`

 A product in the ring has p numbers. 

### `length_strassenList`

 The product of two matrices of 4^j vectors has 4^j vectors. 

### `phaseM`

 The product of a phase. 

### `strassenBound`

 The bound on all the numbers that the routine forms at level `j`, for operands bounded by `α`
and `β`. 

### `strassenBound_nonneg`

 The bound is not negative. 

### `strassenBound_succ`

 The bound of level j + 1 in terms of the bound of level j, for operands that are sums of two. 

### `strassenBound_one_one`

 The bound on the entries of the product of two matrices of zeros and ones. 

### `le_strassenBound_left`

 The bound is at least the bound α for the first operand. 

### `le_strassenBound_right`

 The bound is at least the bound β for the second operand. 

### `absLe_cconv`

 A product in the ring is bounded by p α β. 

### `_root_.ThreeSumApsp.AbsLe.vadd`

 The entries of a sum. 

### `_root_.ThreeSumApsp.AbsLe.vsub`

 The entries of a difference. 

### `_root_.ThreeSumApsp.AbsLe.vadd_self`

 The entries of a sum of two lists with the same bound. 

### `_root_.ThreeSumApsp.AbsLe.vsub_self`

 The entries of a difference of two lists with the same bound. 

### `absLe_strassenList`

 The entries of the result of the routine, and of the products of its phases, are bounded. 

### `length_phaseM_quarter`

 The product of a phase on quarters of the operands has the length of a quarter. 

### `strassenList_succ_eq_phases`

 **The seven phases give Strassen's algorithm.** 
