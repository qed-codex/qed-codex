---
{
  "module": "src/Lib/General/LinearAlgebra/HermitianMatrices.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/LinearAlgebra/HermitianMatrices.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/LinearAlgebra/HermitianMatrices.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Determinants of positive semidefinite matrices, principal minors and hermitian involutions

The file proves inequalities and identities for complex matrices. The norm of a matrix is the `L²`
operator norm, and `≤` between matrices is the positive semidefinite order. It also studies a
hermitian involution `J` and its unitary group `New.U J`, the group of invertible matrices `g` with
`gᴴ * J * g = J`, with real coordinates on skew-hermitian matrices. For signs `ε i = ±1`,
`New.signMatrix ε` is their diagonal matrix and `New.USign ε` its unitary group.

## Main definitions and results

* `New.norm_det_le_norm_det_of_posSemidef`: `0 ≤ P ≤ Q` implies `|det P| ≤ |det Q|`.
* `New.norm_det_sq_le_of_posSemidef`: if the block matrix with rows `(P, A)` and `(B, Q)` is
  positive semidefinite, then `|det A|² ≤ |det P| |det Q|`.
* `New.principalMinor`: the principal minor on the indices satisfying a predicate `p`.
* `New.jacobi_complementary_minor`: Jacobi's theorem, the principal minors of `x⁻¹` from the
  complementary principal minors of `x`.
* `New.IsHermitianInvolution J`: `J` is hermitian and `J * J = 1`. Examples are `1` and the diagonal
  matrices of signs `New.signMatrix ε`.

## Relation to the literature

Known; see `Lib.DiscreteSeries.Haar.TotalMass` for sources.


 ## Positive semidefinite matrices 

### `New.norm_det_le_norm_det_of_posSemidef`

 If `P` and `Q - P` are positive semidefinite complex square matrices, that is `0 ≤ P ≤ Q` in
the Loewner order, then `|det P| ≤ |det Q|`. 

### `New.norm_det_sq_le_of_posSemidef`

 Cauchy–Schwarz inequality for determinants: if the complex block matrix with rows `(P, A)` and
`(B, Q)`, all blocks square of the same size, is positive semidefinite, then
`|det A|² ≤ |det P| * |det Q|`. 

### `New.exists_lowerTriangular_conjTranspose_mul_mul_eq_one`

 Gram–Schmidt for a positive definite matrix `G`: there is a lower triangular matrix `Γ` whose
columns are orthonormal for `G`. 


## Principal minors and Jacobi's complementary minor theorem

* `New.principalMinor_eq_det`: the principal minor of `x` on the indices satisfying `p` is the
  determinant of the matrix with the rows of `x` on `p` and those of `1` off `p`. Most identities of
  this section are reduced to determinants in this way.
* `New.U.principalMinor_coe_inv`, `New.U.principalMinor_compl`: inverse and complementary minors in
  `New.USign ε`. This is the group of `g` in `GL n ℂ` with `gᴴ J g = J`, for the diagonal matrix
  `J = New.signMatrix ε` of signs `ε i = ±1`.


 ### Definition and the operator norm bound 

### `principalMinor`

 The principal minor of the complex matrix `y` on the set of indices satisfying `p`. 

### `norm_principalMinor_le_pow`

 The absolute value of the principal minor of a complex square matrix `x` on the indices
satisfying `p` is at most `‖x‖ ^ k`, where `‖x‖` is the operator norm and `k` is the number of
these indices. 

 ### Principal minors as determinants 

### `principalMinor_eq_det`

 A principal minor is a full determinant: with `D` the diagonal projection onto the indices
satisfying `p`, the matrix `1 - D * (1 - x)` has the rows of `x` on `p` and the rows of `1` off
`p`, and its determinant is the principal minor of `x` on `p`. 

### `principalMinor_fromBlocks`

 A principal minor of the block diagonal matrix with blocks `x` and `y` is the product of the
principal minors of `x` and `y` on the indices of each block that satisfy `p`. 

### `principalMinor_blockDiagonal`

 A principal minor of the block diagonal matrix with blocks `u τ` is the product over `τ` of the
principal minors of `u τ` on the indices `i` for which `(τ, i)` satisfies `p`. 

### `jacobi_complementary_minor`

 Jacobi's complementary minor theorem: for a complex square matrix `x` with `det x ≠ 0`, the
principal minor of `x⁻¹` on the indices satisfying `p` equals the principal minor of `x` on the
complementary indices divided by `det x`. 

 ### Special cases, products and reindexing 

### `principalMinor_mul`

 Suppose `x i j * b j k` has a zero factor whenever `i`, `k` satisfy `p` and `j` does not. This
holds, for instance, when `x i j = 0` whenever `i` satisfies `p` and `j` does not. It also holds
when `b j k = 0` whenever `j` does not satisfy `p` and `k` does. Then the principal minor on `p` of
`x * b` is the product of those of `x` and `b`. 

 ### Indefinite unitary groups, and the bound for the determinant 

### `U.principalMinor_coe_inv`

 For `g` in `USign ε = U (signMatrix ε)`, the unitary group of the diagonal matrix of signs
`ε i = ±1`, each principal minor of the inverse of `g` is the complex conjugate of the same
principal minor of `g`. 

### `U.principalMinor_compl`

 For `g` in `USign ε = U (signMatrix ε)`, the unitary group of the diagonal matrix of signs
`ε i = ±1`, the principal minor on the complement of `p` is `det g` times the conjugate of the
principal minor on `p`. 


## Hermitian involutions and coordinates on skew-hermitian matrices

* `New.skewOfReal`, `New.skewCoords`: real coordinates on skew-hermitian matrices. The `n²`
  coordinates are held in a real `n × n` matrix.


### `IsHermitianInvolution`

 The complex matrix J is a hermitian involution: J* = J and J² = 1. 

### `IsHermitianInvolution.isHermitian`

 The matrix `J` is hermitian. 

### `IsHermitianInvolution.mul_self`

 The matrix `J` is an involution: `J² = 1`. 

### `skewOfReal`

 The skew-hermitian matrix `x` with real coordinates `y`: its entries are `I * y a a` on the
diagonal and `((1 + I) * y a b - (1 - I) * y b a) / √2` off it. The factor `√2` makes
`(y a b, y b a)` an orthogonal change of `(Re x a b, Im x a b)`, so Lebesgue measure in `y` is
Lebesgue measure in `Im x a a` and `Re x a b`, `Im x a b` for one of each pair `(a, b)`, `(b, a)`,
`a ≠ b`. 

### `skewCoords`

 The real coordinates of a complex matrix `x`: the entries `Re x a b + Im x a b`, divided by `√2`
off the diagonal. It is a left inverse of `New.skewOfReal`, and a two-sided one on skew-hermitian
`x`. 


## Norms and determinants in the unitary group of a hermitian involution

* `New.U.norm_det`: the determinant of `g` in `New.U J` has absolute value `1`.


### `U.norm_det`

 For a hermitian involution `J`, the determinant of an element of `U J`, the group of `g` with
`gᴴ * J * g = J`, has absolute value `1`. 

### `U.norm_inv`

 For a hermitian involution `J` and `g` in `U J`, the group of `g` with `gᴴ * J * g = J`, the
inverse of `g` has the operator norm of `g`. 

### `U.one_le_norm`

 For a hermitian involution `J` in positive dimension, every element of `U J`, the group of `g`
with `gᴴ * J * g = J`, has operator norm at least `1`. 
