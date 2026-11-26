---
{
  "module": "ThreeSumApsp/Sec2/Lemma6/Monomials.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec2/Lemma6/Monomials.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec2/Lemma6/Monomials.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The monomials of Schönhage's identity

Two sentences of the paper about the monomials of `G + E`. No later file uses this one: the Lean
proof of `lemma_9` computes the values of `gamma` that it needs from the definition (`gamma_z0`,
`gamma_x_y_z`).

* Section 2.2, the first observation after Lemma 6: a monomial of `G` is a `p_ij q_ij z₀` or an
  `x_i y_j z_ij` (`monomials_G`), and a monomial of `E` has an outer output variable together with
  an inner left or right variable (`monomials_E`).
* Section 2.3.2: the `γ(s, t, z)` of equation (3) is the coefficient of the monomial `s t z` on the
  left-hand side of the identity and so, by Lemma 6, in `G + E` (`gamma_eq_coeff`).

Both rest on the expansion of a product of three linear forms, one in the left, one in the right and
one in the output variables, into the monomials `s t z` (`formL_mul_formR_mul_formO`). Distinct
triples give distinct monomials (`monomialSTZ_inj`), so the coefficient of `s t z` in such a product
is the product of the three coefficients (`coeff_monomialSTZ_forms`).


 ### Products of three linear forms 

### `monomialSTZ`

 The monomial `s t z` (Section 2.3.2), as an exponent vector. 

### `polyL_mul_polyR_mul_polyO`

 The product of a left, a right and an output variable is the monomial `s t z`. 

### `formL_mul_formR_mul_formO`

 The product of three linear forms, one in the left, one in the right and one in the output
variables, expanded into the monomials `s t z`. 

### `monomialSTZ_inj`

 Distinct triples of variables give distinct monomials `s t z`. 

### `coeff_monomialSTZ_forms`

 The coefficient of the monomial `s t z` in a product of three linear forms, one in the left, one
in the right and one in the output variables, is the product of the three coefficients. 

 ### The coefficients `γ` 

### `gamma_eq_coeff_sum`

 After equation (3): `γ(s, t, z)` is "the coefficient of the monomial stz on the
left-hand side of the identity." 

### `gamma_eq_coeff`

 Section 2.3.2: "By Lemma 6, it is also the coefficient of stz in G + E". 

 ### The monomials of `G` and of `E` 

### `exists_mem_support_of_sum`

 A monomial of a sum is a monomial of one of the summands. 

### `exists_of_mem_support_form_mul`

 Every monomial of a product `f g z` of a left form, a right form and an output variable is
`s t z` for a variable `s` of `f` and a variable `t` of `g`. 

### `isInner_of_pHat_ne_zero`

 Every variable of an entry of `p̂` is inner. 

### `isInner_of_qHat_ne_zero`

 Every variable of an entry of `q̂` is inner. 

### `monomials_G`

 Section 2.2, first observation: "every monomial of G consists only of inner variables (p_ij q_ij
z₀) or only of outer variables (x_i y_j z_ij)." 

### `monomials_E`

 Section 2.2, first observation: "every monomial of E has an outer output variable together with
an inner left or right variable." 
