---
{
  "module": "src/New/Spanning/Frames/Levels.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Frames/Levels.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Frames/Levels.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Place data, floor measures and depth

A place datum `F` fixes a unit M, a compact set K and a basis adapted to the frame. The group
measure is built floor by floor: floor `l ≤ ϱ` chooses the frame vector f_l on its quadric and an
element of the Heisenberg group along it, and floor ϱ + 1 carries the measure of H. The letters
Y^(l), K and M are those of the head of `New.Spanning.Frames.Lengths`.

Notions from other files:
* G = `T.G` is the unitary group of `T.splitGram`, a hermitian form with ϱ = `𝔰.ϱ` hyperbolic pairs
  e_a, e*_a; its basis vectors are indexed by `𝔰.BesselIndex`, and n = `𝔰.n` is ϱ + 1.
* G^(l) = `floorGroup l` is the group of isometries that fix the basis vectors of floor below l;
  H = `besselH` is G^(ϱ+1).
* R^(l) = `partialUnitriangularGroup l` is the group of isometries that are unitriangular on the
  first l frame vectors, and U = `besselU` is the Bessel unipotent group.
* `orbitPoint b g` is the vector g⁻¹ f_b, where f_b is the frame vector of floor b, and
  `F.floorQuadricMeasure b` is the measure on the quadric through f_b.
* η_l = `heisenbergMeasure l` is the measure of the Heisenberg group of floor l, and `weylLaw l` is
  a measure carried by the inverse Weyl elements of floor l.

## Main definitions and results

* `New.Floors.PlaceData`, `New.Floors.PlaceData.floorMeasure`, `New.Floors.PlaceData.groupMeasure`:
  the data and the measures.
* `New.Floors.PlaceData.IsNear`, `New.Floors.PlaceData.IsStable`,
  `New.Floors.PlaceData.stableProducts`, `New.Floors.PlaceData.depth`,
  `New.Floors.PlaceData.depthWeight`: points near K, stable vectors, their products with e_a, depth
  and the weight.
* `New.Floors.PlaceData.measurePreserving_orbitPoint`: a floor measure maps to the measure of the
  quadric.
* `New.Floors.PlaceData.partialGroupMeasure_mconv_dirac`,
  `New.Floors.PlaceData.lintegral_partialGroupMeasure_weylElem_inv_mul`: invariance on the right,
  and invariance under a Weyl element on the left for the lower floors, for integrals of functions
  fixed on the left by G^(j), when the group measure is Haar.

## Relation to the literature

See `New.Spanning.MainTerm.EnergyEstimate` for related work.



## Place data, floor measures and their invariance

`New.Floors.descConv σ a i` is the convolution `σ (a + i - 1) ∗ ⋯ ∗ σ a`, and `η_l` is
`New.Floors.Place.heisenbergMeasure l`.


### `PlaceData`

 The data of a place: a basis of hyperbolic pairs and orthonormal vectors, the measures of the
top floor and of H, the level M (the field `levelUnit`), the close pairs of vectors, the compact set
K of the group and the set of positions. 

### `PlaceData.topFloorMeasure`

 The measure of the top floor, on G^(ϱ) = `floorGroup 𝔰.ϱ`. 

### `PlaceData.measureH`

 A right invariant measure carried by H = `besselH`; see
  `measureH_mem_and_invariant_and_le_one`. 

### `PlaceData.levelUnit`

 The level M, a unit by which differences of vectors and frequencies are divided. 

### `PlaceData.closePairs`

 The close pairs (ω₁, ω₂) of vectors. In the place data that are used they are the pairs with
  |ω₁|² + |ω₂|² < 1 at a real place, and those with ω₁ in the lattice and ω₂ ≡ ω₁ modulo M at the
  finite places. 

### `PlaceData.boxSet`

 The compact set K in the unitary group G. 

### `PlaceData.positions`

 The positions: the elements of G by which the second point of a pair differs from the
  first. 

### `PlaceData.sFinite_topFloorMeasure`

 The measure `topFloorMeasure` is s-finite. 

### `PlaceData.sFinite_measureH`

 The measure of H is s-finite. 

### `PlaceData.neZero_measureH`

 The measure of H is not zero. 

### `PlaceData.topFloorMeasure_mem_and_map_eq`

 `topFloorMeasure` is carried by G^(ϱ), and σ ↦ σ⁻¹ f_ϱ maps it to the measure of the top
  quadric. 

### `PlaceData.measureH_mem_and_invariant_and_le_one`

 The measure of H is carried by H, is invariant under right translation by H, and for every g
  gives mass at most 1 to the h with h g ∈ U K. 

### `PlaceData.star_levelUnit`

 The level is fixed by the involution. 

### `PlaceData.isOpen_closePairs_and_zero_mem_and_isCompact_closure`

 The set of close pairs is open, contains 0 and has compact closure. 

### `PlaceData.isCompact_boxSet_and_measurableSet_positions`

 The set K is compact and the set of positions is measurable. 

### `ae_topFloorMeasure_mem_floorGroup`

 The measure `F.topFloorMeasure` of the top floor is carried by G^(ϱ) = `floorGroup 𝔰.ϱ`. 

### `map_orbitPoint_topFloorMeasure`

 The map `orbitPoint 𝔰.top`, σ ↦ σ⁻¹ f_ϱ with f_ϱ = z the last frame vector, carries
`F.topFloorMeasure`, the measure of the top floor that is part of the place data `F`, to
`F.floorQuadricMeasure 𝔰.top`, the measure on the top quadric. 

### `ae_measureH_mem_besselH`

 The measure `F.measureH` is carried by H = `besselH`, the fixer of the hyperbolic pairs and the
last frame vector. 

### `measureH_mconv_dirac`

 The measure `F.measureH` is invariant under right translation by H = `besselH`. 

### `measureH_setOf_mul_mem_boxSet_le_one`

 For every g, the h with h g ∈ U K, that is u h g ∈ K for some u in U, have mass at most 1 for
`F.measureH`. Here U = `besselU` is the Bessel unipotent group and K = `F.boxSet`. 

### `floorMeasure`

 The measure θ_l of floor l on G^(l). For l ≤ ϱ the map `orbitPoint l` carries it to the quadric
measure `F.floorQuadricMeasure l`, and for l < ϱ it lives on the big cell. Floor n = ϱ + 1 carries
the measure of H, and higher floors a unit mass at 1. 

### `instance : SFinite (F.floorMeasure l)`

 Every floor measure is s-finite. 

### `partialGroupMeasure`

 `partialGroupMeasure l i` convolves the Heisenberg and floor measures of the i floors from l on.
For l + i = ϱ + 2 it is invariant under right translation by G^(l)
(`partialGroupMeasure_mconv_dirac`). 

### `groupMeasure`

 The measure (η_{ϱ+1}∗θ_{ϱ+1}) ∗ ⋯ ∗ (η₀∗θ₀) on the unitary group, the convolution over all
floors, where η_a = `heisenbergMeasure a` and θ_a = `F.floorMeasure a`. 

### `quotientMeasureFrom`

 The convolution θ_(ϱ+1) ∗ ⋯ ∗ θ_l of the floor measures from l on. It serves to integrate
functions on G^(l) that are left invariant under U ∩ G^(l). 

### `IsNear`

 A point g is near at j if R^(j) g meets K = `F.boxSet`, where R^(j) =
`partialUnitriangularGroup j`. 

### `blockRank`

 The rank 2 m + 2 of a block of orthonormal basis vectors in which the equation of a quadric is
solved. 

### `FreeIndex`

 The indices of the orthonormal basis vectors that remain when two blocks are set aside. These
vectors span the space X'. 

### `freeIndex`

 The index in ι of a basis vector of X'. These are the first `card ι - 2 * F.blockRank`
orthonormal basis vectors in a fixed numbering of ι. 

### `orthonormalPart`

 The matrix whose columns are the basis vectors of X'; it embeds X' into the space. For a vector
y, we write y_X for the vector of the products of these columns with y. 

### `IsShortFrom`

 A vector ω is short from g and g' if (g⁻¹ ω, g'⁻¹ ω) is a close pair. 

