---
{
  "module": "src/Lib/GLn/Branching/NormBound.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GLn/Branching/NormBound.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GLn/Branching/NormBound.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Branching from GL(n+1) to GL(n) × GL(1): the branching vector and the norm bound

This file treats the branching from `GL(n + 1)` to `GL(n) × GL(1)` for the representations of
`∏ τ, GL (N τ)`. The rows `N τ` are the rows `n τ` together with one new row, given by `ι τ`. A
weight `κ` is given by the numbers `κ τ h` of columns of height `h` at the place `τ`. This file
defines the branching vector and writes products of kernels as the minors of one filling. It
proves the norm bound for an equivariant matrix through the transposed contraction
`New.GL.extendedTensor`.

## Main definitions and results

* `New.GL.branchVector`: the product of the leading minors to the powers `γ`, with the new row
  first, so that every column of positive height contains it, and to the powers `κ`, with the new
  row last, so that no column contains it.
* `New.GL.weylNormSq_mulVec_le_of_equivariant`: the norm bound for an equivariant matrix whose
  transpose sends the extremal vector to a multiple of the branching vector.

Notions from other files:
* `New.MatrixPoly`: Polynomials over `R` in an array of variables `X (a, i)`, with rows `a : m` and
  columns `i : ℕ`.
* `New.rankAt`: The number of elements of the finite row type n_τ at the place τ;
  `New.GL.rowEquivFin n τ : n τ ≃ Fin (rankAt n τ)` is the fixed numbering of these rows, and a
  row's position is its number.
* `New.permArray`: For maps e_τ from rows to natural numbers, the array over R whose entry at row
  (τ,a), column i is 1 if e_τ(a)=i and 0 otherwise.
* `New.toPoly`: The linear map from coordinate vectors ξ to polynomials, ξ ↦ Σ_i (Gξ)_i b_i, with G
  the Gram matrix `New.weylGram` (`New.weylGramOver` is its image over another ring) and b_i the
  basis `New.nablaBasis` of products of minors; `New.GL.nablaCombination` is ξ ↦ Σ_i ξ_i b_i.
* `New.weylEval`: For an array y, the evaluation vector `ev_y` with entries b_i(y); its polynomial
  under `New.toPoly` is `New.weylKernel n κ y`.

## Relation to the literature

Known; see `Lib.GLn.Branching.IntegralMap` for sources.



## The branching vector and integrality of products of minors

A weight `κ` is given by the numbers `κ τ h` of columns of height `h` at the place `τ`.
`New.weylKernel n κ (permArray e)` is the product over `h < rankAt n τ` of the minors on the first
`h` rows in the order `e` and the first `h` columns, to the powers `κ τ h`; `New.rowSubst z f` is
`y ↦ f (z y)`; `New.toPoly n κ` sends a coordinate vector `ξ` to `∑ i, (G ξ) i • b i`, with `G` the
Gram matrix and `b` the basis of minor products.


### `newRowOrder`

 The numbering of the rows `N τ` by `0, …, rankAt N τ - 1` that gives the added row the number
`i τ` and keeps the rows of `n τ` in their fixed order. 

### `branchVector`

 The product over `τ` and `h < rankAt N τ` of the leading `h × h` minors to the power `γ τ h`
with the added row first, and to the power `κ τ h` with it last. 

### `rowSubst_branchVector`

 Multiplying the new row by `s τ` (substituting the matrix `blockScalar ι 1 s`, that is
`diag(1, s τ)` at each `τ`) multiplies `branchVector R ι γ κ'` by the product over `τ` of `s τ` to
the power `diagramWeight (rankAt N) γ (τ, 0)`, the number of columns of `γ` of height
`1, …, rankAt n τ`. 

 ### The product of the two kernels as the minors of one filling 

### `weylKernel_permArray_eq_prod_minor`

 For numberings `e τ` of the rows, the kernel at the array `permArray e` is the product over `τ`
and `h` of the minor on the first `h` rows in the order `e τ`, to the power `κ τ h`. 

### `rowSubst_permMatrix_minor`

 Substituting the permutation matrices of `σ` carries the minor on given rows to the minor on
their images under `σ τ`. 

### `frontPermutation`

 The cyclic permutation of `Fin N` that moves `p` to the front and each position below `p` to the
next one; it is the identity if `N ≤ p`. 

### `frontPermutation_val`

 For `p < N` the permutation sends a position below `p` to the next one and `p` to `0`, and it
fixes the later positions. 

### `finRotate_val`

 The rotation of `Fin N` sends each position other than the last to the next one. 

### `frontRenaming`

 The renaming of the rows `n τ` that moves the row at position `p τ` to the front and each
earlier row to the next position. 

### `extremalRows`

 The rows of column `j` among the columns of height `h`, when the first `k` of these columns hold
the rows at the positions `0, …, h - 1` and the others those at the positions `1, …, h`. 

### `weylKernel_mul_weylKernel_eq_prod_minor`

 Let `κ₀ τ h = κ' τ h + γ τ h` for `0 < h < rankAt n τ`. The product of the kernel of `γ` at the
row order shifted by one and the kernel of `κ'` at the row order `rowEquivFin` is the product, over
the columns of `κ₀`, of the minors on the rows `extremalRows (κ' τ h) h j`. 

### `extremalFilling`

 A filling of the diagram of `κ₀` without its first `p τ` rows, with entries in the last
`rankAt n τ - p τ` rows, numbered from `0`. Among the columns of height `k`, the first
`κ' τ (p τ + k)` hold the rows `0, …, k - 1` and the others the rows `1, …, k`. 

### `leadingWedge_extremalFilling`

 Put the first `p τ` rows on top of `extremalFilling p κ₀ κ'`. In column `j` of height `h` the
entry of index `s` is then the position `s` if `s < p τ` or `j < κ' τ h`, and `s + 1` otherwise. 

### `exists_minor_extremalRows_eq_smul`

 Let a column of height `h` hold the positions `f s = s` if `s < p τ` or `j < k`, and
`f s = s + 1` otherwise, where `j < k` does not occur for `0 < h ≤ p τ`. After the row at position
`p τ` is moved to the front, its minor is that on `extremalRows k h j` up to sign. 

### `exists_smul_rowSubst_extremalFilling`

 Let `p τ` be below the number of rows `rankAt n τ` whenever there are rows, and let `h_rank`
say that the first `p τ` rows and the remaining `rankAt n τ - p τ` make up all the rows. Let `κ'`
have no column of height `h` with `0 < h ≤ p τ`, and let `κ₀ τ h = κ' τ h + γ τ h` for
`0 < h < rankAt n τ`. Put the first `p τ` rows on top of `extremalFilling p κ₀ κ'` and move the row
at position `p τ` to the front. Up to sign, the product of minors becomes the product of the kernel
of `γ` at the row order shifted by one and the kernel of `κ'` at the row order `rowEquivFin`. 

### `exists_smul_weylKernel_mul_eq_toPoly`

 Let `κ'` have no column of height below `q`, and let `κ₀ τ h = κ' τ h + γ τ h` for
`0 < h < rankAt n τ`. Here `weylKernel n κ y` is the polynomial `f(yᵀx)` in `x`, with `f` the
product of leading minors for `κ`, and `toPoly n κ₀ η` is `Σ_i (Gη)_i b_i` for a Weyl vector `η`
(Gram matrix `G`, basis minor products `b_i`). Then some integer `c` with `0 < c` (a hook number)
satisfies two claims. (a) `c ≤ (L ^ L) ^ 3` for every bound `L` of the number of boxes of `κ₀` in
the columns of height `h` with `q ≤ h < rankAt n τ`. (b) `c` times `weylKernel n γ` at the
permutation array of `rowEquivFin` shifted cyclically by one, times `weylKernel n κ'` at that of
`rowEquivFin`, equals `toPoly n κ₀ η` for some `η : WeylIndexFamily n κ₀ → ℤ`. 


## The norm of a branching map

The matrix of a branching map is a multiple of the contraction of tensors followed by the orthogonal
projection to the Weyl module. The contraction takes the coefficient of the new basis vector in the
shortened columns and deletes the terms that contain it in the others. It is used here through its
transpose `New.GL.extendedTensor`, which is isometric on the evaluation vectors after division by
a power of the determinant. The norm bound follows because an orthogonal projection does not
increase norms.


### `leadingMinorAlong`

 The minor of `z` on the first `h` rows and the first `h` columns in the numbering `e`. 

### `branchRows`

 The tableau of `branchVector` at `τ`. Of the columns of height `h`, the first `γ τ h` hold the
first `h` rows in the numbering with the new row first, and the other `κ' τ h` hold the first `h`
rows in the numbering with the new row last. 

### `branchVector_eq_prod_tableauPoly`

 The branching vector is the product of the minors on the columns of `branchRows`. 

### `extendedTensor`

 The transpose of the contraction, applied to the tensor whose factor in a column of height `h`
is the exterior product of the first `h` rows of `a`. The transpose puts the new basis vector in
front of the shortened columns and leaves the others unchanged, so the coordinate at a filling `T`
is the product over the columns of the minor of `diag(a, 1)` with rows from `branchRows` and
columns from `T`. 

### `newRowOrder_symm_of_val_eq_succAbove`

 In the numbering `newRowOrder ι i τ` that gives the new row the number `i τ`, the old row with
number `s` has the number `s` if `s < i τ` and `s + 1` otherwise. 

### `leadingMinorAlong_newRowOrder_zero`

 With the new row first, the leading minor of size `h + 1` of `diag(p, 1)` is the leading minor
of size `h` of `p`. 

### `leadingMinorAlong_newRowOrder_top`

 With the new row last, the leading minors of `diag(p, 1)` of size at most `rankAt n τ` are
those of `p`. 

### `prod_det_blockScalar_branchRows`

 Let `κ₀ τ h = κ' τ h + γ τ (h + 1)` for `0 < h < rankAt n τ`, and let `p τ` be square matrices
over a commutative ring `R`. In the tableau `branchRows ι γ κ' τ`, of the columns of height `h`, the
first `γ τ h` hold the first `h` rows with the new row first, and the other `κ' τ h` hold the first
`h` rows with the new row last. The product over all these columns of the principal minor of
`diag(p τ, 1)` (`blockScalar ι p 1 τ`) on the column's rows equals `det (p τ) ^ κ' τ (rankAt n τ)`
times the product over `h < rankAt n τ` of the `h`-th leading minor of `p τ` along `rowEquivFin`
raised to the power `κ₀ τ h`. 

### `extendedTensor_dotProduct`

 The extended tensors of `a` and `b` pair to the product of the leading minors of `a bᵀ` for
`κ₀`, times a power of the determinant. This is the Cauchy–Binet formula in each column. 

### `weylEval_dotProduct_weylGram_mulVec_weylEval`

 The Gram pairing of the evaluation vectors at `y` and `z` is the product of the leading minors
of `yᵀ z` for `κ₀`, where `y` and `z` are cut down to their square parts. 

### `det_mul_dotProduct_mulVec_eq_extendedTensor`

 Let `v` be the Gram matrix `weylGramOver` times the evaluation vector at the permutation array
of `rowEquivFin`. Let the integral matrix `B` be equivariant for the block group, and let the row
vector `v ᵥ* B` be the coordinates of `c • branchVector ℂ ι γ κ'` in the basis of products of
minors. Then `B` is `c` times the contraction followed by the projection to the Weyl module, in the
following sense. Up to a power of the determinant, the Gram pairing of the evaluation vector at `y`
with `B ξ` is `c` times the pairing of the extended tensor of `y` with the tensor
`fillingMatrixOver ℂ N (γ + κ') *ᵥ ξ` of `ξ`, a vector indexed by column fillings. 

### `span_weylEval_eq_top`

 The evaluation vectors at the arrays whose square parts have `∏ τ, det ^ d τ ≠ 0` span the
Weyl module. 

### `star_extendedTensor`

 Complex conjugation commutes with passing to the extended tensor. 

### `re_dotProduct_mulVec_le_of_forall_dotProduct_eq`

 Let the vectors `m y` have the same Hermitian pairings for the standard form as the vectors
`v y` have for the form `G`, and let `η` lie in the span of the `v y`. If `η` pairs with each `v y`
as `u` pairs with `m y`, so that `η` corresponds to the orthogonal projection of `u` to the span of
the `m y`, then the squared norm of `η` is at most that of `u`. 

### `weylNormSq_mulVec_le_of_equivariant`

 Let `κ₀ τ h = κ' τ h + γ τ (h + 1)` for `0 < h < rankAt n τ`, and let `B` be an integral matrix.
Assume `B * schur (γ + κ') (diag(g, 1)) = (∏ τ, det (g τ) ^ κ' τ (rankAt n τ)) • (schur κ₀ g * B)`
for all complex `g`, with `diag(g, 1)` built by `blockScalar ι`. Let `v` be the Gram matrix
`weylGramOver` times `weylEval` at the permutation array of `rowEquivFin`, and assume also that the
row vector `v ᵥ* B` has the polynomial `c • branchVector ℂ ι γ κ'` under `nablaCombination`
(ξ ↦ Σ ξ_i b_i over the basis products of minors). Then
`weylNormSq (B *ᵥ ξ) ≤ c ^ 2 * weylNormSq ξ` for every complex vector `ξ`. 
