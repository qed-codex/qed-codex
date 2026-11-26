---
{
  "module": "src/New/Spanning/Unfolding/TermStructure.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/TermStructure.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/TermStructure.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The structure of a term

An element `γ` gives two frames, with the spans `A⁺` and `γ A⁺`, and two isotropic spaces `A` and
`γ A` with the intersection `I_γ`. This file describes `A⁺_γ = A⁺ + γ A⁺`, its radical and its
orthogonal complement, which modulo `I_γ` is isometric to `X₀^γ = X₀ ∩ Υ_γ⁻¹ X₀` by the map
`framePerpToX₀`. For an element that agrees and has `gr(γ) = 0` it proves that `A = A_{≤j} ⊕ I_γ`
and `γ A = γ A_{≤j} ⊕ I_γ` for `j = n - 1 - rk I_γ`, and that `j` is the cell rank of `γ`. It also
shows that `I_{u γ u'} = u I_γ` for `u`, `u'` in the unipotent group `U₀`, and that agreement
depends only on the double coset `U₀ γ U₀`. Finally it defines the set `Γ*` (`remainingTerms`) of
the terms that are left for the estimate of the second moment.

Here `n = ϱ + 1`, the frame is `e_1, …, e_{n-1}, z_N` (indexed from `0` in the code), `A` is spanned
by `e_1, …, e_{n-1}`, `A⁺ = A + E z_N`, and `A_{≤j}` is spanned by the first `j` vectors of the
frame. The space has rank `r` and `A^⊥ / A = X₀ ⊥ E z_N` with `X₀` of rank `k`. For `y` orthogonal
to `A` and `γ A` the classes of `y` and `γ⁻¹ y` are `y₀ + λ' z_N` and `y₀' + λ z_N`. A pair
`(μ, μ')` occurs at an index `a` if the two frames share a vector with coefficients `μ`, `μ'` at `a`
and `0` above `a`. In names, `_one` and `_coe` after a word for a span, as in `isotropicSpan_one`
and `flagSpan_coe`, refer to the frames `e_•` and `γ e_•`. The hypothesis `HasPrimitiveRoot5040 E`
says that `E` contains a primitive root of unity of order `5040`.

Notions from other files:
* `linkIsometry γ` is the link isometry `Υ_γ` of `X₀ ⊥ E z⁺` with `y₀ + λ z⁺ ↦ y₀' + λ' z⁺`.
* `termDisc γ` is `gr(γ) = |δ_n|² - N² |δ_{n-1}|²` for the leading minors `δ_j` of the matrix
  `frameProducts γ` of products of the two frames.
* `CharsAgree γ` (`γ` agrees) says that the character `unipotentChar` takes the same value at
  rational `u`, `u'` in `U₀` whenever `u γ = γ u'`.
* `HasCellRank j γ` says that one pair `(ζ, 1)` with `ζ ζ̄ = 1` occurs at all indices `a ≥ j`
  (`NormOnePairOccursFrom j γ`), that `δ_j ≠ 0`, and that `j = n` exactly when `gr(γ) ≠ 0`.

## Relation to the literature

See `New.Spanning.Unfolding.Climbing` for related work.


### `mem_colSpan_submatrix`

 For an injection `e`, a vector `v` is a combination of the columns of `P` with indices in the
range of `e` if and only if it is a combination of all columns of `P` whose coefficients vanish
outside that range. 

 ### The sum of the two frames and its orthogonal complement 

### `frameSum`

 The space `A⁺_γ = A⁺ + γ A⁺`, where `A⁺` is the span of the frame `e_1, …, e_ϱ, z_N`. 

### `framePerp`

 The space `(A⁺_γ)^⊥` of the vectors orthogonal to both frames for the form `S.ratGram`. 

### `inclPositive`

 The inclusion of `X₀` in `X₀ ⊥ E z⁺`. 

### `linkedX₀`

 The space `X₀^γ = X₀ ∩ Υ_γ⁻¹ X₀` of the vectors of `X₀` that the link maps into `X₀`. 

### `framePerpToX₀`

 The map `y ↦ y₀` from `(A⁺_γ)^⊥` to `X₀`. 

### `mem_range_inclPositive`

 A vector of `X₀ ⊥ E z⁺` lies in `X₀` if and only if its coefficient at `z⁺` vanishes. 

### `mem_linkedX₀`

 A vector `v` of `X₀` lies in `X₀^γ` if and only if its image `Υ_γ v` under the link isometry has
the coefficient `0` at `z⁺`. 

### `colSpan_framePair`

 The columns of `framePair γ`, namely the frame `e_1, …, e_ϱ, z_N` and its image under `γ`, span
`A⁺_γ = A⁺ + γ A⁺` (`frameSum γ`). 

### `mem_framePerp_iff_orthogonal`

 A vector `y` lies in `framePerp γ` if and only if its product, for the form `S.ratGram`, with
each vector of `frameSum γ = A⁺ + γ A⁺` vanishes. Here `A⁺ = ⟨e_1, …, e_ϱ, z_N⟩`. 

### `form_frameImage_one`

 For the coefficients `x` of a combination of the frame `e_1, …, e_ϱ, z_N`, the product, for the
form `S.ratGram`, of this combination with `y` is the sum of `x̄_a y(e*_a)` over `a ≤ ϱ` minus
`N x̄_z y(z)`, where `x_z` is the last coefficient and `y(·)` are coordinates of `y`. 

### `form_frameImage_coe`

 For the form `S.ratGram`, the product of a combination with coefficients `x` of the frame
`frameImage γ` with `y` equals the product of the same combination of the frame `frameImage 1` with
`γ⁻¹ y`. 

### `orthogonal_frame_iff`

 A vector `y` is orthogonal, for the form `S.ratGram`, to the span `A⁺` of the frame
`e_1, …, e_ϱ, z_N` (the columns of `frameImage 1`) if and only if its coordinates at the dual
vectors `e*_a` and at `z_N` vanish. 

### `mem_framePerp`

 Let `A⁺_γ = A⁺ + γ A⁺`, where `A⁺ = ⟨e_1, …, e_ϱ, z_N⟩`, and take orthogonal complements for the
hermitian form `S.ratGram`. A vector `y` lies in `(A⁺_γ)^⊥` if and only if it is orthogonal to
`A = ⟨e_1, …, e_ϱ⟩` and to `γ A` and both `λ' = 0` and `λ = 0`. 

### `linkIsometry_comp_indexX₀`

 For `y` in `(A⁺_γ)^⊥` the link isometry `Υ_γ` sends the `X₀`-part of `y` to the `X₀`-part of
`γ⁻¹ y`. 

### `exists_mem_isotropicPerp_comp_eq`

 Let `Υ_γ` be the link isometry of `X₀ ⊥ E z⁺`, where `z⁺` is a vector of norm `N`: for `y`
orthogonal to `A` and `γ A` it sends `y₀ + λ z⁺` to `y₀' + λ' z⁺`, where `y₀`, `y₀'` are the
`X₀`-parts of `y`, `γ⁻¹ y` and `λ'`, `λ` their coordinates at `z_N`. Then every `v` in `X₀` is the
`X₀`-part of some such `y` with `λ = 0`, and the coefficient of `Υ_γ v` at `z⁺` is `λ'`. 

### `range_framePerpToX₀`

 The image of the map `framePerpToX₀ γ` (`y ↦ y₀`, taking the coordinates in `X₀`) is
`linkedX₀ γ`. The map is defined on `(A⁺_γ)^⊥`, the vectors orthogonal for `S.ratGram` to the frame
`e_1, …, e_ϱ, z_N` and to its image under `γ`. The space `linkedX₀ γ` = `X₀^γ` consists of the
vectors of `X₀` that the link isometry maps into `X₀`. 

### `form_framePerpToX₀`

 The map `y ↦ y₀` from `(A⁺_γ)^⊥` to `X₀` sends the form `S.ratGram` of the whole space to the
standard hermitian product of `X₀`. 

### `commonIsotropic_le_framePerp`

 The space `I_γ = A ∩ γ A` is orthogonal to both frames. 

### `ker_framePerpToX₀`

 For `γ` in the group `S.G E`, the kernel of `framePerpToX₀ γ` is `commonIsotropic γ = A ∩ γ A`,
seen inside `framePerp γ`. 

### `form_self_eq_zero_iff_mem_commonIsotropic`

 A vector `y` of `framePerp γ = (A⁺_γ)^⊥` is isotropic for the form `S.ratGram` if and only if it
lies in `commonIsotropic γ = A ∩ γ A`, where `A = ⟨e_1, …, e_ϱ⟩`. 

### `isotropicSpan_le_colSpan_frameImage`

 The space `M A`, spanned by `M e_1, …, M e_ϱ`, lies in `M A⁺`, the span of the columns of
`frameImage M`, which are the images under `M` of the frame `e_1, …, e_ϱ, z`. 

### `frameSum_inf_framePerp`

 The space `I_γ = A ∩ γ A` is the radical of `A⁺_γ = A⁺ + γ A⁺`, that is, the intersection of
`A⁺_γ` with its orthogonal complement. 

### `mem_ker_zRowBlockDiagonal`

 A vector `p` on two copies of the middle coordinates lies in the kernel of
`zRowBlockDiagonal (S.ratMiddle E)` (two copies of the `z`-row of the Gram matrix) if and only if
both `z`-coordinates of `p` are `0`. 

### `mem_commonLink`

 For `γ`, `γ'` in the rational unitary group `S.G E` and a vector `v` of the definite space `X₀`,
`v` lies in `commonLink γ γ'` if and only if two conditions hold. The first condition is that `v`
lies in `linkedX₀ γ`, the vectors of `X₀` that `linkIsometry γ` maps into `X₀`. The second is that
the isometries `linkIsometry γ` and `linkIsometry γ'` of `X₀ ⊥ E z⁺` agree at `v ⊕ᵥ 0`, the vector
with `X₀`-part `v` and zero `z⁺`-coordinate. 

### `commonLink_self`

 For `γ' = γ` the condition `Υ_γ v = Υ_γ' v` always holds, so `commonLink γ γ` is `X₀^γ`. 

### `commonLink_le_linkedX₀_inf`

 The space `commonLink γ γ'` lies in `X₀^γ ∩ X₀^γ'`. It consists of the `x` in `X₀` that are the
`X₀`-coordinates of the first vector of a pair of middle vectors that are orthogonal to `z` and lie
in the links of both `γ` and `γ'`. 

### `finrank_commonLink`

 The rank of `commonLink γ γ'` equals the rank of the space of pairs that lie in both `link γ`
and `link γ'` and are killed by `zRowBlockDiagonal (S.ratMiddle E)`, that is, whose two vectors are
orthogonal to z. 

### `finrank_linkedX₀_add_finrank_inf_le`

 The space `link γ` consists of the pairs of classes of `y` and `γ⁻¹ y` in `A^⊥ / A = X₀ ⊥ E z_N`
for `y` orthogonal to `A = ⟨e_1, …, e_ϱ⟩` and `γ A`. The space `X₀^γ = linkedX₀ γ` consists of the
vectors of `X₀` that `Υ_γ` maps into `X₀`, and `commonLink γ γ'` of the vectors of `X₀^γ` on which
`Υ_γ` and `Υ_γ'` coincide. Then `rk X₀^γ + rk (link γ ∩ link γ') ≤ rk (commonLink γ γ') + (k + 1)`:
the corank of `commonLink γ γ'` in `X₀^γ` is at most the corank of `link γ ∩ link γ'` in
`link γ`. 

### `inv_mulVec_z_eq_of_pairOccursAt`

 Let the pair `(ζ, 1)` occur at the last index `𝔰.top`: a combination of the frame
`e_1, …, e_ϱ, z_N` with coefficient `ζ` at `z_N` equals a combination of its image under `γ` with
coefficient `1` at `γ z_N`. Then `λ = ζ̄ λ'` for every `y` orthogonal to `A = ⟨e_1, …, e_ϱ⟩` and to
`γ A`. 

### `HasCellRank.le_of_termDisc_eq_zero`

 If `γ` has cell rank `j` (`S.HasCellRank j γ`), which includes that `j = ϱ + 1` exactly when
`gr(γ) = S.termDisc γ ≠ 0`, and `S.termDisc γ = 0`, then `j ≤ ϱ`. 

### `HasCellRank.linkedX₀_eq_top`

 If `γ` has cell rank `j` and `S.termDisc γ = 0`, then the link isometry `Υ_γ` maps `X₀` into
itself: `linkedX₀ γ` is all of `X₀`. 

### `CharsAgree.linkedX₀_eq_top`

 Let `E` contain a primitive root of unity of order `5040`. If `γ` agrees and
`gr(γ) = S.termDisc γ` vanishes, then the link of `γ` maps all of `X₀` into `X₀`, that is,
`X₀^γ = X₀`. 

### `disjoint_colSpan_frameImage`

 If `gr(γ) = S.termDisc γ` is not zero, then the span `A⁺` of the frame `e_1, …, e_ϱ, z_N` and
the span `γ A⁺` of its image have the intersection `0`. 

### `commonIsotropic_eq_bot`

 If `gr(γ) = S.termDisc γ` is not zero, then `I_γ = A ∩ γ A` is zero, where
`A = ⟨e_1, …, e_ϱ⟩`. 

### `finrank_colSpan_frameImage`

 The span `γ A⁺` of the image under `γ` of the frame `e_1, …, e_ϱ, z_N` has the rank
`n = ϱ + 1`. 

### `finrank_frameSum_add_finrank_framePerp`

 The ranks of `frameSum γ` = `A⁺_γ = A⁺ + γ A⁺` (the span of the frame and of its image under
`γ`) and of its orthogonal complement `framePerp γ` add up to `𝔰.r`, the rank of the whole space. 

### `finrank_linkedX₀_add_finrank_commonIsotropic`

 The space `X₀^γ` of the vectors of `X₀` that the link of `γ` maps into `X₀` has the rank of
`(A⁺_γ)^⊥ / I_γ`, where `A⁺_γ = A⁺ + γ A⁺` and `I_γ = A ∩ γ A`. 

### `finrank_frameSum_of_termDisc_ne_zero`

 If `gr(γ) = S.termDisc γ` is not zero, then `A⁺_γ = A⁺ + γ A⁺`, the span of the frame and of its
image under `γ`, has the rank `𝔰.n + 𝔰.n`. 

### `finrank_linkedX₀_add_one`

 If `gr(γ) = S.termDisc γ` is not zero, then the space `X₀^γ` of the vectors of
`X₀ = 𝔰.κ → E` that the link `linkIsometry γ` (an isometry of `X₀ ⊥ E z⁺`) maps into `X₀` is a
hyperplane of `X₀`: its rank is `r - 2 n = k - 1`. 

### `HasCellRank.finrank_linkedX₀_add_sub`

 If `γ` has the cell rank `j`, then `finrank E (linkedX₀ γ) + (j - ϱ) = 𝔰.k`, the dimension of
`X₀`. So `X₀^γ` has corank `1` in `X₀` for `j = ϱ + 1` and corank `0` otherwise. 

 ### The flags of the two frames and the cell rank 

### `flagSpan`

 The space `M A_{≤j}` spanned by the images under `M` of the first `j` vectors of the frame
`e_1, …, e_ϱ, z_N`. 

### `mem_flagSpan`

 The vectors of `M A_{≤j}`, the span of the first `j` vectors of the frame `M e_•`, are the
combinations of that frame whose coefficients vanish from the index `j` on. 

### `mem_isotropicSpan`

 The vectors of `M A = ⟨M e_1, …, M e_ϱ⟩` are the combinations of the frame
`M e_1, …, M e_ϱ, M z_N` whose last coefficient vanishes. 

### `finrank_flagSpan_coe`

 The span `flagSpan γ j` of the images under `γ` of the first `j` vectors of the frame
`e_1, …, e_ϱ, z_N` has rank `j`. 

### `frameImage_mulVec_mem_commonIsotropic`

 A vector with the coefficients `x` in the frame `e_1, …, e_ϱ, z_N` and `x'` in its image under
`γ` lies in `I_γ = A ∩ γ A` if one of its coefficients at `z_N` and `γ z_N` vanishes, because the
two coefficients have the same norm. 

### `flagSpan_sup_eq_isotropicSpan`

 Let `I` be a subspace of `M A = ⟨M e_1, …, M e_ϱ⟩` and let `j ≤ ϱ`. Suppose that `I` contains
vectors with any given coefficients in the frame `M e_1, …, M e_ϱ, M z_N` at the indices from `j`
on, the last coefficient being `0`. Then `M A = M A_{≤j} + I`, where `M A_{≤j}` is spanned by the
first `j` vectors of that frame. 

### `_root_.New.NormOnePairOccursFrom.flagSpan_coe_sup_commonIsotropic`

 Let a norm-one pair occur for `γ` from the index `j ≤ ϱ`: for one `ζ` with `ζ ζ̄ = 1`, the frame
`e_1, …, e_ϱ, z_N` and its image under `γ` share a vector with the leading coefficients `ζ` and `1`
at each index from `j` on. Then `γ A = γ A_{≤j} + I_γ`, where `A = ⟨e_1, …, e_ϱ⟩`,
`A_{≤j} = ⟨e_1, …, e_j⟩` and `I_γ = A ∩ γ A`. 

### `_root_.New.NormOnePairOccursFrom.flagSpan_one_sup_commonIsotropic`

 Let a norm-one pair occur for `γ` from the index `j ≤ ϱ`: for one `ζ` with `ζ ζ̄ = 1`, the frame
`e_1, …, e_ϱ, z_N` and its image under `γ` share a vector with the leading coefficients `ζ` and `1`
at each index from `j` on. Then `A = A_{≤j} + I_γ`, where `A = ⟨e_1, …, e_ϱ⟩`,
`A_{≤j} = ⟨e_1, …, e_j⟩` and `I_γ = A ∩ γ A`. 

### `leadingMinor_eq_zero_of_mulVec_eq_zero`

 If a square matrix `Z` kills a nonzero vector `x` whose coefficients vanish from the index `j`
on, then the leading minor of order `j` of `Z` vanishes. 

### `HasCellRank.isLeast_normOnePairOccursFrom`

 Let `δ_i` be the leading minor of order `i` of the matrix `S.frameProducts γ` of the hermitian
products of the frame `e_1, …, e_ϱ, z_N` with its image under `γ`, and let
`gr(γ) = S.termDisc γ = |δ_n|² - N² |δ_{n-1}|²` vanish. Let `γ` have the cell rank `j`: a norm-one
pair occurs from the index `j` on, `δ_j ≠ 0`, and `j = n` exactly when `gr(γ) ≠ 0`. Then `j` is the
least index from which a norm-one pair occurs for `γ`, since a smaller index would give
`δ_j = 0`. 

### `CharsAgree.disjoint_flagSpan_one`

 Let `E` contain a primitive root of unity of order `5040`. Let `S.CharsAgree γ` hold: the
character `unipotentChar` takes the same value at `u` and at `γ⁻¹ u γ` for every rational `u` in
`U₀ ∩ γ U₀ γ⁻¹`. Let `j` be least with `NormOnePairOccursFrom j γ`: for one `ζ` with `ζ ζ̄ = 1`, at
every index from `j` on, the flags of the frame `e_1, …, e_ϱ, z_N` and of its image under `γ` share
a vector with leading coefficients `ζ` and `1`. Then `flagSpan 1 j`, the span of the first `j` frame
vectors, meets `colSpan (frameImage γ)`, the span of the image of the frame under `γ`, only in
`0`. 

### `CharsAgree.disjoint_flagSpan_coe`

 Let `E` contain a primitive root of unity of order `5040`. Let `γ` satisfy `S.CharsAgree γ`: the
character `unipotentChar` takes the same value at `u` and at `γ⁻¹uγ` for every rational `u` in
`U₀ ∩ γU₀γ⁻¹`. Let `j` be least with `NormOnePairOccursFrom j γ`: for one `ζ` with `ζ ζ̄ = 1`, at
every index from `j` on, the flags of the frame `e_1, …, e_ϱ, z_N` and of its image under `γ` share
a vector with leading coefficients `ζ` and `1`. Then `flagSpan γ j`, the span of the images under
`γ` of the first `j` frame vectors, meets the span `colSpan (frameImage 1)` of the frame only in
`0`. 

### `HasCellRank.flagSpan_one_sup_commonIsotropic`

 Let `gr(γ) = S.termDisc γ` vanish and let `γ` have the cell rank `j`. Then `A = A_{≤j} + I_γ`,
where `A = ⟨e_1, …, e_ϱ⟩`, `A_{≤j} = ⟨e_1, …, e_j⟩` and `I_γ = A ∩ γ A`. 

### `HasCellRank.flagSpan_coe_sup_commonIsotropic`

 Let `gr(γ) = S.termDisc γ` vanish and let `γ` have the cell rank `j`. Then
`γ A = γ A_{≤j} + I_γ`, where `A = ⟨e_1, …, e_ϱ⟩`, `A_{≤j} = ⟨e_1, …, e_j⟩` and `I_γ = A ∩ γ A`. 

### `CharsAgree.disjoint_flagSpan_one_commonIsotropic`

 Let `E` contain a primitive root of unity of order `5040`, let `γ` agree, let
`gr(γ) = S.termDisc γ` vanish and let `γ` have the cell rank `j`. Then `A_{≤j} = ⟨e_1, …, e_j⟩`
meets `I_γ = A ∩ γ A` only in `0`. 

### `CharsAgree.disjoint_flagSpan_coe_commonIsotropic`

 Let `E` contain a primitive root of unity of order `5040`, let `γ` agree, let
`gr(γ) = S.termDisc γ` vanish and let `γ` have the cell rank `j`. Then
`γ A_{≤j} = ⟨γ e_1, …, γ e_j⟩` meets `I_γ = A ∩ γ A` only in `0`. 

### `CharsAgree.add_finrank_commonIsotropic_eq`

 Let `E` contain a primitive root of unity of order `5040`. Let `S.CharsAgree γ` hold:
`unipotentChar` takes the same value at `u` and at `γ⁻¹uγ` for every rational `u` in `U₀ ∩ γU₀γ⁻¹`.
Let `S.termDisc γ = |δ_{ϱ+1}|² - N² |δ_ϱ|²` vanish. Let `γ` have the cell rank `j`:
`NormOnePairOccursFrom j γ` holds, `δ_j ≠ 0`, and `j = ϱ + 1` exactly when `S.termDisc γ ≠ 0`. Then
`j + finrank E (commonIsotropic γ) = ϱ`. 

### `CharsAgree.hasCellRank_of_add_finrank_eq`

 Let `E` contain a primitive root of unity of order `5040`, let `γ` agree, let
`gr(γ) = S.termDisc γ` vanish, and let `j + rk I_γ = ϱ` for `I_γ = A ∩ γ A` and `A = ⟨e_1, …, e_ϱ⟩`.
Then `γ` has the cell rank `j`: a norm-one pair occurs for it from the index `j` on, and the leading
minor `δ_j` of the products of the frame with its image is not zero. 

 ### The action of the unipotent group 

### `mulVec_mem_isotropicSpan_one`

 An element `u` of the unipotent group `U₀` maps `A = ⟨e_1, …, e_ϱ⟩` into itself. 

### `mulVec_mem_isotropicSpan_one_iff`

 An element `u` of the unipotent group `U₀` preserves `A = ⟨e_1, …, e_ϱ⟩`: the vector `u y` lies
in `A` if and only if `y` does. 

### `commonIsotropic_besselU_mul`

 For `u`, `u'` in the Bessel unipotent group `besselU` we have `I_{u γ u'} = u I_γ`, where
`I_γ = commonIsotropic γ = A ∩ γ A` and `A = ⟨e_1, …, e_ϱ⟩`. 

### `finrank_commonIsotropic_besselU_mul`

 The rank of `I_γ = A ∩ γ A`, where `A = ⟨e_1, …, e_ϱ⟩`, does not change when `γ` is multiplied
on either side by elements of the unipotent group `U₀`. 

### `unipotentChar_ratToFin_mul`

 The function `ψ_U = S.unipotentChar` on the finite adelic group is multiplicative on the images
under `S.ratToFin` of the rational points of the unipotent group `U₀ = besselU`. 

### `unipotentChar_ratToFin_conj`

 The function `ψ_U = S.unipotentChar` is invariant under conjugation in the rational points of
the unipotent group `U₀`. 

### `charsAgree_mul_mul_iff_of_mem_besselU`

 For `u`, `u'` in `besselU`, the element `u γ u'` agrees if and only if `γ` does. 

 ### The terms that remain 

### `isotropicSpan_eq_iff_finrank`

 For `A = ⟨e_1, …, e_ϱ⟩` we have `A = γ A` if and only if `I_γ = A ∩ γ A` has the rank `ϱ`. 

### `remainingTerms`

 The set `Γ*` of the rational elements `γ` that have `gr(γ) = S.termDisc γ ≠ 0`, or agree and
have `gr(γ) = 0` and `A ≠ γ A`, where `A = ⟨e_1, …, e_ϱ⟩`. 

### `mem_remainingTerms_iff`

 `γ` lies in `Γ*` (`S.remainingTerms`) exactly when `S.termDisc γ ≠ 0`, or `S.CharsAgree γ`,
`S.termDisc γ = 0` and `isotropicSpan 1 ≠ isotropicSpan γ`. 

### `isStable_remainingTerms`

 The set `Γ*` of the remaining terms is stable under the unipotent group on both sides: for `u`,
`u'` in `U₀`, the element `u⁻¹ γ u'` lies in `Γ*` if and only if `γ` does. 

### `_root_.New.NormOnePairOccursFrom.notMem_remainingTerms`

 Let `Γ*` = `S.remainingTerms` be the set of rational `γ` with `S.termDisc γ ≠ 0`, or with
`S.CharsAgree γ`, `S.termDisc γ = 0` and `A ≠ γ A`, where `A = ⟨e_1, …, e_ϱ⟩`. Here
`S.termDisc γ = |δ_{ϱ+1}|² - N²|δ_ϱ|²`, where the `δ_i` are the leading minors of the matrix of
hermitian products of the vectors `e_1, …, e_ϱ, z_N` with their images under `γ`; `z_N` is a vector
of norm `-N`. Suppose `NormOnePairOccursFrom 0 γ` holds: for one `ζ` with `ζ ζ̄ = 1`, the flags
spanned by these vectors and by their images share, at every index, a vector with leading
coefficients `ζ` and `1`. Then `γ ∉ Γ*`. A shared vector gives `S.termDisc γ = 0`, and `A = γ A`,
since both equal `I_γ = A ∩ γ A`. 

### `CharsAgree.normOnePairOccursFrom_zero`

 Let `E` contain a primitive root of unity of order `5040`. If `γ` agrees and is not in the set
`Γ*` of the remaining terms, then a norm-one pair occurs for `γ` from the index `0` on: for one `ζ`
with `ζ ζ̄ = 1`, the frame and its image under `γ` share a vector with the leading coefficients `ζ`
and `1` at every index. 
