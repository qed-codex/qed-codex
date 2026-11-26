---
{
  "module": "src/New/Derivatives/Vacuum/Divisibility.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/Divisibility.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/Divisibility.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Integrality and divisibility of the derivatives of standard data

This file bounds the valuations of the derivatives of the Taylor series of standard data along
homogeneous integral polynomials.

* Standard data of level `δ` at `p` (`standardData`): the span over the `p`-integral complex numbers
  (`embValRing`) of the translates of the integral vacuum by the points `x` for which `δ * x` is
  integral above `p`.
* `V.jetSeries a f`: the Taylor series at `0` of the theta function of `f`, with the variables
  scaled by `a`; the scale `P.jetScale s` is `periodFactor * areaScale / cmPeriod`.
* `jet R Q F`: the derivative `Q(∂) F` at `0`.
* The normal form (`HasNormalForm`): after scaling the variables by `ϖ`, an integral series times
  the exponential of a multiple of the coupling series of the pairs of partner places.
* `ιₚ`: the embedding of `ℂ` into `ℂ_[p]` that comes with `PadicPlace p`.

## Main definitions and results

* `New.Parameters.norm_jet_jetSeries_le_pow`: a lower bound for the valuations of the derivatives of
  the Taylor series of standard data along homogeneous integral polynomials.
* `New.Parameters.exists_hasNormalForm_jetSeries`: at a non-split prime the Taylor series of
  standard data of level one has the normal form.
* `New.Parameters.norm_jet_minorProd_jetSeries_le`: so its derivatives along products of minors have
  the predicted divisibility up to a loss of `card (P.Φ s) * N ^ 3 * (1 + Real.logb p (max (boxes κ
  N) 1))`, where `N = card n'`.
* `New.Parameters.norm_schurJet_jetSeries_le_of_charges`: the bound with removed columns and charges
  for the derivatives along the entries of the Schur matrices.



## Integrality of the derivatives of standard data at all primes

The theta function of standard data of level `δ`, taken at `conj δ * (areaScale / cmPeriod) * z`, is
a power of the product of copies of `θ` along a resolution of the identity times an integral series
in copies of the parameter.


### `norm_jet_jetSeries_le_one`

 **Integrality of the derivatives.** Let `E = P.E s` be the cyclotomic extension at level `s` of
`K = P.K = ℚ(√-d)`, and `V` a hermitian space over `E` with all signs `+1` and the identity matrix
as adelic point (`IsStd`). Standard data of level `δ ≠ 0` at `p` (`standardData`) are the
combinations, with coefficients in the ring `embValRing` of complex numbers that are integral in
`ℂ_[p]`, of the translates of the integral vacuum in `𝒮 V` by the adelic points `x` such that
`δ * x` is integral above `p`. Let `f` be such data and let `F` be the Taylor series at `0` of the
theta function of `f` at `conj δ * d * jetScale * z`. For a polynomial `Q` with coefficients in
`embValRing`, in variables indexed by (infinite place of `E`, coordinate), the derivative `Q(∂) F`
at `0` (`jet`) has norm at most one in `ℂ_[p]`. 

### `norm_jet_jetSeries_le_pow`

 **Integrality at all primes.** Let `V` be a standard hermitian space over `E = P.E s`, and let
`f` be standard data of level `δ ≠ 0` at `p` on it (`standardData V δ`): a `p`-integral combination
of the translates of the integral vacuum by the points that `δ` makes integral above `p`. Let
`jetScale = periodFactor * √(2π / √d) / Ω₀`, where `P.K = ℚ(√-d)`, `Ω₀ 𝓞_K` is the lattice of its CM
curve and `periodFactor` is a normalising constant attached to `E`. Let `Q` be a homogeneous
polynomial of degree `l` with `p`-integral coefficients (in `embValRing`). Then the derivative
`Q(∂)` at `0` (`jet`) of the Taylor series (`jetSeries`) of the theta function of `f` at
`c * jetScale * z` has valuation in `ℂ_[p]` at least `l` times that of `c / (conj δ * d)`. 


## The normal form and the divisibility of standard data

At a non-split prime, which is automatically prime to `q₁`, the Taylor series of standard data of
level one is a product of copies of `θ` along a resolution of the identity that is integral above
the prime, times an integral series, so it has the normal form. Scaling by an integral number keeps
the normal form, and the count of the divisibility of series in normal form applies to it.


### `isIntegralAbove_of_finiteImage_mem`

 Let `α = P.α s` be the finite idele of `E = P.E s` that makes the integral adeles self-dual in
the construction of the Weil representation; the product of `α` and the integer `P.q₁ s` is integral
at every place. Let `p` be a prime that does not divide `P.q₁ s`, and `y` a vector over `E`. If all
coordinates of the adelic vector `finiteImage y = α⁻¹ y` are integral at the places above `p`, then
so are all coordinates of `y`. 

### `exists_hasNormalForm_jetSeries`

 **Normal form at a non-split prime.** Let `V` be a standard hermitian space over the cyclotomic
extension `E = P.E s` of `ℚ(√-d)` (`IsStd`: all signs are `+1` and the adelic point is the identity
matrix), and let `p` be non-split: the character `chiK` of `ℚ(√-d)` is not `1` at `p`. Let `f` be
standard data of level one, a `p`-integral combination of the translates of the integral vacuum by
points integral above `p`, and let `c` be `p`-integral. With
`jetScale = periodFactor * √(2π / √d) / Ω₀` (`Ω₀` the CM period, `periodFactor` a normalising
constant), let `F` be the Taylor series in `ℂ_[p]` of the theta function of `f` at
`c * jetScale * z`, in the variables `z_(τ,i)` (place, coordinate). Then `F` has the normal form
(`HasNormalForm`) `F(ϖ z) = W exp (ϖ ^ (p + 1) / p * ∑_e ∑_j l e j * Γ_e ^ p ^ j)`: the series `W`
has coefficients in the valuation ring `valRingCp p` of `ℂ_[p]`, as are all `l e j`. Here `e` runs
over `partnerExponents P.d p` (`e` odd, or any `e` if `p = d`), the coupling `Γ_e` is the sum of all
`z_(τ,i) ^ p ^ e * z_(τ',i)` with `τ' = P.partner s p e τ` the place `τ` moved by the class of
`-p ^ e`, and `ϖ` has valuation `varpiValuation P.d p`, which is `1 / (p² - 1)` if `p` is inert and
`1 / (2 p - 2)` if `p = d`. 

### `norm_jet_minorProd_jetSeries_le`

 **Divisibility at non-split primes.** Let `f` be standard data of level one on the space of
`n' × n` matrices (`hom` of the spaces `stdSpace`, whose forms are sums of norms of coordinates).
Let `c` be `p`-integral and `F` the Taylor series in `ℂ_[p]` of the theta function of `f` at
`c * jetScale * z`, where `jetScale = periodFactor * √(2π / √d) / Ω₀` (`Ω₀` the CM period,
`periodFactor` a normalising constant); its variable `(τ, b, a)` is the entry `(b, a)` of the matrix
`z_τ`. Let `κ τ h` be the number of columns of height `h` of a diagram at the place `τ`, let `i'` be
standard fillings of these diagrams by elements of `n'` (`WeylIndex`) and `y τ` integral matrices
with rows indexed by `n`. For a column of height `h < N = card n'`, take the minor of `z_τ y_τ` on
the rows that `i'` puts into the column and on the first `h` columns of `y_τ`; `minorProd i' y` is
the product of these minors. The derivative of `F` along it has valuation at least `D` less
`f₀ * N ^ 3 * (1 + log_p max (B, 1))`, where `f₀` is the number of infinite places and
`B = boxes κ N` the number of boxes in columns of height below `N`. Here `D = predictedDivisibility`
is `v ∑_e ∑_τ ((a_τ / p ^ e - a_τ' - a'_τ')⁺ + (l_τ / p ^ e - l_τ')⁺ - a'_τ / p ^ e)`: among the
heights below `N`, `a_τ` counts the columns of height one at `τ`, `a'_τ` the others and `l_τ` their
boxes; `τ'` is the place `-p ^ e τ`, `v = piPrimeValuation P.d p`, and `e` runs over the odd numbers
(all `e ≥ 1` if `p = d`). If `p = d`, half of `∑_τ (min (a_τ, a_τ' + a'_τ') + a'_τ + min (l_τ,
l_τ'))`, with `e = 0`, is subtracted from it. 

### `norm_schurJet_jetSeries_le_of_charges`

 **Divisibility of Schur entries at a non-split prime `p`.** Let `f` be standard data of level
one on the space `Hom(stdSpace n, stdSpace n')` of `n' × n` matrices, and `c` a `p`-integral number.
Let `F` be the Taylor series of the theta function of `f` at `c * jetScale * z`, where
`jetScale = periodFactor * √(2π / √d) / Ω₀` (`Ω₀` the CM period, `periodFactor` a normalising
constant); its variable `(τ, b, a)` is the entry `(b, a)` of the matrix `z_τ`. The Schur matrix of
the diagrams `κ` is the matrix of the map of Weyl modules of shape `κ` that the family `z` induces,
in the bases of chosen standard fillings; `schurJet κ F i' i` is the derivative at `0` of `F` along
the polynomial at its entry `(i', i)`. Let `κ` fit the ranks.

Remove the columns of height one at the places of `erasedPlaces`, and give charges
`p ^ chargeExp τ h b` (place, height, row) such that, for each `e` in `partnerExponents P.d p` with
partner `τ' = -p ^ e τ` of `τ`, each row `b` and each height `h`: if `τ ∈ erasedPlaces`, or `h = 1`
and `τ' ∈ erasedPlaces`, then `chargeExp τ 1 b` or `chargeExp τ' h b` is nonzero
(`IsChargeExponent`). Let `N = card n'` and `B` the number of boxes of `κ` in columns of height
below `N`. Then the sum `fillingCharge chargeExp i'` of the exponents over the boxes of the filling
`i'`, plus the valuation of the derivative, is at least the predicted divisibility of the remaining
diagrams, plus the gain `gammaPrime P.d p` for each removed box among these `B`, less
`f₀ * N ^ 3 * (1 + log_p max (B, 1))`, where `f₀` is the number of infinite places. 
