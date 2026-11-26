---
{
  "module": "ThreeSumApsp/Sec5/Lemma36a.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec5/Lemma36a.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec5/Lemma36a.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Lemma 36(a)

Lemma 36(a) reduces the (min,+)-product, APSP and Exact Triangle with real inputs to `Õ(n/d)`
counting calls, each of `d` comparison counts, and `Õ(n³/d)` further time.  The randomized search
behind it is cited from [CVX22].  The sentence on APSP, "by successive squaring of the weight
matrix, performing ⌈log₂ n⌉ such products", is `theorem_21b_repeated_squaring`, which covers real
weights.  This file proves the other parts that the paper argues itself.
* Fredman's trick (`fredman_trick`, `fredman_trick_le`).
* From the problems to predecessors and successors among the `d` sums of a block.  Exact Triangle:
  `lemma_36a_exact_triangle`.  For the (min,+)-product, `C[i,j]` is chosen below all sums
  (`lemma_36a_min_plus_below`); then its successor is the smallest sum of the block
  (`lemma_36a_min_plus_successor`), and the product is the entrywise minimum over the blocks
  (`lemma_36a_min_plus_blocks`), which are `n/d` blocks of `n²` entries
  (`Lemma36a.mul_sq_eq_cube_div`).
* A counting call is `d` comparison counts.  Its lists have at most `d` numbers
  (`lemma_36a_valid`) and at most one number of each color (`lemma_36a_colors`), so a comparison
  count is a number of colors (Section 5.2, `comparisonCount_eq_card_colors`), and by Fredman's
  trick it is the count that the call asks for (`lemma_36a_count`).  The pair sets have `n²`
  elements in all (`lemma_36a_pairs`), and forming the lists costs `O(nd²)` subtractions
  (`lemma_36a_subtractions`).


 ### Fredman's trick 

### `fredman_trick`

 Section 5.2, Fredman's trick: "a' + b' < a + b if and only if a' - a < b - b'". 

### `fredman_trick_le`

 Fredman's trick with "≤ in place of <" (Lemma 36). 

### `ComparisonCounts.Cmp.fredman`

 Fredman's trick for either comparison. 

 ### Predecessors and successors in the blocks 

### `lemma_36a_exact_triangle`

 Proof of Lemma 36(a): "For Exact Triangle, A[i,k] := w(i,k), B[k,j] := w(k,j), and
C[i,j] := -w(i,j), and there is a triangle of weight zero if and only if, in some block, some C[i,j]
is its own predecessor." The instance has n = b * d vertices per part; A is cut into b blocks of d
consecutive columns and B into the corresponding blocks of d consecutive rows.  In the notation of
Section 3.2, i, k, j run over the parts A, B, C of the instance. 

### `lemma_36a_min_plus_below`

 Proof of Lemma 36(a): "For the (min,+)-product of A and B, we take every C[i,j] smaller
than all the sums, for instance C[i,j] := min_k A[i,k] + min_k B[k,j] - 1."  `rowMin i` is min_k
A[i,k] and `colMin j` is min_k B[k,j]. 

### `lemma_36a_min_plus_successor`

 Proof of Lemma 36(a): "Then the successor of C[i,j] in a block is the smallest sum of
the block". `sums` are the d sums of the block and `c` is a number smaller than all of them. 

### `lemma_36a_min_plus_blocks`

 Proof of Lemma 36(a): "and the product is the entrywise minimum over the n/d blocks".
`M p` is the matrix of the smallest sums of block `p`, that is, the (min,+)-product of the p-th
blocks. 

### `Lemma36a.mul_sq_eq_cube_div`

 Proof of Lemma 36(a): "the entrywise minimum over the n/d blocks, which costs O(n³/d)
comparisons", and "Over the n/d pairs (A',B') ... Õ(n³/d) additional time" (Õ(n²) for each pair).
Here n = b * d: b blocks times n² entries is n³/d. 

 ### The list of the elements of a subset of `[d]` 

### `nodup_listOf`

 The list of the elements of `S` has no repetitions. 

### `mem_listOf`

 The list of the elements of `S` contains exactly the elements of `S`. 

### `length_listOf`

 The list of the elements of `S` has `|S|` entries. 

### `length_listOf_le`

 The list of the elements of `S` has at most `d` entries. 

 ### Comparison counts 

### `Lists.Valid.sum_length_le`

 `n` row lists and `n` column lists of at most `d` numbers contain at most `2nd` numbers. 

### `place_eq_of_color_eq`

 In a list with at most one number of each color, the color determines the place. 

### `comparisonCount_eq_card_colors`

 Section 5.2: "In the comparison counts of Lemma 36(a), every list has at most one number of each
color, so that γ(r,c) is the number of colors k with A[r,k] < B[k,c], where A[r,k] is the number of
color k in R_r and B[k,c] the one in C_c (a color missing from either list is skipped)".  The
bijection sends a pair of places of the same color to that color. 

 ### A counting call is `d` comparison counts 

### `lemma_36a_valid`

 Lemma 36(a): the comparison counts of a counting call have "n row lists and n column
lists of at most d numbers". 

### `lemma_36a_colors`

 Lemma 36(a): "with at most one number of each color in a list". 

### `lemma_36a_count`

 Proof of Lemma 36(a): "By Fredman's trick, A'[i,k'] + B'[k',j] < A'[i,k] + B'[k,j] if
and only if A'[i,k'] - A'[i,k] < B'[k,j] - B'[k',j] ...  Thus the count of a pair (i,j) ∈ P_k is the
comparison count γ(i,j) of these lists with P := P_k."  Also with ≤. 

### `lemma_36a_pairs`

 Lemma 36(a): "with pair sets P_1, …, P_d satisfying ∑_k |P_k| = n²". 

### `lemma_36a_subtractions`

 Lemma 36(a): "forming its lists costs O(nd²) subtractions" (the proof of Lemma 36: "O(nd)
subtractions for each k").  Every number in a list is formed by one subtraction, so the number of
subtractions is the total length of the lists. 
