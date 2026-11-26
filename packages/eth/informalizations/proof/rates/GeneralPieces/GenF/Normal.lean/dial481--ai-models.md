---
{
  "module": "proof/rates/GeneralPieces/GenF/Normal.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/GenF/Normal.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/GenF/Normal.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Lemma 9 (Appendix B), proof, paragraph "One Laurent polynomial": the differential equation of ⟨𝒩⟩

𝒩 = e^{A⁺}·e^{B⁺}·e^{A⁻}·e^{B⁻} is the product defined in the paragraph "Generating functions" of
that proof. Here ⟨𝒩⟩ (`normal`) is differentiated with respect to each of the variables x_n, x'_n
(`pderiv_normal`, `stNeq`).
"Multiplications commute with each other, and so do differentiations": so the derivative with
respect to the inner variable x_n brings down the factor J_n^+(u) on the left and J_n^-(u) on the
right, and
the derivative with respect to the outer variable brings down J_n^+(v) and J_n^-(v). On the left,
the coefficient of t^σ in t_l·w is the coefficient of t^{σ−l} in w (`braW_C_sel_mul`);
on the right, e^{A⁻}·e^{B⁻}·t^σ' is the product, over the parts k of σ', of t_k plus a linear form
in the x_n, x'_n without any t (`Phi` is a ring homomorphism, `ket` is a product), so the derivative
replaces each factor in turn
by the coefficient of the variable in that linear form (`der_factor`, `pderiv_Phi_ket`). The result:
the derivative of ⟨𝒩⟩ for (σ, σ') is a combination of the ⟨𝒩⟩ for (σ − l, σ') and (σ, σ' − k) whose
coefficients are numbers times powers of u, or of v. The statements of the paper on the coefficients
of ⟨𝒩⟩ are derived from this equation (in the form `StNeq`); the paper reads them off 𝒩 directly,
without a differential equation. 

 ### The product rule, for any ring of coefficients 

### `der_multiset_prod`

 The product rule for a product over a multiset. 

### `pderiv_expD_prod`

 ∂/∂x_i of e^𝒪 applied to a product: if ∂f_k/∂x_i + O_i f_k = g_k and e^𝒪 fixes g_k, each factor
in turn is replaced by g_k. 

### `pderiv_three`

 ∂/∂x_i of e^a·e^b·c. 

 ### The operators in A⁻ on the series without any t_k and on the t_k 

### `Normal.JmT_emb`

 J_n^-(u) vanishes on the constant polynomials. 

### `Phi_embW`

 e^{A⁻} fixes the series without any t_k. 

### `JmT_tT`

 J_n^-(u) maps t_k to k·C(−k−1, n−1)·u^{−k−n}. 

### `DD_tT`

 The operator beside x_i in A⁻ maps t_k to k times the coefficient of x_i in 𝖠_k. 

 ### The right side: e^{A⁻}·e^{B⁻}·t^σ' 

### `der_factor`

 ∂/∂x_i + (the operator beside x_i in A⁻), on a factor t_k + k·(the coefficient of ∇_k in B⁻) of
e^{B⁻}·t^σ'. 

### `pderiv_Phi_ket`

 ∂/∂x_i of e^{A⁻}·e^{B⁻}·t^σ': each factor t_k of t^σ' in turn is replaced by k·C(−k−1,
n−1)·u^{−k−n}, or ·v^{−k−n}. 

 ### The left side: e^{A⁺}·e^{B⁺}, and the equation 

### `braW_C_sel_mul`

 The coefficient of t^σ in (the series beside x_i in A⁺ + B⁺)·w: each factor t_l of t^σ in turn
is taken away, with the coefficient C(l−1, n−1)·u^{l−n}, or ·v^{l−n}. 

### `pderiv_normal`

 The differential equation of ⟨𝒩⟩ in every variable x_i, for |σ| ≤ E: one term for every
different part l of σ, from A⁺ or B⁺, and one for every different part k of σ', from A⁻ or B⁻. 

### `stNeq`

 The differential equation of ⟨𝒩⟩, as the statement from which the coefficients of ⟨𝒩⟩ are read
off. 
