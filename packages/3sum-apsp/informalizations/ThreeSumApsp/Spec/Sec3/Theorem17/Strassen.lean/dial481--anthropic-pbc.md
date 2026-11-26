---
{
  "module": "ThreeSumApsp/Spec/Sec3/Theorem17/Strassen.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Spec/Sec3/Theorem17/Strassen.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Spec/Sec3/Theorem17/Strassen.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Strassen's algorithm on lists, and the count of the proof of Theorem 17

Proof of Theorem 17: "Computing PQ takes […] O(n^{log₂ 7}) with Strassen's algorithm".
`strassenList` multiplies two `2^K × 2^K` matrices over `ℤ[x]/(x^p - 1)`, given as lists in Z-order,
and `countOf` reads the number of triples `(a,b,c)` with `S(a,b,c) = w(a,b) + w(b,c) + w(a,c) ≡ 0
(mod p)` off the product.

1. `zRing hp K α` is the list of the matrix `α` over the ring.  The operations on lists are the
   operations of the ring, entry by entry (`zRing_add`, `zRing_sub`), and the quadrants of a matrix
   are the quarters of its list (`quarter_zRing`, `zRing_succ`).
2. `strassenList_zRing`: the algorithm computes the product.  By induction on `K`; Strassen's seven
   products give the four quadrants of the product by an identity that holds summand by summand.
   It makes `7^K` multiplications in the ring, which is `O(n^{log₂ 7})` (`seven_pow_clog_le`).
3. The lists that the routine fills are the matrices `P` and `Q` of the proof of Theorem 17, padded
   with zeros to `2^K` rows and columns (`matPList_eq_zRing`, `matQList_eq_zRing`), and the padding
   does not change the entries of the product (`sum_padP_mul_padQ`).
4. `countOf_eq`: the count is the count of the proof of Theorem 17.


 ## Matrices over the ring, as lists 

### `zRing`

 A matrix over the ring as a list in Z-order. 

### `zRing_add`

 The list of a sum of matrices. 

### `zRing_sub`

 The list of a difference of matrices. 

### `quarter_zRing`

 The quadrants of a matrix are the quarters of its list. 

### `zRing_succ`

 A matrix is put together from its four quadrants. 

 ## Strassen's algorithm 

### `strassenList`

 Strassen's algorithm [Str69] for `2^j × 2^j` matrices over `ℤ[x]/(x^p - 1)` in Z-order. 

### `sum_range_two_pow_succ`

 A sum over twice as many indices. 

### `strassenList_zRing`

 **Strassen's algorithm computes the product**, for matrices over the ring. 

### `seven_pow_clog_le`

 `strassenList p K` calls `cconv` seven times per level, `7^K` times in all.  For `K = ⌈log₂ n⌉`
this is the `O(n^{log₂ 7})` of the proof of Theorem 17: `7^{⌈log₂ n⌉} ≤ 7 n^{log₂ 7}`. 

 ## The count of the proof of Theorem 17 

### `zeros`

 The zero vector. 

### `matPList`

 Proof of Theorem 17: `P[a,c] := x^{w(a,c) mod p}`, padded with zeros to `2^K` rows and columns;
`RAC` holds the residues. 

### `matQList`

 Proof of Theorem 17: `Q[c,b] := x^{w(b,c) mod p}`. 

### `countBy`

 Proof of Theorem 17: "the sum over the pairs (a,b) ∈ A × B of the coefficient of x^{-w(a,b) mod
p} in (PQ)[a,b]"; `RM` is `PQ` in Z-order. 

### `countOf`

 The number `F(p) + Z₀` of triples with `p ∣ S(a,b,c)`, computed as in the proof of Theorem 17.


### `padP`

 The matrix `P` of the proof of Theorem 17, padded with zeros. 

### `padQ`

 The matrix `Q` of the proof of Theorem 17, padded with zeros. 

### `sum_padP_mul_padQ`

 The padding does not change the entries of the product. 

### `matPList_eq_zRing`

 The first list that the routine fills is the matrix `P`, padded. 

### `matQList_eq_zRing`

 The second list that the routine fills is the matrix `Q`, padded. 

### `countOf_eq`

 **The count of the proof of Theorem 17**: `countOf`, computed with Strassen's algorithm from the
three lists of weights, is the number of triples `(a,b,c)` with `S(a,b,c) ≡ 0 (mod p)`. 
