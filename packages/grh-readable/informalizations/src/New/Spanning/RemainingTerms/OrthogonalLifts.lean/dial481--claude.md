---
{
  "module": "src/New/Spanning/RemainingTerms/OrthogonalLifts.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/RemainingTerms/OrthogonalLifts.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/RemainingTerms/OrthogonalLifts.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Orthogonal lifts and the two isotropic lists of a link

Let `γ` have cell rank `j`, let `Λ` be the lattice of a class, `A` the span of `e₁, …, e_ϱ`,
`I = A ∩ γ A`, and let `z` be the last vector of the frame, of norm `-N`. This file defines
orthogonal lifts of a basis `v` of the link of `γ`. These are vectors orthogonal to `A` and `γ A`
over the columns of `(0 | v)`, whose first columns form a basis of `I`. It proves that such lifts
exist and that they are isometric to `v` for `S.linkMetric` after a correction by their products
with `z` and `γ z`. It then adjoins two vectors `z'`, `z''` of norm `N` and computes the
discriminant of the isotropic lists `(e_a, z + z')` and `(γ e_a, γ z + z'')`, `a < j`. It also
shows that `torsionIndex k` divides the index of the classes of the `e_a` and `k e_a` in the
integral vectors of their span, for finite-adelic `k`.

Notions from other files:
* `framePair γ` has the columns `e₁, …, e_ϱ, z` and their images under `γ`;
  `isotropicFramePair γ` leaves out `z` and `γ z`.
* `linkMatrix γ` sends `t` to the middle coordinates of `t` and `γ⁻¹ t`; `link γ` is its image of
  the orthogonal complement of `A + γ A`.
* `HasCellRank j γ` says that `γ` has cell rank `j`: `NormOnePairOccursFrom j γ`, the leading
  `j`-minor of the products of the two frames is nonzero, and `S.termDisc γ ≠ 0` exactly when
  `j = ϱ + 1`.
* `isotropicRowsIndex j k` is the index, among the products of `Λ ∩ A` with the frame of `k`, of
  those from the `e_a`, `a < j`; `torsionIndex k` is the index of the lattice spanned by the
  `e_a` and `k e_a` in the integral vectors of their span.

## Main definitions and results

* `New.Filling.IsOrthogonalLift`, `New.Filling.exists_orthogonal_lift`: orthogonal lifts of a basis
  of the link, and their existence for `γ` of cell rank `j`.
* `New.Filling.abs_norm_det_gram_eq_abs_norm_subframeMinor_sq`,
  `New.Filling.isotropicRowsIndex_mul_dvd_submoduleIndex`: the discriminant of the two lists, and
  a divisor of the index attached to the classes of the `e_a` and `k e_a`, `a < j`.


 ### A basis of `I` and lifts of a basis of the link 

### `IndexNotBelow`

 The indices `b ≥ j` of the basis vectors `e_b` of `A`. 

### `lastPair`

 The vectors `z` and `k z`, as columns. 

### `eStarCols`

 The matrix whose columns are the basis vectors `e*_b` with `b ≥ j`. 

### `IsOrthogonalLift`

 An orthogonal lift of `v` at cell rank `j`. The columns of `u` are orthogonal to the isotropic
space `A = ⟨e₁, …, e_ϱ⟩` and to `γ A`. The first ones, one for each index `b ≥ j`, are dual to the
vectors `e*_b` and are sent to zero by `linkMatrix γ` (the map to the middle coordinates of `t` and
`γ⁻¹ t`). The others are orthogonal to the `e*_b` and are sent to the columns of `v`. 

### `IsOrthogonalLift.orthogonal`

 The columns of `u` are orthogonal to `A` and `γ A`. 

### `IsOrthogonalLift.linkMatrix_mul`

 The map `linkMatrix γ` kills the first columns of `u` and sends the others to those of `v`. 

### `IsOrthogonalLift.dual`

 The first columns of `u` are dual to the `e*_b` with `b ≥ j`, the others are orthogonal to
  them. 

### `HasCellRank.exists_isotropic_inter_vector`

 Let `γ` have cell rank `j`. For any `d`, some vector of `A ∩ γ A`, where `A` is the span of the
isotropic `e_a`, has the coordinates `d a` at the indices `a ≥ j`. It is given by its coefficients
`x` in the frame `e₁, …, e_ϱ, z` (the columns of `frameImage 1`, `z` at the index `𝔰.top`), those of
its image under `γ⁻¹` being `y`. 

### `exists_orthogonal_lift`

 Let `A` be the span of the isotropic basis vectors `e₁, …, e_ϱ`, and let `e*_b` be the isotropic
basis vector dual to `e_b`. If `γ` has cell rank `j` and the columns of `v` span its link, then `v`
has an orthogonal lift `u`: its columns are orthogonal to `A` and `γ A`, their images in the link
are the columns of `(0 | v)`, and their products with the `e*_b`, `b ≥ j`, form the matrix
`(1 | 0)`. 

### `IsOrthogonalLift.apply_inl`

 Let `u` be an orthogonal lift. In its row of the isotropic basis vector `e_i`, `i ≥ j`, it has
the identity in its first block of columns and zero in the second. 

### `IsOrthogonalLift.orthogonal_toCols₁`

 If `u` is an orthogonal lift (`IsOrthogonalLift j γ v u`), its first columns `u.toCols₁` are
orthogonal, for the form `S.ratGram`, to the columns of `isotropicFramePair γ`, which span `A` and
`γ A`. 

### `IsOrthogonalLift.linkMatrix_mul_toCols₁`

 The map `linkMatrix γ` kills the first columns of an orthogonal lift. 

### `IsOrthogonalLift.toCols₁_eq_fromRows`

 The first columns of an orthogonal lift lie in `A`. 

### `IsOrthogonalLift.conjTranspose_isotropicRows_mul_eq_zero`

 The first columns of an orthogonal lift are orthogonal to the frame `γ e_a`, `γ z`. This is
stated for their coordinates in `A` and the products of the `e_a` with that frame. 

### `IsOrthogonalLift.toCols₁_mul_framePair`

 The first columns of an orthogonal lift are orthogonal to both frames `e_a`, `z` and `γ e_a`,
`γ z`. 

### `IsOrthogonalLift.toCols₁_mul_self`

 The first columns of an orthogonal lift are orthogonal to all its columns. 

### `IsOrthogonalLift.gram_add_border`

 The isometry: the Gram matrix of the lifts of `v`, corrected by `N⁻¹` times their products with
`z` and `γ z`, is the Gram matrix of `v` for the positive form `S.linkMetric` on pairs of middle
coordinates. 

 ### The two lists and their index 

### `listPair`

 The vectors `e_a` and `k e_a` with `a < j`, as columns. 

### `abs_norm_det_gram_eq_abs_norm_subframeMinor_sq`

 Take the Gram matrix of the vectors `e_a`, `γ e_a` (`a < j`), `z`, `γ z`, and add `N` to the
diagonal entries of `z` and `γ z`. The norm to `ℚ` of its determinant has the absolute value
`(Nm δ_*)²`, where `δ_* = S.subframeMinor j γ` is the determinant of the products of the subframe
`(e_a, z)`, `a < j`, with its image under `γ`. 

### `submoduleIndex_colLattice_dvd_preimageLattice`

 Let `M` and `P` be matrices over the finite adeles `𝔸f E`, and call a vector integral if its
entries lie in the ring `Ô E` of integral finite adeles. Suppose that the columns of `P` lie in the
`𝔸f E`-span of those of `M`. Then the index of the `Ô E`-span `colLattice M` of the columns of `M`
in the integral vectors of the span of `P` divides the index of the integral vectors in the module
`preimageLattice M` of the `y` with `M y` integral. 

### `toRows₂_gram_framePair_isotropicFramePair`

 Let `k` be finite-adelic, acting on the standard lattice with Gram matrix
`latticeMiddle.splitGram`. The products of the vectors `k e₁, …, k e_ϱ, k z` with the `e_a` form the
conjugate transpose of the rows `isotropicRows` of the `e_a` in the matrix `frameGram k` of frame
products, and those with the `k e_a` vanish. 

### `toRows₁_gram_framePair_isotropicFramePair`

 Let `k` be finite-adelic. The products of the vectors `e₁, …, e_ϱ, z` with the `e_a` vanish,
and those with the `k e_a` form the conjugate transpose of the rows `isotropicRows` of the `e_a` in
the matrix of frame products of `k⁻¹`. 

### `torsionIndex_dvd_submoduleIndex`

 Let `(ι, B, q)` be a basis of `(Λ ∩ I^⊥)/(Λ ∩ I)`, with `B` indexed by `μ`. Suppose `Λ ∩ I` lies
in the lattice of the columns `e_a`, `k e_a` of `isotropicFramePair k` and is orthogonal to them.
Then the torsion index `S.torsionIndex k` divides the index of the classes `q e_a`, `q k e_a` in
the integral vectors of their span. Here `Λ` is the standard lattice of integral vectors, `I` is the
span of the columns of `ι`, and the vectors `k e_a` are assumed integral. 

### `isotropicRowsIndex_mul_dvd_submoduleIndex`

 Let `k` be a finite-adelic element such that the frame `e₁, …, e_ϱ, z` and its image under `k`
(`framePair k`) are integral. Let `Λ` be the standard lattice of integral vectors and `I` the span
of the columns of `ι`. Let these columns be a basis of `Λ ∩ I`, orthogonal to the frame and its
image under `k` and in the lattice of the `e_a` and `k e_a`, and let `q` give the classes in
`(Λ ∩ I^⊥)/(Λ ∩ I)`. Suppose that the classes of the `e_a` and `k e_a` with `a < j` span those of
all `e_a` and `k e_a`. Consider the module `preimageLattice` of the coefficient vectors `y` for
which the combination `(q * listPair j k) y` of the classes with `a < j` is integral. Then the index
of the integral coefficient vectors in it (`0` if infinite) is a multiple of the product of
`S.isotropicRowsIndex j k`, `S.isotropicRowsIndex j k⁻¹` and the torsion index
`S.torsionIndex k`. 
