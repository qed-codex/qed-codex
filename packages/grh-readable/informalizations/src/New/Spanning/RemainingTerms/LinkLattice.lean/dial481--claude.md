---
{
  "module": "src/New/Spanning/RemainingTerms/LinkLattice.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/RemainingTerms/LinkLattice.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/RemainingTerms/LinkLattice.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The lattice of a link

Let `γ` be a term of cell rank `j`, `Λ` the lattice of a class, `A` the span of `e₁, …, e_ϱ`,
`I = A ∩ γ A`, `z` the last vector of the frame, of norm `-N`, and `M = S.M` the level of the
congruence group. The vectors of `Λ` orthogonal to `A` and `γ A` give a lattice `L¹` in the link of
`γ`, and those whose `e_a`-coordinates are divisible by `M` give the lattice `L⁺_γ`. The lattice
`L¹` is realized as an orthogonal complement: adjoin two vectors `z'`, `z''` of norm `N` to the
unimodular lattice `(Λ ∩ I^⊥)/(Λ ∩ I)` (`New.IsQuotientBasis`), and take the complement of the
isotropic lists `(e_a, z + z')` and `(γ e_a, γ z + z'')`, `a < j`.

Notions from other files:
* `linkMatrix γ` sends `t` to the middle coordinates of `t` and `γ⁻¹ t`; `link γ` is its image of
  the orthogonal complement of `A + γ A`.
* `HasCellRank j γ` says that `γ` has cell rank `j`: `NormOnePairOccursFrom j γ`, the leading
  `j`-minor of the products of the two frames is nonzero, and `S.termDisc γ ≠ 0` exactly when
  `j = ϱ + 1`.
* `isotropicRowsIndex j k` is the index, among the products of `Λ ∩ A` with the frame of `k`, of
  those from the `e_a`, `a < j`; `torsionIndex k` is the index of the lattice spanned by the
  `e_a` and `k e_a` in the integral vectors of their span.
* `isotropicFramePair γ` has the columns `e₁, …, e_ϱ` and their images under `γ`.
* `New.Filling.IsOrthogonalLift` (earlier file): vectors orthogonal to `A` and `γ A` over the
  columns of `(0 | v)`, whose first columns are a basis of `I`.

## Main definitions and results

* `New.Filling.exists_lifts_linkDiscSq_le`: the discriminant of `L¹`.
* `New.Filling.exists_hasLevelLifts_linkDiscSq_le`: the discriminant of `L⁺_γ`.


 ### The discriminant of `L¹` 

### `IsOrthogonalLift.exists_basis_orthogonal`

 The first columns of an orthogonal lift, a basis of `I = A ∩ γ A`, extend to a basis of `I^⊥`
over `E` for the form `S.ratGram`: for some `y` the columns of `(u₁ | y)`, with `u₁` these first
columns, have a left inverse, are orthogonal to `I`, and are as many as the dimension of `I^⊥`. 

### `classOf`

 The coordinates of the classes modulo `I` of the rational vectors `t`, where `q` reads the
coordinates in `(Λ ∩ I^⊥)/(Λ ∩ I)` for the lattice `Λ` of the class `c`. 

### `classCoord_orthogonal`

 Let the first columns `u₁` of `u` span `I`. If the rational vectors `t` are orthogonal to `I`,
then in the lattice coordinates `S.classCoord c` of the class `c` they are orthogonal to every
adelic basis `u₁ a` of `I`. 

### `gram_classOf`

 Let `c` be a class in `S.Classes`, `Λ` its lattice, and `I` the span of the first columns
`u.toCols₁` of the rational matrix `u`. In `S.classCoord c`-coordinates, the invertible `a` turns
`u.toCols₁` into a basis of `Λ ∩ I`. Let `B` be a basis of `(Λ ∩ I^⊥)/(Λ ∩ I)` with coordinates `q`.
Take rational `t`, `t'` orthogonal to `I` for `S.ratGram`. Then their classes `classOf c q t`,
`classOf c q t'` have products for `Bᴴ * splitGram * B` equal to `tᴴ * S.ratGram * t'`, embedded in
the finite adeles by `finAdeleMatrix`. 

### `IsOrthogonalLift.toCols₁_mul_toCols₂`

 If `u` is an orthogonal lift (`New.Filling.IsOrthogonalLift`), its first columns, a basis of
`I = A ∩ γ A`, are orthogonal to the others for the form `S.ratGram`. 

### `IsOrthogonalLift.toCols₁_mul_isotropicFramePair`

 The first columns of an orthogonal lift are orthogonal to the `e_a` and the `γ e_a`. 

### `IsOrthogonalLift.toCols₁_mul_lastPair`

 The first columns of an orthogonal lift are orthogonal to `z` and `γ z`, for `z` the last
vector of the frame. 

### `classCoord_mul_listPair`

 In the lattice coordinates of the class `c`, the vectors `e_a`, `γ e_a`, `a < j`, are the
vectors `e_a`, `k e_a` for `k = S.translateByClassReps c c' γ`. 

### `IsOrthogonalLift.exists_mul_classOf_eq_and_linkMatrix_mul_eq`

 Let `u` be an orthogonal lift of `v`, and let `B` be a basis with coordinates `q` of the
quotient `(Λ ∩ I^⊥)/(Λ ∩ I)` of the lattice `Λ` of the class `c`. The representatives `B q t` of the
classes of the lifts `t = u.toCols₂` of `v` are adelic combinations `u w` of the columns of `u`, and
`linkMatrix γ` again sends them to the columns of `v`. 

### `IsOrthogonalLift.col_mem_colLattice_isotropicFramePair`

 Let `u` be an orthogonal lift of `v` at `j`. Its first columns `u₁ = u.toCols₁`, one for each
`b ≥ j`, then lie in `A`. Let `a` be an invertible matrix over the finite adeles `𝔸f E`. Write the
columns of `u₁ a` in the basis of the lattice of `c`, by `S.classCoord c`, and suppose that their
entries lie in the ring `Ô E` of integral finite adeles. Then for every `k` in the finite-adelic
unitary group, each of these columns lies in the `Ô E`-span `colLattice` of the columns
`e₁, …, e_ϱ, k e₁, …, k e_ϱ` of `isotropicFramePair k`. 

### `IsOrthogonalLift.gram_classOf_add_border`

 Let `u` be an orthogonal lift of `v`, and let `B` be a basis with coordinates `q` of the
quotient `(Λ ∩ I^⊥)/(Λ ∩ I)`, with Gram matrix `J₀`. Let `p` be the classes of `z` and `γ z`, for
`z` the last vector of the frame, of norm `-N`. When `J₀` is bordered to `J₀ + N⁻¹ J₀ p p* J₀`, the
classes of the lifts `u.toCols₂` have the Gram matrix of `v` for `S.linkMetric`, the form on pairs
of middle coordinates that is half the sum of the two middle forms plus `N⁻¹` times the norms of the
products with `z`. 

### `IsOrthogonalLift.linkDiscSq_mul_sq_eq`

 **Jacobi's identity in the quotient.** Let the columns of `v` have the orthogonal lifts `u`, let
`k = S.translateByClassReps c c' γ` be the finite-adelic form of `γ`, and let `B` be a basis with
coordinates `q` of `(Λ ∩ I^⊥)/(Λ ∩ I)`. Suppose that `γ` has cell rank `j`, that the frame pair of
`k` is integral, that the rank of the quotient is twice the number of indices `i < j` plus the
number of columns of `v`, and that the classes of the lifts of `v e` form a primitive matrix. Let
`F` be the classes of the `e_i` and `k e_i` with `i < j`, and `latticeIndex` the index of their
lattice in the integral vectors of their span. Then the squared discriminant `S.linkDiscSq v e` of
the lattice with basis `v e` times `latticeIndex ^ 2` is the square of `S.minorNorm j γ`, the
normalized norm of the leading minor of order `j` of the frame products of `γ`, and `F` spans the
classes of all `e_i` and `k e_i`. 

### `exists_lifts_linkDiscSq_le`

 Let `γ` be a rational element of cell rank `j` whose adelic form
`k = S.translateByClassReps c c' γ` keeps the standard lattice `Λ₀` and has the image `t` under the
reduction map `S.reduction` to the finite group `S.ResidueGL`. Let the columns of `v` be a basis of
the link of `γ`, and let `A` be the span of the isotropic `e₁, …, e_ϱ`. Let `w` be the product of
three lattice indices: `isotropicRowsIndex j k`, the same for `k⁻¹`, and `torsionIndex k`. Then for
some invertible finite-adelic `e` the columns of `v e` have integral lifts, and the squared
discriminant `linkDiscSq` of their lattice, times `w ^ 2`, is at most the square of
`S.minorNorm j γ`, which is `Nm (S.subframeMinor j γ) / N ^ (2 f)` for `-N` the norm of the last
frame vector and `f` the number of infinite places. Moreover `w ≠ 0`, that is, the three indices are
finite. 

### `isotropicRowsIndex_mul_torsionIndex_ne_zero`

 For a term `γ` of cell rank `j` from `c'` to `c`, with reduction `s`, the lattice indices
`isotropicRowsIndex` at `k = h_c⁻¹ γ h_c'` and at `k⁻¹` and `torsionIndex` at `k` are finite,
that is, nonzero (an infinite index is `0`). 

### `isotropicRowsIndex_pos`

 For a term of cell rank `j`, the index `isotropicRowsIndex` at `h_c⁻¹ γ h_c'` is finite, hence
positive. 

### `isotropicRowsIndex_inv_pos`

 For a term of cell rank `j`, the index `isotropicRowsIndex` at the inverse of `h_c⁻¹ γ h_c'` is
finite, hence positive. 

### `torsionIndex_pos`

 For a term `γ` over `(c, s, c')` (`termsOver`) of cell rank `j`, the index `torsionIndex` at
`h_c⁻¹ γ h_c'` is finite, hence positive. 

### `maxGauge_pos`

 The gauge `maxGauge` of a term of cell rank `j` is positive: it is the larger of
`termDiscNorm` and `N ^ f` times the norm `minorNorm` of the leading minor (`f` the number of
infinite places), divided by two positive indices. 

 ### The discriminant of `L⁺_γ` 

### `HasLevelLifts`

 The columns of `m` lie in the lattice `L⁺_γ`: they have integral lifts
(`New.Filling.HasIntegralLifts`) whose parts in the isotropic space `A` are divisible by the level
`M`. These are the lifts in `M (Λ ∩ A) ⊕ Λ⁺`, where `Λ` is the lattice of `c` and
`Λ⁺ = Λ ∩ (X₀ ⊕ E z)`, with `X₀ ⊕ E z` the middle space of the frame. 

### `HasLevelLifts.hasIntegralLifts`

 Columns in the lattice `L⁺_γ` (`HasLevelLifts`) have integral lifts. 

### `HasLevelLifts.mul`

 If the columns of `m` lie in the lattice `L⁺_γ` (`HasLevelLifts`), so do those of `m V` for
every integral `V`. 

### `HasLevelLifts.submatrix`

 If the columns of `m` lie in the lattice `L⁺_γ` (`HasLevelLifts`), then so do the columns of
`m.submatrix id e`, the columns of `m` chosen by `e`. 

### `submoduleIndex_ideleM_smul_eq`

 Let `g = S.ideleM` be the level as a unit of the finite adeles `𝔸f E`, and let `L' ≤ L` be
submodules of `n → 𝔸f E` over the ring `Ô E` of integral finite adeles. If `L'` has finite index in
`L` (`submoduleIndex L' L ≠ 0`, an infinite index being `0`), then `[L : g L] = [L' : g L']`. 

### `submoduleIndex_inf`

 The index of `N ⊓ K` in `M` is that of `K` in `M ⊓ N` times that of `N` in `M`. 

### `submoduleIndex_inf_of_le`

 If `M ≤ N`, then `N ⊓ K` and `K` have the same index in `M`. 

### `submoduleIndex_inf_comap`

 If `M ≤ N`, the index in `M` of the elements of `N` that `f` maps into `L` is the index of `L`
in the image `f M`. 

### `submoduleIndex_ideleM_smul_isotropicRows_dvd`

 Let `γ` be a term of cell rank `j` from `c'` to `c`, and put
`k = S.translateByClassReps c c' γ`. Column `a` of `P` holds the products of `e_a` with the frame
`k e₁, …, k e_ϱ, k z`. The lattice `L` spanned by the columns is a copy of `(Λ ∩ A)/(Λ ∩ I)`, for
`Λ` the lattice of `c`, `A` the span of the `e_a` and `I = A ∩ γ A`. The index of `M L` in `L`
divides `M ^ (2 i f)`, where `M = S.M` is the level (`S.ideleM` as a finite idele), `i = min ϱ j`
and `f` is the number of infinite places. 

### `IsOrthogonalLift.eq_mul_of_isotropicRows_mul_eq_zero`

 Let `A` be the span of `e₁, …, e_ϱ` and let `γ` have cell rank `j` (`S.HasCellRank j γ`). Let
`u` be an orthogonal lift of `v`. An adelic vector of `A` is a combination of the rational basis of
`I = A ∩ γ A` formed by the columns of `u.toCols₁` if its products with the rows `isotropicRows` of
`S.frameProducts γ` vanish. The columns of `ω`, in the coordinates of `A`, are such vectors. So `ω`
is `u.toCols₁.toRows₁` times its rows `b ≥ j`. 

### `hasLevelLifts_of_col_mem`

 Let `γ` have cell rank `j`, and let the columns of `t w`, adelic combinations of rational
vectors orthogonal to `A` and `γ A`, be integral in the lattice `Λ` of `c`. Suppose that the part in
`A` of each has the same products with the frame of `γ` as some vector of `M (Λ ∩ A)`. Then their
images in the link lie in `L⁺_γ`, the lattice of the images of vectors of `Λ` orthogonal to `A` and
`γ A` whose part in `A` is divisible by `M` (`HasLevelLifts`): adding vectors of `I = A ∩ γ A` makes
the parts in `A` divisible by `M`. 

### `exists_basis_mulVec_mem_ideleM_smul`

 Let `γ` be a term of cell rank `j` from `c'` to `c`, put `k = S.translateByClassReps c c' γ`,
and let `m` have integral entries. Column `a` of `P` holds the products of `e_a` with the frame
`k e₁, …, k e_ϱ, k z`; let `L` be the lattice spanned by the columns. Then some invertible integral
`B` has `P m x ∈ M L` for each of its columns `x`, and `genIndex (det B)`, the index of its lattice
in the integral vectors, is at most `M ^ (2 i f)`. Here `M = S.M` is the level, `i = min ϱ j` and
`f` is the number of infinite places. 

### `exists_hasLevelLifts_linkDiscSq_le`

 **The lattice of a link.** Let `E` be a CM field with a primitive root of unity of order `5040`,
and let `S : Filling E 𝔰` be data of the filling theorem. Let `γ` be a term from `c'` to `c` of cell
rank `j`, and let the columns of `v` be a basis of its link. For some invertible finite-adelic `e`
the columns of `v e` lie in the lattice `L⁺_γ`, and the torsion index `S.torsionIndex` times the
discriminant of their lattice is at most `M ^ (2 i f) 𝗀♯ / N ^ f`. Here `M = S.M` is the level,
`N = S.N` is minus the norm of the last frame vector, `i = min ϱ j`, `f` is the number of infinite
places and `𝗀♯ = S.minorGauge j c c' γ` is `Nm (S.subframeMinor j γ) / N ^ f` divided by the two
indices `isotropicRowsIndex` at `S.translateByClassReps c c' γ` and at its inverse. 
