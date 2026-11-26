---
{
  "module": "src/Lib/General/LinearAlgebra/MatrixPolynomials.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/LinearAlgebra/MatrixPolynomials.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/LinearAlgebra/MatrixPolynomials.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Minors, polynomials of matrices and twisted norms

This file contains general lemmas on matrices over commutative rings, and three definitions used
elsewhere: a minor of a matrix of variables, a non-degeneracy condition on a trace form and a
freeness condition on a family of integers.

## Main definitions and results

* `New.Rows.variableMinor_ne_zero`: a minor of a matrix of variables with distinct rows and distinct
  columns is not zero.
* `New.IsTraceNondeg r`: the trace form is non-degenerate on the span of the matrices `r g`.
* `New.HasNoSmallRelations e`: here `e : Fin n → ℤ`, with `n` a natural number. A sum of at most
  `(n + 1) ^ 2` of the integers `e i`, together with the number of terms, determines how often each
  `e i` occurs.
* `New.det_eval_eq_zero_iff_not_linearIndependent`: over a field, finitely many functions
  `v j : X → k` are linearly dependent if and only if all the determinants `det (v j (x i))` vanish.
* `New.charpoly_dvd_charpoly_aeval_comp`, `New.isUnit_aeval_iff_isCoprime`: the characteristic
  polynomial of `Y` divides that of `q(Y)` composed with `q`, and `z(Y)` is invertible iff `z` is
  coprime to the characteristic polynomial of `Y`.
* `New.exists_gl_map_eq_of_fixed`: an invertible matrix fixed by `σ` lifts along any injective
  ring map whose image contains the fixed points of `σ`.

Notions from other files:
* `New.twistedNorm τ p δ`: the product `δ · τ(δ) ⋯ τ^(p-1)(δ)` in a monoid `M`, for `τ : M → M`.


 ## A nonvanishing minor of the matrix of variables 

### `New.Rows.variableMinor`

 The minor `det (X (τ, i a, j b))`, with `a b : l`, of the matrix of variables attached to `τ`,
taken in the rows `i` and the columns `j`. 

### `New.Rows.variableMinor_ne_zero`

 If the row indices `i` and the column indices `j` are injective, then the determinant
`variableMinor τ i j` of the matrix of variables `X (τ, i a, j b)` is a nonzero polynomial. 

 ## Trace forms, free integers and vanishing minors 

### `New.IsTraceNondeg`

 The trace form is non-degenerate on the span of the matrices `r g`: any `x` in that span with
`tr (x * r g) = 0` for all `g` is zero. 

### `New.HasNoSmallRelations`

 The integers `e i` are free: two vectors `α`, `β` of natural numbers with
`∑ α i = ∑ β i ≤ (n + 1) ^ 2` and `∑ α i * e i = ∑ β i * e i` are equal. 

### `New.det_eval_eq_zero_iff_not_linearIndependent`

 Functions `v j : X → k` to a field, indexed by the finite type `n`, are linearly dependent if
and only if, for every family of points `x : n → X`, the determinant of the square evaluation
matrix `of (flip v ∘ x)`, with entries `v j (x i)`, is zero. 


## Polynomials evaluated at matrices, fixed matrices and twisted norms

`New.star_aeval`, `New.map_aeval_matrix` and `New.aeval_semiconj` say that `z(Y)` is compatible
with star, with ring maps and with intertwining matrices.


### `star_aeval`

 For an `R`-algebra `A` with compatible star structures, the star of `q(x)` is the value at
`star x` of the polynomial obtained from `q` by applying the star of `R` to its coefficients. 

### `map_aeval_matrix`

 Applying the ring map `ψ` to the entries of `z(Y)` gives the value at the matrix `Y.map ψ` of
the polynomial `z.map ψ`. 

### `twistedNorm_map_eq_prod`

 The twisted norm `z · σ(z) ⋯ σ^(p-1)(z)` of a polynomial `z`, with `σ` acting on coefficients,
is the product of the polynomials `z.map (σ ^ i)` for `i < p`. 

### `aeval_semiconj`

 If `c` intertwines the square matrices `x` and `y`, then it intertwines `q(x)` and `q(y)`. 

### `commute_conjTranspose_aeval`

 For a normal matrix `x`, the conjugate transpose of `w(x)` commutes with `z(x)`. 

### `charpoly_dvd_charpoly_aeval_comp`

 The characteristic polynomial of `Y` divides `χ(q(X))`, where `χ` is the characteristic
polynomial of `q(Y)`. 

### `isUnit_aeval_iff_isCoprime`

 The matrix `z(Y)` is invertible if and only if the polynomial `z` is coprime to the
characteristic polynomial of `Y`. 

### `exists_gl_map_eq_of_fixed`

 Let `σ` be a ring endomorphism of `S` and `ψ : R →+* S` an injective ring homomorphism whose
image contains every element fixed by `σ`. If applying `σ` to the entries of `g : GL n S` leaves
`g` unchanged, then `g` is obtained from an element of `GL n R` by applying `ψ` to the entries. 

### `twistedNorm_diagGL`

 Let `δ = diagGL d` be the invertible diagonal matrix with unit entries `d i`. Its twisted norm
`δ · σ(δ) ⋯ σ^(p-1)(δ)`, with `σ` acting on entries, is diagonal with entries
`∏ l ∈ range p, (σ ^ l) (d i)`. 
