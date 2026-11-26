---
{
  "module": "src/Lib/General/LinearAlgebra/GramDeterminant.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/LinearAlgebra/GramDeterminant.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/LinearAlgebra/GramDeterminant.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Gram determinants

* `New.exists_extend_basis_of_span_eq_top`: an independent family is completed to a basis by members
  of a spanning set.
* `New.det_gram_comp`: `det ⟨u x_i, u x_k⟩ = (normDet u)² det ⟨x_i, x_k⟩` for a family `x` of as
  many vectors as the dimension of the source of `u`; here `(normDet u)² = det (u* u)`.
* `New.norm_det_mul_det_gram_mul_det_le_one`: a bound on a Gram determinant times `conj (det u')`
  and `det u` in a nonarchimedean field when the inner products of the families transformed by `u'`
  and `u` have norm at most `1`.
* `New.formGram`, `New.norm_det_formGram_le`, `New.norm_det_pairing_sq_le`: Gram matrices for a
  form given by a matrix; a consequence of Hadamard's inequality and the Cauchy–Schwarz inequality
  for determinants, for a positive semidefinite form.

Notions from other files:

* `Matrix.gram ℂ x`: the matrix of the inner products `⟨x_i, x_k⟩`.


### `exists_extend_basis_of_span_eq_top`

 A linearly independent family `y` in a finite-dimensional space is completed to a basis by
finitely many members `z` of a given spanning set `S`. 

### `det_gram_comp`

 For a linear map `u` and a family `x` of `dim W` vectors of `W`, the Gram determinant of
`u ∘ x` is that of `x` times `(normDet u) ^ 2`, where `normDet u` is the square root of
`det (u* u)`. 

### `norm_det_mul_det_gram_mul_det_le_one`

 Let `φ` be a family of vectors, `u'` and `u` square matrices, and `ι` a ring homomorphism from
`ℂ` to a nonarchimedean normed field. If the inner products of the transformed families
`∑ c, u' a c • φ c` and `∑ c, u b c • φ c` all have norm at most `1` under `ι`, then so does
`conj (det u') · det ⟨φ_i, φ_k⟩ · det u`, the determinant of these products. 

### `formGram`

 The matrix of the products `star (v i) ⬝ᵥ G *ᵥ v k` of a family `v` for the form `G`. 

### `posSemidef_formGram`

 The matrix `formGram G v` of a positive semidefinite form is positive semidefinite. 

### `norm_det_formGram_le`

 For a positive semidefinite form `G`, if each diagonal product `star (v i) ⬝ᵥ G *ᵥ v i` of a
family `v` of `n` vectors is at most `exp h`, then `‖det (formGram G v)‖ ≤ exp (n * h)`
(Hadamard's inequality). 

### `norm_det_pairing_sq_le`

 The Cauchy–Schwarz inequality in the exterior power, where the product of `v₁ ∧ ⋯ ∧ vₙ` and
`w₁ ∧ ⋯ ∧ wₙ` is `det (v_i* G w_k)`: for `G` positive semidefinite,
`|det (v_i* G w_k)|² ≤ det (v_i* G v_k) det (w_i* G w_k)`. 
