---
{
  "module": "src/New/Spanning/RemainingTerms/BorderedDeterminant.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/RemainingTerms/BorderedDeterminant.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/RemainingTerms/BorderedDeterminant.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Links, lifts and gauges of a term

The data are `S : New.Filling`, and terms are rational elements `γ` of the unitary group
`New.Filling.G`. The frame is `f = (e₁, …, e_ϱ, z)`, `A` is the span of the `e_a` and `X₀` that of
the `x_i`. `S.frameProducts γ` is the matrix of products of `f` with `γ f`, and `S.HasCellRank j γ`
says that `γ` has cell rank `j`. `New.Filling.minorNorm j γ` is the absolute norm of the leading
`j × j` minor of `S.frameProducts γ`, scaled by a power of `N` when `j = ϱ + 1`.

## Main definitions and results

* `New.Filling.gram_linkForm_eq_zero_of_le_link`: the link is isotropic for `S.linkForm`.
* `New.Filling.linkMetric` is a totally positive form (`New.Filling.linkMetric_posDef`), and
  `New.Filling.linkDiscSq` is the squared discriminant of a lattice for it.
* `New.Filling.HasIntegralLifts`: the predicate that the columns of an adelic matrix are images
  under `New.linkMatrix γ` of vectors of `h_c Λ₀` that are adelic combinations of rational vectors
  orthogonal to `A` and `γ A`.
* `New.Filling.paddedLeading`: the first `j` rows of a matrix, completed by rows of `1`; its
  determinant is the leading minor of order `j` (`New.Filling.det_paddedLeading`). For the matrix
  `S.frameProducts γ` its inverse gives the vectors that `f` and `γ f` share
  (`New.Filling.HasCellRank.exists_shared_frame_vector`).
* `New.Filling.latticeDisc`, `New.Filling.isotropicRowsIndex`, `New.Filling.torsionIndex`: a
  discriminant and two lattice indices. `New.submoduleIndex M M'` is the index of `M ⊓ M'` in `M'`,
  `New.colLattice` a column span.
* `New.Filling.subframeMinor`: the minor `δ_*(γ)`, nonzero for a term with a cell rank
  (`New.Filling.HasCellRank.subframeMinor_ne_zero`).
* `New.Filling.minorGauge`, `New.Filling.maxGauge`: the gauges of a term.
  `New.Filling.IsNearRepresentative` marks the kept terms, and `New.Filling.IsNearTermAt` selects
  the terms that are counted.

Notions from other files:
* `New.link`: the pairs of middle coordinates of `t` and `γ⁻¹ t`, for `t` orthogonal to `A` and
  `γ A`; `New.linkMatrix γ` is the matrix of the map that sends `t` to this pair.
* `New.framePair γ`: the matrix `(f | γ f)` of the two frames; `New.isotropicFramePair γ` is its
  part `(A | γ A)`.
* `New.Filling.Classes`: the classes `c` of a finite double coset space of `U(X₀)`; `h_c` is the
  representative of `c`, and `S.translateByClassReps c c' γ` is `h_c⁻¹ γ h_c'`.
* `New.Filling.classCoord`: `S.classCoord c` takes rational coordinates to coordinates in the
  basis of `h_c Λ₀`, in which the middle Gram matrix is `S.latticeMiddle`; in rational coordinates
  it is `S.ratMiddle = diag(1, -N)`, and `S.linkForm` is the form `diag(T, -T)` for this matrix `T`.
* `New.genIndex`: the generalised index `[a]` of an adele `a`; it is `0` for a non-unit.



## Forms on pairs of middle coordinates, lifts, and isotropy of the link

The space has the basis `e_a`; `x_i`, `z`; `e*_a` (`New.Shape.BesselIndex`) and Gram matrix
`New.Filling.ratGram`: `ϱ` hyperbolic pairs around the middle block
`T = S.ratMiddle E = diag(1, -N)`.

* `New.Filling.dotProduct_linkMetric_mulVec`: `linkMetric` is the mean of the products of the two
  images in `X₀ ⊥ E z⁺`, where `z⁺` has norm `N`. On the link it is the form of `X₀ ⊥ E z⁺` on the
  first image, that under `linkSource` (`New.Filling.linkMetric_form_of_mem_link`).
* `New.linkMatrix` is the map to pairs; `New.Filling.gram_linkMatrix_mul` expresses forms on pairs
  through `New.Filling.ratGram`.


### `liouville_gram`

 Liouville inequality for Gram determinants, over a CM field `E` that contains a primitive root
of unity of order `5040`. Let `Q` be positive definite at each infinite place `w`, after mapping its
entries by the complex embedding `Φ w` chosen for `w`. Let `det (aᴴ Q b) ≠ 0`, and let `v`, `v'` be
invertible finite adelic matrices. Write `Nm` for the norm to `ℚ` and `[δ]` for the generalised
index `genIndex δ` of a finite adele `δ`. This is the inverse of the factor by which multiplication
by `δ` scales Haar measure if `δ` is a unit, and `0` otherwise. If `0 ≤ x ≤ [det(vᴴ aᴴ Q b v')]`,
then `x² ≤ [det v]² · |Nm det(aᴴ Q a)| · |Nm det(bᴴ Q b)| · [det v']²`. 

### `gram_linkMatrix_mul`

 Write `h` for the form `S.ratGram` and `T` for its middle block `S.ratMiddle E`. Let the columns
of `t` be orthogonal to `A` and `γ A`, and those of `t'` to `A` and `γ' A`. Then the pairs
`linkMatrix γ * t` and `linkMatrix γ' * t'` have, for the form `diag(a T, -b T)`, the product
`a h(t, t') - b h(t, γ γ'⁻¹ t')`. 

### `gram_linkForm_eq_zero_of_le_link`

 Let `A` be the isotropic span of the basis vectors `e₁, …, e_ϱ`. The link of `γ` is the space of
the pairs of middle coordinates (those in `X₀ ⊕ E z`) of `t` and `γ⁻¹ t`, for `t` orthogonal to `A`
and `γ A`. Two matrices `v`, `u` with columns in the link are orthogonal for the form
`S.linkForm = diag(T, -T)`, where `T = S.ratMiddle E` is the Gram matrix of `X₀ ⊕ E z`. 

### `linkMetric`

 The matrix `½·diag(T, T) + N⁻¹·L* L` on two copies of `X₀ ⊕ E z`, where `T = S.ratMiddle E`,
the two rows `L = zRowBlockDiagonal T` are the `z`-row of `T` in either copy, and `*` is the
conjugate transpose. 

### `linkDiscSq`

 The number `|Nm det(vᴴ Q v)| · [det e]²`, with `Nm` the norm to `ℚ`, `[·]` the generalised
index and `Q = S.linkMetric`: the squared discriminant of the lattice with adelic basis `v e`. 

### `framePair_last_eq_zRowBlockDiagonal_mul`

 Let `T` be a Gram matrix on the middle coordinates and `k` an isometry of `T.splitGram`, the
form made of `ϱ` hyperbolic pairs around `T`. For every vector `t`, its products with `z` and with
`k z` are obtained from its image under `linkMatrix k` by `zRowBlockDiagonal T`, the block diagonal
matrix with two copies of the `z`-row of `T`. 

### `classCoord_eq_fromBlocks`

 The change to lattice coordinates `S.classCoord c` fixes the isotropic coordinates, and on the
middle ones its columns are those of `S.classCoordX₀ c` and the vector `z`. 

### `HasIntegralLifts`

 The columns of `m` are the images under `linkMatrix γ` of vectors of the lattice `h_c Λ₀`
(the vectors with integral `S.classCoord c`-coordinates) that are adelic combinations of rational
vectors orthogonal to `A` and `γ A`. 

 ### Products in the coordinates of the lattice 

### `gram_classCoordX₀`

 The basis `x_i` of `X₀`, written in the lattice coordinates of `c` (the columns of
`S.classCoordX₀ c`), is orthonormal for the middle Gram matrix `S.latticeMiddle` of the lattice. 

### `classCoord_gram`

 The products of rational vectors `t`, `t'` for the form `S.ratGram` can be computed in the
lattice coordinates `S.classCoord c` of a class `c`, with the Gram matrix of `S.latticeMiddle`. 

### `linkMetric_eq_smul_fromBlocks`

 The form `S.linkMetric` is half the orthogonal sum of two copies of `S.positiveGram`, the
Gram matrix `diag(1, N)` of the space `X₀ ⊥ E z⁺`, in which `z⁺` has norm `N`. 

### `linkMetric_posDef`

 `S.linkMetric` is positive definite at every complex embedding `Φ w` of the CM type. 

### `dotProduct_linkMetric_mulVec`

 Let `X₀ ⊥ E z⁺` be the space of middle coordinates with the Gram matrix
`S.positiveGram = diag(1, N)`. Its last basis vector `z⁺` has norm `N = S.N`, the prime of the
filling `S`. Let `p`, `q` be pairs of middle coordinate vectors, indexed by
`𝔰.MiddleIndex ⊕ 𝔰.MiddleIndex`. The form `linkMetric` on `p`, `q` is the mean of the products in
this space of their two images under `linkSource` and under `linkTarget`. `linkSource` takes the
`X₀`-part of the first member and the `z`-coordinate of the second; `linkTarget` does the same with
the members exchanged. 

### `linkMetric_form_of_mem_link`

 For pairs `p`, `q` in the link of `γ`, the form `linkMetric` is the product of their images
under `linkSource` for the Gram matrix `S.positiveGram = diag(1, N)` on the middle coordinates. 

### `det_gram_linkMetric_ne_zero`

 If the columns of `v` are independent (`v` has a left inverse), then their Gram matrix for
`S.linkMetric` has nonzero determinant. 

### `card_eq_finrank_colSpan`

 If `v` has a left inverse, the number of its columns is the dimension of their span. 

### `classCoord_mul_framePair`

 In the lattice coordinates `S.classCoord c`, the frame pair `framePair γ` (entries embedded in
the finite adeles) is `framePair` of `S.translateByClassReps c c' γ`, namely h_c⁻¹ γ h_c'. 

### `classCoord_mul_isotropicFramePair`

 In the lattice coordinates `S.classCoord c`, the pair `isotropicFramePair γ` = (A | γ A) of
isotropic frames (entries embedded in the finite adeles) is `isotropicFramePair` of
`S.translateByClassReps c c' γ`, namely h_c⁻¹ γ h_c'. 

### `framePair_translateByClassReps_mul_classCoord`

 Let `k = S.translateByClassReps c c' γ = h_c⁻¹ γ h_c'` be the matrix of the rational element `γ`
in the bases of the lattices of the classes `c` and `c'`, and let `C = S.classCoord c` take rational
coordinates to those of the lattice of `c`. In these the form has the Gram matrix
`J = (S.latticeMiddle (𝔸f E)).splitGram`, made of `ϱ` hyperbolic pairs around the middle block
`S.latticeMiddle`; in rational coordinates it has the Gram matrix `J₀ = S.ratGram`. Write `F_g(k)`
for the columns with the indices `g` of `framePair k = (f | k f)`. Then
`F_g(k)ᴴ J (C t) = F_g(γ)ᴴ J₀ t` as finite adelic matrices, for every rational matrix `t` with rows
indexed by the basis `e₁, …, e_ϱ, x_i, z, e*₁, …, e*_ϱ`. 

### `isIntMatrix_framePair`

 If the matrix of `k` has entries in a subring `O`, so has the pair `(f | k f)` of frames. 


## Lattice indices, gauges and the selection of counted terms

A term `γ` is taken with two classes `c`, `c'`; its adelic form is
`S.translateByClassReps c c' γ = h_c⁻¹ γ h_c'`.


 ### Rows of the matrix of products 

### `IndexBelow`

 The indices `a < j` of the isotropic vectors `e_a` of the frame. 

### `isotropicRows`

 The rows of `Z` that belong to the isotropic vectors of the frame. 

### `paddedLeading`

 The first `j` rows of `Z`, completed by rows of the identity matrix. 

### `det_paddedLeading`

 The matrix `paddedLeading j Z` keeps the first `j` rows of `Z` and completes them by the
remaining rows of the identity matrix. Its determinant is the leading minor `D_j` of `Z`. 

 ### Discriminants and indices 

### `frameMiddle`

 The middle coordinates of the image of the frame under `γ`: those in `X₀` and along `z`. 

### `latticeDisc`

 The discriminant (`New.Filling.sublatticeDiscriminant`) of `Λ ∩ V`, for the lattice `Λ` of the
class `c` and a subspace `V` of `X₀`. 

### `isotropicRowsIndex`

 Among the products of `Λ ∩ A` with the frame of `k`, the index of those that
come from the vectors `e_a` with `a < j`. 

### `torsionIndex`

 The index of `Λ ∩ A + k (Λ ∩ A)` in `Λ ∩ (A + k A)`, for the standard lattice `Λ` and the
isotropic space `A`. 

### `minorNorm`

 The absolute norm of the leading minor of order `j` of the matrix of products of the frame with
its image under `γ`, divided by `N ^ (2 r)` at the top rank `j = ϱ + 1`, with `r` the number of
infinite places. 

### `subframeIndices`

 The indices of the subframe made of the first `j` vectors of the frame `(e₁, …, e_ϱ, z)` and its
last vector `z`. For `j = ϱ` and `j = ϱ + 1` the subframe is the whole frame. 

### `subframeMinor`

 The minor `δ_*(γ)` of `S.frameProducts γ` on the rows and columns `subframeIndices j`: the
determinant of the products of the subframe made of the first `j` vectors of the frame
`(e₁, …, e_ϱ, z)` and its last vector `z` with the image of this subframe under `γ`. 

### `minorGauge`

 The gauge `𝗀♯ = Nm δ_*(γ) / (i_γ i'_γ N ^ r)` of the term `γ` from `c'` to `c`. Here `Nm` is the
absolute norm, `δ_*(γ) = S.subframeMinor j γ`, `i_γ` and `i'_γ` are the indices `isotropicRowsIndex`
at `h_c⁻¹ γ h_c'` and at its inverse, and `r` is the number of infinite places. 

### `maxGauge`

 The larger of `𝗀♯ = minorGauge` and `termDiscNorm`, the product of the absolute values of
`𝗀(γ) = S.termDisc γ` at the infinite places. The gauge `𝗀*` is this number times a power of the
congruence level `S.M`. 

### `IsNearRepresentative`

 The term `γ` is near, and it is the chosen element of its double coset `U⁰_c γ U⁰_c'`. Near
means that some archimedean point `y` and `γ⁻¹ y` both lie in `S.boxedPoints`, the reduced points
of bounded size at every infinite place. The group `U⁰_c = S.classUnipotent₀ c` consists of the
rational `u` in the unipotent group `besselU` that fix every vector of the frame and have
`h_c⁻¹ u h_c` in the principal congruence subgroup `S.principalLevel`. 

### `IsNearTermAt`

 Let `p = (c', γ)`, and let `B = S.reducedImage besselS` be the image in the finite group
`S.ResidueGL` of the integral points of the Bessel subgroup `besselS`. The term `γ` from `c'` to `c`
is near and chosen (`IsNearRepresentative`) and has a cell rank (`HasCellRank`). Moreover
`h_c⁻¹ γ h_c'` is integral with reduction `s` (`termsOver`), and `s = r t` for the chosen
representative `r` of the coset `s B`. 

### `isotropicRowsIndex_top`

 At the top rank `j = ϱ + 1` all isotropic vectors of the frame are counted, so the index
`isotropicRowsIndex` is `1`. 

 ### Terms of cell rank `j` 

### `HasCellRank.minorNorm_pos`

 If `γ` has cell rank `j` (`S.HasCellRank j γ`), then `S.minorNorm j γ`, the absolute norm of the
leading minor of order `j` of `S.frameProducts γ` (divided by a power of `N` when `j = ϱ + 1`), is
positive. 

### `HasCellRank.inv`

 If `γ` has cell rank `j` for `S`, then so does `γ⁻¹`. That is, `New.NormOnePairOccursFrom j`
holds, the leading minor `D_j` of `S.frameProducts` is nonzero, and `S.termDisc` is nonzero exactly
when `j = ϱ+1`, for `γ⁻¹` as for `γ`. 

### `HasCellRank.paddedLeading_mul_inv`

 If `γ` has cell rank `j` (`S.HasCellRank j γ`), then `paddedLeading j (S.frameProducts γ)`, the
first `j` rows of `S.frameProducts γ` completed by identity rows, is invertible: its product with
its inverse is `1`. 

### `HasCellRank.exists_shared_frame_vector`

 Let `γ` have cell rank `j`: the flags of the frame `f` and of `γ f` share a vector at each index
from `j` on, and the leading minor `D_j` of the matrix `Z = S.frameProducts γ` of products of `f`
with `γ f` is nonzero. The matrix `paddedLeading j Z` keeps the rows `a < j` of `Z` and has rows of
the identity elsewhere; its determinant is `D_j`, so it is invertible. For `b ≥ j`, the combination
of the columns `frameImage γ` of `γ f` whose coefficients form column `b` of its inverse is
`frameImage 1 *ᵥ w` for some `w`, so it lies in the span of `f`. 

### `HasCellRank.unique`

 A term has at most one cell rank: if `γ` has the cell ranks `j` and `j'`, then `j = j'`. With
`D_l` the leading minors of `S.frameProducts γ`, cell rank `j` means that norm-one pairs occur from
the index `j` on (`New.NormOnePairOccursFrom`), `D_j ≠ 0`, and that `𝗀(γ) = |D_{ϱ+1}|² - N² |D_ϱ|²`
is nonzero exactly when `j = ϱ + 1`. 


## The hermitian form against a moved frame

Let `k` be an isometry and `n` a vector orthogonal to `f` and `k f`.
`New.Filling.isotropicRows_conjTranspose_mul_eq` expresses the conjugate transpose of the first `ϱ`
rows of the frame Gram matrix of `k`, applied to the `e`-coordinates of `n`, through the form `T` on
the middle parts.


### `New.Filling.isotropicRows_conjTranspose_mul_eq`

 Let `T` be a Gram matrix on the middle coordinates and `k` an isometry of `T.splitGram`, the
form made of `ϱ` hyperbolic pairs `e_a`, `e*_a` around `T`. Let the columns of `n` be orthogonal to
both frames `f` and `k f`: to `A` and `k A`, and to `z` and `k z`. Then the adjoint of the first `ϱ`
rows of the matrix `T.frameGram k` of products of `f` with `k f`, times minus the `e_a`-coordinates
`n.toRows₁` of `n`, is the matrix of `T`-products of the middle coordinates `frameMiddle k` of `k f`
with the middle coordinates `n.toRows₂.toRows₁` of `n`. 


## The padded matrix with the last row of the products

For `γ` of cell rank `j`, keep the first `j` rows and the last row of the matrix of products, and
complete them by rows of the identity matrix. The determinant is the minor `S.subframeMinor j γ`,
and its norm is `minorNorm j γ` times a power of `N`. This expresses the gauges through `minorNorm`.


### `New.det_updateRow_of_mulVec_eq_single`

 If `B y` is the `i`-th basis vector, then putting `r` for the `i`-th row of `B` multiplies the
determinant by `r ⬝ᵥ y`. 

### `minorNorm_inv`

 The leading minors for `γ⁻¹` are the conjugates of those for `γ`, so their norms agree. 

### `HasCellRank.abs_norm_det_updateRow_paddedLeading`

 Let the CM field `E` have `r = numInfPlaces E` infinite places and contain a primitive `5040`-th
root of unity. Let `N = S.N` be the prime of the data `S`. Let `γ` have cell rank `j`
(`S.HasCellRank j γ`); in particular the leading minor of order `j` of `Z` is nonzero. Here
`Z = S.frameProducts γ` is the matrix of hermitian products of the frame `f = (e₁,…,e_ϱ,z)` with
`γ f`. Keep the rows `a < j` and the last row (index `𝔰.top`) of `Z`, and put rows of the identity
matrix for the others. The absolute value of the norm to `ℚ` of the determinant is
`N ^ (2 r) * S.minorNorm j γ`. 

### `HasCellRank.abs_norm_subframeMinor`

 Let the CM field `E` have `r` infinite places and contain a primitive `5040`-th root of unity.
Let `Z = S.frameProducts γ` be the matrix of products of the frame `f = (e₁, …, e_ϱ, z)` with `γ f`,
and let `γ` have the cell rank `j`: at every index `l ≥ j` (counted from `0`) the flags of `f` and
`γ f` share a vector with leading coefficients `ζ` and `1` (one `ζ` with `ζ ζ̄ = 1`), the leading
minor `D_j` of order `j` of `Z` is nonzero, and `j = ϱ + 1` exactly when `S.termDisc γ ≠ 0`. Then
the absolute norm of `S.subframeMinor j γ`, the minor of `Z` on the first `j` rows and columns and
the last one, is `N ^ (2 r) * S.minorNorm j γ`. Here `N = S.N` is the prime of the data `S`, and
`S.minorNorm j γ` is the absolute norm of `D_j`, divided by `N ^ (2 r)` when `j = ϱ + 1`. 

### `HasCellRank.subframeMinor_ne_zero`

 If `γ` has the cell rank `j`, then the minor `δ_*(γ) = S.subframeMinor j γ` of the products of
the first `j` vectors of the frame `(e₁, …, e_ϱ, z)` and its last vector `z` with their images under
`γ` is not zero. 

### `HasCellRank.minorGauge_eq`

 Let the CM field `E` have `r` infinite places and contain a primitive `5040`-th root of unity,
let `N = S.N` be the prime of the data `S`, and let `γ` have the cell rank `j`. Put
`k = S.translateByClassReps c c' γ = h_c⁻¹ γ h_c'`. Take the rows `a = 1, …, ϱ` of the matrix of
products of the frame `f = (e₁, …, e_ϱ, z)` with `k f`; `S.isotropicRowsIndex j k` is the index, in
the lattice that they span, of the lattice spanned by the first `j` of them. Then the gauge
`𝗀♯ = S.minorGauge j c c' γ` is `N ^ r * S.minorNorm j γ` divided by the product of these indices at
`k` and at `k⁻¹`. 

### `HasCellRank.maxGauge_eq`

 Let the CM field `E` have `r` infinite places and contain a primitive `5040`-th root of unity,
let `N = S.N` be the prime of the data `S`, and let `γ` have the cell rank `j`. Let `m` be the
larger of `N ^ r * S.minorNorm j γ` and `S.termDiscNorm γ`, the product of the absolute values of
`𝗀(γ) = S.termDisc γ` at the infinite places. Put
`k = S.translateByClassReps c c' γ = h_c⁻¹ γ h_c'`. Take the rows `a = 1, …, ϱ` of the matrix of
products of the frame `f = (e₁, …, e_ϱ, z)` with `k f`; `S.isotropicRowsIndex j k` is the index, in
the lattice that they span, of the lattice spanned by the first `j` of them. Then
`S.maxGauge j c c' γ` is `m` divided by the product of these indices at `k` and at `k⁻¹`. 
