---
{
  "module": "src/New/Derivatives/Vacuum/IntegralVacuum.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/IntegralVacuum.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/IntegralVacuum.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The integral vacuum θ°: integrality and bounds of its values, standard data at p

Fix the parameters `P`, the field `E = P.E s` and a hermitian space `V` of rank `n` over it. The
integral vacuum θ° = `New.Parameters.intVacuum` is the vacuum scaled by `vacuumScale ^ n`. The
factor `New.Parameters.vacuumScale` is provided by
`New.Parameters.exists_mul_vacElem_integral_bounded` for the standard space of rank one. To obtain
it, a multiple of the vacuum is written as a sum of translates of one vector. For a standard space,
the values of θ° at the points `New.finVec x` are integral at every prime, have bounded conjugates,
and are not all zero. A vector `f` is read as the function `f y = θ(ϱ(y) f)` of adelic vectors `y`.

## Main definitions and results

* `New.Parameters.IsThetaProduct`, `New.Parameters.exists_isThetaProduct`: a vector whose theta
  function is the product of theta functions of a CM lattice along the resolution of powers of `ζ`,
  that is, along the vectors `ζᵏ / q₁`, `k < q₁`, which form a tight frame of `E` over `K`.
* `New.Parameters.standardData V δ`: the module of standard data at a prime `p`. Its scalars are the
  complex numbers that the `p`-adic place sends to integers, and it is spanned by the translates
  `V.finHeisenbergOp x θ°`, for the `x` with `δ x` integral above `p`.
* `New.Parameters.norm_intVacuum_le_one`: the values of θ° at the points `New.finVec x` are integral
  at every prime.
* `New.Parameters.norm_ringEquiv_intVacuum_le`: their conjugates under the automorphisms of `ℂ` are
  bounded; `New.Parameters.norm_gal_intVacuum_le` is the case of automorphisms over `K`.
* `New.Parameters.norm_dataInner_self_le`: a bound for `f` at these points bounds its squared norm
  `New.Space.dataInner f f`, the mean of `|f y| ^ 2` over adelic vectors modulo rational ones.
* `New.Parameters.exists_isJetConjugate_translates`: the conjugates of the jets of the translates of
  one vector that generates the finite part.

Notions from other files:
* `New.Parameters`: The fixed parameters: a multiple `q₀` of `18480 = 16 · 3 · 5 · 7 · 11` and a
  prime `d` with `d ≡ q₀/2 - 1 mod q₀`.
* `New.Parameters.E`: The field E = K(ζ) obtained from K = ℚ(√-d) by adjoining a primitive root of
  unity ζ of order `P.q₁ s`.
* `New.Space`: a hermitian space with a point, given by a matrix J over E and x in GL_n(𝔸) with xᴴJx
  equal to the diagonal matrix of its signs at the infinite places and 1 at the finite places.
* `New.Space.vacElem`: The vacuum: the product of the Gaussian and a twisted indicator of a lattice,
  as an element of 𝒮(V).
* `New.Space.IsStd`: The space `V` is standard: all its signs are `+1` and its point is the identity
  matrix.


 ## The integral vacuum in rank one 

### `exists_norm_gal_torsion_value_le`

 The theta function `θ` of the CM lattice `cmCurve` (the lattice `Ω₀ 𝓞_K`, `Ω₀ = cmPeriod`) is
the translate of its sigma function by a point of order two, normalised to `θ 0 = 1`. The twisted
translate `twistedTranslate 1 u θ`, of degree one, is `z ↦ exp (-π (z ū + |u|² / 2) / A) θ (z + u)`,
with `A` the area of the lattice. For the torsion points `u = x Ω₀`, `x ∈ K`, the conjugates over
`K` of its values at `z = 0` are bounded. 

### `exists_smul_vac_eq_sum`

 Let `E` be a CM field with Weil data (the element `ȷ`, the idele `α` and the splitting character
that define the Weil representation), let `V` be standard and let `δ` be integral (in the finite
adelic integers `Ô E`) with `δ δ̄ = N ≠ 0`. Suppose that the theta functional `V.θ` takes the value
`1` at `F` and that `entireTheta F` is a theta function for `δ̄ 𝔞₀ⁿ`, that is, an entire function
fixed by the signed translations along `δ̄ 𝔞₀ⁿ`. Here `idealLattice E n = 𝔞₀ⁿ` is the lattice of
the rational vectors `γ` with `α⁻¹ γ` integral at all finite places. Then a nonzero multiple of the
vacuum is a sum of `N ^ (f n)` translates `finHeisenbergOp (a j) (ϱ(finVec b) F)`. Here `f` is the
number of infinite places, `n` the rank, `ϱ` the action of adelic vectors, and `finHeisenbergOp x`
is `ϱ(finVec x)` times the scalar `stdLattice.semichar x`. 

### `zetaCoord`

 The coordinate `-u† y ∈ K` of `y ∈ E` along the vector `u = ζᵏ / q₁` of the frame of powers of
`ζ`, that is minus the trace from `E` to `K` of `y * star ζᵏ`, divided by `q₁`. 

### `zetaCoord_smul`

 The coordinate along a vector of the frame commutes with multiplication by elements of `K`. 

### `zetaCoordThetaTranslate`

 The twisted translate of the theta function of the CM lattice `C` by `Ω` times the coordinate
of `y ∈ E` along the vector `ζᵏ / q₁` of the frame of powers of `ζ`. 

### `zetaLinearSeries`

 The linear form along the frame vector `ζᵏ / q₁` in the coordinate `j`, for the period `Ω` and
the scale `c`: the power series `Ω / q₁ / areaScale * c * ∑ w, conj (Φ w ζᵏ) * z (w, j)` in
variables `z` indexed by infinite places of `E` and coordinates. Here `areaScale = √(2π / √d)`,
`Φ w` is the complex embedding chosen at the place `w`, and `linearSeries a` is `∑ y, a y * z y`. 

### `IsThetaProduct`

 The vector `F` is the product of copies of the theta function of `C` along the frame of the
`ζᵏ / q₁`, each taken `q₁` times, in every coordinate. The period `Ω` scales the coordinates along
the frame to complex numbers, and the level `e` gives the lattice `q₁ e 𝔞₀ⁿ` of periods, where
`𝔞₀ⁿ = idealLattice E n` consists of the rational vectors `γ` with `α⁻¹ γ` integral, `α` being the
idele of the Weil data and `q₁` the order of `ζ`. 

### `IsThetaProduct.mem_finitePart`

 The vector lies in the finite part, the span of the translates of the vacuum by the operators
  `finHeisenbergOp`. 

### `IsThetaProduct.theta_translate`

 The theta value of the translate by a rational vector `γ` is a product of values at `0` of
  twisted translates of the theta function of `C`. Here `finiteImage γ` is the finite adelic vector
  `α⁻¹ γ`, with `α` the idele of the Weil data. 

### `IsThetaProduct.jetSeries_translate`

 The series of jets `jetSeries c` of that translate (for a standard space, the Taylor series at
  `0` of its theta function at the scale `c`) is a product of Taylor series `taylorAtZero` at `0` of
  functions of one variable, each composed with a linear form. 

### `IsThetaProduct.norm_le_one`

 The values at finite points are integral at every prime `p`, for every `p`-adic place of `ℂ`
  (a ring homomorphism `ιₚ` from `ℂ` to `ℂ_[p]`). 

### `IsThetaProduct.isThetaFunction`

 The theta function of the vector is a theta function for `q₁ e 𝔞₀ⁿ`. 

### `IsThetaProduct.theta_eq_one`

 The theta functional takes the value `1` at a theta product. 

### `exists_isThetaProduct`

 Let `V` be standard and let `C` be a CM lattice of area `|Ω|² √d / 2` that contains a multiple
`Ω e`. Then `V` has a theta product for `C`, `Ω` and `e`. 

### `exists_isThetaProduct_cmCurve`

 A standard space has a theta product of level one for the lattice `cmPeriod 𝓞_K` of
`cmCurve`. 

### `IsThetaProduct.exists_smul_vacElem_eq_sum`

 A theta product of level one for `C` and `Ω` is a vector `F` of the finite part whose theta
values and jets at rational translates are those of products of the theta function of `C` along the
vectors `ζᵏ / q₁`, with `q₁` the order of `ζ`, and whose theta function is a theta function for
`q₁ 𝔞₀ⁿ`. In a standard space of rank `n`, a nonzero multiple of the vacuum is then a sum of
`(q₁ ^ 2) ^ (f n)` vectors `finHeisenbergOp (a j) (ϱ(finVec b) F)`, with `f` the number of infinite
places: each is `F` translated by the common finite vector `b`, then by `a j`, and multiplied by the
scalar `stdLattice.semichar (a j)`. 

### `sq_q₁_pow_card_infinitePlace_le`

 With `f` the number of infinite places of `E = P.E s` and `q₁ = P.q₁ s`, one has
`(q₁ ^ 2) ^ f ≤ exp (q₁) ^ (2 * q₁)`. 

### `exists_mul_vacElem_integral_bounded`

 The integral vacuum in rank one: a nonzero multiple of the vacuum has values at the finite
points `finVec x` that are integral (`ιₚ` is the map to the `p`-adic complex numbers) and whose
conjugates over `K` have modulus at most `exp (C q₁²)`, with `C` independent of `s`. 

### `vacuumBoundConst`

 The constant `C` in the bound `exp (C q₁²)` for the conjugates of the values of the integral
vacuum of rank one, chosen from `exists_mul_vacElem_integral_bounded`; see `IsVacuumScale`. 


## The integral vacuum θ° and the module of standard data at p

These are the data to which the integrality of jets (`New.Parameters.norm_jet_jetSeries_le_one`)
applies.


### `IsVacuumScale`

 The scalar `c` normalises the vacuum of the standard space of rank one: it is nonzero, and the
values of `c • vacElem` at finite points are integral with bounded conjugates. 

### `IsVacuumScale.ne_zero`

 The scalar is nonzero. 

### `IsVacuumScale.norm_le_one`

 The values of `c • vacElem` are integral at every prime. 

### `IsVacuumScale.norm_gal_le`

 Their conjugates over `K` have norm at most `exp (C * q₁ ^ 2)`, where `C` is
  `vacuumBoundConst`. 

### `vacuumScale`

 The nonzero number by which the vacuum of rank one is multiplied to have integral values with
bounded conjugates, chosen from `exists_mul_vacElem_integral_bounded`. 

### `intVacuum`

 The integral vacuum: the vacuum of a space of rank `n` times `vacuumScale ^ n`. 

### `integralAfter`

 The additive subgroup of vectors `x` of finite adeles that are integral after multiplication by
`δ`: all coordinates of `δ x` are integral at the places of `E` in `S`. Here `evalAt w` is the
component at the place `w`, and `v` is the valuation of the completion at `w`. 

### `standardData`

 Standard data at `p`: the span over the ring `embValRing` (the complex numbers that the
`p`-adic place sends to integers) of the translates of the integral vacuum by the points that `δ`
makes integral above `p`. 


## Integrality, bounds and nonvanishing of the values of θ°

The point `New.finVec x` has finite part a fixed multiple of `x` and archimedean part zero.

`Gal(ℂ/K)` is the group of automorphisms of `ℂ` over `K = ℚ(√-d)`.


### `intVacuum_finVec_eq_prod`

 At a finite point `finVec x`, the integral vacuum of a standard space is the product over the
coordinates `x i` of the values of the scaled vacuum of rank one. 

### `norm_intVacuum_le_one`

 The values of the integral vacuum of rank `n` at the points `finVec x`, with archimedean part
zero, are integral at every prime. 

### `norm_gal_intVacuum_le`

 The conjugates over `K` of the values of the integral vacuum of rank `n` have modulus at most
`exp (C q₁² n)`, with the constant `C = vacuumBoundConst` of the case of rank one. 

### `exists_algEquiv_norm_eq`

 Every automorphism of `ℂ` has the same absolute values as some automorphism over the
imaginary quadratic field `K`. 

### `norm_ringEquiv_intVacuum_le`

 All conjugates `σ (intVacuum V (finVec x))` under automorphisms `σ` of `ℂ` of the values at
`finVec x` of the integral vacuum of the standard space `V` of rank `card n` have modulus at most
`exp (C q₁²) ^ card n`. Here `q₁ = P.q₁ s` and `C = vacuumBoundConst` is the constant of the case of
rank one. 

### `norm_dataInner_self_le`

 Let a vector `f` of a standard space be read as the function `f y = θ(ϱ(y) f)` of an adelic
vector `y`, with `θ` the theta functional. If `|f|` is at most `M` at all points `finVec x`, whose
archimedean part is zero, then `dataInner f f`, the mean of `|f|²`, has modulus at most `M ^ 2`. 

### `exists_intVacuum_ne_zero`

 For a standard space `V`, there is a finite adelic vector `x` such that the integral vacuum
`intVacuum V` is nonzero at the point `finVec x`. 


## Conjugates of the jets of the translates of one vector

The product of copies of the theta function along the vectors `ζᵏ / q₁` (the resolution of powers
of `ζ`) also serves to compute the action of the automorphisms of `ℂ` over `K` on jets.


### `bigOmega_pos`

 The number `bigOmega P s`, which is `exp (chowlaSelbergConst d) * 2π / rootDiscr E`, is
positive. Here `chowlaSelbergConst d` is `γ - Re L'/L(1, χ_K)`, with `γ` Euler's constant. 

### `jetScale_ne_zero`

 The scale `jetScale = periodFactor * areaScale / cmPeriod`, at which the Taylor series of theta
functions are taken, is nonzero. 

### `norm_gal_periodFactor_div_mul_areaScale_sq`

 Let `cmCurve` be the CM lattice `cmPeriod 𝓞_K` and `galConjugate σ` its conjugate by `σ`, with
`E = P.E s`, `K = K P` and `d = P.d`. If the period parallelogram of the conjugate lattice has the
area `|Ω|² √d / 2`, then the scale `σ periodFactor / Ω * areaScale` has the squared norm
`(bigOmega P s)⁻¹`. Here `bigOmega P s` is `exp (γ - Re L'/L(1, χ_K)) * 2π / rootDiscr E`, with `γ`
Euler's constant and `rootDiscr E` the root discriminant of `E`. Here `areaScale` is `√(2π / √d)`
and `periodFactor` is `vacuumRoot / chowlaSelbergUnit`. The denominator is the number chosen in the
formula of Chowla and Selberg for `cmCurve`. 

### `finitePart_le_span_translates`

 Let `V` be a space and `F` a vector of `𝒮 V`. Suppose `c • vacElem`, with `c ≠ 0`, is a sum of
translates `finHeisenbergOp (a j) (ϱ(finVec b) F)`. Then the finite part `finitePart` (the span of
the vectors `finHeisenbergOp z vacElem`) is contained in the span of the translates `ϱ(finVec x) F`
over all finite adelic vectors `x`. 

### `map_zetaLinearSeries`

 The series `zetaLinearSeries Ω c k j` is the linear form `Ω / q₁ / areaScale * c * ∑ w, conj (Φ
w ζᵏ) * z (w, j)` in the variables `z`, the sum being over the infinite places `w` of `E = P.E s`.
Here `ζ` is the root of unity that generates `E` over `K`, and `Φ w` is the complex embedding chosen
at `w`. An automorphism `σ` of `ℂ` over `K`, applied to the coefficients, takes this form for the
period `cmPeriod` and the scale `jetScale` to that for the period `Ω` and the scale
`σ periodFactor / Ω * areaScale`, up to the permutation `placePerm s σ` of the infinite places
induced by `σ`. Here `q₁` is the order of `ζ`, `areaScale = √(2π / √d)`,
`periodFactor = vacuumRoot / chowlaSelbergUnit` and
`jetScale = periodFactor * areaScale / cmPeriod`. 

### `exists_rational_translate_eq`

 Let `F` be a vector of the finite part, `β` a finite adele of `K` and, for each `x ∈ K`, `U x` a
neighbourhood of `β x`. For a rational vector `γ` there is `a ∈ K` such that the translates of `F`
by `β γ` and `a γ` agree and `a x` lies in `U x` for each coordinate `x = zetaCoord s k (γ i) ∈ K`
of `γ i` along a resolution vector `ζᵏ / q₁`. 

### `IsThetaProduct.isJetConjugate_of_map_taylorAtZero_eq`

 Let `F` be a theta product for `cmCurve` with period `cmPeriod` and level `e`, and `F'` one for
the conjugate curve by `σ` with period `Ω` and level `e'`. The factors of a theta product at a
rational vector `γ` are the functions `zetaCoordThetaTranslate C Ω k (γ j)`, the twisted translates
of the theta function of `C` by `Ω` times the coordinate of `γ j` along `ζᵏ / q₁`. If `σ` takes the
Taylor series of the factors of `F` at `γ` to those of the factors of `F'` at `γ'`, then it takes
the jets of the translate of `F` by `γ` at the scale
`jetScale = periodFactor * areaScale / cmPeriod` to those of the translate of `F'` by `γ'` at the
scale `σ periodFactor / Ω * areaScale`, with the infinite places permuted by `σ`. 

### `exists_isJetConjugate_translates`

 For each automorphism `σ` of `ℂ` over `K` there is a finite adele `B σ` of `E` such that every
standard space `V` has a vector `F` of the finite part with `θ F = 1`, whose translates
`ϱ(finVec x) F` span the finite part, and, for each `σ`, a vector `F'` of the finite part and a
scale `t` with `|t|² = 1 / bigOmega` such that `σ` takes the jets of the translate of `F` by `x`, at
the scale `jetScale`, to those of the translate of `F'` by `B σ • x` at the scale `t`, with the
infinite places permuted by `σ`. Here `θ` is the theta functional of `V`, `finVec x` is the adelic
vector with finite part a fixed multiple of `x` and archimedean part zero, and `jetScale` and
`bigOmega` are the scale and the period constant attached to `P` and `s`. 
