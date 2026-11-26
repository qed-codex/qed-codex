---
{
  "module": "src/New/Spanning/Unfolding/Link.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Link.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Link.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Links of isometries, the link isometry Υ_γ, and invariance under `besselU`

Let `γ` be an isometry of the form `T.splitGram`, which is made of `ϱ` hyperbolic planes and a
middle space with Gram matrix `T`. Let `A` be the span of the first `ϱ` basis vectors, and let
`New.frameImage γ` be the image of the frame `(e₁, …, e_ϱ, z)`. The link of `γ` is the set of pairs
of middle coordinates of `t` and `γ⁻¹ t`, for `t` orthogonal to `A` and `γ A`.

A filling `S` over a CM field `E` provides a prime `N = S.N`. Its middle space is `X₀ ⊥ E z_N`,
where `X₀` has an orthonormal basis indexed by `𝔰.κ` and `z = z_N` has the norm `-N`. The positive
space `X₀ ⊥ E z⁺` has the same coordinates, and `z⁺` has the norm `N`. After an exchange of the
`z_N`-coordinates of the two members of each pair (`linkSource`, `linkTarget`), the link is the
graph of an isometry `Υ_γ` (`linkIsometry`) of the positive space. The quantity `termDisc γ`
vanishes if and only if the spans of the frame and of its image under `γ` share a nonzero vector.

## Main definitions and results

* `New.Filling.link_inv_mul_mul_of_mem_besselU`,
  `New.Filling.frameDisc_frameGram_inv_mul_mul_of_mem_besselU`: the link and `New.frameDisc` are
  unchanged under `γ ↦ u⁻¹ γ u'` with `u`, `u'` in `besselU`.
* `New.NormOnePairOccursFrom.besselU_mul`, `New.NormOnePairOccursFrom.inv`: the norm-one pair
  condition is preserved by left multiplication by `besselU` and by inversion. With the invariance
  of the minors and of `termDisc`, this makes the cells stable (`New.Filling.isStable_hasCellRank`).
* `New.Filling.frameDisc_weylElem_mul`, `New.Filling.link_weylElem_mul_eq_iff`: values on the big
  cell, at `weylElem 𝔰.ϱ p * σ` with `σ` an isometry of the middle space. There the link determines
  `σ`.
* `New.Filling.linkIsometry`, `New.Filling.mem_link_iff_linkIsometry`: the isometry `Υ_γ`, and the
  link as its graph.
* `New.Filling.linkIsometry_frameImage_mulVec`, `New.Filling.mul_dotProduct_comp_indexX₀_eq_sub`:
  the link on combinations of the second frame, and the norm identity that follows.
* `New.Filling.termDisc_eq_zero_iff`: the criterion for the vanishing of `termDisc γ`.

Notions from other files:
* `New.Shape.Form.splitGram`: the Gram matrix of `ϱ` hyperbolic planes and a middle space with Gram
  matrix `T`. The basis is `e₁, …, e_ϱ`, the middle vectors, `e*₁, …, e*_ϱ` (indices `New.eStar`).
* `New.Shape.Form.besselU`: the isometries that are block upper unitriangular for this basis.
* `New.Shape.Form.frameGram`: the `(ϱ + 1) × (ϱ + 1)` matrix of the products `h(f_j, γ f_l)` of the
  frame `f` with its image under `γ`, where `h` is the form `T.splitGram`.
* `New.Filling`: arithmetic data over a CM field `E`, among them the prime `S.N`. The matrix
  `S.ratMiddle E` is the Gram matrix of `X₀ ⊥ E z_N`, `S.ratGram` is its `splitGram`, `S.G E` is the
  group of isometries of `S.ratGram`, and `S.frameProducts γ` is the frame Gram matrix of `γ`.
* `New.frameDisc`: for a matrix of size `ϱ + 1` with leading minors `D_l`, the quantity
  `|D_{ϱ+1}|² - N² |D_ϱ|²`. Its value at `S.N` and the frame Gram matrix of `γ` is
  `New.Filling.termDisc γ`.
* `New.NormOnePairOccursFrom j γ`, the condition that a norm-one pair occurs from `j`: there is a
  `c` with `c c̄ = 1` such that, for every frame index `a ≥ j` (counted from `0`), the flags of `f`
  and `γ f` share a vector with leading coefficients `c` and `1` at `a`.



## Invariance of links and cells under the unipotent group

A vector `t` is orthogonal to `A` and `γ A` iff the coordinates at the `e*_a` of `t` and `γ⁻¹ t`
vanish. This describes the link in coordinates and gives its invariance under `besselU`.


### `splitGram_mulVec`

 The form `T.splitGram` exchanges the first and last blocks of coordinates of `v` and applies `T`
to the middle block. 

### `linkMatrix_mulVec`

 The matrix `linkMatrix γ` sends `t` to the pair of the middle blocks of `t` and of `γ⁻¹ t`. 

### `orthogonal_isotropicFramePair_iff`

 A vector `t` is orthogonal to `A = ⟨e₁, …, e_ϱ⟩` and to `γ A` (so to the span `A + γ A` of the
columns of `isotropicFramePair γ`) iff the last `ϱ` coordinates, those at the `e*_a`, of both `t`
and `γ⁻¹ t` vanish. 

### `mem_link`

 The link in coordinates: a pair `p = (y, y')` of middle vectors is in the link of `γ` iff,
for some `a`, `γ` maps the vector with blocks `(a, y', 0)` to a vector with last two blocks
`(y, 0)`. 

### `NormOnePairOccursFrom.inv`

 Let `f = (e₁, …, e_ϱ, z)` be the frame. The condition `NormOnePairOccursFrom j γ` says that, for
some `c` with `c c̄ = 1` and every index `a ≥ j`, there are combinations of `f` and of `γ f` that
are equal, have no coefficients above `a`, and have the coefficients `c` and `1` at `a`. If it holds
for `γ`, then it holds for `γ⁻¹`. 

### `Filling.exists_frameImage_eq_of_pairOccursAt`

 Let `f = frameImage 1` be the frame `(e₁, …, e_ϱ, z)`, and let `frameImage γ` be its image
`γ f`. Suppose `PairOccursAt γ c 1 a` holds for each index `a ≥ j`: some combination of `f` equals
some combination of `γ f`, with no coefficients above `a` and with coefficients `c` and `1` at `a`.
Then for every `y` there are `x` and `y'` with `frameImage 1 *ᵥ x = frameImage γ *ᵥ y'` and
`y' a = y a` for all `a ≥ j`. 

### `Filling.exists_frameImage_eq_of_normOnePairOccursFrom`

 Let `γ` satisfy the norm-one pair condition from some `j ≤ ϱ + 1` (for some `c` of norm `1`, the
flags of the frame `f = (e₁, …, e_ϱ, z)` and of `γ f` share a vector with leading coefficients `c`
and `1` at each index `a ≥ j`). Then for every `y` the spans of `f` and `γ f` share a vector whose
coefficients `y'` in `γ f` agree with `y` at the indices `a ≥ j`. 

### `NormOnePairOccursFrom.besselU_mul`

 Let `f = (e₁, …, e_ϱ, z)` be the frame. The norm-one pair condition from `j` says that there is
one `c` with `c c̄ = 1` such that, for every index `a ≥ j`, some combination of `f` equals some
combination of `γ f`, both with no coefficients above `a` and with the coefficients `c` and `1` at
`a`. If it holds for `γ` and `u` is in `besselU`, the group of the isometries that are block upper
unitriangular for the basis `e₁, …, e_ϱ`, middle vectors, `e*₁, …, e*_ϱ`, then it holds for
`u γ`. 

### `mulVec_apply_inr_of_mem_besselU`

 An element of the unipotent group `besselU` fixes the last two blocks of coordinates of a vector
whose last block vanishes. 

### `Filling.link_inv_mul_mul_of_mem_besselU`

 Let `u` and `u'` lie in `besselU`, the group of the isometries that are block upper
unitriangular for the basis `e₁, …, e_ϱ`, middle vectors, `e*₁, …, e*_ϱ`, and so induce the identity
on the middle space. Then the link of `u⁻¹ γ u'` is the link of `γ`. 

### `Filling.frameDisc_frameGram_inv_mul_mul_of_mem_besselU`

 For `u` and `u'` in the unipotent group `besselU`, the quantity `New.frameDisc N`, that is
`|D_{ϱ+1}|² - N² |D_ϱ|²` in the leading minors `D_l`, of the frame Gram matrix is the same for
`u⁻¹ γ u'` as for `γ`. 

### `Filling.isStable_hasCellRank`

 Let `D_l` be the leading minors of the frame Gram matrix `S.frameProducts γ`, the matrix of the
products `h(f_b, γ f_l)` of the frame `f = (e₁, …, e_ϱ, z_N)` with its image under `γ`, so that
`S.termDisc γ = |D_{ϱ+1}|² - N² |D_ϱ|²`. The cell of rank `j` consists of the `γ` in `S.G E` such
that: for some `c` with `c c̄ = 1` and every index `a ≥ j`, a combination of `f` equals one of
`γ f`, both with no coefficients above `a` and with `c`, `1` at `a`; `D_j ≠ 0`; and
`S.termDisc γ ≠ 0` exactly if `j = ϱ + 1`. This cell is stable: for `u`, `u'` in the unipotent group
`besselU`, it contains `u⁻¹ γ u'` if and only if it contains `γ`. 

 ### The big cell 

### `Filling.frameDisc_weylElem_mul`

 Over a field `A` with involution, let `T.splitGram` be hermitian and invertible, with isometry
group `T.G`. Let `σ` fix the hyperbolic planes, and let `w_p = weylElem 𝔰.ϱ p` send `e_a` to
`p a • e*_a`. Let `t = T.frameGram σ 𝔰.top 𝔰.top` be the product of the last frame vector `z` with
`σ z`, and let `d` be the product of the first `ϱ` units of `p`. Let `T.frameGram (w_p σ)` be the
matrix of products of the frame `(e₁, …, e_ϱ, z)` with its image under `w_p σ`. Then `frameDisc N`
of this matrix, that is `|D_{ϱ+1}|² - N² |D_ϱ|²` in its leading minors `D_l`, equals
`d d̄ (t t̄ - N²)`. 

### `Filling.mem_link_weylElem_mul_iff`

 Over a field with involution, let `T.splitGram` be hermitian and invertible. Let `ρ` fix the
hyperbolic planes, and let `w_r = weylElem 𝔰.ϱ r` send `e_a` to `r a • e*_a`. The link of `w_r ρ` is
the graph of the middle block of `ρ`: a pair lies in it if and only if its first member is the image
of the second under this block. 

### `Filling.link_weylElem_mul_eq_iff`

 Over a field with involution, let `T.splitGram` be hermitian and invertible. Let `σ`, `τ` fix
the hyperbolic planes, and let `w_p = weylElem 𝔰.ϱ p` send `e_a` to `p a • e*_a`. Then `w_p σ` and
`w_q τ` have the same link exactly when `σ = τ`. 


## The link as an isometry

The middle form is that of `X₀ ⊥ E z_N`, where `z_N` has the norm `-N`.

A vector `y` orthogonal to `A` and `γ A` gives two classes in `A^⊥ / A = X₀ ⊥ E z_N`, those of `y`
and of `γ⁻¹ y`.


### `rank_conjTranspose_eq`

 Over a field with involution a matrix and its conjugate transpose have the same rank. 

### `colSpan_fromCols`

 The columns of two matrices set side by side span the sum of the two column spaces. 

### `isotropicSpan`

 The space `M A` spanned by the columns `M e_1, …, M e_ϱ`, where `A = ⟨e_1, …, e_ϱ⟩`. 

### `commonIsotropic`

 The space `I_γ = A ∩ γ A`, where `A = ⟨e_1, …, e_ϱ⟩`. 

### `isotropicPerp`

 The orthogonal complement `(A + γ A)^⊥`, where `A = ⟨e_1, …, e_ϱ⟩`, for the form
`S.ratGram = (S.ratMiddle E).splitGram` of `ϱ` hyperbolic planes and the space `X₀ ⊥ E z_N`. 

### `positiveGram`

 The Gram matrix of the positive space `X₀ ⊥ E z⁺`, where `X₀` has an orthonormal basis and `z⁺`
has the norm `S.N`, the prime of the filling `S`. 

### `linkSource`

 The map that sends the pair of classes `(y₀ + λ' z_N, y₀' + λ z_N)` to `y₀ + λ z⁺`. 

### `linkTarget`

 The map that sends the pair of classes `(y₀ + λ' z_N, y₀' + λ z_N)` to `y₀' + λ' z⁺`. 

### `eq_of_linkSource_eq_of_linkTarget_eq`

 A pair `p` of classes (a function on `𝔰.MiddleIndex ⊕ 𝔰.MiddleIndex`) is determined by its two
images `linkSource E 𝔰 p` and `linkTarget E 𝔰 p` in `X₀ ⊥ E z⁺`. 

### `dotProduct_positiveGram_mulVec_eq_sum_add`

 The form `S.positiveGram` of `X₀ ⊥ E z⁺` in coordinates: `𝔰.κ` indexes an orthonormal basis of
`X₀`, and `z⁺`, at the index `inr ()`, has the norm `S.N`. 

### `dotProduct_ratMiddle_mulVec_eq_sum_sub`

 The form `S.ratMiddle E` of `X₀ ⊥ E z_N` in coordinates: `𝔰.κ` indexes an orthonormal basis of
`X₀`, and `z_N`, at the index `inr ()`, has the norm `-S.N`. 

### `eq_zero_of_positiveGram_form_eq_zero`

 The form of the space `X₀ ⊥ E z⁺` is anisotropic: only the zero vector has norm `0`. 

 ### The rank of the link and the link isometry 

### `mem_isotropicPerp`

 A vector `y` is orthogonal to `A` and `γ A`, where `A` is the span of `e_1, …, e_ϱ`, if and only
if the coordinates of `y` and of `γ⁻¹ y` at the dual basis vectors `e*_a` vanish. 

### `link_eq_map`

 The link of `γ` is the image of `(A + γ A)^⊥` under the map `linkMatrix γ`, which sends `y` to
the pair of the middle coordinates of `y` and of `γ⁻¹ y`. 

### `mem_link_iff_exists_mem_isotropicPerp`

 A pair lies in the link of `γ` if and only if it consists of the middle coordinates of `y` and
of `γ⁻¹ y` for some `y` in `(A + γ A)^⊥`. 

### `linkMatrix_mulVec_mem_link`

 The classes in `X₀ ⊥ E z_N` of `y` and `γ⁻¹ y`, for `y` orthogonal to `A` and `γ A`, form a
pair in the link of `γ`. 

### `linkSource_linkMatrix_mulVec`

 The map `linkSource` sends the pair `linkMatrix γ *ᵥ y` of middle blocks of `y` and `γ⁻¹ y` to
`y₀ + λ z⁺`, where `y₀` are the coordinates of `y` in `X₀` (indices `𝔰.indexX₀`) and `λ` is the
coordinate of `γ⁻¹ y` at `z_N` (index `𝔰.z`). 

### `linkTarget_linkMatrix_mulVec`

 The map `linkTarget` sends the pair `linkMatrix γ *ᵥ y` of middle blocks of `y` and `γ⁻¹ y` to
`y₀' + λ' z⁺`, where `y₀'` are the coordinates of `γ⁻¹ y` in `X₀` (indices `𝔰.indexX₀`) and `λ'`
is the coordinate of `y` at `z_N` (index `𝔰.z`). 

### `ratGram_form_of_eStar_eq_zero`

 If `y` and `y'` lie in `A^⊥`, that is, their coordinates at the `e*_a` vanish, then their
product for the form `S.ratGram` of the whole space is the product of their middle coordinates for
the form `S.ratMiddle E` of `A^⊥ / A = X₀ ⊥ E z_N`. 

### `form_linkSource_eq_form_linkTarget`

 For pairs `p`, `q` in the link of `γ`, the product in the positive space `X₀ ⊥ E z⁺` of their
images under `linkSource` equals that of their images under `linkTarget`. 

### `eq_zero_of_linkSource_or_linkTarget_eq_zero`

 A pair `p = (y₀ + λ' z_N, y₀' + λ z_N)` in the link vanishes as soon as one of its images
`linkSource p = y₀ + λ z⁺` and `linkTarget p = y₀' + λ' z⁺` in the positive space `X₀ ⊥ E z⁺`
vanishes. 

### `mem_isotropicSpan_one`

 A vector lies in the span `A` of `e_1, …, e_ϱ` if and only if its coordinates outside the first
block vanish. 

### `isotropicSpan_eq_map`

 The span of `M e_1, …, M e_ϱ` is the image under `M` of the span `A` of `e_1, …, e_ϱ`. 

### `mem_isotropicSpan_coe`

 A vector `y` lies in `γ A` if and only if `γ⁻¹ y` lies in `A`, the span of `e_1, …, e_ϱ`. 

### `mem_commonIsotropic`

 A vector `y` lies in `commonIsotropic γ` if and only if it lies in `isotropicPerp γ` and
`linkMatrix γ *ᵥ y = 0`. 

### `finrank_isotropicSpan_coe`

 The space `γ A`, spanned by `γ e_1, …, γ e_ϱ`, has rank `ϱ`. 

### `colSpan_isotropicFramePair`

 The columns `e_1, …, e_ϱ, γ e_1, …, γ e_ϱ` of `isotropicFramePair γ` span `A + γ A`, where `A`
is the span of `e_1, …, e_ϱ`. 

### `rank_isotropicFramePair_add_finrank_commonIsotropic`

 Let `A` be the span of `e_1, …, e_ϱ`. The rank of `A + γ A`, the column space of
`isotropicFramePair γ`, and the rank of `commonIsotropic γ = A ∩ γ A` add up to `2 ϱ`. 

### `rank_add_finrank_isotropicPerp`

 Let `A = ⟨e_1, …, e_ϱ⟩`. The rank of `A + γ A`, which is the column space of
`isotropicFramePair γ`, plus the rank of its orthogonal complement `isotropicPerp γ` equals the rank
`𝔰.r` of the whole space. 

### `finrank_link_add_finrank_commonIsotropic`

 The rank of `link γ` plus the rank of `commonIsotropic γ` (the space `I_γ = A ∩ γ A`, with
`A = ⟨e_1, …, e_ϱ⟩`) equals the rank of `isotropicPerp γ = (A + γ A)^⊥`. So the link has the rank of
`(A + γ A)^⊥ / I_γ`. 

### `finrank_link`

 The link `link γ` consists of the pairs of middle blocks of `y` and `γ⁻¹ y`, for `y` orthogonal
to `A = ⟨e_1, …, e_ϱ⟩` and to `γ A`. It has rank `𝔰.k + 1`, where `𝔰.k` is the rank of `X₀`. 

### `bijective_domRestrict_link`

 A linear map from pairs of middle coordinate vectors to middle coordinate vectors that is
injective on the link of `γ` is a bijection from the link onto the middle coordinate vectors. 

### `linkSourceEquiv`

 The bijection `(y₀ + λ' z_N, y₀' + λ z_N) ↦ y₀ + λ z⁺` from the link onto `X₀ ⊥ E z⁺`. 

### `linkTargetEquiv`

 The bijection `(y₀ + λ' z_N, y₀' + λ z_N) ↦ y₀' + λ' z⁺` from the link onto `X₀ ⊥ E z⁺`. 

### `linkIsometry`

 The link isometry `Υ_γ` of `X₀ ⊥ E z⁺`: for a pair `(y₀ + λ' z_N, y₀' + λ z_N)` in the link of
`γ`, it sends `y₀ + λ z⁺` to `y₀' + λ' z⁺`. Here `z_N` has the norm `-N` and `z⁺` the norm `N`,
for the prime `N = S.N` of the filling `S`. 

### `linkIsometry_linkSource`

 For `p = (y₀ + λ' z_N, y₀' + λ z_N)` in the link of `γ`, the isometry `Υ_γ` sends
`linkSource p = y₀ + λ z⁺` to `linkTarget p = y₀' + λ' z⁺`. 

### `exists_mem_link_linkSource_eq`

 The map `linkSource` sends the link of `γ` onto `X₀ ⊥ E z⁺`. 

### `dotProduct_positiveGram_mulVec_linkIsometry`

 The map `Υ_γ = linkIsometry γ` preserves the form of the positive space `X₀ ⊥ E z⁺`, whose Gram
matrix is `S.positiveGram`. 

### `perpToPositive`

 The map `y ↦ y₀ + λ z⁺` on `(A + γ A)^⊥`, where `y₀` is the `X₀`-part of `y` and `λ` is the
`z_N`-coordinate of `γ⁻¹ y`. 

### `commonIsotropic_le_isotropicPerp`

 Let `A` be the span of `e_1, …, e_ϱ`. The space `commonIsotropic γ = A ∩ γ A` lies in
`isotropicPerp γ = (A + γ A)^⊥`. 

### `ker_perpToPositive`

 Let `A` be the span of `e_1, …, e_ϱ`, and let `γ` lie in the unitary group `S.G E`. The map
`perpToPositive γ` sends `y` in `isotropicPerp γ = (A + γ A)^⊥` to `y₀ + λ z⁺` in the positive space
`X₀ ⊥ E z⁺`. Here `z⁺` is a vector of norm `S.N`, `y₀` is the `X₀`-part of `y`, and `λ` is the
`z_N`-coordinate of `γ⁻¹ y`. The kernel of `perpToPositive γ` is `commonIsotropic γ = A ∩ γ A`,
viewed inside `isotropicPerp γ`. 

### `perpToPositive_surjective`

 The map `perpToPositive γ`, `y ↦ y₀ + λ z⁺`, sends `isotropicPerp γ = (A + γ A)^⊥` onto
`X₀ ⊥ E z⁺`, where `A` is the span of `e_1, …, e_ϱ`. 

### `ker_perpToPositive_and_surjective`

 The space `commonIsotropic γ = A ∩ γ A`, for `A` the span of `e_1, …, e_ϱ`, lies in
`isotropicPerp γ = (A + γ A)^⊥`. The map `perpToPositive γ`, `y ↦ y₀ + λ z⁺`, sends `y` to its
`X₀`-part `y₀` plus `λ z⁺`, where `λ` is the `z_N`-coordinate of `γ⁻¹ y`. It has kernel `A ∩ γ A`
and is surjective, so it induces a bijection from `(A + γ A)^⊥ / (A ∩ γ A)` onto `X₀ ⊥ E z⁺`. 

### `mem_link_iff_linkIsometry`

 The link of `γ` is the graph of `Υ_γ`: a pair `p` lies in it if and only if `Υ_γ` sends
`linkSource p` to `linkTarget p`. 

### `linkIsometry_eq_iff`

 Two elements of `S.G E` have the same link isometry if and only if they have the same link. 

### `linkIsometry_inv_mul_mul_of_mem_besselU`

 The link isometry is the same for `u⁻¹ γ u'` as for `γ`, when `u` and `u'` lie in the Bessel
unipotent group `besselU`, because the two links are equal. 

### `dotProduct_linkForm_mulVec_eq_sub`

 The product of two pairs `p`, `q` for the form `S.linkForm = T ⊕ -T`, where `T` is the form of
`X₀ ⊥ E z_N`, is the difference of the products, in the positive space `X₀ ⊥ E z⁺` with Gram matrix
`S.positiveGram`, of their images under `linkSource` and of their images under `linkTarget`. 

### `_root_.New.mem_link_iff_orthogonal`

 The link of `γ` consists of the pairs of middle blocks of `y` and `γ⁻¹ y`, for `y` orthogonal to
`A = ⟨e_1, …, e_ϱ⟩` and to `γ A`. It is its own orthogonal complement for the form `S.linkForm` on
pairs of middle vectors, which is `S.ratMiddle E` on the first member minus `S.ratMiddle E` on the
second. 

 ### The link on the second frame, and the vanishing of `termDisc` 

### `linkIsometry_frameImage_mulVec`

 Let `S` be a filling over the CM field `E`, with the prime `N = S.N`, and let `γ` lie in
`S.G E`. The columns of `frameImage γ` are the images under `γ` of the frame
`f = (e_1, …, e_ϱ, z_N)`. Let their combination `y = γ f · c` have the products `(0, …, 0, c')` with
`f`. Let `y₀` be the `X₀`-part of `y` and `c_z = c 𝔰.top` the last coefficient. Then
`linkIsometry γ`, the isometry of `X₀ ⊥ E z⁺` read off from the link of `γ`, where `z⁺` has the norm
`N`, sends `y₀ + c_z z⁺` to `-(c' / N) z⁺`. 

### `mul_dotProduct_comp_indexX₀_eq_sub`

 Let `S` be a filling over the CM field `E`, with the prime `N = S.N`, and let `γ ∈ S.G E`. Let
`y = frameImage γ *ᵥ c` be a combination of the image `γ f` of the frame `f = (e_1, …, e_ϱ, z)`
whose products with `f`, the vector `S.frameProducts γ *ᵥ c`, are `(0, …, 0, c')`. Let
`y₀ = y ∘ 𝔰.indexX₀` be the part of `y` in the definite summand `X₀`, and `c_z = c 𝔰.top` the
coefficient at `z`. Then `N ⟨y₀, y₀⟩ = c' c̄' - N² c_z c̄_z`. 

### `exists_frameImage_eq_iff`

 Let `f = (e_1, …, e_ϱ, z)` be the frame and let `y = γ f · c` have the products
`S.frameProducts γ *ᵥ c = (0, …, 0, c')` with `f`. Then `y` is a combination of `f` if and only if
its `X₀`-part vanishes. 

### `exists_frameImage_eq_of_frameProducts_mulVec_eq_zero`

 Let `f = (e_1, …, e_ϱ, z)` be the frame. If `y = frameImage γ *ᵥ c` is orthogonal to the whole
frame `f`, that is `S.frameProducts γ *ᵥ c = 0`, then `y` equals `frameImage 1 *ᵥ x` for some `x`,
so it is a combination of `f`. 

### `termDisc_eq_zero_iff_exists`

 Let `S` be a filling over the CM field `E`, with the prime `N = S.N`. Let `f = frameImage 1` be
the frame `(e_1, …, e_ϱ, z)`, and let `frameImage γ` be its image `γ f`. Let `δ` be the determinant
of the matrix of products of `f` with `γ f`, and `δ'` its leading minor of size `ϱ`. Then
`S.termDisc γ = |δ|² - N² |δ'|²` vanishes if and only if there are coefficient vectors `x` and
`y ≠ 0` with `frameImage 1 *ᵥ x = frameImage γ *ᵥ y`. 

### `frameImage_mulVec_eq_zero_iff`

 The vectors `γ e_1, …, γ e_ϱ, γ z`, the columns of `frameImage γ`, are linearly independent. 

### `termDisc_eq_zero_iff`

 The quantity `S.termDisc γ`, formed from the last two leading minors of the matrix of products
of the frame `f = (e_1, …, e_ϱ, z)` with `γ f`, vanishes if and only if the spans of `f` and of
`γ f` have a nonzero intersection. 
