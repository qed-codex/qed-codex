---
{
  "module": "src/New/Derivatives/FormalGroup/FrobeniusCongruence.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/FormalGroup/FrobeniusCongruence.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/FormalGroup/FrobeniusCongruence.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Frobenius congruence for `θ` and the coefficient of `z ^ (p - 1)` in `x`

Let `d ≡ 7` modulo `8` be a prime, `C` a lattice with complex multiplication by the integers of
`K = ℚ(√-d)`, and `p` a prime that does not split in `K`. This file proves that
`θ(π_p z) / θ(z) ^ q_p` is `1` modulo `π_p` in `𝒪[[y]]`. For `g = -log θ` it follows that
`q_p g(z) - g(π_p z)` lies in `π_p 𝒪[[y]]`. Independently of this congruence, it shows by a
recursion that at an inert prime the coefficient of `z ^ (p - 1)` in `x` is a unit; this is used in
the last step for the exponent on one curve (`New.CMLattice.norm_coeff_exponentSeries_eq_one`).

Notions from other files:
* `chiK d p` is the Legendre symbol `(p / d)`: it is `1`, `-1`, `0` when `p` is split, inert,
  ramified in `K`.
* `π_p = piPrime d p` is `√-d` for `p = d` and `p` otherwise; `q_p = primeNorm d p` is `p ^ 2` for
  inert `p` and `p` otherwise.
* `PadicPlace p` is the choice of a ring homomorphism `ιₚ : ℂ →+* ℂ_[p]`, and `taylorVia ιₚ f` is
  the Taylor series of `f` at `0`, with coefficients sent to `ℂ_[p]` by `ιₚ`.
* `θ`, `x`, `y` are the series of the theta function `C.θ`, of `C.translatedX z = ℘(z + t) - ℘(t)`
  and of `C.translatedY z = (℘'(z + t) - a₁ x(z)) / 2`. Here `t = C.t` is the chosen point of order
  two, the lattice is scaled so that `℘''(t) = 2`, and `a₁ = C.a₁` satisfies `a₁ ^ 2 = 12 ℘(t)`;
  moreover `g = C.negLogTheta = -log θ`.
* `C.integralSeriesRing = 𝒪[[y]]` is the ring of power series in `y` with coefficients in the
  valuation ring `𝒪` of `ℂ_[p]`.

## Main definitions and results

* `New.CMLattice.exists_rescale_theta_eq_pow_mul_one_add_smul`: at a non-split prime `p` the
  quotient `θ(π_p z) / θ(z) ^ q_p` is `1` modulo `π_p` in `𝒪[[y]]`.
* `New.CMLattice.exists_negLogTheta_frobenius_congruence`: `q_p g(z) - g(π_p z) ∈ π_p 𝒪[[y]]` for
  `g = -log θ`.
* `New.CMLattice.norm_coeff_taylorVia_translatedX_eq_one`: at an inert prime `p` the coefficient
  of `z ^ (p - 1)` in the series `x` is a unit.



## The Frobenius congruence for `θ`

The quotient `θ(π_p z) / θ(z) ^ q_p` is a polynomial in `x` of degree less than `q_p / 2`, so the
congruence can be checked below the degree `q_p`, where `π_p g` is integral.


### `ne_two_of_chiK_ne_one`

 A prime `p` with `chiK d p ≠ 1`, that is, with Legendre symbol `(p / d) ≠ 1`, so that `p` does
not split in `ℚ(√-d)`, is odd (`p ≠ 2`), as `2` splits. 

### `odd_primeNorm`

 Let `d ≡ 7` modulo `8` be a prime. If the prime `p` does not split in `ℚ(√-d)`, that is
`chiK d p ≠ 1`, then `primeNorm d p`, which is `p ^ 2` or `p`, is odd, since the prime `2`
splits. 

### `lt_primeNorm_of_chiK_eq_neg_one`

 If `p` is inert in `ℚ(√-d)`, then `p < q_p = primeNorm d p = p ^ 2`. 

### `norm_primeNorm`

 Let `d ≡ 7` modulo `8` be a prime and `p` a prime that does not split in `ℚ(√-d)`. Then
`|q_p| = |π_p| ^ 2` in `ℂ_[p]`, as `q_p = ± π_p ^ 2`. 

### `norm_piPrime_le_rpow`

 Let `d ≡ 7` modulo `8` be a prime and `p` a prime that does not split in `ℚ(√-d)`. Then
`|π_p| ≤ p ^ (-1 / (p - 1))` in `ℂ_[p]`, as `p ≥ 3` (the prime `2` splits) and the valuation of
`π_p` is at least `1 / 2`. 

### `norm_piPrime_le_norm_sqrt_neg`

 Let `d ≡ 7` modulo `8` and `p` be primes. Then `|π_p| ≤ |√-d|` in `ℂ_[p]`, via the homomorphism
`ιₚ : ℂ →+* ℂ_[p]` that `PadicPlace p` chooses. 

### `norm_piPrime_le_norm_natCast`

 Let `d ≡ 7` modulo `8` and `p` be primes. Then `|π_p| ≤ |n|` in `ℂ_[p]` for `0 < n < q_p`. 

### `norm_piPrime_le_norm_mul_succ`

 Let `d ≡ 7` modulo `8` and `p` be primes. Then `|π_p| ≤ |(k + 2) (k + 1)|` in `ℂ_[p]` for
`k + 2 < q_p`, as one of the two factors is prime to `p`. 

### `exists_rescale_theta_eq_pow_mul_aeval`

 Let `d ≡ 7` modulo `8` be a prime and `p` a prime that does not split in `ℚ(√-d)`. Then
`θ(π_p z) = θ(z) ^ q_p * R(x(z))` as power series over `ℂ_[p]`, for a polynomial `R` of degree less
than `q_p / 2`. 

### `norm_piPrime_mul_coeff_negLogTheta_le_one`

 Let `d ≡ 7` modulo `8` be a prime and `p` a prime that does not split in `ℚ(√-d)`. Then
`|π_p| |g_n| ≤ 1` for the `n`-th coefficient `g_n` of `g` and `n < q_p`. 

### `norm_coeff_smul_negLogTheta_sub_rescale_le`

 Let `d ≡ 7` modulo `8` be a prime and `p` a prime that does not split in `ℚ(√-d)`. For `n < q_p`
the `n`-th coefficient `(q_p - π_p ^ n) g_n` of `q_p g(z) - g(π_p z)` has norm at most `|π_p|`. 

### `exists_rescale_theta_eq_pow_mul_one_add_smul`

 The Frobenius congruence. Let `d ≡ 7` modulo `8` be a prime and `p` a prime that does not split
in `ℚ(√-d)`. The Taylor series of `θ` at `0`, mapped by the chosen `ιₚ : ℂ →+* ℂ_[p]`, satisfies
`θ(π_p z) = θ(z) ^ q_p * (1 + π_p H)` for some `H ∈ 𝒪[[y]]`. 

### `exists_negLogTheta_frobenius_congruence`

 The logarithm of the Frobenius congruence. Let `d ≡ 7` modulo `8` be a prime and `p` a prime
that does not split in `ℚ(√-d)`. Then `q_p g(z) - g(π_p z) = π_p H` for some `H ∈ 𝒪[[y]]`. 


## The coefficient of `z ^ (p - 1)` in `x` at an inert prime

The numbers `h_n = [z ^ (p - 1)] x ^ n` satisfy a three-term recursion modulo `p` that leads from
`h_0 = 0` and `h_1` to `h_((p - 1) / 2) = 1`.


### `derivative_taylorVia_translatedX_sq`

 `x'² = 4 x³ + a₁² x² + 4 x` for the Taylor series `x` of `℘(z + t) - ℘(t)`, with coefficients
mapped to `K` by `ι`. 

### `derivative_derivative_taylorVia_translatedX`

 `x'' = 6 x² + a₁² x + 2` for the Taylor series `x` of `℘(z + t) - ℘(t)`, with coefficients
mapped to `K` by `ι`. 

### `derivative_pow_mul_derivative_taylorVia_translatedX`

 `(xⁿ x')' = (4 n + 6) xⁿ⁺² + (n + 1) a₁² xⁿ⁺¹ + (4 n + 2) xⁿ` for the Taylor series `x` of
`℘(z + t) - ℘(t)`, with coefficients mapped to `K` by `ι`. 

### `norm_coeff_pow_taylorVia_translatedX_recursion_lt_one`

 Let `d ≡ 7` modulo `8` be a prime and `p` a prime that is inert in `ℚ(√-d)`. The numbers
`h_n = [z ^ (p - 1)] x ^ n` satisfy a recursion modulo the maximal ideal: `(4 n + 6)
h_(n + 2) + (n + 1) a₁² h_(n + 1) + (4 n + 2) h_n` has norm less than `1`. 

### `coeff_two_mul_taylorVia_translatedX_pow`

 The coefficient of `z ^ (2 m)` in `x ^ m` is `1`, as the Taylor series `x` of
`℘(z + t) - ℘(t)`, mapped by `ιₚ : ℂ →+* ℂ_[p]`, is `z² + ⋯`. Here `t = C.t` is the chosen point of
order two, with `℘''(t) = 2`. 

### `norm_coeff_pow_taylorVia_translatedX_lt_one`

 Let `d ≡ 7` modulo `8` be a prime and `p = 2 m + 1` a prime that is inert in `ℚ(√-d)`. If the
coefficient of `z ^ (p - 1)` in `x` has norm less than `1`, then so does that in `x ^ n` for every
`n ≤ m`, by the recursion for these coefficients. 

### `norm_coeff_taylorVia_translatedX_eq_one`

 Let `d ≡ 7` modulo `8` be a prime and `p` a prime that is inert in `ℚ(√-d)`. The coefficient of
`z ^ (p - 1)` in the Taylor series `x` of `℘(z + t) - ℘(t)`, mapped by `ιₚ : ℂ →+* ℂ_[p]`, has norm
`1`. 
