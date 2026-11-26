---
{
  "module": "ThreeSumApsp/Sec5/Corollary40.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec5/Corollary40.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec5/Corollary40.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Corollary 40: the hinted Mv conjectures

Conjectures 5.2 and 5.7 of [vdBNS19] fail for `0 < τ < 1/18` (Phase 2 in `O(n^{2-0.063τ})` time,
Phase 3 in `O(n^{1+0.437τ})`) and Conjecture 5.12 for `0 < τ₁ < τ₂/18`, because the data structure
of Corollary 26 answers the last phase by queries; with smaller savings they fail up to `ε*`.
Running times are not defined here.  This file proves the parts of the proof that are not running
times.
* "We compute over ℤ with 0/1 matrices; a Boolean entry is 1 exactly when the corresponding integer
  entry is positive" (`boolMul_eq_true_iff_pos`).  So the outputs of the first two problems are
  signs of entries of an integer product `XY` (`vHintedOutput_eq_true_iff`,
  `MvHintedOutput_eq_true_iff`).  For Conjecture 5.12 the product is cut into blocks of rows
  (`mul_apply_eq_blockOfRows_mul`).
* "In each case the phases beat the conjectured bounds": running times with exponents below all the
  bounds of a conjecture refute it (`not_conjecture52_of_achieves`,
  `not_conjecture57_of_achieves`, `not_conjecture512_of_achieves`).
* The variant with a sparse matrix as the hint (Section 5.4) is again a product with a small inner
  dimension (`boolMul_boolMul_eq_boolMul_submatrix`).

Nothing else rests on `mul_apply_eq_blockOfRows_mul` and `boolMul_boolMul_eq_boolMul_submatrix`.


 ### Boolean products from integer products 

### `boolMul_eq_true`

 An entry of a Boolean product is true exactly if some term of it is. 

### `toInt_eq_one_iff`

 An entry of the 0/1 matrix of a Boolean matrix is 1 exactly if the Boolean entry is true. 

### `toInt_nonneg`

 The entries of a 0/1 matrix are not negative. 

### `abs_toInt_le`

 The entries of a 0/1 matrix are at most 1 in absolute value. 

### `toInt_mul_toInt`

 A term of a product of 0/1 matrices is 0 or 1, and it is 1 exactly if both entries are true. 

### `boolMul_eq_true_iff_pos`

 Proof of Corollary 40: "We compute over ℤ with 0/1 matrices; a Boolean entry is 1 exactly when
the corresponding integer entry is positive." 

### `vHintedOutput_eq_true_iff`

 Proof of Corollary 40, paragraph "Conjecture 5.2 of [vdBNS19]": "we preprocess X := M and Y := V
...  In Phase 3, the n entries of column i of MV are n queries". 

### `MvHintedOutput_eq_true_iff`

 Proof of Corollary 40, paragraph "Conjecture 5.7 of [vdBNS19]": "The proof is the same, with
X := N_{[n],I} and Y := V, which are both known in Phase 2 (X may have repeated columns, which do
not affect the argument)." 

### `mul_apply_eq_blockOfRows_mul`

 Proof of Corollary 40, paragraph "Conjecture 5.12 of [vdBNS19]": "Cut the n rows of U into n/t₂
blocks of t₂ rows, and preprocess each of the n/t₂ products of a block with Y, which are products of
a t₂ × t₁ matrix by a t₁ × t₂ matrix". Here n = b * t₂.  Every entry of XY is an entry of one of
these products. 

 ### From the running times to "the conjecture fails"

Running times are not defined in this file.  See `Conjecture52` for the meaning of `Achieves`;
`hmono` says that an algorithm that meets a time bound meets every larger one. 

### `not_conjecture52_of_achieves`

 Corollary 40: "In each case the phases beat the conjectured bounds".  An algorithm whose
exponents `a₂`, `a₃` are below the bounds `ω` and `1 + τ` of Conjecture 5.2 refutes it: `ε` is the
smaller margin.  In Corollary 40, `a₂` is `2 - 0.063τ` or `2 - γτ`, which is below `ω` "whatever the
value of ω, since ω(1,1,τ) = ω(1,τ,1) ≥ 2", and `a₃` is `1 + 0.437τ` or `1 + τ/2`. 

### `not_conjecture57_of_achieves`

 Corollary 40: "In each case the phases beat the conjectured bounds".  Conjecture 5.7 has the two
bounds of Conjecture 5.2 for another problem, so `not_conjecture52_of_achieves` applies. 

### `not_conjecture512_of_achieves`

 Corollary 40: "In each case the phases beat the conjectured bounds", for the three bounds `ω₂`,
`ω₃`, `τ₁ + τ₂` of Conjecture 5.12.  In Corollary 40, Phase 2 only stores `I`, so `a₂ = τ₁`, and `τ₁
< ω(1,τ₁,1)` has to hold as well.  It does, since `τ₁ < 1` (Section 5.4) and `ω(1,τ₁,1) ≥ 2`. The
other two exponents are `1 + τ₂ - 0.063τ₁` or `1 + τ₂ - γτ₁`, below `ω(τ₂,τ₁,1) ≥ 1 + τ₂`, and `τ₂ +
0.437τ₁` or `τ₂ + τ₁/2`. 

 ### The discussion after Corollary 40 

### `boolMul_boolMul_eq_boolMul_submatrix`

 Section 5.4, on the variant of Conjecture 5.7 in [vdBSZ24] "in which Phase 2 gives a matrix with
at most n^τ nonzero entries instead of the vector I.  Our proof applies to this variant as well,
since after Phase 2 the product again has inner dimension at most n^τ".  In that variant M, P, V are
n × n Boolean matrices and the output is a column of M P V.  If the nonzero entries of P are at the
t positions (a_k, b_k), then M P V is the product of the n × t matrix of the columns a_k of M and
the t × n matrix of the rows b_k of V. 
