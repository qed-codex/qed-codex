---
{
  "module": "src/Lib/GLn/SchurModule/Polarisation.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GLn/SchurModule/Polarisation.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GLn/SchurModule/Polarisation.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Irreducibility under U(n)^Φ, polarisation and averaging of determinant polynomials

The representations `New.conjWeylRep κ e` of the compact group U(n)^Φ are irreducible, and so is the
module `New.nablaFamily` of semi-invariant polynomials.

## Main definitions and results

* `New.span_conjWeylRep_eq_top`, `New.mem_span_rowSubst_unitary`: irreducibility under U(n)^Φ, for
  coordinate vectors and for semi-invariant polynomials.
* `New.exists_pairedDetProd_eq_sum_unitary`: for `card p < card n`, a product of determinants
  `det (η τ k * Y τ)` is a combination of unitary translates of one product of powers of minors,
  with coefficients independent of `Y`.
* `New.exists_forall_eq_mul_map_det_pow`: a linear form `M` that takes the unitary translates of a
  polynomial `q` in square matrices to `t * ∏ τ, det (u τ) ^ c τ` has
  `t = a * M (∏ τ, det (z τ) ^ c τ)`, with `a` depending only on `q` and `c`.

Notions from other files:
* `New.conjWeylRep κ e`: the action of U(n)^Φ on the coordinate vectors `WeylIndex n κ → ℂ` by the
  Schur matrices of the conjugate matrices, times the powers `e` of their determinants;
  `USign (1 : n → ℤˣ)` is the unitary group U(n).
* `New.nablaFamily`: the module of Borel semi-invariant polynomials in rows (τ,a), coloured by τ,
  whose weight has `κ τ h` columns of height `h` at τ, for the heights below |n_τ|.
* `New.rowSubst`: for matrices z_τ, the substitution f ↦ f(zy).
* `New.pairedDetProd`: the element ∏_τ ∏_k det(η_{τk} Y_τ) of a ℂ-algebra S, for n×p matrices Y_τ
  over S and complex p×n matrices η_{τk}.
* `New.Rows.variableMinor`: the minor det(x_{τ,i(a),j(b)}) of the matrix of variables at τ, in rows
  i and columns j.

## Relation to the literature

Irreducibility under U(n) is part of the known theory of the contravariant form on Weyl's lattice.
See `Lib.GLn.SchurModule.SchurNorm`.



## Irreducibility and polarisation of products of determinants

Let `card p < card n`. A product of `d τ` maximal minors of each `n × p` matrix of variables lies in
the module `New.nablaFamily` whose diagram at `τ` has `d τ` columns of height `card p`. This module
is irreducible under U(n)^Φ, so the unitary translates of one product of powers of minors span it.


### `span_conjWeylRep_eq_top`

 The representation `New.conjWeylRep κ e` of the product over `Φ` of copies of U(n) (`USign 1`),
acting on complex coordinate vectors `WeylIndex n κ → ℂ` (`WeylIndex n κ` indexes a basis of the
Weyl module below, whose dimension is `card (WeylIndex n κ)`) by the matrices `New.conjWeylMatrix`,
is irreducible: the translates of any non-zero vector `v` span the whole space. This is the Weyl
module with `κ τ h` columns of height `h` at `τ`, twisted by the powers `e` of the determinants. 

### `mem_span_rowSubst_unitary`

 The module `New.nablaFamily` of Borel semi-invariant polynomials of weight `κ` is irreducible
under U(n)^Φ: if `f` is a non-zero member (a polynomial in `MatrixPoly (Σ _ : Φ, n) ℂ`, whose
variables are `X (⟨τ, i⟩, t)` with row `(τ, i)` and column `t : ℕ`), each member `g` is a linear
combination of the polynomials `y ↦ f (uᵀ y)` with `u` in U(n)^Φ = `Φ → USign 1`. Here
`New.rowSubst z f` is `y ↦ f (z y)`.

This is Weyl's theorem that the highest weight modules of GL_n(ℂ) are irreducible under the compact
group U(n), for polynomial weights and products of copies of U(n). 

### `map_pairedDetProd`

 An algebra map `φ` carries `pairedDetProd Y η`, the product over `τ` and `k` of the
`det (η τ k * Y τ)`, to the same product for the images of the matrices `Y τ` under `φ`. 

### `pairedDetProd_mem_nablaFamily`

 Let `card p < card n` and let `Y τ` be the `n × p` matrix formed by the first `card p` columns
of the variables at `τ`, numbered by `equivFin p`. The product `pairedDetProd Y η` of the
`det (η τ k * Y τ)` lies in the module `New.nablaFamily` of Borel semi-invariants whose diagram at
`τ` has `card (ι τ)` columns of height `card p`. 

### `rowSubst_pairedDetProd_X`

 Let `Y τ` be the `n × p` matrix formed by the first `card p` columns of the variables at `τ`,
numbered by `equivFin p`. The substitution `rowSubst z` of `z y` for `y` takes `pairedDetProd Y η`,
the product of the `det (η τ k * Y τ)`, to the product of the `det (η τ k * z τ * Y τ)`. 

### `exists_pairedDetProd_eq_sum_unitary`

 Polarisation. Let `card p < card n`, and let `η₀` be the `p × n` matrix whose row `k` is the
standard basis vector at `r k`, for an injective `r`. For all complex `p × n` matrices `η τ k`, the
product `pairedDetProd Y η` of the `det (η τ k * Y τ)` is a finite combination of the products
`∏ τ, det (η₀ * (u τ)ᵀ * Y τ) ^ card (ι τ)` with `u τ` unitary (`USign 1` is U(n)). The
coefficients do not depend on the matrices `Y τ` or on the algebra `S` that holds their entries. 


## Averaging polynomials in square matrices

A tuple `u` of unitary matrices carries a polynomial `q (z)` to `q (uᵀ z)`.


### `exists_forall_map_eq_integral_translate`

 The mean over U(n)^Φ (here `Φ → USign 1`), with a continuous weight `w`, of the translates
`q (uᵀ z)` of a polynomial `q` in square matrices `z τ` is a polynomial: there is one whose value
under each linear form `M` is the integral of `w u * M (q (uᵀ z))` for the Haar probability measure
`volume`. 

### `eq_smul_det_pow_of_unitary`

 A polynomial `f` in square matrices whose value at `xᵀ` is `a * ∏ τ, det (x τ) ^ c τ` for all
`x` in U(n)^Φ = `Φ → USign 1` is `a * ∏ τ, det (z τ) ^ c τ`, where `det (z τ)` is
`variableMinor τ id id`. 

### `exists_forall_eq_mul_map_det_pow`

 Averaging over U(n)^Φ = `Φ → USign 1`. Let `q` be a polynomial in square matrices `z τ`. There
is a number `a` such that every linear form `M` with `M (q (uᵀ z)) = t * ∏ τ, det (u τ) ^ c τ` for
all unitary `u` has `t = a * M (∏ τ, det (z τ) ^ c τ)`. Here `t = M q`, by `u = 1`, and `det (z τ)`
is `variableMinor τ id id`. 
