---
{
  "module": "src/New/Reduction/Data/Sizes.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/Sizes.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/Sizes.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Sizes of the data

This file proves size estimates for admissible data `D : Data P`: for the scales, the ranks, the
field and the primes. The table recalls the main sizes, including those proved in the imported
files. Each quantity has bounds `exp l ≤ F` and `|F| ≤ exp l'` that instance search finds and
carries through sums, products and powers; `le_of_hasLogBound` proves `F ≤ G` by comparing the upper
exponent of `F` with the lower exponent of `G`, using the inequalities between the scales.

| quantity | size proved | degree in `x` |
|---|---|---|
| `s`, `l₀` | `s ≤ 32 log x`, `27 s < l₀ ≤ 81 s` | `0` |
| `log x₁`, `log b` | `(log x₁)⁶ ≤ log b`, `(log b)¹⁰⁰ ≤ x` | `≤ 1 / 100` |
| `m` | `[√x, 2 √x]` | `1 / 2` |
| `k`, `r`, `t` | `r` in `[x⁵, 3 x⁵]`, `k ≤ r ≤ 2 k`, `t = 5 r` | `5` |
| `n_m` | `k + m (t + 1)` | `11 / 2` |
| `2 ^ s`, `f`, `q₁` | `x¹¹ ≤ m ^ 22 = 2 ^ s ≤ f ≤ q₁ ≤ x¹²` | `11`; the upper bound is rounded up |
| `rootDisc`, `1 / Ω` | `[x¹⁰, x¹²]`, `[1, x¹³]` | `11`; the bounds are rounded |
| the gap `Δ = D.gap` | `2 r⁸` | `40` |
| `x₁` | `x ^ 10⁶ ≤ x₁` | at least `10⁶` |
| `b`, `a = x b`, the weights `κ` | `x₁ ^ 10⁶ ≤ b`, `a / x₁ ≤ κ ≤ b` | |
| `M = p₀ p₁` | `[b²⁰, b²²]` | |
| `N` | `log N` in `[m log b, 30 m log b]` | |

Notions from other files:
* `Data P`: admissible data over the parameters `P`; among its fields are the logarithms `logX`,
  `logX₁`, `logB` of the scales `x`, `x₁`, `b`, the numbers `m`, `r`, `towerExp` (the `s` of the
  table), the primes `levelPrime 0`, `levelPrime 1` and the level `N`.
* `D.E`: the CM field `K(ζ_{q₁})` over `K = ℚ(√-d)`, with `D.f` infinite places and root
  discriminant `rd_E = D.rootDisc`.
* `P.bigOmega s`: the real number `Ω = exp (γ - Re L'/L(1, χ_K)) · 2π / rd_E`.


 ### Scales and the exponent of the tower 

### `x_pow_le_x₁`

 The scales `x = exp logX` (the length of the prime sum) and `x₁ = exp logX₁` of admissible data
satisfy `x ^ 10⁶ ≤ x₁`. 

### `x₁_pow_le_b`

 The scales `x₁ = exp logX₁` and `b = exp logB` of admissible data satisfy `x₁ ^ 10⁶ ≤ b`. 

### `logX₁_pow_le_logB`

 The scales `x₁` and `b` of admissible data satisfy `(log x₁) ^ 6 ≤ log b`. 

### `logB_pow_le_x`

 The scales `x` and `b` of admissible data satisfy `(log b) ^ 100 ≤ x`. 

### `m_sq_mem_Icc`

 The number `m` of admissible data has the size of `√x`, for the scale `x = exp logX`:
`x ≤ m² ≤ 4 x`. 

### `towerExp_ne_zero`

 The exponent `s = D.towerExp` of the tower of admissible data `D`, for which `2 ^ s = m ^ 22`
with `m = D.m ≥ 2`, is not zero. 

### `x₁_pow_le_sqrt_b`

 The scales `x₁` and `b` of admissible data satisfy `x₁ ^ (3 l₀²) ≤ √b`, where `l₀` is the least
power of `3` above `27 s` and `s` is the exponent of the tower. 

 ### Ranks and invariants of the field

The numbers `m`, `k` are even and `r`, `t` are odd by the imported lemmas `m_even`, `k_even`,
`r_odd`, `t_odd`; hence every `n_j = k + j (t + 1)` is even (`New.Data.n_even`). 

### `r_le_two_mul_k`

 The numbers `r ≥ x⁵` and `m ≤ 2 √x` of admissible data satisfy `r ≤ 2 k` for
`k = r + 1 - m`. 

### `m_pow_eq_two_pow_towerExp`

 The rank `m = D.m` and the exponent `s = D.towerExp` of the field `E = P.E s` of the data `D`
satisfy `m ^ 22 = 2 ^ s`. 

### `m_pow_le_two_pow_l₀`

 The number `m` of successive theta lifts of admissible data, a power of `2`, satisfies
`m ^ 594 ≤ 2 ^ l₀`. Here `s = D.towerExp` is the exponent with `m ^ 22 = 2 ^ s`, and `l₀ = l₀ s` is
the least power of `3` above `27 s`. 

### `f_mem_Icc`

 The number `f` of infinite places of the field `E = K(ζ_{q₁})`, `K = ℚ(√-d)`, satisfies
`m ^ 22 ≤ f ≤ q₁`. Here `m` is the number of successive theta lifts, a power of `2` with
`m ^ 22 = 2 ^ s` for `s = D.towerExp`, and `q₁ = 3 l₀ 2 ^ s q₀` is the order of the root of unity,
with `l₀` the least power of `3` above `27 s` and `q₀` the fixed modulus of the parameters. 

### `f_even`

 The number `f` of infinite places of the field `E` of the data is even. 

### `q₁_le`

 The order `q₁` of the root of unity that generates `E` over `K` is at most `x¹²`, where `x` is
the scale `D.x` of the data. 

### `q₂_le`

 The modulus `q₂ s = (q₀ d) ^ (s + 6)` is at most `x ^ (33 q₀ d)`. Here `q₀`, a multiple of
`18480`, and the prime `d` with `K = ℚ(√-d)` are the fixed parameters, `s` is the exponent of the
tower and `x = exp logX` is the length of the prime sum. 

### `log_classNumber_le`

 The class number `h_E` of the CM field `E` of admissible data satisfies `log h_E ≤ x ^ 30`,
where `x = exp logX` is the length of the prime sum. 

 ### Weights

The bounds `a / x₁ ≤ κ ≤ b` and `κ + x⁴² ≤ 2 b` for the weight `κ = D.weight σ` are the imported
lemmas `weight_mem_Icc`, `weight_le_b` and `weight_add_x_pow_le_two_mul_b`; those for the sequence
`D.shiftedWeight` are `shiftedWeight_mem_Icc` and `log_shiftedWeight_le`. 

### `a_div_x₁_mem_Icc`

 With the scales `x = exp logX`, `x₁ = exp logX₁` and `b = exp logB` of admissible data and the
product `a = x b`, the quotient `a / x₁` satisfies `x ^ 999 ≤ a / x₁ ≤ b / x ^ 999`. 

 ### Primes, levels and the number `Ω`

The bound `b²⁰ ≤ M ≤ b²²` is `M_mem_Icc`; the range for the level is `logLevelTarget_mem_Icc`,
`log_N_mem_Icc_logLevelTarget` and `log_N_mem_Icc`. How the three primes split in `E` is in
`New.Parameters.star_mem_iff_notMem`, `New.Parameters.intValuation_eq_of_mul_star` and
`New.Data.q_eq_levelPrime`. 

### `levelPrime_mem_Ioo`

 Each of the two prime factors `p₀ = D.levelPrime 0`, `p₁ = D.levelPrime 1` of the number
`M = p₀ p₁` of admissible data exceeds `b²` and is smaller than the prime `N` (the level). 

### `bigOmega_le_one`

 For the exponent `s = D.towerExp` of admissible data, the real number
`Ω = P.bigOmega s = exp (γ - Re L'/L(1, χ_K)) · 2π / rd_E` is at most `1`. Here `γ` is Euler's
constant, `χ_K` the quadratic character of `K = ℚ(√-d)` and `rd_E` the root discriminant of the
field `E = P.E s`, a cyclotomic extension of `K`. 

### `log_M_div_bigOmega_mem_Icc`

 For admissible data `D` over the parameters `P`, `20 log b ≤ log (M / Ω) ≤ 23 log b`. 

### `abs_log_M_mul_rootDisc_le`

 For admissible data `D`, `|log (M rd_E / 2π)| ≤ 23 log b`. Here `b = exp D.logB` is the largest
scale, `M = p₀ p₁` is the product of the two distinct primes `pᵢ = D.levelPrime i`, which lie in
`[b¹⁰, b¹¹]`, and `rd_E = D.rootDisc` is the root discriminant of the CM field `E` of the data. 
