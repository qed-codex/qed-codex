---
{
  "module": "src/Lib/GLn/SchurModule/SchurOrthogonality.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GLn/SchurModule/SchurOrthogonality.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GLn/SchurModule/SchurOrthogonality.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Algebraic representations of GL(n) on unitary groups: Schur orthogonality

A weight `(κ, e)` consists of the numbers `κ τ h` of columns of height `h` and an exponent `e τ` of
the determinant. Only the heights below `card n` enter the index type `New.WeylIndex n κ` and, for
square matrices, `New.schur`. `New.weylRep κ e g` is `∏ τ, det (g τ) ^ e τ` times `schur κ g`. These
representations are restricted to products of unitary groups `U(s)^Φ`. The file defines the
hermitian Gram form, which is invariant when all signs are `1` (`New.gramForm_conjWeylRep`, in
`Lib.GLn.SchurModule.SchurNorm`), and the highest vectors.

## Main definitions and results

* `New.conjWeylMatrix`, `New.conjWeylRep`: the conjugate action of weight `(κ, e)`, as matrices and
  as a representation: `g` acts by `New.weylRep κ e` at the entrywise complex conjugate of `g`.
* `New.gramForm`: the hermitian form `ξ* G η` of the Gram matrix `G = weylGramOver`.
* `New.decreasingPosition`, `New.highestVector`: the order that a vector `l` puts on the rows, and
  the evaluation vector at the frame of that order.
* `New.weylRep_coeff_eq_prod_weightMinors`: the matrix coefficient of `New.weylRep κ e` at a highest
  vector is a product of the functions `New.weightMinors`, products of principal minors.
* `New.schur_orthogonality`: Schur's orthogonality relations on the compact group U(n)^Φ.

Notions from other files:
* `New.schur`: The Schur matrix S_κ(z) of matrices z_τ of size n'_τ×n_τ. Row i holds chosen
  coordinates of b'_i(zy) in the family b_j(y)·∏_τ det(y_τ)^{d_τ}. Here b'_i and b_j are the
  standard basis polynomials in the rows n' and n, and d is given by `New.schurDetExp`.
* `New.WeylIndex`: The type of families of chosen standard fillings over the places, in the case
  where the row type is the same finite type n at every place, that is
  `WeylIndexFamily (fun _ ↦ n) κ`; `WeylIndexFamily` allows a row type n_τ at each place τ.
* `New.nablaBasis`: For a family i of chosen standard fillings, the polynomial b_i, the product over
  the places τ of the minor products of the fillings i_τ.
* `New.weylEval`: For an array y, the vector of the values b_i(y).
* `New.weightMinors`: For a matrix `g` and integer weights `l`, the product over integers `t` of the
  principal minor of `g` on `{i | t ≤ l i}`, each factor with `t ≤ 0` divided by `det g`.

## Relation to the literature

Known; see `Lib.GLn.SchurModule.SchurNorm` and `Lib.GLn.SchurModule.MinorBasis` for sources.



## The conjugate representation, Gram form and highest vector

* `New.hcParameter`, `New.IsHCParam`: twice the Harish-Chandra parameter of a weight.
* `New.Exchange.schur_eq_one`: the Schur matrix when all columns have full height.


### `conjWeylMatrix`

 The matrix representation of the product over places of the unitary groups of the diagonal
form of signs s: g acts by `New.weylRep` at the entrywise complex conjugate of g. 

### `conjWeylRep`

 The complex linear representation of the product over places of the unitary groups of signs
s on coordinate vectors of weight κ, acting by the matrices `New.conjWeylMatrix`. 

 ### Highest vector and Harish-Chandra parameter 

### `decreasingPosition`

 For an integer vector l and an index i, the number of indices j with l_j > l_i. 

### `highestVector`

 The complex evaluation vector of weight κ at the array with entry 1 in row a of block w
exactly in column #{j : l_w(j) > l_w(a)}, and 0 elsewhere. 

### `hcParameter`

 The integer 2μ_p + N − 1 − 2p, entry p (counted from 0) of twice the Harish-Chandra parameter
μ + ρ in rank N, where μ_p = e_w + Σ_{p<h<N} κ_w(h) is the highest weight at the place w; the sum is
`diagramWeight (fun _ ↦ N) κ (w, p)`. 

### `IsHCParam`

 `l` lists twice the Harish-Chandra parameter of the weight `(κ, e)`, in some order: at each
place `w` the numbers `l w i` are distinct, and each of them is `hcParameter κ e (card n) w p` for
some position `p < card n`. As `hcParameter` is strictly decreasing in `p`, the position of `i` is
necessarily `decreasingPosition (l w) i`, the number of `j` with `l w i < l w j`. 

### `gramForm`

 The sesquilinear form (ξ,η) ↦ ξ* G η on complex coordinate vectors of weight κ, conjugate
linear in ξ, with G the integer Gram matrix. 

### `gramForm_apply`

 The Gram form at `ξ` and `η` is `ξ* G η` for the Gram matrix `G = weylGramOver`. 

### `Exchange.nablaBasis_eq_one`

 If all columns of `κ` have height `card n` (`κ τ k = 0` for `k ≠ card n`), every basis
polynomial `nablaBasis R _ κ j` is the empty product `1`. 

### `Exchange.schur_eq_one`

 If all columns of `κ` have height `card n` (`κ τ k = 0` for `k ≠ card n`), the Schur matrix of
every tuple `z` of square matrices is the `1 × 1` identity matrix. 


## Matrix coefficients and Schur's orthogonality relations on U(n)^Φ

* `New.exists_intertwining_mean`: averaging a matrix over a compact group gives an intertwiner.


### `instance : Nonempty (WeylIndex n κ)`

 The index type `WeylIndex n κ` is never empty: it indexes the coordinates of a vector of norm
one. 

### `star_highestVector`

 For any integer labels `l w : n → ℤ` of the rows at each place `w`, `highestVector κ l` is the
complex evaluation vector of weight `κ` at the array whose block `w` has entry 1 in row `a` exactly
at column `#{j : l w j > l w a}`, and 0 elsewhere. This highest vector has real (integer)
coordinates: it is its own complex conjugate. 

### `conj_gramForm`

 The form `gramForm` is hermitian: swapping the arguments conjugates the value. 

### `ext_gramForm_left`

 The Gram form is non-degenerate: a vector is determined by its pairings with all vectors. 

### `exists_equiv_decreasingPosition`

 For injective l, the position in decreasing order is a bijection onto {0, …, |n| − 1}, and
that for −l is the reversed one. 

### `continuous_conjWeylRep`

 For each vector `ξ`, the map `g ↦ conjWeylRep κ e g ξ` is continuous on the product of unitary
groups of signs `s`. 

### `exists_intertwining_mean`

 For matrix representations S, R of a compact group with a Haar measure ν and a matrix M such
that g ↦ S(g)MR(g⁻¹) is continuous, there is B with BR(y) = S(y)B for all y and ∫ L(S(g) M R(g⁻¹))
dν = L(B) for every linear L. 

### `weightMinors_add_sum_ite`

 The function `weightMinors` for the weight `c + ∑ h ∈ t, k h • 1_{p < h}` at an invertible
matrix `x`: `x.det ^ c` times the product of the principal minors on `{i | p i < h}` to the powers
`k h`. 

### `weylRep_coeff_eq_prod_weightMinors`

 Let v be the evaluation vector of weight κ at the array `permArray` with entry 1 in row i of
block τ exactly in column p_τ(i), for bijections p_τ : n_τ ≃ Fin (rankAt n τ), so rankAt n
τ = |n_τ|. Let ρ = `New.weylRep` of weight (κ, e) and μ = `New.diagramWeight`. For g in ∏_τ GL(n_τ,
ℂ), the coefficient (v, ρ(g)v) for the bilinear Gram form is the product over τ of
`New.weightMinors` at g_τ for the weight i ↦ e_τ + μ(τ, p_τ(i)). 

### `schur_orthogonality`

 Schur orthogonality for the representation ρ = `New.conjWeylRep` of weight (κ, e) of the compact
group U(n)^Φ: for f linear into ℂ and any vectors a, b, c, ∫ ⟨a, ρ(x⁻¹)b⟩ f(ρ(x)c) dx = (dim ρ)⁻¹
⟨a, c⟩ f(b), with ⟨·,·⟩ = `New.gramForm`, and dx the Haar measure `volume`, of total mass one. 

### `gramForm_highestVector_self`

 For integer labels `l w : n → ℤ` of the rows at each place `w`, `highestVector κ l` is the
complex evaluation vector of weight `κ` at the array whose block `w` has entry 1 in row `a` exactly
at column `#{j : l w j > l w a}`, and 0 elsewhere. If each `l w` is injective, this highest vector
v⁺ is a unit vector for `gramForm`, the form `(ξ, η) ↦ ξ* G η` with `G` the integer Gram matrix:
⟨v⁺, v⁺⟩ = 1. 