### `IsStable`

 The class of ω in Y^(l) is stable at g and g', with ω as its lift at g: the vector ω is
orthogonal to the e_b, b < l, and (g⁻¹ ω, g'⁻¹ ω') is a close pair for some ω' that agrees with ω
at all indices k with l ≤ `level k` (for l ≤ ϱ, another lift of the class). 

### `stableProducts`

 The set 𝔡_a at the points x and x y: the products ⟨e_a, ω⟩ with the vectors ω of Y^(a) that are
stable at x and x y. In the place data that are used it is a disc at a real place, and at the finite
places a fractional ideal, contained in the integers if x is near at a + 1. 

### `depth`

 The depth of the vector e_a at the points x and x y: the inverse of the volume of 𝔡_a. In the
place data that are used it is as follows. At the finite places it is the index of the ideal 𝔡_a if
x is near at a + 1 (`New.Floors.IntegralPlace.IsLargeLatticeData.exists_ideal_depth_eq`). At a real
place it is 1 / π times the infimum of |ζ|² at x plus |ζ|² at x y over the duals ζ of e_a in Y^(a)
(`New.Floors.RealPlaceSizes.depth_eq`). 

### `volumeExponent`

 The exponent s of the depths in `depthWeight`: the rank of X' minus (3 n + 1 + m). 

