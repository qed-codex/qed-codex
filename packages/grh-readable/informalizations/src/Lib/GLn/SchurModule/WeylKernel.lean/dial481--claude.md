---
{
  "module": "src/Lib/GLn/SchurModule/WeylKernel.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GLn/SchurModule/WeylKernel.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GLn/SchurModule/WeylKernel.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The Weyl kernel and its Gram matrix: the hook number bound, positivity, Schur's lemma

This file studies the reproducing kernel `K(x, y) = f(yᵀ x)` (`New.weylKernel`), where
`f = New.highestPoly` is the product of leading principal minors. `G = New.weylGram` is the integer
Gram matrix of `K` in the basis `b_i = New.nablaBasis` (products of minors) of the semi-invariants
`New.nablaFamily`. The hook number `New.hookNumber κ N = ⟨f, f⟩ = f(∂) f(0)` is the Fock pairing
of `f` with itself. It is positive and at most `(L ^ L) ^ 3` when the diagrams have at most `L`
boxes in total (`New.hookNumber_pos`, `New.hookNumber_le`). This file also proves that the unitary
group is Zariski dense, and derives Schur's lemma for the Schur matrices.

## Main definitions and results

* `New.toPoly_weylEval`, `New.toPoly_schur`: `New.toPoly`, `ξ ↦ ∑ (G ξ)_i b_i`, sends the vector
  `ev_y = (b_i(y))` (`New.weylEval`) to `K(·, y)`. It turns the Schur matrix of `z` into
  substitution of `zᵀ`, applied after multiplying by the determinant powers `New.detPow` with
  exponents `New.schurDetExp`.
* `New.fillingMatrix_transpose_mul_self`: `G` is the matrix of the form restricted from tensors.
  Hence `G` is symmetric, positive definite, and makes the Schur matrices of `g` and `gᵀ` adjoint
  (`New.weylGram_isSymm`, `New.weylGramOver_posDef`, `New.weylGramOver_mul_schur`).
* `New.mem_range_scalar_of_commute_schur`: a matrix that commutes with `New.schur κ g` for all
  unitary `g` is scalar.

Notions from other files:
* `New.WeylIndexFamily n κ`: families that choose, for each place `τ`, a standard filling with rows
  `n τ`; they index the basis `b_i`.
* `New.schur κ z`: the Schur matrix `S_κ(z)` of matrices `z τ` of size `n' τ × n τ`. Row `i`
  holds the coordinates of `b'_i(z y)` in the products `b_j(y) · ∏_τ det(y_τ)^{d_τ}`, where `b'` is
  the basis for the rows `n'` and `d = New.schurDetExp n n' κ`.

## Relation to the literature

Known; see `Lib.GLn.SchurModule.SchurNorm` and `Lib.GLn.Dual` for sources.



## Positivity and a bound for the hook number

* `New.hookNumber_pos`, `New.hookNumber_le`: the hook number is positive, and at most
  `(L ^ L) ^ 3` when the diagrams have at most `L` boxes in total.


### `hookNumber_pos`

 The hook number, the Fock pairing of `New.highestPoly ℤ κ N` with itself, is positive. 

### `fockPairing_monomial_monomial_le`

 Two monomials with coefficients `± 1` have Fock pairing at most `d !`, where `d` is the degree
of the first. 

### `fockPairing_tableauPoly_le`

 Take at each place `τ` a filling `T τ` with `κ τ h` columns of height `h` for `h < N τ`, and
multiply the minors of all columns. If the degree `∑ τ, ∑ h < N τ, h * κ τ h` of this product is at
most `L`, then its Fock pairing with itself is at most `L ^ (3 * L)`. 

### `hookNumber_le`

 Suppose the diagrams with `κ τ h` columns of height `h < N τ` have at most `L` boxes in total,
that is, Σ_τ Σ_{h<N τ} h·κ τ h ≤ L. Then `hookNumber κ N` is at most `(L ^ L) ^ 3`. Here
`hookNumber κ N` is the integer ⟨f,f⟩ = f(∂)f(0), where f is the product over places τ and heights
h < N τ of the leading principal h×h minors raised to the power κ τ h. 


## The kernel and the Gram matrix

Linear identities are tested on the vectors `weylEval n κ y` (`New.GL.ext_weylEval`). An array `y`
has rows `(τ, a)` and columns in `ℕ`; `New.diagramWeight` is the partition with `κ τ h` columns of
height `h`.


 ### Evaluation vectors and the kernel 

### `squarePart`

 For an array `y` and enumerations `e τ` of the rows, the square matrix at the place `τ` with
`(a, b)` entry `y((τ, a), e τ b)`: the columns of block `τ` numbered below `|n τ|`. 

### `schur_squarePart_mulVec`

 Every evaluation vector `ev_y` is the image of the evaluation vector at the permutation array
of `e` under the Schur matrix of the square part `New.GL.squarePart e y` of `y`. 

### `ext_weylEval`

 Two linear maps `L`, `L'` into a free module over a domain are equal if they agree on the
evaluation vectors `weylEval n κ y`. It is enough to take the arrays `y` whose entries lie in an
infinite set `s` and at which `detPow R n d`, the product of the powers `d τ` of the determinants
of the square blocks, does not vanish. 

### `rowSubst_highestPoly`

 `f(yᵀ x)` as a polynomial in `x`: the product of the leading minors of `yᵀ x`. 

### `weylKernel_symm`

 The kernel is symmetric in `x` and `y`: `K(·, y)` is the generic kernel, whose coefficients are
polynomials in the variables for `y`, with `y` put in for its variables `x`, and the coefficient
variables kept as the new variables. 

### `weylKernel_borelMul`

 Multiplying `y` on the right by the upper triangular part of `b` scales the kernel `K(·, y)`
by `∏ b(τ, i, i) ^ λ(τ, i)`, with `λ = New.diagramWeight (rankAt n) κ`. 

### `eval_toPoly`

 For a vector ξ of the Weyl module over a commutative ring `R` and an array `y` over `R`, the
value at `y` of the polynomial `toPoly n κ ξ = Σ_i (Gξ)_i b_i` equals ev_yᵀ G ξ. Here the b_i are
the basis products of minors `nablaBasis`, indexed by `WeylIndexFamily n κ`, and
ev_y = `weylEval n κ y` is the vector of values b_i(y). G is the integer Gram matrix `weylGram`, the
coefficients of the generic kernel in the products b_i(x) b_j(y), mapped into `R`. 

### `blockScalar`

 For square matrices `g τ` and scalars `s τ`, the block diagonal matrix `diag(g τ, s τ)`,
reindexed by `n' τ` through the bijection `ι τ : n τ ⊕ Unit ≃ n' τ`. 

### `diagramWeight_eq_succ_add`

 The weight at `(τ, i)` is the weight at `(τ, i + 1)` plus `κ τ (i + 1)` when `i + 1 < N τ`:
the columns of height `i + 1` are counted at `i` but not at `i + 1`. 

### `rowSubst_weylKernel_permArray`

 The kernel `weylKernel n κ y` is the polynomial f(yᵀx) in x, with f the product of leading
minors; here y is the permutation array of `e` (entry 1 at row (τ,a), column `e τ a`, else 0). If
`g τ a b = 0` whenever `e τ a < e τ b`, substituting x ↦ g x in the kernel (`rowSubst g`) scales it
by `∏ g τ a a ^ λ(τ, e τ a)`, with `λ = New.diagramWeight (rankAt n) κ`. 

 ### The kernel formula 

### `toPoly_weylEval`

 The polynomial attached by the Gram matrix to the evaluation vector ev_y is the kernel x ↦
f(yᵀx), f the highest weight product of leading minors. 

### `GL.weylGram_eq_submatrix`

 The Gram matrix `New.weylGram` does not depend on the labelling of the places: for a bijection
`p` from `Φ` to `Ψ`, the Gram matrix of `(n, κ)` is that of the data transported to `Ψ`, with rows
and columns reindexed along `p`. 

 ### The form restricted from tensors 

### `weylKernel_eq_sum_fillingPoly`

 The kernel at `y` is the pairing of the tensor of `y` with the tensor of the variables. 

### `fillingMatrix_transpose_mul_self`

 Let F = `fillingMatrix n κ` be the integral matrix of the embedding of the Weyl module into
tensors, whose row `T` holds the coordinates of the product of minors of `T` in the standard basis.
Then FᵀF = `weylGram n κ`: the Gram matrix is that of the form on tensors for which the basis
tensors are orthonormal, restricted to the Weyl module. 

### `weylGramOver_eq_transpose_mul`

 The Gram matrix `weylGramOver` over `R`, which is the integer matrix `New.weylGram` mapped into
`R`, equals FᵀF. Here F = `fillingMatrixOver R n κ` is the integer matrix `fillingMatrix` mapped
into `R`. Thus the Gram matrix is that of the form restricted from tensors. 

### `toPoly_eq_sum_fillingPoly`

 The polynomial of a vector is the pairing of its tensor with the tensor of the variables. 

### `weylGram_isSymm`

 The integer Gram matrix `weylGram n κ` is symmetric. Its entries are the chosen coefficients of
the generic kernel `weylKernel n κ` in the products b_i(x) b_j(y) of the basis minor products
b = `nablaBasis`, indexed by `WeylIndexFamily n κ`. 

### `weylGramOver_posDef`

 The Gram matrix `weylGram n κ` of the Weyl module, indexed by `WeylIndexFamily n κ` and with
entries mapped into `ℂ` (`weylGramOver`), is positive definite. It is the Gram matrix of the
restriction to the Weyl module of the form on tensors for which the standard basis tensors are
orthonormal (see `fillingMatrix_transpose_mul_self`). 

### `weylGramOver_mul_schur`

 For a family `g` of square matrices `g τ`, let `G = weylGramOver` be the integer Gram matrix
`New.weylGram` for rows `n` and column counts `κ`, mapped into `R` and indexed by
`WeylIndexFamily n κ`. Let `schur κ g` be the Schur matrix S_κ(g) of `g` acting on the Weyl module.
Then G·S_κ(g) = S_κ(gᵀ)ᵀ·G, so the Schur matrices of `g` and of the transposes `(g τ)ᵀ` are adjoint
for the form with Gram matrix G. 

 ### Schur matrices and substitution 

### `GL.vecMul_schur_eq_iff`

 If the ranks fit `κ`, then `c ᵥ* S_κ(z) = x` if and only if the substitution `y ↦ z y` sends
`Σ_i c_i b'_i` to `(Σ_j x_j b_j) · ∏_τ det(y_τ)^{d_τ}`, with `d = New.schurDetExp n n' κ`. 

### `toPoly_schur`

 Let `R` be a domain of characteristic zero, and assume `FitsRanks n n' κ`: at each place τ,
|n_τ| ≤ |n'_τ| and `κ τ h = 0` for |n_τ| < h < |n'_τ|. For a family `z τ` of `n' τ × n τ` matrices
and a Weyl module vector ξ, the polynomial `toPoly n' κ` of S_κ(z)ξ, where S_κ(z) = `schur κ z` is
the Schur matrix, is x ↦ (ξ̂·D)(zᵀx). Here ξ̂ = `toPoly n κ ξ` = Σ_i (Gξ)_i b_i (G the Gram matrix,
b_i the basis minor products), and D = ∏_τ det_τ^{d_τ}, with det_τ the determinant of the variables
in block τ and its first |n_τ| columns. The exponent is d_τ = `schurDetExp n n' κ τ`, equal to
`κ τ |n_τ|` if |n_τ| < |n'_τ| and 0 otherwise. 

### `toPoly_injective`

 Over a domain of characteristic zero, the map sending a coordinate vector ξ to the
polynomial ∑ (Gξ)_i b_i, G the Gram matrix, is injective. 

### `range_toPoly`

 Let `toPoly n κ` be the map on the Weyl module `WeylIndexFamily n κ → ℂ` sending ξ to Σ_i (Gξ)_i
b_i. Here G is the Gram matrix `weylGramOver` (the integer matrix `New.weylGram` mapped into ℂ), and
b_i = `nablaBasis ℂ n κ i` are the basis minor products. Over ℂ, its range is exactly the module
`New.nablaFamily ℂ n κ` of Borel semi-invariant polynomials of the weight given by κ. 


## Zariski density of the unitary group and Schur's lemma

`New.weylEval n κ y` is the vector of the values at the array `y` of the basis minor products.


### `GL.analyticOnNhd_evalMatrix`

 For a complex polynomial P in the entries of a family of square matrices, its value
`evalMatrix g P` at the family `g` is an entire function of `g`. 

### `GL.zariski_dense_unitary`

 The unitary group is Zariski dense. Let P be a complex polynomial in the entries of a family
of square matrices `g τ`, and write `evalMatrix g P` for its value at `g`. If P vanishes at every
family of unitary matrices (`(g τ)ᴴ * g τ = 1` for all τ), then it vanishes at every family x. 

### `GL.ext_schur_weylEval`

 Over a field `K` of characteristic zero, let `v₀` be the frame vector of the enumerations `e`,
the evaluation vector at the permutation array of `e`. Two linear maps that agree on
`schur κ g *ᵥ v₀` for all tuples `g` of invertible matrices are equal.

So the translates of the frame vector under the product of general linear groups span the module.
The reason is duality: they are the evaluation vectors at invertible arrays, and a polynomial that
vanishes on invertible matrices is zero.

In other words, the frame vector is cyclic for the product of the general linear groups. 

### `mem_range_scalar_of_commute_schur`

 Schur's lemma for the unitary group: a complex matrix `T` that commutes with `schur κ g` for
every tuple `g` of unitary matrices is a scalar matrix.

A form of Weyl's theorem on irreducibility of the complex Schur module: the commutant of the Schur
matrices of all tuples of unitary matrices consists of scalars. 
