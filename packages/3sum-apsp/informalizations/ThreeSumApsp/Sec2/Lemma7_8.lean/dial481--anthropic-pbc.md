---
{
  "module": "ThreeSumApsp/Sec2/Lemma7_8.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec2/Lemma7_8.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec2/Lemma7_8.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Lemmas 7 and 8: what `Full` computes

Section 2.3.2. Lemma 7: at the leaf `τ`, `Full(a, b)` multiplies `Φ_τ(a)` by
`Ψ_τ(b)`, and it returns `Mult(a, b)`, whose entry at `w` is the sum of these products over the
leaves contributing to `w` (equation (2)). Lemma 8:
`Mult(a, b)[w] = ∑_{u,v} γ(u₁, v₁, w₁) ⋯ γ(u_L, v_L, w_L) a[u] b[v]`, with the `γ` of equation (3).

* `Φ_τ` and `Ψ_τ` are the same expression for two families of linear forms (`encodeWith`), so what
  holds for both is proved once.
* Lemma 7 is proved by induction on `L`, as in the paper. Step (2) is the encoding:
  `Φ_{λτ'}(a) = Φ_{τ'}(A_λ)` and `Ψ_{λτ'}(b) = Ψ_{τ'}(B_λ)` (`Phi_cons`, `Psi_cons`). Step (4) is
  the decoding: the leaves contributing to `z w'` are the `λτ'` with `λ` contributing to `z` and
  `τ'` to `w'` (`Leaf.contributes_succ`), so `Full` and `Mult` both satisfy
  `c[z w'] = ∑_{λ contributing to z} C_λ[w']` (`Full_succ`, `Mult_succ`).
* Lemma 8: the leaves contributing to `w` choose a term contributing to `w_ℓ` independently at each
  level `ℓ` (`Leaf.filter_contributes_eq_piFinset`), so the sum over these leaves of a product over
  the levels is a product of sums (`prod_gamma_eq_sum_contributes`).


 ### Which leaves contribute to an output string 

### `Leaf.contributes_succ`

 In the proof of Lemma 7: "the leaves contributing to zw' are the λτ' with λ
contributing to z and τ' contributing to w'".  Here `λ = τ 0`, `τ' = Fin.tail τ`, `z = w 0` and
`w' = Fin.tail w`. 

### `sum_strings_succ`

 A sum over the strings of length `L + 1` is a sum over the first variable `s` and the rest `u'`
of the string `s u'`. 

### `Leaf.sum_contributes_succ`

 A sum over the leaves contributing to `w`, split by the first term of the leaf. 

### `Leaf.filter_contributes_eq_piFinset`

 In the proof of Lemma 8: the leaves contributing to `w` "are the leaves whose term at
level ℓ contributes to w_ℓ, independently for each ℓ". 

### `mem_Leaves`

 Membership in `Leaves(U)`. 

 ### The two encodings at once 

### `encodeWith`

 The number `∑_u a[u] ∏_ℓ c_{τ_ℓ}(u_ℓ)`, for an array `a` on the strings over a finite alphabet
and the coefficients `c` of a family of linear forms, one for each term. By definition it is
`Φ_τ(a)` for `c = φ` and `Ψ_τ(b)` for `c = ψ`. 

### `encodeWith_zero`

 For `L = 0` the only string is empty, and so are the products over the levels. 

### `encodeWith_cons`

 The number at the leaf `λτ'` for `a` is the number at the leaf `τ'` for `∑_s c_λ(s) a_s`. 

 ### Lemma 7 

### `Phi_cons`

 In the proof of Lemma 7: "for every leaf λτ' we have
Φ_{λτ'}(a) = ∑_s φ_λ(s) Φ_{τ'}(a_s) = Φ_{τ'}(A_λ)". 

### `Psi_cons`

 In the proof of Lemma 7: "and similarly Ψ_{λτ'}(b) = Ψ_{τ'}(B_λ)". 

### `Phi_zero`

 "For L = 0, the only leaf is the empty string τ, and Φ_τ(a) = a […], as the products over the
levels are empty" (proof of Lemma 7). 

### `Psi_zero`

 "and Ψ_τ(b) = b" (proof of Lemma 7). 

### `Lemma7.multiplied_at_leaf`

 **Lemma 7**, first half.  "At the leaf τ, Full(a, b) multiplies Φ_τ(a) by Ψ_τ(b)". 

### `Full_succ`

 Step (4) of `Full`, as it is read in the proof of Lemma 7:
`c[z w'] = ∑_{λ contributing to z} C_λ[w']`. 

### `Mult_succ`

 In the proof of Lemma 7:
`Mult(a, b)[z w'] = ∑_{λ contributing to z} Mult(A_λ, B_λ)[w']`. 

### `Lemma7.returns_Mult`

 **Lemma 7**, second half.  "and it returns Mult(a, b)." 

### `lemma_7`

 **Lemma 7**.  "At the leaf τ, Full(a, b) multiplies Φ_τ(a) by Ψ_τ(b), and it returns
Mult(a, b)." 

 ### Lemma 8 

### `prod_gamma_eq_sum_contributes`

 The display in the proof of Lemma 8: the sum, over the leaves `τ` contributing
to `w`, of `∏_ℓ φ_{τ_ℓ}(u_ℓ) ψ_{τ_ℓ}(v_ℓ)` "is the product of sums ∏_ℓ ∑_{τ_ℓ contributing to w_ℓ}
φ_{τ_ℓ}(u_ℓ) ψ_{τ_ℓ}(v_ℓ) = ∏_ℓ γ(u_ℓ, v_ℓ, w_ℓ) by (3)". 

### `lemma_8`

 **Lemma 8**.  "For all arrays a, b and every output string w,
Mult(a, b)[w] = ∑_{u,v} γ(u₁, v₁, w₁) γ(u₂, v₂, w₂) ⋯ γ(u_L, v_L, w_L) a[u] b[v],
the sum over all left strings u and right strings v." 
