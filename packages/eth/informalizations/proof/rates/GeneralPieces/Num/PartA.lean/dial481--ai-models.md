---
{
  "module": "proof/rates/GeneralPieces/Num/PartA.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Num/PartA.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Num/PartA.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Part (a) of Theorem A, along its proof in Appendix A

The proof is followed sentence by sentence, in the order of the text: the recursion for x_ℓ = log
K_ℓ and the closed formula; x_ℓ ≥ 2^ℓ·x₀ ≥ max(ℓ, x₀) and x_{ℓ+1} ≤ 10·x_ℓ;
e_ℓ ≥ ρ^ℓ/2; the recursion for y_ℓ = e_ℓ·ρ^{−ℓ}; K_ℓ ≥ 2^{18(ℓ+1)}; the bound on y_ℓ by an
exponential times a sum, and its value below 0.85; ρ^ℓ = (2^ℓ)^{−α'} and 2^ℓ ≥ x_ℓ/(3x₀+6).
`thmRunningTime_a` collects the four assertions of part (a). Only the definition of x_ℓ by its
recursion and K_ℓ = 2^{x_ℓ} in three forms (`K_eq`, `K_cast`, `logb_K`) are taken from the imported
module `ClauseBound.Gen.PartA`. 

 ## The numbers x_ℓ 

### `logK_eq_x`

 «The numbers x_ℓ = log K_ℓ»: the logarithm of K_ℓ to base 2 is the natural number x_ℓ. 

### `x_succ`

 «… satisfy x_{ℓ+1} = 2x_ℓ + 6ℓ + 2x₀». 

### `x_formula`

 «… which gives the formula by induction»: x_ℓ = (3x₀+6)·2^ℓ − 6ℓ − 2x₀ − 6. 

### `logK_formula`

 The first assertion of part (a): log K_ℓ = (3x₀+6)·2^ℓ − 6ℓ − 2x₀ − 6. 

### `x_ge_pow`

 «x_ℓ ≥ 2^ℓ·x₀». 

### `pow_ge_max`

 «2^ℓ·x₀ ≥ max{ℓ, x₀}». 

### `x_succ_le`

 «… we get x_{ℓ+1} ≤ 10·x_ℓ». 

### `x_lt_succ`

 x_ℓ < x_{ℓ+1}, from the recursion. 

### `K_lt_le`

 The second assertion of part (a): K_ℓ < K_{ℓ+1} ≤ K_ℓ^10. 

 ## The numbers e_ℓ 

### `e_ge_half_pow`

 «Clearly e_ℓ ≥ ρ^ℓ/2»: e₀ = 1/2, and e_{ℓ+1} ≥ ρ·e_ℓ, because the other two terms of the
recursion are not negative. 

### `y`

 y_ℓ = e_ℓ·ρ^{−ℓ}. 

### `y_zero`

 y₀ = 1/2. 

### `y_succ_le`

 «By ρ ≥ 1/2, the numbers y_ℓ = e_ℓ·ρ^{−ℓ} satisfy y_{ℓ+1} ≤ (1 + 2^{−ℓ−2})·y_ℓ + 6·2^ℓ/K_ℓ.» 

### `K_ge_pow`

 «… and K_ℓ ≥ 2^{18(ℓ+1)}», because x_ℓ ≥ 2^ℓ·x₀ ≥ (ℓ+1)·18. 

### `y_succ_le'`

 The two together: y_{ℓ+1} ≤ (1 + 2^{−ℓ−2})·y_ℓ + 6·2^{ℓ−18(ℓ+1)}. 

### `le_exp_sum_mul`

 The step that the text leaves to the reader: if u_{ℓ+1} ≤ (1 + a_ℓ)·u_ℓ + b_ℓ with a_ℓ, b_ℓ, u₀
≥ 0, then u_ℓ ≤ exp(Σ_{j<ℓ} a_j)·(u₀ + Σ_{j<ℓ} b_j), because 1 + a ≤ exp a. 

### `hasSum_a`

 Σ_{j≥0} 2^{−j−2} = 1/2. 

### `hasSum_b`

 Σ_{j≥0} 6·2^{j−18(j+1)} = 6·2^{−18}/(1 − 2^{−17}). 

### `y_le_exp_tsum`

 «So y_ℓ ≤ exp(Σ_{j≥0} 2^{−j−2})·(1/2 + Σ_{j≥0} 6·2^{j−18(j+1)})». 

### `exp_tsum_le`

 «… ≤ e^{1/2}·0.51». 

### `exp_half_mul_lt`

 «… < 0.85». 

### `y_lt`

 y_ℓ < 0.85. 

### `e_le_of_y`

 e_ℓ ≤ 0.85·ρ^ℓ, from y_ℓ < 0.85. 

 ## ρ^ℓ against log K_ℓ 

### `rho_pow_eq`

 «Finally ρ^ℓ = (2^ℓ)^{−α'}», where α' = log(1/ρ). 

### `two_pow_ge`

 «… and 2^ℓ ≥ x_ℓ/(3x₀+6).» 

### `rho_pow_le`

 The last assertion of part (a): ρ^ℓ ≤ ((3x₀+6)/log K_ℓ)^{α'}. 

 ## Part (a) 

### `TheoremAa`

 The four assertions of part (a) of Theorem A, for one ρ and one x₀. 

### `TheoremAa.logK`

 log K_ℓ = (3x₀+6)·2^ℓ − 6ℓ − 2x₀ − 6 

### `TheoremAa.K_lt_le`

 so K_ℓ < K_{ℓ+1} ≤ K_ℓ^10 

### `TheoremAa.e_bounds`

 ρ^ℓ/2 ≤ e_ℓ ≤ 0.85·ρ^ℓ 

### `TheoremAa.rho_pow`

 where ρ^ℓ ≤ ((3x₀+6)/log K_ℓ)^{α'}, α' = log(1/ρ) 

### `thmRunningTime_a`

 Part (a) of Theorem A, for 1/2 ≤ ρ < 1 and every x₀ ≥ 18. It does not need pieces, nor 2^x₀ ≥ c + 5. 
