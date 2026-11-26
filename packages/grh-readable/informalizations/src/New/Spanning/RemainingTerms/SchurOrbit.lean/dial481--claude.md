---
{
  "module": "src/New/Spanning/RemainingTerms/SchurOrbit.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/RemainingTerms/SchurOrbit.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/RemainingTerms/SchurOrbit.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Schur's test for one orbit

A term is a rational point `γ` of the unitary group with
`S.translateByClassReps c c' γ = h_c⁻¹ γ h_c'` integral. Its orbit is the double coset of `γ` under
the groups `New.Filling.classUnipotent₀` of unipotent elements of level `M = S.M` that fix the
frame. The amplitude majorants of the terms of an orbit are summed by Schur's test: the mean of the
sum of the weights over the orbit is reduced to a sum over a lattice, and then to the integral of a
kernel divided by the covolume of the lattice.

Throughout, `Λ` is the lattice of the class `c`, `A` is the isotropic space spanned by `e₁, …, e_ϱ`,
and `X₀` is the positive definite part of dimension `k`. For a term of cell rank `j`
(`New.Filling.HasCellRank`) put `i = min ϱ j`. The unit frame at an infinite place is the frame
rescaled by `New.Filling.basisScale`.

Notions from other files:
* `S.frameProducts γ`: the matrix of products of the frame `e₁, …, e_ϱ, z` with its image by `γ`.
* `S.HasCellRank j γ`: in `γ` a norm-one pair occurs from `j`, its leading minor of order `j` is
  nonzero, and `S.termDisc γ` is nonzero exactly when `j = ϱ + 1`.
* `S.schurWeight c' γ i y`: the boxed cutoff of `c'` at `γ⁻¹ y` times the product over the places of
  the powers `-(k + i)` of the ratio of volumes `volumeRatio`.
* `S.tailScale`: the number `α = b ^ (k f / 4)`, where `f` is the number of infinite places.

## Main definitions and results

* `New.Filling.tsum_orbit_le_of_isLatticeTranslate`: the frames of an orbit lie in at most
  `isotropicRowsIndex ^ k` cosets of a lattice.
* `New.Filling.exists_tsum_schurWeight_le`: from cosets to the lattice.
* `New.Filling.tsum_schurIntegral_le`: from the lattice to an integral.
* `New.Filling.sq_tsum_amplitudeMajorant_doubleCoset_le`,
  `New.Filling.tsum_amplitudeMajorant_orbit_le`: the test, and its form as a bound by
  `New.Filling.orbitBound`.


### `HasCellRank.of_mem_doubleCoset`

 The terms of an orbit have the same cell rank: if `δ` lies in the double coset of `γ` under the
unipotent groups `classUnipotent₀` of `c` and `c'`, and `γ` has cell rank `j`, then so has `δ`. 

### `frameProducts_eq_of_mem_doubleCoset`

 If `δ` lies in the orbit of `γ`, the double coset under the groups `classUnipotent₀` of the
classes `c` and `c'`, then `δ` and `γ` have the same matrix of products of the frame with its
image. 

### `termsOver.of_mem_doubleCoset`

 The terms of an orbit lie over the same block `(c, s, c')`: if `γ ∈ S.termsOver c s c'` (its
translate by the class representatives is integral with residue `s`), then so is every `δ` in the
double coset of `γ` under `classUnipotent₀ c` and `classUnipotent₀ c'`. 

### `col_frameMiddle_sub_mem`

 For `δ` in the orbit of `γ`, the conjugate of each row `i` of middle coordinates of the frame
moved by `translateByClassReps c c' δ` differs from that for `γ` by `M` times an `Ô`-combination of
the conjugates of the isotropic rows of the products (`frameGram`) of the frame with its image under
`translateByClassReps c c' γ`. 

### `realFrameGram_ratToInf_congr`

 Two elements `δ`, `γ` of `S.G E` with the same matrix `frameProducts` have, at every infinite
place `v`, images `S.ratToInf δ v` and `S.ratToInf γ v` in `G₁` with the same matrix
`realFrameGram`. 

### `realFrameGram_inv_mul_ratToInf`

 If `δ` has the same matrix `frameProducts` as `γ` and `u ∈ besselU0` (a unipotent element of
`G₁` fixing each frame vector), then at every infinite place `v`, `u⁻¹ * S.ratToInf δ v` has the
same matrix `realFrameGram` as `S.ratToInf γ v`. 

### `norm_det_submatrix_realFrameGram`

 At the infinite place `v`, take the leading `j × j` minor of `realFrameGram (S.ratToInf γ v)`,
the matrix of products in the unit frame. Its modulus is
`(|realM v| ^ ∑_{a < j} (ϱ - a)) ^ 2 / N ^ j` times `‖Φ v (leadingMinor (frameProducts γ) j)‖`. So
each index `a < j` contributes the square of its scale `basisScale`, which is
`realM v ^ (ϱ - a) / √N`. 

### `HasCellRank.norm_det_subframeBlock`

 If `γ` has cell rank `j`, the determinant of the products of `e₁, …, e_i, z` (`i = min ϱ j`)
with their images, in the unit frame at `v` (the matrix `subframeBlock`), has the modulus of the
rescaled leading minor of order `j` of `S.frameProducts γ`. 

### `col_conjTranspose_mul_mem`

 A matrix product `P * M` with `P` integral has the conjugates of its rows in every `Ô`-module
that contains the conjugates of the rows of `M`. 

### `initialIsotropicIndex`

 The first `min ϱ j` indices of the isotropic vectors of the frame. 

### `shiftScaling`

 The diagonal matrix with entries `S.M / basisScale v (e_l)`, `l < min ϱ j`. It converts the
parameters of a shift, given in the rational frame, to the unit frame at the place `v`. 

### `eichlerShift`

 The shift with parameter `x`: at each infinite place, the unipotent element with central
parameter `0` that acts on `X₀` as the product of the Eichler maps along `e₁, …, e_i`,
`i = min ϱ j`, with the parameters given by the rows of `(shiftScaling j v)ᴴ * x v`: the vectors
`x_l` multiplied by the conjugates of `S.M / basisScale v (e_l)`. 

### `kernelBound`

 The bound of `RealPlace.exists_majorant_volumeRatio_inv_pow` for the integral of the kernel at
the place `v`, times the Jacobian of the passage to the parameters of `eichlerShift`. 

### `IsLatticeTranslate`

 The columns of `l` lie in `Λ ∩ X₀`, where `Λ` is the lattice of the class `c`, and modulo the
isotropic space the frame of `p` is that of `p₀` moved in `X₀` by `S.M • l` times the first
`min ϱ j` rows of the matrix of products of `γ`. 

### `eichlerShift_mem`

 At every place a shift `eichlerShift` is a unipotent element that fixes the frame. 

### `IsLatticeTranslate.frameX₀Part_eq`

 Let `p` be a lattice translate of `p₀` by `q`, for the lattice of the class `c` and the matrix
of products of `γ`. In the unit frame at the place `v`, the parts in `X₀` of the two frames
(`frameX₀Part`) differ by the conjugate transpose of the rescaled point `conjColumnsAtInfinity q`
times the first `min ϱ j` isotropic rows of products of `γ`. 

### `frameX₀Part_eichlerShift_inv_mul`

 **The shifted points.** Let `p` be a lattice translate of `p₀` by `q`, both with the matrix of
products `frameProducts γ`. Let `u` lie in `besselU0`, and let `s` be `eichlerShift j x v`. Then the
parts in `X₀` (`frameX₀Part`) of the frames of `(u s)⁻¹ p` and of `u⁻¹ p₀` at `v` differ by a
product. The first factor is the conjugate transpose of the point `conjColumnsAtInfinity q + x`,
rescaled by `shiftScaling j v`. The second factor is the first `min ϱ j` isotropic rows of products
of `γ`. 

### `frameMiddle_translateByClassReps_sub`

 Two terms with the same matrix of products differ, in the middle part of the frame, by vectors
of `X₀`: in the basis of the lattice of `c`, the difference is `S.classCoordX₀ c` times the
difference of the rational coordinates in `X₀`, taken as finite adeles. 

### `HasCellRank.det_subframeBlock_ne_zero`

 If `γ` has cell rank `j`, the products of `e₁, …, e_i, z` (`i = min ϱ j`) with their images
form an invertible matrix at every infinite place. 

### `HasCellRank.exists_isLatticeTranslate`

 Let `γ` have cell rank `j` (`HasCellRank`), let `ξ` be the first `min ϱ j` isotropic rows of
`frameProducts γ`, and let `p₀`, `p` have the same matrix of products as `γ`. Suppose the middle
parts (`frameMiddle`) of the frames moved by `translateByClassReps c c' p` and
`translateByClassReps c c' p₀` differ row by row by `M` times `Ô`-linear combinations of the rows of
`ξ`, taken as finite adeles (`finAdeleMatrix`). Then `p` is a lattice translate of `p₀`. 

### `tsum_orbit_le_of_isLatticeTranslate`

 Let `γ` have cell rank `j` and lie over the block `(c, s, c')`, let `Λ` be the lattice of the
class `c` and `A` the span of the isotropic vectors `e_a` of the frame. A term `p` is a lattice
translate of `p₀` by `l` if `l` has columns in `Λ ∩ X₀` and, modulo `A`, the frame of `p` is that of
`p₀` moved in `X₀` by `M l` times the first `min ϱ j` rows of products of `γ`. If the sum of `w` is
at most `bound` over every subset `B` of the orbit of `γ` that consists of translates of one of its
points, then the sum over the orbit is at most `isotropicRowsIndex ^ k * bound`, as the orbit falls
into at most `isotropicRowsIndex ^ k` such sets. 

### `tsum_schurWeight_fibre_le`

 Let the terms of `B` lie in the orbit of `γ` and be lattice translates of `p₀` with parameters
`l`. The frames of the terms with one lattice point `q` differ by vectors of the isotropic space. So
by packing, for `γ` over the block `(c, s, c')` and any exponent `i`, the sum of their weights
`schurWeight` at `y` is at most `tailScale` times a common bound `C` for the products over the
places of the powers `-(k + i)` of the ratios of the volumes (`volumeRatio`). 

### `HasCellRank.exists_majorant_lintegral_le_kernelBound`

 **The kernel at one place.** Let `γ` have cell rank `j`, let `i = min ϱ j`, let `y` be boxed,
and let `Z` be the matrix of products of `γ` in the unit frame at `v`. Let `g₀` have the products
`Z`, with a norm-one pair from `j`. There is a measurable `φ` on `X₀ ^ i` with integral at most
`kernelBound j γ v` such that `volumeRatio g (y v) ^ (-(k + i)) ≤ φ A` for every `g` with the same
two properties whose frame differs in `X₀` from that of `g₀` by the rescaled point `A` times the
first `i` rows of `Z`. 

### `exists_tsum_schurWeight_le`

 **From cosets to a lattice.** Let `γ` be a term of cell rank `j` over the block `(c, s, c')`,
let `i = min ϱ j` and let `Λ` be the lattice of `c`. Let `B` be a set of terms of the orbit of `γ`,
each a lattice translate of `p₀ ∈ B`: the matrix `l p` has columns in `Λ ∩ X₀` and, modulo the
isotropic space, the frame of `p` is that of `p₀` moved in `X₀` by `M * l p` times the first `i`
rows of products of `γ`. Let `u v` be unipotent and fix the frame at every place `v`, and let `y` be
boxed. There is a measurable `φ` whose integral is at most the product of the explicit numbers
`kernelBound j γ v`, which bound the integrals of its local factors, such that for every `x` the sum
over `B` of the weights `schurWeight` at `u * eichlerShift j x * y` is at most `S.tailScale` times
the sum of `φ` over the translate by `x` of the lattice `(Λ ∩ X₀) ^ i` (`columnLattice`). 

### `norm_det_shiftScaling`

 The matrix `shiftScaling j v` is diagonal with entries `M / basisScale v (e_l)` for `l < i`. The
absolute value of its determinant is `(M √N) ^ i / |realM v| ^ ∑_{a < j} (ϱ - a)`, where
`i = min ϱ j`, `M = S.M` is the level, `N = S.N` is the number with `h(z, z) = -N`, and `S.realM v`
is the ratio of consecutive scales `basisScale` of the isotropic vectors. 

### `kernelBound_le`

 Let `γ` have cell rank `j ≥ 1`, let `i = min ϱ j`, and let `δ` be the image of the leading minor
of order `j` of `S.frameProducts γ` under the chosen embedding `Φ v` at the place `v`. The number
`kernelBound j γ v`, which bounds the integral over `X₀ ^ i` of the kernel of Schur's test at `v`,
is at most `((2 ρ²) ^ (i + 1) N ^ j / |δ|) ^ i` times the main factor
`((b ^ 13 / M²) ^ i N ^ (j - ϱ) / |δ|) ^ k`. Here `ρ = frameBoxRadius = b ^ (37 n)`, and the
truncated difference `j - ϱ` is `1` at the top rank `j = ϱ + 1` and `0` below. 

### `prod_kernelBound_le`

 Let `γ` be a term of cell rank `j ≥ 1` over the block `(c, s, c')` and let `i = min ϱ j`. The
number `kernelBound j γ v` bounds the integral over `X₀ ^ i` of the kernel of Schur's test at the
place `v`. Its product over the `f` infinite places is at most
`tailScale * (b ^ 13 / M²) ^ (i k f) * minorNorm ^ (-k / 2)`, where `minorNorm` is the absolute norm
of the leading minor of order `j` of `S.frameProducts γ`, divided by `N ^ (2 f)` if `j = ϱ + 1`. 

### `tsum_schurWeight_ratToInf_mul`

 The sum of the weights `schurWeight` over the orbit of `γ` is left invariant under the
subgroup `classUnipotent₀ c`, which permutes the orbit and fixes the frame. 

### `tsum_schurIntegral_le`

 **From the lattice to an integral.** Let `γ` have cell rank `j ≥ 1` (`HasCellRank`) and lie in
`termsOver c s c'`.

One factor `schurIntegral` of Schur's test (the integral of the box cutoff of `c` times the squared
norm of the cut Bessel function times `schurWeight`), summed over the orbit of `γ`, is at most
`unipotentCovolume * #BesselCoord` times `tailScale² (b ^ 13 / M²) ^ (i k f)
(isotropicRowsIndex / √minorNorm) ^ k`. Here `i = min ϱ j`, `k = |κ|` and `f` is the number of
infinite places. Let `Λ` be the lattice of `c` and `A` the span of the isotropic vectors `e_a`. Then
`isotropicRowsIndex` is the index, in the lattice of the rows of products of `Λ ∩ A` with the frame
of `translateByClassReps c c' γ = h_c⁻¹ γ h_c'`, of the part that comes from the `e_a` with
`a < j`. 

