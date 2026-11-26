---
{
  "module": "src/New/Derivatives/Sharpness/OneCurve.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Sharpness/OneCurve.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Sharpness/OneCurve.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Derivatives of integral expansions

* `New.exists_monomial_max_norm_coeff`: among the integral series in the `f i`, times a fixed
  series, a monomial of degree at most `|α|` has the largest coefficient at `α`.
* `New.CMLattice.katz_divisibility_limit`: for every `n` some `g ∈ 𝒪[[y]]` has `v(g⁽ⁿ⁾(0)) ≤ γ_p n`,
  where `γ_p = 1 / (p - 1) - ρ_p`.

The least valuation of `g⁽ⁿ⁾(0)` is superadditive in `n`, by the integrality of the group law, and
the formal parameter bounds it when `n` is a power of `q_p`. We work with absolute values, so that
least valuations become greatest norms and sums become products.

## Notation

* `d` is a prime congruent to `7` mod `8` (`PrimeSevenModEight d`), and a ring homomorphism
  `ιₚ : ℂ →+* ℂ_[p]` is fixed (`PadicPlace p`).
* `C : CMLattice d` is a lattice `Λ` stable under the integers of `ℚ(√-d)`, with a point `t` of
  order two modulo `Λ` and a square root `a₁` of `12 ℘(t)`.
* `y = taylorVia ιₚ C.translatedY` is the Taylor series at `0` of
  `(℘'(z + t) - a₁ (℘(z + t) - ℘(t))) / 2`, carried to `ℂ_p` by the chosen map `ιₚ : ℂ →+* ℂ_[p]`.
* `C.integralSeriesRing` is `𝒪[[y]]`, the power series in `y` over the valuation ring `𝒪` of `ℂ_p`.
* `primeNorm d p` is `q_p`, the norm of a prime of `ℚ(√-d)` above `p`, and `varpiValuation d p` is
  `ρ_p = 1 / (e (q_p - 1))`, with `e` the ramification index; `gammaPrime d p` is the rate
  `γ_p = 1 / (p - 1) - ρ_p`.

## Relation to the literature

At inert primes the rate `γ_p` is that of Katz, Divisibilities, congruences, and Cartier duality.


### `exists_monomial_max_norm_coeff`

 Let the `f i` be finitely many series over `ℂ_p` without constant term (`HasSubst f`), and let
`s` be a series. There is a monomial `∏ f i ^ m i` with `|m| ≤ |α|` such that the coefficient at `α`
of `(∏ f i ^ m i) * s` is at least as large in norm as that of `G(f) * s`, for every series `G` over
the valuation ring of `ℂ_p`; `seriesToCp G` is `G` read over `ℂ_p`. 

### `pow_le_of_submultiplicative`

 Let `0 < b ≤ 1`, and let `c` be a submultiplicative sequence in `[0, 1]` with `c 0 = 1`. If
`b ^ q ≤ c q` for arbitrarily large `q`, then `b ^ n ≤ c n` for all `n` (a form of Fekete's
lemma). 

### `rpow_pow_le_norm_factorial_succ`

 Legendre's bound `v((n + 1)!) ≤ n / (p - 1)`, for the norm of `ℂ_p`. 

### `factorial_mul_coeff_subst_add`

 Differentiating `g(z₀ + z₁)` `m` times in `z₀` and `n` times in `z₁` at `0` gives
`g⁽ᵐ⁺ⁿ⁾(0)`. Here `linearSeries ![1, 1]` is the linear form `z₀ + z₁`. 

### `coeff_subst_mul_subst`

 The coefficient of `z₀ ^ m z₁ ^ n` in `g(z₀) h(z₁)` is the product of the `m`-th coefficient
of `g` and the `n`-th coefficient of `h`. Here `linearSeries ![1, 0]` and `linearSeries ![0, 1]` are
the linear forms `z₀` and `z₁`. 

### `maxDerivNorm`

 The greatest norm of `g⁽ⁿ⁾(0) = n! · coeff n g` for `g` in `𝒪[[y]] = C.integralSeriesRing`; it
is `p ^ (-v)` for the least valuation `v` of these derivatives. 

### `exists_isGreatest_norm_deriv`

 Among the `g` in `C.integralSeriesRing`, the power series in `y` over the valuation ring of
`ℂ_p`, the greatest norm of `g⁽ⁿ⁾(0) = n! · coeff n g` is attained by a power of `y`. 

### `exists_norm_deriv_eq_maxDerivNorm`

 The greatest norm `C.maxDerivNorm n` of `g⁽ⁿ⁾(0) = n! · coeff n g` is attained by some `g` in
`𝒪[[y]] = C.integralSeriesRing`. 

### `norm_deriv_le_maxDerivNorm`

 For `g` in `𝒪[[y]] = C.integralSeriesRing`, the norm of `g⁽ⁿ⁾(0) = n! · coeff n g` is at most
`C.maxDerivNorm n`. 

### `norm_deriv_le_one`

 If `g` lies in `C.integralSeriesRing`, the power series in `y` over the valuation ring of `ℂ_p`,
then `g⁽ⁿ⁾(0) = n! · coeff n g` has norm at most `1`, as this ring is stable under
differentiation. 

### `maxDerivNorm_zero`

 The greatest norm `C.maxDerivNorm 0` of `g(0)`, for `g` in `𝒪[[y]] = C.integralSeriesRing`, is
`1`, attained by the series `1`. 

### `exists_norm_coeff_le_norm_coeff_prod_pow`

 Let `μ_i z = linearSeries (μ i)` be the linear form with coefficients `μ i`. For some monomial
`∏ y(μ_i z) ^ e i`, the norm of its coefficient at `α` bounds that of every element of
`C.multiSeriesRing μ`, the ring of power series in the `y(μ_i z)` over the valuation ring of
`ℂ_p`. 

### `exists_norm_coeff_subst_add_le`

 Substituting `linearSeries ![1, 1]` replaces `z` by `z₀ + z₁`. The coefficient of
`z₀ ^ m z₁ ^ n` in `y(z₀ + z₁) ^ j` has norm at most that of `coeff m (y ^ a) * coeff n (y ^ b)` for
some `a` and `b`. 

### `maxDerivNorm_add_le`

 The greatest norm `C.maxDerivNorm n` of `g⁽ⁿ⁾(0)`, for `g` a power series in `y` over the
valuation ring of `ℂ_p`, is submultiplicative in `n`: the least valuation is superadditive. 

### `norm_eq_one_of_piPrimeInt_dvd_sub_one`

 Let `π_p` be `√-d` if `p = d` and `p` otherwise, and let `piPrimeInt d` be its image under the
map `ιₚ : ℂ →+* ℂ_[p]` of `PadicPlace p`, an integer of norm less than `1`. An integer of `ℂ_p`
that is `1` modulo `piPrimeInt d` has norm `1`. 

### `norm_coeff_formalParam_of_eq_primeNorm_pow`

 Let `q = primeNorm d p` be the norm of a prime of `ℚ(√-d)` above `p`. If `n + 1` is a power of
`q`, then the coefficient of `z ^ (n + 1)` in `C.formalParam`, the part of `y` in degrees `≡ 1` mod
`q - 1`, has valuation `-n ρ_p`. 

### `pow_le_maxDerivNorm_of_eq_primeNorm_pow`

 Let `q = primeNorm d p` be the norm of a prime of `ℚ(√-d)` above `p`. If `n + 1` is a power of
`q`, then the greatest norm `C.maxDerivNorm (n + 1)` of `g⁽ⁿ⁺¹⁾(0)`, for `g` a power series in `y`
over the valuation ring of `ℂ_p`, is at least `p ^ (-n γ_p)`. 

### `katz_divisibility_limit`

 The limit on Katz's divisibility of derivatives: no divisibility better than the rate `γ_p`
holds for all series.

For every `n` there is `f` in `C.integralSeriesRing`, the power series in `y` over the valuation
ring of `ℂ_p`, whose derivative `f⁽ⁿ⁾(0) = n! · coeff n f` has norm at least `p ^ (-n γ_p)`. 
