---
{
  "module": "src/Lib/DiscreteSeries/Bruhat/FloorMeasures.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Bruhat/FloorMeasures.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Bruhat/FloorMeasures.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Heisenberg elements, measures of the floors, hyperbolic bases and Plancherel at a place

Algebra and measure theory on the unitary group `G` of the form `New.Shape.Form.splitGram T`, first
over a ring with involution and a `τ` of trace one, then over a place `A` (`New.Floors.Place`),
along its floors. The basis is `e_a`, a middle block, `e*_a` (`a < ϱ`). `V_l` is spanned by the
basis vectors of floor at least `l`: for `l ≤ ϱ`, the middle block and the pairs with `l ≤ a`. `h`
is the form. The frame `f_0, …, f_ϱ` (`New.Shape.besselFrame`) is `e_0, …, e_(ϱ-1)` followed by
the last vector `z` of the middle block.

In `New.Floors.FloorGroups`, the groups `floorGroup`, `unipotentBelow`, `floorUnipotent` and
`partialUnitriangularGroup` are `G_l = U(V_l)`, `N_(<l)`, `N_l = G_l ∩ N_(<l+1)` and `Q_l`. The
group `Q_l` consists of the elements unitriangular on the first `l` frame vectors, for `l ≤ ϱ + 1`.

`∗ₘ` is convolution of measures, so `μ ∗ₘ dirac s` is the right translate of `μ` by `s`.

* `New.Floors.TraceOne.heisenbergElem`, `New.Floors.FloorGroups.exists_eq_heisenbergElem_of_mem`:
  `N_a` is a Heisenberg group, given by Eichler maps.
* `New.Floors.FloorGroups.bijOn_mulVec_eStar`: `u ↦ u e*_a` maps `N_a` bijectively onto the
  isotropic vectors `y` of `V_a` with `h(e_a, y) = 1`.
* `New.Floors.FloorGroups.existsUnique_prod_of_mem_besselU`: an element of `N_(<ϱ)` is a product in
  `N_0 ⋯ N_(ϱ-1)` with unique factors.
* `New.Floors.Place.heisenbergMeasure`, `New.Floors.ascConv`: invariant measures on `N_l` and, by
  convolution, on `N_(<j)`.
* `New.Floors.HyperbolicBasis`, `New.Floors.HyperbolicBasis.floorQuadricMeasure`: hyperbolic bases
  of `V_ϱ` and `V_b`, and measures on quadrics in `V_b`, which disintegrate the Haar measure
  (`New.Floors.HyperbolicBasis.isDisintegration_floorVolume`).
* `New.Floors.Place.plancherel_inequality`: Plancherel's inequality on `A ^ ι`.

Notions from other files:
* `New.SplitIndex`: The index set made of ϱ indices, a middle set μ, and ϱ further indices, as a
  disjoint union.
* `New.Shape.Form.splitGram`: The Gram matrix of ϱ hyperbolic planes and a middle space with Gram
  matrix T: identity blocks pair the first and last ϱ indices, T is the middle block, all else is
  zero.
* `New.Floors.FloorGroups.floorOf`: The floor of a basis index: `a` for `e_a` and `e*_a`, `ϱ` for
  `z`, `ϱ + 1` for the other middle indices.
* `New.inclMatrix`: For a map u: m → n of index sets, the n×m matrix whose j-th column is the
  standard basis vector e_{u(j)}.

## Relation to the literature

Known; see `Lib.DiscreteSeries.Bruhat.ComplexPlace` for sources.


 ### The Heisenberg groups of the floors and the Bessel subgroup 

### `_root_.New.Floors.TraceOne.heisenbergElem`

 The isometry ν(v, β) of floor a: the Eichler transformation with
e*_a ↦ e*_a + v + (β − τh(v,v))e_a, for β skew. Here v is a vector of the floors at least a + 1,
extended by zero. 

### `heisenbergElem_mulVec`

 The Heisenberg element ν(v, β) sends w to w + w(e*_a)v + ((β − τh(v, v))w(e*_a) − h(v, w))e_a.
Here w(e*_a) is the e*_a coordinate of w, and v is the vector of floors at least a + 1, extended by
zero. 

### `heisenbergElem_mem_floorUnipotent`

 Let `A` have a trace-one element τ (τ + τ̄ = 1) and let `T.splitGram` be hermitian and
invertible. For a < ϱ, a vector v on the basis indices of floor at least a + 1 and a skew-adjoint β,
the Heisenberg element ν(v, β) of floor a lies in N_a = G_a ∩ N_(<a+1). Here ν(v, β) is the Eichler
transformation e*_a ↦ e*_a + v + (β − τh(v,v))e_a, and G_a is the group of isometries fixing every
basis vector of floor below a. 

### `mul_heisenbergElem`

 Let `s` lie in `G_{a+1}` (`floorGroup (a + 1)`), the group fixing the basis vectors of floor at
most a. Let ν(v, β) = `heisenbergElem a (v, β)` be the Heisenberg isometry of floor a, where v is a
vector on the floors at least a + 1 and β is skew-adjoint. Then s ν(v, β) = ν(sv, β) s, where sv is
the block of s on the floors at least a + 1 applied to v. 

### `heisenbergElem_mul`

 The Heisenberg group law: ν(v, β)ν(v', β') = ν(v + v', β + β' + (x − x̄)), where x = τh(v', v).
Here v and v' are vectors of the floors at least a + 1, extended by zero, β and β' are skew, h is
the form of the Gram matrix, and τ is the given element with τ + τ̄ = 1.

A special case of the composition law of Eichler–Siegel transformations on the unipotent radical of
an isotropic line's stabiliser, in matrix coordinates for one floor. 

### `exists_heisenbergElem_mulVec_eq`

 An isotropic vector w that vanishes on the floors below a and has coordinate 1 at e*_a is
ν(v, β)e*_a for some Heisenberg element ν(v, β) of floor a. 

### `exists_col_eq_heisenbergElem`

 Let g lie in G_a and let i be the index of e_a or e*_a. If c times column i of g has coordinate
1 at e*_a, then it equals ν(v, β)e*_a for some Heisenberg element ν(v, β) of floor a. 

### `inv_mul_mem_floorGroup_succ`

 If g⁻¹s lies in Q_{a+1} ∩ G_a and ge*_a = se*_a, then g⁻¹s lies in G_{a+1}. 

### `exists_heisenbergElem_mem_floorGroup`

 For a < ϱ and g in Q_{a+1} ∩ G_a, there is a Heisenberg element ν(v, β) of floor a such that
g⁻¹ν(v, β) lies in G_{a+1}. 

### `exists_floorGroup_mul_floorUnipotent`

 An element of `Q_(l+1) ∩ G_l` is a product of an element of `G_(l+1)` and one of `N_l`. 

### `exists_floorGroup_mul_unipotentBelow`

 Every element s of Q_j (unitriangular on the first j frame vectors) is a product s = γν with γ
in G_j (fixing the basis vectors of floor below j) and ν in N_(<j) (`unipotentBelow j`). 

### `_root_.New.mem_besselS`

 Let `A` have a trace-one element and let the Gram matrix `T.splitGram` of the whole space be
hermitian and invertible. Then an isometry s lies in the Bessel subgroup `besselS`, the subgroup
generated by `besselU` and `besselH`, if and only if s = uh. Here u lies in `besselU`, the
isometries that are block upper unitriangular for the levels with identity middle block, and h lies
in `besselH`, the isometries fixing every basis vector of floor at most ϱ (the `e_a`, the `e*_a` and
`z`). 

### `besselS_le_normalizer_besselU0`

 If the Gram matrix of the whole space is hermitian and invertible, then the Bessel subgroup
`besselS` normalises `besselU0`, the group of the elements of `besselU` that fix the frame. 

### `unipotentBelow_induction`

 Induction along the groups N_(<j), for a hermitian invertible Gram matrix. Suppose C 0 1 holds,
and C j ν implies C (j+1) (γν) for all γ in N_j. Then C j s holds for every s in N_(<j). 

### `exists_eq_heisenbergElem_of_mem`

 Let `A` have a trace-one element τ and let `T.splitGram` be hermitian and invertible. For a < ϱ,
every g in N_a = G_a ∩ N_(<a+1) equals a Heisenberg element ν(v, β) of floor a, for some vector v on
the indices of floor at least a + 1 and some skew-adjoint β. Here ν(v, β) is the Eichler
transformation e*_a ↦ e*_a + v + (β − τh(v,v))e_a.

A weaker form of the standard parametrization of the unipotent radical of an isotropic line's
stabiliser by Eichler–Siegel transformations. It gives existence only, for one floor, without
uniqueness of parameters. 

### `bijOn_mulVec_eStar`

 The map u ↦ ue*_a is a bijection from N_a = `floorUnipotent a`, the group of Eichler maps along
e_a, onto the isotropic vectors y that vanish on the floors below a (they are orthogonal to the
first a hyperbolic planes) and have h(e_a, y) = 1. 

### `prod_ofFn_mem_unipotentBelow`

 A product x_0 ⋯ x_(j-1) with x_l in N_l = `floorUnipotent l` lies in
N_(<j) = `unipotentBelow j`. 

### `existsUnique_prod_of_mem_unipotentBelow`

 Every element of N_(<j) = `unipotentBelow j` is a product x_0 ⋯ x_(j-1) with unique factors x_l
in N_l = `floorUnipotent l`. Here N_(<j) is the group of isometries of `splitGram T` that are
unitriangular when the basis vectors of floor below `j` keep their level and all others get the
middle level ϱ, and N_l = G_l ∩ N_(<l+1). The floor of a basis vector is `a` for the a-th hyperbolic
pair, ϱ for the last vector z of the middle block, and ϱ + 1 for the other middle vectors. 

### `existsUnique_prod_of_mem_besselU`

 Every element of the unipotent group `besselU` is a product x_0 ⋯ x_(ϱ-1) with unique factors
x_l in N_l = `floorUnipotent l`, the group of Eichler maps along e_l. 

### `heisenbergElem_inv`

 Let `A` have a trace-one element τ (τ + τ̄ = 1) and let `T.splitGram` be hermitian and
invertible, with h(v, w) = v* · `T.splitGram` · w. For a < ϱ, a vector v on the indices of floor at
least a + 1 (extended by zero) and a skew-adjoint β, the inverse of the Heisenberg element ν(v, β)
of floor a is ν(−v, x − x̄ − β), where x = τh(v, v). 

### `frameMatrix_heisenbergElem`

 The Heisenberg element ν(v, β) of floor a acts on the frame by a matrix that differs from `1`
only in row a, by the products −h(v, f_c) with the frame vectors. 

### `simpleRootSum_conj_heisenbergElem`

 Let s be in G_{a+1}, so that s fixes the basis vectors of floor below a + 1. Let v be a vector
of the floors at least a + 1, extended by zero, let β be skew, and let ν(v,
β) = `heisenbergElem a (v, β)` be the Eichler transformation e*_a ↦ e*_a + v + (β − τh(v,v))e_a.
Then the sum of the entries just above the diagonal of the block of sν(v, β)s⁻¹ on the frame (f_0,
…, f_ϱ) = (e_0, …, e_(ϱ-1), z) equals −h(v, s⁻¹f_{a+1}), where s⁻¹f_{a+1} is
`orbitPoint a.succ s`. 

 ### The Haar measure of `V_l` 

### `FloorGroups.floorVolume`

 Haar measure of `V_l`, as a measure on all vectors: the image of the volume on the coordinates
of floor at least `l` under extension by zero. 

 ### Hyperbolic bases, Weyl elements and changes of coordinates 

### `HyperbolicBasis`

 A basis of the middle space `V_ϱ`, which has Gram matrix `T` and rank `𝔰.k + 1`: a first
hyperbolic pair, `m` more pairs and an orthonormal part indexed by `ι`. So there are
`card ι + 2 * m + 2` basis vectors, and the field `card_eq` equates the two counts. As the modulus
of `det T` is 1, the change of coordinates preserves volume
(`New.Floors.HyperbolicBasis.measurePreserving_mulVec`). 

### `HyperbolicBasis.basisMatrix`

 The matrix whose columns are the basis vectors. 

### `HyperbolicBasis.gram_eq`

 The Gram matrix of the basis for `T`: m + 1 hyperbolic planes and an orthonormal part. 

### `HyperbolicBasis.card_eq`

 The number of basis vectors is the rank of V_ϱ. 

### `HyperbolicBasis.modulus_det`

 The modulus of the determinant of `T` is 1. 

### `Place.weylLaw`

 The image of the measure md(c)^{d_l} dc on A under c ↦ w_l(c)⁻¹, where w_l(c) is the Weyl
element of floor l and d_l = `𝔰.k` + 1 + 2(ϱ − (l + 1)), the subtraction being truncated. 

### `measurePreserving_inclMatrix`

 Reindexing the coordinates along a bijection preserves the volume. 

### `gram_inclMatrix`

 The Gram matrix of the standard basis vectors `e_(g j)` for `J` is the submatrix of `J` on the
indices `g j`. 

### `map_inclMatrix_eq_floorVolume`

 If `f` enumerates the basis indices of `V_l` without repetition, then extension by zero along
`f` carries the volume of `n → A` to the Haar measure of `V_l`. 

### `map_inclMatrix_middle_eq_floorVolume`

 Extension by zero from the middle block carries the volume to the Haar measure of `V_ϱ`. 

### `FloorPairs`

 The indices of the hyperbolic pairs of `V_b` after the first: the `m` other pairs of `V_ϱ`, and
the pairs `e_a`, `e*_a` with `b ≤ a`. 

### `HyperbolicBasis.middleVector`

 The vector of index `j` of the basis `F` of `V_ϱ`, extended by zero to the coordinates of the
`e_a` and the `e*_a`. 

### `HyperbolicBasis.floorBasis`

 The basis of `V_b` made of the basis `F` of `V_ϱ` and the pairs `e_a`, `e*_a` with `b ≤ a`, as
the columns of a matrix. It is the block matrix of `F.basisMatrix` and the identity on these pairs,
with its rows placed among the basis indices and its columns reordered. The columns are listed in
`New.Floors.HyperbolicBasis.col_floorBasis`, and the Gram matrix is computed in
`New.Floors.HyperbolicBasis.gram_floorBasis`. 

### `HyperbolicBasis.col_floorBasis`

 The columns of `F.floorBasis b` are, in this order: the first pair of `F`; the first vectors of
the `m` other pairs of `F`, then the `e_a`; the orthonormal vectors of `F`; the second vectors of
the `m` other pairs of `F`, then the `e*_a`. 

### `HyperbolicBasis.gram_floorBasis`

 The Gram matrix of `F.floorBasis b` consists of a hyperbolic plane for the first pair, one for
each pair indexed by `FloorPairs b m`, and an orthonormal part indexed by `ι`. 

### `HyperbolicBasis.measurePreserving_mulVec`

 Multiplication by `F.basisMatrix`, the matrix of the hyperbolic basis `F` of `V_ϱ`, preserves
the volume of coordinate vectors. 

### `HyperbolicBasis.map_floorBasis_volume`

 The basis `F.floorBasis b` carries the volume of its coordinates to the Haar measure of
`V_b`. 

### `Place.heisenbergMeasure`

 The measure `η_l` on the unitary group. For `l < ϱ` it is the image of the Haar measure of
`V_(l+1)` times the skew measure of the place, under the Heisenberg parametrisation
`New.Floors.TraceOne.heisenbergElem` of `N_l`. Otherwise it is the unit mass at `1`. 

### `measurableSet_floorGroup`

 The group `G_l` is a measurable set: finitely many entries are prescribed. 

### `isClosedEmbedding_unitary_coe`

 The unitary group is closed in the space of matrices, with the subspace topology. 

### `measurable_unitary_of_coe`

 A function with values in the unitary group is measurable if it is measurable as a function
with values in matrices. 

### `measurePreserving_floor_block_mulVec`

 An element `s` of `G_l` acts on the coordinates of floor at least `l` by a block that preserves
their volume. 

### `ae_mem_floorUnipotent`

 The measure `η_l = heisenbergMeasure l` is carried by `N_l`. 

### `heisenbergMeasure_mconv_dirac`

 The measure `η_l = heisenbergMeasure l` on the unitary group `T.G` is invariant under right and
under left translation by every element `s` of `N_l = floorUnipotent l = G_l ∩ N_(<l+1)`, that is,
`η_l ∗ δ_s = η_l` and `δ_s ∗ η_l = η_l`. For `l < ϱ`, `η_l` is the image of Haar measure on
`V_(l+1)` times the skew measure under the Heisenberg parametrisation of `N_l`; otherwise it is the
unit mass at `1`. 

### `dirac_mconv_heisenbergMeasure_comm`

 Let `η_l = heisenbergMeasure l` be the measure on the unitary group `T.G` carried by the
Heisenberg group `N_l`. For `l < ϱ` it is the image of Haar measure on `V_(l+1)` times the skew
measure of the place under `heisenbergElem`, and otherwise it is the unit mass at `1`. If `s` lies
in `G_(l+1) = floorGroup (l + 1)`, the unitary elements fixing every basis vector of floor below
`l + 1`, then `dirac s ∗ₘ η_l = η_l ∗ₘ dirac s`. 

 ### Convolutions along the floors, quadric measures and Plancherel 

### `descConv`

 For measures σ_l on the unitary group, the convolution σ_{a+i−1} ∗ ⋯ ∗ σ_a in descending order
of i consecutive terms; the Dirac measure at 1 if i = 0. 

### `ascConv`

 For measures σ_l on the unitary group, the convolution σ_0 ∗ ⋯ ∗ σ_{j−1} in ascending order; the
Dirac measure at 1 if j = 0. 

### `lintegral_eq_of_dirac_mconv_eq`

 If `dirac s ∗ₘ μ = μ ∗ₘ dirac t`, then the substitution `x ↦ s⁻¹ * x * t` preserves integrals
against `μ`. 

### `lintegral_mconv_symm`

 The integral against a convolution as an iterated integral, with the right factor outside. 

### `mconv_apply_eq_lintegral`

 The mass of `Y` under `μ ∗ₘ ν` is the `ν`-integral of the mass of `Y * y⁻¹` under `μ`. 

### `ae_mem_mconv`

 The convolution of two measures carried by a measurable subgroup `S` is carried by `S`. 

### `mconv_comm_of_ae`

 If `dirac s` commutes with `ν` for `μ`-almost every `s`, then `μ` commutes with `ν` under
convolution. 

### `descConv_add`

 A descending convolution of `i + j` terms splits after the first `i` indices. 

### `descConv_succ`

 A descending convolution starting at `0` gains its next term `σ i` on the left. 

### `exists_ne_zero_of_ae`

 A function with nonzero integral is nonzero at some point where a given almost everywhere
property holds. 

### `HyperbolicBasis.floorQuadricMeasure`

 The measure on a quadric in V_b: the image of `New.Floors.Place.quadricMeasure` with parameter β
under the basis `F.floorBasis b`. By default, β is obtained from h(f_b, f_b) by `skewUnitMul`. 

### `HyperbolicBasis.isDisintegration_floorVolume`

 Let `V_b` be the span of the basis vectors of floor at least `b`, with Haar measure
`floorVolume b` (the volume on those coordinates, extended by zero). The measures
`F.floorQuadricMeasure b β`, images under the basis `F.floorBasis b` of the quadric measures with
skew parameter `β`, disintegrate this Haar measure along `h(x, x)`, where `h = T.splitGram`. 

### `exists_factor_orbitPoint`

 Let `b ≤ ϱ` and let `Z` be a nonempty standard Borel space. Let `Φ : T.G → Z` be a measurable
function that is left invariant under `Q_(b+1) ∩ G_b`, where `Q_(b+1)` is the partially
unitriangular group `partialUnitriangularGroup (b + 1)` and `G_b = floorGroup b` is the group of
isometries fixing every basis vector of floor below `b`. Then there is a measurable `Ψ` on vectors
with `Φ σ = Ψ (orbitPoint b σ)` for every `σ ∈ G_b`, where `orbitPoint b σ = σ⁻¹ f_b` and `f_b` is
the vector of index `b` in the frame `(e_0, …, e_{ϱ-1}, z)`. 

### `ae_descConv_mem`

 If every `σ l` is carried by `G_l`, then so is the descending convolution starting at `l`. 

### `ascConv_heisenbergMeasure_dirac_comm`

 Let `η_i = heisenbergMeasure i` be the measure on the unitary group `T.G` carried by the
Heisenberg group `N_i`: the image of Haar measure on `V_(i+1)` times the skew measure of the place
for `i < ϱ`, and the unit mass at `1` otherwise. Let `η_{<j} = ascConv heisenbergMeasure j` be the
convolution `η₀ ∗ ⋯ ∗ η_{j−1}`, which is the Dirac mass at `1` if `j = 0`. For every `s` in
`G_j = T.floorGroup j`, the unitary elements fixing every basis vector of floor below `j`, the Dirac
mass at `s` commutes with `η_{<j}` under convolution. 

### `ascConv_heisenbergMeasure_succ`

 η_{<j+1} = η_j ∗ η_{<j}: the last factor may be moved to the front, as η_j is carried by G_j. 

### `ascConv_heisenbergMeasure_invariant`

 Let `A` be a place and `T` a middle Gram matrix whose split Gram matrix `T.splitGram` is
hermitian and invertible. In the unitary group of `T.splitGram`, let η_{<j} = η₀ ∗ ⋯ ∗ η_{j−1} be
the ascending convolution of the Heisenberg measures. Here η_l is the image of Haar measure on
V_(l+1) times the skew measure under the parametrisation of N_l for l < ϱ, and the unit mass at 1
otherwise. Then η_{<j} ∗ δ_s = η_{<j} and δ_s ∗ η_{<j} = η_{<j} for every s in N_(<j), the group of
elements that are unitriangular when basis vectors of floor below j keep their level and all others
get the middle level. 

### `ae_ascConv_mem_unipotentBelow`

 The measure η_{<j} = η₀ ∗ ⋯ ∗ η_{j−1} is carried by `N_(<j)`. 

### `Place.lintegral_damped_fourier_le`

 Plancherel's inequality with a damping factor `∏ i, G (v i)`, for `G ≥ 0` continuous and
integrable and the additive character `ψ` of the place `A`: the constant is the `L¹` norm of the
transform of `G` (dilated by `ξ`), to the power `card ι`. 

### `Place.plancherel_inequality`

 Plancherel's inequality at a place A: for a unit η and f measurable and integrable on A^ι,
∫ |∫ ψ(η v*w) f(w) dw|² dv ≤ (c/md η)^{|ι|} ∫ |f|². Here v*w is `star v ⬝ᵥ w`, ψ is the additive
character of the place, and md is its `modulus`. The constant c = `kernelBound` is part of the data
of the place: a bound in [0, ∞] on the L¹ norm of the Fourier transform of a kernel that the place
provides. 
