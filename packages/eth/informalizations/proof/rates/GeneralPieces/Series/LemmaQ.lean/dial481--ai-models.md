---
{
  "module": "proof/rates/GeneralPieces/Series/LemmaQ.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Series/LemmaQ.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Series/LemmaQ.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The lemma on the operators Q_s, for matrices, with the constant a[−h]b

The three claims: (a) Q_s(a,b) does not change if the two factors are exchanged in all its products
at once; (b) Q_s(a,b) = 0 on the monomials of weight E for |s| > E + h;
(c) the Q_s(a,b) with |s| ≤ E + h add up to (a[−h]b)·Id. Here a is a combination of monomials of
    weight at most h (a list of pairs of a coefficient and a list of parts),
b is one monomial of weight h, and an operator is its matrix, with entries (π, σ) for monomials
without a part 0; the factor of b^μ is put in where the pieces are defined. The condition h ≥ 1 of
the
paper is not needed.
The proof is that of the paper: the claims are linear in a (`Qk_eq_sum`, `Qk'_eq_sum`), and for a
monomial they are read off the one Laurent polynomial F. The theorems here
take the expansion of f₊ and f₋ as a hypothesis; in the file
proof/rates/GeneralPieces/GenF/Main.lean it is proved from the equation in the proof of Lemma 9 that
writes the products in the two orders as e^κ·N and e^{κ'}·N.
Lemma 9 of the paper, on the ring, is `AppHalfPieces.lemmaQ` in the file
proof/rates/GeneralPieces/Main.lean; it applies the theorems of this file to the expansion directly. 

### `pairF`

 The number a[−h]b for a combination a of monomials: the entry (1, b) of the matrix of a[−h]. 

### `sum_list_comm`

 A sum over a finite set of sums over a list is the sum over the list of the sums over the set. 

### `sum_range_two_mul`

 For a monomial of weight h' ≤ h the sum over i ≤ 2h stops at H = h' + h, because C(H,i) = 0 for
i > H. 

### `Qk_eq_sum`

 Q_s(a,b) is linear in a, and a^{⟨i⟩} = C(H,i)·a for a monomial a. 

### `Qk'_eq_sum`

 The same with the factors exchanged. 

### `sum_qP_of`

 Claim (c) for monomials, with the constant a[−h]b. 

### `Qk_eq_Qk'_of`

 Claim (a): Q_s(a,b) does not change if the two factors are exchanged in all its products at
once. 

### `Qk_eq_zero_of`

 Claim (b): Q_s(a,b) vanishes on the monomials of weight E for |s| > E + h. 

### `sum_Qk_of`

 Claim (c): on the monomials of weight E, the Q_s(a,b) with |s| ≤ E + h add up to (a[−h]b)·Id. 
