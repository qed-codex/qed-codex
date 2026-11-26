---
{
  "module": "src/Lib/General/Algebra/SeriesCongruences.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Algebra/SeriesCongruences.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Algebra/SeriesCongruences.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Power series with prime power exponents, congruences and convergent sums

This file studies power series of the form `∑_{i ∈ I} z ^ p ^ i` and congruences between power
series modulo a constant `π`, with the facts on continuity and convergent sums that are needed to
work with such congruences.

## Main definitions and results

* `New.primePowerSeries`: the series `∑_{i ∈ I} z ^ p ^ i`.
* `New.primePowerSeries_even_pow`: in characteristic `p` the `p`-th power of `∑_{i even} z ^ p ^ i`
  is `∑_{i odd} z ^ p ^ i`.
* `New.exists_eq_pow_add_pow_of_coeff_mul_ne_zero`: a product of two series `∑_{i ∈ I} z ^ p ^ i`
  has only terms of the degrees `p ^ i + p ^ j`.
* `New.dvd_sum_pow_sub_sum`: for a prime `p` the `p ^ j`-th powers are additive modulo a divisor of
  `p`.
* `New.continuous_subst_of_constantCoeff_eq_zero`, `New.continuous_pderiv`: substitution of finitely
  many series without constant term and differentiation are continuous.
* `New.C_dvd_of_hasSum`: over the valuation ring of `ℂ_[p]` a convergent sum of power series
  divisible by `π` is divisible by `π`.

Power series carry the topology of coefficientwise convergence.

## Relation to the literature

Known result: elementary facts on power series in characteristic `p`.

Known result: elementary facts on formal power series with the topology of coefficientwise
convergence. Source: Bourbaki, Algebra II, Chapter IV.


 ## Series with prime power exponents 

### `primePowerSeries`

 The series `∑_{i ∈ I} z ^ p ^ i` over `R`: its coefficient of degree `n` is `1` if `n = p ^ i`
for some `i ∈ I`, and `0` otherwise. 

### `primePowerSeries_even_pow`

 In characteristic `p` the `p`-th power of `∑_{i even} z ^ p ^ i` is `∑_{i odd} z ^ p ^ i`. Here
`primePowerSeries R p I` is the series `∑_{i ∈ I} z ^ p ^ i`. 

### `exists_eq_pow_add_pow_of_coeff_mul_ne_zero`

 The product of `primePowerSeries R p I = ∑_{i ∈ I} z ^ p ^ i` and
`primePowerSeries R p J = ∑_{j ∈ J} z ^ p ^ j` has only terms of the degrees `p ^ i + p ^ j` with
`i ∈ I` and `j ∈ J`. 

### `exists_pow_add_pow_eq`

 The number `p ^ i + p ^ i'` has the form `(p ^ e + 1) p ^ j` where `e` has the parity of
`i + i'`. 

### `injective_pow_add_one_mul_pow`

 For an odd prime `p` the numbers `e` and `j` are determined by `(p ^ e + 1) p ^ j`. 

### `pow_add_pow_eq_iff`

 For an odd prime `p` one has `p ^ i + p ^ i' = (p ^ e + 1) p ^ j` exactly if `j` is the smaller
and `e + j` the larger of the numbers `i` and `i'`. 

### `coeff_primePowerSeries_mul`

 For an odd prime `p` the coefficient of degree `(p ^ e + 1) p ^ j` in the product of
`primePowerSeries R p I = ∑_{i ∈ I} z ^ p ^ i` and `primePowerSeries R p J = ∑_{i' ∈ J} z ^ p ^ i'`
counts the pairs `(i, i') ∈ I × J` among `(e + j, j)` and `(j, e + j)`. 

### `coeff_primePowerSeries_odd_mul_even`

 For an odd prime `p` and odd `e` the product of `∑_{i odd} z ^ p ^ i` and `∑_{i even} z ^ p ^ i`
has coefficient `1` in degree `(p ^ e + 1) p ^ j`. 

### `coeff_primePowerSeries_univ_sq`

 For an odd prime `p` the square of `primePowerSeries R p Set.univ = ∑_i z ^ p ^ i` has in degree
`(p ^ e + 1) p ^ j` the coefficient `1` if `e = 0`, and `2` otherwise. 

### `hasSum_smul_X_pow_mul_X_pow`

 Let `p` be an odd prime. A series `f` that has terms only in the degrees `(p ^ e + 1) p ^ j`
with `e ∈ S`, with coefficients `l e j`, is the sum of the `l e j • (z ^ p ^ e z) ^ p ^ j` in the
topology of coefficientwise convergence. 

### `hasSum_primePowerSeries_odd_mul_even`

 For an odd prime `p` and `l ∈ R` the series `l (∑_{i odd} z ^ p ^ i) (∑_{i even} z ^ p ^ i)` is
the sum of the `l (z ^ p ^ e z) ^ p ^ j` over the odd `e` and all `j`. 

### `hasSum_primePowerSeries_univ_sq_sub`

 Let `p` be an odd prime, let `half` be an inverse of `2` in `R`, let `l ∈ R` and
`P = primePowerSeries R p Set.univ = ∑_i z ^ p ^ i`. Then `l (P ^ 2 - z ^ 2 / 2)` is the sum of the
`l_{e j} (z ^ p ^ e z) ^ p ^ j` over all `e` and `j`, where `l_{0 0} = l / 2`, `l_{0 j} = l` for
`j ≥ 1`, and `l_{e j} = 2 l` for `e ≥ 1`. 

 ## Congruences and infinite sums of power series 

### `dvd_sum_pow_sub_sum`

 If `π` divides the prime `p` in `R`, then `p ^ j`-th powers are additive modulo `π`. 

### `degree_le_order_prod_pow`

 If the series `Z x` have no constant term, then the monomial `∏_x Z x ^ d x` has order at least
the total degree of `d`. 

### `continuous_subst_of_constantCoeff_eq_zero`

 Substitution of series `Z x` without constant term for finitely many variables `x` is continuous
in the topology of coefficientwise convergence. 

### `continuous_pderiv`

 Partial differentiation of power series is continuous in the topology of coefficientwise
convergence. 

### `summable_of_finite_order_le`

 A family of power series is summable, in the topology of coefficientwise convergence, if for
each `n` only finitely many of its members have order at most `n`. 

### `summable_smul_pow_pow`

 The family `l e j • G e ^ p ^ j`, indexed by `e ∈ S` and `j ∈ ℕ`, is summable if `1 < p` and
each `G e` has order at least `p ^ e + 1`. 

### `dvd_iff_norm_le`

 In the valuation ring of `ℂ_[p]` the element `x` divides `y` exactly if `‖y‖ ≤ ‖x‖`. 

### `dvd_of_hasSum`

 In the valuation ring of `ℂ_[p]` the sum of a convergent family of multiples of `π` is a
multiple of `π`. 

### `C_dvd_of_hasSum`

 A convergent sum of power series over the valuation ring `valRingCp p` of `ℂ_[p]`, each
divisible by the constant `π`, is divisible by `π`. 

 ## Congruences in one variable 

### `dvd_sub_smul_of_dvd_sub`

 If `F ≡ l G` and `G ≡ H` modulo `D`, then `F ≡ l H` modulo `D`. 

### `norm_sub_le_of_norm_one_sub_mul_sub_le`

 In `ℂ_[p]` let `‖t‖ ≤ ‖π‖ < 1` and `‖a‖ ≤ 1`. If `(1 - t) x ≡ a` modulo `π`, then `x ≡ a` modulo
`π`, where `y ≡ y'` means `‖y - y'‖ ≤ ‖π‖`. 
