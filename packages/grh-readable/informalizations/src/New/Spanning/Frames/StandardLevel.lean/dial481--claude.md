---
{
  "module": "src/New/Spanning/Frames/StandardLevel.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Frames/StandardLevel.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Frames/StandardLevel.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Place data and gauges at a finite place from the lattice of integral vectors

The estimates on the tower of unitary groups are proved for an abstract place `A` (a
`New.Floors.Place`) with a place datum (`New.Floors.PlaceData`) and a gauge (`New.Floors.Gauge`).
This file supplies these data at a finite place `New.Floors.IntegralPlace`, whose ring of integers
is `integers`, from the lattice of integral vectors. A finite place in this sense may be a finite
set of finite places read as one ring.

* `New.Floors.IntegralPlace.IsLatticeData`, `New.Floors.IntegralPlace.exists_isLatticeData`: the
  lattice datum, and its existence.
* `New.Floors.IntegralPlace.IsLargeLatticeData`,
  `New.Floors.IntegralPlace.IsLargeLatticeData.gauge`: such a datum with rank bounds, a character
  trivial on traces and a unimodular group, and its gauges.
* `New.Floors.IntegralPlace.IsLargeLatticeData.heisenbergMeasure_eq_floorModulus`,
  `New.Floors.IntegralPlace.IsLargeLatticeData.ascConv_mconv_unitaryLevel_coset`: masses of the
  congruence subgroup `K(g)` and its cosets.
* `New.Floors.IntegralPlace.IsLargeLatticeData.groupMeasure_boxSet_le`,
  `New.Floors.IntegralPlace.IsLargeLatticeData.le_partialGroupMeasure_boxSet`,
  `New.Floors.IntegralPlace.IsLargeLatticeData.isHaarMeasure_groupMeasure`: bounds for the mass of
  the group of integral isometries, and the fact that `F.groupMeasure` is a Haar measure.

The form `h` has Gram matrix `T.splitGram`: `ϱ` hyperbolic planes and a middle block `T`. The number
`ϱ` comes from the shape `𝔰`. `New.unitaryLevel integers g J` is the congruence subgroup `K(g)` of
the unitary group (integral elements congruent to `1` modulo `g`), `P.modulus u` is the factor by
which a unit `u` scales the volume, and `z` is the last vector of the frame e_0, …, e_(ϱ-1), z.

Notions from other files:
* `New.latticeMiddleGram`: The Gram matrix of X₀ ⊕ Az in the basis x_i (i ≠ k₀), v, z, where
  v = x_{k₀}/p̄ + z/N and N = p p̄.
* `New.idealZeta`: The ideal zeta sum ∑ [R : I]^(−s) over the ideals I of finite index in R, for a
  natural number s, with values in [0, ∞].
* `New.Floors.HyperbolicBasis`: A basis of the middle block made of a first hyperbolic pair, `m`
  more pairs and an orthonormal part indexed by `ι`.
* `New.Shape.Form.besselU`, `New.Shape.Form.besselH`: The block upper unitriangular isometries, and
  the isometries that fix all basis vectors outside X₀.

## Relation to the literature

See `New.Spanning.MainTerm.EnergyEstimate` for related work.


 ### The vector `x - (π π̄)⁻¹ t z` in the lattice basis 

### `vectorOfLastEntry`

 The vector x − (ππ̄)⁻¹t z of X₀ ⊕ Az, for x in `𝔰.κ → A` and t in A, written in the lattice
basis `besselLatticeBasis 𝔰 π`. 

### `form_vectorOfLastEntry`

 Let `π π̄ = N`, let `h` be the form with Gram matrix `J = (latticeMiddleGram 𝔰 N).splitGram`,
and let `e = vectorOfLastEntry π t x`. Then (a) `h(e, e) = x* x - t t̄ / (π π̄)`, and (b)
`h(z, e) = t`. 

### `continuous_vectorOfLastEntry`

 The vector `vectorOfLastEntry π t x` depends continuously on the pair `(t, x)`. 

 ### The lattice datum of integral vectors 

### `PlaceData.congruenceSubgroup`

 The principal congruence subgroup K(g) of the place datum `F`: the integral isometries congruent
to 1 modulo the unit `g = F.levelUnit`. 

### `IntegralPlace.congruentPairs`

 The pairs (ω₁, ω₂) of vectors with ω₁ integral and ω₂ ≡ ω₁ modulo g. 

### `IntegralPlace.isOpen_congruentPairs_and_isCompact_closure`

 For a unit `g` of the finite place `A`, the set `P.congruentPairs 𝔰 g` of the pairs (ω₁, ω₂)
with ω₁ and g⁻¹ (ω₁ - ω₂) integral is open, contains 0 and has compact closure. 

### `IntegralPlace.IsLatticeData`

 The place datum `F` at a finite place is the one given by the lattice of integral vectors. Its
data are integral (`integral_data`). Its box is the group `K` of integral isometries, and its close
pairs are the pairs of integral vectors congruent modulo the level. Its measures are normalised or
bounded below on `K` (`volume_le_and_boxSet_closePairs_positions_eq`). An isotropic vector is dual
to the last frame vector (`exists_isotropic`). 

### `IntegralPlace.IsLatticeData.integral_data`

 The Gram matrix is hermitian and invertible over `integers`, the basis `F.basisMatrix` is
  integral, and the unit `F.levelUnit` is integral and fixed by the involution. 

### `IntegralPlace.IsLatticeData.volume_le_and_boxSet_closePairs_positions_eq`

 The box `F.boxSet` is the group of integral isometries. Its `F.topFloorMeasure`-measure is at
  least the volume of the units of `integers`, and its `F.measureH`-measure is `1`. The close pairs
  are the pairs of integral vectors congruent modulo `F.levelUnit`. The positions `F.positions` are
  the `y⁻¹ * u * y
  * k`, with `u` in `T.besselU` and `k` in `F.congruenceSubgroup`. 

### `IntegralPlace.IsLatticeData.exists_isotropic`

 There is a vector `u` such that pairing with `u` reads the coordinate at the last frame vector
  z, and this coordinate of `u` is zero; so `u` is isotropic with h(u, z) = 1. 

### `IntegralPlace.IsLargeLatticeData`

 A lattice datum with `m + 1` further hyperbolic pairs is large if its ranks satisfy the bounds
of `zeta_le_and_le_card`, the character of the place is trivial on traces, and the unitary group is
unimodular. 

### `IntegralPlace.IsLargeLatticeData.zeta_le_and_le_card`

 The ideal zeta sum of `P.integers` at `m` has `𝔰.n`-th power at most `1 + 2⁻¹ ^ 𝔰.n`, the
  number `m` is less than `9 * 𝔰.n`, and the orthonormal part of the basis has at least `53 * 𝔰.n`
  vectors. 

### `IntegralPlace.IsLargeLatticeData.psi_add_star`

 The character of the place is trivial on traces. 

### `IntegralPlace.IsLargeLatticeData.unimodular`

 The unitary group is unimodular: some left Haar measure is right invariant. 

### `IntegralPlace.exists_right_invariant_measure_besselH`

 Let `T.G` be the unitary group of the form with middle block `T` over the finite place `A`, and
K = `unitaryLevel integers 1 T.splitGram` its subgroup of isometries over the ring of integers.
Let H = `T.besselH` be the fixer of the basis vectors outside `𝔰.κ`, and 𝖴 = `T.besselU` the group
of block upper unitriangular isometries. There is an s-finite measure on `T.G`, carried by H and
invariant under right translation by H, that gives K mass `1` and, for every `y`, gives the set
𝖴 K y⁻¹ mass at most `1`. 

### `IntegralPlace.exists_isIntMatrix_hyperbolicBasis`

 Let `N` in `P.integers` be self-conjugate and let the rank `𝔰.k` of X₀ be `|ι| + 2 m + 1`. Then
the middle block `latticeMiddleGram 𝔰 N` has an integral hyperbolic basis in which the coordinate
at z (the index `inr ()`) of a vector is its coefficient at the second vector `inl 1` of the first
pair. 

### `IntegralPlace.isIntMatrix_floorBasis`

 If a hyperbolic basis of the middle block is integral, so is the basis of each floor. 

### `HyperbolicBasis.floorBasis_mulVec_eq_zero`

 A combination of the columns of `B.floorBasis b`, the basis of the space of the floor `b`,
vanishes at every basis index whose floor (`floorOf`) is below `b`. 

### `IntegralPlace.star_dotProduct_mulVec_mem_integers`

 An integral form `J` takes values in `P.integers` on integral vectors. 

### `IntegralPlace.isIntMatrix_vecMulVec_star_vecMul`

 For an integral form `J` and integral vectors `v` and `w`, the matrix of the rank one map
`y ↦ h(w, y) v` is integral, where `h` is the form of `J`. 

### `IntegralPlace.flatChart_mem_intVectors`

 The flat chart `flatChart J β` of the quadric `h(v, v) = δ⁻¹ β` in a hyperbolic plane plus an
integral form `J`, with integral parameter `β`, maps `((t, w), a)` to an integral vector if `t` is a
unit of `P.integers` and `w` and `a` are integral. 

### `IntegralPlace.topEichler_mem_unitaryLevel_one`

 Let `T.splitGram` be unimodular over `P.integers`. Let `u` be an integral vector with
`star u ᵥ* T.splitGram` equal to the dual of the last frame vector z, and with z-coordinate `0`. Let
`e` be integral with z-coordinate `r`, a unit of `P.integers`. Then the scaled Eichler map along `u`
attached to `e` lies in `unitaryLevel P.integers 1 T.splitGram`, the group of integral
isometries. 

### `IntegralPlace.exists_measure_floorGroup_top`

 Let the form be unimodular, let `u` be an integral isotropic vector dual to the last frame
vector z, and let `B` be an integral hyperbolic basis in which the z-coordinate is the coefficient
at the second vector of the first pair. Then there is a measure `θ` on the group of the top floor
(`T.floorGroup 𝔰.ϱ`) that `orbitPoint`, the map `σ ↦ σ⁻¹ z`, carries to the measure
`B.floorQuadricMeasure` of the top quadric, and that gives the group of integral isometries mass at
least the volume of `P.intUnits`, the set of units of the ring of integers. 

### `IntegralPlace.exists_isLatticeData`

 At the finite place `P`, let `N` be in `P.integers` with `star N = N`, let `g` be a unit of `A`
in `P.integers` with `star g = g`, and let the rank `𝔰.k` of X₀ be `|ι| + 2 m + 1`. Then the matrix
`latticeMiddleGram 𝔰 N` has a place datum `F : PlaceData ι (latticeMiddleGram 𝔰 N) m` with
`P.IsLatticeData F` and `F.levelUnit = g`. 

 ### Large lattice data: gauges and masses 

### `closePairs_eq`

 The close pairs of a large lattice datum are the pairs of integral vectors congruent modulo the
level. 

### `two_le_two_div_modulus`

 An integral unit `α` of `A` has `modulus α ≤ 1`, so `2 ≤ 2 / modulus α`. 

### `inv_modulus_pow_le`

 For a unit `α` of `A`, the inverse modulus of `α ^ j` is at most `(2 / modulus α) ^ j`. 

### `idealZeta_mul_inv_modulus_pow_le`

 Let `F` be a large lattice datum with `m + 1` further pairs, so that the ideal zeta sum
`ζ = idealZeta P.integers m` is at most 2, and let `α` be an integral unit of `A`. The bound
`ζ * modulus (α ^ j) ^ (-n)`, which occurs for masses on quadrics, is at most `(2 / modulus α) ^ k`
if `j * n + 1 ≤ k`. 

### `boxSet_eq`

 The box of a large lattice datum is the group of integral isometries. 

### `isUnimodular_splitGram`

 If `F` is a large lattice datum (`P.IsLargeLatticeData F`), the Gram matrix `T.splitGram` is
hermitian and invertible over `integers`, that is, unimodular. 

### `isIntMatrix_basisMatrix`

 At a large lattice datum the basis matrix has entries in `integers`. 

### `idealZeta_le_two`

 At a large lattice datum with `m + 1` further hyperbolic pairs, the ideal zeta sum of
`P.integers` at `m` is at most `2`. 

### `star_dotProduct_splitGram_mulVec_mem`

 At a large lattice datum the form `T.splitGram` takes integral values on integral vectors. 

### `exists_kernel_isDisintegration_coordinateBox_le`

 The quadrics of a block. The place datum has m + 1 further hyperbolic pairs, so a block has rank
2 m + 4. Its volume disintegrates along the standard form into an s-finite kernel, and on each
quadric the points y with u y integral, u a unit, have mass at most ζ |u|^(-(2 m + 3)), where ζ is
the ideal zeta sum `idealZeta P.integers m`. 

### `mem_of_mem_productDifferences`

 For a large lattice datum `F`, the elements of `F.productDifferences` are integral. These are
the numbers (h(ω₁, ω'₁) - h(ω₂, ω'₂)) / g, where g = `F.levelUnit`, h is the form `T.splitGram`, and
(ω₁, ω₂), (ω'₁, ω'₂) are pairs in `F.closePairs`. 

### `exists_intGL_mulVec_mem_commonVectors`

 Let `F` be a large lattice datum, `x` an integral isometry, and `z = y⁻¹ u y k` with `u` in
`T.besselU` and `k` in `F.congruenceSubgroup`. Let `v` have `ϱ` rows, and let `σ` split
`F.FreeIndex` into `3 ϱ` excepted indices and `d` others, listed by `σ ∘ inr`. There is a matrix `V`
invertible over the integers such that every integral combination `ω` of its columns at these `d`
indices is in `F.commonVectors x z v`: `v ω = 0`, and (x⁻¹ w, (x z)⁻¹ w) is a close pair for the
vector `w = F.orthonormalPart *ᵥ ω`. 

### `exists_isCommonBound`

 Let `F` be a large lattice datum, `α` an integral unit of `A`, and `S` the sizes for which size
`j` means that `α ^ j * c` is integral. Let `x` be an integral isometry (`F.boxSet`), `z` a product
`y⁻¹ u y k` with `u` in `T.besselU` and `k` in `F.congruenceSubgroup` (`F.positions`), and
W = `F.commonVectors x z v`. Some measurable φ is an `IsCommonBound` with loss `2 / P.modulus α`:
φ(w) bounds 1 / vol ⟨w, W⟩ and the volume of the `c` with ⟨c w, W⟩ ⊆ `F.productDifferences`, and the
integral of `φ ^ F.volumeExponent` over the vectors of size `j` is at most
`(2 / P.modulus α) ^ (99 * 𝔰.n * (j + 1))`. 

### `gauge`

 The gauge of scale `α` at a large lattice datum, for an integral self-conjugate unit `α` of `A`:
a number `x` has size `j` if `α ^ j * x` is integral, and the field `loss` is `2 / P.modulus α`. 

### `leadingMinor_mem_of_isNear`

 At a large lattice datum, let `y` and `γ⁻¹ y` be near at `l`: elements of
`partialUnitriangularGroup l` move them into the group of integral isometries. Then the leading
minors of order `j ≤ l` of the matrix of the products `h(f_a, γ f_b)` of the frame vectors are
integral. 

### `exists_mul_heisenbergElem_mem_unitaryLevel_iff`

 At a large lattice datum `F`, let `g` be an integral self-conjugate unit of `A`, `a < 𝔰.ϱ`, and
`S` a subgroup of the unipotent group `unipotentBelow a` of the floors below `a`. Some `u ∈ S` moves
the point `P.heisenbergElem a (v, β)` of the Heisenberg group of floor `a` into the congruence
subgroup `unitaryLevel integers g T.splitGram` exactly when every entry of `g⁻¹ * v` and also
`g⁻¹ * β` are integral. 

### `heisenbergMeasure_eq_floorModulus`

 For a large lattice datum, an integral self-conjugate unit `g` of `A`, `a < ϱ` and a subgroup
`S` of the unipotent group `unipotentBelow a` of the floors below `a`, the set `S·K(g)` has mass
`F.floorModulus a g = modulus g ^ (𝔰.k + 1 + 2(ϱ − a − 1) + 1/2)` for the measure
`heisenbergMeasure a` of the Heisenberg group of floor `a`. 

### `ascConv_unitaryLevel`

 For a large lattice datum `F` (`P.IsLargeLatticeData F`), a self-conjugate unit `g` of `A` in
`integers`, and `j ≤ 𝔰.ϱ` (the number of hyperbolic planes), the convolution
`ascConv heisenbergMeasure j` of the Heisenberg measures `heisenbergMeasure l`, `l < j`, gives the
congruence subgroup `unitaryLevel integers g T.splitGram` the mass `∏ l < j, F.floorModulus l g`.
Each factor is
|g|^(r+1/2), where r is the rank of the vector part of floor `l`. 

### `ascConv_mconv_unitaryLevel_coset`

 Unfolding over all floors. Let `F` be a large lattice datum and `g` a self-conjugate unit of `A`
in `integers`. Write `K(g) = unitaryLevel integers g T.splitGram`. Then the convolution
`ascConv heisenbergMeasure (𝔰.ϱ + 2) ∗ₘ θ` gives the coset `K(g) c⁻¹` the mass
`∏ l < 𝔰.ϱ, F.floorModulus l g` times the `θ`-mass of `𝖴 K(g) c⁻¹`. Here `𝖴` is the Bessel unipotent
group `T.besselU`. 

### `groupMeasure_boxSet_le`

 For a large lattice datum `F` at a finite place, the box `F.boxSet`, which is the group of
integral isometries, has `F.groupMeasure`-mass at most `1 + 2⁻¹ ^ n`, where `n = ϱ + 1`. 

### `mul_le_mconv_boxSet`

 The box of a large lattice datum is a group, so its mass for a convolution `σ ∗ₘ θ` is at least
the product of its masses for `σ` and `θ`. 

### `volume_intUnits_le_weylLaw_boxSet`

 Let `F` be a large lattice datum. The measure `weylLaw l` is the image of `modulus c ^ d dc`
under `c ↦ (floorWeyl l c)⁻¹`, for a natural number `d` depending on the floor `l`. It gives the box
`F.boxSet` mass at least the volume of `P.intUnits`, the set of units of the ring of integers. 

### `le_partialGroupMeasure_boxSet`

 Let `F` be a large lattice datum at a finite place. Let `l + i = 𝔰.ϱ`. The measure
`F.partialGroupMeasure l (i + 2)` convolves the Heisenberg and floor measures of the `i + 2` floors
from `l` on. It gives the box `F.boxSet`, the group of integral isometries, mass at least
`volume P.intUnits ^ (i + 1)`. 

### `isHaarMeasure_groupMeasure`

 For a large lattice datum, `F.groupMeasure` is a Haar measure. 
