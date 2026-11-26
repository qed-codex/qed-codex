---
{
  "module": "ThreeSumApsp/Spec/Sec4/Theorem30/PartialSums.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Spec/Sec4/Theorem30/PartialSums.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Spec/Sec4/Theorem30/PartialSums.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Bounds on the partial sums (proof of Theorem 30, "Word size")

"every value we compute is a sum of at most 10^m products of two such numbers".  A routine that adds
up numbers one after the other holds, at every moment, the sum of an initial part of a list.  This
file bounds all these sums, for two encodings whose entries are at most A and B in absolute value.

* What the dynamic program of Lemma 29 computes for a cube with e stars is at most 10^e A B
  (`abs_dpValue_le`), and so is every sum of an initial part of the ten values that it adds up
  for the cube (`abs_dp_partial_sum_le`).
* The numbers that a query adds up stand for disjoint sets of leaves contributing to its output
  string η (the paper's w), of which there are 10^m (`Lemma28.card_leaves`); so every sum of an
  initial part of them is at most 10^m A B (`abs_query_partial_sum_le`).


 ## The dynamic program of Lemma 29 

### `mul_nonneg_of_abs_le`

 A B ≥ 0 for bounds A, B on the two arrays. 

### `abs_mul_le`

 The product at a leaf is at most A B in absolute value. 

### `abs_dpValue_le`

 What the dynamic program computes at depth e is at most 10^e A B in absolute value. 

### `abs_dpValueD_le`

 What the dynamic program on digits computes for a cube at depth e is at most 10^e A B in
absolute value. 

### `abs_dp_partial_sum_le`

 The ten values that the dynamic program adds up for a box with e + 1 stars (the proof of Lemma
29), the star at position ℓ being replaced by the ten terms in the order of their digits: every sum
of an initial part of them is at most 10^{e+1} A B. 

 ## A query 

### `abs_query_partial_sum_le`

 Every sum of an initial part of the numbers that a query adds up is at most 10^m A B in absolute
value: the numbers stand for disjoint sets of leaves contributing to η, of which there are 10^m. 
