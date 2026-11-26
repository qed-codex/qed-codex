---
{
  "module": "src/New/Spanning/Frames/FiberMeasures.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Frames/FiberMeasures.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Frames/FiberMeasures.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Fiber measures of the standard form, and the top quadric by its last entry

At a finite place and in rank at least two, the volume of `κ → A` disintegrates along `ω ↦ ω* ω`
into the fiber measures `Place.normFiberMeasure`. The main result,
`HyperbolicBasis.integral_floorQuadricMeasure_top`, writes the measure of the quadric of vectors of
norm `-N` in `X₀ ⊕ A z` as an integral, over the last entry `t = ⟨z, y⟩` of a vector `y`, of the
fiber measures of the spheres `ω* ω = t t̄ / N - N` in `X₀`.

Notions from other files:

* `Place A`: a locally compact star ring with Haar volume, a multiplicative `modulus`, skew unit
  `δ = skewUnit` and Haar measure `skewMeasure` on the skew elements; `IntegralPlace A` is a finite
  place, or a finite set of finite places read as one ring.
* `P.IsDisintegration μ J l`: the measures `l b`, for skew `b`, are the fiber measures of `μ` on the
  quadrics `x* J x = δ⁻¹ b` and depend continuously on `b`.
* `flatChart S b`, `P.quadricMeasure S b`: coordinates and measure on the quadric of norm `δ⁻¹ b`
  for `planeSumGram S`, the Gram matrix of a hyperbolic plane plus `S`.
* `latticeMiddleGram 𝔰 N`: the Gram matrix of `X₀ ⊕ A z`, where `X₀` has an orthonormal basis `x_i`
  indexed by `𝔰.κ` and `z` has norm `-N`, `N = π π̄`, in the lattice basis `x_i` (`i ≠ k₀`),
  `v = x_{k₀} / π̄ + z / N`, `z`. For such a Gram matrix `T : 𝔰.Form A`, the matrix `T.splitGram`
  is that of the whole space, with hyperbolic planes added.
* `vectorOfLastEntry π t x`: the vector `y = x - (π π̄)⁻¹ t z` of `X₀ ⊕ A z`, in the lattice basis
  of the whole space. Its pairing `⟨z, y⟩` with the last frame vector `z`, called its last entry, is
  `t`.

## Relation to the literature

See `New.Spanning.MainTerm.EnergyEstimate` for related work.


### `Place.IsDisintegration.continuous_integral`

 Let the measures `l b`, indexed by the skew elements `b` of the place `A`, disintegrate `μ`
along the form `J`. For a continuous complex function `f` of compact support, the integral of `f`
against `l b` depends continuously on `b`. 

### `Place.normFiberMeasure`

 The fiber measures `dω / d⟨ω, ω⟩` of the standard hermitian form on `κ → A`: the disintegration
of the volume along `ω ↦ ω* ω`, if there is one (it is unique by `IsDisintegration.unique`), and an
arbitrary family otherwise. At a finite place and in rank at least two the disintegration exists
(`IntegralPlace.isDisintegration_normFiberMeasure`), and the measure at `b` lives on the quadric
`ω* ω = δ⁻¹ b`, where `δ = P.skewUnit` (`IntegralPlace.ae_normFiberMeasure_dotProduct_eq`). 

### `lastEntrySphereIndex`

 The skew element `δ α`, where `δ = P.skewUnit`, `α = t t̄ / N - N` and `N = π π̄`; it is the
index in `Place.normFiberMeasure` of the sphere `ω* ω = α`. With `z` the last frame vector, of norm
`-N` and orthogonal to `X₀`, the vector `y = ω - N⁻¹ t z` has `⟨z, y⟩ = t`, and it has norm `-N` if
and only if `ω` lies on this sphere. 

### `continuous_lastEntrySphereIndex`

 The skew element `lastEntrySphereIndex π t = δ (t t̄ / N - N)`, where `δ = P.skewUnit` and
`N = π π̄`, depends continuously on `t`. 

### `measurePreserving_append_last`

 For a unit `u` and an s-finite measure `ζ`, the map
`(t, (s, w), z) ↦ ((s, (w, u t)), z)`, which appends `u t` to the vector `w`, carries
`modulus u • dt` times `ds dw dζ` to the volume of `A × (κ ⊕ Unit → A)` times `ζ`. 

### `lastVectorQuadric`

 The top quadric of the form `T.splitGram`: the vectors of `X₀ ⊕ A z`, that is with no component
along the hyperbolic pairs (the indices of floor less than `𝔰.ϱ`), that have the norm of the last
frame vector `z`. 

### `isClosedEmbedding_vectorOfLastEntry`

 For fixed `t`, the map `vectorOfLastEntry π t` is a closed embedding. It sends `x` in
`X₀ = (𝔰.κ → A)` to `x - (π π̄)⁻¹ t z`. 

### `middleBasisMatrix`

 The orthonormal basis of `X₀` followed by `π⁻¹ z`, in the coordinates of the lattice basis. 

### `gram_middleBasisMatrix`

 Let `X₀`, of index set `𝔰.κ`, have the orthonormal basis `x_i`, let `z` be orthogonal to `X₀` of
norm `-N`, where `π π̄ = N`, and let `k₀ = 𝔰.k₀` be the marked index. The form
`latticeMiddleGram 𝔰 N` of `X₀ ⊕ A z` is written in the lattice basis `x_i` (`i ≠ k₀`),
`v = x_{k₀} / π̄ + z / N`, `z`. In the basis `middleBasisMatrix`, made of the `x_i` and `π⁻¹ z`,
its Gram matrix is `diag(1, …, 1, -1)`. 

### `vectorOfLastEntry_eq_mulVec`

 In the basis `middleBasisMatrix`, the orthonormal basis of `X₀` followed by `π⁻¹ z`, the vector
`vectorOfLastEntry π t x = x - (π π̄)⁻¹ t z` has the coordinates `x` on `X₀` and `-π̄⁻¹ t` at
`π⁻¹ z`. The matrix `inclMatrix A (inr ∘ inl)` includes `X₀ ⊕ A z`, the middle block of indices, in
the whole space. 

### `IntegralPlace.isDisintegration_normFiberMeasure`

 At a finite place and in rank at least two, the fiber measures `P.normFiberMeasure κ`
disintegrate the volume of `κ → A` along the standard form `x ↦ x* x`. 

### `IntegralPlace.normFiberMeasure_eq_map`

 For a basis `B` of the standard form with Gram matrix `planeSumGram 1`, the fiber measure
`P.normFiberMeasure κ b` of `x ↦ x* x` is the image under `B` of the measure `P.quadricMeasure 1 b`
of the flat chart. 

### `IntegralPlace.normFiberMeasure_eq_map_flatChart`

 At a finite place and in rank at least two, let the columns of `B` have Gram matrix
`planeSumGram 1` for the standard form `x ↦ x* x`: a hyperbolic pair, then orthonormal vectors. In
this basis `flatChart 1 b` sends coordinates `p = ((t, w), a)`, with `a` skew, to a point of the
quadric of norm `δ⁻¹ b` whenever `t` is a unit. The fiber measure `P.normFiberMeasure κ b` of
`x ↦ x* x` is the image under `p ↦ B (flatChart 1 b p)` of the volume in `(t, w)` times
`P.skewMeasure`, the Haar measure of the place on the skew elements. 

### `IntegralPlace.ae_normFiberMeasure_dotProduct_eq`

 At the finite place `P`, if `κ` has at least two elements, the fiber measure
`P.normFiberMeasure κ b` of `x ↦ x* x` on `κ → A` lives on the quadric `x* x = δ⁻¹ b`, where
`δ = P.skewUnit`: almost every `x` satisfies this equation. 

### `IntegralPlace.ae_vectorOfLastEntry_mem_lastVectorQuadric`

 Let `π π̄ = N`, let `X₀ = 𝔰.κ → A` have an orthonormal basis of at least two vectors and let `z`
be orthogonal to it, of norm `-N`; `latticeMiddleGram 𝔰 N` is the form of `X₀ ⊕ A z`. For almost
every `x` for the fiber measure `P.normFiberMeasure 𝔰.κ (lastEntrySphereIndex π t)` of `x ↦ x* x`,
which lives on the sphere `x* x = t t̄ / N - N`, the vector `vectorOfLastEntry π t x = x - N⁻¹ t z`
lies on the top quadric `lastVectorQuadric (latticeMiddleGram 𝔰 N)`, that of the vectors of norm
`-N` in `X₀ ⊕ A z`. 

### `HyperbolicBasis.measurePreserving_inclMatrix_flatChart`

 Let `E` be a basis of `X₀ ⊕ A z` that begins with a hyperbolic pair: its Gram matrix for `T` is
`planeSumGram S`, with `S` hermitian and `S * S = 1`. Then the flat chart of `E`, included in the
whole space by the matrix `inclMatrix A (inr ∘ inl)`, carries the product of the volume and of
`P.skewMeasure`, the Haar measure of the skew elements, to the measure
`F.floorQuadricMeasure 𝔰.top b` of the quadric of norm `δ⁻¹ b` in `X₀ ⊕ A z`, `δ = P.skewUnit`.
Here `F` is any basis of `X₀ ⊕ A z` made of `m + 1` hyperbolic pairs and orthonormal vectors
indexed by `ι`, and `T.splitGram`, the form of the whole space, is hermitian and invertible. 

### `flatChart_comp_sumAssoc`

 Let `π π̄ = N` and `b = -δ N`, where `δ = P.skewUnit`. The form `fromBlocks 1 0 0 (-1)` is an
orthonormal part on `κ` plus a vector of norm `-1`, and its `flatChart` parametrises the quadric of
norm `δ⁻¹ b = -N` of a hyperbolic plane plus this form. At `((s, w ⊕ -π̄⁻¹ t), a)`, this chart,
reindexed by `Equiv.sumAssoc`, equals `flatChart 1 (lastEntrySphereIndex π t) ((s, w), a)`, the
chart of the sphere of norm `t t̄ / N - N`, followed by the last coordinate `-π̄⁻¹ t`. 

### `HyperbolicBasis.measurePreserving_vectorOfLastEntry_flatChart`

 Let `π π̄ = N`, let `X₀` have rank at least two and let `B` be a basis of `X₀` with Gram matrix
`planeSumGram 1`. Send a pair `(t, p)` to the vector `vectorOfLastEntry π t x = x - N⁻¹ t z`, where
`x` is the point with coordinates `p` in the flat chart of the sphere `x* x = t t̄ / N - N`. This
map carries `(modulus π)⁻¹ dt` times the measure of the chart to `F.floorQuadricMeasure 𝔰.top`, the
measure, defined by a hyperbolic basis `F` of `X₀ ⊕ A z`, of the quadric of vectors of norm
`⟨z, z⟩ = -N`. 

### `HyperbolicBasis.integral_floorQuadricMeasure_top`

 Let `A` be a semilocal field with involution, `P` a finite place on it and `π` a unit of `A`
with `π π̄ = N`; multiplication by `π` scales the volume of `A` by `P.modulus π`. The matrix
`latticeMiddleGram 𝔰 N` is the form of `X₀ ⊕ A z` in the lattice basis, where `X₀ = (𝔰.κ → A)` is
the standard hermitian space, of rank at least two, and `z` is orthogonal to it of norm `-N`. The
whole space `𝔰.BesselIndex → A` adds `𝔰.ϱ` hyperbolic planes, and its form is hermitian and
invertible. Let `f` be continuous of compact support on the whole space.
For `t` in `A`, take `(P.modulus π)⁻¹` times the integral of
`f (vectorOfLastEntry π t x) = f (x - N⁻¹ t z)` against the fiber measure
`P.normFiberMeasure 𝔰.κ (lastEntrySphereIndex π t)` of the sphere `x* x = t t̄ / N - N` in `X₀`.
This function of `t` is integrable, and its integral is that of `f` against
`F.floorQuadricMeasure 𝔰.top`. The latter has its default index `δ ⟨z, z⟩`, where `δ = P.skewUnit`:
it is the measure on the quadric of vectors of norm `-N` in `X₀ ⊕ A z` defined by a basis `F` made
of `m + 1` hyperbolic pairs and orthonormal vectors indexed by `ι`. 
