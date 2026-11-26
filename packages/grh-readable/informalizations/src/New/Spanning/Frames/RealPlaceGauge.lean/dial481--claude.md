---
{
  "module": "src/New/Spanning/Frames/RealPlaceGauge.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Frames/RealPlaceGauge.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Frames/RealPlaceGauge.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Floor measures at the complex place: Haar measure, place datum and gauge

The group `New.Shape.G₁` is the unitary group of the complex form with basis `e_a`, `x_i` (`i : κ`),
`z`, `e*_a`. Here the `e_a, e*_a` are `ϱ` hyperbolic pairs, the `x_i` are orthonormal and
`h(z, z) = -1`. The filling argument at a place needs a place datum (`New.Floors.PlaceData`) and a
gauge (`New.Floors.Gauge`). A place datum consists of measures on the floors of a tower of
subgroups, a set of close pairs of vectors and a box; a gauge consists of sizes in which volumes are
bounded by powers of one constant. The place `ℂ` lies over a real place of the totally real field,
and the docstrings call it a real place.

## Main definitions and results

* `New.Floors.ascConv_heisenbergMeasure_eq_besselHaar`: the convolution of the measures
  `New.Floors.Place.heisenbergMeasure` on the Heisenberg groups of the floors is
  `New.Shape.besselHaar`, Lebesgue measure in the free entries of the unipotent group
  `New.Shape.Form.besselU`. Both are invariant, and the Gaussian `New.Floors.dualColumnGaussian`
  fixes the constant.
* `New.Floors.RealPlaceSizes.complexData`, `New.Floors.RealPlaceSizes.gauge`: the place datum and
  the gauge at `ℂ`.
* `New.Floors.RealPlaceSizes.haarRatio`,
  `New.Floors.RealPlaceSizes.haarRatio_ne_zero_and_groupMeasure_eq_smul`: the product measure
  `New.Floors.PlaceData.groupMeasure` over all floors is a finite positive multiple of the Haar
  measure, and the multiple is bounded by a ratio of volumes `New.volU` of compact unitary groups.
  The bound (`New.Floors.RealPlaceSizes.inv_groupMeasure_le`) compares two descriptions of the fibre
  measure of the Gram map on tuples `(y_0, y*_0, …, y_(ϱ-1), y*_(ϱ-1), y_ϱ)`: by Haar measure, and
  by choosing the vectors in turn.
* `New.Floors.RealPlaceSizes.exists_orthonormal_mul_eq_zero_and_fixed`: common subspaces of two
  points at `ℂ`, orthogonal to `n` given vectors, of each rank up to the free rank less `3 n`.
* `New.Floors.lengthAt`, `New.Floors.inducedLength`, `New.Floors.realDepth`: the Euclidean length at
  a point of `G₁`, the induced length on a quotient along the frame, and the depth of a frame vector
  as the infimum of |ζ|_g² + |ζ|_g'² over its duals ζ.
* `New.Floors.RealPlaceSizes.stableProducts_eq`, `New.Floors.RealPlaceSizes.depth_eq`: the set 𝔡_a
  (`New.Floors.PlaceData.stableProducts`) is a disc, and its inverse area
  `New.Floors.PlaceData.depth` is `New.Floors.realDepth` divided by π.

Notions from other files:
* `New.Floors.complexPlace`: The place `ℂ`: `τ = 1/2`, `δ = i/2`, `ν` the image of Lebesgue measure
  under `r ↦ r i`, modulus `‖x‖ ^ 2`, character `x ↦ exp (x - x̄)` and constant
  `kernelBound = π ^ 2`.
* `New.Floors.cellChart`: The chart of floor `l`: if `l = ϱ` and `c ≠ 0`, the boost with parameter
  `c / min 1 ‖c‖`; otherwise the Weyl element `floorWeyl l c`, which is `1` if `l ≥ ϱ` or `c = 0`.
* `New.Floors.cellLaw`: for floor l, the image of the measure with density `cellDensity 𝔰 l` on ℂ
  under `c ↦ (cellChart 𝔰 l c)⁻¹`; the chart is a Weyl element below the top floor ϱ.
* `New.Floors.PlaceData.floorMeasure`: the measure θ_l of floor l of place data; `groupMeasure` is
  𝖬 = (η_{ϱ+1} ∗ θ_{ϱ+1}) ∗ ⋯ ∗ (η₀ ∗ θ₀), with η_l = `Place.heisenbergMeasure l`.
* `New.LeGramFibre J E m`: the law of `g E` under `m` is at most the fibre measure of the Gram map
  on the tuples with the Gram matrix of `E`.

## Relation to the literature

See `Lib.DiscreteSeries.Bruhat.ComplexPlace` for sources.



## Convolution of the measures of the Heisenberg groups

The pair of index `a` has floor `a`, `z` has floor `ϱ` and the `x_i` have floor `ϱ + 1`
(`New.Floors.FloorGroups.floorOf`).


### `dualColumnGaussian`

 The Gaussian exp(−π Σ_{b<l}(Σ_i |g_{i,e*_b}|² + (Im g_{e_b,e*_b})²)) on G₁, the inner sum over
the indices i of floor greater than b. 

### `heisenbergElem_mulVec_single_eStar`

 The Heisenberg element of floor `a` with vector `v` (on the floors above `a`) and skew parameter
`β` sends `e*_a` to `e*_a + v + (β - τ h(v, v)) e_a`, where `v` is extended by zero. 

### `heisenbergElem_mulVec_single_eStar_of_lt`

 A Heisenberg element of floor `a` fixes the basis vectors `e*_b` with `b < a`. 

### `dualColumnGaussian_succ_mul_heisenbergElem`

 Let `ν` lie in the unitriangular group `unipotentBelow a` of the floors below `a`, and let `n`
be the Heisenberg element of floor `a` with vector `v` and skew parameter `β`. The Gaussian
`dualColumnGaussian` in the free entries of the columns `e*_b`, `b ≤ a`, of `ν n` is
`exp (-π (|v|² + (Im β)²))` times the Gaussian in those of the columns `e*_b`, `b < a`, of `ν`. 

### `lintegral_heisenbergMeasure_complex`

 At the place `ℂ` the measure `heisenbergMeasure a` on the Heisenberg group of floor `a < ϱ` is
the image of Lebesgue measure in `(v, r)` under the map to the Heisenberg element with vector `v`
and skew parameter `r i`. 

### `lintegral_dualColumnGaussian_ascConv`

 Let `l ≤ ϱ`. The Gaussian `dualColumnGaussian l` has integral `1` against the convolution
`η_0 ∗ ⋯ ∗ η_(l-1)` of the measures `heisenbergMeasure` of the floors below `l`. 

### `dualColumnGaussian_inv`

 For `y` in G₁, the Gaussian `dualColumnGaussian ϱ` at `y⁻¹` is the standard Gaussian in the
entries of `y` in the rows `e_a`: the complex entries at the positions `IsFreeEntry` (column `e_b`
or `e*_b` with `b > a`, or a middle column) and the imaginary parts of the entries at
`(e_a, e*_a)`. 

### `lintegral_dualColumnGaussian_inv_besselHaar`

 The function `y ↦ dualColumnGaussian ϱ y⁻¹` has integral `1` against the Haar measure
`besselHaar` of the unipotent group 𝖴 = `besselU`. 

### `ascConv_heisenbergMeasure_eq_besselHaar`

 The Haar measure `New.Shape.besselHaar` of the unipotent group 𝖴 = `besselU`, carried to G₁ by
the inclusion, is the convolution η₀ ∗ ⋯ ∗ η_{ϱ−1} of the measures
`New.Floors.Place.heisenbergMeasure` on the Heisenberg groups of the floors. 


## The place datum and the gauge at the complex place

`∗ₘ` is convolution of measures. In comments 𝖴 is the unipotent group `New.Shape.Form.besselU` and H
the image of `U(κ)` in `G₁`.


### `RealPlaceSizes`

 The numerical hypotheses at a real place on the shape `𝔰`, a box radius `ρ`, an exponent `s` and
a base `b`. Here ϱ is the number of hyperbolic planes, n = ϱ + 1, k = |κ| is the rank of the
positive summand X₀ and r the rank of the whole space: ρ = b^(6n+2) ≥ 8r with b ≥ 2,
k = s + 3n + 6 ≥ n⁷, s > 10⁹n³ and ϱ ≥ 10⁸. 

### `RealPlaceSizes.rho_eq`

 The box radius is ρ = b^(6n+2). 

### `RealPlaceSizes.eight_mul_r_le_rho`

 The box radius ρ is at least eight times the rank r. 

### `RealPlaceSizes.k_eq`

 The rank of X₀ is s + 3n + 6. 

### `RealPlaceSizes.mul_cube_lt_s`

 The exponent s exceeds 10⁹ n³. 

### `RealPlaceSizes.pow_seven_le_k`

 The rank of X₀ is at least n⁷. 

### `RealPlaceSizes.ten_pow_le_varrho`

 The number ϱ is at least 10⁸. 

### `RealPlaceSizes.two_le_b`

 The base b is at least 2. 

### `norm_apply_le_one_of_sq_add_sq_lt_one`

 If the squared Euclidean lengths of two vectors add up to less than `1`, all their entries have
modulus at most `1`. 

### `map_embedH_mconv_dirac`

 The Haar measure of the compact group `U(κ)`, carried into `𝔰.G₁` by `embedH`, is invariant
under right translation by the image of an element `u` of `U(κ)`. 

### `RealPlaceSizes.complexData`

 The place datum at `ℂ`: the unit `levelUnit = 1`, the close pairs `(ω₁, ω₂)` with
`|ω₁|² + |ω₂|² < 1` for the Euclidean length, the box `‖x‖ ≤ ρ` in operator norm, all positions
allowed, `measureH` the Haar measure of the compact group `U(κ)` carried into `𝔰.G₁`, and
`topFloorMeasure` the law `cellLaw ϱ` of floor `ϱ` convolved with `measureH`. 

### `RealPlaceSizes.haarRatio`

 A chosen constant c in [0, ∞] with 𝖬 = c · dy, where 𝖬 is the product `groupMeasure` of the
measures of all floors of the place datum at ℂ and dy is the Haar measure `volume` on G₁. 

### `RealPlaceSizes.leGramFibre_mconv_floorMeasure`

 Assume the numerical hypotheses `hF` on the ranks and the box radius, and let
`θ_l = floorMeasure l` be the measure of floor `l` of the place datum `complexData` at `ℂ`. Let `E`
be the tuple of the basis vectors of the floors below `l`, and `E'` the same tuple with the frame
vector `besselFrame l` of floor `l` added; `q` is its set of indices. If the image of `m` under
`g ↦ g E` is at most the fibre measure of the Gram map over the Gram matrix of `E` (`LeGramFibre`),
then the same holds for `E'` and the image of the product of `m` and `θ_l / 2` under
`(g, σ) ↦ g σ⁻¹ E'`. 

### `apply_of_mem_floorUnipotent`

 An element `g` of the Heisenberg group `floorUnipotent a` of floor `a` fixes `e_a` and the basis
vectors of lower floors: in these columns `k` it agrees with the identity matrix. 

### `RealPlaceSizes.leGramFibre_partialGroupMeasure`

 Assume the numerical hypotheses `hF` on the ranks and the box radius, and let `l ≤ ϱ`. For the
place datum `complexData` at `ℂ`, the measure `partialGroupMeasure 0 l` is the product
`(η_(l-1) ∗ θ_(l-1)) ∗ ⋯ ∗ (η_0 ∗ θ_0)`, where `η_a` is the measure of the Heisenberg group of floor
`a` and `θ_a` the measure of floor `a`. Its image under `g ↦ g⁻¹ (e_0, e*_0, …, e_(l-1), e*_(l-1))`,
divided by `2 ^ (2 l)`, is at most the fibre measure of the Gram map on the tuples with the Gram
matrix of the first `l` hyperbolic pairs. 

### `RealPlaceSizes.inv_groupMeasure_le`

 Assume the numerical hypotheses `hF` on the ranks and the box radius. Let `groupMeasure` be the
product of the Heisenberg and floor measures of all floors of the place datum `complexData` at `ℂ`.
Its image under inversion is at most `volU r / volU k` times the Haar measure `volume` of `G₁`. 

### `RealPlaceSizes.groupMeasure_eq_haarRatio_smul`

 The convolution `groupMeasure` of the Heisenberg and floor measures of all floors of the place
datum at `ℂ` is `haarRatio` times the Haar measure of `G₁`. 

### `RealPlaceSizes.haarRatio_le`

 Assume the numerical hypotheses `hF`. The constant `haarRatio`, the ratio of the measure
`groupMeasure` of the place datum at ℂ to the Haar measure of `G₁`, is at most `volU r / volU k`, a
ratio of volumes of unitary groups. 

### `RealPlaceSizes.lintegral_quotientMeasureFrom_eq_haarRatio_mul`

 Assume the numerical hypotheses `hF`. Let `f` be a measurable function on `G₁` that is invariant
on the left under the unipotent group 𝖴 = `besselU`. Its integral against the convolution
`quotientMeasureFrom 0` of the floor measures of the place datum `complexData` at `ℂ` is `haarRatio`
times its integral against `besselQuotMeasure`, which integrates over `𝖴 \ G₁`. 

### `RealPlaceSizes.haarRatio_ne_zero_and_groupMeasure_eq_smul`

 Assume the numerical hypotheses `hF` on the ranks and the box radius. The measure `groupMeasure`
of the place datum `complexData` at `ℂ` is a number `haarRatio`, neither `0` nor `∞`, times the Haar
measure `volume` of `G₁`. For measurable `f` invariant on the left under 𝖴, the integral of `f`
against `quotientMeasureFrom 0 = θ_(ϱ+1) ∗ ⋯ ∗ θ_0`, the product of the measures of the floors, is
`haarRatio` times its integral against `besselQuotMeasure`, the Haar measure weighted by a cutoff
for 𝖴. Moreover `haarRatio` is at most `volU r / volU k`, a ratio of volumes of unitary groups. 

### `instance : hF.complexData.groupMeasure.IsHaarMeasure`

 The measure `groupMeasure` of the place datum at `ℂ` is a Haar measure on `G₁`. 

### `volume_closedBall_pi_complex`

 The polydisc of radius `r` in `ι → ℂ` has volume `(π r²) ^ card ι`. 

### `exists_unitary_mul_submatrix_eq_zero`

 If the rank of `C` plus `d` is at most the number of columns of `C`, then some `d` columns of a
unitary matrix `Q` lie in the kernel of `C`. 

### `measurePreserving_normSq_prod_compl`

 Let `Q` be a unitary matrix and `D` a nonempty set of indices. Send `u` to the squared length of
the coordinates in `D` of `Qᴴ u` and to the other coordinates. This carries Lebesgue measure to the
product of Lebesgue measure and the measure on `r > 0` with density
`sphereDensity #D r / 2 = π ^ #D r ^ (#D - 1) / (#D - 1)!`. 

### `norm_unitary_conjTranspose_mulVec_le`

 If the entries of `u` have modulus at most `R` and `Q` is unitary, then the entries of `Qᴴ u`
have modulus at most `card ι * R`. 

### `setLIntegral_inv_pow_sphereDensity_le`

 The integral of `(36 / r) ^ s` over `0 < r ≤ R` against the density
`sphereDensity (s + 1) r / 2 = π ^ (s + 1) r ^ s / s!` is at most `4 * 3 ^ 144 * R`. 

### `exists_orthonormal_ker_lintegral_le`

 Let n = `𝔰.n` = ϱ + 1; the shape 𝔰 enters only through this number. Let C be a matrix with
s + 1 + 3 n ≤ L columns and rank at most 3 n, and let L ≥ 4. The kernel of C contains orthonormal
vectors, the columns of a matrix O, such that for every j the integral of (36 / |Oᴴ u|²)^s over the
u with entries of modulus at most L^j is at most (L²)^(99 n (j+1)). 

### `RealPlaceSizes.four_le`

 The box size `ρ` is at least 4, being at least 8 times the rank. 

### `RealPlaceSizes.norm_sq_mulVec_of_fixed`

 Let `e = orthonormalPart` be the matrix whose columns are the free orthonormal basis vectors of
the place datum at `ℂ`, and let `g` be in the unitary group `G₁` of the form of matrix `J₁`. If `J₁`
fixes `g e w`, then `g e w` and `w` have the same Euclidean length. 

### `RealPlaceSizes.norm_le_of_mem_productDifferences`

 At a real place, with `⟨u, v⟩ = star u ⬝ᵥ J₁ v`, the numbers `⟨ω₁, ω'₁⟩ - ⟨ω₂, ω'₂⟩` for two
close pairs `(ω₁, ω₂)` and `(ω'₁, ω'₂)`, which form the set `productDifferences`, have modulus at
most `1`. 

### `RealPlaceSizes.closedBall_subset_image_commonVectors`

 Assume the numerical hypotheses `hF`, and let `e = orthonormalPart` embed the span `X'` of the
free orthonormal basis vectors of the place datum at `ℂ` into the space. The common vectors are the
`w` in `X'` with `v w = 0` and `|x⁻¹ e w|² + |(x y)⁻¹ e w|² < 1`. Let the columns of `O` be
orthonormal, killed by `v`, and carried by `x⁻¹ e` and `(x y)⁻¹ e` into the space on which `J₁` is
the identity. If `r = |Oᴴ u|²` is not `0`, the products `⟨u, w⟩` with the common vectors `w` cover
the closed disc of radius `|Oᴴ u| / 2`. 

### `volume_closedBall_eq_ofReal_pi_mul_sq`

 A closed disc of radius `R ≥ 0` in `ℂ` has area `π R²`. 

### `inv_volume_le_of_closedBall_subset`

 For `t > 0`, a set `W ⊆ ℂ` that contains the closed disc of radius `√t / 2` about `0` has
`(volume W)⁻¹` at most `36 / t`. 

### `volume_le_of_subset_closedBall`

 For `t > 0`, a subset of the disc of radius `2 / √t` in `ℂ` has area at most `36 / t`. 

### `J₁_mulVec_eq_self_of_apply_eq`

 The Gram matrix `J₁` swaps `e_a` with `e*_a`, fixes the `x_i` and negates `z`. So it fixes a
vector `w` with equal coordinates at `e_a` and `e*_a` and with coordinate `0` at `z`. 

### `RealPlaceSizes.card_freeIndex_complexData`

 At `ℂ` the span `X'` of the free orthonormal basis vectors has rank `s + 1 + 3 n`. 

### `RealPlaceSizes.card_freeIndex_complexData_le`

 For the place datum `hF.complexData` at `ℂ`, the number of indices in `FreeIndex` (the
orthonormal basis vectors left when two blocks are set aside) is at most the box radius `ρ`. 

### `RealPlaceSizes.exists_rank_le_and_fixed_of_mulVec_eq_zero`

 Assume the numerical hypotheses `hF`. Let `e = orthonormalPart` embed the span `X'` of the free
orthonormal basis vectors (`FreeIndex`) of the place datum `complexData` at `ℂ` into the space. Let
`x` and `y` be in `G₁`, and let `v` be a matrix whose number of rows is at most `𝔰.n`. Then there is
a matrix `C` of rank at most `3 * 𝔰.n` such that every `w` in `X'` with `C w = 0` has `v w = 0`.
Such a `w` also has `J₁ g e w = g e w` for `g = x⁻¹` and `g = (x y)⁻¹`. 

### `RealPlaceSizes.exists_orthonormal_mul_eq_zero_and_fixed`

 Let `e = orthonormalPart` embed the span `X'` of the free orthonormal basis vectors of the place
datum at `ℂ` into the space, let `x` and `y` be in `G₁`, and let `v` be a matrix with at most `n`
rows. For every `d` up to the rank of `X'` less `3 n` there are `d` orthonormal vectors of `X'`, the
columns of `O`, that are killed by `v` and carried by `x⁻¹ e` and by `(x y)⁻¹ e` into the space on
which `J₁` is the identity. 

### `RealPlaceSizes.exists_isCommonBound`

 Let `L ≥ ρ`, and let `S` be the size in which size `j` means modulus at most `L ^ j`. Let
`W = commonVectors x y v` be the set of the `w` with `v w = 0` and `|x⁻¹ w|² + |(x y)⁻¹ w|² < 1`.
Then some measurable `φ` is a common bound for `W` with constant `L²`: `φ u` bounds the inverse area
of `⟨u, W⟩` and the area of the numbers `c` with `⟨c u, W⟩` inside `productDifferences`, a subset of
the unit disc, and the integral of `φ ^ volumeExponent` over the vectors of size `j` is at most
`(L²) ^ (99 n (j + 1))`. 

### `norm_toLp_sq_le`

 A vector of `𝔰.BesselIndex → ℂ` with entries of modulus at most `R` has squared Euclidean length
at most `r R²`, where `r` is the rank. 

### `RealPlaceSizes.smul_mem_closePairs`

 Assume the numerical hypotheses `hF` and `ρ ≤ L`. Take two vectors `ω₁`, `ω₂` indexed by
`𝔰.BesselIndex` whose entries have modulus at most `L ^ i`. Dividing both by `L ^ (i + 2)` gives a
pair in `closePairs` of the place datum `complexData` at ℂ. 

### `RealPlaceSizes.gauge`

 The gauge of scale `L ≥ ρ` for the place datum at `ℂ`: a number has size `j` if its modulus is
at most `L ^ j`, and the constant whose powers bound moduli and volumes is the field `loss`, equal
to `L²`. 

### `RealPlaceSizes.mem_gauge_ofSize_iff`

 A number has size `j` in the gauge of scale `L` if and only if its modulus is at most
`L ^ j`. 

### `RealPlaceSizes.norm_leadingMinor_le_of_isNear`

 At the place `ℂ`, let each of the points `y` and `γ⁻¹ y` be near at `l`: some element of the
partly unitriangular group `partialUnitriangularGroup l` moves it into the box of operator norm at
most `ρ`. Then the leading minors of order `j ≤ l` of `realFrameGram γ`, the matrix of the products
`h(f_a, γ f_b)` of the `n` frame vectors `f = (e_0, …, e_(ϱ-1), z)`, have modulus at most
`ρ ^ (9 n)`. 

 ### Lengths and the depth at the complex place 

### `lengthAt`

 The length of the vector y at the point g: the Euclidean length of g⁻¹ y. 

### `inducedLength`

 The length at the point g of the class of y modulo the e_b, b < l: the infimum of the lengths
at g of its lifts. 

### `realDepth`

 The depth of e_a at the points g and g': the infimum of |ζ|_g² + |ζ|_g'², for the lengths
`inducedLength` modulo the e_b, b < a, over the ζ orthogonal to these e_b with ⟨e_a, ζ⟩ = 1. The
product ⟨e_a, ζ⟩ is the coordinate of ζ at e*_a. 

### `inducedLength_sq_lt_iff`

 The squared induced length of y at g is below t exactly if some lift y' of its class modulo the
e_b, b < l, has squared length below t at g. 

### `realDepth_lt_iff`

 The depth of the basis vector e_a at the points g and g' is below t exactly if there are a
vector ζ orthogonal to the e_b, b < a, with ⟨e_a, ζ⟩ = 1 and a vector ζ' congruent to ζ modulo these
e_b such that |g⁻¹ ζ|² + |g'⁻¹ ζ'|² < t in the Euclidean length. 

### `RealPlaceSizes.mem_stableProducts_iff`

 At ℂ a number c lies in `stableProducts a x y` exactly if c = ⟨e_a, ω⟩ for a vector ω orthogonal
to the e_b, b < a, whose class modulo these e_b has a lift ω' with |ω|_x² + |ω'|_{x y}² < 1. 

### `RealPlaceSizes.stableProducts_eq`

 Assume the numerical hypotheses `hF`. For the place datum `complexData` at ℂ, the set
`stableProducts a x y` of products with e_a (see `mem_stableProducts_iff`) is the disc of the c ∈ ℂ
with ‖c‖² d < 1. Here d = `realDepth a x (x * y)` is the depth of e_a at the points x and x y. 

### `RealPlaceSizes.depth_eq`

 At ℂ the depth `PlaceData.depth a x y`, the inverse area of the set `stableProducts a x y`, is
the depth `realDepth` of e_a at the points x and x y, divided by π. 

### `RealPlaceSizes.lengthLeAt_of_lengthAt_le`

 If y has length at most L^i at g, then y has size i at g in the gauge of scale L: the entries of
g⁻¹ y have modulus at most L^i. 

### `RealPlaceSizes.lengthAt_le_of_lengthLeAt`

 Let y have size i at g in the gauge of scale L: the entries of g⁻¹ y have modulus at most L^i.
Then y has length at most √r L^i at g, where r is the rank. 
