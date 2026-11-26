---
{
  "module": "src/New/Reduction/Data/AdmissibleData.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/AdmissibleData.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/AdmissibleData.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Admissible data

Fix parameters `P : New.Parameters`. The data `D : New.Data P` are the objects that grow with the
length `x` of the prime sum: scales, ranks, the field `E`, the `a`-places and `b`-places, weights,
three primes, and numbers read off from them.

Letters used in comments, and the names in the code:

| letter | code |
|---|---|
| `p₀`, `p₁` | `D.levelPrime 0`, `D.levelPrime 1` |
| `π_M`, `π_N` | `star D.piMBar`, `D.piN` |
| `κ(τ)`, `κ_j(τ)` | `D.weight τ`, `D.liftWeight j τ` |
| `s`, `Δ` | `D.towerExp`, `D.gap` |
| `s_∞`, `s_fin` | `D.jetSize`, `D.primeSum` |

## Main definitions and results

* `New.Data`: the data; `New.Parameters.IsSparse` is the condition on the `b`-places. The scales and
  ranks are asked to lie in ranges only. The data with the exact values are
  `New.Parameters.IsAdmissibleData`; they are admissible for large `x`
  (`New.eventually_exists_data_of_isAdmissibleData`). Sizes are compared in the files `Magnitudes`
  and `Sizes` of this folder.
* `New.Parameters.logLevelMin_mem_Icc`: the lower end `N₋` of the range for the level has logarithm
  between `m log b` and `24 m log b`.

Notions from other files:
* `New.Parameters`: a multiple `q₀` of `18480 = 16 · 3 · 5 · 7 · 11` and a prime `d` with
  `d ≡ q₀/2 - 1 mod q₀`; they determine the field `P.K = ℚ(√-d)`.
* `New.towerDeg s`: the number `3 l₀ 2 ^ s`, where `l₀ = New.l₀ s` is, for `s ≥ 1`, the least power
  of `3` above `27 s`. The modulus `P.q₁ s` is `q₀ * towerDeg s`.
* `P.E s`, `P.Φ s`: the field `E = K(ζ)`, with `ζ` a primitive `q₁`-th root of unity, and its
  infinite places, which form a group isomorphic to `(ℤ/q₁)ˣ`.
* `P.q₂ s`: the number `(q₀ d) ^ (s + 6)`.


### `New.Parameters.constantBound`

 A bound for the constants that depend on `q₀` and `d` only. It is the sum of the constant
`P.vacuumBoundConst` in the bound for the conjugates of the integral vacuum, `2 d + 6`, `q₀`, the
absolute value of `chowlaSelbergConst d = γ - Re L'/L(1, χ_K)`, and `∑_w |log ‖Φ'(w)‖|`, where `w`
runs over the complex roots of the cyclotomic polynomial `Φ` of order `q₀`. 

### `New.Parameters.IsSparse`

 A set `T` of infinite places of `P.E s`, viewed in `(ℤ/q₁)ˣ` with `q₁ = P.q₁ s`, is sparse for
the primes up to `L` if for all primes `ℓ ≤ L` and integers `0 < i < j < l₀ s` there are no places
`σ, τ, ρ` in `T`, distinct or not, with `τ / σ ≡ ± ℓ ^ i` and `ρ / σ ≡ ± ℓ ^ j` modulo the part of
`q₁` prime to `ℓ`. The two signs are independent. 

### `New.Parameters.logLevelMin`

 The logarithm of `N₋ = κ̄ ^ m (M rd_E / 2π) ^ (m - 1) b ^ (-15 / 2)`, the lower end of the
range for the level. Here `κ̄` is the geometric mean of the weights `κ τ` over the infinite
places `τ` of `E = P.E s`, `rd_E` is the root discriminant of `E`, and `logB = log b`. 

### `New.Data`

 The data for the parameters `P`: scales `x`, `x₁`, `b`, the number `m` of lifts, the rank `r`,
the exponent `s` of the field `E = P.E s`, a sparse set of `b`-places with the weights that it
determines, and primes `p₀`, `p₁`, `N` with integers of `K` and of `E` whose products with their
conjugates are `p₀ p₁` and `N`. The scales, `m` and `r` are not fixed: they lie in ranges, `m` and
`r` are powers of `2` and `3`, and `q₁ x₁` divides `b`. `New.eventually_exists_data` constructs data
with explicit `x₁`, `b`, `m`, `r` for every large integer `x`. 

### `New.Data.natX`

 The length `x` of the prime sum, an integer. 

### `New.Data.natX₁`

 The second cut-off `x₁`, an integer. 

### `New.Data.natB`

 The weight `b` at the `b`-places, an integer. 

### `New.Data.logX`

 The logarithm of `x`. 

### `New.Data.logX₁`

 The logarithm of `x₁`. 

### `New.Data.logB`

 The logarithm of `b`. 

### `New.Data.exp_logX`

 `logX = log x`. 

### `New.Data.exp_logX₁`

 `logX₁ = log x₁`. 

### `New.Data.exp_logB`

 `logB = log b`. 

### `New.Data.constantBound_le`

 `log log b ≥ 10¹² c`, where `c = P.constantBound` bounds the constants that depend on `P`
  only. 

### `New.Data.mul_log_logB_le_logX`

 `(log b) ^ 100 ≤ x`. 

### `New.Data.logX_le_logX₁`

 `x ^ 10⁶ ≤ x₁`. 

### `New.Data.logX₁_le_logB`

 `x₁ ^ 10⁶ ≤ b`. 

### `New.Data.log_logX₁_le_log_logB`

 `(log x₁) ^ 6 ≤ log b`. 

### `New.Data.m`

 The number `m` of lifts in the chain. 

### `New.Data.r`

 The rank `r` of the target, that is, of the hermitian spaces `New.Data.spaceW` over `E`. 

### `New.Data.towerExp`

 The exponent `s` with `2 ^ s = m ^ 22`; the field is `P.E s`. 

### `New.Data.m_mem`

 `m` lies in `[√x, 2 √x]`. 

### `New.Data.r_mem`

 `r` lies in `[x⁵, 3 x⁵]`. 

### `New.Data.exists_m_eq_two_pow`

 `m` is a power of `2` with positive exponent, and `2 ^ s = m ^ 22`. 

### `New.Data.exists_r_eq_three_pow`

 `r` is a power of `3` with positive exponent. 

### `New.Data.towerExp_le`

 `s ≤ 32 log x`. 

### `New.Data.dvd_natB`

 `b` is a multiple of `q₁ x₁`. 

### `New.Data.bPlaces`

 The set `Φ_b` of `b`-places. 

### `New.Data.placeClass_of_mem_bPlaces`

 The `b`-places are `≡ -1` modulo `q₀`. 

### `New.Data.towerDeg_le_card_bPlaces_mul`

 There are at least `towerDeg s / log b` of them; `towerDeg s` is the number of places `≡ 1`
  modulo `q₀`. 

### `New.Data.sparse`

 The `b`-places are sparse for the primes up to `k t`, where `k = r + 1 - m` and `t = 5 r`. 

### `New.Data.weight`

 The weight `κ(τ)` of a place. 

### `New.Data.weight_eq`

 The weight is `b = a / x` at the `b`-places and `a / x₁` elsewhere, where `a = x b`. 

### `New.Data.levelPrime`

 The two primes `p₀`, `p₁` of the principal level. 

### `New.Data.levelPrime_prime`

 `p₀` and `p₁` are prime. 

### `New.Data.levelPrime_modEq_one_q₂_sq`

 `p₀, p₁ ≡ 1` modulo `q₂²`, with `q₂ = P.q₂ s`. 

### `New.Data.levelPrime_injective`

 `p₀ ≠ p₁`. 

### `New.Data.levelPrime_mem`

 `p₀` and `p₁` lie in `[b¹⁰, b¹¹]`. 

### `New.Data.piMBar`

 An integer of `K` of norm `M = p₀ p₁`; its conjugate is written `π_M`. 

### `New.Data.piMBar_mul_star`

 `piMBar` times its conjugate is `p₀ p₁`. 

### `New.Data.N`

 The level `N`. 

### `New.Data.N_prime`

 `N` is prime. 

### `New.Data.N_modEq_one_q₂_sq`

 `N ≡ 1` modulo `q₂²`. 

### `New.Data.log_N_mem`

 `log N₋ ≤ log N ≤ log N₋ + √(log b)`, with `N₋` as in `New.Parameters.logLevelMin`. 

### `New.Data.piN`

 An integer `π_N` of `E` whose product with its complex conjugate is `N`. 

### `New.Data.piN_mul_star`

 `π_N` times its conjugate is `N`. 

### `x`

 The length `x` of the prime sum, as a real number. 

### `x₁`

 The second cut-off `x₁`, as a real number. 

### `b`

 The weight `b` at the `b`-places, as a real number. 

### `E`

 The field `E = K(ζ)`, with `ζ` a primitive root of unity of order `q₁`. 

### `Φ`

 The infinite places of `E`; they form the group `Gal(E/K) = (ℤ/q₁)ˣ`. 

### `q₁`

 The order `q₁ = 3 l₀ m ^ 22 q₀` of the root of unity that generates `E` over `K`; here
`l₀ = New.l₀ D.towerExp` and `m ^ 22 = 2 ^ D.towerExp`. 

### `f`

 The number `f` of infinite places of `E`. 

### `cyclotomicConductor`

 The number `q₁ d`; the field `E` lies in the cyclotomic field of this order. 

### `rootDisc`

 The root discriminant `rd_E` of `E`. 

### `k`

 The rank `k = r + 1 - m` of the source; the subtraction is exact by `New.Data.r_add_one`. 

### `t`

 The number `t = 5 r`; consecutive ranks `n j` differ by `t + 1`. 

### `halfGap`

 Half the gap, `Δ / 2 = r ^ 8`. 

### `gap`

 The gap `Δ = 2 r ^ 8` between the weights `D.liftWeight j σ` of consecutive lifts. 

### `reducedHalfGap`

 The number `Δ / 2 - (t + 1) / 2`, where `Δ / 2 = D.halfGap`; note that `t` is odd. 

### `a`

 The number `a = x b`, called the long order; the sum `D.primeSum` runs over `1 ≤ ν ≤ a`. 

### `offWeight`

 The weight `a / x₁` at the places outside the set `D.bPlaces` of `b`-places. 

### `placeOfInt`

 The place that corresponds to the class of `j` in `(ℤ/q₁)ˣ` if `j` is prime to `q₁`, and the
identity place otherwise. 

### `n`

 The ranks `n_j = k + j (t + 1)`. 

### `posRank`

 The number `k + j - 1`. In the `j`-th step, `1 ≤ j ≤ m`, of the chain of theta lifts it is the
number of plus signs of the diagonal hermitian space `W_j = New.Data.spaceW` of rank `r` over `E`,
whose signs are `New.Data.signsW`. 

### `M`

 The principal level `M = p₀ p₁`. 

### `aPlaces`

 The set `Φ_a` of `a`-places: the places `≡ 1` modulo `q₀`. 

### `shiftedWeight`

 The number `κ(σ) + (i + 1) Δ / 2`, where `κ = D.weight` and `Δ / 2 = D.halfGap` is half the
gap. 

### `liftWeight`

 The weight `κ_j(σ) = κ(σ) + (j + 1/2) Δ` of the character of the `j`-th lift. 

### `primeSum`

 The prime sum `s_fin(y, σ) = ∑ Λ_K(ν) (y / ν - κ(-ν σ))₊` over `1 ≤ ν ≤ a`. Here
`Λ_K(ν) = Λ(ν) (1 - χ_K(ν))` is `lambdaKResidueClass P.d 1 ν`, and `-ν σ` is the product of `σ` with
`D.placeOfInt (-ν)`, which is the identity place if `ν` is not prime to `q₁`. 

### `errorUnit`

 The unit of loss `f a log³ b`, with `f` the number of infinite places and `a = x b`. 

### `jetSize`

 The size `s_∞(j) = log j! + j log (M / Ω)` of a derivative of order `j`. Here `M = D.M` and
`Ω = P.bigOmega D.towerExp = exp (γ - Re L'/L(1, χ_K)) 2π / rd_E`. 

### `directionAmount`

 The direction amount `∑_σ (s_∞(κ(σ)) - s_fin(κ(σ), σ))`, summed over all infinite places `σ`:
the size `s_∞ = D.jetSize` of a derivative of order `κ(σ)`, less the prime sum `s_fin = D.primeSum`
that measures its guaranteed divisibility. 

 ## The size of `N₋`

The bounds for `N₋` do not involve the level `N`, so they can be used to construct it. 

### `one_le_rootDiscr`

 The root discriminant of a number field is at least `1`. 

### `rootDiscr_mem_Icc`

 If a positive integer `c` lies in the different of the number field `K`, then the root
discriminant of `K` lies between `1` and `c`. 

### `sum_log_div_card_mem_Icc`

 If real numbers `κ i`, indexed by a nonempty finite type, lie in `[1, exp L]`, then the mean of
their logarithms lies in `[0, L]`. 

### `log_mul_div_two_pi_mem_Icc`

 If `b = exp L` with `L ≥ 7`, `M` lies in `[b ^ 20, b ^ 22]` and `R` lies in `[1, b]`, then
`M R / 2π` lies in `[b ^ 19, b ^ 23]`; the bounds are stated for the logarithm. 

### `Parameters.logLevelMin_mem_Icc`

 The bounds `m log b ≤ log N₋ ≤ 24 m log b` for `log N₋ = P.logLevelMin s m κ M L`, the logarithm
of `N₋ = κ̄ ^ m (M rd_E / 2π) ^ (m - 1) b ^ (-15 / 2)`, where `b = exp L`. The parameters `P`
consist of a modulus `q₀` and a prime `d = P.d`. The index `s` selects the multiple `q₁ = P.q₁ s` of
`q₀` and the field `E = K(ζ_{q₁})` over `K = ℚ(√-d)`, whose infinite places form the type `P.Φ s`.
Further `κ̄` is the geometric mean of the weights `κ` over these places, and `rd_E` is the root
discriminant of `E`, which is at most `q₁ d`. The hypotheses are `L ≥ 7`, `m ≥ 2`, weights in
`[1, b]`, `M` in `[b ^ 20, b ^ 22]` and `q₁ d ≤ b`. 
