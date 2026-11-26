---
{
  "module": "ThreeSumApsp/Programs/Sec3/Theorem17/Hashing/Count.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem17/Hashing/Count.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem17/Hashing/Count.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The count of the proof of Theorem 17, read off the product PQ

"then F(p) + Z₀ is the sum over the pairs (a,b) ∈ A × B of the coefficient of x^{-w(a,b) mod p} in
(PQ)[a,b]."  Here F(p) is the number of false positives of p, that is, of triples with S(a,b,c) =
w(a,b) + w(b,c) + w(a,c) ≠ 0 and p ∣ S(a,b,c), and Z₀ is the number of zero triangles.

This file proves that the routine countZero returns this sum, `countBy`.  It does not prove that the
sum is F(p) + Z₀: that is `countOf_eq`, a theorem about lists with no program in it.

countZero(rm, rab, mort, n, p): the cells from rm hold the product PQ, a matrix of 4^K vectors of p
coefficients each, in Z-order, where 2^K ≥ n; the cells from rab hold the residues of the weights
w(a,b) mod p, that of (a, b) at place a n + b; the cells from mort hold the table of `spread`, from
which the place of a pair in Z-order is formed.  The routine goes through the pairs (a, b) in the
order of their places a n + b, reads the residue ϱ of w(a,b), forms (p - ϱ) mod p by one test, and
adds the coefficient number (p - ϱ) mod p of the vector of (a, b) (`countTerm`,
`countZeroAdd_spec`); then it steps to the next pair.  The loop is `countZero_spec`.


### `Mat`

 The local variables of countZero.  The arguments: Mat = rm, Residues = rab, Places = mort,
Num = n, Prime = p.  Then Square = n²; Idx = t = a n + b, the number of the pair; Row = a; Col = b;
Total, the sum; Expo, the exponent (p - ϱ) mod p. 

### `countZeroAdd`

 The term of the pair (a, b) is added to the sum. 

### `countZeroBody`

 countZero(rm, rab, mort, n, p).  The sum is returned in local 0. 

### `countZeroTime`

 An upper bound on the number of steps of countZero. 

### `countTerm`

 The term of the pair number i: the coefficient of x^{-w(a,b) mod p} in (PQ)[a,b]. 

### `CountZeroPre`

 What countZero needs: where the arrays lie, and what they hold.  RM is the list of the 4^K p
coefficients at rm, of absolute value at most V, and RAB is the list of the n² residues at rab. 

### `index_lt`

 The place of the term of the pair number t lies in the list RM of the 4^K p coefficients. 

### `readTerm`

 The term of the pair number t. 

### `countZeroAdd_spec`

 **The term of the pair number t is added.** 

### `countZero_spec`

 **countZero** returns the count and leaves the memory as it was. 

### `countZero_meets`

 **countZero** as a procedure. 
