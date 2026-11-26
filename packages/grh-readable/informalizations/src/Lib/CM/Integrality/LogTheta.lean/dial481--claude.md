---
{
  "module": "src/Lib/CM/Integrality/LogTheta.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/CM/Integrality/LogTheta.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/CM/Integrality/LogTheta.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The logarithm of the theta function of a CM lattice and the integral group law

For a CM lattice, `g = -log θ` is the power series of the negative logarithm of its theta function,
read in `ℂ_p`. The file proves integrality statements for `g` and its rescalings; `expSubst f` is
the exponential series evaluated at a series `f` without constant term.

The integrality statements about the ring `𝒪[[y]]` assume that `d` is a prime congruent to `7`
modulo `8` (`PrimeSevenModEight d`). The main imported notions are the following.

* `C.θ`: the translate of the sigma function `C.σ` of the lattice `Λ` by the two-torsion point `t`,
  twisted and normalised to `θ(0) = 1`.
* `C.translatedX` and `C.translatedY`: the coordinates `x(z) = ℘(z + t) - ℘(t)` and
  `y(z) = (℘'(z + t) - a₁ x(z)) / 2` on the cubic `y² + a₁ x y = x³ + x` of the lattice; `y` is a
  parameter at the origin.
* `taylorVia ιₚ f`: the Taylor series of `f` at `0`, read in `ℂ_p` through the place `ιₚ`.
* `C.integralSeriesRing`: the ring `𝒪[[y]]` of integral power series in the series of `y`.
* `normPairClosure d`: the closure in `ℂ_p²` of the set of pairs `(α, α ᾱ)`, for integers `α` of
  `K = ℚ(√-d)`.

## Main definitions and results

* `New.CMLattice.derivative_derivative_negLogTheta`: `g'' = g''(0) + x`.
* `New.CMLattice.rescale_translatedY_mem_of_mem_normPairClosure`,
  `New.CMLattice.expSubst_sub_rescale_mem`: for a limit `(δ, s)` of pairs `(α, α ᾱ)` with `α` an
  integer of `K`, the series `y(δ z)` and `exp (s g(z) - g(δ z))` lie in `𝒪[[y]]`.
* `New.CMLattice.norm_sqrt_mul_coeff_two_negLogTheta_le_one`: `√-d g''(0)` is integral.
* `New.CMLattice.multiSeriesRing`: for linear forms `μ_i`, the ring `𝒪[[y(μ_i z)]]` of integral
  power series in the series `y(μ_i z)`.
* `New.CMLattice.translatedY_add_mem_multiSeriesRing`: the group law is integral.

## Relation to the literature

Known result: the second logarithmic derivative of a theta function is a Weierstrass function up to
a constant. Moreover `θ(α z) / θ(z) ^ (α ᾱ)` is a unit on the formal group.

Known result: the formal group law of a Weierstrass curve has integral coefficients. Source:
Silverman, The Arithmetic of Elliptic Curves, IV.1 and IV.2.



## The logarithm of the theta function

The addition formula for `θ`, differentiated twice, gives `g'' = g''(0) + x`.


### `continuous_rescale`

 The series `f(a z)` depends continuously on `a`, coefficient by coefficient. 

### `continuous_expSubst_smul`

 For a series `g` without constant term, `exp (s g)` depends continuously on `s`. 

### `IsSeriesGenerator.isClosed`

 If the subring `B` is the ring `𝒪[[T]]` of integral power series in `T`, then it is closed
under coefficientwise limits. 

### `coeff_two_subst`

 If `T(0) = 0`, then the coefficient of `X²` in `f(T)` is `f₁ T₂ + f₂ T₁²`, where `f_n` and
`T_n` are the coefficients of `X ^ n` in `f` and `T`. 

### `IsSeriesGenerator.norm_coeff_two_le_one`

 If an element `f` of the ring `B = 𝒪[[T]]` of integral power series in `T = X + ⋯` has no
linear term, then its coefficient of `X²` is its coefficient of `T²`, so it is integral. 

### `expSubst_mul_expSubst_neg_eq_one`

 For a series `g` without constant term, `exp g * exp (-g) = 1`. 

### `expSubst_natCast_smul_eq_pow`

 For a series `g` without constant term and a natural number `n`, `exp (n g) = (exp g) ^ n`. 

### `deriv_theta_zero`

 The derivative of the even function `θ` vanishes at `0`. 

### `deriv_theta_sq`

 Let `Λ` be the lattice of `C`, `t` its 2-torsion point and `θ` its theta function. For
`z + t ∉ Λ`, we have `θ'(z)² = θ(z) θ''(z) + (−θ''(0) + x(z)) θ(z)²`, where `x(z) = ℘(z + t) − ℘(t)`
is `translatedX`. This is the equation `g'' = g''(0) + x(z)` for `g = -log θ`, multiplied by `θ²`;
here `g''(0) = -θ''(0)`. 

### `negLogTheta`

 The power series `g = -log θ` with `g(0) = 0`: the negative logarithm of the Taylor series of
`θ`, read in `ℂ_p`. 

### `coeff_one_negLogTheta`

 The linear coefficient of `g = -log θ` vanishes, since `θ'(0) = 0`. 

### `derivative_taylorVia_theta_sq`

 The Taylor series `θ` satisfies `θ'² = θ θ'' + (g''(0) + x) θ²`, with `g''(0) = -θ''(0)` and
`x = translatedX`. 

### `derivative_derivative_negLogTheta`

 Let `ιₚ : ℂ → ℂ_[p]` be a `p`-adic place. Let `g = -log θ` be the negative logarithm, normalised
by `g(0) = 0`, of the Taylor series at `0` of the theta function `θ` of `C`, read in `ℂ_[p]`. Let
`x` be the Taylor series of `translatedX`, `x(z) = ℘(z + t) − ℘(t)` for the 2-torsion point `t`,
with coefficients mapped to `ℂ_[p]` by `ιₚ`. Then `g'' = g''(0) + x` as power series, where the
constant `g''(0)` is twice the second coefficient of `g`. 

### `expSubst_sub_rescale_eq`

 The identity `exp (s g(z) - g(δ z)) = exp (s g(z)) θ(δ z)` for `g = -log θ`, where
`exp f = expSubst f` is the exponential series evaluated at `f`. 

### `expSubst_smul_negLogTheta_sub_rescale_eq`

 If `θ(δ z) = θ(z) ^ n u`, then `exp (n g(z) - g(δ z)) = u` for `g = -log θ`, where
`exp f = expSubst f` is the exponential series evaluated at `f`. 

### `X_sq_dvd_taylorVia_translatedX`

 The Taylor series at `0` of `x = C.translatedX`, i.e. of `℘(z + t) − ℘(t)`, with `ιₚ` applied to
its coefficients, is divisible by `X ^ 2` in `ℂ_p⟦X⟧`: it has no terms of degree below two. 

### `coeff_two_taylorVia_translatedX`

 The coefficient of `z²` in the series of `x = translatedX` in `ℂ_p` is `1`. 

### `expSubst_sub_rescale_mem_of_mem_quadInt`

 For an integer `a` of `K = ℚ(√-d)` and `g = -log θ`, the series
`exp (a ā g(z) - g(a z)) = θ(a z) / θ(z) ^ (a ā)` lies in `integralSeriesRing`, the ring `𝒪[[y]]` of
integral series in `y = translatedY`. 

### `mem_integralSeriesRing_of_mem_normPairClosure`

 Let `F δ s` be a series that depends continuously on `(δ, s)` and lies in `integralSeriesRing`,
the ring `𝒪[[y]]` of integral series in `y = translatedY`, at the pairs `(α, α ᾱ)` in `ℂ_p²`, with
`α` an integer of `K = ℚ(√-d)`. Then it lies in this ring at every limit of these pairs. 

### `rescale_translatedY_mem_of_mem_normPairClosure`

 For `d` a prime `≡ 7 (mod 8)`, a `p`-adic place `ιₚ`, and `(δ, s)` in `normPairClosure d`, the
closure in `ℂ_p²` of the pairs `ιₚ(α, α ᾱ)` with `α` an integer of `K = ℚ(√-d)`: let `y(X)` be the
`ιₚ`-Taylor series at `0` of `y = C.translatedY`, where `y(z) = ½(℘′(z + t) − a₁x(z))` and
`x(z) = ℘(z + t) − ℘(t)`. Then the rescaled series `y(δ X)` lies in `C.integralSeriesRing`, the ring
`𝒪[[y]]` of integral power series in `y(X)`. 

### `expSubst_sub_rescale_mem`

 For `d` a prime `≡ 7 (mod 8)`, a `p`-adic place `ιₚ`, and `(δ, s)` in `normPairClosure d`, the
closure in `ℂ_p²` of the pairs `ιₚ(α, α ᾱ)` with `α` an integer of `K = ℚ(√-d)`: let
`g = C.negLogTheta` be the series `-log θ` over `ℂ_p` with `g(0) = 0`. Then `exp (s g(X) - g(δ X))`
lies in `C.integralSeriesRing`. This is the ring `𝒪[[y]]` of integral power series in the
`ιₚ`-Taylor series of `y = C.translatedY`, where `y(z) = ½(℘′(z + t) − a₁x(z))` and
`x(z) = ℘(z + t) − ℘(t)`. 

### `mul_coeff_two_negLogTheta_mem_valRingCp`

 For an integer `a` of `K = ℚ(√-d)` and `g = -log θ`, the number `a (ā - a) g''(0) / 2` is
integral in `ℂ_p`: it is the coefficient of `y²` in `exp (a ā g(z) - g(a z)) ∈ 𝒪[[y]]`. Here
`g''(0) / 2` is the second coefficient of `g`. 

### `norm_sqrt_mul_coeff_two_negLogTheta_le_one`

 Let `d` be a prime that is 7 modulo 8 and `ιₚ : ℂ → ℂ_[p]` a `p`-adic place. Let `g = -log θ` be
the negative logarithm, with `g(0) = 0`, of the Taylor series at `0` of the theta function `θ` of
`C`, read in `ℂ_[p]`. Then, for `√-d = i √d`, the number `ιₚ(√-d) g''(0)` has norm at most `1` in
`ℂ_[p]`; here `g''(0)` is twice the second coefficient of `g`. 

 ## The constant coefficient in one variable 

### `mvPowerSeries_constantCoeff_eq`

 The constant coefficient of a series in one variable, read as a multivariate series, is its
constant coefficient as a power series. 


## Integral expansions in several variables and the group law

Euler's addition formula gives `y(z₀ + z₁)` as a polynomial in `a₁`, `x(z_i)`, `y(z_i)` and the
inverse of the unit `1 - x(z₀) x(z₁)`.


### `hasSubst_linearSeries`

 The linear form `linearSeries c = ∑ x, c x • X x` has constant term zero, so it can be
substituted into a power series. 

### `pderiv_subst_linearSeries`

 The chain rule for a series `g` at a linear form: the partial derivative of `g(c z)` in the
variable `z_x` is `c x` times `g'(c z)`. 

### `rescale_subst_linearSeries_eq_mul`

 Scaling the variables of `g(c z)` scales the coefficients of the linear form. 

### `eulerAddition`

 Euler's formula for the `y`-coordinate of the sum of two points `(x₀, y₀)` and `(x₁, y₁)` on
the cubic `y² + a x y = x³ + x` with origin `(0, 0)`; here `u` stands for `1 / (1 - x₀ x₁)`.
The factor `1 + x₀ x₁ u` then equals `u`; in this form the value at `x₀ = y₀ = 0` is `y₁` for every
`u`. 

### `eulerAddition_mem`

 A subring that contains `a`, the coordinates `x₀`, `y₀`, `x₁`, `y₁` and `u` contains the value
of Euler's formula at them. 

### `derivation_eulerAddition`

 Euler's formula is constant when the two points move on the cubic in opposite directions along
the invariant vector field `x' = 2 y + a x`, `y' = 1 + 3 x² - a y`: a derivation `D` with `D a = 0`
that acts in this way on two points of the cubic kills Euler's formula, if
`u (1 - x₀ x₁) = 1`. 

### `constantCoeff_translatedY_subst_linearSeries`

 For a linear form `c z` (`linearSeries c`), the series `y(c z)` has constant term zero; here
`y(z)` is the Taylor series of `translatedY` at the origin, read in `ℂ_[p]` through `ιₚ`. 

### `hasSubst_translatedY_subst`

 The family of series `y(μ_i z)` can be substituted into a power series in the variables indexed
by `I`; here `y` is the Taylor series of `translatedY` at the origin, read in `ℂ_[p]` through
`ιₚ`, and `linearSeries (μ i)` is the linear form `μ_i z`. 

### `multiSeriesRing`

 The ring `𝒪[[y(μ_i z)]]` of integral power series in the series `y(μ_i z)`, for a family of
linear forms `μ_i` and `y = translatedY`: the image of the series over `valRingCp p`, mapped into
`ℂ_[p]` by `seriesToCp`, under the substitution of the `y(μ_i z)`. 

### `mem_multiSeriesRing_iff`

 A series lies in `𝒪[[y(μ_i z)]]` if and only if it is `G(y(μ_i z))` for a series `G` with
coefficients in `valRingCp p`, the ring of integers of `ℂ_[p]`; `seriesToCp` is the inclusion of
these series into those over `ℂ_[p]`. 

### `constantCoeff_subst_translatedY_subst`

 Substituting the series `y(μ_i z)`, for `y = translatedY`, into a series `G` does not change its
constant term. 

### `exists_mul_eq_one_of_mem_multiSeriesRing`

 An element of `𝒪[[y(μ_i z)]]` whose constant term has norm one is a unit of that ring. 

### `taylorVia_curve_eq_subst_linearSeries`

 The series `x(c z)` and `y(c z)`, for the Taylor series `x` of `translatedX` and `y` of
`translatedY`, satisfy the equation `y² + a₁ x y = x³ + x` of the cubic. 

### `pderiv_translatedX_subst_linearSeries`

 The equation `x' = 2 y + a₁ x`, read at a linear form: the partial derivative of `x(c z)` in
the variable `z_j` is `c j` times `2 y(c z) + a₁ x(c z)`. 

### `pderiv_translatedY_subst_linearSeries`

 The equation `y' = 1 + 3 x² - a₁ y`, read at a linear form: the partial derivative of `y(c z)`
in the variable `z_j` is `c j` times `1 + 3 x(c z)² - a₁ y(c z)`. 

### `subst_mem_multiSeriesRing`

 An element `v` of `𝒪[[y]]` (the ring `integralSeriesRing` of the lattice), taken at the linear
form `μ_i z` (`linearSeries (μ i)`), lies in the ring `𝒪[[y(μ_j z)]]` of all the forms. The
hypothesis `PrimeSevenModEight d` says that `d` is a prime that is 7 modulo 8. 

### `eq_of_pderiv_sub_eq_of_rescale_eq`

 A series in two variables is determined by its image under `∂₀ - ∂₁` and its value at
`z₀ = 0`. 

### `translatedY_add_mem_multiSeriesRing`

 Let `d` be a prime that is 7 modulo 8 and `ιₚ : ℂ → ℂ_[p]` a `p`-adic place. Let `y(z)` be the
Taylor series at `0` of `translatedY`, `y(z) = ½(℘′(z + t) − a₁x(z))` with `x(z) = ℘(z + t) − ℘(t)`,
with coefficients mapped to `ℂ_[p]` by `ιₚ`. The group law is integral: `y(z₀ + z₁)` lies in
`𝒪[[y(z₀), y(z₁)]]`, the ring `multiSeriesRing` of integral power series in `y(z₀)` and `y(z₁)`;
here `linearSeries 1` is `z₀ + z₁` and the rows of the matrix are the forms `z₀` and `z₁`. This is
the integrality of the formal group law of a Weierstrass curve (Silverman, The Arithmetic of
Elliptic Curves, IV.1 and IV.2) for the cubic of `C`, proved by Euler's addition formula. 
