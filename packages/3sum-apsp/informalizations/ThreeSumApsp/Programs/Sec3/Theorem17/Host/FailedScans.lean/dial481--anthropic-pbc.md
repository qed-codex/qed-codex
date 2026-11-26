---
{
  "module": "ThreeSumApsp/Programs/Sec3/Theorem17/Host/FailedScans.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem17/Host/FailedScans.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem17/Host/FailedScans.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The host of Theorem 17: failed scans and false positives

Proof of Theorem 17: "distinct scans contain distinct false positives, so there are at most F(p)
failed scans" (`HostData.sum_fails_le`).  An accepted query pair `(a, b)` of an instance whose scan
fails has a vertex `c` in the piece of the instance with `p ∣ S(a,b,c)` and `S(a,b,c) ≠ 0`
(`exists_false_positive`); such a triple is a false positive of `p`, and `F(p)` is their number.
Different pairs (instance, query pair) give different triples (`Valid.eq_of_place_eq`): `c`
determines the piece; `(a, b)` determines the place `a n + b`; the place determines the position in
the list of all pairs, which has no repetition; and the position determines the chunk.

The statement `theorem_17` is about the reduction on finite sets, and there the same sentences are
`TriangleInstance.exists_isFalsePositive_of_mem_failedScans`,
`TriangleInstance.eq_of_mem_acceptedPairs` and `TriangleInstance.card_failedScans_le`.  The two
proofs run in parallel.  They share `F(p)` and the counting step, which is stated for any family of
scans (`TriangleInstance.card_le_F_of_distinct_scans`).


### `Valid.eq_of_place_eq`

 Two query pairs at the same place, of instances with the same piece, are the same. 

### `exists_false_positive`

 Proof of Theorem 17: "A failed scan [...] contains a c ∈ C_k with S(a,b,c) ≡ 0 (mod p) but
S(a,b,c) ≠ 0". 

### `c0_add_div`

 A vertex of the piece of an instance determines the number of the piece. 

### `length_filter_range`

 The length of a filtered range, as the size of a set. 

### `sum_fails_le`

 Proof of Theorem 17: "distinct scans contain distinct false positives, so there are at most F(p)
failed scans". 
