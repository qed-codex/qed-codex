---
{
  "module": "ThreeSumApsp/Sec3/Theorem17.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec3/Theorem17.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec3/Theorem17.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Theorem 17: Exact Triangle reduces to Lop-AE-SparseTri

The proof has three steps.

1. Hashing: a prime `p` in the range `[√D/2, √D)` with few false positives is selected
   (`TriangleInstance.exists_isSelectedPrime`, `Hashing.F_le_falsePositiveConst_mul`).
2. The instances: there are at most `4ng` of them (`TriangleInstance.card_instanceIndices_le`), each
   with a middle part of at most `D` vertices (`TriangleInstance.middleAtMost_lopInstance`) and at
   most `n²/√D` query pairs (`TriangleInstance.card_chunkOf_le`).
3. Witnesses: the scans of the accepted pairs find a zero triangle if there is one, and all but one
   of them contain a false positive of their own (`Theorem17.correctness`,
   `TriangleInstance.F_add_one_mul_pieceSize_le`).

`theorem_17` puts them together.  Before it stand three smaller statements: the arithmetic behind
the terms `n^{ω+o(1)} D^{3/2}` and `n² D g` of the additional time (`theorem_17_hashing_sum_sq_le`,
`theorem_17_write_cost`), and that the accepted pairs can be put in some order
(`theorem_17_scanOrder_exists`).  The file ends with the part of Remark 18 that is about these
instances (`remark_18_block`).


 ### Two terms of the additional time, and the order of the scans 

### `theorem_17_hashing_sum_sq_le`

 Proof of Theorem 17: "each of them O(p²) word operations, so n^{ω+o(1)} D^{3/2} time over the
fewer than √D primes in the range": the sum of `p²` over the primes in the range is at most
`D^{3/2}`.  Only this sum is stated.  That the counts are read off a product of matrices over
ℤ[x]/(x^p − 1) (proof of Theorem 17) is a lemma of the library. 

### `theorem_17_write_cost`

 Proof of Theorem 17: "Writing them down costs O(n² D g): the two bipartite graphs of an instance
have O(nD) entries".  The two biadjacency matrices of an instance have `2nD` entries, and there are
at most `4ng` instances.  The statement is arithmetic on the number of instances: `2nD` is a number
here, not the size of an object.  The query pairs are not counted; the paper goes on "and the chunks
are computed once and shared by the pieces".

NOTE.
* `g ≤ √D` is not needed.
* `p` is any prime of the range, selected or not. 

### `theorem_17_scanOrder_exists`

 Proof of Theorem 17: the accepted pairs can be put in some order, so the statements about every
order of the scans are not empty. 

 ### Theorem 17 

### `theorem_17`

 **Theorem 17** (Exact Triangle to Lop-AE-SparseTri, deterministically), everything
except the running time: "Let 16 ≤ D ≤ n, and let 1 ≤ g ≤ √D be an integer.  Exact Triangle on n
vertices per part with weights of absolute value at most n^ν reduces deterministically to at most
4ng instances of Lop-AE-SparseTri(n, D), each with at most n²/√D query pairs [...].  The reduction
is non-adaptive: it produces all the instances before it makes any oracle call".

The reduction is defined step by step as in the proof: a selected prime `p`, the instances
`T.lopInstance D g p ι` for `ι ∈ T.instanceIndices D g p`, and the scans `T.runScans D g L` of the
accepted pairs in any order `L`.  Non-adaptivity is visible in the statement: the instances do not
depend on `ans`.  The answer is that of the search version (Section 3.2): a zero triangle, or the
report that there is none.  The last clause bounds the number of scans times the size of a piece, an
upper bound on the number of triples that the scans look at; this count is behind the term
`O(ν n³ log n/g)` of the additional time (`κ` is the paper's ν).  Its constant `C` depends on
nothing. Arithmetic behind the other two terms is in `theorem_17_hashing_sum_sq_le` and
`theorem_17_write_cost`.  For the time itself see `docs/REMARKS.md`, "Section 3: running times".

NOTE.  The paper does not say that `D` is an integer; here it is a natural number, as in every use
of the theorem, and the bound on the number of chunks uses this (see the library's lemma
`TriangleInstance.totalChunks_le`). 

 ### Remark 18 

### `remark_18_block`

 **Remark 18**: "With residues in place of their intervals, the block C_k × {−j} of our
instance for ϱ and C_k is their graph G_{−ϱ−j,j,ϱ}, and our instance puts the p graphs with the same
ϱ side by side."  The half of the sentence that is about our instance: a middle vertex `(c, σ)` with
`σ ≡ −j` is adjacent to `a` exactly if `w(a,c) ≡ −ϱ − j` and to `b` exactly if `w(b,c) ≡ j`, while
the query pairs have `w(a,b) ≡ ϱ`; these three residues, in this order, are the index of the graph.
The instance has the index `(ϱ, i, k)`: residue, chunk, piece.  The comparison with the graphs of
[VX20] is not formalized. 
