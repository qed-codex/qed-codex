---
{
  "module": "ThreeSumApsp/Sec3/Theorem17/Witnesses.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec3/Theorem17/Witnesses.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec3/Theorem17/Witnesses.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Theorem 17, third step: witnesses

For every query pair that the oracle accepts, the piece `C_k` of its instance is scanned for a `c`
with `S(a,b,c) = 0`, and the scans stop at the first zero triangle.  As in the paper:

* a zero triangle is always found (`TriangleInstance.exists_mem_acceptedPairs`);
* a failed scan contains a false positive of `p`
  (`TriangleInstance.exists_isFalsePositive_of_mem_failedScans`), and distinct scans contain
  distinct false positives (`TriangleInstance.eq_of_mem_acceptedPairs`), so there are at most `F(p)`
  failed scans (`TriangleInstance.card_le_F_of_distinct_scans`,
  `TriangleInstance.card_failedScans_le`);
* a scan looks at at most `⌈s/g⌉ ≤ 2√D/g` vertices (`pieceSize_le_two_mul_sqrt_div`), so the scans
  cost `O((F(p) + 1)√D/g) = O(κ n³ log n/g)` (`TriangleInstance.F_add_one_mul_pieceSize_le`).

`Theorem17.correctness` puts the first two together.

The program for Theorem 17 works on lists, and for its lists the sentences of this step are lemmas
of their own: `HostData.found_m` answers `TriangleInstance.exists_mem_acceptedPairs`,
`HostData.exists_false_positive` answers
`TriangleInstance.exists_isFalsePositive_of_mem_failedScans`, `HostData.Valid.eq_of_place_eq`
answers `TriangleInstance.eq_of_mem_acceptedPairs`, and `HostData.sum_fails_le` answers
`TriangleInstance.card_failedScans_le`.  The two proofs share `F(p)`, the first step of the
proof, the number of instances and the counting step `TriangleInstance.card_le_F_of_distinct_scans`;
no theorem about programs rests on another lemma of this file.


 ### Scans and accepted pairs 

### `scanPiece_eq_some`

 Proof of Theorem 17, "scan the piece C_k of its instance for a c with S(a,b,c) = 0": a `c` that
a scan returns lies in the piece and has `S(a,b,c) = 0`. 

### `scanPiece_eq_none_iff`

 A scan fails exactly if the piece has no `c` with `S(a,b,c) = 0`. 

### `scanOf`

 The scan that belongs to `x = ((ϱ, j, k), (a, b))`, a query pair `(a, b)` of the instance with
index `(ϱ, j, k)`: the piece `C_k` is scanned for the pair `(a, b)`. 

### `runScans_spec`

 What the scans over a list of pairs return: a triangle that is returned is a zero triangle; if
none is returned, then every scan failed; and all the scans that are carried out, except possibly
the last one, fail. 

### `IsOracleAnswer`

 The hypothesis on the oracle: `ans ι` is a correct answer to the instance with index `ι`, for
every instance of the reduction. 

### `failedScans`

 Proof of Theorem 17: a "failed scan, of a piece C_k for a pair (a,b)": the oracle accepted the
pair in the instance, and the piece contains no `c` with `S(a,b,c) = 0`. 

### `mem_acceptedPairs`

 The accepted pairs: an index of an instance, a query pair of that instance, and the answer
"yes". 

 ### The sentences of the paragraph "Witnesses" 

### `exists_mem_acceptedPairs`

 Proof of Theorem 17: "A zero triangle is always found, since its c lies in some piece and makes
the oracle accept its pair." 

### `exists_isFalsePositive_of_mem_failedScans`

 Proof of Theorem 17: "A failed scan, of a piece C_k for a pair (a,b), contains a c ∈ C_k with
S(a,b,c) ≡ 0 (mod p) but S(a,b,c) ≠ 0, that is, a false positive (a,b,c) of p". 

### `eq_of_mem_acceptedPairs`

 Proof of Theorem 17: "distinct scans contain distinct false positives": a triple `(a,b,c)`
belongs to the scan of at most one accepted pair. 

### `card_le_F_of_distinct_scans`

 Proof of Theorem 17: "distinct scans contain distinct false positives, so there are at most F(p)
failed scans", for any finite family `s` of scans and any notion "the scan `x` contains the triple
`t`".  The scans of the accepted pairs (`card_failedScans_le`) and the scans of the program
(`HostData.sum_fails_le`) are two such families. 

### `card_failedScans_le`

 Proof of Theorem 17: "so there are at most F(p) failed scans". 

### `pieceSize_le_two_mul_sqrt_div`

 Proof of Theorem 17: the length of a scan, the `O(√D/g)` in "the scans cost O((F(p) + 1)√D/g)":
a piece has at most `⌈s/g⌉ ≤ 2√D/g` vertices. 

### `TriangleInstance.F_add_one_mul_pieceSize_le`

 Proof of Theorem 17: "the scans cost O((F(p) + 1)√D/g) = O(ν n³ log n/g)". 

 ### The output of the reduction 

### `Theorem17.correctness`

 **Theorem 17, correctness.**  Given any correct answers of an oracle for
Lop-AE-SparseTri to the instances of the reduction, and whatever the order `L` of the scans, the
reduction's output is correct: it is a zero triangle if one exists, and `none` otherwise.  It
carries out at most `F(p) + 1` scans ("We stop as soon as a zero triangle is found"). 