### `sq_tsum_amplitudeMajorant_doubleCoset_le`

 **Schur's test.** Let `S` be admissible data over a CM field `E` with a primitive 5040th root of
unity, with size parameter `b`, `M = p₀ p₁` and `k = dim X₀`. Let `γ` have cell rank `j ≥ 1` and lie
over the block `(c, s, c')`. The square of the sum over its orbit of the absolute amplitudes, taken
with the cut Bessel functions `W♭` (`.cut`), is at most
`(V d τ² (b ^ 13 / M²) ^ (i k f))² (N ^ f / minorGauge) ^ k`.
Here `i = min ϱ j`, `V` is `unipotentCovolume`, the common covolume of the
unipotent groups of the classes, `d` is the number of Bessel coordinates, `τ = tailScale`, `f` is
the number of infinite places, and the gauge `minorGauge` is `N ^ f * minorNorm` divided by the two
indices `isotropicRowsIndex` of the term. 

### `div_tailScale_pow_mul_identitySecondMoment_le_cellRankSecondMoment`

 At cell rank `j ≥ 1`, the second moment `cellRankSecondMoment j` is at least `α ^ (8 - 32 i)`
times `identitySecondMoment`. Here `identitySecondMoment` is the order of the reduced image of the
Bessel subgroup `besselS` times the dimension `sourceDim` of the space of source forms, and
`cellRankSecondMoment j` is `mainSecondMoment` for `j = ϱ + 1` and `α ^ (-16)` times
`identitySecondMoment` for `j ≤ ϱ`. 

### `b_pow_div_M_sq_le`

 The field `le_M` of `S` gives `S.b ^ 19 ≤ S.M`, so the factor `S.b ^ 13 / S.M²` is at most
`1 / (S.b ^ 4 S.M)`. 

### `tsum_amplitudeMajorant_orbit_le`

 Let `γ` lie over the block `(c, s, c')` and have cell rank `j ≥ 1`, and let
`termDiscNorm γ ≤ N ^ f * minorNorm j γ`, so that `maxGauge` equals `minorGauge` at `γ`. Then the
absolute amplitudes of the terms of its orbit, taken with the cut Bessel functions `W♭` (`.cut`),
add up to at most `unipotentCovolume` times `orbitBound`, which is
`α² √(D_j / (n_p (M ^ (2 i f) x) ^ k))` at the gauge `x = maxGauge`. Here `i = min ϱ j`,
`k = dim X₀`, `D_j` is the second moment `cellRankSecondMoment j`, `n_p = pairCountScale` and
`α = tailScale`. 