### `depthWeight`

 The weight of length j at the points x and x y: the product of the powers depth^(-s),
s = `F.volumeExponent`, over the first j vectors e_a. 

### `commonVectors`

 The common vectors: the ω in X' that are killed by the rows of v and are short from g
and g z. 

### `productDifferences`

 The numbers (⟨ω₁, ω'₁⟩ - ⟨ω₂, ω'₂⟩) / M for two pairs (ω₁, ω₂), (ω'₁, ω'₂) in `closePairs`. In
the place data that are used they lie in the disc of radius 1 at a real place and are integral at
the finite places. 

### `IsCommonBound`

 The function φ on X' controls the products with the set W of vectors, and its s-th power,
s = `F.volumeExponent`, has integral at most Λ^(99 n (j+1)) over the vectors of size j for the
scale `S`. 

### `IsCommonBound.measurable`

 The function φ is measurable. 

### `IsCommonBound.inv_volume_le`

 φ(u) bounds 1 / vol ⟨u, W⟩. 

### `IsCommonBound.volume_le`

 φ(u) bounds the volume of the numbers c with ⟨c u, W⟩ inside `productDifferences`. 

### `IsCommonBound.lintegral_le`

 The integral of φ^s over the vectors of size j is at most Λ^(99 n (j+1)). 

### `floorModulus`

 The number |g|^(r+1/2), where r = k + 1 + 2 (ϱ - (l + 1)) is the rank of the vector part of the
Heisenberg group of floor l; by default g is the level M. 

### `floorIndexEnum`

 The enumeration of the basis of V_a, the span of the basis vectors of floor at least a: first
the hyperbolic pair e_a, e*_a, then the basis vectors of the higher floors. 

### `upperGram`

 The Gram matrix of the basis vectors of floor at least l. 

### `floorIndexEnum_injective`

 The enumeration `floorIndexEnum a` of the basis of V_a has no repetitions. 

### `mem_range_floorIndexEnum`

 The enumeration `floorIndexEnum a` lists exactly the basis indices of floor at least a. 

### `gram_inclMatrix_floorIndexEnum`

 In the basis `floorIndexEnum a` of V_a, the form `T.splitGram` is a hyperbolic plane plus the
form `upperGram (a + 1)` on the higher floors. 

