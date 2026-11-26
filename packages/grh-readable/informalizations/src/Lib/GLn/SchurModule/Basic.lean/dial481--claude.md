---
{
  "module": "src/Lib/GLn/SchurModule/Basic.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GLn/SchurModule/Basic.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GLn/SchurModule/Basic.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Schur modules: semi-invariants, minors, Fock pairing, Schur and Gram matrices

This file sets up a polynomial model of the representations of products of general linear groups
over any commutative ring `R`. The variables `X (a, i)` of `New.MatrixPoly m R` form an array with
rows `a : m` and columns `i : ℕ`. A colour map `c` assigns each row a place `τ`, and a weight `κ`
gives the number `κ τ h` of columns of height `h` at `τ`. `New.nabla R c l` consists of the `f` with
`f(y b) = ∏ b(τ, i, i) ^ l(τ, i) · f(y)` for upper triangular `b`, one matrix for each colour, and a
chosen set of products of minors is taken as its basis. The Weyl module is the dual module, written
in the dual basis as `New.WeylIndexFamily n κ → R`; `Lib.GLn.SchurModule.TensorModel` embeds it into
a tensor product of exterior powers. Left substitution `f ↦ f(z y)` and the Fock pairing
`⟨p, q⟩ = p(∂) q (0)` are the main tools. The rows of the Schur matrix expand the substituted basis
elements, so it acts on the Weyl module, and the Gram matrix is the coefficient matrix of the kernel
`New.weylKernel` in the basis.

## Main definitions and results

* `New.jet`, `New.fockPairing`: the pairing `P(∂) F` at `0`, with power series and with polynomials;
  `New.fockPairing_linSubst` computes adjoints of linear substitutions.
* `New.nabla`, `New.nablaFamily`: the semi-invariants under upper triangular matrices acting on
  columns.
* `New.tableauPoly`, `New.IsTableauBasis`, `New.nablaBasis`: products of minors, and a chosen basis
  among them.
* `New.schur`, `New.weylGram`, `New.weylEval`: the matrix of `f ↦ f(z y)`, the Gram matrix and the
  evaluation vectors in that basis.
* `New.mem_nabla`, `New.minor_mem_nabla`, `New.rowSubst_mem_nabla`: membership as an identity over
  all algebras; minors are members; left substitution `f ↦ f(z y)` (`New.rowSubst`) keeps the
  weight.
* `New.fockPairing_comm`, `New.fockPairing_rowSubst`, `New.fockPairing_star_self_pos`: the pairing
  `⟨p, q⟩ = p(∂) q (0)` is symmetric, the adjoint of `New.rowSubst z` is substitution by the
  transposes, and `⟨p̄, p⟩ > 0` for `p ≠ 0`.

## Relation to the literature

Known; see `Lib.GLn.SchurModule.MinorBasis` for sources.



## The polynomial model and its basic objects

Bases are chosen by `Classical.epsilon`. Coordinates in `schur` and `weylGram` are chosen by
`Function.invFun`.


### `borelMul`

 For a row colouring `c` and arrays `b` and `y`, the array `y b` has `(a, j)` entry
`Σ_{i≤j} y(a,i) b(c(a),i,j)`; here `x = (a, j)`. It uses the upper triangular part of `b` at the
colour of `a`. 

### `diagramWeight`

 For bounds `N` and column multiplicities `κ` (`κ τ h` columns of height `h` at `τ`, for
`h < N τ`), the finitely supported weight whose value at `(τ, i)`, columns numbered from 0, is the
sum of `κ τ h` over `i < h < N τ`. 

 ### Polynomial arrays, the Fock pairing, minors, semi-invariants and fillings 

### `MatrixPoly`

 Polynomials over `R` in an array of variables `X (a, i)`, with rows `a : m` and columns
`i : ℕ`. 

### `Tableau`

 The type of fillings assigning, for each height h<N, to each of k(h) columns an h-tuple of
elements of m, with no ordering condition. 

### `jet`

 The bilinear pairing of a polynomial P with a formal power series F giving P(∂)F(0), the sum
over exponents d of d! times both d-th coefficients. 

### `fockPairing`

 The bilinear form on polynomials ⟨P,Q⟩ = P(∂)Q(0), for which monomials are orthogonal and
⟨x^d,x^d⟩ = d!. 

### `minor`

 For an h-tuple I of rows, the polynomial determinant of the h×h matrix of variables in rows
I and the first h columns. 

### `nabla`

 For a row colouring `c : m → Φ` and a weight `l`, the module of Borel semi-invariants: the
polynomials `f` with `f(yβ) = ∏ β_{τ,ii}^{l(τ,i)} f(y)` for generic upper triangular matrices `β_τ`,
one per colour. 

### `tableauPoly`

 For a filling `T` with entries in `σ` and a map `e : σ → m` to the rows, the product over
the columns of `T` of the minors `New.minor` whose rows are the `e`-images of the column's
entries. 

### `GL.alternant`

 For x in ℂ^N and l : ℕ → ℕ, the alternant det(x_i^{l(N−1−j)+j}), 0 ≤ i, j < N, if l(N) = 0,
and zero otherwise. 

### `IsTableauBasis`

 The set `s` of fillings is a standard set, in two parts: (a) over every commutative ring the
minor products of `s` form a basis of the span of all minor products; (b) for every enumeration `e`
of the rows and every `x : m → ℂ`, `(Σ_{T∈s} x^T) a_0(x) = a_λ(x)`. Here `x^T` is the product of `x`
over the entries of `T`, `a` is the alternant `New.GL.alternant`, and `λ(i)` is the sum of `k(h)`
over `i < h < N`. 

### `IsTableauBasis.linearIndepOn`

 For a standard set `s` (`IsTableauBasis`), over every commutative ring `R` the minor products
`tableauPoly R id T`, `T ∈ s`, are linearly independent. 

### `IsTableauBasis.mem_span`

 For a standard set `s`, over every commutative ring `R` the minor product of every filling `T`
lies in the span of the minor products of the members of `s`. 

### `IsTableauBasis.weyl_character_formula`

 The Weyl character formula for a standard set `s`: for every enumeration `e : Fin M ≃ m` of
the rows and every `x : m → ℂ`, `(Σ_{T ∈ s} x^T) a_0(x) = a_λ(x)`, where `x^T` is the product of
`x` over the entries of `T`, `a` is `New.GL.alternant` and `λ i` is the sum of `k h` over
`i < h < N`. 

### `IsTableauBasis.of_linearIndepOn_of_mem_span_of_character`

 A set `s` of fillings is a standard set if, over every commutative ring, its minor products are
linearly independent and span all minor products, and it satisfies the Weyl character formula. 

### `BasisTableau`

 The standard fillings: the members of a chosen finite set of fillings that satisfies
`IsTableauBasis` as soon as some set does. This is the case for a finite alphabet `m`
(`isTableauBasis_epsilon`). They need not be semistandard tableaux. 

### `rankAt`

 The number of elements of the finite row type n_τ at the place τ. 

### `GL.rowEquivFin`

 The fixed enumeration of the rows of n_τ by 0,…,|n_τ|−1, as an equivalence of n_τ with `Fin`
|n_τ|. 

### `WeylIndexFamily`

 The type of families choosing, for each place τ, a filling in the chosen standard set with
rows n_τ, heights below |n_τ| and multiplicities κ_τ. It indexes the basis `nablaBasis` of
`nablaFamily`; the Weyl module over `R` is the dual, `WeylIndexFamily n κ → R` in the dual basis. 

### `WeylIndex`

 The type of families of chosen standard fillings over the places, in the case where the row
type is the same finite type n at every place. 

### `nablaFamily`

 The module of Borel semi-invariant polynomials in rows (τ,a), coloured by τ, whose weight is
the partition tuple built from κ using heights below |n_τ|. It is the span ∇ of the products of
minors, one for each column of the diagram (`span_fillingPoly`). 

### `nablaBasis`

 For a family i of chosen standard fillings, the polynomial that is the product over places τ
of the minor product of i_τ in the rows of block τ. 

### `highestPoly`

 The polynomial product over places τ and h<N_τ of the leading principal h×h minor of the
variables in block τ raised to κ_τ(h). 

### `detPow`

 For exponents `e : Φ → ℕ`, the product over places τ of the determinant of the variables in
all rows of block τ (fixed enumeration) and the first |n_τ| columns, raised to `e τ`. 

### `GL.genericMatrixAt`

 The generic tuple of square matrices: the `(a, b)` entry at `τ` is the variable
`X ⟨τ, a, b⟩`. 

### `hookNumber`

 The hook number: the integer ⟨f,f⟩ = f(∂)f(0), where f is the product of the leading
principal h×h minors raised to κ_τ(h), h<N_τ. 

### `schurDetExp`

 The natural number κ_τ(|n_τ|) if |n_τ| < |n'_τ|, and 0 otherwise, as a function of the place
τ. Under `FitsRanks` and for |n_τ| > 0 it is the length of row number |n_τ|, counted from 1, of the
diagram with κ_τ(h) columns of height h < |n'_τ|. 

### `FitsRanks`

 The condition, at every place τ, that |n_τ| ≤ |n'_τ| and κ_τ(h) = 0 for |n_τ| < h < |n'_τ|:
the diagram with κ_τ(h) columns of height h < |n'_τ| has at most |n_τ| rows. 

 ### Substitutions and evaluations 

### `rowSubst`

 For matrices z_τ of size n'_τ×n_τ, the algebra homomorphism f ↦ f(zy) sending variable
y_{(τ,b),i} to Σ_a z_τ(b,a) y_{(τ,a),i}; here `x = (⟨τ, b⟩, i)`. 

### `permArray`

 For maps e_τ from rows to natural numbers, the array over R whose entry at row (τ,a), column
i is 1 if e_τ(a)=i and 0 otherwise. 

### `instance : CoeOut (∀ τ : Φ, n τ ≃ Fin (rankAt n τ)) (∀ τ : Φ, n τ → ℕ)`

 A numbering of the rows is read as a map to `ℕ`. 

### `GL.nablaCombination`

 The R-linear map sending a coordinate vector ξ to the polynomial Σ_i ξ_i b_i, where the b_i are
the basis products of minors `New.nablaBasis`. 

### `GL.evalMatrix`

 For square matrices `z τ`, the ring homomorphism from polynomials in variables (τ,a,b) to R
evaluating each variable at the matrix entry z_τ(a,b); here `x = ⟨τ, (a, b)⟩`. 

### `jet_eq_sum`

 For a polynomial `f` and a power series `F`, the pairing `jet R f F`, that is `f(∂) F (0)`, is
the sum of `f.coeff d * d! * F.coeff d` over the monomials `d` of `f`, where `d!` is the product of
the factorials of the exponents. 

### `jet_monomial`

 The pairing of the monomial `a * X ^ α` with the power series `F` is `a * α! * F.coeff α`,
where `α!` is the product of the factorials of the exponents. 

### `prod_factorial_add_single`

 Raising the exponent at `i` by one multiplies `d!` by `d i + 1`. 

### `jet_mul_X`

 For the pairing `jet R f F = f(∂) F (0)` of a polynomial with a power series, multiplication of
`f` by `X i` is adjoint to the derivative of `F` in `X i`. 

### `fockPairing_monomial`

 The Fock pairing `⟨a * X ^ α, g⟩` is `α! * a * g.coeff α`, where `α!` is the product of the
factorials of the exponents. 

### `fockPairing_C`

 The Fock pairing of a constant `a` with `g` is `a` times the constant term of `g`. 

### `fockPairing_mul_X`

 For the Fock form, multiplication by `X i` is adjoint to the derivative in `X i`. 

### `schur`

 The Schur matrix `S_κ(z)` of a family of matrices `z τ` of size `n' τ × n τ`. Let `b` and `b'`
be `nablaBasis` for `n` and `n'`, and let `d` be `schurDetExp n n' κ`. Row `i` holds chosen
coordinates of `b'_i(z y)` in the family `b_j(y) * ∏ τ, det(y_τ) ^ d τ`; see
`sum_schur_smul_eq_rowSubst_of_exists`. The row is unspecified if there are no such coordinates;
they exist under `FitsRanks n n' κ` (`sum_schur_smul_nablaBasis`). It is the map of Weyl modules
induced by `z`; for square `z` it is the restriction of the action on tensors
(`fillingMatrixOver_mul_schur`). 

### `sum_schur_smul_eq_rowSubst_of_exists`

 In the notation of `schur` (`n τ`, `n' τ` the finite row types and `κ τ h` the column counts at
the place `τ`): if `b'_i(z y)` is a linear combination of the products
`b_j(y) * ∏ τ, det(y_τ) ^ d τ`, then row `i` of the Schur matrix gives the coefficients of such a
combination. 

### `tableauWeight`

 For a family i of fillings, a place τ and a row a, the number of entries of the filling i_τ
equal to a. 

### `weylKernel`

 For an array `y` over `R`, the polynomial `f(yᵀx)` in `x`, where `f` is the product of leading
minors `New.highestPoly`. Block `τ` uses the first `|n_τ|` columns of `y`. It is the pairing of the
tensors of `x` and `y` (`weylKernel_eq_sum_fillingPoly`). 

### `weylGram`

 The Gram matrix `G`: chosen integer coefficients of the generic kernel `weylKernel n κ X` in
the products `b_i(x) * b_j(y)`, where `b` is `nablaBasis`. The kernel is first expanded in the
`b_i(x)` with coefficients in `ℤ[y]`, and row `i` expands the `i`-th coefficient in the `b_j(y)`;
see `sum_weylGram_smul_eq_weylKernel_of_exists`. Both expansions exist, and `toPoly_weylEval` states
the resulting identity. It is the matrix of the form on the Weyl module for which the basis tensors
are orthonormal (`fillingMatrix_transpose_mul_self`). 

### `sum_weylGram_smul_eq_weylKernel_of_exists`

 Let `n τ` be the finite row type and `κ τ h` the number of columns of height `h` at the place
`τ`, let `y` be the array of variables `X` with rows `(τ, a)`, and let `b = nablaBasis`. If `b` is
linearly independent over the polynomial ring `ℤ[y]` and the generic kernel `weylKernel n κ X` is an
integer combination of the products `b_i(x) * b_j(y)`, then `weylGram` gives the coefficients of
such a combination. 

### `weylGramOver`

 The integer Gram matrix `New.weylGram` for the row type n and column counts κ, with its entries
mapped into R. 

### `toPoly`

 The polynomial of a vector ξ of the Weyl module: Σ_i (Gξ)_i b_i, with G the Gram matrix and b_i
the basis minor products. It is the pairing of the tensor of ξ with the tensor of the variables
(`toPoly_eq_sum_fillingPoly`). 

### `weylEval`

 For an array `y` over `R`, the value `b_i(y)` at `y` of the basis product of minors
`b_i = nablaBasis R n κ i`. The vector `weylEval n κ y` of the Weyl module is the evaluation at `y`;
as a tensor it is the tensor of `y` (`fillingMatrixOver_mulVec_weylEval`). 

 ### Linear substitutions, symmetric powers and polynomials from coefficients 

### `linSubst`

 For an m×σ matrix z over R, the R-algebra map from polynomials in variables indexed by σ to
those indexed by m sending X_b to ∑_t z_{tb} X_t. 

### `pderiv_linSubst`

 The chain rule for a linear substitution: the derivative of `p(zᵀx)` in `x_i` is
`Σ_a z_{ia} (∂p/∂x_a)(zᵀx)`. 

### `fockPairing_linSubst`

 For an `m × σ` matrix `z` over the commutative ring `R`, the substitutions by `z` and by `zᵀ`
(`New.linSubst`) are adjoint for the Fock form `⟨p, q⟩ = p(∂) q (0)`. 

### `Monomials`

 The exponents of the monomials of degree `a` in variables indexed by `σ`. 

### `linSubst_eq_bind₁`

 `linSubst A` substitutes for each variable the linear form of the matching row of `Aᵀ`. 

### `sum_monomials_eq_of_isHomogeneous`

 A polynomial `f`, homogeneous of degree `a` in finitely many variables, is the sum of its terms
`f.coeff β • X ^ β` over the exponents `β` of degree `a`. 

### `symPowMatrix`

 The a-th symmetric power: the homomorphism sending a square matrix A to the matrix, in the
monomial basis, of `New.linSubst` A on forms of degree a. 

### `exponentOf`

 For a family `β` of degree-`a` exponent vectors indexed by `S`, the single exponent vector on
the variables `(b, s)` whose value is `β_s(b)`. 

### `polyOfCoeffs`

 For a coefficient function F on families β of degree-a exponents, the polynomial ∑_β F(β)
x^β in the variables (b,s). 


## Semi-invariants, substitution, the Fock pairing and change of coefficients

* `New.diagramWeight_apply`: the weight in closed form.
* The pairings and the polynomials `New.nablaBasis`, `New.highestPoly`, `New.detPow` commute with
  change of the coefficient ring.


 ### Semi-invariants 

### `mem_nabla`

 `f` lies in `New.nabla R c l` (it is a semi-invariant of weight `l` for the row colouring `c`)
iff for every `R`-algebra `S` and all arrays `b`, `y` over `S` we have
`f(y b) = ∏ b(τ, i, i) ^ l(τ, i) · f(y)`. Here `y b` is `New.borelMul c b y`, the array with
`(a, j)` entry `Σ_{i ≤ j} y(a, i) b(c a, i, j)`, so only the upper triangular part of `b` is
used. 

### `instance : SetLike.GradedMonoid (nabla R c)`

 Semi-invariants multiply, and their weights add. 

### `minor_mem_nabla`

 A minor on `h` rows of colour `τ` and the first `h` columns is a semi-invariant of weight `1`
at `(τ, 0), …, (τ, h - 1)` and `0` elsewhere. 

### `rowSubst_mem_nabla`

 Colour the row `(τ, a)` by `τ` (the colouring `fst`). If `f` is a Borel semi-invariant of
weight `l` in the rows `(τ, b)`, `b : n' τ`, then its substitution `f ↦ f(z y)` by the matrices
`z τ` of size `n' τ × n τ` (`New.rowSubst`) is a Borel semi-invariant of the same weight in the
rows `(τ, a)`, `a : n τ`. 

 ### Substitution and the Fock pairing 

### `rowSubst_rowSubst`

 Substituting by `z'` (from the rows `n'' τ` to the rows `n' τ`) and then by `z` (to the rows
`n τ`) is substituting by the products `z' τ * z τ`. 

### `fockPairing_eq_sum`

 The Fock pairing `⟨p, q⟩` is the sum, over the monomials `d` of `p`, of
`p.coeff d * d! * q.coeff d`, where `d!` is the product of the factorials of the exponents. 

### `fockPairing_comm`

 The Fock pairing is symmetric. 

### `map_fockPairing`

 The Fock pairing commutes with a change of coefficients along a ring homomorphism `φ`. 

### `fockPairing_rowSubst`

 The adjoint of substitution by `z` for the Fock pairing is substitution by the transposes. 

### `fockPairing_star_self_pos`

 Over a star-ordered domain `R`, `⟨p̄, p⟩ > 0` for every nonzero polynomial `p`, where `p̄`
applies `star` to each coefficient. 

 ### The weight, and change of coefficients 

### `diagramWeight_apply`

 The weight at `(τ, i)` is the number `∑ i < h < N τ, κ τ h` of columns of colour `τ` higher
than `i`. 
