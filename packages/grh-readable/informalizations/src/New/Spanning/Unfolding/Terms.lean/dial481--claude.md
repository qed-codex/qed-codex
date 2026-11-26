---
{
  "module": "src/New/Spanning/Unfolding/Terms.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Terms.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Terms.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Near terms in the filling theorem: frames, cell ranks, nearness and integrality

The terms `γ` of the count in the filling theorem are rational elements of the unitary group.
The data are `S : New.Filling E 𝔰` for a shape `𝔰`, with the size hypotheses
`New.Filling.IsAdmissible`, which compare all constants with powers of the large parameter `b`.
For the frame `(e₁, …, e_ϱ, z)`, `New.frameImage γ` is the matrix of its image under `γ`, and
`S.frameProducts γ` is the Gram matrix of the frame against its image, with leading minors
`New.leadingMinor`. This file describes how the flags of the frame and of its image under `γ` meet,
defines the cell rank and nearness of `γ`, proves a norm identity for `S.termDisc γ`, bounds the
Gram entries of near terms by powers of `S.b`, and shows that the Gram entries of terms are
algebraic integers.

## Main definitions and results

* `New.Filling.CharsAgree`, `New.PairOccursAt`, `New.Filling.HasCellRank`: the terms that respect
  the unipotent character, the vectors common to the two flags of a term, and its cell rank.
* `New.Filling.IsNear`: `γ` is near if some boxed point `y` (`New.Filling.boxedPoints`) has `γ⁻¹ y`
  boxed.
* `New.Filling.norm_sq_middle_part_eq`, `New.Filling.map_termDisc_eq_norm`: a norm identity, which
  makes `S.termDisc γ` real and nonnegative at every infinite place. So `S.termDisc γ` is totally
  positive or zero (`New.Filling.termDisc_pos_or_eq_zero`).
* `New.Filling.IsNear.norm_frameProducts_le`, `New.Filling.IsNear.norm_map_leadingMinor_sq_le`: for
  a near term, the Gram entries and the leading minors are bounded by powers of the size parameter
  `S.b`.

Notions from other files:
* `New.Filling.G`: for a commutative ring R with involution, the unitary group over R of ϱ
  hyperbolic pairs and the middle Gram matrix diag(1, …, 1, −N) on X₀ ⊕ Ez, in the basis e₁, …, e_ϱ;
  x_i (i in κ), z; e*₁, …, e*_ϱ.
* `New.Filling.termDisc`: 𝗀(γ) = |D_{ϱ+1}|² − N²|D_ϱ|², with D_l the leading minors of
  `New.Filling.frameProducts γ`.
* `New.Shape.Form.besselU`, `New.Shape.Form.besselU0`: the Bessel unipotent group 𝖴 of isometries
  that are block upper unitriangular and trivial on the middle block, and its elements that fix each
  vector of the frame.
* `New.Filling.mainSecondMoment`, `New.Filling.identitySecondMoment`: the numbers
  sourceDim² / (besselDegree · mass), with the mass of the genus of the standard lattice, and
  sourceDim times the order of the reduced image of the Bessel subgroup `besselS`.


### `Filling.zRowBlockDiagonal`

 For a square matrix T on the middle coordinates, the two-row block diagonal matrix with two
copies of the row of T indexed by z. 

### `commonLink`

 The module of the vectors x of X₀ for which there is a pair of middle vectors, both orthogonal
to z, that lies in the links (`New.link`) of both γ and γ' and whose first vector has
X₀-coordinates x. 

### `PairOccursAt`

 The frame f = (e₁, …, e_ϱ, z) and its image γf satisfy fx = γfy for some coefficient vectors
x, y that vanish at indices above a and have x_a = c, y_a = c'. 

### `NormOnePairOccursFrom`

 For some c with c c̄ = 1 and every index a ≥ j (counted from 0), the flags of f and γf share a
vector with leading coefficients c and 1 at a. 

 ### Forms, coordinates, cell ranks and nearness 

### `ratGram`

 The Gram matrix over E of the form on the space: two dual isotropic blocks of rank ϱ around the
middle Gram matrix `S.ratMiddle E` of X₀⊕Ez. 

### `linkForm`

 The block diagonal matrix diag(M, −M) over E on two copies of X₀⊕Ez, M = `S.ratMiddle E`. 

### `classCoord`

 For a class c, the inverse of the matrix `New.Filling.classBasis` c; it takes rational
coordinates to coordinates in the basis of the lattice h_cΛ₀. 

### `classCoordX₀`

 The matrix whose columns are the standard basis vectors of X₀, written in the basis of the
middle part of the lattice h_cΛ₀ of the class c. It is `New.middleInclusionMatrix` times the inverse
of the chosen representative `c.out` of c in U(X₀)(𝔸_f), whose image in the unitary group of V is
h_c = `S.classRep c`. It depends on this choice of representative. 

### `pairCountScale`

 The number `n_p = #R̄₀ n_X N ^ (-k f)` against which pairs of terms are counted: here `R̄₀` is
the reduced image of the Bessel subgroup `besselS`, `n_X` the number of classes and `f` the number
of infinite places. 

### `HasCellRank`

 γ has cell rank j ≤ ϱ+1: `New.NormOnePairOccursFrom` j holds, the leading minor D_j of
`S.frameProducts γ` is nonzero, and `S.termDisc γ` is nonzero exactly when j = ϱ+1. 

### `HasCellRank.normOnePairOccursFrom`

 For some c with c c̄ = 1 and every index a ≥ j, the flags of the frame f and of γf share a
  vector with leading coefficients c and 1 at a. 

### `HasCellRank.leadingMinor_ne_zero`

 The leading minor D_j of the products of the two frames is nonzero. 

### `HasCellRank.lt_iff_termDisc_ne_zero`

 The cell rank is the top one, ϱ+1, exactly when `S.termDisc γ` is nonzero. 

### `termDiscNorm`

 The product over the infinite places v of E of the complex absolute values of the images under
the embeddings `Φ v` of `S.termDisc γ` = |D_{ϱ+1}|² − N²|D_ϱ|², where D_l is the leading minor of
order l of `S.frameProducts γ`. 

### `IsNear`

 The rational element γ is near: there is an archimedean point y such that both y and γ⁻¹y
lie in the set `New.Filling.boxedPoints` of boxed points. 

### `CharsAgree`

 The finite character `New.Filling.unipotentChar` takes the same value at u and at γ⁻¹uγ for
every rational u in 𝖴 ∩ γ𝖴γ⁻¹. 

 ### Frames and the Bessel subgroup 

### `frameImage_mul`

 The frame columns of a product s s' are s times those of s'. 

### `frameImage_mul_of_mem_besselU0`

 Multiplying γ on the right by an element u of `New.Shape.Form.besselU0`, which fixes the frame
(e₁, …, e_ϱ, z), does not change the image of the frame. 

### `frameImage_inv_mul_eq_iff`

 The isometry s⁻¹s' fixes the frame (e₁, …, e_ϱ, z) if and only if s and s' map the frame to
the same vectors. 

### `form_frameImage_mulVec`

 A unitary γ preserves the form on combinations of frame vectors: γf · y has the same product
with itself as f · y. 

 ### Vectors shared by two frames and the norm identity 

### `star_mul_last_eq_of_frameImage_eq`

 If `f · x = γ f · y`, then the `z`-coefficients of `x` and `y` have the same norm. 

### `frameProducts_mulVec_of_frameImage_eq`

 If `γ f · y = f · x`, then its products with the frame vanish except the one with `z`, which
is `-N` times the `z`-coefficient of `x`. 

### `eq_zero_of_ratMiddle_form_eq_zero`

 The middle form is anisotropic on the vectors without `z`-coordinate. 

### `frameImage_mulVec_eStar_eq_zero`

 If `γ f · y` is orthogonal to `e₁, …, e_ϱ` and has product `D` with `z`, then it has no
`e*`-part. 

### `neg_mul_frameImage_mulVec_z_eq`

 If `γ f · y` is orthogonal to `e₁, …, e_ϱ` and has product `D` with `z`, then `-N` times
its `z`-coordinate is `D`. 

### `mul_sum_norm_sq_frameImage_mulVec_eq`

 If `γ f · y` is orthogonal to `e₁, …, e_ϱ` and has product `D` with `z`, then at each
infinite place `N` times the squared length of its `X₀`-part is `|D|² - N² |y_z|²`. 

### `exists_frameImage_one_mulVec_eq_of_nonpos`

 A vector `t` without `e*`-part lies in the span of the frame `f` if, at some infinite place,
`N` times the squared length of its `X₀`-part is at most zero. 

### `norm_sq_middle_part_eq`

 Let `γ` be a rational element of the unitary group, `f = (e₁, …, e_ϱ, z)` the frame, and let
`t = γ f · y` be the combination of the image vectors with coefficients `y`. Suppose that `t` is
orthogonal to `e₁, …, e_ϱ` and has product `D` with `z`. Then `t` has no component along the dual
vectors `e*₁, …, e*_ϱ`, and `-N` times its `z`-coordinate is `D`. At each infinite place, `N` times
the squared length of the `X₀`-part of `t` is `|D|² - N² |y_z|²`, where `y_z = y 𝔰.top`; if it is at
most zero at some place, then `t` lies in the span of `f`. 

### `map_termDisc_eq_norm`

 Let γ be any rational element of the unitary group, and let D_l be the leading minors of the
matrix `S.frameProducts γ` of products of the frame (e₁, …, e_ϱ, z) with its image under γ. At every
infinite place v the image of `S.termDisc γ` = |D_{ϱ+1}|² − N²|D_ϱ|², where |x|² means x x̄, equals
its absolute value: it is real and nonnegative. 

### `hasCellRank_last`

 If `S.termDisc γ` is nonzero, then `γ` has cell rank `ϱ + 1` (`S.HasCellRank` at
`last (𝔰.ϱ + 1)`). First, `NormOnePairOccursFrom (ϱ + 1)` holds vacuously, since no frame index lies
beyond it. Second, the determinant of `S.frameProducts γ` is nonzero. 

### `termDisc_pos_or_eq_zero`

 Either `S.termDisc γ` is totally positive, and then the matrix of products of the two frames
has a nonzero determinant, or `S.termDisc γ` vanishes. 

### `gramDiscReal_realFrameGram_ratToInf`

 Let `γ` be a rational element of the unitary group and `γ_v = S.ratToInf γ v` its rescaled image
at the infinite place `v`. Let `Z = realFrameGram γ_v` be the matrix of products of the frame
`(e₁, …, e_ϱ, z)` with its image under `γ_v`, and `D_ϱ` the leading principal minor of order `ϱ` of
`Z`. Then `gramDiscReal Z = |det Z|² - |D_ϱ|²` is `s²` times the complex absolute value of
`S.termDisc γ` under the embedding `Φ v`, where `s` is the product of the squared scales
`S.frameScaleSq v a` of the `n = ϱ + 1` frame vectors. 

 ### Passing to the infinite and the finite places; the Bessel group; sizes of constants 

### `ratToInf_mem_besselU0`

 The image of an element of `New.Shape.Form.besselU0` at an infinite place lies in the
corresponding subgroup of the complex unitary group `𝔰.G₁`. 

### `frameImage_ratToInf_mulVec`

 The image of γ at v is the conjugate of Φ_v γ by the diagonal `S.basisScale v`, so applied to
frame coordinates rescaled relative to a reference index a it gives the rescaled value of γf · y. 

### `_root_.New.NormOnePairOccursFrom.ratToInf`

 The property that a norm-one pair occurs from `j` passes from a rational element γ to its
rescaled image `S.ratToInf γ v` at any infinite place `v`. 

### `termsOver.isIntMatrix_translateByClassReps`

 If γ is a term over (c, r, c'), then the matrix of h_c⁻¹ γ h_c' in the lattice basis is
integral over Ô E. 

### `classCoord_conj_splitGram`

 For a class c, the matrix classCoord c, which takes rational coordinates to coordinates in the
basis of the lattice h_cΛ₀, carries the form in rational coordinates to the form in lattice
coordinates. 

### `frameImage_translateByClassReps`

 The frame image of h_c⁻¹ γ h_c' in the lattice basis is the frame image of γ, read in the
adeles and written in the coordinates classCoord c of the lattice h_cΛ₀. 

### `frameGram_translateByClassReps`

 The Gram matrix of the adelic element `h_c⁻¹ γ h_c'` in the lattice basis is that of `γ`. 

### `IsNear.mul_of_mem_besselU0`

 If γ is near, that is, γ joins two boxed archimedean points, then so is u γ u' for rational u
and u' in the group besselU0 of Bessel unipotent elements that fix the frame. 

### `mem_besselS_of_frameImage_eq_one`

 An isometry that fixes every vector of the frame (e₁, …, e_ϱ, z) lies in `besselS`. 

### `pow_le_tailScale`

 For admissible data with size parameter `b`, the powers `b ^ e` with `e ≤ 10 ^ 5 n ^ 9 f` are at
most `τ = S.tailScale = b ^ (k f / 4)`. Here `n = ϱ + 1` is the number of frame vectors, `k` is the
rank of `X₀` and `f` is the number of infinite places. 

### `tailScale_pow_four`

 For admissible data, the fourth power of `tailScale` `τ = b ^ (k f / 4)` is `b ^ (k f)`, where
`k = 𝔰.k` and `f = numInfPlaces E` is the number of infinite places of `E`. 

### `tailScale_pow_mul_identitySecondMoment_le`

 The ratio of `mainSecondMoment` to `identitySecondMoment` is at least `τ ^ 44 = b ^ (11 k f)`,
where `τ = tailScale`. 

### `pairCountScale_pos`

 The number `pairCountScale`, which is the size of the reduced image of the Bessel subgroup times
the number of classes, divided by `N ^ (k f)`, is positive. 

### `mul_sq_le_cube`

 For a natural number `C ≤ 10 ^ 5`, `C * 𝔰.n ^ 2 ≤ 𝔰.n ^ 3`. This holds because the filling data
`S` forces `𝔰.n ≥ 10 ^ 5`. 

### `IsNear.norm_frameProducts_le`

 Let the data be admissible, with size parameter `b = S.b`, and let `γ` be near: some archimedean
point `y` has both `y` and `γ⁻¹ y` in `boxedPoints`. Then the products of the frame vectors with
their images under `γ`, the entries of `S.frameProducts γ`, have absolute value at most
`b ^ (134 n)`, `n = ϱ + 1`, at every infinite place `w`. 

### `IsNear.norm_map_leadingMinor_sq_le`

 For admissible data with size parameter `b = S.b` and a near term `γ` (see `IsNear`), the
leading minors of the matrix `S.frameProducts γ` of products of the frame with its image under `γ`
have squared absolute value at most `b ^ (270 n²)`, `n = ϱ + 1`, at every infinite place `w`. 

### `termsOver.inv_mul_mem_reducedImage`

 Under `S.IsAdmissible`, if `γ` is a term over `(c, r, c')` and `u` is a term over `(c, r', d)`
with the same frame image `frameImage γ = frameImage u`, then `r⁻¹ * r'` lies in
`S.reducedImage besselS`, the reduced image of the Bessel subgroup. So `r` and `r'` lie in one left
coset of it. 

### `termsOver.eq_and_mem_classUnipotent₀`

 Under `S.IsAdmissible`, let `γ ∈ S.termsOver c r c'` and `u ∈ S.termsOver c r d`. Suppose they
have the same `frameImage`, the image of the frame `(e₁, …, e_ϱ, z)`. Then `c' = d` and `γ⁻¹ * u`
lies in `S.classUnipotent₀ c'`, the integral unipotent elements fixing every frame vector. 

### `isIntegral_frameProducts`

 If `γ` is a term over `(c, r, c')`, so that `h_c⁻¹ γ h_c'` is integral, then the products of
the frame with its image under `γ` are algebraic integers. 
