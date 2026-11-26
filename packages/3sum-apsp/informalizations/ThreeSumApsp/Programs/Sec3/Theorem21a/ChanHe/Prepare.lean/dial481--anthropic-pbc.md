---
{
  "module": "ThreeSumApsp/Programs/Sec3/Theorem21a/ChanHe/Prepare.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem21a/ChanHe/Prepare.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem21a/ChanHe/Prepare.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# 3SUM from Convolution-3SUM: filling the arrays of the host

Theorem 21(a), after [CH20, Theorem 5.1].  prep(n, V, Λ, m, x, b) fills
those arrays of the memory map `Map` with base b that do not depend on a splitting; the cells for
the three sets and for the doubles are left as they are.  It has five parts.

* prepAddr computes the addresses of the arrays (`prepAddr_runs`).
* prepTables writes the primes up to m and zeros into the count table (`prepTables_ends`).
* prepSorted writes a sorted copy of the input (`prepSorted_ends`).
* prepValues writes the distinct values, how often each occurs, and the binary digits of the labels
  of the values (`prepValues_ends`).
* prepTail writes the block of parameters of the recursive procedure and the cell that holds 0, and
  returns the number of distinct values (`prepTail_ends`).

The sieve and sorting use cells behind the arrays as scratch space.  The arrays are filled in the
order of their addresses, and a part changes no cell below the first array that it fills, except
that prepTail writes the block of parameters at the base.  So what an earlier part has written is
still there at the end (`PrepValues.frontMem`), and the arrays lie as the loop over the splittings
wants them (`FrontMem.of_map`).  `prepBody_ends` puts the five parts together, and `prep_spec` is
the specification.


 ## The program 

### `Len`

 The locals of prep.  The arguments: n, V, Λ, m, x and the base b.  Then the address of the
primes, the number m², the addresses of the count table, the sorted copy, the values, their
multiplicities, the table of digits, the three sets, the doubles and the cell that holds 0, and the
free pointer behind the arrays.  Then the number of primes, a local for results that are not read,
and the number of distinct values. 

### `prepAddr`

 The addresses of the arrays. 

### `prepTables`

 The primes, and zeros in the count table. 

### `prepSorted`

 The sorted copy of the input. 

### `prepValues`

 The distinct values with their multiplicities, and the binary digits of their labels. 

### `prepTail`

 The block of parameters, the cell that holds 0, and the result. 

### `prepBody`

 prep(n, V, Λ, m, x, b), over the procedures pPrimes, pFill, pCopy, pSort, pDistinct, pBits. 

### `prepFrame`

 The arguments of prep and the addresses that prepAddr computes, as the list of the locals. 

 ## The five parts 

### `prepAddr_runs`

 prepAddr computes the addresses. 

### `ok_primes`

 What prep may use covers what the sieve needs. 

### `ok_sort`

 What prep may use covers what sorting needs. 

### `prepTables_ends`

 prepTables writes the primes and the zeros, and changes no other cell below the free pointer
behind the arrays. 

### `prepSorted_ends`

 prepSorted writes a sorted copy of the input, and changes no cell below it. 

### `two_mul_lt_two_pow_Lam`

 The labels for V have `Lam V` binary digits. 

### `two_pow_Lam_le`

 `2 ^ Lam V` is at most twice as large as it has to be. 

### `tBits_mono`

 The time of bits grows with the number of elements. 

### `Distinct.Ctx.of_consecutive`

 What distinct assumes holds when the three regions stand one after the other. 

### `PrepValues`

 What prepValues leaves in the memory: the distinct values D of the input X, how often each
occurs, and the binary digits of their labels. 

### `PrepValues.values`

 D lists the distinct values, and C how often each occurs. 

### `PrepValues.bounded`

 The values have absolute value at most V. 

### `PrepValues.segVal`

 The values stand at val. 

### `PrepValues.segMul`

 Their multiplicities stand at mul. 

### `PrepValues.segTable`

 The binary digits of their labels stand at bt. 

### `prepValues_ends`

 prepValues writes the distinct values, their multiplicities and the binary digits, and changes
no cell below them. 

### `prepTail_ends`

 prepTail writes the block of parameters and the cell that holds 0, and returns the number of
distinct values. 

 ## The whole routine 

### `FrontMem.of_map`

 The arrays of the map lie as the loop over the splittings wants them. 

### `PrepValues.frontMem`

 What the earlier parts have written is still there after prepTail. 

### `prepBody_ends`

 The five parts one after the other. 

### `prep_spec`

 **prep** meets its specification. 
