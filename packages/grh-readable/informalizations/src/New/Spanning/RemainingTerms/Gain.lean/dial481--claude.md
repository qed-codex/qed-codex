---
{
  "module": "src/New/Spanning/RemainingTerms/Gain.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/RemainingTerms/Gain.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/RemainingTerms/Gain.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The gain: a discriminant bound for the common lattice of two terms over one block

Take two terms `γ`, `γ'` over one block `(c, s, c')` whose `s` agrees. The square of the
discriminant of their common lattice `L₁₂` is at most the product of their values of `S.levelGauge`,
divided by a power of `M / 2` if the links differ, and by the square of the norm of the places at
which `s` meets if the links are equal and `S.termDisc` does not vanish
(`New.Filling.pairDiscriminant_sq_le`). A block is a pair of classes `c`, `c'` with an element `s`
of the finite group `S.ResidueGL`. The element `s` agrees if the character `S.unipotentChar` takes
the same value on any two integral unipotents `u`, `u'` whose reductions satisfy `ū s = s ū'`.

The proof descends from the lattice `L⁺_γ` of each link in three steps.

* The congruence (`New.Filling.LinkSplitting.one_le_mul_linkDiscSq`): passing to the intersection of
  the two links gains a power of `M / 2`, as `γ γ'⁻¹` is `1` modulo `M` on `Λ`.
* The cut (`New.Filling.nonempty_linkSplitting`): passing to `commonLink γ γ'`, the vectors of `X₀`
  that both links send to one vector of `X₀`. This gives
  `New.Filling.torsionIndex_mul_discriminant_commonPart_le`, a bound for the parts `S.commonPart` of
  the lattices of the two terms, with the torsion indices saved.
* The index (`New.Filling.submoduleIndex_pairLattice_dvd_torsionIndex`): passing to `L₁₂` costs at
  most the torsion index of the other term.

Here `A` is the span of `e₁, …, e_ϱ`, `Λ` is the lattice of the class `c`, `M` is the level and
`L_γ = S.termLattice c c' γ`. The lattice `L⁺_γ` consists of the vectors of the link of `γ` with an
integral lift whose part in `A` is divisible by `M` (`New.Filling.HasLevelLifts`). The space `X₀`
and the line `E z` make up the middle space of the frame, and `X₀ ⊥ E z⁺` is positive definite, with
`z⁺` of norm `S.N`. The torsion index of `γ` is `S.torsionIndex (S.translateByClassReps c c' γ)`.

Notions from other files:
* `link γ`: the pairs of classes in `A^⊥ / A` of `t` and `γ⁻¹ t`, for `t` orthogonal to `A + γ A`.
* `linkIsometry γ`: the isometry `Υ_γ` of `X₀ ⊥ E z⁺` that the link of `γ` determines.
* `S.termsOver c s c'`: the rational `γ` with `h_c⁻¹ γ h_c'` in the stabilizer of the lattice and
  reducing to `s`; this product is `S.translateByClassReps c c' γ`.
* `S.HasCellRank j γ`: `γ` has cell rank `j ≤ ϱ + 1`, the top one exactly if `S.termDisc γ ≠ 0`.
* `S.levelGauge j c c' γ`: the gauge `𝗀*` of the term, a positive real bound for discriminants.


 ### Ranks 

### `linkCorank_eq_zero_iff`

 The corank `S.linkCorank γ γ'`, the codimension of the intersection of the links of `γ` and
`γ'` in each of them, vanishes exactly if the links are equal. 

### `le_finrank_commonLink_add`

 Let `γ` have cell rank `j`. The codimension in `X₀` of `commonLink γ γ'`, the space of the
vectors that both links send to one vector of `X₀`, is at most `c⁺ + (j - ϱ)`. Here
`c⁺ = S.linkCorank γ γ'` is the codimension of the intersection of the links in each of them, and
the natural number `j - ϱ` is `1` at the top rank and `0` below. 

### `termDisc_eq_zero_iff_of_link_eq`

 Let `γ` and `γ'` have cell ranks and the same link. Then `𝗀 = S.termDisc` vanishes at `γ` if and
only if it vanishes at `γ'`. 

 ### The congruence 

### `abs_norm_det_smul`

 Let `a` have absolute value `r` at every complex embedding of the CM type, and let `f` be the
number of infinite places. Multiplying an `i × i` matrix by `a` multiplies the absolute norm to
`ℚ` of its determinant by `r ^ (2 i f)`. 

### `positiveGram_posDef`

 The form of `X₀ ⊥ E z⁺` is positive definite at every complex embedding `Φ w` of the CM type. 

### `abs_norm_det_gram_sub_le`

 Let `b` and `b'` be `i` columns with the same Gram matrix in `X₀ ⊥ E z⁺`, so that `b' = u b`
for an isometry `u`. Then the absolute norm to `ℚ` of the Gram determinant of `b - b' = (1 - u) b`
is at most `4 ^ (2 i f)` times that of `b`, where `f` is the number of infinite places: at each
place the first is at most `4 ^ i` times the second in modulus. 

### `sourceCols`

 The matrix whose columns are the vectors `y₀ + λ z⁺` of `X₀ ⊥ E z⁺` attached to the columns
`(y₀ + λ' z, y₀' + λ z)` of `y`. 

### `conjTranspose_mul_mul_apply_eq_dotProduct`

 The entries of `yᴴ Q y'` are the values of the form with matrix `Q` on the columns of `y` and
`y'`. 

### `gram_linkMetric_eq_gram_sourceCols`

 Let `y` be a matrix whose columns span a submodule of `link γ`. Its Gram matrix for
`S.linkMetric`, the positive form on pairs of middle vectors, equals the Gram matrix for
`S.positiveGram` of the vectors `sourceCols y` of `X₀ ⊥ E z⁺`. 

### `gram_linkForm_eq_gram_sourceCols_sub`

 A pair of middle vectors `(y₀ + λ' z, y₀' + λ z)` has the source `y₀ + λ z⁺` and the target
`y₀' + λ' z⁺` in `X₀ ⊥ E z⁺`. Let the columns of `y` and `y'` lie in the links of `γ` and `γ'`, and
let `Υ_γ b' = Υ_γ' (sourceCols y')`. Then the products of `y` with `y'` for `S.linkForm`, the
difference of the forms on the two middle vectors, are those of `sourceCols y` with
`sourceCols y' - b'` for the form `S.positiveGram`. 

### `one_le_mul_linkDiscSq`

 Let `y v` and `y' v'` be lattices of rank `i` in the links of `γ` and `γ'`, given by rational
columns and adelic bases. Suppose that `S.linkForm`, the difference of the forms on the two middle
vectors of a pair, pairs `y` with `y'` nondegenerately and the lattices with values in `M Ô`, for
the level `M = S.M`. Then the product of their squared discriminants `S.linkDiscSq` is at least
`(M / 2) ^ (4 i f)`, where `f` is the number of infinite places. 

### `det_conjTranspose_mul_linkForm_mul_ne_zero`

 Let the columns of `m` lie in the link of `γ'` and span the link of `γ` together with those of
`y`. Let the columns of `y'` lie in the link of `γ'` and be independent modulo the intersection of
the links. Then `S.linkForm`, the difference of the forms on the two middle vectors of a pair,
pairs `y` and `y'` nondegenerately. 

### `gram_finAdeleMatrix_mul`

 Let `a w` and `b w'` be adelic combinations of the rational columns `a` and `b`. Their matrix
of products for the form `r B` is `wᴴ (r aᴴ B b) w'`, with `finAdeleMatrix` the diagonal embedding
of rational matrices into adelic ones. 

### `LinkSplitting.one_le_mul_linkDiscSq`

 **The congruence.** Let `γ`, `γ'` lie in `S.termsOver c s c'`.
`D : S.LinkSplitting c c' j x γ γ' i` splits the link of `γ` into its intersection with the link of
`γ'` and a complement of rank `i` with a lattice. `D'` does the same for `γ'`, with `j'`, `x'`. The
two lattices are paired nondegenerately by `S.linkForm`, the difference of the forms on the two
middle vectors of a pair, with values in `M Ô` for `M = S.M`. So the product of their squared
discriminants `S.linkDiscSq` is at least `(M / 2) ^ (4 i f)`, where `f = numInfPlaces E` is the
number of infinite places. 

 ### The congruence and the cut together 

### `levelGauge_pos`

 If `γ` is a term over `(c, s, c')` (it lies in `S.termsOver c s c'`) and has cell rank `j`, then
its gauge `S.levelGauge j c c' γ` is positive. 

### `torsionIndex_mul_discriminant_commonPart_le`

 **Congruence and cut.** Let `γ`, `γ'` be rational terms over one block. Let `s` agree, let `x`
be at most `S.meetNorm s`, the product of the norms of the places at which `s` meets, and let `j`,
`j'` be the cell ranks of the terms: `S.HasCellRank j γ` puts `γ` in normal form from the index `j`
on, with a nonzero leading minor of order `j` in the products of the frame with its image.

For each term multiply its torsion index `S.torsionIndex`, the index of `Λ ∩ A + k (Λ ∩ A)` in
`Λ ∩ (A + k A)` for `k = S.translateByClassReps c c' γ`, by the discriminant of `S.commonPart`, the
part of its lattice in `commonLink γ γ'`, the subspace of `X₀` common to the two links. The product
of these two numbers is at most `(2 / M) ^ (2 c⁺ f)` times the product of the gauges `S.levelGauge`:
the gauge is the larger of `S.N ^ f * minorNorm` and `termDiscNorm` of the term, divided by its two
isotropic row indices, times `M ^ (2 min(ϱ, j) f)`, `j'` for `γ'`. Here `M = S.M` is the level,
`c⁺ = S.linkCorank γ γ'` is the codimension of the intersection of the links in each and `f` is the
number of infinite places. The bound may be divided by `x ^ 2` if `c⁺ = 0` and `γ` has the top rank
`𝔰.ϱ < j`. 

 ### The index 

### `frameImage_conjTranspose_mulVec`

 Let `T` be a Gram matrix on the middle space `X₀ ⊕ ⟨z⟩` of the shape `𝔰`, and `T.splitGram` the
form of `𝔰.ϱ` hyperbolic planes `eᵢ, e*ᵢ` with `T` on the middle. Let `k` be a matrix indexed by
`𝔰.BesselIndex`. Let `a ⊕ᵥ (m ⊕ᵥ 0)` be a vector with coordinates `a` on `e₁, …, e_ϱ`, `m` on the
middle (indexed by `𝔰.MiddleIndex`) and `0` on `e*₁, …, e*_ϱ`. Its products with `frameImage k`, the
image under `k` of the frame `e₁, …, e_ϱ, z`, have two parts. One part pairs `a` with
`isotropicRows (T.frameGram k)`, the rows for `e₁, …, e_ϱ` of the matrix of products of the frame
with its image. The other part pairs `m` with `frameMiddle k`, the middle parts of that image,
through `T`. 

### `mulVec_sub_mem_colSpan_isotropicFramePair`

 Let `t` be a vector of `A ⊕ X₀` whose part `v` in `X₀` lies in `commonLink γ γ'`, the vectors of
`X₀` that are the first entry of a pair, orthogonal to `z`, lying in the links of both `γ` and `γ'`.
If `t` is orthogonal for the form `S.ratGram` to the frame `(γ e₁, …, γ e_ϱ, γ z)` of `γ`, then
`γ' γ⁻¹ t - t` lies in `A + γ' A`, the span of the columns of `isotropicFramePair γ'`. 

### `exists_sub_one_mul_eq_isotropicFramePair_mul_add`

 Let the columns of `p` lie in `commonLink γ γ'` and let those of `P` be the `e_a` and the
columns of `p`. Then `(γ' γ⁻¹ - 1) P = F W + Z Q` for some matrices `W` and `Z`. Here the columns of
`F = isotropicFramePair γ'` are the `e_a` and the `γ' e_a`, and `Q` is the matrix of products of `P`
with the frame `(γ e₁, …, γ e_ϱ, γ z)` for the form `S.ratGram`. 

### `translateByClassReps_mul_classCoord`

 The matrix `S.classCoord c`, which passes to the coordinates of the lattice of `c`, intertwines
the rational matrix `δ` with `S.translateByClassReps c c δ`. 

### `sub_one_mulVec_mem_colSpan_isotropicFramePair`

 The adelic form of `mulVec_sub_mem_colSpan_isotropicFramePair`, in the coordinates of the
lattice of `c`. Let `y` be a vector of `A ⊕ X₀` whose part in `X₀` is an adelic vector `v` of the
lattice of `commonLink γ γ'`. If `y` is orthogonal to the frame of `γ`, then `(γ' γ⁻¹ - 1) y` lies
in `A + γ' A`. Here each term acts by its `S.translateByClassReps`. 

### `map_commonPart_le`

 Let `γ` and `γ'` lie in `S.termsOver c s c'`: rational elements with `h_c⁻¹ γ h_c'` in `K` that
reduce to `s`. Work in the coordinates in which the lattice `Λ` of `c` is that of the integral
vectors and `γ'` acts by `k = S.translateByClassReps c c' γ'`. Take `v` in `S.commonPart c c' γ γ'`,
the part of `L_γ = S.termLattice c c' γ` in `commonLink γ γ'`. Its products with the frame
`(k e₁, …, k e_ϱ, k z)` are `M` times those of a vector of `Λ ∩ (A + k A)` plus `M` times those of a
vector of `Λ ∩ A`. So the image of the common part under this pairing lies in the sum of the two
lattices on the right. 

### `submoduleIndex_pairLattice_dvd_torsionIndex`

 **The index.** Let `γ`, `γ'` both lie in `S.termsOver c s c'`, with lattices `L_γ`, `L_γ'` given
by `S.termLattice`. The part of `L_γ` in `commonLink γ γ'` is `S.commonPart c c' γ γ'`, and it
contains the common lattice `L₁₂ = S.pairLattice c c' γ γ'`, the part of `L_γ ∩ L_γ'` in that space.
The index of `L₁₂` in it (`submoduleIndex`) divides the torsion index of `γ'`: the index
`S.torsionIndex` of `Λ ∩ A + k (Λ ∩ A)` in `Λ ∩ (A + k A)`, for the standard lattice `Λ`, the
isotropic space `A` and `k = S.translateByClassReps c c' γ'`. 

### `isLatticeOfRank_and_pairDiscriminant_le`

 Let `γ`, `γ'` lie in `S.termsOver c s c'` and have cell ranks `j`, `j'` (`S.HasCellRank`), where
`s` agrees (`S.Agrees`, a condition on the unipotent character). Then
`L₁₂ = S.pairLattice c c' γ γ'`, the part of `L_γ ∩ L_γ'` in `commonLink γ γ'`, is a full lattice in
that subspace, and its discriminant `S.pairDiscriminant` is at most that of `S.commonPart`, the part
of `L_γ` there, times the torsion index of `γ'`, the index of `Λ ∩ A + k (Λ ∩ A)` in `Λ ∩ (A + k A)`
for `k = S.translateByClassReps c c' γ'`. 

### `isLatticeOfRank_pairLattice`

 Suppose `s` agrees (`S.Agrees s`), and `γ`, `γ'` are terms over `(c, s, c')` with cell ranks
`j`, `j'`. Then their common lattice `S.pairLattice c c' γ γ'` is a lattice of rank
`finrank E (commonLink γ γ')`. 

### `one_le_pairDiscriminant`

 Let `γ` and `γ'` be terms over `(c, s, c')` with cell ranks `j` and `j'`, and let `s` agree
(`S.Agrees s`). Then `S.pairDiscriminant c c' γ γ'`, the discriminant of the common lattice of `γ`
and `γ'`, is at least `1`, as this lattice lies in an integral one. 

### `pairDiscriminant_sq_le`

 **Gain.** Let `γ`, `γ'` be rational terms of cell ranks `j`, `j'` over one block: two classes
`c`, `c'` and an element `s` of `S.ResidueGL` to which both reduce after translation to the lattices
of the classes. Let `s` agree and let `x` be at most `S.meetNorm s`, the product of the norms of the
places at which `s` meets (modulo such a place the spans of the frame and of its image under `s`
share a nonzero vector). The common lattice `S.pairLattice` is the part of `L_γ ∩ L_γ'` in
`commonLink γ γ'`, the subspace of `X₀` common to the two links, for the lattices `L_γ`, `L_γ'` of
the terms. Its discriminant is at most `(2 / M) ^ (c⁺ f)` times the geometric mean of the gauges
`S.levelGauge`, each the larger of `S.N ^ f * minorNorm` and `termDiscNorm`, divided by the two
isotropic row indices, times `M ^ (2 min(ϱ, j) f)`, `j'` for `γ'`. Here `M = S.M` is the level,
`c⁺ = S.linkCorank γ γ'` is the codimension in each link of the intersection of the two, and `f` is
the number of infinite places. The bound may be divided by `x` if `c⁺ = 0` and `γ` has the top rank
`𝔰.ϱ < j`. The inequality is stated squared. 

 ### The gauge of a near term 

### `IsNear.levelGauge_le`

 Let the data satisfy the standing hypotheses `S.IsAdmissible`. Let `γ` be a term of cell rank
`j` over a block. Let `γ` be near: some archimedean point `y` and `γ⁻¹ y` both lie in
`S.boxedPoints`, the reduced points of bounded Bessel length at every infinite place. Then the gauge
`S.levelGauge`, the larger of `S.N ^ f * S.minorNorm j γ` and `S.termDiscNorm γ`, divided by its two
isotropic row indices, times `M ^ (2 min(ϱ, j) f)`, is at most `S.discriminantBound = b ^ (n³ f)`.
Here `M` is the congruence level, `b = S.b` the size bound, `n = ϱ + 1` and `f` the number of
infinite places. 
