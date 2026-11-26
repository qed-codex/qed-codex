---
{
  "module": "proof/rates/GeneralPieces/Ring/LemmaQ.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Ring/LemmaQ.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Ring/LemmaQ.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The lemma on the operators Q_s, on the ring ℚ[t₁, t₂, …]

`GeneralPieces.lemmaQ` is a conditional statement. Its conclusion is Lemma 9 of Appendix B in the
form in which the paper states it (`AppHalfPieces.LemmaQ`): for h ≥ 1, b ∈ V_h, a a combination of
monomials of weight at most
h, on V_E. It is derived from the same three claims for the integer matrices of the operators, in
which a is an integer combination of monomials, given as a list of (coefficient, parts) pairs, b is
a
monomial and the claim is about one entry; these are the hypotheses `StMatA`, `StMatB`, `StMatC`,
and they carry the content of the lemma. They are proved along the paper's proof of the lemma:
`proof/rates/GeneralPieces/Main.lean` proves them by applying `GeneralPieces.Series.Qk_eq_Qk'_of`,
`Qk_eq_zero_of` and `sum_Qk_of` to the expansion of f₊ and f₋ (`AppHalfPieces.stExpansion`).
The steps: "All three claims are linear in a and b", and in the polynomial they are applied to
(`Tri`, `Tri.eq_zero`), so a, b and f may be taken to be monomials; for a monomial a of weight h',
a^⟨i⟩ = C(h'+h, i)·a (`angle_tpow`); the coefficients of a[r]b[r']t^σ are the entries of the product
of the two matrices (`coef_comp`), because b[r']t^σ has weight |σ| + r' by (O1).
The facts on a[r] that come with display (47) (proved as `GeneralPieces.opFacts`), the property (O1)
(`GeneralPieces.o1`) and the agreement of the matrices with the operators (`GeneralPieces.stBridge`)
are hypotheses as well.
`proof/rates/GeneralPieces/Main.lean` feeds all of them in and has the lemma without hypotheses. 

 ### The three claims for the matrices 

### `StMatA`

 Claim (a) for the matrices. 

### `StMatB`

 Claim (b) for the matrices. 

### `StMatC`

 Claim (c) for the matrices, with the constant a[−h]b, the entry in the row of the monomial 1 and
the column of b of the matrix of a[−h]. 

 ### Coefficients 

### `eq_sum_of_subset`

 A polynomial is the sum of its monomials, over any finite set of partitions that contains all
that occur. 

### `eq_sum_ptnsZ`

 A polynomial of weight E is a combination of the t^μ with |μ| = E. 

### `ptnsLe`

 The partitions of weight at most h. 

### `eq_sum_ptnsLe`

 a = Σ_{h' ≤ h} ā_{h'} is a combination of the t^μ with |μ| ≤ h. 

 ### "All three claims are linear in a and b" 

### `Tri`

 T(a, b, f) is linear in each of a, b and f. 

### `eq_zero`

 "So let a = t^μ with |μ| = h' ≤ h and b = t^ν": a claim T(a, b, f) = 0 that is linear in a, b
and f holds for all a = Σ_{h' ≤ h} ā_{h'}, b ∈ V_h and f ∈ V_E if it holds for monomials. 

### `tri_ab`

 a^⟨i⟩[r] b[r'] f is linear in a, b and f. 

### `tri_ba`

 b[r'] a^⟨i⟩[r] f is linear in a, b and f. 

### `tri_Q`

 Q_s(a, b) f is linear in a, b and f. 

### `tri_Q'`

 The same with the factors exchanged. 

### `tri_pairing`

 (a[−h]b)·f is linear in a, b and f. 

 ### Monomials 

### `lst`

 The parts of a partition, listed, as natural numbers. 

### `angle_tpow`

 "Then a^⟨i⟩ = C(H, i)·a with H = h' + h", for a = t^μ with |μ| = h' ≤ h. 

### `coef_op_tpow`

 The coefficients of a[r]t^σ, for a monomial a, are the entries of the matrix. 

### `sum_Pz`

 A sum over the multisets of positive natural numbers with sum m is a sum over the partitions of
m. 

### `coef_comp`

 The coefficients of a[r]b[r']t^σ, for monomials a and b, are the entries of the product of the
two matrices: by (O1), b[r']t^σ is a combination of the t^τ with |τ| = |σ| + r'. 

### `coef_Q_mon`

 The coefficients of Q_s(a, b)t^σ for monomials a and b. 

### `coef_Q'_mon`

 The same with the factors exchanged. 

### `pairing_mon`

 The number a[−h]b for monomials a and b is the entry in the row of the monomial 1 and the column
of b of the matrix of a[−h]. 

### `lemmaQ`

 If the three claims of Lemma 9 on the operators Q_s hold for the matrices, the lemma holds in
the form in which the paper states it. The hypotheses are proved in the file named at the head. 