### `floorQuadricMeasure_castSucc_eq_map`

 For a < ϱ, the measure `F.floorQuadricMeasure a.castSucc` on the quadric h(v, v) = 0 of V_a can
be computed in the basis `floorIndexEnum a`. It is the image, under extension by zero, of the
measure `quadricMeasure` with parameter 0 of a hyperbolic plane plus the form `upperGram (a + 1)` on
the higher floors. 

### `inclMatrix_mulVec_flatChart_eq_heisenbergElem_mulVec`

 Let a < ϱ, let t be a unit, u a vector on the floors above a and β skew. The point ((t, t u), β)
of the chart `flatChart` of the quadric h(v, v) = 0 for a hyperbolic plane plus `upperGram (a + 1)`
is sent by `inclMatrix A (floorIndexEnum a)` to the image of e_a under the product of the Heisenberg
element `heisenbergElem a (u, β)` and the Weyl element `floorWeyl a t`. 

### `measurePreserving_orbitPoint`

 Let f be the b-th vector of the frame (e_0, …, e_{ϱ-1}, z) = `𝔰.besselFrame`. The map
`orbitPoint b`, σ ↦ σ⁻¹ f, carries the measure `F.floorMeasure b` on the isometries fixing the basis
vectors of floor below b to the measure `F.floorQuadricMeasure b` on the quadric h(v, v) = h(f, f)
in the span of the other basis vectors. 

### `measurePreserving_mulVec_orbitPoint`

 For a floor `b : Fin 𝔰.n`, that is b ≤ ϱ, and s in G^(b) = `floorGroup b`, the map σ ↦ s σ⁻¹ f,
with f the frame vector of floor b, carries the floor measure `F.floorMeasure b` to the quadric
measure `F.floorQuadricMeasure b`. 

### `ae_floorMeasure_mem`

 The measure θ_l = `F.floorMeasure l` of floor l is concentrated on the group
G^(l) = `floorGroup l`: almost every `x` lies in `floorGroup l`. 

### `lintegral_floorMeasure_congr`

 Congruence rule for integrals over floor `l`: since `F.floorMeasure l` is carried by the group
G^(l) = `floorGroup l`, the integrand may be changed outside G^(l). 

### `floorMeasure_top`

 The measure of floor `𝔰.n = ϱ + 1` is the measure of H. 

### `quotientMeasureFrom_eq_succ_mconv`

 The convolution θ_{ϱ+1} ∗ ⋯ ∗ θ_l of the floor measures from floor `l` on is the convolution
from floor `l + 1` on, convolved with θ_l = `F.floorMeasure l`. 

### `descConv_floorMeasure_succ`

 Let l < ϱ = `𝔰.ϱ`, the number of hyperbolic pairs, and let θ_a = `F.floorMeasure a`. Then
θ_{l+i} ∗ ⋯ ∗ θ_l equals `weylLaw l` ∗ (θ_{l+i} ∗ ⋯ ∗ θ_{l+1}) ∗ η_l. Here `weylLaw l` is carried by
the inverses of the elements `floorWeyl l c` that swap the lines of e_l and e*_l, and
η_l = `heisenbergMeasure l` is the Haar measure of the Heisenberg group attached to e_l. 

### `weylRatio_succ_mul_floorWeyl_inv`

 Let j < ϱ and let w_j(c) = `floorWeyl j c` be the Weyl element of floor j with unit parameter
c. The diagonal elements `weylRatio (j + 1) p q` and `weylRatio j p q`, with entries p_a / q_a at
the e_a, differ by a factor that takes w_j((p_j / q_j) c)⁻¹ to w_j(c)⁻¹. 

### `lintegral_weylRatio_mul`

 Let j ≤ ϱ = `𝔰.ϱ`, the number of hyperbolic pairs e_a, e*_a, and let `weylRatio j p q` be the
