---
{
  "module": "ThreeSumApsp/Sec2/Lemma9.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec2/Lemma9.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec2/Lemma9.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Lemma 9: one run of `Full` computes all the products `X_Q Y_Q`

Section 2.3.3. The inner set of a string is the set of the levels at which it has
an inner variable (`p`, `q` or `z₀`). For a set `Q` of `m` levels, the left strings with inner set
`Q` index the entries of an `N₀ × D` matrix `X_Q`, the right strings those of a `D × N₀` matrix
`Y_Q`, and the output strings those of the product `X_Q Y_Q`. The arrays `a` and `b` hold all the
`X_Q` and all the `Y_Q` side by side. Lemma 9 says that `Mult(a, b)[w] = (X_Q Y_Q)[w]` for every
output string `w` with such an inner set.

* The strings with inner set `Q` are `leftStrOf Q hQ r π`, `rightStrOf Q hQ π c` and
  `outStrOf Q hQ r c` (`existsUnique_leftStr`, `existsUnique_rightStr`, `existsUnique_outStr`). At
  the first two the arrays hold `X_Q[r, π]` and `Y_Q[π, c]` (`arrayL_leftStrOf`,
  `arrayR_rightStrOf`).
* The two facts about `γ` that the proof needs are finite checks on the definition of `gamma`
  (`gamma_z0`, `gamma_x_y_z`); no other lemma is used for them.
* The proof of Lemma 9. By Lemma 8 the entry at `w` is a sum over all pairs `(u, v)`. In a summand
  that is not zero, `u` has inner set `Q`, the row of `w` as its outer part and some inner part `π`,
  and `v` has inner set `Q`, the column of `w` as its outer part and the same inner part
  (`exists_of_summand_ne_zero`). Each of these summands has coefficient 1 (`prod_gamma_eq_one`).
  Their sum is the entry of the matrix product (`Mult_arrays_eq_mul`, `lemma_9`).


 ### The sizes of the matrices, and Figure 4 

### `card_outerStr`

 Section 2.3.3: there are `N₀` strings of `L - m` outer left (or right) variables. 

### `card_innerStr`

 Section 2.3.3: there are `D` strings of `m` inner left (or right) variables. 

### `card_subsets_eq_K`

 Section 2.3.3: there are `K = binom(L, m)` subsets `Q` of `{1, …, L}` of size `m`. 

### `figure_4`

 Figure 4, for `L = 6` and `m = 2`.  This docstring counts levels and indices from 1,
as the paper does; the Lean text counts them from 0, so that the inner set {2, 5} is `{1, 4}` and x₁
is `.x 0`.  The strings `u = x₁ p₁₁ x₂ x₃ p₂₂ x₁`, `v = y₃ q₁₁ y₁ y₃ q₂₂ y₂` and
`w = z₁₃ z₀ z₂₁ z₃₃ z₀ z₁₂` have the inner set `{2, 5}`; `u` has the outer part `x₁x₂x₃x₁` and the
inner part `p₁₁p₂₂`; `v` has the inner part `q₁₁q₂₂` and the outer part `y₃y₁y₃y₂`; `w` has the row
`x₁x₂x₃x₁` and the column `y₃y₁y₃y₂`.  The sizes `81 × 16`, `16 × 81` and `81 × 81` of the matrices
and the number `binom(6, 2) = 15` of products, which the figure also shows, are not stated here. 

 ### The input arrays 

### `arrayL_leftStrOf`

 The entry of the left input array at the string with inner set `Q`, outer part `r` and inner
part `π` is `X_Q[r, π]`. 

### `arrayR_rightStrOf`

 The entry of the right input array at the string with inner set `Q`, inner part `π` and outer
part `c` is `Y_Q[π, c]`. 

 ### The proof of Lemma 9 

### `gamma_z0`

 In the proof of Lemma 9: "the only monomials of G + E that contain z₀ are the p_ij q_ij
z₀, with coefficient 1." Stated for `γ(s, t, z₀)`, which is the coefficient of `s t z₀` in `G + E`
by `gamma_eq_coeff`. 

### `gamma_x_y_z`

 In the proof of Lemma 9: "The only monomial of G + E that contains z_ij and no inner
variable is x_i y_j z_ij, with coefficient 1". Stated for `γ(x_i', y_j', z_ij)`, which is the
coefficient of `x_i' y_j' z_ij` in `G + E` by `gamma_eq_coeff`. 

### `eq_x_y_of_gamma_ne_zero`

 The statement on `γ(x_i', y_j', z_ij)` as it is used: if `s` and `t` are outer and
`γ(s, t, z_ij) ≠ 0`, then `(s, t) = (x_i, y_j)`. 

### `exists_of_summand_ne_zero`

 The summands of Lemma 8 that can be nonzero. Let `w` be the output string with inner
set `Q`, row `r` and column `c`. If `γ(u_ℓ, v_ℓ, w_ℓ) ≠ 0` at every level and the inner sets of `u`
and `v` have `m` elements, then `u` has inner set `Q`, outer part `r` and some inner part `π`, and
`v` has inner set `Q`, outer part `c` and the inner part with the same indices. 

### `prod_gamma_eq_one`

 In the proof of Lemma 9: the coefficient of the summand of `π` "is 1". 

### `Mult_arrays_eq_mul`

 Lemma 9 for the output string with inner set `Q`, row `r` and column `c`: by Lemma 8 the entry
is a sum over all pairs `(u, v)`, and the summands that remain are those of the matrix product. 

### `lemma_9`

 **Lemma 9**.  "For the input arrays a, b above and every output string w whose inner
set Q has exactly m elements, Mult(a, b)[w] = (X_Q Y_Q)[w]."  (Equation (4).) 

### `Full_arrays_eq_mul`

 Section 2.3.3: "one run of Full […] computes all K of the products X_Q Y_Q." 
