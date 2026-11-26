---
{
  "module": "src/New/Spanning/RemainingTerms/FrameCount.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/RemainingTerms/FrameCount.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/RemainingTerms/FrameCount.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Frames of near terms: short shared vectors and moves between frames

This file proves lemmas for counting the frames `γ f` of the remaining terms `p = (c', γ)` modulo
moves. Here `f = (e₁, …, e_ϱ, z)` is the standard frame, `New.frameImage γ` is the frame `γ f`, and
`Z = S.frameProducts γ` is the matrix of products of `f` with `γ f`. At boxed points the frames are
uniformly independent, so the vectors shared by the two frames of a near term are short.

## Main definitions and results

* `New.Filling.IsNearTermAt.eq_of_frameImage_eq`: near terms moved by elements of
  `New.Filling.classUnipotent₀` are determined by their frames.
* `New.Filling.HasCellRank.mulVec_eStar_eq_zero_and_sum_indexX₀_le`,
  `New.Filling.col_eq_zero_of_norm_lt_one`: certain vectors have a short `X₀`-part, and a short
  vector of the lattice of `c` in `X₀` is zero.
* `New.Filling.exists_mem_classUnipotent₀_frameImage_mul_eq`: take two terms with the same integral
  `S.frameProducts`, with nonzero leading minor of order `j`, and the same shared vectors, whose
  frames agree outside the first block of rows and differ in that block by `S.frameModulus` times an
  integral matrix. Then an element of `S.classUnipotent₀ c` carries one frame to the other.

Notions from other files:
* `New.Filling.paddedLeading`: the first j rows of Z, completed by rows of the identity matrix.
* `New.Filling.HasCellRank`: γ has cell rank j, that is, the flags of the two frames share vectors
  from the index j on (`NormOnePairOccursFrom`), the leading minor D_j of Z(γ) is nonzero, and the
  discriminant `termDisc` of γ is nonzero exactly when j = ϱ + 1.
* `New.Filling.classUnipotent₀`: the rational unipotent elements of level M for the class c that fix
  every vector of the frame.
* `New.Filling.IsNear`: γ is near if y and γ⁻¹y are both boxed points for some archimedean y.

## Relation to the literature

See `New.Spanning.RemainingTerms.Sum` for related work.



## Short vectors of terms with a cell rank, and near terms with equal frames

Throughout, "`γ` has cell rank `j`" means `S.HasCellRank j γ` (this is not the level `M = S.M`). In
this section only `IsNearTermAt.eq_of_frameImage_eq` assumes `S.IsAdmissible`, and no lemma assumes
a primitive 5040th root of unity in `E`.


### `HasCellRank.mulVec_eStar_eq_zero_and_sum_indexX₀_le`

 Let `γ` have cell rank `j` (`HasCellRank`), let `Z = S.frameProducts γ` be the matrix of
products of the frame `f` with `γ f`, and let `k` be the last index or `j ≤ k`. The combination `y`
of the frame `γ f` with the coefficients of column `k` of `(paddedLeading j Z)⁻¹` has (a) no
coordinates along the isotropic vectors `e*_a` dual to the `e_a` and (b) an `X₀`-part of squared
length at most `1/5` under the embedding `Φ v` of every infinite place `v`. 

### `col_eq_zero_of_norm_lt_one`

 Let `l` be a matrix over `E` whose columns are vectors of `X₀` in the lattice of the class `c`
(their lattice coordinates `S.classCoordX₀ c * l` are integral). If column `i` has squared length
below `1` at every infinite place, it is zero. 

### `IsNearTermAt.eq_of_frameImage_eq`

 Let `S` satisfy the standing hypotheses `S.IsAdmissible` on the level and the sizes. Let `u` and
`u'` be in `U⁰_c = S.classUnipotent₀ c`, the rational unipotent elements of level `S.M` for the
class `c` that fix the standard frame. Let `p = (c', γ)` and `p' = (c'', γ')` be near terms for `c`
at the same position `t` (`IsNearTermAt`). If `u γ` and `u' γ'` have the same frame image
(`frameImage`), then `p = p'`. 


## Uniform independence of frames at boxed points

At a boxed point `y` the coefficients of a combination of the vectors `y⁻¹ f_l` are bounded by a
power of `b` times its length.


### `norm_adjugate_le`

 If the entries of `A` have norm at most `B`, those of its adjugate have norm at most
`(n ^ 2 * B) ^ n`, as they are minors of order `n` up to sign. 

### `norm_adjugate_le_pow`

 If the entries of a complex matrix of order `ϱ + 1` have norm at most `b ^ e`, where `b = S.b`
is the size parameter of the data `S`, those of its adjugate have norm at most `b ^ ((2 + e) ϱ)`. 

### `norm_coeff_le_norm_sum_frameVector`

 Let `y` be a point of the real unitary group `𝔰.G₁`. Let the vectors `y⁻¹ f_l = frameVector y l`
of the frame `f = (e₁, …, e_ϱ, z)` have length at most `S.frameBoxRadius = b ^ (37 n)`. Let `y` also
have length at most `b ^ (7 n)`. Here `b = S.b`, `ϱ` is the number of hyperbolic planes, and
`n = ϱ + 1`. The length `besselLength y` is the infimum of the operator norm `‖s y‖ + 1` over `s` in
the Bessel subgroup. Then each coefficient `x a` of the combination `∑ x l • frameVector y l` is at
most `b ^ (46 n²)` times the length of the combination. 

### `sum_smul_frameVector_eq`

 At the infinite place `v`, for `y` giving a point of `𝔰.G₁` at each infinite place and a column
`x` over `E`: take `frameImage γ *ᵥ x`, embed each coordinate `i` by `Φ v`, divide it by
`S.basisScale v i`, and apply `(y v)⁻¹`. The result is the sum over `k` of
`Φ v (x k) / S.basisScale v (𝔰.besselFrame k)` times `frameVector (((S.ratToInf γ)⁻¹ * y) v) k`. 

### `norm_basisScale_besselFrame_le`

 Let `S` satisfy the standing hypotheses `S.IsAdmissible`, which give `1 ≤ |κ_v| ≤ b ^ 23` for
`κ_v = S.realM v` and `b = S.b`. At the infinite place `v` of the CM field `E`, the scale factors
`S.basisScale v` of the normalised basis at two vectors of the frame differ in norm by a factor at
most `b ^ (23 ϱ)`. 

### `norm_sum_div_basisScale_smul_frameVector_le`

 Let `S` satisfy the standing hypotheses `S.IsAdmissible` on the level and the sizes, and let `v`
be an infinite place of the CM field `E`. Let the frame vectors `z⁻¹ f_k` at `z` have length at most
`S.frameBoxRadius = b ^ (37 n)`. Take their combination whose coefficients are numbers `x k` of norm
at most `B` divided by the scale factors `S.basisScale v` of the normalised basis. Its length is at
most `B b ^ (1 + 23 ϱ + 37 n)` divided by the norm of the scale factor of any frame vector `a`,
where `b = S.b` and `n = ϱ + 1`. 

### `IsNear.norm_adjugate_paddedLeading_le`

 Assume `S.IsAdmissible`, the standing hypotheses on the level and the sizes. Let `γ` be near
(`S.IsNear γ`): for some point `y` of `𝔰.G₁` at each infinite place, both `y` and `γ⁻¹ y` lie in
`boxedPoints`. Let `Y` be the first `j` rows of the matrix `S.frameProducts γ` of products
`h(f_i, γ f_l)`, completed by rows of the identity matrix. At every infinite place `v`, with
embedding `Φ v`, the entries of the adjugate of `Y` have norm at most
`S.b ^ ((2 + 134 𝔰.n) 𝔰.ϱ)`. 

### `sharedVectors`

 The coordinates in the isotropic space `A` spanned by `e₁, …, e_ϱ` of the columns `k ≥ j` of
`γ f · adj Y`, where `f` is the frame, `γ f = frameImage γ`, and `Y` consists of the first `j` rows
of the matrix of products completed by rows of `1`; the columns `k < j` are set to `0`. For `γ` of
cell rank `j` these columns lie both in the span of `f` and in the span of `γ f`. There are none
when `j = ϱ + 1`. 

### `HasCellRank.exists_frameImage_one_mulVec_eq`

 Let `γ` have cell rank `j` (`S.HasCellRank j γ`). Let `k ≥ j`. Then column `k` of `γ f · adj Y`
lies in the span of the frame `f = frameImage 1`. Here `γ f = frameImage γ`, and `Y` is the first
`j` rows of the matrix of products `S.frameProducts γ`, completed by rows of the identity matrix. 

### `frameProducts_mul_of_mem_besselU0`

 Left multiplication by an element `u` of `besselU0`, the unipotent elements that fix each vector
of the frame `f`, does not change the matrix of products `h(f_i, γ f_l)`. 

### `HasCellRank.sharedVectors_mul_of_mem_besselU0`

 Let `γ` have cell rank `j` (`S.HasCellRank j γ`) and let `u` be in `besselU0`, the unipotent
elements that fix each vector of the frame `f`. Then `u γ` and `γ` have the same shared vectors (the
first `ϱ` coordinates of the columns `k ≥ j` of `γ f · adj Y`, see `sharedVectors`), as these
columns lie in the span of `f`. 

### `HasCellRank.norm_sharedVectors_le`

 Let `S` satisfy the standing hypotheses `S.IsAdmissible` on the level and the sizes. Let `γ`
have cell rank `j`. Let `γ` also be near. Let `Y` be the first `j` rows of `S.frameProducts γ`
completed by rows of `1`. If `j ≤ k`, column `k` of `S.sharedVectors j γ` consists of the
coordinates along `e₁, …, e_ϱ` of column `k` of `γ f · adj Y`, which lies in the spans of both the
frame `f` and `γ f`. If `k < j`, the column is zero. All these entries have norm at most
`S.b ^ (182 n²)` under the embedding `Φ v` of every infinite place `v`, where `n = ϱ + 1`. 


## Moving frames by the unipotent group of the level

Take two frames with the same integral matrix of products, with nonzero leading minor, and the same
shared vectors. If they agree outside the isotropic space and are congruent modulo `frameModulus`,
they are carried to one another by a move, that is, a unipotent element of level `M` that fixes the
standard frame.


### `skewSolution`

 The matrix `σ = δ̄ μ α - δ (μ α)ᴴ - αᴴ Pᴴ μ α`, a skew-hermitian solution of `σ P = δ δ̄ μ` when
`Pᴴ μ` is skew-hermitian and `μ α P = δ μ`. Under these hypotheses, if `δ` is invertible and
`δ⁻¹ μ α`, `δ⁻¹ P α` have the blocks `(μ₁, 0; μ₂, 0)`, `(1, 0; θ, 0)`, then `σ` is `δ δ̄` times the
block matrix `(μ₁ + μ₂ᴴ θ, -μ₂ᴴ; μ₂, 0)`. 

### `conjTranspose_skewSolution`

 If `Pᴴ μ` is skew-hermitian, so is `skewSolution P μ α δ`. 

### `skewSolution_mul`

 If `Pᴴ μ` is skew-hermitian and `μ α P = δ μ`, then `σ = skewSolution P μ α δ` solves
`σ P = δ δ̄ μ`: the first term gives `δ δ̄ μ` and the other two cancel. 

### `isIntMatrix_skewSolution`

 If `P`, `μ`, `α` and `δ` have entries in a subring `O` stable under the involution, so has
`skewSolution P μ α δ`. 

### `frameModulus`

 The modulus `M * det (Y * Yᴴ)` for frames with the products `Z`, where `M = S.M` is the product
of the two level primes and `Y` consists of the first `j` rows of `Z` completed by rows of `1`. 

### `isStarStable_comap_Ô`

 The elements of `E` that are integral at every finite place, the preimage of the ring `Ô E` of
integral finite adeles, form a subring stable under conjugation. 

### `frameModulus_ne_zero`

 The modulus `S.frameModulus j Z`, which is `M * det (Y * Yᴴ)` with `M = S.M` and `Y` the first
`j` rows of `Z` completed by rows of `1`, is nonzero if `leadingMinor Z j`, which is `det Y`, is
nonzero. 

### `isIntMatrix_paddedLeading`

 If the entries of `Z` are algebraic integers, then its first `j` rows completed by rows of `1`
have entries that are integral at every finite place. 

### `mul_paddedLeading_eq_submatrix_mul_isotropicRows`

 Let `Y` be the first `j` rows of `Z` completed by rows of `1`, and let `P = isotropicRows Z` be
the first `ϱ` rows of `Z`. If the last column and the columns `k ≥ j` of `η` vanish, then `η Y` is
the product of the first `ϱ` columns of `η` with `P`, as the other rows of `Y` are rows of `P`. 

### `mul_adjugate_mul_isotropicRows`

 Let `Y` be the first `j` rows of `Z` completed by rows of `1`, let `P = isotropicRows Z` be the
first `ϱ` rows of `Z` and `α` the first `ϱ` columns of `adj Y`. If the last column and the columns
`k ≥ j` of `X adj Y` vanish, then `X α P = det Y • X`, as the other rows of `Y` are rows of `P`. 

### `mulVec_adjugate_top_eq_zero`

 At the top cell rank `j = ϱ + 1`, with `paddedLeading j Z = Z`, let `P = isotropicRows Z` be the
first `ϱ` rows of the invertible matrix `Z` over the CM field `E`. If `Pᴴ μ` is skew-hermitian for
the complex conjugation of `E`, then `μ` kills the last column of `adj Z`: so does `P`, and `Pᴴ` is
injective. 

### `inclMatrix_conjTranspose_mul_frameImage`

 The products of the isotropic vectors `e₁, …, e_ϱ` (the columns of `inclMatrix E Sum.inl`) with
the frame `γ f` for the Gram matrix `S.ratGram` are the first `ϱ` rows of `S.frameProducts γ`. 

### `conjTranspose_mul_isotropicRows_eq_neg`

 Let `γ` and `γ'` be in the unitary group `S.G E`, with underlying matrices `γ.val.val` and
`γ'.val.val`. Let the frame of `γ'` be that of `γ` with `ξ` added to the first block of rows, and
let `P` be the first `ϱ` rows of `S.frameProducts γ`. Then `Pᴴ ξ` is skew-hermitian for the complex
conjugation of the CM field `E`, as both frames have the same Gram matrix. 

### `frameImage_sub_mul_adjugate_apply_eq_zero`

 Let `γ` and `γ'` have the same matrix of products `S.frameProducts` and the same shared vectors
`S.sharedVectors j`. Here `Y = paddedLeading j (S.frameProducts γ)` is the first `j` rows of the
matrix of products completed by rows of `1`. Let `ξ` be the first block of rows (`toRows₁`) of
`frameImage γ' - frameImage γ`, the difference of the images `γ' f`, `γ f` of the frame. Then the
columns `k ≥ j` of `ξ adj Y` vanish. 

### `exists_frameImage_mul_eq_add_fromRows`

 Let `S` satisfy the standing hypotheses `S.IsAdmissible` on the level and the sizes. Let `σ` be
a skew-hermitian matrix over `E` that is integral at every finite place, and let `P` be the first
`ϱ` rows of `S.frameProducts γ`. Then an element of `S.classUnipotent₀ c`, the unipotent group of
level `M` fixing the standard frame `f`, adds `M σ P` to the first block of rows of
`γ f = frameImage γ`. Here `M = S.M` is the product of the two level primes. 

### `exists_mem_classUnipotent₀_frameImage_mul_eq`

 Let `S` satisfy the standing hypotheses `S.IsAdmissible` on the level and the sizes. Let `γ` and
`γ'` have the same integral matrix of products `Z = S.frameProducts γ` with nonzero leading minor of
order `j`, and the same shared vectors `S.sharedVectors j`. Let `Y` be the first `j` rows of `Z`
completed by rows of `1`. If the two frames agree outside the isotropic space and differ there by
`S.frameModulus j Z = M det (Y Yᴴ)` times an integral matrix `X`, then a move, an element of the
unipotent group `S.classUnipotent₀ c` of level `M = S.M` fixing the standard frame, carries the
frame of `γ` to that of `γ'`. 