diagonal isometry that scales e_a by p_a / q_a for a < j. Left translation by it multiplies the
integral of a measurable Φ ≥ 0 for `F.quotientMeasureFrom 0`, the convolution of all the measures
`F.floorMeasure a`, by the product over a < j of |p_a / q_a| ^ (k + 2 (ϱ - a)). Here k = `𝔰.k` and
|·| is the `modulus` of the ring `A`, the factor by which a unit scales its volume. 

### `lintegral_floorMeasure_mul_right`

 Let S be a subgroup that contains G^(l) = `floorGroup l`, the isometries fixing the basis
vectors of floor below l, and let R^(l) = `partialUnitriangularGroup l` be the group of the
isometries unitriangular on the first l frame vectors. If f ≥ 0 is measurable and left invariant
under R^(l+1) ∩ S, its integral for the measure `F.floorMeasure l` on G^(l) does not change under
right translation by an element s of R^(l) ∩ S. 

### `ae_partialGroupMeasure_mem`

 The convolution `F.partialGroupMeasure l i` of the Heisenberg and floor measures of the `i`
floors from `l` on is carried by G^(l) = `floorGroup l`, the isometries fixing the basis vectors of
floor below `l`. 

### `partialGroupMeasure_mconv_dirac`

 Let η_a = `heisenbergMeasure a` and θ_a = `F.floorMeasure a`. If l + i = ϱ + 2, the convolution
(η_{ϱ+1}∗θ_{ϱ+1}) ∗ ⋯ ∗ (η_l∗θ_l) of i factors is invariant under right translation by every s in
G^(l) = `floorGroup l`. 

### `isMulRightInvariant_groupMeasure`

 The group measure, the convolution over all floors, is right invariant. 

### `partialGroupMeasure_zero_eq`

 Let η_a = `heisenbergMeasure a` and θ_a = `F.floorMeasure a`. The measure
`F.partialGroupMeasure 0 j` = (η_{j−1}∗θ_{j−1}) ∗ ⋯ ∗ (η₀∗θ₀) equals the ascending convolution η₀ ∗
⋯ ∗ η_{j−1} convolved with the descending convolution θ_{j−1} ∗ ⋯ ∗ θ₀. 

### `floorMeasure_ne_zero`

 The measure θ_l = `F.floorMeasure l` of every floor of the place datum `F` is non-zero. 

### `partialGroupMeasure_ne_zero`

 The measure `F.partialGroupMeasure l i` of the place data `F` is non-zero. It is the convolution
of the measures `heisenbergMeasure a` and `F.floorMeasure a` over the `i` floors l ≤ a < l + i.
Floor a < ϱ is the hyperbolic pair e_a, e*_a, floor ϱ is z, and floor ϱ + 1 holds the other middle
vectors. 

### `lintegral_mul_left_eq_of_factor`

 Let the measure `F.groupMeasure` on the unitary group, the convolution over all floors, be a
Haar measure and equal `ρ ∗ ν`, with `ρ` carried by the subgroup `S`, right invariant under `S` and
commuting with the unit mass at `s`. Then left translation by `s` does not change the `ν`-integral
of a measurable `Φ ≥ 0` that is invariant under left translation by `S` (`S.FixesLeft Φ`). 

### `lintegral_partialGroupMeasure_weylElem_inv_mul`

 Let `F.groupMeasure`, the convolution of the measures `heisenbergMeasure a` and
`F.floorMeasure a` over all ϱ + 2 floors a (ϱ = `𝔰.ϱ`), be a Haar measure. Let j ≤ ϱ + 2 and let `p`
be a sequence of units. Let w be the inverse of the Weyl element `weylElem j p`, which sends e_a to
p_a e*_a and e*_a to e_a / p̄_a for a < j and fixes the other basis vectors. If Φ ≥ 0 is measurable
and left invariant under G^(j) = `floorGroup j`, the isometries fixing the basis vectors of floor
below j, then Φ(w g) and Φ(g) have the same integral for the convolution `F.partialGroupMeasure 0 j`
over the floors below j. 
