---
{
  "module": "ThreeSumApsp/Sec4/Corollary31.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec4/Corollary31.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec4/Corollary31.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Corollary 31: the costs of Theorem 30 as powers of `D`

"We repeat the proof of Corollary 26 with L := ⌈cm⌉ and t := ⌈θm⌉". Here `L` is `levelsOf c m` and
`t` is `switchOf θ m`, for constants `c > 10` and `0 < θ < 0.9`; the inner dimension satisfies
`2 ≤ D ≤ N^ε` with `ε < R_c(γ)`, and `m = ⌈log_4 D⌉`. The main result is `Corollary31.costs`: for
all `m` from some `m₀` on, the preprocessing cost (8) of Theorem 30 (`cost8`, the sum of a first
term for the boxes and a last term for the encodings) is `O(N² log² D / D^γ)`, and its query cost
`L ∑_{d ≤ t} α_d` (`costQuery`) is `O(D^q log D)`. What the paper says of the finitely many smaller
`m` is `Corollary31.small_m`; nothing else rests on that lemma.

The steps are those of the proof of Corollary 26. What does not depend on `c` and `θ` is proved
before, for both corollaries; the rest is what the paper says of each step.

* Setting up. As for Corollary 26, the inner dimension is padded to `D = 4^m`
  (`Corollary26.setting_up`, `Corollary26.padding`); this changes the bounds by a constant factor
  (`padded_le`). The hypothesis reads `N ≥ 4^{(m-1)/ε}` (`Corollary31.hypothesis`).
* Boxes. `ρ < ρ_c` and `ρ^t ≤ D^{-γ}` (`Corollary31.rho_lt`, `Corollary31.rho_pow_le`), which bounds
  the first term of (8) (`Corollary31.first_term`).
* Queries. The calculation of Corollary 26, `∑_{d ≤ t} α_d ≤ (9x)^t (1 + 1/x)^m` (`sum_alpha_le`),
  with `x = (1-θ)/θ` in place of 8 gives `O(D^q)` (`Corollary31.sum_alpha`) and so
  `Corollary31.query_cost`.
* Encodings. As for Corollary 26, inequality (10) (`eq_10`) bounds the last term of (8)
  (`Equation10.last_term`) and gives the hypothesis `N ≥ √K N₀` of Theorem 30
  (`Equation10.tile_fits`). Its left-hand side is `O(√m · Λ^m)` (`Corollary31.lhs10_le`), and the
  base `Λ` is smaller than the base `4^{1/ε}` (`eq_11_iff`). This `Λ` is the general form of the `Λ`
  of Corollary 26 (`exp_lnΛ`, `baseLambda_eq_exp_lnΛ`).

The last sentence of the corollary, on `R_c(0)`, is `sec4_Rc_strictAntiOn` and
`sec4_Rc_zero_tendsto`. Bounds "up to a constant" are written with `Dominated`, in the one parameter
`m` or in the record `Sizes` of the given `D`, of `N` and of `m`.


 ### Setting up 

### `Admissible`

 The hypotheses of Corollary 31 on its parameters: "Let c > 10 and 0 < θ < 0.9", and "ε <
R_c(γ)". 

### `Admissible.gamma_pos`

 The exponent `γ` of admissible parameters is positive. 

### `ten_mul_le_levelsOf`

 With "L := ⌈cm⌉" (proof of Corollary 31) the hypothesis `L ≥ 10m` of Theorem 30 holds. 

### `levelsOf_le`

 `L = ⌈cm⌉ ≤ (c + 1) m` for `m ≥ 1`. 

### `dominated_cast_log_D`

 `m = O(log D)` for `D = 4^m`. 

### `dominated_levelsOf_log_D`

 `L = ⌈cm⌉ = O(log D)` for `D = 4^m`. 

### `Corollary31.hypothesis`

 Proof of Corollary 31: "After the padding, the assumption D ≤ N^ε now reads N ≥ 4^{(m-1)/ε}",
because `4^{m-1} < D ≤ N^ε` for the original `D`. 

 ### Boxes 

### `Corollary31.rho_lt`

 Proof of Corollary 31: "ρ < ρ_c", where `ρ = 9m/(L-m+1)` and `L = ⌈cm⌉ ≥ cm`. 

### `Corollary31.rho_pow_le`

 Proof of Corollary 31: "ρ < ρ_c gives ρ^t ≤ ρ_c^{θm} = D^{-γ}". 

### `Corollary31.first_term`

 The step on the boxes for general `c` and `θ`: `1/(1-ρ) = O(1)` and `ρ^t ≤ D^{-γ}`, so the first
term of (8) is `O(L m D^{-γ} N²) = O(N² log² D / D^γ)`. (In the proof of Corollary 26: "Hence the
first term of (8) is O(m² N²/D^γ)".) The common factor `N²` is left out. 

 ### Queries 

### `Corollary31.sum_alpha`

 Proof of Corollary 31: "the same calculation with x := (1-θ)/θ in place of 8, where 9x > 1
because θ < 0.9, gives ∑_{d≤t} α_d ≤ (9x)^t (1+1/x)^m = O(D^q)". The constant is `9x`, because
`t = ⌈θm⌉ < θm + 1`. 

### `Corollary31.query_cost`

 The query cost `L ∑_{d ≤ t} α_d` of Theorem 30 is `O(L D^q) = O(D^q log D)`, for `D = 4^m`. (In
the proof of Corollary 26: "Hence a query takes O(L D^q) = O(m D^q) time".) 

 ### Encodings

As in the proof of Corollary 26, `m`-th powers are compared by comparing their bases. The paper's
sentences are one lemma each: the bound on the binomial coefficient (`Corollary31.le_K`, for which
`Corollary31.mul_entropy_monotoneOn` passes from `L` to `cm`), the bound `O(√m · Λ^m)` on the
left-hand side (`Corollary31.lhs10_le`), where `Λ` is `Real.exp (lnΛ c γ)` (`exp_lnΛ`), and
`Λ < 4^{1/ε}` (`eq_11_iff`); `eq_10` puts them together with `Corollary31.hypothesis`. Throughout,
`L = ⌈cm⌉`, and `D₀` is the inner dimension before padding. 

### `Corollary31.mul_entropy_monotoneOn`

 The function `x ↦ x H(m/x)` is increasing on `x ≥ m ≥ 1`. The entropy function is concave with
`H(0) = 0`, and `m/y` is the point `(x/y) (m/x) + (1 - x/y) 0`. 

### `Corollary31.le_K`

 Proof of Corollary 31: the bound on the binomial coefficient (`exp_entropy_div_le_choose`), for
`K = binom(L, m)`. It gives `K ≥ e^{L H(m/L)}/(L+1) ≥ e^{cm H(1/c)}/(cm+2)`, as `cm ≤ L < cm + 1`
and `x ↦ x H(m/x)` is increasing. 

### `le_sqrt_K`

 The bound on `K`, under the square root: `√K ≥ (e^{(1/2) c H(1/c)})^m / (√(c+2) √m)`. 

### `ten_pow_div_N0_le`

 `10^L / N₀ = (10/3)^L 3^m ≤ (10/3) (10^c 3^{-(c-1)})^m`, as `N₀ = 3^{L-m}` and `L < cm + 1`. 

### `exp_lnΛ`

 `Real.exp (lnΛ c γ)` is the `Λ` of Section 4.4: "Λ := 10^c e^{-(1/2) c H(1/c)} 3^{-(c-1)} 4^γ".


### `Corollary31.lhs10_le`

 Proof of Corollary 31: "the left-hand side of (10) is O(√m · Λ^m)", for `m ≥ 1`, with
`L = ⌈cm⌉`, `Λ = Real.exp (lnΛ c γ)` and any real `γ`. 

### `exists_mul_sqrt_le_pow`

 A power `r^m` with `r > 1` exceeds `A √m` "once m exceeds a constant". 

### `pos_of_le_rpow`

 `4^{m-1} < D₀ ≤ N^ε` is possible only for `ε > 0`, because `D₀ ≥ 2`. 

### `eq_10`

 Equation (10), `D^γ · 10^L / (√K N₀) ≤ N`, with the parameters of Corollary 31, whose proof
says: "the inequality (10) thus holds once m exceeds a constant depending on c, θ, and ε". Here `D₀`
is the original inner dimension, `m = ⌈log_4 D₀⌉` (that is, `4^{m-1} < D₀ ≤ 4^m`), the `D` of (10)
is the padded `4^m`, `L = ⌈cm⌉`, `γ = θ ln(1/ρ_c)/ln 4`, and `D₀ ≤ N^ε` with `ε < R_c(γ)`. The
threshold `m₀` depends only on `c`, `θ`, `ε`. No hypothesis `ε > 0` is needed: for `ε ≤ 0` no
natural number `N` satisfies `2 ≤ D₀ ≤ N^ε`. 

 ### The corollary 

### `dominated_cost8`

 The expression (8) is `O(N² log² D / D^γ)`, in the given `D`, wherever (10) holds: by the step
on the boxes and by (10) this is so for `D = 4^m`, and the padding only affects the constant. 

### `dominated_costQuery`

 The cost of a query is `O(D^q log D)`, in the given `D`. 

### `Sizes.Corollary31`

 The instances of Corollary 31 from a threshold `m₀` on: `2 ≤ D ≤ N^ε` and `m = ⌈log_4 D⌉ ≥ m₀`.


### `Corollary31.costs`

 Corollary 31, the cost bounds obtained from Theorem 30, for all large `m`. For `c > 10`,
`0 < θ < 0.9`, `ε < R_c(γ)` there are a constant `C` and a threshold `m₀`, depending only on `c`,
`θ`, `ε` ("The constants hidden in the O(·) depend on c, θ, and ε"), such that for all `2 ≤ D ≤ N^ε`
with `m = ⌈log_4 D⌉ ≥ m₀`, `L = ⌈cm⌉`, `t = ⌈θm⌉`: the hypothesis `N ≥ √K N₀` of Theorem 30 holds,
the expression (8) is at most `C N² log² D / D^γ`, and the query cost is at most `C D^q log D`, all
in terms of the original `D`. (The case `m < m₀` is `Corollary31.small_m`. No hypothesis `ε > 0` is
needed: for `ε ≤ 0` no natural number `N` satisfies `2 ≤ D₀ ≤ N^ε`.) 

### `Corollary31.small_m`

 Proof of Corollary 31: "for smaller m the corollary again holds trivially": `D` is bounded, and
a query can compute an inner product. For `D₀ ≤ 4^{m₀}` the `D₀` operations of an inner product are
at most `C D₀^q log D₀`, with a constant `C` that depends only on `q` and `m₀`. 
