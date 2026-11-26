---
{
  "module": "src/Lib/SiegelWeil/OneVector/StandardQuadrics.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/SiegelWeil/OneVector/StandardQuadrics.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/SiegelWeil/OneVector/StandardQuadrics.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The quadrics of the standard form at a finite place

At a finite place the standard hermitian form of rank at least two has a basis that begins with a
hyperbolic pair. So the volume disintegrates along the form, and the local density bound applies to
the measures of its quadrics.

* `New.Floors.IntegralPlace.isDisintegration_of_hyperbolic_basis`: the disintegration.
* `New.Floors.IntegralPlace.exists_kernel_isDisintegration_le`: if ψ is trivial on traces,
  ζ_R(μ) ≤ 2 and the rank is at least 2μ + 2, then some s-finite kernel is a disintegration of the
  volume for which the points y of a quadric with u y integral, for a unit u, have bounded mass.

Notions from other files:
* `New.Floors.Place.IsDisintegration`: a family of measures on the quadrics of a form, continuous
  in the index, whose integral over the index is a given measure.
* `New.Floors.Place.quadricMeasure`: the measure on a quadric of a hyperbolic plane plus a form.
* `New.idealZeta`: the sum ζ_R(s) of [R : I]^(−s) over the ideals I of finite index in R.
* `New.Floors.coordinateBox`: the vectors with all coordinates in a given set.

## Relation to the literature

Known result: a local density bound for hermitian forms. See
`Lib.SiegelWeil.OneVector.SiegelClassSum`.


### `Place.isDisintegration_map_quadricMeasure`

 Let `B` have as many columns as rows, with Gram matrix `planeSumGram S` for the form `T`: a
hyperbolic plane plus `S`. Let `det T` have modulus one (a matrix scales the volume by the modulus
of its determinant) and let `S` be hermitian with `S * S = 1`, so that the columns of `B` are a
basis. Then `B` carries the measures `P.quadricMeasure S b`, on the quadrics of norm `δ⁻¹ b` for
`planeSumGram S` (`δ = P.skewUnit`), to a disintegration of the volume along `T`: they are the fiber
measures of the volume on the quadrics `x* T x = δ⁻¹ b`. 

### `card_eq_card_pair_sum`

 A finite type with at least two elements has the cardinality of a pair plus a rest. 

### `IntegralPlace.exists_hyperbolic_basis`

 At a finite place, the standard hermitian form of rank at least two has a basis that begins
with a hyperbolic pair and ends with orthonormal vectors: its Gram matrix is `planeSumGram 1`. 

### `IntegralPlace.isDisintegration_of_hyperbolic_basis`

 Let `A` be a finite place and let `κ` have at least two elements. Let `B` be a basis for the
standard form on `κ → A` with Gram matrix `planeSumGram 1`: a hyperbolic pair, then orthonormal
vectors. It carries the measures `P.quadricMeasure 1 b`, for skew `b`, on the quadrics of norm
`δ⁻¹ b` for `planeSumGram 1` (`δ = P.skewUnit`), to a disintegration of the volume along
`x ↦ x* x`: they are its fiber measures on the quadrics `x* x = δ⁻¹ b`. 

### `IntegralPlace.exists_kernel_isDisintegration_le`

 Let A be a finite place whose additive character ψ is trivial on traces x + x̄, let ζ_R(μ) ≤ 2,
and let κ have r + 1 ≥ 2μ + 2 elements. Then the volume of A^κ disintegrates along the standard
form x ↦ x* x into an s-finite kernel l, with l β on the quadric x* x = δ⁻¹ β for skew β, and for a
unit u the set `coordinateBox` of the points y with all u y_i in R has mass at most ζ_R(μ) |u|^(-r)
for each l β. Here R is the ring of integers of A, δ = `skewUnit`, ζ_R(μ) = `idealZeta R μ` is the
sum of [R : I]^(-μ) over the ideals I of finite index, and |x| = `modulus x` is the factor by which
multiplication by x scales the volume of A. 
