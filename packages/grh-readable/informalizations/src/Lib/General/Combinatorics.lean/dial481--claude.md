---
{
  "module": "src/Lib/General/Combinatorics.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Combinatorics.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Combinatorics.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The q-binomial theorem, fibre sums, and Schur polynomials in the coefficients

The q-binomial theorem is proved as a sum over the subspaces of a vector space over a field with `q`
elements. There is a lemma on grouping a finite sum by the fibres of a map. Schur polynomials are
defined without division, as integer polynomials in the coefficients of a monic polynomial; `s_l(r)`
denotes the Schur polynomial with exponent tuple `l`, evaluated at a tuple of roots `r`. Three
algebraic facts serve to extract values of Schur polynomials from vanishing linear forms.

## Main definitions and results

* `New.q_binomial_submodule`: the sum of `New.heckePolyCoeff X U` over the subspaces `U` of `W` is
  `New.SiegelWeil.qPochhammer q (dim W) X`.
* `New.Variety.genericSchur`, `New.Variety.rootCoeffEval`: the Schur polynomial in the coefficients,
  and evaluation at the coefficients of the monic polynomial with a given multiset of roots.
* `New.Variety.rootCoeffEval_genericSchur_mul_det`: the value times the Vandermonde determinant is
  `det (r i ^ l j)`.
* `New.Variety.sum_lagrange_smul_rootCoeffEval`: for distinct elements r₁, …, r_a of a field,
  summing s_l(r₁, …, X rᵢ, …) against the Lagrange factors ∏_{k ≠ i} (X rᵢ − r_k)/(rᵢ − r_k)
  gives s_l(r)·∑ⱼ X^(l j).
* `New.Variety.map_prod_rootCoeffEval_eq_zero`: a linear form that kills the families
  j ↦ ∏_{i, σ} ∏_{t ∈ x(j, σ)} (1 − c(i, σ)(α) t) for all α, with the c(i, σ) algebraically
  independent, kills the products over σ of polynomials of bounded degree in the coefficients of
  ∏_{t ∈ x(j, σ)} (X − t).

## Relation to the literature

Known results: the q-binomial theorem, counted over the subspaces of a finite vector space, and the
bialternant formula for Schur polynomials.


 ## The q-binomial theorem over the subspaces of a finite vector space 

### `New.SiegelWeil.qPochhammer`

 The product of `1 - q ^ l * X` over `0 ≤ l < m`. For `q` the norm of a split place, it is the
Hecke polynomial of the trivial representation in rank `m`. 

### `New.heckePolyCoeff`

 The number `(-X) ^ d * q ^ (d choose 2)` attached to a subspace `U` of `k^n` of dimension `d`,
where `q` is the number of elements of `k`. 

### `New.inf_sup_span_singleton_of_covBy`

 If `W` covers `H` in the lattice of subspaces, then a subspace `U ≤ W` is spanned by `U ⊓ H` and
any vector of `U` outside `H`. 

### `New.finrank_eq_finrank_inf_add_one_of_covBy`

 If `W` covers `H` in the lattice of subspaces, then `U ⊓ H` has codimension one in every
subspace `U ≤ W` that is not contained in `H`. 

### `New.sum_inf_eq_sum_of_covBy`

 If `W` covers `H` and `v` is a vector of `W` outside `H`, then `U ↦ U ⊓ H` is a bijection from
the subspaces `U ≤ W` containing `v` onto the subspaces of `H`; stated for sums of a function. 

### `New.q_binomial_submodule`

 The q-binomial theorem for subspaces: for a subspace `W` of `k^n`, with `n` finite and `k` a
field with `q` elements, and for `X : ℂ`, the sum of `(-X) ^ dim U * q ^ (dim U choose 2)`
(`heckePolyCoeff X U`) over the subspaces `U ≤ W` is `∏ l < dim W, (1 - q ^ l * X)`
(`SiegelWeil.qPochhammer q (dim W) X`).

A variant of the finite q-binomial theorem as in Macdonald, with a sum over subspaces in place of
Gaussian binomial coefficients. 

 ## Sums over an image grouped by fibres 

### `New.Variety.finsum_image_eq_zero_of_fibers`

 Let `S` be a finite set and `ψ` a map. If for `t ∈ S` the value `F (ψ t)` divided by the size of
the fibre of `ψ` in `S` through `t` is `G t / D`, and `G` has sum zero over `S`, then `F` has sum
zero over `ψ '' S`. 


## Schur polynomials in the coefficients of a monic polynomial

A Schur polynomial in `a` variables is symmetric, so it is an integer polynomial in the coefficients
of `∏ (X - r i)`. Here it is defined in that form, without division, for any tuple of exponents
`l : Fin a → ℕ` (classically `l j` is a part of a partition plus `j`).


### `genericSchur`

 For exponents `l : Fin a → ℕ`, the determinant of the matrix of coefficients of the remainders
of the `X ^ l j` modulo `freeMonic ℤ a`, the generic monic polynomial of degree `a`. It is an
integer polynomial in the `a` generic coefficients. 

### `rootCoeffEval`

 Evaluation of an integer polynomial in `a` variables at the coefficients of degree less than `a`
of `∏ (X - t)`, with `t` running over the multiset `s`. Applied to `genericSchur l`, with `s` of
size `a`, it gives the value of the Schur polynomial at the roots. 

### `rootCoeffEval_map`

 `rootCoeffEval s`, evaluation at the coefficients of `∏ t ∈ s, (X - t)`, commutes with a ring
homomorphism `f`, applied to the roots. 

### `rootCoeffEval_genericSchur_mul_det`

 The bialternant formula over a domain `R`: the Schur polynomial `genericSchur l`, evaluated at
the coefficients of `∏ (X - r i)`, times the Vandermonde determinant of `r` is the generalised
Vandermonde determinant `det (r i ^ l j)`. 

 ## Extracting Schur polynomials from vanishing linear forms 

### `sum_aeval_lagrange_basis_mul_C_pow`

 Lagrange interpolation of `X ^ j`, for `j < a`, at distinct nodes `r₁, …, r_a`, evaluated at a
polynomial `t`. 

### `sum_lagrange_smul_rootCoeffEval`

 For distinct `r₁, …, r_a` in a field `K` and exponents `l : Fin a → ℕ`, the identity `∑ᵢ
∏_{k ≠ i} (X rᵢ - r_k) / (rᵢ - r_k) · s_l(r₁, …, X rᵢ, …, r_a) = s_l(r) · ∑ⱼ X ^ l j` holds in
`K[X]`. Here `s_l(r)` is `genericSchur l` evaluated by `rootCoeffEval` at the coefficients of
`∏ (T - r_k)`. This is the determinant of the coefficients of the remainders of the `X ^ l j` modulo
that product, so the exponents `l j` play the role of the alternant exponents `λ_j + a - j` of a
Schur polynomial, not of a partition `λ`. 

### `algebraicIndependent_embedding_two_mul`

 For a number field `E` and a type `ι`, the doubled coordinate functions `α ↦ σ (2 * α i)` on
`(𝓞 E)^ι`, indexed by the pairs `(i, σ)` of an index `i: ι` and an embedding `σ` of `E` in `ℂ`, are
algebraically independent over `ℂ`. 

### `map_prod_rootCoeffEval_eq_zero`

 Let the functions `c (i, σ) : A → K` be algebraically independent over `K`, let each polynomial
`q σ` have total degree at most `card ι`, and let each multiset `x j σ` have `a` elements. If a
linear form `L` kills the family `j ↦ ∏_{i, σ} ∏_{t ∈ x j σ} (1 - c (i, σ) α * t)` for every `α`,
then it kills `j ↦ ∏_σ rootCoeffEval (x j σ) (q σ)`, where `rootCoeffEval (x j σ)` evaluates at the
coefficients of `∏_{t ∈ x j σ} (X - t)`. 
