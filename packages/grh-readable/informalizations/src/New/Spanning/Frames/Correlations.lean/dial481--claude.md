---
{
  "module": "src/New/Spanning/Frames/Correlations.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Frames/Correlations.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Frames/Correlations.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The scale, near points and partial correlations

The structure `New.Floors.Gauge` collects the few facts about a place that the estimates use. A
correlation is a kernel on pairs of points with a character law; integrating it over the floors from
`l` on gives the partial correlations. The letters G^(l), R^(l), U_(<l) are those of the head of
`New.Spanning.Frames.Lengths`, and K, M those of `New.Spanning.Frames.Levels`.

## Main definitions and results

* `New.Floors.Gauge`, `New.Floors.Gauge.positionsOfSize`: a scale with its constant Λ =
  `Γ.loss`, and the close positions.
* `New.Floors.PlaceData.IsPairingKernel`, `New.Floors.PlaceData.partialCorrelation`: kernels and
  partial correlations.
* `New.Floors.PlaceData.weightedSquare`, `New.Floors.PlaceData.weightedSquareIntegral`: the second
  moments of one frame.
* `New.Floors.Gauge.isBalanced_of_isNear`: near points are balanced.

Notions from other files:
* `New.Floors.PlaceData`: the data of a place, among them the level M = `F.levelUnit`, the compact
  set K = `F.boxSet` of the unitary group G = `T.G`, and the set `F.positions` of the elements by
  which the second point of a pair differs from the first.
* `New.Floors.PlaceData.IsNear`: g is near at j if R^(j) g meets K, for R^(j) =
  `partialUnitriangularGroup j`.
* `New.Floors.PlaceData.floorMeasure`, `New.Floors.PlaceData.quotientMeasureFrom`: the measure of
  floor l on G^(l) = `floorGroup l`, and the convolution of the measures of the floors from l on.
* `New.Floors.Size`: a filtration `ofSize i` of the numbers by size; a vector or a matrix has size i
  if all its entries have.

## Relation to the literature

See `New.Spanning.MainTerm.EnergyEstimate` for related work.


### `FloorMassLe`

 For every g, the integral of c(σ g) for the measure of floor j, over the σ with σ g near at
j + 1 (`IsNear`), is at most the bound `K` (a number, not the compact set `F.boxSet`). 

### `partialCorrelation`

 The correlation from floor j on: the integral of k(x g, x y) in x for `F.quotientMeasureFrom j`,
the measure on G that represents the quotient (U ∩ G^(j)) ∖ G^(j), where U = `besselU`. 

### `IsPairingKernel`

 The rules for a kernel k on G × G and an element w that commutes with G^(j). They hold for the
correlation k(g, y) = ⟪W g, W (w y)⟫ of a Bessel function W. 

### `IsPairingKernel.measurable`

 The kernel is jointly measurable. 

### `IsPairingKernel.equivariance`

 For n, n' in U_(<l) = `unipotentBelow l`, putting n before g and n' before y multiplies the
  correlation from floor l + 1 on by ψ((σ₀(w n' w⁻¹) - σ₀(n)) / M), where σ₀ = `simpleRootSum`, ψ is
  the additive character of the place and M = `F.levelUnit` is the level. 

### `IsPairingKernel.conj_eq_self`

 The element w commutes with G^(j). 

### `IsPairingKernel.exists_lintegral_le`

 The integral of |k(x g, x y)| over the floors from l on has a finite bound that does not
  depend on g and y. 

### `IsPairingKernel.isNear_of_partialCorrelation_ne_zero`

 If the correlation of g and y from floor l on is not zero, then g is near at l. 

### `invDepthWeight`

 The function of z that is the inverse of the weight `F.depthWeight j z x` of length j at the
points z and z x if z is near at j, and 0 elsewhere. 

### `pivotL1Norm`

 The integral over the σ in floor j of the modulus of the correlation of σ g and σ y from floor
j + 1 on. 

### `weightedSquare`

 The weight of length j times the squared modulus of the correlation from floor j + 1 on, both
taken at the points g and g x. 

### `weightedSquareSum`

 The function b_j(g) = ∫ (a_j + b_{j+1})(σ g) dθ_j(σ) for j < n = `𝔰.n`, and 0 for j ≥ n, where
a_j is `New.Floors.PlaceData.weightedSquare` at the position x and θ_j = `F.floorMeasure j`. 

### `weightedSquareIntegral`

 The integral of `F.weightedSquareSum k x j`, the sum of the weighted squared correlations from
floor j on, over the floors below j. 

### `Gauge`

 The data through which a gauge is used at either kind of place, for the data F: sizes of numbers
for one scale element, together with a number Λ = `loss` whose powers bound moduli and volumes, also
those of the products with close pairs. It is not the length itself: lengths at a point are bounded
by `New.Floors.Size.LengthLeAt`, and at a real place the length is `lengthAt`. The last two fields
are the facts that are proved separately at a real place and at the finite places. 

### `Gauge.loss`

 The constant Λ of the scale: losses are its powers. 

### `Gauge.isCompact_ofSize`

 The set of numbers of size j is compact. 

### `Gauge.two_le_loss`

 Λ is at least 2. 

### `Gauge.loss_ne_top`

 Λ is finite. 

### `Gauge.pairs_le`

 The number m of further hyperbolic pairs is at most 9 n. 

### `Gauge.one_le_kernelBound`

 The constant `P.kernelBound` in Plancherel's formula is at least 1. 

### `Gauge.levelUnit_mem_ofSize`

 The level M has size 1. 

### `Gauge.hasMatrixSize_basisMatrix`

 The basis has size 1. 

### `Gauge.traceOne_div_mem_ofSize`

 The element of trace one, divided by the skew unit, has size 1. 

### `Gauge.hasMatrixSize_boxSet`

 The elements of K = `F.boxSet` have size 1. 

### `Gauge.mem_vecsOfSize_of_mem_closePairs`

 For a close pair (ω₁, ω₂), the vectors ω₁ and (ω₁ - ω₂) / M have size 1. 

### `Gauge.exists_unit_smul_mem_closePairs`

 If 1 / M has size 1, some unit c with inverse of size i + 2 turns any two vectors of size i
  into a close pair. 

### `Gauge.modulus_le`

 An invertible number of size j has modulus at most Λ^j. 

### `Gauge.volume_ofSize_le`

 The numbers of size j have volume at most Λ^(j+1). 

### `Gauge.two_mul_blockRank_le`

 There is room for two blocks among the orthonormal basis vectors. 

### `Gauge.exists_blockKernel`

 The quadrics of a block, of rank p = `F.blockRank`. The volume of A^p disintegrates along the
  standard form into an s-finite kernel, each measure of which gives mass at most Λ^(p (j+1)) to
  the vectors of size j. 

### `Gauge.exists_commonBound`

 Common vectors. For g in K, a position z and ϱ linear forms on X' = `F.FreeIndex → A` (the
  rows of v), let W = `F.commonVectors g z v` be the set of vectors killed by the forms and short
  (`IsShortFrom`) from g and g z. Some φ controls the products ⟨u, ω⟩ with ω ∈ W, in the sense of
  `IsCommonBound`. 

### `Gauge.one_le_loss`

 The constant Λ of a gauge is at least 1. 

### `Gauge.leadingMinor_mem_ofSize_of_isNear`

 Let `y` and `γ⁻¹ y` be near at `l`: elements of `partialUnitriangularGroup l` move them into the
compact set `F.boxSet` of the place datum `F`. Then the leading minors of order `j ≤ l` of the
matrix `T.frameGram γ` of the products `h(e_a, γ e_b)` of the frame vectors, for the form `h` with
Gram matrix `T.splitGram`, lie in step `9 * 𝔰.n` of the filtration by size of every gauge `Γ`. 

### `Gauge.positionsOfSize`

 The close positions of a gauge Γ for the place datum F: the positions z ∈ `F.positions` for
which the matrix (z - 1) / M has size 1, where M = `F.levelUnit` is the level. 

### `isNear_mul_iff`

 Being near at j (some element of R^(j) = `partialUnitriangularGroup j` moves the point into
`F.boxSet`) does not change under left multiplication by an element ξ of R^(j). 

### `IsNear.anti`

 If g is near at i (an element of `partialUnitriangularGroup i` moves it into `F.boxSet`), it is
near at every j ≤ i, since these groups decrease with i. 

### `IsNear.of_floorGroup_mul`

 If x lies in G^(j) = `floorGroup j` and x g is near at some i ≥ j (an element of
`partialUnitriangularGroup i` moves it into `F.boxSet`), then g is near at j. 

### `measurableSet_isNear`

 The set of points of the unitary group that are near at `j` for the place datum `F` (some
element of `partialUnitriangularGroup j` moves them into the compact set `F.boxSet`) is
measurable. 

### `quotientMeasureFrom_isNear_le`

 Suppose that on each floor a < n the σ with σ g near at a + 1 (`IsNear`) have mass at most V for
`F.floorMeasure a`, whatever g is. Then for every c the g with g c near at ϱ + 2 have mass at most
V^(n-l) for the measure `F.quotientMeasureFrom l` of the floors from l on. Here n = `𝔰.n` = ϱ + 1,
and ϱ is the number of hyperbolic pairs of the shape `𝔰`. 

### `Size.mem_vecsOfSize_of_congrBelow_heisenbergElem`

 Coordinates of a Heisenberg element. Let n = `heisenbergElem a t` have the parameters
t = (ω, β) on floor a, so that (n - 1) e*_a = ω + (β - τ ⟨ω, ω⟩) e_a, where τ = `element` has trace
one and ω is extended by zero. If v differs from (n - 1) e*_a only in the coordinates e_b, b < a
(`CongrBelow`), and v / u has size i, then ω / u and (β - τ ⟨ω, ω⟩) / u have size i. 

### `isOrthogonalBelow_single_eStar`

 The vector e*_a is orthogonal to the e_b with b < a. 

### `congrBelow_sub_one_mulVec`

 For n in G^(a) = `floorGroup a` and ν in U_(<a) = `unipotentBelow a`, the vector (ν n - 1) e*_a
differs from (n - 1) e*_a only in the coordinates e_b, b < a. 

### `Size.mem_vecsOfSize_and_mem_ofSize_of_heisenbergElem`

 Let the Heisenberg element n = `heisenbergElem a t` have the parameters t = (ω, β) on floor a,
with ω extended by zero, and let τ = `element`. If (ν n - 1) e*_a / u has size i for some ν in
U_(<a) = `T.unipotentBelow a`, then ω / u and (β - τ ⟨ω, ω⟩) / u have size i. 

### `measurableSet_vecsOfSize`

 The set of vectors all of whose entries have size `j` for the gauge `Γ` is measurable. 

### `isBalanced_of_isNear`

 If the isometry g is near at j for the place datum `F`, each vector e_a (`a : Fin 𝔰.ϱ`) with
a < j is balanced at g for the gauge `Γ` of `F` with exponent 5: some lift of e_a and some dual of
e_a are moved by g⁻¹ to vectors of size 5. 

### `orbitPoint_mem_vecsOfSize`

 Coordinates of a frame vector. Let g have size i for the gauge `Γ` of the place datum `F`, let σ
lie in G^(b) = `floorGroup b`, and let σ g be near at b + 1. Then `orbitPoint b σ`, the image under
σ⁻¹ of the frame vector number b, has size i + 6. Size i means that all entries lie in
`Γ.ofSize i`. 

### `measurableSet_positionsOfSize`

 The set of close positions of the gauge `Γ` of the place datum `F`, the positions z for which
(z - 1) / M has size 1 with M = `F.levelUnit`, is measurable. 

 ### The averaged kernel 

### `stronglyMeasurable_partialCorrelation`

 For a pairing kernel `k`, the correlation from floor `l` on is jointly strongly measurable. 

### `mono`

 If `k` is a pairing kernel at floor `j`, it is one at every floor `l ≥ j`, with the same `d`. 

### `integrable_quotientMeasureFrom`

 For a pairing kernel `k`, the integral over the floors from `l` on that defines
`F.partialCorrelation l k g y` converges absolutely. 

### `integrable_quotientMeasureFrom_mconv_floorMeasure`

 For a pairing kernel `k`, the function x ↦ k(x g, x y) is integrable for the convolution of the
measure of the floors from `l + 1` on with the measure of floor `l`. 

### `integrable_partialCorrelation_succ`

 For a pairing kernel `k`, the correlation `F.partialCorrelation (l + 1) k (σ * g) (σ * y)` from
floor `l + 1` on is integrable in σ for the measure `F.floorMeasure l` of floor `l`. 

### `partialCorrelation_eq_integral_floorMeasure`

 For a pairing kernel `k`, the correlation `F.partialCorrelation l k g y` from floor `l` on is
the integral of `F.partialCorrelation (l + 1) k (σ * g) (σ * y)` in σ for the measure
`F.floorMeasure l` of floor `l`. 

### `partialCorrelation_eq_integral_succ`

 For a pairing kernel `k` with element `d` at any floor `j`, the correlation
`F.partialCorrelation l k g y` from floor `l` on is an absolutely convergent integral: that of
`F.partialCorrelation (l + 1) k (σ * g) (σ * y)` over σ against θ_l = `F.floorMeasure l`. 

### `enorm_partialCorrelation_le`

 For a pairing kernel `k`, the modulus of the correlation from floor `l` on is at most
`F.pivotL1Norm l k g y`, the integral over floor `l` of the modulus of the correlation from floor
`l + 1` on. 

### `partialCorrelation_mul_left`

 Let `k` satisfy `F.IsPairingKernel j k d` with `j ≤ l`. Then `F.partialCorrelation l k`, the
integral of k(x g, x y) in x for `F.quotientMeasureFrom l`, is unchanged when both arguments are
left translated by the same `s` in R^(l) ∩ G^(j). 
