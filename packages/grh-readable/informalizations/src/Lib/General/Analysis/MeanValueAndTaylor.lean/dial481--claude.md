---
{
  "module": "src/Lib/General/Analysis/MeanValueAndTaylor.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Analysis/MeanValueAndTaylor.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Analysis/MeanValueAndTaylor.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Circle means, Taylor series at zero, a power bound, and smooth matrix operations

This file proves mean value facts for circle averages and a halving criterion for upper bounds. It
develops the algebra of Taylor series at 0 of analytic functions and proves an elementary bound of
x^l by a factorial and exponentials. It also gives smoothness rules for matrix operations and
extends analytic germs to globally smooth maps.

The imported notion `New.taylorAtZero f` is the formal power series whose `n`-th coefficient is
`iteratedDeriv n f 0 / n !`, the Taylor series of `f : ℂ → ℂ` at 0.

## Main definitions and results

* `New.taylorAtZero_mul`, `New.taylorAtZero_comp_mul`, `New.eq_of_taylorAtZero_eq`: Taylor series
  at 0 of products and of `z ↦ f (a * z)`; such a series determines an entire function.
* `New.integral_eq_of_circle_mean`: an integral is unchanged when the integrand is replaced by its
  mean over a family of measure preserving maps indexed by the circle `ℝ / ℤ`.
* `New.integral_comp_toCircle_eq_apply_zero`: the mean value property over the unit circle of a
  function holomorphic on the closed unit disc, for the Haar probability measure of `ℝ / ℤ`.
* `New.le_of_halving`: let `c ≥ 0`. A function bounded above is at most `c` if each of its bounds
  can be halved at the points where it exceeds `c`.
* `New.exists_contDiff_eventuallyEq`: a map on a finite-dimensional space that is of class `C^ω`
  at a point agrees near it with a globally smooth map.

## Relation to the literature

The results of this file include the mean value property of holomorphic functions and the fact that
an entire function is determined by its Taylor series at 0.


 ## Circle averages, the mean value property and a halving criterion for upper bounds 

### `New.integral_eq_of_circle_mean`

 Averaging over a family of measure preserving maps. Let `μ` be s-finite. Let `T θ`, for `θ` in
`ℝ / ℤ`, be jointly measurable maps that preserve `μ`. If `f` is integrable and the mean of
`f (T θ x)` over `θ` is `g x` for every `x`, then `f` and `g` have the same integral. 

### `New.integral_comp_toCircle_eq_apply_zero`

 The mean value property: the mean over the unit circle of a function holomorphic on the closed
unit disc is its value at the centre. 

### `New.le_of_halving`

 Halving criterion: let `f` be a real function bounded above and `c ≥ 0`. If for every upper
bound `M ≥ 0` of `f` each value is at most `M / 2` or at most `c`, then `f ≤ c`. 


## Algebra of one-variable Taylor series at 0

For functions analytic at 0 the Taylor series `New.taylorAtZero` respects sums, products, powers and
polynomial expressions (`New.taylorAtZero_add`, `New.taylorAtZero_mul`, `New.taylorAtZero_pow`,
`New.taylorAtZero_eval`); by `New.taylorAtZero_comp_mul` the series of z ↦ f (a z) is the series of
f rescaled by a, and `New.eq_of_taylorAtZero_eq` says that the Taylor series at 0 determines an
entire function.


### `taylorAtZero_comp_mul`

 The Taylor series `taylorAtZero` at 0 of `z ↦ f (a * z)` is that of `f` with the `n`-th
coefficient multiplied by `a ^ n` (`PowerSeries.rescale a`). No analyticity is needed. 

### `eq_of_taylorAtZero_eq`

 Two entire functions with the same Taylor series at 0 are equal. 

### `taylorAtZero_add`

 The Taylor series at 0 of a sum of two functions analytic at 0 is the sum of their Taylor
series. 

### `taylorAtZero_mul`

 The Taylor series at 0 of a product of two functions analytic at 0 is the product of their
Taylor series. 

### `taylorAtZero_eval`

 Let `f` be analytic at 0 and `P` a polynomial. Then the Taylor series of `P ∘ f` is `P`
evaluated at the Taylor series of `f`. 

### `taylorAtZero_pow`

 The Taylor series at 0 of `f ^ n` is the `n`-th power of that of `f`, for `f` analytic
at 0. 

 ## A bound of x^l by a factorial and an exponential 

### `New.pow_le_exp_log_factorial_add`

 For a natural number `l`, a real `x ≥ 0` and a real `v`:
`x ^ l ≤ exp (log l! + l v + x / exp v)`. This is `t ^ l / l! ≤ exp t` at `t = x / exp v`. 


## Smoothness of matrix operations and extension of analytic germs

Matrices carry the elementwise sup norm. The exponent `N` is any order of smoothness, finite, `∞`
or analytic (`ω`).


### `exists_contDiff_eventuallyEq`

 A map from a finite-dimensional real normed space to a real normed space that is of class
`C^ω` at `x` (analytic, if the target is complete) agrees near `x` with a globally smooth map. 

### `contDiff_conj`

 Complex conjugation is smooth over `ℝ`, of every order `N`. 

### `contDiff_matrix_mul`

 Matrix multiplication of complex matrices is smooth over `ℝ` for the elementwise norm. 

### `contDiff_conjTranspose`

 The conjugate transpose of complex matrices is smooth over `ℝ` for the elementwise norm. 

### `contDiff_matrix_exp`

 The exponential of complex square matrices is smooth over `ℝ` for the elementwise norm. 
