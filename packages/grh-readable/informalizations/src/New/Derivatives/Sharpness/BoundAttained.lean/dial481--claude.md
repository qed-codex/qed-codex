---
{
  "module": "src/New/Derivatives/Sharpness/BoundAttained.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Sharpness/BoundAttained.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Sharpness/BoundAttained.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Sharpness of the valuation bound

* `New.Data.exists_le_norm_coeff_indicatorDatum`: the reduction to the curve. Some Taylor
  coefficient of degree `l` of an indicator datum, times the factor `vacuumScale ^ 12` of the
  integral vacuum, has valuation at most `val₁₂(l) + v(M ^ (12 f) c₀)`, where `c₀` is a value of the
  integral vacuum.
* `New.Data.exists_rpow_neg_localPrimeSumTotal_le_norm_coeff`: for degrees `l` between the weights
  `κ` and `κ + x ^ 42`, with `x = D.x`, there is one number `t ≠ 0` with small conjugates such that
  at every prime some Taylor coefficient of degree `l` of an indicator datum, times `∏ l!` and the
  factor `vacuumScale ^ 12` of the integral vacuum, has valuation at most `S_p + v(t)`.

The theta product times monomials in the function `y` along the forms of a tight frame is the Taylor
series of a vector with integral values, and Fourier inversion expands that vector in translates of
the vacuum. Each translate is a sum of indicator data times roots of unity.

Notions from other files:
* A tight frame of length `M` with multiplicities `c` is a family `w` of lattice vectors with
  `∑ c i Φ_σ(w i) conj(Φ_τ(w i)) = M δ_{σ τ}` (`New.IsTightFrame`). Here `M = D.M`.
* `val_n(l) ≤ r` (`CMLattice.LeastValLE`) says that some coefficient of degree `l` in some product
  over `n` copies of `H Θ` has valuation at most `r`. Here `Θ` is the theta product of the frame and
  `H` is an integral series in the functions `y` along the forms of the frame.
* `intVacuum V` is the vacuum `V.vacElem` times `vacuumScale ^ n`, where `n` is the rank of `V`.
* `π_M = D.piM` is the conjugate of the integer `π̄_M = D.piMBar` of `K`, of norm `M`.
* `D.localPrimeSumTotal p` is the forced divisibility `S_p` at the weights of `D`, the sum of
  `D.localPrimeSum p (D.weight τ) τ` over the infinite places `τ`.
* `α` is the finite idele of the Weil data of `D.E`, `𝔞₀ = E ∩ α Ô` its lattice, `finVec x` the
  adelic vector `(0, α x)` with zero part at infinity, and `D.f` the number of infinite places
  of `D.E`.

## Relation to the literature

Sharpness for one curve (slope `p / (p² - 1)`, attained in infinitely many degrees) is known in the
literature.

Related work: Bannai–Kobayashi, Algebraic theta functions and the p-adic interpolation of
Eisenstein–Kronecker numbers (arXiv v1), 2006; Bannai–Kobayashi–Yasuda, Radius of convergence of the
p-adic sigma function, 2017; Schneider–Teitelbaum, p-adic Fourier theory, 2001; Bannai–Kobayashi,
Integral structures on p-adic Fourier theory, 2016.


### `copyEmbedding`

 The embedding of the variables of one copy as the `b`-th of `k` copies. 

### `copyExponent`

 The exponent in `k` copies of the variables whose part in the `b`-th copy is `α b`. 

### `copyExponent_apply`

 The part of `copyExponent α` in the `b`-th copy is `α b`. 

### `coeff_prod_rename_copyEmbedding`

 The coefficient at `copyExponent α` of a product of series, each in the variables of its own
copy, is the product of the coefficients at the exponents `α b` of the copies. 

### `map_subst_linearSeries_copy`

 Substitute the linear form `∑ x, μ x • X_(x, b)` (`linearSeries`) in the variables of copy
`b` into the Taylor series of `f`, and apply `ιₚ : ℂ → ℂ_[p]` to the coefficients. The result is
the series `taylorVia ιₚ f` along the form `ιₚ ∘ μ` of one copy, renamed into copy `b`. 

### `norm_natCast_prod_eq_rpow_neg_sum`

 The `p`-adic norm of a product of nonzero natural numbers is `p` to minus the sum of their
valuations. 

### `twelveSpace`

 The hermitian space `Hom(E, E¹²)` of `12 × 1` matrices over `E = D.E`, where `E` and `E¹²` carry
the sum of the norms of the coordinates (`stdSpace`). The sign of a coordinate is the product of
the signs of its row and column, here always `+1` (`homSigns 1 1`). The vectors of this file lie
in `𝒮 D.twelveSpace`, the space of functions on adelic vectors that models the adelic Heisenberg
representation. 

### `twelveTaylor`

 The series `Space.jetSeries` of a vector `F` on `Hom(E, E¹²)` at the scale `a = π_M * jetScale`:
for `F` in the finite part it is the Taylor series at `0` of `z ↦ Θ_F(a z)`, where `Θ_F` is the
theta function `Space.entireTheta F`. Here `π_M` is the conjugate of `D.piMBar` and
`jetScale = periodFactor * areaScale / cmPeriod`, where `cmPeriod 𝓞_K` is the lattice of the curve
`P.cmCurve`, `areaScale = √(2π / √d)` for `d = P.d`, and
`periodFactor = vacuumRoot / chowlaSelbergUnit` is a constant of the field `D.E = P.E D.towerExp`,
the cyclotomic extension of `K` at the level `D.towerExp` of the tower. 

### `indicatorDatum`

 The vector on `Hom(E, E¹²)` whose part at infinity is the Gaussian `exp(-|x|² / 2)`
(`Fock.vacVector`), whose part at the places dividing `𝔪` is the indicator of the class `y₀` of
matrices over the residue ring `𝔪.ResidueRing = O_E/𝔪`, and which agrees with the vacuum
`Space.vacElem` at the other finite places. The three parts are put together by `modDatum`. 

### `exists_integral_isThetaFunction_twelveTaylor_eq`

 Let `D` be admissible data for the parameters `P`, with `K = P.K = ℚ(√-d)` and `E = D.E` the
cyclotomic extension `P.E D.towerExp` of `K`; `D.Φ` is the set of its infinite places `τ`. Let `w`
be a tight frame of length `M = D.M` with multiplicities `c`. Let
`μ_i(z) = periodFactor * ∑ conj(Φ_τ(w i)) z_τ` be its linear forms (`resolutionForms`, read through
an embedding `ιₚ : ℂ → ℂ_[p]`). Let `θ` be the theta function of the elliptic curve
`P.cmCurve = ℂ / cmPeriod 𝓞_K`, let `y(z) = ½(℘′(z + t) - a₁(℘(z + t) - ℘(t)))` for its point `t`
and coefficient `a₁` (`translatedY`), and `Θ = ∏ θ(μ_i z) ^ c i` (`thetaProd`).

If `3 e b i ≤ c i`, there is a vector `F` of `𝒮 D.twelveSpace`, the Heisenberg model of functions on
the adelic `12 × 1` matrices over `E`, such that
* the rescaled Taylor series `twelveTaylor F` of its theta function `Space.entireTheta F` is the
  product over twelve copies `b` of the variables of the series `∏ y(μ_i z) ^ e b i * Θ`;
* its values at the adelic vectors `finVec x = (0, α x)`, for `x` over the finite adeles `𝔸f E`, are
  integral at `ιₚ`;
* its theta function is fixed by the signed translations along `π_M 𝔞₀¹²` (`IsThetaFunction`). 

### `exists_norm_le_norm_indicatorDatum`

 Let `D` be admissible data for the parameters `P`, with CM field `E = D.E` over `K = P.K`, and
let `F` lie in `𝒮 D.twelveSpace`, the Heisenberg model of functions on the adelic `12 × 1` matrices
over `E`. Let `F` have integral values at the adelic vectors `finVec x = (0, α x)`, for `x` over the
finite adeles `𝔸f E` and `α` the finite idele of the Weil data of `E`. Let its theta function be
fixed by the signed translations along `π_M 𝔞₀¹²`. Let `𝔪 = (π_M)`. For every linear form `L` and
every vector `y` over `𝔸f E` there is a class `y₀` modulo `𝔪` such that the valuation of
`L (indicatorDatum 𝔪 y₀)` is at most that of `M ^ (12 f) L(F)` times the value of the vacuum at
`finVec y`. 

### `exists_le_norm_coeff_indicatorDatum`

 Reduction to the curve. Let `D` be admissible data for the parameters `P`, with CM field
`E = D.E = P.E D.towerExp`, whose `f = D.f` infinite places form `D.Φ`; valuations are taken at
`ιₚ : ℂ → ℂ_[p]`. Let `w` be a tight frame of length `M = D.M` with linear forms `μ_i`
(`resolutionForms`) and multiplicities `c i ≥ 3 |l|`. Suppose `val₁₂(l) ≤ r` (`LeastValLE`): some
coefficient of degree `l` in some product over twelve copies of the variables of series `H Θ` has
valuation at most `r`, where `Θ = ∏ θ(μ_i z) ^ c i` and each `H` is an integral series in the
`y(μ_i z)`, for the functions `θ` and `y` of the elliptic curve `P.cmCurve`. Then for some class
`y₀` modulo `𝔪 = (π_M)`, `π_M = D.piM`, some coefficient of degree `l` of the rescaled Taylor series
(`twelveTaylor`) of the theta function of `indicatorDatum 𝔪 y₀`, times `vacuumScale ^ 12`, has
valuation at most `r + v(M ^ (12 f) c₀)`.

The vacuum is the Gaussian times the twisted indicator of the standard lattice, on the adelic
`12 × 1` matrices over `E` (`twelveSpace`); `indicatorDatum 𝔪 y₀` is the vacuum with its part at the
places dividing `𝔪` replaced by the indicator of `y₀`. The integral vacuum `intVacuum` is the vacuum
times `vacuumScale ^ 12`, a constant that makes its values integral, and `c₀` is its value at the
adelic vector `finVec y` with zero part at infinity. 

### `norm_map_mul_intVacuum_le`

 Let `D` be admissible data for the parameters `P`, with CM field `E = D.E`, whose `f = D.f`
infinite places form `D.Φ`. For degrees `l ≤ κ + x ^ 42` at the weights `κ = D.weight`, all
conjugates of `t = M ^ (12 f) c₀ ∏ B_τ ^ 2` are at most `exp (f m b / k)` in absolute value. Here
`x`, `b` are scales and `m`, `r` ranks of `D`, with `k = D.k = r + 1 - m` and `M = D.M`. Further
`B_τ = D.lossProduct (l τ) = (l⁻ + 1) ⋯ (l⁻ + n)` with `n = D.lossFactorCount = ⌈6 b / k⌉` and
`l⁻ = (l τ - n)₊`. The number `c₀` is the value at `finVec y`, an adelic vector with zero part at
infinity, of the integral vacuum `intVacuum`: the Gaussian times the twisted indicator of the
standard lattice on the adelic `12 × 1` matrices over `E` (`twelveSpace`), multiplied by the
constant `vacuumScale ^ 12` that makes its values integral. 

### `exists_rpow_neg_localPrimeSumTotal_le_norm_coeff`

 Sharpness. Let `D` be admissible data for the parameters `P`, with `K = ℚ(√-d)` for the prime
`d = P.d` and `E = D.E = P.E D.towerExp` the extension of `K` by the roots of unity of order
`q₁ = D.q₁`. For degrees `l` with `κ ≤ l ≤ κ + x ^ 42` at the weights `κ = D.weight` there is a
number `t ≠ 0` with all conjugates at most `exp (f m b / k)` such that, at every prime `p` and
embedding `ιₚ : ℂ → ℂ_[p]`, for some exponent `γ` of degree `l` and some class `y₀` modulo
`𝔪 = (π_M)` the valuation of the coefficient at `γ` of `twelveTaylor (indicatorDatum 𝔪 y₀)`, times
`vacuumScale ^ 12 ∏ l!`, is at most `S_p + v(t)`.

The numbers `x`, `b` are scales and `m`, `r` ranks of `D`, `k = r + 1 - m`, and `π_M = D.piM` is an
integer of `K` of norm `D.M`. 
