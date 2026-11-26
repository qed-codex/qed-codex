---
{
  "module": "ThreeSumApsp/Programs/Sec3/Theorem17/Host/InstanceFacts.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem17/Host/InstanceFacts.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem17/Host/InstanceFacts.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The host of Theorem 17: what is true of the list of its instances

Proof of Theorem 17.  A `HostData` describes the instances that the host forms after the prime has
been chosen, the answers of the solver, and the scans.  This file proves, without any program in
sight:

* the instances are well formed: pieces, chunks, query pairs and matrices have the sizes that the
  solver asks for (`Valid.piece_le`, `Valid.lo_add_le`, `Valid.length_WI`, `length_matX`, …);
* the query pair number `i` of instance `t` is `(rowOf t i, colOf t i)`, read off its place
  `a n + b` (`getD_WI`, `getD_WJ`), which is the entry at position `lo t + i` of the list of all
  pairs; every pair meets every vertex of `C` in some instance (`Valid.exists_query`);
* a query pair `(a, b)` is accepted if and only if the piece has a vertex `c` with `p ∣ S(a,b,c)`,
  where `S(a,b,c) = w(a,b) + w(b,c) + w(a,c)` is `sumAt` (`acc_iff`), and its scan succeeds if and
  only if the piece has a `c` with `S(a,b,c) = 0` (`hit_iff`);
* a zero triangle is found if and only if there is one (`found_m`; for the reduction on finite sets,
  of which `theorem_17` speaks, the same sentence is `TriangleInstance.exists_mem_acceptedPairs`,
  and neither proof uses the other);
* all scans but one fail (`sum_execs_le`);
* the parameters of Theorem 17 give valid data (`valid_of_params`).


### `Valid`

 What is assumed about the data: positive sizes, a piece with its labels fits into the middle
part, and three lists of `n²` weights. 

 ## Residues, pieces and chunks 

### `Valid.p_ne`

 The prime is not 0. 

### `Valid.rab_lt`

 All residues are below `p`. 

### `Valid.length_sortedIdx`

 The list of all pairs has `n²` entries. 

### `div_chunkCount_lt`

 The number `t / chunkCount` of the piece of an instance `t < m` is below the number of pieces.


### `mod_chunkCount_lt`

 The number `t % chunkCount` of the chunk of an instance `t < m` is below the number of chunks.


### `chunk_mem`

 The chunk of an instance is an entry of the table of the chunks. 

### `Valid.chunk_entry`

 The residue of a chunk is below `p`; a chunk has between 1 and `cap` pairs, and it ends within
the list of all pairs. 

### `Valid.rho_lt`

 The residue of a chunk is below `p`. 

### `w_le_cap`

 A chunk has at most `cap` pairs. 

### `Valid.lo_add_le`

 A chunk ends within the list of all pairs. 

### `Valid.c0_lt`

 A piece starts below `n`. 

### `len_le`

 A piece has at most `q` vertices. 

### `Valid.piece_le`

 A piece ends within `C`. 

### `Valid.len_mul_le`

 A piece with its labels fits into the middle part. 

 ## The query pairs of an instance 

### `place`

 The place `a n + b` of the query pair `(a, b)` number `i` of instance `t`: the entry at position
`lo t + i` of the list of all pairs. 

### `rowOf`

 The vertex `a` of the query pair number `i` of instance `t`. 

### `colOf`

 The vertex `b` of the query pair number `i` of instance `t`. 

### `getD_WI`

 The rows of the query pairs, as the host lists them. 

### `getD_WJ`

 The columns of the query pairs, as the host lists them. 

### `Valid.place_lt`

 A place is below `n²`. 

### `Valid.rowOf_lt`

 The row of a query pair is a vertex of `A`. 

### `Valid.colOf_lt`

 The column of a query pair is a vertex of `B`. 

### `rowOf_mul_add_colOf`

 The pair gives the place back. 

### `Valid.rab_place`

 The weight `w(a,b)` of a query pair has the residue of its chunk. 

### `zip_eq`

 The query pairs of an instance, from the places. 

### `nodup_zip`

 No query pair is listed twice. 

### `lt_of_mem_WI`

 The rows of the query pairs are vertices of `A`. 

### `lt_of_mem_WJ`

 The columns of the query pairs are vertices of `B`. 

### `Valid.length_QI`

 The list of the rows of all pairs has `n²` entries. 

### `Valid.length_QJ`

 The list of the columns of all pairs has `n²` entries. 

### `Valid.length_WI`

 An instance lists the row of each of its query pairs. 

### `Valid.length_WJ`

 An instance lists the column of each of its query pairs. 

 ## The two matrices of an instance 

### `length_matX`

 The matrix `X` has `n` rows and `D` columns. 

### `length_matY`

 The matrix `Y` has `D` rows and `n` columns. 

### `matX_zero_or_one`

 The entries of `X` are 0 and 1. 

### `matY_zero_or_one`

 The entries of `Y` are 0 and 1. 

### `Valid.exists_getD_sortedIdx`

 Every place stands at some position of the list of all pairs. 

### `Valid.exists_query`

 Proof of Theorem 17, "its c lies in some piece": every pair `(a, b)` is a query pair of an
instance whose piece contains a given vertex `c`. 

 ## Acceptance 

### `sumAt`

 The weight `S(a,b,c) = w(a,b) + w(b,c) + w(a,c)` of the triangle `(a, b, c)`, read from the
three lists. 

### `sum_ne_zero_iff`

 A sum of numbers that are 0 or 1 is not 0 if and only if one of them is 1. 

### `labels_eq_iff`

 Proof of Theorem 17: "the condition S(a,b,c) ≡ 0 (mod p) has become the equality w(a,c) + ϱ ≡
−w(b,c) of a label of (a,c) and a label of (b,c)".  Here `wAC`, `wAB` and `wBC` are the three
weights, and `ϱ` is the residue of `wAB`. 

### `getD_xList`

 An entry of the matrix `X` of an instance. 

### `getD_yList`

 An entry of the matrix `Y` of an instance. 

### `thinEntry_ne_zero_iff`

 The entry `(XY)[a, b]` of an instance is not 0 if and only if the labels of `a` and `b` agree at
some vertex of the piece. 

### `Valid.getD_ans`

 The answer of the solver for a query pair: 1 if `(XY)[a, b] ≠ 0`, and 0 otherwise. 

### `acc_iff`

 Proof of Theorem 17: "a query pair (a,b) ∈ 𝒬 has a common neighbor if and only if some c ∈ C_k
has S(a,b,c) ≡ 0 (mod p)". 

### `hit_iff`

 Proof of Theorem 17, "scan the piece C_k of its instance for a c with S(a,b,c) = 0": when the
scan succeeds.


 ## Correctness 

### `hasZero_iff_sumAt`

 Brute force finds a zero triangle if and only if there is one. 

### `found_iff`

 A zero triangle has been found before instance `T` if and only if some accepted query pair of an
earlier instance has a successful scan. 

### `found_m`

 Proof of Theorem 17: "A zero triangle is always found, since its c lies in some piece and makes
the oracle accept its pair."  After all instances a zero triangle has been found if and only if
there is one.


### `sum_execs_le`

 Proof of Theorem 17: "We stop as soon as a zero triangle is found", so all scans but one fail.


### `valid_of_params`

 The parameters of Theorem 17 give valid data. 
