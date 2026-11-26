---
{
  "module": "src/New/Derivatives/Sharpness/LeastValuation.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Sharpness/LeastValuation.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Sharpness/LeastValuation.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Least valuations of coefficients of theta products

The file bounds the least valuation `val_n(ν)` of a coefficient of degree `ν` in a product
`∏ (H_c Θ)(z_c)` over `n` copies of the variables.

The imported notions used in the statements are:

* `CMLattice d`: a lattice in `ℂ`, with a marked point `t` of order two and normalized at `t`, that
  is stable under the ring of integers of `ℚ(√-d)` if `d ≠ 0`. The results that need `d` to be a
  prime with `d ≡ 7 (mod 8)` assume `PrimeSevenModEight d`. Its function `C.θ` is the twisted
  translate by `t` of the sigma function with value `1` at `0`, and `C.translatedY` is an affine
  combination of `℘'(z + t)` and `℘(z + t)`.
* `PadicPlace p`: a ring homomorphism `ιₚ : ℂ →+* ℂ_[p]`. By `taylorVia ιₚ f` is meant the Taylor
  series of `f` at `0` with `ιₚ` applied to the coefficients.
* `C.thetaProd μ m`: the series `Θ = ∏ θ(μ_j z) ^ m j`, where `θ` is the Taylor series of `C.θ`
  and the `μ_j` are linear forms over `ℂ_p`.
* `C.multiSeriesRing μ`: the ring of integral power series in the series `y(μ_j z)`, where `y` is
  the Taylor series of `C.translatedY`.
* `varpiValuation d p`: the number `ρ_p`, equal to `1 / (p - 1)`, `1 / (p² - 1)`, `1 / (2 p - 2)`
  when `p` is split, inert, ramified in `ℚ(√-d)`. A scaling of valuation at least `ρ_p` makes the
  series in `y` integral.
* `gammaPrime d p`: the rate `γ_p = 1 / (p - 1) - ρ_p`.

## Main definitions and results

* `New.CMLattice.LeastValLE`: the relation `val_n(ν) ≤ r` for the least valuation of a coefficient
  of degree `ν` in a product `∏ (H_c Θ)(z_c)` over `n` copies of the variables.
* `New.CMLattice.LeastValLE.add`, `New.CMLattice.leastValLE_of_copySubst`: the two rules, for
  products and for integral substitutions.
* `New.CMLattice.scaledThetaProd`: the product `∏ Θ(δ_c z)` of scaled copies of `Θ`.
* `New.CMLattice.exists_scaledThetaProd_mem_mul_eq_one`: six scaled copies of `Θ` multiply to a unit
  of the ring of integral series in the `y(μ_j z)`.
* `New.CMLattice.leastValLE_of_unit_coefficients`, `New.CMLattice.leastValLE_zero_of_span`: two
  bounds for `val₆` in all degrees, when one form has unit coefficients and when integral
  combinations of the forms give the coordinates up to a unit.



## Least valuations of coefficients of theta products

For suitable scales in `ℤ_p` whose squares add up to zero, the product of six scaled copies of `Θ`
is a unit of the ring of integral series in the `y(μ_j z)`.


### `IsLowestTerm`

 `c z ^ m` is the lowest term of `f` for the weight `w`: in weight at most that of `m`, the
coefficients of `f` are those of the monomial `c z ^ m` (here `c = 0` is allowed). 

### `IsLowestTerm.mul`

 The lowest term of a product is the product of the lowest terms: if `f` has lowest term
`c * z ^ D` and `g` has lowest term `d * z ^ D'` for the weights `w`, then `f * g` has lowest term
`(c * d) * z ^ (D + D')`. 

### `IsLowestTerm.prod`

 If each factor `f i` has lowest term `c i * z ^ α i` for the weights `w`, then the product of
the `f i` has lowest term `(∏ c i) * z ^ (∑ α i)`. 

### `IsLowestTerm.pow`

 If `f` has lowest term `c * z ^ α`, then `f ^ k` has lowest term `c ^ k * z ^ (k • α)`. 

### `copySubst`

 The substitution `F ↦ F (∑ a_k z_k)` of a linear combination of copies `z_k` of the variables
`z`, with the same coefficients `a_k` for all variables. The copy `k` of the variable `x` is the
variable `(x, k)`. 

### `pderiv_copySubst`

 The chain rule: the derivative of `F (∑ a_l z_l)` in the `k`-th copy of the variable `x` is
`a_k` times `(∂_x F) (∑ a_l z_l)`. 

### `map_copySubst`

 The substitution of copies commutes with a change of coefficients along a ring map. 

### `killCompl_copySubst`

 Setting all copies but the `k`-th to zero turns `F (∑ a_l z_l)` into `F (a_k z)`. 

### `rescale_copySubst`

 Scaling all variables by `r` commutes with the substitution of copies: both composites send
`F` to `F (∑ r a_k z_k)`. 

### `mapDomain_fst_apply`

 The exponent `γ.mapDomain Prod.fst` adds up the copies of each variable in `γ`. 

### `prod_factorial_mapDomain_fst`

 For `γ : X × K →₀ ℕ`, let `γ.mapDomain Prod.fst` be the exponent on `X` that adds up `γ (x, k)`
over `k`. Then `∏ x, (γ.mapDomain Prod.fst x)!` is `∏ y, (γ y)!` times the product over `x` of the
multinomial coefficients of the exponents `γ (x, k)`, `k : K`. 

### `prod_factorial_mul_coeff_copySubst`

 Let `δ` be the exponent that adds up the copies of each variable in `γ`. Then `γ!` times the
coefficient of `z ^ γ` in `F (∑ a_k z_k)` is `a ^ γ` times `δ!` times the coefficient of `z ^ δ`
in `F`. 

### `coeff_copySubst`

 Over a domain of characteristic zero, the coefficient of `z ^ γ` in `F (∑ a_k z_k)` is `a ^ γ`
times a product of multinomial coefficients times the coefficient of `F` whose exponent adds up the
copies of each variable in `γ`. 

### `norm_coeff_copySubst_le`

 A coefficient of `F (∑ a_k z_k)` with integral `a_k` is at most as large as the coefficient of
`F` of the same degree, of which it is an integral multiple. The degree of the exponent `γ` adds up
the copies of each variable. 

### `padicInt_sum_four_squares`

 Every `p`-adic integer is a sum of four squares, by Lagrange's theorem and compactness. 

### `LeastValLE`

 The relation `val_n(ν) ≤ r`: some coefficient of degree `ν` in some product `∏ (H_c Θ)(z_c)`
over `n` copies `z_c` of the variables has valuation at most `r`. Here `C : CMLattice d` is a
lattice in `ℂ` with a marked point `t` of order two, which is stable under the integers of
`ℚ(√-d)` if `d ≠ 0`. The series `Θ = ∏ θ(μ_j z) ^ m j` is `C.thetaProd μ m`, the
`H_c` are integral series in the `y(μ_j z)`, and `θ`, `y` are the Taylor series of `C.θ` (the
normalized sigma function translated by `t`) and `C.translatedY` (a combination of the Weierstrass
functions at `z + t`), read in `ℂ_p` through the place `ιₚ` of `PadicPlace p`. A coefficient of the
product is the product of one coefficient of each factor. 

### `constantCoeff_thetaProd`

 The series `Θ = ∏ θ(μ_j z) ^ m j` has constant term `1`, because `θ(0) = 1`. 

### `isLowestTerm_thetaProd`

 The series `Θ = ∏ θ(μ_j z) ^ m j` has lowest term `1` for the total degree. 

### `LeastValLE.mono`

 If `val_n(ν) ≤ r` and `r ≤ r'`, then `val_n(ν) ≤ r'`, where `val_n(ν)` is the least valuation
of a coefficient of degree `ν` in a product `∏ (H_c Θ)(z_c)` over `n` copies of the variables. 

### `leastValLE_zero`

 `C.LeastValLE μ m n 0 0`: in degree `0`, some product `∏ (H_c Θ)(z_c)` over `n` copies `z_c` of
the variables, with `Θ = C.thetaProd μ m`, has a coefficient of valuation at most `0`: take all
`H_c = 1`. 

### `LeastValLE.add`

 Least valuations are subadditive: if `val_n(ν) ≤ r` and `val_n'(ν') ≤ r'`, then
`val_(n+n')(ν + ν') ≤ r + r'`. 

### `leastValLE_of_copySubst`

 Let `Θ = C.thetaProd μ m = ∏ θ(μ_j z) ^ m j` and `H_c ∈ C.multiSeriesRing μ` for `c < n`.
Substitute `z_c = ∑ A c k z'_k` in `∏ (H_c Θ)(z_c)`, with the `A c k` integers of `ℂ_p`. If the
coefficient of `z' ^ γ` in the result has `p`-adic valuation at most `r`, then
`C.LeastValLE μ m n ν r` holds for the degree `ν` that adds up the copies of each variable in `γ`:
some coefficient of degree `ν` in some product `∏ (H'_c Θ)(z_c)` over `n` copies `z_c` of the
variables, with `H'_c ∈ C.multiSeriesRing μ`, has valuation at most `r`. 

### `leastValLE_of_rescale`

 Let `Θ = C.thetaProd μ m = ∏ θ(μ_j z) ^ m j` and `H_c ∈ C.multiSeriesRing μ` for `c < n`. If,
for integers `δ_c` of `ℂ_p`, the coefficient of `z ^ ν` in `∏ (H_c Θ)(δ_c z)` has `p`-adic valuation
at most `r`, then `C.LeastValLE μ m n ν r` holds: some coefficient of degree `ν` in some product
`∏ (H'_c Θ)(z_c)` over `n` copies `z_c` of the variables, with `H'_c ∈ C.multiSeriesRing μ`, has
valuation at most `r`. 

### `LeastValLE.exists_monomial`

 Let `Θ = C.thetaProd μ m = ∏ θ(μ_j z) ^ m j`. Assume `C.LeastValLE μ m n ν r`: some coefficient
of degree `ν` in some product `∏ (H_c Θ)(z_c)` over `n` copies `z_c` of the variables, for some
`H_c ∈ C.multiSeriesRing μ`, has `p`-adic valuation at most `r`. Then the same holds with each `H_c`
a monomial `∏ y(μ_j z) ^ e c j` of degree at most `|ν|`; the coefficient is the product of the
coefficients of `z ^ α c` in `H_c Θ`, and `linearSeries (μ j)` is the form `μ_j z`. 

### `prod_rescale_theta_mem`

 Let `θ` and `y` be the Taylor series of `C.θ` and `C.translatedY`, read in `ℂ_p` through the
place `ιₚ`, for a lattice `C` with multiplication by the integers of `ℚ(√-d)`: `C.θ` is its
normalized sigma function translated by the marked point `t` of order two, and `C.translatedY` a
combination of its Weierstrass functions at `z + t`. If `∑ δ_c ^ 2 = 0` in `ℤ_p`, then `∏ θ(δ_c z)`
is an integral series in `y`. 

### `scaledThetaProd`

 The product `∏ Θ(δ_c z)` of copies of `Θ = C.thetaProd μ m = ∏ θ(μ_j z) ^ m j` scaled by
`p`-adic integers `δ_c`, where `θ` is the Taylor series of the theta function `C.θ`, read in `ℂ_p`,
and the `μ_j z` are linear forms. 

### `constantCoeff_scaledThetaProd`

 The product `∏ Θ(δ_c z)` of the scaled copies of `Θ = ∏ θ(μ_j z) ^ m j` has constant term
`1`. 

### `scaledThetaProd_eq_prod_subst`

 With `u(z) = ∏ θ(δ_c z)`, the product `∏ Θ(δ_c z)` of the scaled copies of
`Θ = ∏ θ(μ_j z) ^ m j` is `∏ u(μ_j z) ^ m j`. 

### `scaledThetaProd_mem`

 If `∑ δ_c ^ 2 = 0` in `ℤ_p`, then the product `C.scaledThetaProd μ m δ = ∏ Θ(δ_c z)` of the
scaled copies of `Θ = ∏ θ(μ_j z) ^ m j` lies in `C.multiSeriesRing μ`.

Here `C` is a lattice in `ℂ` with multiplication by the integers of `ℚ(√-d)`, for a prime
`d ≡ 7 (mod 8)`, and with a marked point `t` of order two. The series `θ` and `y` are the Taylor
series at `0`, read in `ℂ_p` through the embedding `ιₚ` of `ℂ`, of `C.θ` (the twisted translate by
`t` of the sigma function, with value `1` at `0`) and of `C.translatedY` (the function
`(℘'(z + t) - a₁ (℘(z + t) - ℘(t))) / 2`, where `a₁² = 12 ℘(t)`). The `μ_j z = ∑ μ j x * z_x`, for
`j : J`, are linear forms in the variables `z_x`, for `x : X`, and `C.multiSeriesRing μ` is the ring
of power series in the `y(μ_j z)` with coefficients in the integers of `ℂ_p`. 

### `exists_scaledThetaProd_mul_eq_one`

 If `∑ δ_c ^ 2 = 0` in `ℤ_p`, then the product `C.scaledThetaProd μ m δ = ∏ Θ(δ_c z)` of the
scaled copies of `Θ = ∏ θ(μ_j z) ^ m j` has an inverse in `C.multiSeriesRing μ`. 

### `exists_scaledThetaProd_mem_mul_eq_one`

 There are six `p`-adic integers `δ 0 = 1, δ 1, …, δ 5` such that the product
`C.scaledThetaProd μ m δ` of the scaled copies `Θ(δ_c z)` of `Θ = ∏ θ(μ_j z) ^ m j` is a unit of
`C.multiSeriesRing μ` with constant term `1`. 

### `leastValLE_of_unit_coefficients`

 If one of the forms `μ_j` has unit coefficients, then `val₆(ν) ≤ γ_p |ν| - v(ν!)`: some
coefficient of degree `ν` in some product `∏ (H_c Θ)(z_c)` over six copies `z_c` of the variables,
with `Θ = C.thetaProd μ m = ∏ θ(μ_j z) ^ m j` and `H_c ∈ C.multiSeriesRing μ`, has valuation at most
`γ_p |ν| - v(ν!)`. The letter `v` is the `p`-adic valuation, `ν! = ∏ (ν x)!`, and
`γ_p = gammaPrime d p` is `0`, `p / (p² - 1)`, `1 / (2 p - 2)` when `p` is split, inert, ramified in
`ℚ(√-d)`. 

### `leastValLE_zero_of_span`

 If each coordinate `z_x`, up to a unit `s`, is a combination `∑ a x j • μ_j z` with coefficients
in the ring `valRingCp p` of integers of `ℂ_p`, then `val₆(ν) ≤ 0` in every degree `ν`: some
coefficient of degree `ν` in some product `∏ (H_c Θ)(z_c)` over six copies `z_c` of the variables,
with `Θ = C.thetaProd μ m = ∏ θ(μ_j z) ^ m j` and `H_c ∈ C.multiSeriesRing μ`, has `p`-adic
valuation at most `0`. 

### `rescale_mem_range_seriesToCp_of_mem_multiSeriesRing`

 If the coefficients of the forms `μ_j` are integers of `ℂ_p` and `ϖ` has `p`-adic valuation at
least `ρ_p = varpiValuation d p`, then a series `H ∈ C.multiSeriesRing μ` has integral coefficients
after the scaling `z ↦ ϖ z`: the result is in the range of `seriesToCp`, the inclusion of series
over the integers of `ℂ_p`. 
