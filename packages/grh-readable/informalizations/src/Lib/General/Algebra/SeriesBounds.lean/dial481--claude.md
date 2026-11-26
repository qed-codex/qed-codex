---
{
  "module": "src/Lib/General/Algebra/SeriesBounds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Algebra/SeriesBounds.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Algebra/SeriesBounds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Integrality of exponentials, logarithms and roots of power series

The file first shows that, over an algebraically closed valued field, there is an integral point at
which finitely many given polynomials are at least as large as all their coefficients. It then
bounds the coefficients of power series built by exponentials, logarithms and roots over `ℂ_[p]`.
There `v` denotes the additive valuation with `v(p) = 1`, so that `‖c‖ = p ^ (-v(c))`, and `v(g)`
for a series `g` is the infimum of the valuations of its coefficients. `expSubst g` is `exp ℂ_[p]`
substituted at `g`, written `exp g`, and `logOf f` is `log ℂ_[p]`, the series of `log (1 + X)`,
substituted at `f - 1`, written `log f`. For `g(0) = 0` it proves that `exp g` is integral when
`v(g) ≥ 1 / (p - 1)`, gives a divisibility criterion for `exp g - 1`, and shows that `exp g` lies in
a ring `𝒪[[T]]` if its `m`-th power does, for `m` prime to `p`.

The imported notions used in the statements are these.

* `seriesToCp` is the inclusion of the series with integral coefficients into all series over
  `ℂ_[p]`. Its range consists of the series whose coefficients have norm at most `1`.
* `IsSeriesGenerator B T` says that `T = X + ⋯` and that `B` is the ring of all integral series in
  `T`, written `B = 𝒪[[T]]`.

## Main definitions and results

* `New.exists_val_coeff_le_val_eval`: at one integral point, finitely many polynomials are at least
  as large as all their coefficients.
* `New.norm_coeff_expSubst_le_one`: `exp g` is integral if `g(0) = 0` and `v(g) ≥ 1 / (p - 1)`,
  degree by degree.
* `New.norm_coeff_expSubst_sub_one_le`, `New.IsSeriesGenerator.mem_of_expSubst_smul_eq`: for
  `v(c) ≥ 1 / (p - 1)` and `g(0) = 0`, the number `c` divides `exp g - 1` if it divides `g`, and,
  for `c ≠ 0` and in a ring `𝒪[[T]]`, `c` divides `g` if it divides `exp g - 1`.
* `New.IsSeriesGenerator.expSubst_mem_of_pow_mem`: if `g(0) = 0` and `(exp g) ^ m ∈ 𝒪[[T]]` with `m`
  prime to `p`, then `exp g ∈ 𝒪[[T]]`.

## Relation to the literature

Known result: the Gauss norm equals the supremum norm on the unit polydisc over an algebraically
closed valued field. Source: Bosch, Güntzer and Remmert, *Non-Archimedean Analysis*.

Known result: the integrality of the `p`-adic exponential and logarithm on series of large enough
valuation, and of the binomial series with exponent in `ℤ_p`.



## A general integral point

Each polynomial is a constant times a polynomial with nonzero reduction. As the residue field is
infinite, there is a point at which none of the reductions vanishes.


### `New.exists_val_coeff_le_val_eval`

 Over an algebraically closed valued field there is an integral point at which each of finitely
many polynomials takes a value at least as large as all its coefficients. 


## Bounds for exponentials, logarithms and roots

The bounds come from Legendre's formula for `v(j!)` and from the binomial series over `ℤ_p`.


### `derivative_expSubst`

 If `g(0) = 0`, then `(exp g)' = exp g * g'`, where `exp g` is `expSubst g`. 

### `constantCoeff_expSubst`

 If `g(0) = 0`, then `exp g` has constant term `1`. 

### `constantCoeff_smul_sub_rescale`

 If `g(0) = 0`, then `s g(X) - g(δ X)` has constant term `0`. 

### `mul_derivative_logOf`

 The logarithmic derivative: `f (log f)' = f'` if `f(0) = 1`. 

### `logOf_expSubst`

 If `g(0) = 0`, then `log (exp g) = g`, where `exp g` is `expSubst g`. 

### `expSubst_logOf`

 If `f(0) = 1`, then `exp (log f) = f`, where `exp` is `expSubst` and `log f` is `logOf f`. 

### `norm_coeff_pow_le`

 Let `g` be a series in any variables and `r ≥ 0`. If the coefficients of `g` in degrees `≤ l`
have norm at most `r`, those of `g ^ j` in these degrees have norm at most `r ^ j`. 

### `norm_coeff_subst_le`

 Let `g` be a series in any variables with `g(0) = 0`, with coefficients in degrees `≤ l` of
norm at most `r`, where `r ≥ 0`, and let `f = ∑ f_j X ^ j` satisfy `‖f_j‖ r ^ j ≤ s` for all `j`.
Then the coefficients of `f(g)` in degrees `≤ l` have norm at most `s`. 

### `norm_coeff_expSubst_le_one`

 Let `g(0) = 0`. If the coefficients of `g` in degrees `≤ l` have norm at most
`p ^ (-1 / (p - 1))`, that is, valuation at least `1 / (p - 1)`, then `exp g`, written `expSubst g`,
is integral in these degrees.

A consequence of the upper bound `v(j!) ≤ j / (p - 1)` given by Legendre's formula, applied to the
terms `g ^ j / j!` of the exponential series. 

### `norm_coeff_pow_le_of_lt`

 If the coefficients of the series `g` in one variable below the degree `l` have norm at most
`r`, where `r ≥ 0`, those of `g ^ j` below the degree `l` have norm at most `r ^ j`. 

### `norm_coeff_subst_le_of_lt`

 Let `g` be a series in one variable with `g(0) = 0`, with coefficients below the degree `l`
of norm at most `r`, where `r ≥ 0`, and let `f = ∑ f_j X ^ j` satisfy `‖f_j‖ r ^ j ≤ s` for all
`j`. Then the coefficients of `f(g)` below the degree `l` have norm at most `s`. 

### `norm_coeff_le_of_aeval`

 A triangular system: let `x = X ^ 2 + ⋯` be integral below the degree `l` and `R` a polynomial.
If the coefficients of `R(x)` below the degree `l` have norm at most `s`, then so do the
coefficients `R_i` of `R` with `2 i < l`. 

### `norm_pow_le_norm_factorial_succ`

 If `v(c) ≥ 1 / (p - 1)`, that is, `‖c‖ ≤ p ^ (-1 / (p - 1))`, then `c ^ j / (j + 1)!` is
integral, as `v((j + 1)!) ≤ j / (p - 1)`. 

### `norm_pow_le_norm_succ`

 If `v(c) ≥ 1 / (p - 1)`, that is, `‖c‖ ≤ p ^ (-1 / (p - 1))`, then `c ^ j / (j + 1)` is
integral. 

### `norm_coeff_expSubst_sub_one_le`

 Let `v(c) ≥ 1 / (p - 1)`, that is, `‖c‖ ≤ p ^ (-1 / (p - 1))`, and `g(0) = 0`. If `c` divides
the coefficients of `g` below the degree `l`, that is, they have norm at most `‖c‖`, then it also
divides those of `exp g - 1`, where `exp g` is `expSubst g`. 

### `inv_smul_rescale_log_mem`

 If `v(c) ≥ 1 / (p - 1)`, that is, `‖c‖ ≤ p ^ (-1 / (p - 1))`, the series `log (1 + c X) / c`
is integral: it lies in the range of `seriesToCp`, the inclusion of the integral series. 

### `exists_pow_eq_one_add_X`

 For `m` prime to `p` the series `1 + X` has an `m`-th root with constant term `1` and integral
coefficients (it lies in the range of `seriesToCp`): the binomial series with exponent `1 / m`, as
its coefficients lie in `ℤ_p`. 

### `eq_of_pow_eq_pow_of_constantCoeff_eq_one`

 Two series with constant term `1` and the same `m`-th power, `m ≠ 0`, are equal. 

### `subst_mem`

 Let `B = 𝒪[[T]]` (`IsSeriesGenerator B T`: `T = X + ⋯` and `B` is the ring of all integral
series in `T`), let `f` be a series with integral coefficients (an element of the range of
`seriesToCp`) and `h ∈ B` without constant term. Then `f(h) ∈ B`. 

### `mem_of_expSubst_smul_eq`

 Let `B = 𝒪[[T]]` (`IsSeriesGenerator B T`), `c ≠ 0`, `v(c) ≥ 1 / (p - 1)`, that is,
`‖c‖ ≤ p ^ (-1 / (p - 1))`, and `g(0) = 0`. If `exp (c g) = 1 + c H` with `H ∈ B`, where `exp` is
`expSubst`, then `g ∈ B`. 

### `expSubst_mem_of_pow_mem`

 Let `B = 𝒪[[T]]` (`IsSeriesGenerator B T`: `T = X + ⋯` and `B` is the ring of all integral
series in `T`), `m` prime to `p` and `g(0) = 0`. If `(exp g) ^ m ∈ B`, where `exp g` is
`expSubst g`, then `exp g ∈ B`. 
