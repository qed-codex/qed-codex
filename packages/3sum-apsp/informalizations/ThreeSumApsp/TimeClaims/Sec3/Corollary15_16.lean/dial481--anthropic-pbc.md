---
{
  "module": "ThreeSumApsp/TimeClaims/Sec3/Corollary15_16.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/TimeClaims/Sec3/Corollary15_16.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/TimeClaims/Sec3/Corollary15_16.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Running-time claims of Section 3.1: Corollaries 15 and 16

All lemmas are about an arbitrary interpretation `M : DetTimeModel` of "is solved in time T".

* Corollary 15, first case, from Theorem 5 ("Apply Theorem 5 with N = n to the two biadjacency
  matrices"): `Corollary15.first_of_theorem_5`.
* Corollary 15, general case ("splitting W into sets of at most n²/√D query pairs"):
  `Corollary15.general_of_theorem_5`.  One call costs `O(n² log² D / D^{1/18})`, and all calls
  with the overhead cost `O((n² + |W| √D) log² D / D^{1/18})` (`dominated_calls`).
* Corollary 16 from Corollary 26 ("This is Corollary 26 with N = n"):
  `Corollary16.of_corollary_26`.

In each deduction the overheads `n D`, `|W|` and `1` of writing the matrices and copying the answers
are at most the bound of the corollary, because `n ≥ D^18`.  The bounds are added up by the calculus
of `Dominated` on the parameters `n`, `D`, `w`.


 ## The calculus on the parameters `n`, `D`, `w` 

### `LopSize`

 The parameters of an instance of (#)Lop-AE-SparseTri: `n` and `D` as in Definition 13, and the
number `w` of query pairs. 

### `LopSize.n`

 The number of vertices of the two large parts. 

### `LopSize.D`

 The bound on the number of vertices of the middle part. 

### `LopSize.w`

 The number of query pairs. 

### `exists_const_count_detect`

 From the time `T` for the product of the two biadjacency matrices to the times for counting and
for detection (the claims `LopCountFromThinProduct` and `LopDetectFromCount`): if `T` and the
overheads `n D`, `w` and `1` are `O(g)`, so are the two times, with one constant. 

 ## Corollary 15, the first case 

### `Corollary15.first_of_theorem_5`

 The deduction of the first case of Corollary 15 from Theorem 5: "Apply Theorem 5 with
N = n to the two biadjacency matrices". 

 ## Corollary 15, the general case 

### `dominated_calls`

 "For larger W, apply the theorem to each of at most [...] pieces": if one call costs
`O(n² log² D / D^{1/18})`, then all calls cost `O((n² + w √D) log² D / D^{1/18})`. 

### `Corollary15.general_of_theorem_5`

 The deduction of the general case of Corollary 15 from Theorem 5: "For larger W, apply
the theorem to each of at most [...] pieces." 

 ## Corollary 16 

### `Corollary16.of_corollary_26`

 The deduction of Corollary 16 from Corollary 26: "This is Corollary 26 with N = n,
applied to the two biadjacency matrices as above." 
