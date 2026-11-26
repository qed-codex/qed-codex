---
{
  "module": "src/New/Derivatives/Vacuum/Scale.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/Scale.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/Scale.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The scale of the Taylor series of a vector

* `New.Space.jet_jetSeries_of_isHomogeneous`: the derivative of the Taylor series along a
  homogeneous polynomial is a theta value times a power of the scale.
* `New.Parameters.norm_periodFactor_mul_daggerForms_le_one`: the scaled linear form of a vector `y`
  is integral at `p` if `α⁻¹ y` is integral above `p`.
* `New.Parameters.norm_jetScale_sq`: the modulus of `jetScale`, from the area of the CM lattice and
  the formula of Chowla and Selberg.

The period scale is `jetScale` times an integer `π_M` of `K` of norm `M`. The statements with this
factor are `New.Data.norm_conj_piMBar_mul_jetScale_sq` and
`New.Data.norm_taylorScale_eq_one_of_not_dvd`.

The statements use these notions:
* `jetSeries a f`: the Taylor series of the theta function of `f`, with variables scaled by `a`;
  `jet R Q F` is the derivative at zero of the series `F` along the polynomial `Q`.
* `daggerForms u j`: the coefficients in `ℂ_p` of the linear form `z ↦ y† z` of the vector
  `y = u j`; at a pair `(v, i)` of an infinite place and a coordinate the coefficient is the image
  in `ℂ_p` of the complex conjugate of `Φ_v (y i)`, with `Φ_v` the embedding chosen at `v`.
* `periodFactor`: the complex number `vacuumRoot / chowlaSelbergUnit`, where `vacuumRoot` is a root
  of the inverse of the value `chiFin α` of a character at the idele `α` and the denominator is a
  unit at every `p`-adic place; `jetScale` is `periodFactor * √(2π / √d) / cmPeriod`, where
  `cmPeriod * 𝓞_K` is the lattice of the CM curve of the field `K = ℚ(i√d)`.

## Relation to the literature

The modulus of `jetScale` is computed from the formula of Chowla and Selberg,
`New.CMLattice.chowla_selberg`.


### `jet_rescale`

 Scaling all variables of a power series `F` by `a` multiplies the derivative `jet R Q F` at
zero along a homogeneous polynomial `Q` of degree `l` by `a ^ l`. 

### `Space.jet_jetSeries_of_isHomogeneous`

 Let `E` be a CM number field with a chosen CM type (`CMType`) and the data of its Weil
representation (`WeilData`). For a homogeneous polynomial `Q` of degree `l` and a vector `f` of
the Weil representation `𝒮 V` of the hermitian space `V` with signs `ε`, the derivative at zero
along `Q` of the series `V.jetSeries a f` is `a ^ l θ(v_Q ⊗ f)`. Here `θ` is the theta functional,
`realSigns E ε` gives each pair (infinite place, coordinate) the sign of the coordinate,
`v_Q = polyVector Q` is the Fock vector of `Q` for these signs, and `⊗` is `V.integrated`, the
bilinear map that integrates the action of the real Heisenberg group on `f` against `v_Q`. The
series `V.jetSeries a f` has one variable for each such pair; its coefficient at the monomial
`z ^ α` is `a ^ |α| / α! * θ(v_{z ^ α} ⊗ f)`. 

### `norm_adeleExtension_le_one_iff`

 Let `σ` be an embedding of the number field `E` into a `p`-adic field `F`, that is, a normed
algebra over `ℚ_p` that is a field, here ultrametric and not necessarily complete. The image of a
finite adele `x` under the extension of `σ` to finite adeles has norm at most one if and only if
the component of `x` at the place induced by `σ` is integral. 

### `CMLattice.area_eq_of_a₁_eq`

 Let `d` be a prime that is `7` modulo `8`. Two CM lattices for `d` with the same invariant
`a₁` (a square root of `12 ℘(t)` for the marked point `t` of order two) have the same area. 

### `norm_periodFactor_mul_daggerForms_le_one`

 Let `y = u j` be a vector over the field `E = P.E s` of the parameters at the index `s`, a
cyclotomic extension of `K = P.K = ℚ(i√d)`, and `α = P.α s` their idele. Let `ιₚ : ℂ → ℂ_p` be the
ring homomorphism chosen by `PadicPlace p`. For a pair `x = (v, i)` of an infinite place of `E` and
a coordinate, `daggerForms u j x` is the image under `ιₚ` of the complex conjugate of `Φ_v (y i)`,
with `Φ_v : E → ℂ` the embedding that the CM type chooses at `v`. If the finite adelic vector
`α⁻¹ y` (`finiteImage (u j)`) is integral at all places above `p` (`integralAfter 1`), then the
product of `ιₚ periodFactor` and this coefficient has norm at most one. 

### `norm_jetScale_sq`

 Let `P` be the fixed parameters, and `E = P.E s` the field at the index `s`, a cyclotomic
extension of `K = ℚ(i√d)`. The squared modulus of `jetScale = periodFactor * √(2π / √d) / cmPeriod`,
the scale of the Taylor series at the index `s`, is the inverse of
`bigOmega = exp (γ - Re L'/L(1, χ_K)) * 2π / rd_E`. Here `γ` is Euler's constant, `χ_K` the
quadratic character of `K` and `rd_E` the root discriminant of `E`. 
