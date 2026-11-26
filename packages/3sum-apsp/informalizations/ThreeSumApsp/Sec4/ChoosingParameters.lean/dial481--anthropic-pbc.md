---
{
  "module": "ThreeSumApsp/Sec4/ChoosingParameters.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec4/ChoosingParameters.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec4/ChoosingParameters.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# 4.4 Choosing the parameters: the entropy function, the exponents `γ` and `q`, equation (11)

Section 4.4 chooses the parameters `L` and `t` of Theorem 30. This file has the facts that its
proofs use about `D = 4^m` and about the notions with which Corollary 31 is stated ("Other choices
of the parameters"). The notation of the paper: `entropy` is `H`, `rhoC c` is `ρ_c = 9/(c-1)`,
`gammaOf c θ` is `γ = θ ln(1/ρ_c)/ln 4`, `qOf θ` is `q = (H(θ) + θ ln 9)/ln 4`, `lnΛ c γ` is the
denominator `ln Λ` of (11), `Rc c γ` is `R_c(γ) = ln 4/ln Λ`, and `D m` is `D = 4^m`.

* The entropy function `H` is Mathlib's `Real.binEntropy` (`entropy_eq_binEntropy`); continuity,
  concavity and the derivative come from there.
* Powers and logarithms of `D = 4^m` (`cast_D_pos`, `one_le_cast_D`, `log_cast_D`,
  `cast_le_log_cast_D`, `cast_D_rpow`).
* The bound `binom(n, k) ≥ e^{n H(k/n)}/(n+1)` (`exp_entropy_div_le_choose`): it is the standard
  bound `binom(n, k) ≥ 1/(n+1) · n^n/(k^k (n-k)^{n-k})`, as `e^{n H(k/n)} = n^n/(k^k (n-k)^{n-k})`.
* One section for each of `ρ_c`, `γ`, `q`, and `ln Λ` with `R_c(γ)`: signs, monotonicity and
  continuity, and the three facts that tie them to the costs: `ρ_c^{θm} = D^{-γ}`
  (`rhoC_rpow_eq_D_rpow`), `e^{m(H(θ) + θ ln 9)} = D^q` (`exp_entropy_eq_D_rpow_qOf`), and
  `Λ < 4^{1/ε}` if and only if `ε < R_c(γ)` (`eq_11_iff`).


 ### The entropy function: the link with Mathlib's `Real.binEntropy` 

### `entropy_eq_binEntropy`

 The entropy function of Section 4.4 is Mathlib's binary entropy function. 

### `entropy_continuous`

 The entropy function is continuous on the whole real line. 

### `entropy_nonneg`

 `H(x) ≥ 0` for `0 ≤ x ≤ 1`. 

### `entropy_le_log_two`

 `H(x) ≤ ln 2`. 

### `entropy_zero`

 `H(0) = 0`. 

### `entropy_concaveOn`

 The entropy function is concave on `[0, 1]`. 

### `hasDerivAt_entropy`

 The derivative of the entropy function, `H'(x) = ln((1-x)/x)` for `0 < x < 1`. 

 ### Powers and logarithms of `D = 4^m` 

### `log_four_pos`

 `ln 4 > 0`. 

### `cast_D_eq`

 `D = 4^m` as a real number. 

### `cast_D_pos`

 `D > 0`. 

### `one_le_cast_D`

 `D ≥ 1`. 

### `log_cast_D`

 `ln D = m ln 4`. 

### `cast_le_log_cast_D`

 `m ≤ ln D`. 

### `cast_D_rpow`

 `D^x = e^{x m ln 4}`. 

 ### The lower bound on binomial coefficients by the entropy function 

### `pow_eq_exp_mul_log`

 `x^j = e^{j ln x}` for `x ≥ 0`, provided that `x = 0` forces `j = 0`. 

### `exp_entropy_eq`

 `e^{b H(a/b)} = 1 / (p^a (1-p)^{b-a})` with `p = a/b`. 

### `exp_entropy_div_le_choose`

 Proof of Corollary 31: "the same bound on the binomial coefficient, binom(n, k) ≥ e^{n
H(k/n)}/(n+1)", for `k ≤ n`. 

 ### The decay rate `ρ_c` 

### `rhoC_pos`

 `ρ_c = 9/(c-1) > 0` for `c > 10`. 

### `rhoC_lt_one`

 `ρ_c = 9/(c-1) < 1` for `c > 10`. 

### `one_div_rhoC`

 `1/ρ_c = (c - 1)/9`. 

### `log_inv_rhoC_pos`

 `ln(1/ρ_c) = ln((c - 1)/9)` is positive for `c > 10`. 

### `log_inv_rhoC_lt`

 `ln(1/ρ_c)` increases with `c`. 

 ### The exponent `γ` 

### `gammaOf_eq_mul`

 `γ` is proportional to `θ`. 

### `corollary_31_gamma_pos`

 Corollary 31: "γ := θ ln(1/ρ_c)/ln 4 > 0". 

### `gammaOf_strictMono`

 `γ` increases with `θ` (for fixed `c > 10`). 

### `gammaOf_lt_gammaOf`

 At a fixed `θ > 0`, `γ` increases with the ratio `c > 10`, because `1/ρ_c = (c - 1)/9`. 

### `rhoC_rpow_eq_D_rpow`

 Proof of Corollary 31: "ρ_c^{θm} = D^{-γ}", with `D = 4^m` and `γ = θ ln(1/ρ_c)/ln 4`. 

 ### The exponent `q` 

### `continuous_qOf`

 `q` is a continuous function of `θ`. 

### `qOf_strictMonoOn`

 The exponent `q` is strictly increasing in `θ` on `[0, 0.9]`: the derivative of `H(θ) + θ ln 9`
is `ln(9(1-θ)/θ)`, which is positive for `0 < θ < 0.9`. 

### `qOf_nonneg`

 The exponent `q` is not negative for `0 < θ < 0.9`. 

### `qOf_zero`

 `q` increases with `θ` from 0 to `log_4 10` on `(0, 0.9)`: the value at `θ = 0`. That `q`
increases is `qOf_strictMonoOn`. 

### `qOf_nine_tenths`

 `q` increases with `θ` from 0 to `log_4 10` on `(0, 0.9)`: the value at `θ = 0.9`. Indeed
`H(0.9) + 0.9 ln 9 = ln 10`, because `ln 0.9 = ln 9 - ln 10` and `ln 0.1 = -ln 10`. 

### `continuous_gammaOf_add_qOf`

 The sum `γ + q`, which is `κ` at the `θ` of an entry of the right half of Table 2, is continuous
in `θ`. 

### `exp_entropy_eq_D_rpow_qOf`

 `e^{m(H(θ) + θ ln 9)} = D^q` with `D = 4^m` and `q = (H(θ) + θ ln 9)/ln 4`. 

 ### The denominator `ln Λ` of equation (11), and `R_c(γ)` 

### `lnΛ_eq_add`

 `ln Λ` depends on `γ` through the summand `γ ln 4` only. 

### `lnΛ_pos`

 The denominator `ln Λ` of (11) is positive for `c ≥ 10` and `γ ≥ 0`. (Implicit in the paper,
which divides by it. Here it follows from `H ≤ ln 2` and `ln 10 = ln 2 + ln 5`.) 

### `eq_11_iff`

 Equation (11) defines `R_c(γ) := ln 4/ln Λ` (the definition `Rc`, where `lnΛ c γ` is `ln Λ`).
The proof of Corollary 31 uses it in this form: "ε < R_c(γ) says that Λ < 4^{1/ε}".  Here `c ≥ 10`,
`γ ≥ 0`, and `ε > 0`, which the hypothesis 2 ≤ D ≤ N^ε of the corollary implies; for `ε ≤ 0`,
ε < R_c(γ) holds and Λ < 4^{1/ε} does not. 

### `Rc_continuousOn`

 `R_c(γ)` is continuous in `γ`, which the proof of Theorem 24 uses ("as θ → 0, the first
expression tends to 0 and the second to R_c(0)"). 

### `Rc_strictAntiOn_right`

 `R_c(γ)` decreases as `γ` increases; so in "The ε of a row of the table is the smallest R_c(γ)
over its entries" (Section 4.4) the smallest is at the largest `γ` of the row. 
