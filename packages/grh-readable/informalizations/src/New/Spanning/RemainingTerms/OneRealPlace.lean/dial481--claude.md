---
{
  "module": "src/New/Spanning/RemainingTerms/OneRealPlace.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/RemainingTerms/OneRealPlace.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/RemainingTerms/OneRealPlace.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The weight of Schur's test at one real place

`New.Shape.G₁` is the unitary group of the form `New.Shape.J₁`, which consists of `ϱ` hyperbolic
planes, a positive part `X₀` indexed by `κ` and one negative vector `z`. The frame is
`f = (e₁, …, e_ϱ, z)`, `A` is the span of the `e_a`, and `V₋` is the `-1` eigenspace of `J₁`. The
weight is a power `ν(y) ^ (-(k + i))`, `k = dim X₀`, of the ratio of the volumes of the projections
of the frames `γ f` and `f` to the negative space `y V₋`. Let norm-one pairs occur for `γ` from
level `j` and put `i = min ϱ j`. Then `ν(y)` can be computed modulo `I = A ∩ γ A`, on the subframe
`e₁, …, e_i, z`. It is bounded from below by a multiple of `det (1 + v vᴴ)`, where the columns of
`v` lie in `X₀` and move affinely when `y` is moved by a unipotent element `g` that fixes the frame.
Since `ν` for `γ` at `g y` is `ν` for `g⁻¹ γ` at `y`, the point `y` stays fixed here and `γ` is
replaced by `g⁻¹ γ`.

Notions from other files:
* `New.Shape.frameCols`, `New.Shape.definiteCols`: the matrices with the vectors of the frame,
  respectively the basis of `X₀`, as columns.
* `New.realFrameGram γ`: the matrix of the products of `f` with `γ f`.
* `New.NormOnePairOccursFrom j γ`: at each index from `j` on, the flags of `f` and `γ f` share a
  vector, with leading coefficients `c` and `1` for one fixed `c` of modulus `1`.

## Main definitions and results

* `New.volumeRatio`: the ratio `ν(y)` of the two volumes.
* `New.RealPlace.IsNegativeBasis.volumeRatio_eq`: `ν(y)` in a basis of `y V₋ ∩ I^⊥`.
* `New.RealPlace.IsTriangularBasis.norm_det_mul_le_volumeRatio`: the lower bound for `ν(y)`.
* `New.RealPlace.differenceX₀_eq_add`: the dependence of `v` on the unipotent element.
* `New.RealPlace.exists_majorant_volumeRatio_inv_pow`: an integrable majorant of `ν ^ (-(k + i))`.


### `frameVolume`

 The volume, up to a constant factor, of the projection of the frame to the negative space
`γ V₋`, where `V₋` is the `-1` eigenspace of `J₁`: the modulus of the determinant of the products
of the frame with the basis `γ (1 - J₁) frameCols` of `γ V₋`. 

### `RealPlace.frameX₀Part`

 The coordinates in `X₀` of the vectors of the frame moved by `γ`, as columns. 

### `RealPlace.J₁_mulVec_eq_self`

 A vector `w` whose products with the columns of `(1 - J₁) * frameCols` vanish is fixed by `J₁`:
`J₁ w = w`. 

### `RealPlace.form_frameCols_mulVec`

 The hermitian form `J₁` on the combination `frameCols *ᵥ x` of the frame vectors equals
`-‖x top‖ ^ 2`, where `x top` is the coefficient of `z`. 

### `frameVolume_pos`

 For `γ ∈ G₁`, the volume `frameVolume γ` of the projection of the frame `e₁, …, e_ϱ, z` to the
negative space `γ V₋` is positive. 

### `frameVolume_mul_left`

 The volume does not change when the point `y` is moved by a unipotent element `γ` that fixes
every vector of the frame. 

### `volumeRatio`

 The ratio `ν(y)` of the volumes of the projections of the frame of `γ` and of the standard
frame to the negative space `y V₋`. Vectors shared by the two flags cancel in it
(`New.RealPlace.IsNegativeBasis.volumeRatio_eq`). 

### `volumeRatio_inv`

 `volumeRatio` for `γ⁻¹` at the point `γ⁻¹ * y` is the inverse of `volumeRatio` for `γ` at `y`:
exchanging the two frames inverts the ratio. 

### `volumeRatio_mul_left`

 For a unipotent element `u` that fixes the frame, the ratio for `γ` at the point `u y` is the
ratio for `u⁻¹ γ` at the point `y`. 

### `RealPlace.posSemidef_neg_gram_mul_frameCols`

 For `γ ∈ G₁`, the form `J₁` is negative semidefinite on the span of the frame `γ f`, where
`f = (e₁, …, e_ϱ, z)` is given by the columns of `frameCols`: for any matrix `a` of coefficients,
minus the Gram matrix for `J₁` of the columns of `γ f a` is positive semidefinite. 

### `RealPlace.gram_definiteCols_mul_eq`

 Let `X₀` be the positive definite part of the form `J₁`; its basis vectors are the columns of
`definiteCols`, so `definiteColsᴴ * Y` holds the coordinates in `X₀` of the columns of `Y`. If
these columns are orthogonal for `J₁` to the frame `e₁, …, e_ϱ, z`, their Gram matrix for `J₁` is
the Euclidean Gram matrix of their coordinates in `X₀`. 

### `RealPlace.frameLeftInverse`

 The left inverse of `frameCols` that vanishes on the orthogonal complement of the negative
space `y V₋`. It gives the coordinates of the projection to `y V₋` in the projected frame. 

### `RealPlace.volumeRatio_eq_norm_det`

 The ratio is the modulus of the determinant of the projection of `γ f` to `y V₋`, written in
the basis given by the projection of `f`. 

### `RealPlace.frameCols_J₁_gram`

 The form on the span of the frame is minus the squared modulus of the coefficient of `z`. 

### `RealPlace.conjTranspose_realFrameGram_mulVec`

 If the vector `frameCols x = γ frameCols x'` lies in the span of the frame `f` and in the span
of `γ f`, then its products with the frame `γ f` are `(0, …, 0, -x' top)`. That is,
`(realFrameGram γ)ᴴ x = Pi.single top (-x' top)`. Here `realFrameGram γ` is the matrix of the
products `h(f_j, γ f_l)` of the frame with its translate by `γ`, and `top` is the index of `z`. Also
the coefficients `x top` and `x' top` of `z` have the same modulus. 

### `RealPlace.J₁_mul_coe`

 An element `y` preserves the form `J₁`, so `J₁ y = (y⁻¹)ᴴ J₁`. 

### `RealPlace.J₁_mul_one_sub_J₁_mul`

 The columns of `(1 - J₁) * frameCols` lie in the `-1` eigenspace of `J₁`, that is `J₁ * ((1 -
J₁) * frameCols) = -((1 - J₁) * frameCols)`. 

### `RealPlace.J₁_mul_inv_conjTranspose`

 An element `y` preserves the form `J₁`, so `J₁ (y⁻¹)ᴴ = y J₁`. 

### `RealPlace.J₁_mul_frameLeftInverse_conjTranspose`

 The columns of `J₁ Bᴴ`, `B = frameLeftInverse y`, are combinations of the columns of
`y (1 - J₁) frameCols`, which form a basis of the negative space `y V₋`. 

### `RealPlace.exists_eq_one_sub_J₁_mul`

 The `-1` eigenspace `V₋` of `J₁` is spanned by the columns of `(1 - J₁) * frameCols`: a matrix
`W` with `J₁ * W = -W` equals `(1 - J₁) * frameCols * a` for some matrix `a`. 

### `RealPlace.eq_mul_of_J₁_mul_eq_neg`

 A vector of the negative space `y V₋` is determined by its products for `J₁` with the frame
`f`. Let `B = frameLeftInverse y` be the left inverse of `frameCols` (so `B f = 1`) that vanishes
on the orthogonal complement of `y V₋` for `J₁`. If the columns of `y⁻¹ ω` lie in the `-1`
eigenspace `V₋` of `J₁`, then `ω` is `J₁ Bᴴ` times the matrix `fᴴ J₁ ω` of these products. 

### `RealPlace.norm_det_eq_norm_det_mul_inclMatrix`

 Let the columns of `inclMatrix ℂ e` be the basis vectors at the indices `e l`, and let `pᴴ`
be a left inverse of this matrix. Suppose that for each other index `b` the matrix `N` maps a
vector `x'` to a vector `x` in the kernel of `pᴴ`, both with last nonzero coefficient at `b`,
that of `x'` equal to `1` and that of `x` of modulus `1`. Then `|det N|` is the modulus of the
determinant of the product of `pᴴ`, `N` and `inclMatrix ℂ e`. 

### `RealPlace.subframeIndex`

 The indices of the subframe `e₁, …, e_i, z` among those of the frame. 

### `RealPlace.subframeIndex_self`

 For `i = ϱ` the subframe is the whole frame, with the same indices. 

### `RealPlace.le_and_ne_top_of_notMem_range`

 An index of the frame outside the subframe `e₁, …, e_i, z` is that of a vector `e_{b+1}` with
`i ≤ b < ϱ`. 

### `RealPlace.subframeCols`

 The vectors `e₁, …, e_i, z` of the subframe, as columns. 

### `RealPlace.subframeBlock`

 The matrix of the products of the subframe `e₁, …, e_i, z` with its image, cut out of the
matrix `Z` of the products of the frames. 

### `RealPlace.IsNegativeBasis`

 The columns of `ω` lie in the negative space at `y`, are orthogonal to `I = A ∩ γ A`, where `A`
is the isotropic space, and pair perfectly with the subframe. For `γ` with norm-one pairs occurring
from level `j` with `i = min ϱ j` they are a basis of `y V₋ ∩ I^⊥`. 

### `RealPlace.IsNegativeBasis.J₁_mul`

 The columns of `y⁻¹ ω` lie in `V₋`. 

### `RealPlace.IsNegativeBasis.orthogonal`

 The columns of `ω` are orthogonal to every vector `f x = γ f x'` that lies in `A`. 

### `RealPlace.IsNegativeBasis.det_ne_zero`

 The products of the subframe with the columns of `ω` form an invertible matrix. 

### `RealPlace.IsNegativeBasis.volumeRatio_eq`

 **The weight modulo `I`.** Let `γ, y ∈ G₁`, let `f = (e₁, …, e_ϱ, z)` be the frame, `A` the span
of the `e_a`, `I = A ∩ γ A` and `V₋` the `-1` eigenspace of `J₁`. Let `NormOnePairOccursFrom j γ`
hold, with `i = min ϱ j`; `subframeCols` has the vectors `e₁, …, e_i, z` of the subframe as columns.
Let `ω` be a negative basis (`IsNegativeBasis`): its `i + 1` columns lie in `y V₋`, are orthogonal
to `I` for `J₁`, and their `J₁`-products with the subframe form an invertible matrix. Then
`volumeRatio γ y`, the ratio `ν(y)` of the volumes of the projections of `γ f` and `f` to `y V₋`, is
the modulus of the determinant of the products of `ω` with `γ e₁, …, γ e_i, γ z`, divided by that of
the products of `ω` with `e₁, …, e_i, z`. 

### `RealPlace.dualProducts`

 The products of the frame with the basis of the span of `γ e₁, …, γ e_i, γ z` that is dual to
the subframe `e₁, …, e_i, z`, in terms of the matrix `Z` of the products of the two frames. 

### `RealPlace.inclMatrix_mul_dualProducts`

 If the subframe `e₁, …, e_i, z` and its image have products of nonzero determinant, the rows of
`dualProducts` that belong to the subframe form the identity matrix. 

### `RealPlace.frameCols_mul_mul_subframeCols`

 If `Z` is the matrix of the products of the two frames, the products of the frame with the
image under `γ` of the subframe `e₁, …, e_i, z` are the columns of `Z` at its indices. 

### `RealPlace.IsTriangularBasis`

 The columns of `ω` are a basis with Gram matrix `-1` of a subspace of the negative space at `y`.
Their products with the subframe `e₁, …, e_i, z` form the lower triangular matrix `L`, and those
with the whole frame are the ones that orthogonality to `I = A ∩ γ A` dictates when the frames `f`
and `γ f` have the products `Z`. 

### `RealPlace.IsTriangularBasis.J₁_mul`

 The columns of `y⁻¹ ω` lie in `V₋`. 

### `RealPlace.IsTriangularBasis.gram_eq_neg_one`

 The Gram matrix of `ω` is `-1`. 

### `RealPlace.IsTriangularBasis.products_eq`

 The products of the frame with `ω` are those with the basis of the span of the image of the
  subframe whose products with the subframe form `L`. 

### `RealPlace.IsTriangularBasis.triangular`

 `L` is lower triangular. 

### `RealPlace.IsTriangularBasis.det_ne_zero`

 `L` is invertible. 

### `RealPlace.exists_isTriangularBasis`

 Let `i ≤ ϱ` and let `Z` be a square matrix indexed by the frame whose block
`B = subframeBlock hi_le Z` at the indices of the subframe `e₁, …, e_i, z` has nonzero determinant.
The matrix `dualProducts hi_le Z` consists of the columns of `Z` at these indices, times `B⁻¹`. Then
at every point `y ∈ G₁` there is a triangular basis: vectors `ω` in `y V₋` with `J₁`-Gram matrix
`-1` whose products with the frame are `dualProducts hi_le Z * L`, with `L` lower triangular and
invertible. It comes from the Gram–Schmidt process applied to the vectors of `y V₋` with products
`dualProducts hi_le Z`. 

### `conjTranspose_subframeCols_mul_J₁_mul_eq`

 If the block of `Z` at the subframe `e₁, …, e_i, z` is invertible and `(ω, L)` is a triangular
basis at `y ∈ G₁`, the products of the subframe with `ω` form the matrix `L`. 

### `isNegativeBasis`

 Let `γ, y ∈ G₁`, let `Z` be the matrix of products of the frames `f` and `γ f` and let its block
at the subframe `e₁, …, e_i, z` be invertible. Then a triangular basis `ω` is a negative basis: its
columns lie in `y V₋`, pair perfectly with the subframe and are orthogonal to `A ∩ γ A`. 

### `norm_dotProduct_J₁_mul_col_le_norm`

 The vectors `y⁻¹ ω_l` of a triangular basis are orthonormal in the `-1` eigenspace `V₋` of
`J₁`, so the product for the form `J₁` of a vector `x` with `y⁻¹ ω_l` is at most the length of
`x`. 

### `apply_eq_frameVector_dotProduct`

 If the block of `Z` at the subframe `e₁, …, e_i, z` is invertible, the entry `L a l` of a
triangular basis is the product for the form `J₁` of the `a`-th vector of the subframe with `ω_l`,
both moved by `y⁻¹`. 

### `norm_det_le`

 If the frame vectors `y⁻¹ f_a` have length at most `ρ` and the block of `Z` at the subframe
`e₁, …, e_i, z` is invertible, then `|det L| ≤ ρ ^ (i + 1)` for every triangular basis `(ω, L)`
at `y`. 

### `norm_det_eq_mul_norm_last`

 As `L` is triangular, its determinant has the modulus of that of its leading block of order
`i` times that of its last diagonal entry. 

### `RealPlace.imageBasis`

 If `Z` is the matrix of products of the frames `f` and `γ f`, with invertible block at the
subframe `e₁, …, e_i, z`, and `L` is invertible: the basis of the span of `γ e₁, …, γ e_i, γ z`
whose products with the subframe form `L`. 

### `RealPlace.differenceX₀`

 The classes `v_l` in `X₀`, that is the coordinates in `X₀`, of the differences between
`imageBasis` and `ω`. 

### `conjTranspose_frameCols_mul_J₁_mul_sub_eq_zero`

 Let `γ, y ∈ G₁`, let `Z` be the matrix of products of the frames `f` and `γ f` and let `(ω, L)`
be a triangular basis at `y`. Then the differences `imageBasis - ω` are orthogonal to the frame. 

### `gram_differenceX₀`

 Let `γ, y ∈ G₁`, let `Z` be the matrix of products of the frames `f` and `γ f` and let `(ω, L)`
be a triangular basis at `y`. Then the differences `imageBasis - ω` have the same Gram matrix as
their classes `differenceX₀` in `X₀`. 

### `norm_det_mul_le_volumeRatio`

 **A lower bound for the ratio.** Let norm-one pairs occur for `γ ∈ G₁` from level `j`, with
`i = min ϱ j` and `Z` the products of the two frames. Let the determinant `δ` of the block of the
subframe in `Z` be nonzero, let `(ω, L)` be a triangular basis at `y`, and let the columns of
`v = differenceX₀ hi γ Z ω L` be the parts in `X₀` of `ω'_l - ω_l`, for the basis `ω'` of the span
of `γ e₁, …, γ e_i, γ z` with products `L` with the subframe. Then the ratio `ν(y)` of the volumes
of the projections of `γ f` and `f` to `y V₋` satisfies
`ν(y) ≥ 2 ^ (-i - 1) |δ| det (1 + v vᴴ) / |det L|²`. 

### `RealPlace.differenceX₀_eq_add`

 **The translates.** Let `γ, γ₀ ∈ G₁` and let the block `B` of `Z` at the indices of the subframe
`e₁, …, e_i, z` be invertible. The matrix `differenceX₀ hi γ Z ω L` holds the coordinates in `X₀` of
the columns of `γ (e₁, …, e_i, z) B⁻¹ L - ω`. If the part in `X₀` of the image of the subframe under
`γ` is that under `γ₀` plus `Aᴴ` times the first `i` rows of `B`, then this matrix for `γ` is the
one for `γ₀` plus `Aᴴ` times the first `i` rows of `L`. 

### `RealPlace.exists_common_vector_of_normOnePairOccursFrom`

 Let norm-one pairs occur for `γ ∈ G₁` from level `i ≤ ϱ`, with matrix `Z` of products of the two
frames. The spans of the two frames share a vector `f x` that is a combination `c` of the image of
the subframe, with coefficient `1` at `γ z`. The coefficient `x z` of `z` has modulus `1`, and the
products of the subframe with `f x` are `(0, …, 0, -x z)`. 

### `RealPlace.norm_det_subframeBlock`

 Let norm-one pairs occur for `γ ∈ G₁` from level `j ≤ n = ϱ + 1`, let `Z` be the matrix of
products of the two frames and let `i = min ϱ j`. Then the determinant of the block
`subframeBlock hi_le Z` of `Z` at the indices of the subframe `e₁, …, e_i, z` has the modulus of the
leading principal minor of order `j` of `Z`. 

### `norm_last_le`

 **The last column, top level.** Let `i = ϱ`, so that the subframe `e₁, …, e_i, z` is the whole
frame, and let `Z` be any square matrix indexed by the frame whose block of the subframe (here all
of `Z`) is invertible. If `y ∈ G₁` has length at most `θ` (`besselLength`, the infimum of
`‖s y‖ + 1` over the Bessel subgroup), then `|L (last i) (last i)| ≤ θ` for every triangular basis
`(ω, L)` at `y` for `Z`. 

### `norm_last_sq_eq_one_add_dotProduct_differenceX₀`

 **The last column, lower levels.** Let norm-one pairs occur for `γ ∈ G₁` from level `i ≤ ϱ`, so
that the flags of `f` and `γ f` share a vector at `z`, and let `Z` be the products of the two
frames, with invertible block of the subframe `e₁, …, e_i, z`. Let `(ω, L)` be a triangular basis at
`y`: the vectors `ω` lie in `y V₋`, have Gram matrix `-1` and lower triangular products `L` with the
subframe. Let `ω'` be the basis of the span of `γ e₁, …, γ e_i, γ z` with the same products `L`, and
let `v_z`, the last column of `differenceX₀`, be the part in `X₀` of `ω'_z - ω_z`. Then
`|L_zz|² = 1 + |v_z|²`. 

### `norm_last_sq_le`

 **The last column.** Let norm-one pairs occur for `γ ∈ G₁` from level `j ≤ n = ϱ + 1`, let
`i = min ϱ j` and let `Z` be the products of the frames `f` and `γ f`, with invertible block of the
subframe `e₁, …, e_i, z`. Let `y` have length (`besselLength`) at most `θ`, let `(ω, L)` be a
triangular basis at `y`, and let `v_z`, the last column of `differenceX₀`, be the part in `X₀` of
`ω'_z - ω_z` for the basis `ω'` of the span of `γ e₁, …, γ e_i, γ z` with products `L` with the
subframe. Then `|L_zz|² ≤ θ ^ (2 (j - i)) (1 + |v_z|²)`. 

### `RealPlace.exists_majorant_volumeRatio_inv_pow`

 **One real place.** Let `y ∈ G₁`, let the vectors `y⁻¹ f_a` have length at most `ρ`, let `y`
have length (`besselLength`) at most `θ`, and let `k = dim X₀ ≥ 7`. Let norm-one pairs occur for
`γ₀ ∈ G₁` from level `j ≤ ϱ + 1`, with `i = min ϱ j`. Let `Z` be the matrix of products of the
frames `f` and `γ₀ f`, and let the determinant `δ` of its block of the subframe `e₁, …, e_i, z` be
nonzero. There is a measurable `φ` on `X₀ ^ i` with integral at most `(2 ρ²) ^ ((i + 1) i) (2 ^
(i + 1) θ ^ (2 (j - i))) ^ k / |δ| ^ (k + i)` such that `ν ^ (-(k + i)) ≤ φ A` whenever norm-one
pairs occur for `γ` from level `j` with the same products `Z` and the parts in `X₀` of the images of
the subframe under `γ` and `γ₀` differ by `Aᴴ` times the first `i` rows of the block. 

### `RealPlace.frameX₀Part_unipotentOf_inv_mul`

 For `γ ∈ G₁`, left multiplication by the inverse of the unipotent element `unipotentOf q` with
parameters `q = (a, b)` adds `aᴴ` times the rows of the isotropic vectors in the matrix of products
to the part in `X₀` of the frame `γ f`. 
