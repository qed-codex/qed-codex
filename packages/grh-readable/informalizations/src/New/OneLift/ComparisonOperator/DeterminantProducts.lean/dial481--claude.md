---
{
  "module": "src/New/OneLift/ComparisonOperator/DeterminantProducts.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/ComparisonOperator/DeterminantProducts.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/ComparisonOperator/DeterminantProducts.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Products of determinants and first-column coordinates under substitution

This file studies polynomials in the entries of variable matrices `x_τ`, one for each `τ : Φ`, with
rows indexed by `N` and columns by `L`. It studies how these polynomials transform under the
two-sided linear substitutions `New.Rows.twoSidedSubst`, `x_τ ↦ c_τᵀ x_τ g_τᵀ`. It treats products
of determinants of constant matrices stacked over `x_τ`. It also treats the coordinates of a
polynomial in its first `p` columns, where `p` is a number of columns.

## Main definitions and results

* `New.Rows.stackedDetProd`, `New.Rows.twoSidedSubst_stackedDetProd`: a product of determinants of
  constant matrices stacked over `x_τ` (`New.Rows.stackedDet`). The substitution sends the product
  for the matrices `M τ k * (g τ)ᵀ` to a scalar multiple of the product for the matrices `M τ k`.
* `New.Rows.firstColsCoord`, `New.Rows.twoSidedSubst_firstColsCoord`: the coordinates of a
  polynomial in its first `p` columns; if the substitution with column matrices
  `fromBlocks 1 0 0 (g τ)` (fixing the first `p` columns) sends `F'` to a multiple of `F`, the
  coordinates of `F'` and `F` are related by the Schur matrix (`New.schur`).

Notions from other files:
* `New.nablaBasis`, `New.schur`: products of minors indexed by families of standard fillings
  (`New.WeylIndexFamily`), and the matrix of a substitution of rows in these polynomials.


### `New.exists_det_fromCols_eq_mul_det`

 Let `Z` be a complex matrix with rows indexed by `L` and columns by `N`, and let `e` identify
`L` with `a ⊕ N`. There are a matrix `Y` and a constant `γ` such that for all `X` the determinant
of the square matrix `(X | Z)`, with columns ordered by `e`, is `γ * det (Y X)ᵀ`. 

### `twoSidedSubst`

 The substitution `x_τ ↦ c_τᵀ x_τ g_τᵀ` on complex polynomials in the entries of `N × L`
matrices `x_τ`. 

### `inFirstCols`

 Rewrites a polynomial in matrix entries `x_{τ,i,j}` as a polynomial in the first `p` columns,
with coefficients polynomials in the entries of the columns indexed by `L`. 

### `stackedDetProd`

 The product over `τ` and `k` of the determinants of `M τ k` stacked over the variable matrix
`x_τ` (`New.Rows.stackedDet`), columns ordered by `e`. 

### `twoSidedSubst_stackedDetProd`

 Write `det (A; x_τ)` for the determinant of a constant matrix `A` stacked over the variable
matrix `x_τ`; `stackedDetProd` is a product of these. Substituting `x_τ ↦ c_τᵀ x_τ g_τᵀ` in the
product of the `det (M τ k * g_τᵀ; x_τ)` gives the product of the `det (M τ k; x_τ)`, each factor
at `τ` multiplied by `det c_τ * det g_τ`. 

### `firstColsCoord`

 The coordinate `l` of `F` in the first `p` columns: regard `F` as a polynomial in these
columns (`New.Rows.inFirstCols`), pair it with the basis polynomial `l` of weight `κ` (a product of
minors, `nablaBasis`) by the form `⟨P, Q⟩ = P(∂) Q (0)` (`fockPairing`) and divide by the hook
number. This is the integer `⟨f, f⟩` for the product `f` of the leading principal minors with
exponents `κ`, at the ranks `rankAt (fun _ ↦ N) τ = card N`. The result is a polynomial in the
entries of the columns `L`. If `F` is the polynomial (`toPoly`) of a vector `ζ (z)` of the Weyl
module of weight `κ`, with `z` the columns `L`, these are the coordinates of `ζ (z)`. 

### `twoSidedSubst_firstColsCoord`

 Let `F`, `F'` be polynomials in the entries of matrices `x_τ` with columns `Fin p ⊕ L`, and
suppose that the substitution `x_τ ↦ c_τᵀ x_τ diag(1, g_τ)ᵀ` (`twoSidedSubst`) sends `F'` to
`s • F`. Let `b_l` be the products of minors of weight `κ` in the first `p` columns (`nablaBasis`),
indexed by families `l` of standard fillings. The coordinate `firstColsCoord κ F l` is the Fock
pairing of `F` with `b_l` in these columns, divided by the hook number; it is a polynomial in the
entries `z_τ` of the columns `L`. The Schur matrix is given by
`b_l (c y) = ∑ l', schur κ c l l' * b_l' (y)`. Then the combination of the coordinates of `F'` by
its row `l` goes to `s` times the coordinate `l` of `F` under `z_τ ↦ c_τᵀ z_τ g_τᵀ`. 
