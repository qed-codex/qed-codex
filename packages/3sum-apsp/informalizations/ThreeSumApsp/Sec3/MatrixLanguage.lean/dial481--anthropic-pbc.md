---
{
  "module": "ThreeSumApsp/Sec3/MatrixLanguage.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec3/MatrixLanguage.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec3/MatrixLanguage.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Section 3.1: the lopsided problem in matrix language, and footnote 8

Section 3.1: "The counting version #Lop-AE-SparseTri(n,D) is also equivalent, up to polylogarithmic
factors, to [...] computing the wanted entries (XY)[I,J], (I,J) ∈ W, of a thin matrix product".
This file proves the two directions, without running times.  Of its lemmas, the programs for
Corollaries 15 and 16 use `LopInstance.numTriangles_ne_zero_iff` and `Footnote8.zero_one`; nothing
rests on the others.

* **From an instance to matrices.**  Number the at most `D` middle vertices of an instance by column
  indices (`LopInstance.MiddleAtMost.nonempty_embedding`), and let `X` and `Y` be its biadjacency
  matrices.  The Boolean product of `X` and `Y` has a 1 at `(a, b)` exactly if the pair lies in a
  triangle (`LopInstance.boolProduct_eq_one_iff_inTriangle`), and `(XY)[a,b]` is the number of
  common neighbors of `a` and `b` (`LopInstance.matX_mul_matY_apply`), which is nonzero exactly if
  the pair lies in a triangle (`LopInstance.matX_mul_matY_apply_ne_zero_iff`).  So an instance of
  #Lop-AE-SparseTri asks for the wanted entries of a thin matrix product
  (`LopInstance.isCountingAnswer_iff_isWantedEntries`), and its answer also answers Lop-AE-SparseTri
  (`LopInstance.isDetectionAnswer_of_isCountingAnswer`).
* **Footnote 8**, the converse.  The entries of a product of two 0/1 matrices are the triangle
  counts of an instance (`Footnote8.zero_one`).  The entries of a product of integer matrices with
  `β`-bit entries are combinations of the triangle counts of `4β²` instances
  (`Footnote8.entries_from_counts`): split into positive and negative parts (`Footnote8.parts`),
  write the entries in binary (`Footnote8.binary`), and multiply out (`Footnote8.product`).  Entries
  of absolute value `n^{O(1)}` have `O(log n)` bits (`Footnote8.bits`).


 ### The two tasks 

### `LopInstance.IsCountingAnswer`

 **Definition 14**, the task: "for every edge (a, b) ∈ W we ask for the number of triangles it
lies in".  `ans` is a correct answer to the instance `I` of #Lop-AE-SparseTri; its values outside
`W` are not constrained. 

### `IsWantedEntries`

 Section 3.1 and Theorem 5: "computing the wanted entries (XY)[I,J], (I,J) ∈ W, of a thin
matrix product".  `ans` gives the wanted entries of `XY`; its values outside `W` are not
constrained. 

 ### From an instance to matrices 

### `LopInstance.matX`

 Section 3.1: "let X ∈ {0,1}^{n×D} [...] be the biadjacency [matrix] of the edges between A and M
[...], that is, X[a,v] = 1 if and only if a ∈ A and v ∈ M are adjacent [...] (padded with zeros if M
has fewer than D vertices)".  The paper leaves the numbering of the middle vertices by column
indices implicit; here it is an arbitrary injection `e` of `M` into the `D` column indices, and the
columns outside its range are the padding. 

### `LopInstance.matY`

 Section 3.1: "Y ∈ {0,1}^{D×n} [...], Y[v,b] = 1 if and only if v ∈ M and b ∈ B are adjacent
(padded with zeros if M has fewer than D vertices)".  See `LopInstance.matX` for `e`. 

### `boolProduct`

 Section 3.1: "the Boolean product of X and Y", for matrices with entries 0 and 1: the entry at
`(a, b)` is 1 if `X[a,j] = Y[j,b] = 1` for some `j`, and 0 otherwise. 

### `MiddleAtMost.nonempty_embedding`

 Section 3.1, "(padded with zeros if M has fewer than D vertices)": a middle part of at most `D`
vertices can be numbered by column indices.  The lemmas below hold for every such numbering `e`. 

### `matX_apply_emb`

 Section 3.1: "X[a,v] = 1 if and only if a ∈ A and v ∈ M are adjacent".  The entry of `X` in the
column `e v` of the middle vertex `v`. 

### `matY_apply_emb`

 Section 3.1: "Y[v,b] = 1 if and only if v ∈ M and b ∈ B are adjacent".  The entry of `Y` in the
row `e v` of the middle vertex `v`. 

### `matX_apply_of_notMem_range`

 Section 3.1, "(padded with zeros if M has fewer than D vertices)": a column of `X` that belongs
to no middle vertex is zero. 

### `numTriangles_eq_card`

 The number of triangles through a pair, as the number of elements of a finite set. 

### `numTriangles_ne_zero_iff`

 A pair lies in a triangle exactly if its number of triangles is not zero. 

### `boolProduct_eq_one_iff_inTriangle`

 Section 3.1: "Lop-AE-SparseTri(n,D) asks for the entries of the Boolean product of X and Y at
the positions in W".  The entry at `(a, b)` is 1 exactly if the pair lies in a triangle. 

### `matX_mul_matY_apply`

 Section 3.1: "#Lop-AE-SparseTri(n,D) asks for the corresponding entries of the product of X and
Y over the integers"; proof of Corollary 15: "the entries (XY)[a,b] [...] are the numbers of common
neighbors". 

### `matX_mul_matY_apply_ne_zero_iff`

 Proof of Corollary 15: "and they are nonzero exactly for the query pairs that lie in a
triangle". 

### `isCountingAnswer_iff_isWantedEntries`

 Section 3.1, "In the language of Section 2, W is the set of wanted positions": the correct
answers to an instance of #Lop-AE-SparseTri are exactly the wanted entries of the thin product of
its two biadjacency matrices. 

### `isDetectionAnswer_of_isCountingAnswer`

 Proof of Corollary 15: a correct answer to the counting problem gives a correct answer to the
detection problem (Corollaries 15 and 16 solve both at once). 

 ### Footnote 8 

### `matPos`

 Footnote 8: the positive part of an integer matrix, entry by entry `max(x, 0)`. 

### `matNeg`

 Footnote 8: the negative part of an integer matrix, entry by entry `max(-x, 0)`, so that
`X = matPos X - matNeg X`. 

### `matBit`

 Footnote 8: "write their entries in binary, X = ∑_i 2^i X_i [...] with 0/1 matrices X_i".
`matBit X i` is `X_i`: its entries are the binary digits of weight `2^i` of the entries of `X` (used
for matrices with entries `≥ 0`). 

### `LopInstance.ofMatrices_middleAtMost`

 The instance that two matrices describe has the `D` column indices as its middle part. 

### `Footnote8.zero_one`

 Footnote 8, first sentence: "An instance of #Lop-AE-SparseTri(n,D) asks for the wanted entries
of a thin matrix product of two 0/1 matrices."  Conversely to `LopInstance.matX_mul_matY_apply`: the
entries of a product of two 0/1 matrices are the triangle counts of the instance `ofMatrices X Y W`,
whatever `W` is. 

### `Footnote8.parts`

 Footnote 8: "split each matrix into its positive and negative parts". 

### `emod_two_pow_eq_sum_digits`

 `x mod 2^β` is the sum of the last `β` binary digits of `x`, with their weights. 

### `Footnote8.binary`

 Footnote 8: "write their entries in binary, X = ∑_i 2^i X_i", for a matrix with entries in
`[0, 2^β)`. 

### `matBit_eq_zero_or_one`

 Footnote 8: "with 0/1 matrices X_i". 

### `Footnote8.product`

 Footnote 8: "Then XY = ∑_{i,j} 2^{i+j} X_i Y_j", for matrices with entries in `[0, 2^β)`. 

### `mul_apply_eq_sum_numTriangles`

 Footnote 8 for matrices with entries in `[0, 2^β)`: every entry of the product is a combination
of the triangle counts of the `β²` instances given by a binary digit of `X` and one of `Y`. 

### `matPos_matNeg_lt`

 The two parts of a matrix with entries of absolute value less than `2^β` have entries in
`[0, 2^β)`. 

### `Footnote8.entries_from_counts`

 Footnote 8, conclusion: "so a product with b-bit entries costs O(b²) instances
of #Lop-AE-SparseTri(n,D) with the same query pairs W".  (The paper's `b` is `β` here.)  For
matrices with entries of absolute value less than `2^β`, every entry of `XY` is the sum, with
weights `2^{i+j}` and signs +, −, −, +, of the triangle counts of the `4β²` instances given by a
binary digit of the positive or negative part of `X` and one of `Y`, all with the same `W`. 

### `Footnote8.bits`

 Footnote 8 with the sentence it belongs to, "matrices [...] whose entries have absolute value
n^{O(1)}": an integer of absolute value at most `n^c` has `β = ⌊c log₂ n⌋ + 1` bits, that is,
`O(log n)`, so that "O(b²) instances" is a polylogarithmic number. 
