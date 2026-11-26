---
{
  "module": "proof/rates/GeneralPieces/GenF/Bra.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/GenF/Bra.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/GenF/Bra.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The lemma on the operators Q_s, paragraph "Generating functions": elementary rules

Rules for the definitions of `Defs.lean` that the other files of this paragraph use: the two
families of variables (`sel`, `xi`, `xo`), linear and bilinear forms in the variables (`lin`,
`bil`), and
the coefficient of t^σ (`bra` on the series in v, `braW` on the power series in the x_n, x'_n). The
main rule is `bra_lin_mul`: if every coefficient of g is a linear form in the t_l, the coefficient
of t^σ
in g·f is the sum over the different parts l of σ of the coefficient of t_l in g times the
coefficient of t^{σ − l} in f. It is applied to t_k, to J_n^+(v) and to the part of J_n^+(u) with l
≤ E.
Nothing here is a sentence of the paper. 

 ### The two families of variables 

### `sel_xi'`

 On the inner family, with the value 0 at the index 0. 

### `sel_xo'`

 On the outer family, with the value 0 at the index 0. 

### `xi_or_xo`

 Every variable belongs to the inner or to the outer family. 

### `map_sel`

 A map φ with φ 0 = 0 may be applied to the values. 

 ### Linear forms in the variables 

 ### Bilinear forms in the variables 

 ### The coefficient of t^σ in a series in v 

### `braH`

 `bra σ` as an additive map. 

### `coeff_mul_big`

 The coefficients of a product, as a sum over any two sets that contain the supports. 

### `bra_emb_mul`

 Series without the t_k may be taken out. 

### `eq_single_of_degree`

 An exponent of degree 1 is that of a variable. 

### `coeff_linear_mul`

 The coefficients of p·q for a linear form p in the t_l. 

### `Lin1`

 Every coefficient of g is a linear form in the t_l. 

### `bra_lin_mul`

 If every coefficient of g is a linear form in the t_l, the coefficient of t^σ in g·f is the sum
over the different parts l of σ of the coefficient of t_l in g times the coefficient of
t^{σ − l} in f. 

 ### The three linear forms: t_k, J_n^+(v), and the part of J_n^+(u) with l ≤ E 

### `degree_of_coeff_C_mul_X`

 c·t_k is a linear form. 

### `bra_tT_mul`

 The coefficient of t^σ in t_k·f. 

### `bet_eq_zero_of_lt`

 C(l−1, n−1) = 0 for l < n. 

### `coeff_smul_mo`

 q·u^x·v^y, coefficient by coefficient in v. 

### `bra_single_JpV`

 The coefficient of t_l in J_n^+(v) is C(l−1, n−1)·v^{l−n}. 

### `bra_JpV_mul`

 The coefficient of t^σ in J_n^+(v)·f. 

### `bra_single_JpU`

 The coefficient of t_l in the part of J_n^+(u) with l ≤ E is C(l−1, n−1)·u^{l−n} for l ≤ E. 

### `bra_prod_tT`

 The coefficient of t^σ in the monomial t^σ'. 

 ### The coefficient of t^σ in a power series in the x_n, x'_n 

### `braWH`

 `braW σ` as an additive map. 

### `braW_embW_mul`

 Power series without the t_k may be taken out. 

### `pderiv_braW`

 Taking the coefficient of t^σ commutes with ∂/∂x_i. 

### `braW_C_lin_mul`

 The rule `bra_lin_mul` for power series. 
