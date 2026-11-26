---
{
  "module": "src/New/Spanning/RemainingTerms/LinkVectors.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/RemainingTerms/LinkVectors.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/RemainingTerms/LinkVectors.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The vectors `z⁺` and `Υ_γ⁻¹ z⁺`

Let `γ` be an element of the unitary group, with the link isometry `Υ_γ` of the positive space
`X₀ ⊥ E z⁺`. Let `z` be the last vector of the frame and let `A` be spanned by the others. The
vectors of the lattice `Λ` of a class `c` that are orthogonal to `A` and `γ A` have as their image a
lattice `L¹` in `X₀ ⊥ E z⁺`. It contains the lattice `L⁺_γ` of the vectors whose part in `A` is
divisible by the level `M = S.M`, so what lies in the dual of `L¹` lies in the dual of `L⁺_γ`.

* `New.Filling.linkVectors_mulVec_perpToPositive_mem`: if `γ` is a term over `(c, s, c')`, the
  products of `z⁺` and `Υ_γ⁻¹ z⁺` with `L¹` are integral.
* `New.Filling.linkVectors_mulVec_eq_zero_iff`: the orthogonal complement of the two vectors is
  `X₀^γ = X₀ ∩ Υ_γ⁻¹ X₀`.
* `New.Filling.exists_lift_mem_linkedX₀_iff_exists_orthogonal`: the vectors of `L⁺_γ ∩ X₀^γ`.
* `New.Filling.HasCellRank.exists_linkIsometry_symm_eq_smul`,
  `New.Filling.linearIndependent_linkVectors_and_prod_norm_det`: the two vectors are proportional if
  `γ` has a cell rank and the discriminant `𝗀` of the two frames is zero; if `𝗀` is not zero, they
  are independent, and their Gram determinant is computed
  (`New.Filling.linearIndependent_linkVectors`, `New.Filling.prod_norm_det_gram_linkVectors`).
* `New.Filling.linkVectorPairs`: the negatives of the two vectors, as pairs in the graph of `Υ_γ`;
  there they represent the products with `z` and `γ z`
  (`New.Filling.linkVectorPairs_mul_linkMetric_mul`).

Notions from other files:
* `S.G E`: the unitary group of the form `S.ratGram` on the space with the basis `e₁, …, e_ϱ`, a
  basis of `X₀`, `z`, `e*₁, …, e*_ϱ`; the frame is `(e₁, …, e_ϱ, z)`.
* `S.positiveGram`: the Gram matrix of `X₀ ⊥ E z⁺`, where `z⁺` has the norm `N = S.N`.
* `linkIsometry γ`: the isometry `Υ_γ` of `X₀ ⊥ E z⁺`.
* `S.HasCellRank j γ`: the term `γ` has the cell rank `j`, the order of a distinguished leading
  minor of the products of the frame with its image under `γ`.
* `perpToPositive γ`: the map from `isotropicPerp γ = (A + γ A)^⊥` to `X₀ ⊥ E z⁺`.


### `linkVectors`

 The two vectors `z⁺` and `Υ_γ⁻¹ z⁺` of the positive space `X₀ ⊥ E z⁺`, as columns. Here
`Υ_γ = linkIsometry γ` is the link isometry of `γ`, and `inr ()` is the index of `z⁺`. 

### `lastFramePair`

 The two vectors `k z` and `z`, as columns, where `k` is in the unitary group of the form with
the middle block `T`, and `z` is the last vector of the frame `(e₁, …, e_ϱ, z)`. 

### `linkVectors_mulVec`

 The products of a vector `a` of `X₀ ⊥ E z⁺` with `z⁺` and `Υ_γ⁻¹ z⁺` are `N` times the
`z⁺`-coordinates of `a` and of `Υ_γ a`, where `Υ_γ` is the link isometry of `γ`. 

### `linkVectors_mulVec_eq_zero_iff`

 The vectors `a` orthogonal, for `S.positiveGram`, to `z⁺` and `Υ_γ⁻¹ z⁺` in `X₀ ⊥ E z⁺` are
exactly the image under `inclPositive E 𝔰` of `X₀^γ = X₀ ∩ Υ_γ⁻¹ X₀` (`linkedX₀ γ`). 

### `frameImage_conjTranspose_mulVec_eq_zero_iff`

 A vector `y` is orthogonal to the frame `(γ e₁, …, γ e_ϱ, γ z)` if and only if the coordinates
of `γ⁻¹ y` at the dual basis vectors `e*_a` and at `z` vanish. 

### `linkIsometry_perpToPositive_apply`

 Let `A` be spanned by the vectors of the frame other than the last one, `z`. For `y` in
`isotropicPerp γ`, so orthogonal to `A` and `γ A`, let `v = perpToPositive γ y` be its image in
`X₀ ⊥ E z⁺`. Then the `z⁺`-coordinate (index `inr ()`) of `Υ_γ v = linkIsometry γ v` is the
`z`-coordinate of `y`. 

### `linkVectors_mulVec_perpToPositive`

 Let `A` be spanned by the vectors of the frame other than the last one, `z`. For `y` orthogonal
to `A` and `γ A`, with the image `v` in `X₀ ⊥ E z⁺`, the products of `v` with `z⁺` and `Υ_γ⁻¹ z⁺`
are minus those of `y` with `γ z` and `z`. 

### `isIntMatrix_lastFramePair_mul`

 If `k` lies in the stabilizer of the standard lattice, the linear forms given by the products
with `k z` and `z`, in the lattice basis (where the middle block of the Gram matrix is
`S.latticeMiddle`), have coefficients in the integral finite adeles. 

### `linkVectors_mulVec_perpToPositive_mem`

 Let `γ` be a term over `(c, s, c')`: in the coordinates of the classes `c` and `c'` it
stabilizes the standard lattice and has the reduction `s`. Let `Λ` be the lattice of the class `c`,
and let `A` be spanned by the vectors of the frame other than the last one. The vectors `z⁺` and
`Υ_γ⁻¹ z⁺` have integral products with the image in `X₀ ⊥ E z⁺` of every vector `y` of `Λ` that is
orthogonal to `A` and `γ A`. 

### `elim_mem_preimageLattice_classCoord_iff`

 Let `Λ` be the lattice of the class `c`. For `a` in the span of `e₁, …, e_ϱ` and `v` in
`X₀`, the vector `a + v` lies in `Λ` if and only if `a` has integral coordinates and `v` lies in
`Λ ∩ X₀`. 

### `exists_lift_mem_linkedX₀_iff_exists_orthogonal`

 Let `Λ` be the lattice of the class `c`, let `A` be spanned by the vectors of the frame other
than the last one, and let `L⁺_γ` be the image in `X₀ ⊥ E z⁺` of the vectors of `Λ` that are
orthogonal to `A` and `γ A` and whose part in `A` is divisible by the level `M = S.M`. A vector `v`
of `X₀` lies in `L⁺_γ` and in `X₀^γ = X₀ ∩ Υ_γ⁻¹ X₀` (`linkedX₀ γ`) if and only if it lies in `Λ`
and some vector of `v + M (Λ ∩ A)` is orthogonal to the image of the frame under `γ`. 

### `HasCellRank.exists_linkIsometry_symm_eq_smul`

 Let `γ` have a cell rank `j` (`HasCellRank`): it is in the normal form
`NormOnePairOccursFrom j γ`, the leading minor of order `j` of the products of the frame with its
image under `γ` is not zero, and `j` is the top index `ϱ + 1` exactly if the discriminant
`𝗀 = S.termDisc γ` of these two frames is not zero. If `𝗀 = 0`, then `Υ_γ⁻¹ z⁺` is a multiple of
`z⁺`. 

### `HasCellRank.termDisc_eq_mul_linkIsometry_symm`

 Let `γ` have the cell rank `j`: it is in the normal form `NormOnePairOccursFrom j γ`, the
leading minor `δ_j` of order `j` of the products of the frame with its image under `γ` is not zero,
and `j` is the top index exactly if the discriminant `𝗀` of these two frames is not zero. Then
`𝗀 = |δ_j|² (1 - |u|²)`, where `u` is the `z⁺`-coordinate of `Υ_γ⁻¹ z⁺`, `Υ_γ` is the link
isometry of `γ`, and `|x|²` means `x x̄`. 

### `gram_linkVectors`

 The Gram matrix of `z⁺` and `Υ_γ⁻¹ z⁺` for the form `S.positiveGram` of the positive space
`X₀ ⊥ E z⁺`. Both diagonal entries are `N = S.N`, the norm of `z⁺`. The entries off the diagonal are
`N u` (row 1, column 2) and `N ū` (row 2, column 1), where `u` is the `z⁺`-coordinate of
`Υ_γ⁻¹ z⁺`. 

### `HasCellRank.det_gram_linkVectors_mul`

 If `γ` has the cell rank `j` (`HasCellRank`), the Gram determinant of `z⁺` and `Υ_γ⁻¹ z⁺`,
times `|δ_j|²`, is `N² 𝗀`. Here `𝗀` is the discriminant of the frame and its image under `γ`, and
`δ_j` is the leading minor of order `j` of their products, which is not zero. 

### `HasCellRank.norm_det_gram_linkVectors`

 Let `γ` have the cell rank `j` (`HasCellRank`), so that the leading minor `δ_j` of order `j` of
the products of the frame with its image under `γ` is not zero, and let `𝗀` be the discriminant of
these two frames. At each infinite place `v` the Gram determinant of `z⁺` and `Υ_γ⁻¹ z⁺` has the
modulus `N² |𝗀|_v / |δ_j|_v²`. Here `|x|_v` is the modulus `‖Φ v x‖` under the complex embedding
chosen at `v`. 

### `linearIndependent_linkVectors`

 If the discriminant `𝗀 = S.termDisc γ` of the frame and its image under `γ` is not zero, then
`z⁺` and `Υ_γ⁻¹ z⁺`, the columns of `linkVectors γ` (with `Υ_γ = linkIsometry γ`), are linearly
independent. 

### `prod_norm_det_gram_linkVectors`

 If the discriminant `𝗀` of the frame and its image under `γ` is not zero, then the product over
the `f` infinite places `v` of the modulus of the Gram determinant of `z⁺` and `Υ_γ⁻¹ z⁺` under the
embedding `Φ v` is `N ^ f Nm 𝗀 / 𝗀♯`. Here `Υ_γ` is the link isometry of `γ`, the prime `N = S.N`
is the norm of `z⁺`, and `Nm 𝗀 = S.termDiscNorm γ` is the same product for `𝗀`. The gauge
`𝗀♯ = S.minorGauge ⊤ c c' γ` at the top cell rank is the absolute norm of the determinant of the
products of the two frames, divided by `N ^ f`: the two indices through which the gauge depends on
the classes `c` and `c'` are `1` at this rank. 

### `linearIndependent_linkVectors_and_prod_norm_det`

 Let `E` contain a primitive 5040th root of unity. If the discriminant `𝗀` of the frame and its
image under `γ` is not zero, then `z⁺` and `Υ_γ⁻¹ z⁺` are linearly independent, and the lattice that
they span has the discriminant `N ^ f Nm 𝗀 / 𝗀♯`. The discriminant is the product over the `f`
infinite places `v` of the modulus of the Gram determinant under the embedding `Φ v`,
`Nm 𝗀 = S.termDiscNorm γ` is the same product for `𝗀`, and `𝗀♯` is the gauge `minorGauge` at the top
cell rank, for any classes `c` and `c'`. 

 ### The two vectors as pairs in the link 

### `zFormIndex`

 The index in `linkVectors γ = (z⁺, Υ_γ⁻¹ z⁺)` of the vector that represents the product with
`z` on each half of a pair: `Υ_γ⁻¹ z⁺` for the first half and `z⁺` for the second half, on which
this is the product with `γ z` before the pair is formed. 

### `linkVectorPairs`

 The two pairs in the link of `γ` (the graph of `Υ_γ`) with the sources `-Υ_γ⁻¹ z⁺` (column
`inl ()`) and `-z⁺` (column `inr ()`). 

### `conjTranspose_linkVectorPairs_mul_mulVec_apply`

 The link of `γ` (`link γ`) consists of the pairs of the classes of `t` and `γ⁻¹ t` modulo `A`,
for `t` orthogonal to `A` and `γ A`. Write such a pair as `p = (y₀ + λ' z, y₀' + λ z)`, so that `λ'`
is the `z`-coordinate of the first class and `λ` that of the second; its source `linkSource E 𝔰 p`
is `y₀ + λ z⁺`. The two columns of `linkVectorPairs γ` are the pairs with the sources `-Υ_γ⁻¹ z⁺`
(column `inl ()`) and `-z⁺` (column `inr ()`). The product of column `a` with `p`, for the form
`S.linkMetric` on pairs, is minus the product of column `zFormIndex a` of `linkVectors γ` with
`y₀ + λ z⁺`, for the form `S.positiveGram` of `X₀ ⊥ E z⁺`. 

### `linkVectorPairs_mul_linkMetric_mul`

 Let the columns of `w` lie in the link of `γ`. Their products with the columns of
`linkVectorPairs γ` for `S.linkMetric` are the two rows `zRowBlockDiagonal (S.ratMiddle E)` applied
to them: the products with `z` on each half of a pair. 

### `gram_linkVectorPairs`

 The Gram matrix of the two columns of `linkVectorPairs γ` for `S.linkMetric` equals the Gram
matrix of `Υ_γ⁻¹ z⁺` and `z⁺` for `S.positiveGram`: that is, the Gram matrix of the columns of
`linkVectors γ`, reindexed by `zFormIndex`. 
