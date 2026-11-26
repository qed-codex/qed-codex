---
{
  "module": "src/Lib/DiscreteSeries/Bruhat/FloorFibre.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Bruhat/FloorFibre.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Bruhat/FloorFibre.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Measures of a floor below fibre measures, at the place ℂ

The group `New.Shape.G₁` is the unitary group of the complex form `h` (Gram matrix `𝔰.J₁`) with
basis `e_a`, `x_i` (`i : κ`), `z`, `e*_a`: `ϱ` hyperbolic pairs `e_a, e*_a`, the `x_i` orthonormal
and `h(z, z) = -1`. The pair of index `a` has floor `a`, `z` has floor `ϱ` and the `x_i` have floor
`ϱ + 1` (`New.Floors.FloorGroups.floorOf`); `V_b`, for a floor `b : Fin 𝔰.n` (so `b ≤ ϱ`), is
spanned by the basis vectors of floor at least `b`; `oppositeIndex` exchanges the indices of `e_a`
and `e*_a`.

A vector `y` is chosen with given products with earlier basis vectors and with a given norm
`h(y, y)`. Here `New.LeFibreMeasure μ ν π b l` says that the measure `l` is at most the fibre
measure `dμ / dν` of the map `π` over the point `b`.

## Main definitions and results

* `New.Floors.leFibreMeasure_frameVector`: for the frame vector of a floor, half the quadric measure
  of the floor is at most the fibre measure.
* `New.Floors.leFibreMeasure_dualVector`: for the dual vector, half the measure of the Heisenberg
  group of the floor is at most the fibre measure.

The factor one half arises because these measures are quotients by `d(h(y, y) / 2)`. The last
section proves that the measures of the Heisenberg groups are invariant under inversion, as is the
Haar measure of the unitary group of the span of the `x_i`, carried into `G₁`.

Notions from other files:
* `New.Floors.HyperbolicBasis.floorQuadricMeasure`: The measure on a quadric in V_b: the image of
  `New.Floors.Place.quadricMeasure` with parameter β under the basis `F.floorBasis b`.
* `New.Floors.Place.heisenbergMeasure`: The measure on the Heisenberg group of floor `a`: the image
  of `dv` times the skew measure under the map that sends `(v, β)` to the isometry with
  `e*_a ↦ e*_a + v + (β - h(v, v) / 2) e_a`. For `a ≥ ϱ` it is the unit mass at `1`.
* `New.Shape.besselFrame`: The frame `(e_0, …, e_(ϱ-1), z)`, with one vector on each floor up to
  `ϱ`.
* `New.Floors.complexPlace`: The place `ℂ`: `τ = 1/2`, `δ = i/2`, `ν` the image of Lebesgue measure
  under `r ↦ r i`, modulus `‖x‖ ^ 2`, character `x ↦ exp (x - x̄)` and constant `c = π ^ 2`.

## Relation to the literature

Known; see `Lib.DiscreteSeries.Bruhat.ComplexPlace` for sources.


 ### Linear conditions and quadrics 

### `inclMatrix_sumElim_mulVec`

 For the matrix `inclMatrix ℂ f` of the map that sends the basis vector at `a` to the one at
`f a`, the image of a vector `(t, v)` under the matrix of `f ⊕ g` is the sum of the images of
`t` and `v`. 

### `leFibreMeasure_coords`

 Let `f` and `g` together enumerate the index set `ι`. On the vectors whose coordinates along
`f` are `c`, Lebesgue measure in the coordinates along `g` is at most the fibre measure of
`y ↦ y ∘ f` over `c`. 

### `range_oppositeIndex_val`

 The image of the indices with property `p` under the involution `oppositeIndex`, which
exchanges `e_a` with `e*_a`, consists of the indices whose opposite has property `p`. 

### `skewOfLevel`

 The skew element `i t / 2`, which indexes the quadric `h(v, v) = t` at the place `ℂ`. 

### `measurePreserving_skewOfLevel`

 The map `t ↦ i t / 2` carries `dt / 2` to the measure of the place `ℂ` on the skew elements. 

### `skewUnitMul_eq_skewOfLevel`

 Multiplication of a real number `Γ` by the skew unit `δ = i / 2` of the place `ℂ` gives
`skewOfLevel Γ = i Γ / 2`. 

### `measurePreserving_half_add`

 A complex number is `t / 2 + β` with `t` real and `β` skew, and Lebesgue measure is
`dt dν(β) / 2` for the measure `ν` on the skew elements. 

### `leFibreMeasure_quadricMeasure`

 Let `h` be the orthogonal sum of a hyperbolic plane and a hermitian form `T` (its Gram matrix is
`planeSumGram T`). Half the measure `quadricMeasure` of the quadric `h(v, v) = t₀`, which is indexed
by `skewOfLevel t₀ = i t₀ / 2`, is at most the fibre measure `dv / dh(v, v)` (`LeFibreMeasure`)
over `t₀`. 

### `leFibreMeasure_floorQuadric`

 Let `h` be the form with Gram matrix `J₁` and `V_b` the span of the basis vectors of floor at
least `b`, with Lebesgue measure `floorVolume b`. Half the measure `floorQuadricMeasure` of the
quadric `h(y, y) = t₀` in `V_b`, indexed by `skewOfLevel t₀ = i t₀ / 2` and taken in the
hyperbolic basis `complexBasis 𝔰`, is at most the fibre measure `dy / dh(y, y)` (`LeFibreMeasure`)
on `V_b`. 

### `J₁_mulVec_apply_eq_oppositeIndex`

 The product `(J₁ *ᵥ y) i` of `y` with the basis vector of an index `i` of a floor below `ϱ` is
the coordinate of `y` at the opposite index. 

### `leFibreMeasure_frameVector`

 The frame vector `f_b` of floor `b`, the basis vector of index `besselFrame b`. The vectors
`y` orthogonal for the form `h` of matrix `J₁` to the basis vectors of lower floors (`floorOf`)
form `V_b`. Half the measure of the quadric `h(y, y) = h(f_b, f_b)` in `V_b`, which is the default
level of `floorQuadricMeasure b`, is at most the fibre measure (`LeFibreMeasure`) of the products of
`y` with these vectors and with itself. 

### `dualPoint`

 The vector `e*_a + v + μ e_a`, for `p = (μ, v)` with `v` in the span `V_(a+1)` of the basis
vectors of floor greater than `a`. 

### `re_form_dualPoint`

 The norm of `dualPoint a (μ, v) = e*_a + v + μ e_a` for the form `h` of matrix `J₁` is
`2 Re μ + h(v, v)`. Here `v` lives on the indices of floor (`floorOf`) greater than `a`, and
`inclMatrix` extends it by zero. 

### `leFibreMeasure_dualPoint`

 For the form `h` of matrix `J₁`, consider the products of `y` with `e_a` and with the basis
vectors of lower floors (`floorOf`). Over their values at `e*_a` (index `eStar a`), the image of
`dμ dv` under `dualPoint a (μ, v) = e*_a + v + μ e_a` is at most the fibre measure
(`LeFibreMeasure`). 

### `re_skewAdjoint_complex`

 The real part of a skew element of `ℂ` is zero. 

### `lintegral_map_dualPoint`

 The integral against the image of `dμ dv` under `dualPoint a`, in the coordinates `(v, t, β)`
with `μ = t / 2 + β - q v`, for a continuous shift `q`, `t` real and `β` skew. 

### `leFibreMeasure_heisenbergMeasure`

 On the image under `dualPoint a (μ, v) = e*_a + v + μ e_a` of `dμ dv`, half the image of the
measure of the Heisenberg group of floor `a` under `u ↦ u e*_a` is at most the fibre measure
`dμ dv / dh(y, y)` (`LeFibreMeasure`) over the value `0`, for the form `h` of matrix `J₁`. Here
`eStar a` is the index of `e*_a`. 

### `leFibreMeasure_dualVector`

 The dual vector `e*_a` of floor `a`, of index `eStar a`. For the form `h` of matrix `J₁`, on the
isotropic vectors `y` with `h(e_a, y) = 1` that are orthogonal to the basis vectors of lower floors
(`floorOf`), half the image of the measure of the Heisenberg group under `u ↦ u e*_a` is at most the
fibre measure (`LeFibreMeasure`) of the products of `y` with these vectors, with `e_a` and with
itself. 

 ### Inversion 

### `inv_mconv`

 The image under inversion of the convolution `μ ∗ₘ ν` of two s-finite measures is the
convolution of their images in the opposite order. 

### `instance : (volume.map (embedH (𝔰`

 The Haar measure of the unitary group of the span of the vectors `x_i`, carried into `G₁` by
`embedH`, is invariant under inversion. 

### `instance (l : ℕ) : (complexPlace.heisenbergMeasure l : Measure 𝔰.G₁).IsInvInvariant`

 The measure of the Heisenberg group of floor `l` in `G₁` (the unit mass at `1` for `l ≥ ϱ`) is
invariant under inversion. 
