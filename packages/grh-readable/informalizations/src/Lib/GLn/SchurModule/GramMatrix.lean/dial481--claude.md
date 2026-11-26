---
{
  "module": "src/Lib/GLn/SchurModule/GramMatrix.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GLn/SchurModule/GramMatrix.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GLn/SchurModule/GramMatrix.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Fock pairing, Hermitian norm and Cartan products for the Gram matrix of the Weyl kernel

This file uses the Fock pairing `⟨P, Q⟩ = P(∂) Q (0)` (`New.fockPairing`) and Schur's lemma to show
that the Gram matrix `G = New.weylGram` times the matrix of the Fock pairings of the basis
`b_i = New.nablaBasis` (products of minors) of the semi-invariants `New.nablaFamily` is the hook
number `New.hookNumber κ N = ⟨f, f⟩`, the Fock pairing of `f = New.highestPoly` with itself.
It treats weights with one row at each place. It defines the squared
norm `New.weylNormSq ξ = re (ξ* G ξ)` and builds a tight frame of integral vectors. It shows that
this norm is submultiplicative under Cartan multiplication of polynomials of weights `κ` and `κ'`,
and defines the products of determinants `New.pairedDetProd`.

## Main definitions and results

* `New.weylGram_mul_fockPairing`, `New.fockPairing_toPoly_nablaBasis`: by Schur's lemma, `G` times
  the matrix of the Fock pairings `⟨b_i, b_j⟩` is the hook number `New.hookNumber`.
* `New.GL.comulMatrix`: the matrix `C`, in the bases `New.nablaBasis`, of multiplication of
  polynomials of weights `κ` and `κ'` into those of weight `κ + κ'`;
  `New.GL.vecMul_comulMatrix_eq_iff`: acting on row vectors, `C` multiplies polynomials;
  `New.GL.comulMatrix_mulVec_weylEval`: acting on columns, it sends an evaluation vector to a tensor
  product of two.
* `New.GL.comulMatrix_isometry`, `New.GL.comulMatrix_equivariant`, `New.GL.hasLeftInv_comulMatrix`:
  `C` is an isometry for the Gram matrices, intertwines the Schur matrices, and has a left inverse
  over `ℤ`.

Notions from other files:
* `New.WeylIndexFamily n κ`: families that choose, for each place `τ`, a standard filling with rows
  `n τ`; they index the basis `b_i`.
* `New.schur κ z`: the Schur matrix `S_κ(z)` of matrices `z τ` of size `n' τ × n τ`. Row `i`
  holds the coordinates of `b'_i(z y)` in the products `b_j(y) · ∏_τ det(y_τ)^{d_τ}`, where `b'` is
  the basis for the rows `n'` and `d = New.schurDetExp n n' κ`.
* `New.mem_range_scalar_of_commute_schur` (`Lib.GLn.SchurModule.WeylKernel`): Schur's lemma, a
  matrix that commutes with `New.schur κ g` for all unitary `g` is scalar.

## Relation to the literature

Known; see `Lib.GLn.SchurModule.SchurNorm` and `Lib.GLn.Dual` for sources.



## The Fock form and the Gram matrix

A vector `ξ` pairs with a polynomial `P = ∑ c_k b_k` in two ways, by `ξ(P) = ∑ ξ_k c_k` and by the
Fock pairing `⟨ξ̂, P⟩` with `ξ̂ = New.toPoly n κ ξ`. By Schur's lemma the two are proportional, and
the factor is the hook number.


### `fockPairing_toPoly_nablaBasis_eq_mulVec`

 The Fock pairing of the polynomial Σ_i (Gξ)_i b_i attached to ξ with b_k is the coordinate k of
HᵀGξ, where G is the Gram matrix and H the integer matrix of the Fock pairings ⟨b_i, b_j⟩. 

### `fockPairing_weylKernel_permArray_self`

 The kernel at the permutation array of the row numbering `rowEquivFin` is the product of the
leading minors with the rows renamed, so its Fock pairing with itself is the hook number. 

### `weylGram_mul_fockPairing`

 The Gram matrix `weylGram n κ` has as entries the integer coefficients of the generic kernel
`weylKernel` in the products b_i(x)·b_j(y), where b = `nablaBasis` are the basis minor products. It
times the matrix of Fock pairings ⟨b_i,b_j⟩ = b_i(∂)b_j(0) equals the hook number
`hookNumber κ (rankAt n)` times the identity matrix. 

### `fockPairing_toPoly_nablaBasis`

 Let ξ be a vector of the Weyl module `WeylIndexFamily n κ → R` over any commutative ring `R`,
and let `toPoly n κ ξ` be its polynomial Σ_i (Gξ)_i b_i. Here G is the Gram matrix `weylGramOver`
and b_i = `nablaBasis R n κ i` are the basis minor products. For each index k, the Fock pairing
⟨P,Q⟩ = P(∂)Q(0) of `toPoly n κ ξ` with b_k equals `hookNumber κ (rankAt n)` times the coordinate
ξ_k. 

### `fockPairing_toPoly_toPoly`

 For vectors ξ, η of the Weyl module over a commutative ring `R` (functions on
`WeylIndexFamily n κ`), the Fock pairing ⟨P,Q⟩ = P(∂)Q(0) of the polynomials
`toPoly n κ ξ = Σ_i (Gξ)_i b_i` and `toPoly n κ η` equals the hook number times ξᵀ G η. Here the b_i
are the basis products of minors `nablaBasis`, indexed by `WeylIndexFamily n κ`. G is the integer
Gram matrix `weylGram`, the coefficients of the generic kernel `weylKernel` in the products b_i(x)
b_j(y), mapped into `R`. The hook number is ⟨f,f⟩, where f is the product over places τ of the
leading principal h×h minors raised to κ_τ(h), for h < |n_τ|. 

### `exists_weylGram_mulVec_eq_hookNumber_smul`

 The orthogonal projection of an integral tensor `v` to the Weyl module becomes integral after
multiplication by the hook number: some integral vector has the same pairings with the Weyl module
as that multiple of `v`. 


## Weights with one row at each place

If only columns of height one occur, with `κ τ 1` of them at `τ`, the basis polynomials are
monomials in the first columns `z_τ` of variables.


### `firstColumnExponent`

 The exponent of the monomial `∏ z_τ ^ α_τ`, where `z_τ` is the first column of variables at
`τ`. 

### `prod_firstColumnExponent`

 A product over the exponent `firstColumnExponent α` runs over the variables in the first
columns. 

### `multinomialMonomial`

 The polynomial `∏_τ (|α_τ|! / α_τ!) z_τ ^ α_τ` in the first columns `z_τ` of variables, where
`|α_τ|` is the sum of the exponents at `τ` and `α_τ!` the product of their factorials. 

### `prod_tableauPoly_one_row`

 Suppose only columns of height at most one occur (`κ τ h = 0` for 1 < h < `N τ`). Then the
product over τ of the polynomials `tableauPoly` of the fillings `T τ` (products of minors on the
rows given by the columns' entries) is a monomial in the first column of variables at each τ. Its
exponent at (τ, b) is the number of height-one columns of `T τ` with entry b. 

### `hookNumber_one_row`

 The hook number of a weight with one row at each place is the product of the factorials of the
row lengths. 

### `exists_toPoly_eq_sum_multinomialMonomial`

 Over a field `R` of characteristic zero, assume every row type `n τ` has more than one element
(`1 < rankAt n τ`) and `κ τ h = 0` for `1 < h < rankAt n τ`, so the weight is one row of length
`κ τ 1` at each place. Then there is an injective assignment `α` from basis indices
`i : WeylIndexFamily n κ` to exponent families, with `∑ b, α i τ b = κ τ 1` for every τ. For every
vector ξ, its polynomial `toPoly n κ ξ = Σ_i (Gξ)_i b_i` (G the Gram matrix, b_i the basis minor
products) equals `∑ i, ξ i • multinomialMonomial R (α i)`, where `multinomialMonomial R α = ∏_τ
(|α_τ|!/α_τ!) z_τ^{α_τ}` in the first columns `z_τ` of the variables. 

### `toPoly_mem_span_multinomialMonomial_iff`

 Over a field `R` of characteristic zero, assume every row type `n τ` has more than one element
(`1 < rankAt n τ`) and `κ τ h = 0` for `1 < h < rankAt n τ`, so the weight is one row of length
`κ τ 1` at each place. Let `A` be a subring of `R`. A vector ξ has all coordinates `ξ i` in `A` if
and only if its polynomial `toPoly n κ ξ = Σ_i (Gξ)_i b_i` (G the Gram matrix, b_i the basis minor
products) lies in the `A`-span of the `multinomialMonomial R α` with `∑ b, α τ b = κ τ 1` for all τ.
Here `multinomialMonomial R α = ∏_τ (|α_τ|!/α_τ!) z_τ^{α_τ}` in the first columns `z_τ` of the
variables. 


## The Hermitian norm

* `New.weylNormSq`: the squared norm `re (ξ* G ξ)` of a complex coordinate vector `ξ`.
* `New.GL.weylNormSq_weylEval_permArray`: the evaluation vector `New.weylEval` at the permutation
  array of enumerations of the rows has norm `1`.
* `New.GL.exists_tightFrame`: the hook number times the orthogonal projections of the basis tensors
  to the Weyl module form a tight frame of integral vectors; `New.GL.card_columnFilling_le` bounds
  the number of basis tensors.


### `weylNormSq`

 For a complex coordinate vector ξ, the real part of ξ* G ξ, where G is the integer Gram
matrix. It is the squared norm of ξ for the Hermitian form of G, which is positive definite. 

### `weylNormSq_comp_smul`

 The squared Gram norm of `σ ∘ (t • ξ)` is `‖σ t‖ ^ 2` times that of `σ ∘ ξ`, for multiplicative
`σ`. 

### `posDef_cauchy_schwarz`

 Cauchy–Schwarz for the Hermitian form of a positive definite complex matrix M:
`‖x* M y‖ ^ 2 ≤ re (y* M y) * re (x* M x)`. 

### `coe_weylNormSq`

 As a complex number, the squared Gram norm `weylNormSq ξ` is `ξ* G ξ` itself: its imaginary part
is zero because G is positive semidefinite. 

### `star_weylEval`

 The complex conjugate of the evaluation vector at y (the values `b_i y` of the basis minor
products) is the evaluation vector at the conjugate array, since the `b_i` have integer
coefficients. 

### `weylNormSq_weylEval_permArray`

 For enumerations `e τ` of the rows, the evaluation vector at the permutation array of e (entry
1 at row `(τ, a)` and column `e τ a`, and 0 elsewhere) has Gram norm 1. 

### `exists_tightFrame`

 A tight frame of integral vectors. Let `hk` be the hook number and `⟨ξ, ξ'⟩ = ξ* G ξ'` the form
of the Gram matrix. There are integral vectors `η T`, one for each basis tensor `T`
(`New.ColumnFilling`), with `∑ T, ⟨η T, ξ⟩ η T = hk² ξ` for all `ξ` and of norm at most `hk`. 

### `card_columnFilling_le`

 If all ranks are at most `t ≥ 1` and the diagrams have at most `L` boxes in total, there are at
most `t ^ L` basis tensors (`New.ColumnFilling`). 

### `exists_toPoly_eq_hookNumber_smul`

 Over any commutative ring, let f be a Borel semi-invariant of the weight given by κ
(`New.nablaFamily`). Then the hook number times f is `toPoly n κ ζ` for some coordinate vector ζ,
where `New.toPoly` sends ζ to `∑ i, (G ζ) i • b i` (G the Gram matrix, b the basis minor
products). 


## Cartan multiplication and norms of products

`New.WeylIndexFamily n κ` indexes the basis, and `New.weylEval n κ y` is the vector of values of the
basis at `y`. The tensor product `(p, q) ↦ a p * b q` is written `(vecMulVec b a).vec`, since
`Matrix.vec` swaps the two indices.


### `comulMatrix`

 The matrix of multiplication: row `(p, q)` holds the integer coordinates of the product of the
basis elements `nablaBasis ℤ n κ p` and `nablaBasis ℤ n κ' q` in the basis for `κ + κ'`, cast to
`R`. 

### `comulMatrix_mulVec_weylEval`

 The multiplication matrix sends the evaluation vector at `y` for `κ + κ'` to the tensor product
of those for `κ` and `κ'`: the right side is `(p, q) ↦ weylEval n κ' y q * weylEval n κ y p`. 

### `vecMul_comulMatrix_eq_iff`

 Work over an infinite domain, and let `a ⊗ b` be the row vector `(vecMulVec b a).vec`, with
entry `b q * a p` at `(p, q)`. Then `a ⊗ b` times the multiplication matrix is `x` exactly when the
product of the polynomials with coordinates `a` (basis for `κ`) and `b` (basis for `κ'`) has
coordinates `x` (basis for `κ + κ'`). 

### `comulMatrix_isometry`

 Over an infinite domain, the multiplication matrix `C` is an isometry for the Gram forms:
`Cᵀ (G κ ⊗ G κ') C = G (κ + κ')`, where `G` is the Gram matrix `weylGram` mapped into `R`. 

### `comulMatrix_equivariant`

 Over an infinite domain, the multiplication matrix `C` is equivariant: for the Schur matrices
`S` of a family `g` of square matrices, `(S κ g ⊗ S κ' g) C = C * S (κ + κ') g`. 

### `comulMatrix_isometry_and_equivariant`

 Over an infinite domain, let `C` be the multiplication matrix.
(a) `Cᵀ (G κ ⊗ G κ') C = G (κ + κ')` for the Gram matrices `G`; this part does not involve `g`.
(b) `(S κ g ⊗ S κ' g) C = C * S (κ + κ') g` for the Schur matrices `S` of any family `g` of square
matrices. 

### `hasLeftInv_comulMatrix`

 The integer matrix whose row (p, q) lists the coordinates of the product of the basis minor
products b_p for κ and b_q for κ', in the basis for κ + κ', has an integer left inverse. 

### `_root_.New.weylNormSq_le_mul_of_toPoly_eq`

 Let ξ, η, ζ be complex vectors of the Weyl modules of weights κ, κ' and κ+κ'. Assume the
polynomial of ζ is the product of those of ξ and η, where the polynomial `toPoly` of a vector ξ is
Σ_i (Gξ)_i b_i, with G the integer Gram matrix and b_i the basis minor products. Then
`weylNormSq ζ ≤ weylNormSq ξ * weylNormSq η`, where `weylNormSq ξ` is the real part of ξ* G ξ, the
squared norm for the positive definite Hermitian form of G. 


## Products of determinants

* `New.pairedDetProd`: the product of the determinants `det (η τ k * Y τ)`, with one matrix `Y τ`
  for each `τ : Φ`.


### `pairedDetProd`

 The element ∏_τ ∏_k det(η_{τk} Y_τ) of the ℂ-algebra S, for n×a matrices Y_τ over S and
complex a×n matrices η_{τk}. 
