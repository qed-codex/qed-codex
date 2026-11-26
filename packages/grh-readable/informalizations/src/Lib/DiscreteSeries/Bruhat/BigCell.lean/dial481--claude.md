---
{
  "module": "src/Lib/DiscreteSeries/Bruhat/BigCell.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Bruhat/BigCell.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Bruhat/BigCell.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The big cell: Bruhat decomposition of terms with non-zero leading minors, and its freeness

The big cell of the Bruhat decomposition for the unipotent group `𝖴` = `New.Shape.Form.besselU`
(isometries that are block upper unitriangular in the basis below), over a ring with involution. The
existence of the decomposition is proved assuming an element `τ` with `τ + star τ = 1` (`TraceOne`).

* `New.Filling.exists_big_cell_decomp`: over a field with such a `τ`, if the leading minors
  `δ_1, …, δ_{n-1}` of `Z(γ)` are nonzero, then `γ ∈ 𝖴 w_p σ 𝖴` with `σ` fixing the hyperbolic
  pairs. Here `n = ϱ + 1`.
* `New.Filling.big_cell_factors_unique`: the element `u⁻¹ w_p σ u'` determines `p a` for `a < ϱ`,
  `σ`, `u` and `u'`. `New.Filling.big_cell_unique` is the case of one fixed `σ`.
* `New.Filling.exists_integral_big_cell_decomp`, `New.Filling.big_cell_factors_mem_intGL`: for a
  form that is unimodular over a subring `R` closed under `star` (`IsStarStable R`), the factors of
  an element of `GL(R)` whose leading minors are units of `R` lie in `GL(R)`.

`Z(γ)` = `New.Shape.Form.frameGram T γ` is the matrix of products of the frame
`(e_0, …, e_{ϱ-1}, z)` with its image, indexed by `Fin n`; its last index `𝔰.top` is the one of `z`.
`New.Floors.FloorGroups.weylElem j p` (`w_p`) sends `e_a` to `p a • e*_a` and `e*_a` to
`(star (p a))⁻¹ • e_a` on the first `j` hyperbolic pairs, and `New.Shape.Form.floorGroup j` is the
group of isometries that fix these pairs. The floor `j` is the `j`-th hyperbolic pair `(e_j, e*_j)`.

Notions from other files:
* `New.Shape.BesselIndex`: The index set of the basis: `inl a` for e_a, `inr (inl _)` for the middle
  vectors, among them z, and `inr (inr a)` for e*_a.
* `New.Shape.Form.splitGram`: The Gram matrix of ϱ hyperbolic planes and a middle space with Gram
  matrix T: identity blocks pair the first and last ϱ indices, T is the middle block, all else is
  zero.

## Relation to the literature

This is a case of the known Bruhat decomposition of a unitary group on its big cell. See
`Lib.DiscreteSeries.Bruhat.ComplexPlace`.


### `coe_weylElem_mul`

 Let `σ` fix all hyperbolic pairs (`σ ∈ floorGroup ϱ`), and let `w_p` send `e_a` to `p a • e*_a`
and `e*_a` to `(star (p a))⁻¹ • e_a`. In the blocks `(e, (middle, e*))` the matrix of `w_p σ`
consists of the diagonal matrices of `w_p` in the places `(e, e*)` and `(e*, e)` and of the middle
block of `σ`. 

### `frameGram_weylElem_mul`

 Let `w_p` be the Weyl element sending `e_a ↦ p a · e*_a` and `e*_a ↦ e_a / star (p a)` for
`a < ϱ` and fixing the other basis vectors, and let `σ` fix all hyperbolic pairs. Then `Z(w_p σ)`,
the matrix of products of the frame `(e_0, …, e_{ϱ-1}, z)` with its image under `w_p σ`, is
diagonal. Its diagonal entries are `p 0, …, p (ϱ - 1)` followed by the entry of `Z(σ)` at
`(z, z)`. 

### `leadingMinor_weylElem_mul`

 Let `w_p` (`weylElem ϱ p`) be the Weyl element sending e_a ↦ p_a e*_a and e*_a ↦ e_a/p̄_a for
a < ϱ and fixing the other basis vectors. If `σ ∈ floorGroup ϱ` (it fixes all hyperbolic pairs) and
`l < ϱ`, then the leading minor `δ_{l+1}` of `Z(w_p σ)` is the product `p 0 ⋯ p l`. Here `Z(w_p σ)`
is the matrix of products of the frame with its image, and `δ_{l+1}` is the determinant of its upper
left block of order l + 1. 

### `leadingMinor_weylElem_mul_of_last_entry`

 Let `Z(γ)` (`frameGram`) be the (ϱ+1)×(ϱ+1) matrix of the products h(f_j, γ f_l) of the frame
f = (e_0, …, e_{ϱ-1}, z) with its image under γ. Let `w_p` (`weylElem ϱ p`) be the Weyl element
sending e_a ↦ p_a e*_a and e*_a ↦ e_a/p̄_a for a < ϱ and fixing the other basis vectors. If
`σ ∈ floorGroup ϱ` (it fixes all hyperbolic pairs) and the entry of `Z(σ)` at `(z, z)` is `p ϱ`,
then for every `l : Fin (n + 1)`, i.e. 0 ≤ l ≤ ϱ + 1, the leading minor of order `l` of `Z(w_p σ)`
is `p 0 ⋯ p (l - 1)`. 

### `weylElem_congr`

 The Weyl element `w_p` on all `ϱ` hyperbolic pairs depends only on the scalars `p a` for
`a < ϱ`. 

### `mem_intGL_of_isIntMatrix`

 If the Gram matrix of the form is unimodular over the subring `R` (hermitian and in `GL(R)`),
then an isometry whose matrix has its entries in `R` lies in `GL(R)`. 

### `heisenbergElem_mem_intGL`

 Let the form `h` be unimodular over `R`, let `τ + star τ = 1` and let `j < ϱ`. The pair
`v = (v₁, β)` of a vector of floors above `j` (the basis vectors outside the first `j + 1`
hyperbolic pairs) and a skew scalar gives the Heisenberg element `ν(v)` of floor `j`, the isometry
with `e*_j ↦ e*_j + v₁ + (β - τ h(v₁, v₁)) e_j`. If this maps `e*_j` to a vector with entries in
`R`, then it lies in `GL(R)`. 

### `weylOn_mem_intGL`

 Let the form be unimodular over `R`. If `x a` and its inverse lie in `R` for every `a` with
`P a` (`Ring.inverse` is `0` at non-units), then `weylOn P x` lies in `GL(R)`: this is the isometry
that sends `e_a` to `x a • e*_a` and `e*_a` to `(star (x a))⁻¹ • e_a` on those floors `a` where
`P a` holds and `x a` is a unit and fixes all other basis vectors. 

### `exists_pivot_mul_eq_one`

 Let the form be integral over `R`, let `σ` fix the first `j` hyperbolic pairs and let `w_p`
exchange `e_a` and `e*_a` on them up to the scalars `p a`. Let `w_p σ` be integral, and let the
leading minor `δ_{j+1}` of `Z(w_p σ)`, the matrix of products of the frame
`(e_0, …, e_{ϱ-1}, z)` with its image, have an inverse in `R`. Then the pivot `⟨e_j, σ e_j⟩`,
which is the entry of `σ` at `(e*_j, e_j)`, has an inverse in `R` too. 

### `exists_eq_mul_floorWeyl_mul_of_mem_intGL`

 One step of the normal form. Let the form be unimodular over `R`, let `σ` lie in `GL(R)` and
fix the first `j` hyperbolic pairs, and let its pivot `x`, the entry at `(e*_j, e_j)`, be a unit
of `R`. Then `σ = a w_j(x) σ' b⁻¹`, where `w_j(x) = floorWeyl j x` exchanges `e_j` and `e*_j` up to
the scalar `x`, `σ'` fixes one pair more, `a` and `b` are in the unipotent group `𝖴`, `a` fixes
the first `j` pairs, and `a`, `b`, `σ'` lie in `GL(R)`. 

### `exists_integral_big_cell_decomp`

 The normal form on the big cell, with integrality. Let the form be unimodular over `R`, let
`γ` lie in `GL(R)`, and let the leading minors `δ_1, …, δ_{n-1}` of `Z(γ)`, the matrix of
products of the frame with its image, have inverses in `R` (here `n = ϱ + 1`). Then for every
`j ≤ ϱ` we have `γ = u⁻¹ w_p σ u'`, where `u` and `u'` are in the unipotent group `𝖴`, `w_p`
exchanges `e_a` and `e*_a` up to the scalars `p a` for `a < j` and `σ` fixes these pairs; `u`,
`u'` and `σ` lie in `GL(R)` and the first `j` entries of `p` are units of `R`. 

### `exists_big_cell_decomp`

 The normal form on the big cell over a field with an element `τ` such that `τ + star τ = 1`: if
the leading minors `δ_1, …, δ_{n-1}` of the matrix `Z(γ)` of products of the frame with its image
are nonzero (the index also allows `δ_0 = 1`), then `γ = u⁻¹ w_p σ u'`. Here `u`, `u'` are in the
unipotent group `𝖴`, `σ` fixes all hyperbolic pairs, and `w_p = weylElem ϱ p`, for units `p a`,
sends e_a ↦ p_a e*_a and e*_a ↦ e_a/p̄_a for a < ϱ and fixes the other basis vectors. 

### `big_cell_column_eq`

 Let `y`, `y'` be in the unipotent group `𝖴`, let `σ`, `τ` fix all hyperbolic pairs, and let
`w_p σ y' = y w_q τ`, where `w_p` sends `e_a` to `p a • e*_a`. Comparing the columns at `e_b` of
both sides gives that `y` fixes `e*_b` and that `p b = q b`, for `b < ϱ`. 

### `big_cell_factors_unique`

 The factors of the normal form on the big cell are unique: if `u⁻¹ w_p σ u' = v⁻¹ w_q τ v'` with
`u`, `u'`, `v`, `v'` in the unipotent group `𝖴` and `σ`, `τ` fixing all hyperbolic pairs (`w_p`
exchanges `e_a` and `e*_a` up to the scalars `p a`), then `p` and `q` agree below `ϱ`, `σ = τ`,
`u = v` and `u' = v'`. 

### `big_cell_unique`

 If `σ` fixes all hyperbolic pairs and `v₁ w_p σ v₂⁻¹ = w₁ w_q σ w₂⁻¹` with `v = (v₁, v₂)`,
`w = (w₁, w₂)` in `𝖴 × 𝖴`, then `v = w` and `p`, `q` agree below `ϱ`. So `(v, w_p)` can be
recovered from the element `v₁ w_p σ v₂⁻¹`. Here `𝖴` = `besselU` is the unipotent group and
`w_p` exchanges `e_a` and `e*_a` up to the scalars `p a`. 

### `big_cell_factors_mem_intGL`

 Let `T.splitGram` be unimodular over `R`, and let `w_p = weylElem ϱ p` send e_a ↦ p_a e*_a and
e*_a ↦ e_a/p̄_a for a < ϱ, fixing the other basis vectors. If `u⁻¹ w_p σ u'` lies in `GL(R)`, where
`u`, `u'` are in the unipotent group `𝖴` and `σ` fixes all hyperbolic pairs, and the inverses of
`p a`, `a < ϱ`, lie in `R`, then `u`, `σ` and `u'` lie in `GL(R)`. 
