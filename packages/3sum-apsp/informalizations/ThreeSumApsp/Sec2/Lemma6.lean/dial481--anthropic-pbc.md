---
{
  "module": "ThreeSumApsp/Sec2/Lemma6.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec2/Lemma6.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec2/Lemma6.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Lemma 6: Schönhage's identity

Sections 2.1 and 2.2. After Strassen's identity (equation (1)), which the paper
recalls, this file treats Schönhage's. It has ten terms `λ`, each the product of a linear form `φ_λ`
in the seven left variables, a linear form `ψ_λ` in the seven right variables and a linear form
`χ_λ` in the ten output variables. Lemma 6 says that `∑_λ φ_λ ψ_λ χ_λ = G + E`, an identity of
polynomials in the 24 variables: `G` holds the outer product and the inner product that are wanted,
and `E` is an error.

* A linear form is the vector of its coefficients. `formL`, `formR` and `formO` turn it into a
  polynomial, and they are linear (`formL_eq_linearCombination` and its two companions).
* The proof of `lemma_6` is the paper's. The coefficient of `z_ij` comes only from the term `P_ij`.
  In the coefficient of `z₀` the products `x_i y_j` cancel, the cross terms vanish because the
  columns of `p̂` and the rows of `q̂` sum to zero (`pHat_column_sum`, `qHat_row_sum`), and what
  remains is the inner product (`sum_pHat_mul_qHat`).
* Second observation after the lemma: every term contributes to `z₀`, and only `P_ij` contributes to
  `z_ij` (`Term.contributes_z0`, `Term.contributes_z_iff`).

The later files on Section 2 use the second observation and the coefficients of the forms; none of
their proofs uses `lemma_6`.


### `eq_1`

 Equation (1) and the display after it: Strassen's seven products give the product of
two 2 × 2 matrices.  The entries may be blocks, so they are taken in a ring that need not be
commutative. 

 ### The alphabets 

### `LeftVar.equiv`

 The left variables, listed: `x i` is `.inl i`, and `p i j` is `.inr (i, j)`. 

### `RightVar.equiv`

 The right variables, listed: `y j` is `.inl j`, and `q i j` is `.inr (i, j)`. 

### `Term.equiv`

 The terms, listed: `P i j` is `some (i, j)`, and `P0` is `none`. 

### `card_leftVar`

 Section 2.2: there are "seven left variables". 

### `card_rightVar`

 Section 2.2: there are "seven right variables". 

### `card_term`

 Section 2.2: "Schönhage's identity has ten terms". 

### `sum_term`

 A sum over the ten terms, split into the `P_ij` and `P₀`. 

 ### Linear forms as polynomials 

### `formL_eq_linearCombination`

 `formL` is the linear map that sends the form consisting of the single variable `s` to the
polynomial `s`. 

### `formR_eq_linearCombination`

 `formR` is the linear map that sends the form consisting of the single variable `t` to the
polynomial `t`. 

### `formO_eq_linearCombination`

 `formO` is the linear map that sends the form consisting of the single variable `z` to the
polynomial `z`. 

### `formL_single`

 The form consisting of a single left variable is that variable. 

### `formR_single`

 The form consisting of a single right variable is that variable. 

### `formO_single`

 The form consisting of a single output variable is that variable. 

### `formL_phi_P`

 Section 2.2, the display of the linear forms: `φ_{P_ij} = x_i + p̂_ij`. 

### `formR_psi_P`

 Section 2.2, the display of the linear forms: `ψ_{P_ij} = y_j + q̂_ij`. 

### `formO_chi_P`

 Section 2.2, the display of the linear forms: `χ_{P_ij} = z_ij + z₀`. 

### `formL_phi_P0`

 Section 2.2, the display of the linear forms: `φ_{P₀} = -(x₁ + x₂ + x₃)`. 

### `formR_psi_P0`

 Section 2.2, the display of the linear forms: `ψ_{P₀} = y₁ + y₂ + y₃`. 

### `formO_chi_P0`

 Section 2.2, the display of the linear forms: `χ_{P₀} = z₀`. 

 ### Lemma 6 

### `pHat_column_sum`

 Section 2.2: "every column of p̂ […] sums to zero". 

### `qHat_row_sum`

 Section 2.2: "every row of q̂ sums to zero". 

### `sum_pHat_mul_qHat`

 Section 2.2: "Notice that ∑_{i,j=1}^{3} p̂_ij q̂_ij = ∑_{i,j=1}^{2} p_ij q_ij is the desired
inner product." 

### `lemma_6`

 **Lemma 6**.  "Summing over the ten terms, ∑_λ φ_λ ψ_λ χ_λ = G + E, where E :=
∑_{i,j=1}^{3} (x_i q̂_ij + p̂_ij y_j + p̂_ij q̂_ij) z_ij."  An identity of polynomials with integer
coefficients in the 24 variables. 

 ### Which terms contribute to which output variables 

### `Term.contributes_z0`

 Section 2.2, second observation: "every term contributes to z₀". 

### `Term.contributes_z_iff`

 Section 2.2, second observation: "only P_ij contributes to z_ij". 

### `Term.contributes_iff`

 The second observation in one statement: a term contributes to `z` if and only if `z` is inner,
that is `z₀`, or the term is `z.privateTerm`, which is `P_ij` for `z = z_ij`. (This is the term that
the private leaf of Section 2.4.3 has at a level with the variable `z`.) 

### `Term.sum_contributes`

 A sum over the terms contributing to `z` has the one summand `P_ij` for `z = z_ij`, and runs
over all terms for `z = z₀`. This is how step (4) of the recursions assembles the slice at `z`. 

### `chi_eq_ite`

 Section 2.2: "the χ_λ forms are all sums of output variables (without any minus signs or other
coefficients)". 
