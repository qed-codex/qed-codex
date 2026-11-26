---
{
  "module": "src/Lib/General/LinearAlgebra/MatrixNormBounds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/LinearAlgebra/MatrixNormBounds.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/LinearAlgebra/MatrixNormBounds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Auerbach's lemma, ultrametric matrix bounds and Gram norms

This file collects norm estimates for linear maps and matrices.

## Main definitions and results

* `New.exists_auerbach`: linear forms indexed by a compact space that vanish together only at `0`,
  with images in a normed field depending continuously on the index, contain the coordinate forms
  of a basis on whose vectors all forms of the family take values of image norm at most `1`. These
  forms are chosen to maximise the norm of the image of their determinant; Cramer's rule gives the
  bound.
* `New.norm_mulVec_le_of_nonneg`, `New.norm_mulVec_le`: over an ultrametric field, a matrix whose
  entries have norm at most `c ≥ 0` multiplies the sup norm of a vector by at most `c`, whatever its
  size.
* `New.sqrt_weylNormSq_le_of_dual`: a bound on the Gram norm of Weyl modules by duality.
* `New.sqrt_weylNormSq_sum_le`: the triangle inequality for the Gram norm of Weyl modules.

## Relation to the literature

Known result: Auerbach's lemma, here for a compact family of linear forms.


 ## Auerbach's lemma for a compact family of linear forms 

### `New.exists_auerbach`

 Auerbach's lemma. Let `ℓ a` (`a` in a compact topological space `A`) be linear forms on a
finite-dimensional `K`-space `U` whose only common zero is `0`. Let `φ : K →+* L` map to a normed
field, and let `a ↦ φ (ℓ a v)` be continuous for every `v`. Then there are indices `S k` and a
basis `z` such that the coordinates of `z` are the forms `ℓ (S k)` and `‖φ (ℓ a (z k))‖ ≤ 1` for
all `a`, `k`. The result depends on the basis `b` only through its index type `ι`. The topology
`topA` of `A` is implicit: it is found from the continuity hypothesis. 

 ## Sup norm bound for matrix–vector products over ultrametric fields 

### `New.norm_mulVec_le_of_nonneg`

 Over an ultrametric normed field, a matrix whose entries have norm at most `c ≥ 0` multiplies
the sup norm of a vector by at most `c`, whatever the size of the matrix. 

### `New.norm_mulVec_le`

 If all entries of a matrix `M` over an ultrametric normed field have norm at most `c`, then
`‖M.mulVec x‖ ≤ c * ‖x‖` in the sup norm. This is the form of `New.norm_mulVec_le_of_nonneg` for
explicit constants: the hypothesis `0 ≤ c` comes last and is proved by `simp` when omitted. 


## Duality for Gram norms

For an automorphism `σ` of `ℂ`, we bound the values at `σ ∘ v` of the Gram norm
`ξ ↦ √(weylNormSq ξ)`, where `New.weylNormSq ξ` is the real part of `ξ* G ξ` for the integer Gram
matrix `G`. The coordinates are indexed by `New.WeylIndex n κ`: families, one for each `τ : T`, of
basis tableaux with entries indexed by `n` and column multiplicities `κ τ`.


### `sqrt_weylNormSq_le_of_dual`

 Duality for the Gram norm `ξ ↦ √(weylNormSq ξ)` after an automorphism `σ` of `ℂ`, on vectors
indexed by `WeylIndex n κ` (families of basis tableaux): here `weylNormSq ξ` is `Re (ξ* G ξ)` for
the positive definite integer Gram matrix `G = weylGram n κ` of the Weyl-module basis given by these
tableaux (entries in `n`, column multiplicities `κ τ` for each `τ : T`). If `‖σ (c ⬝ᵥ v)‖ ≤ C` for
every vector `c` with `‖σ (c ⬝ᵥ w)‖ ≤ √(weylNormSq (σ ∘ w))` for all `w`, then the Gram norm of
`σ ∘ v` is at most `C`. 

### `sqrt_weylNormSq_sum_le`

 Triangle inequality for the Gram norm `ξ ↦ √(weylNormSq ξ)` on vectors indexed by
`WeylIndex n κ` (families of basis tableaux, entries in `n`, column multiplicities `κ τ`), where
`weylNormSq ξ = Re (ξ* G ξ)` for the positive definite integer Gram matrix `G = weylGram n κ`, after
an automorphism `σ` of `ℂ`: the Gram norm of `σ` applied to a finite sum of vectors is at most the
sum of their Gram norms after `σ`. 
