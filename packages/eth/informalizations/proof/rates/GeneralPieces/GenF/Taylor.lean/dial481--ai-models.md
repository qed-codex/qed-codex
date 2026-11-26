---
{
  "module": "proof/rates/GeneralPieces/GenF/Taylor.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/GenF/Taylor.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/GenF/Taylor.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The exponential of Σ_v x_v·O_v for operators O_v, and Taylor's formula

Let A be a commutative ℚ-algebra, X a set of variables and O_v (v ∈ X) ℚ-linear maps A → A. The
operator 𝒪 = Σ_v x_v·O_v acts on the power series in the variables X over A (`opX`): O_v is applied
to
every coefficient, and the result is multiplied by x_v. It raises the degree in the x_v by one, so
e^𝒪 = Σ_n 𝒪ⁿ/n! (`expOp`) is a finite sum in every coefficient. If the O_v are derivations, 𝒪 is a
derivation (`opX_mul`), so e^𝒪 is a ring homomorphism by Leibniz's rule (`expOp_mul`, `expOpHom`),
which commutes with the exponential of power series (`expOp_expW`). Taylor's formula, of the kind
used in the proof
of Lemma 9 (Appendix B): if 𝒪(𝒪 f) = 0, then e^𝒪 f = f + 𝒪 f (`expOp_of_sq_zero`); for e^{Σ x_i D_i}
with derivations D_i this is `expD_of_sq_zero`. 

 ### Series without monomials of low degree 

### `Low`

 f has no monomials of degree less than d. 

 ### The operator 𝒪 = Σ_v x_v·O_v 

### `mapE`

 A linear map applied to every coefficient. 

### `opX`

 𝒪 = Σ_v x_v·O_v: the coefficient of α in 𝒪 f is Σ_v O_v(the coefficient of α − e_v in f), over
the variables v that occur in α. 

### `Low.opX`

 𝒪 raises the degree by one. 

### `coeff_iterate_eq_zero`

 𝒪ⁿ f has no monomials of degree less than n. 

### `coeff_opX_eq`

 In the coefficient of α, 𝒪 is the finite sum Σ_{v ∈ s} x_v·O_v, for every finite set s that
contains the variables of α. 

 ### Derivations 

### `IsDer`

 The product rule. 

### `mapE_mul`

 A derivation applied to every coefficient is a derivation. 

### `opX_mul`

 𝒪 is a derivation if the O_v are. 

### `iterate_mul`

 Leibniz's rule for the n-th power of a derivation. 

### `iterate_mul_div`

 The same, divided by n!. 

 ### The exponential e^𝒪 

### `opN`

 Σ_{n < N} 𝒪ⁿ f/n!. 

### `expOp`

 e^𝒪 f = Σ_n 𝒪ⁿ f/n!: the coefficient of a monomial of degree d is taken from the sum over n ≤ d. 

### `coeff_expOp`

 More terms of the sum do not change the coefficient. 

### `expOp_mul`

 e^𝒪 is multiplicative if the O_v are derivations. 

### `expOp_of_sq_zero`

 If 𝒪(𝒪 f) = 0, then e^𝒪 f = f + 𝒪 f. 

### `expOp_of_zero`

 If 𝒪 f = 0, then e^𝒪 f = f. 

### `expOpHom`

 e^𝒪 as a ring homomorphism. 

### `coeff_expOp_congr`

 The coefficient of α in e^𝒪 f depends only on the coefficients of f at the monomials of degree
at most that of α. 

### `expOp_expW`

 e^𝒪 commutes with the exponential of power series. 

### `constantCoeff_expOp`

 e^𝒪 does not change the constant term. 

 ### The series Σ_v x_v·b_v 

### `lin`

 Σ_v x_v·b_v: the coefficient of x_v is b_v, all other coefficients are 0. 

 ### The same for derivations 

### `mapD`

 A derivation applied to every coefficient. 

### `dsum`

 Σ_i x_i·D_i. 

### `expD`

 e^{Σ_i x_i·D_i}, a ring homomorphism. 

### `expD_of_zero`

 e^{Σ x_i D_i} fixes the series on whose coefficients all D_i vanish. 

### `expD_of_sq_zero`

 Taylor's formula: e^{Σ x_i D_i} w = w + Σ_i x_i·D_i w, if all D_i D_j vanish on the coefficients
of w. 

### `expD_expW`

 e^{Σ x_i D_i} commutes with the exponential of power series. 
