---
{
  "module": "ThreeSumApsp/Sec3/Theorem17/Instances.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec3/Theorem17/Instances.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec3/Theorem17/Instances.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Theorem 17, second step: the instances

With `s = ⌊√D⌋`, the part `C` is split into `h` pieces of at most `⌈s/g⌉` vertices, the pairs
`(a,b)` are grouped by `ϱ = w(a,b) mod p` into the sets `W_ϱ`, and every `W_ϱ` is cut into chunks of
at most `n²/√D` pairs.  There is one instance of Lop-AE-SparseTri(n, D) for each chunk and each
piece.  As in the paper:

* the pieces, and `h ≤ ⌈ng/s⌉` (`existsUnique_mem_piece`, `card_piece_le`,
  `numPieces_le`);
* the sets `W_ϱ` and their chunks (`TriangleInstance.existsUnique_mem_residueClass`,
  `TriangleInstance.card_chunkOf_le`);
* there are at most `p + √D ≤ 2√D` chunks in all (`TriangleInstance.totalChunks_le`); as a chunk
  holds a whole number of pairs, this rests on `n² < (s + 1)⌊n²/√D⌋ + p` (`sq_lt_mul_queryCap_add`);
* the middle part has at most `sp ≤ D` vertices (`TriangleInstance.middleAtMost_lopInstance`);
* within a chunk, `S(a,b,c) ≡ 0 (mod p)` is an equality of labels
  (`TriangleInstance.S_modEq_zero_iff`), so a query pair has a common neighbor if and only if some
  `c` in the piece has `S(a,b,c) ≡ 0 (mod p)` (`TriangleInstance.inTriangle_lopInstance_iff`);
* there are at most `2√D h ≤ 4ng` instances (`le_sOf_and_sqrt_le`,
  `TriangleInstance.card_instanceIndices_le`).

The file ends with a remark of Section 3.1 and of Remark 20: a vertex of `A` or `B` has at most
`⌈s/g⌉` neighbors in an instance (`TriangleInstance.ncard_nbr_lopInstance_le`).  Nothing else rests
on it.


 ### The pieces 

### `sOf_le_sqrt`

 `s = ⌊√D⌋ ≤ √D`. 

### `sqrt_lt_sOf_add_one`

 `√D < s + 1`. 

### `sOf_pos`

 `s > 0` because `D ≥ 16`. 

### `pieceSize_pos`

 The bound `⌈s/g⌉` on the size of a piece is at least 1. 

### `pieceSize_le_sOf`

 `⌈s/g⌉ ≤ s` because `g ≥ 1`. 

### `mem_piece`

 A vertex lies in the piece number `k` exactly if its number divided by `⌈s/g⌉` is `k`. 

### `existsUnique_mem_piece`

 Proof of Theorem 17: "split C into pieces C₁, …, C_h of at most ⌈s/g⌉ vertices each": every
vertex of `C` lies in exactly one of the `h` pieces. 

### `card_piece_le`

 Proof of Theorem 17, "pieces [...] of at most ⌈s/g⌉ vertices each": `|C_k| ≤ ⌈s/g⌉`, because the
numbers of the vertices of the piece number `k` lie in `[k ⌈s/g⌉, (k + 1) ⌈s/g⌉)`. 

### `numPieces_le`

 Proof of Theorem 17: "so that h ≤ ⌈ng/s⌉". 

 ### Residues 

### `resFin`

 The residue of the integer `x` modulo `p`, as an element of `Fin p`. 

### `resFin_modEq`

 The residue of `x` is congruent to `x`. 

### `modEq_iff_eq_resFin`

 An element of `Fin p` is congruent to `x` modulo `p` exactly if it is the residue of `x`. 

 ### The arithmetic behind the two counts 

### `numChunks_mul_le`

 The number `⌈|S|/cap⌉` of chunks of `S` satisfies `⌈|S|/cap⌉ cap ≤ |S| + cap − 1`. 

### `one_le_gap_mul`

 `s + 1` exceeds `√D` by at least `1/(2√D + 1)`: since `(s + 1)²` and `D` are integers,
`1 ≤ (s + 1)² − D = (s + 1 − √D)(s + 1 + √D)`. 

### `sq_lt_mul_queryCap_add`

 The inequality behind "at most p + √D [...] chunks": `n² < (s + 1) ⌊n²/√D⌋ + p`.

Write `r = √D`, `x = n²/r` and `δ = s + 1 − r`.  Then
`(s + 1)⌊x⌋ > (s + 1)(x − 1) = n² + xδ − (s + 1)`, so it is enough that `xδ ≥ r/2 + 1 ≥ s + 1 − p`.
This holds because `x ≥ r³` (as `D ≤ n`), `δ ≥ 1/(2r + 1)` (as `D` is an integer) and `r ≥ 4`. 

### `le_sOf_and_sqrt_le`

 Proof of Theorem 17: the two facts used for the count of the instances, "s ≥ √D − 1 ≥ 3√D/4
because D ≥ 16, and √D ≤ √n ≤ 2n/3 because D ≤ n and we may assume n ≥ 3". 

 ### The sets `W_ϱ` 

### `mem_residueClass`

 A pair lies in `W_ϱ` exactly if `ϱ` is the residue of its weight. 

### `existsUnique_mem_residueClass`

 Proof of Theorem 17, the sets `W_ϱ` for `ϱ ∈ ℤ_p`: every pair `(a,b) ∈ A × B` lies in exactly
one of them. 

### `sum_card_residueClass`

 The sets `W_ϱ` have `n²` pairs in all. 

 ### The chunks 

### `card_chunkOf_le`

 Proof of Theorem 17: "cut it into chunks of at most n²/√D query pairs".  (The chunks of `W_ϱ`
cover it: `biUnion_chunk`.) 

### `totalChunks_le_add_sOf`

 There are at most `p + s` chunks in all.  Each `W_ϱ` has at most `(|W_ϱ| + cap − 1)/cap` chunks,
where `cap = ⌊n²/√D⌋`, so `p + s + 1` chunks or more would need `n² ≥ (s + 1) cap + p` pairs. 

### `totalChunks_le`

 Proof of Theorem 17: "There are at most p + √D ≤ 2√D chunks in all."

NOTE.  A chunk holds a whole number of pairs, at most `⌊n²/√D⌋`, so the count is at most
`p + (n² − p)/⌊n²/√D⌋`, and the second term can exceed `√D` slightly.  The printed bound is still
true, because the count is an integer, `D` is an integer and `D ≤ n` (`sq_lt_mul_queryCap_add`). 

 ### The instances 

### `middleAtMost_lopInstance`

 Proof of Theorem 17: "middle part C_k × ℤ_p, of size at most sp ≤ D".  So each instance is an
instance of Lop-AE-SparseTri(n, D). 

### `mem_lopInstance_W`

 A query pair of the instance with index `(ϱ, j, k)` lies in `W_ϱ`, and `j` is the number of its
chunk. 

### `S_modEq_zero_iff`

 Proof of Theorem 17: "Within the chunk, the condition S(a,b,c) ≡ 0 (mod p) has become the
equality w(a,c) + ϱ ≡ −w(b,c) of a label of (a,c) and a label of (b,c)". 

### `inTriangle_lopInstance_iff`

 Proof of Theorem 17: "a query pair (a,b) ∈ 𝒬 has a common neighbor if and only if some c ∈ C_k
has S(a,b,c) ≡ 0 (mod p)". 

### `mem_instanceIndices`

 Proof of Theorem 17, "For each chunk 𝒬 ⊆ W_ϱ and each piece C_k": `(ϱ, j, k)` is the index of an
instance exactly if `j` is the number of a chunk of `W_ϱ` and `k` the number of a piece. 

### `card_instanceIndices`

 There are as many instances as chunks times pieces. 

### `card_instanceIndices_le`

 Proof of Theorem 17: "There are at most 2√D h ≤ 2√D(ng/s + 1) ≤ 4ng instances". 

 ### The neighborhoods in an instance 

### `LopInstance.nbrA`

 Section 3.1, offline Set Disjointness: "the sets are the neighborhoods in M of the vertices of A
and B".  The set of `a ∈ A`. 

### `LopInstance.nbrB`

 Section 3.1, offline Set Disjointness: the set of `b ∈ B`. 

### `ncard_graph`

 The graph of a function into `Fin p` has as many points as the domain. 

### `TriangleInstance.ncard_nbr_lopInstance_le`

 Section 3.1, "The reductions below [...] produce at most n²/√D query pairs and sets of at most
√D elements", and Remark 20, "every vertex of A has O(√D/g) neighbors in the middle part": in an
instance of the reduction, a vertex of `A` or of `B` has exactly one neighbor `(c, σ)` for every
`c ∈ C_k`, hence at most `⌈s/g⌉` neighbors.  (And `⌈s/g⌉ ≤ s ≤ √D`; for `g ≤ √D` also
`⌈s/g⌉ ≤ 2√D/g`, `pieceSize_le_two_mul_sqrt_div`.) 
