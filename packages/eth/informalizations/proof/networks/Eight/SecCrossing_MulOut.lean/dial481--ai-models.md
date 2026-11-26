---
{
  "module": "proof/networks/Eight/SecCrossing_MulOut.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/SecCrossing_MulOut.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/SecCrossing_MulOut.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Lemma 2(a): «multiplying them out one at a time»: what the program computes, and how large its lists are

The proof of Lemma 2(a) in Section 4 says: «The t factors are polynomials in T of degree at most 1
with coefficients in {−1, 0, 1}, so multiplying them out one at a time takes time poly(λ), and |A_i|
≤ C(t, i) ≤ 2^t.»
The program is in proof/networks/Eight/SecCrossing_PolyDefs.lean. A polynomial in T is kept as the
list of its coefficients, lowest first. mulStep r c l is the list of (r + T·c)·(polynomial of l);
mulUpTo q n is the list after the first n
factors, starting from the list [1]; mulOut q is the list after all t factors; aMul (i, q) is its
entry number i.

What is proved here:
* getD_mulUpTo: the entry number i after n factors is the coefficient of T^i in the product of the
  first n factors; mulOut_eq_A, stAMul: on four strings of λ bits the entry number i of mulOut is
  A_i.
* length_mulUpTo, abs_getD_mulUpTo_le_choose, abs_getD_mulUpTo_le: after n factors the list has n +
  1 entries, the entry number j is at most C(n, j) ≤ 2^n in absolute value. So every list that
  occurs is short (len_mulUpTo_le), and the values of the program are at most 2^t in absolute value
  (abs_aMul_le).
Small auxiliary statements are in the namespace Eight.MulOut. 

 ### Lists and strings 

### `MulOut.getD_ofFn`

 A position of the list of a string holds the bit of the string, and 0 beyond the end («Append 3t
− λ zeros to each of x, y, u, v»). 

### `MulOut.blkL_ofFn`

 The block number s of the list of a string is the block number s of the string. 

 ### One multiplication 

### `length_mulStep`

 One multiplication makes the list longer by one entry. 

### `getD_mulStep`

 The entry number j after one multiplication is r·l_j + c·l_{j−1}, also beyond the end of the
list, where all three entries count as 0. 

### `mulUpTo_succ`

 The factor number n is multiplied in after the factors number 0, …, n − 1. 

 ### The lists hold the coefficients of the products 

### `getD_mulUpTo`

 After n factors the entry number i is the coefficient of T^i in the product of the first n
factors. 

### `mulOut_eq_A`

 On four strings of λ bits, written as lists, the entry number i of mulOut is A_i, for every λ
and every i (for i > t both are 0). Same as in the paper: A_i is the coefficient of T^i in the
product of the t factors. 

### `stAMul`

 The program aMul computes A_i, for every λ and every i. 

 ### The lists stay short 

### `length_mulUpTo`

 After n factors the list has n + 1 entries. 

### `MulOut.abs_rAt_le`

 «coefficients in {−1, 0, 1}»: |R| ≤ 1 at every block. 

### `MulOut.abs_cAt_le`

 «coefficients in {−1, 0, 1}»: |C| ≤ 1 at every block. 

### `abs_getD_mulUpTo_le_choose`

 After n factors the entry number j is at most C(n, j) in absolute value, by Pascal's rule. At n =
t this is the paper's «|A_i| ≤ C(t, i)». 

### `abs_getD_mulUpTo_le`

 After n factors every entry is at most 2^n in absolute value. 

### `abs_aMul_le`

 The paper's «|A_i| ≤ 2^t», read off the program, for all inputs. 

### `MulOut.len_listZ_le`

 The word of a list of k integers whose words have length at most b has length at most k·(b + 2) + 2. 

### `MulOut.len_int_le`

 The word of an integer of absolute value at most 2^n has length at most 3n + 8. 

### `len_mulUpTo_le`

 The word of the list after n factors has length at most (n + 1)(3n + 10) + 2: the list has n + 1
entries, and each is an integer of at most n + 1 binary digits whose word has at most 3n + 8 bits. 

### `MulOut.tL_le_len`

 The number of blocks is at most the length of the word of the four strings. 
