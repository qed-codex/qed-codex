---
{
  "module": "src/Lib/General/LinearAlgebra/MinorProducts.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/LinearAlgebra/MinorProducts.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/LinearAlgebra/MinorProducts.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Products of principal minors, Fischer's inequality and the Cauchy–Binet formula

For an integer vector `w` and an invertible complex matrix `x`, m_w(x) = `New.weightMinors w x` is
the product over all integers `t` of the principal minors `New.principalMinor` of `x` on
`{i | t ≤ w i}`. The factors with `t ≤ 0` are divided by `x.det`. The file develops the calculus of
m_w and the closure properties of the invertible triangular matrices `New.IsBorelMatrix o`.

## Main definitions and results

* `New.weightMinors_eq_det_zpow_mul_prod`: the finite form `x.det ^ a * ∏_{a < t ≤ b}` of minors,
  when `a ≤ w ≤ b`.
* `New.fischer_det_inequality`: for a positive semidefinite matrix in 2×2 block form,
  |det z| ≤ |det z₁₁| · |det z₂₂|.
* `New.fischer_inequality`: for positive semidefinite z, the principal minor
  (`New.principalMinor`) on a disjoint union of two index sets is at most, in absolute value, the
  product of the two principal minors.
* `New.hadamard_det_inequality`: for positive semidefinite z, |det z| is at most the product of
  the |z_ii|.
* `New.det_mul_eq_sum_minors`: the Cauchy–Binet formula.
* `New.det_fromCols_eq_sum_minors`, `New.sum_norm_det_fromCols_sq_le`: the Laplace expansion along
  a block of columns and a bound for its complementary minors.



## The products m_w of principal minors and invertible triangular matrices

The matrices with `New.IsBorelMatrix o` (invertible, `b i j = 0` when `o j < o i`) are closed under
products and inverses. For injective `o` their diagonal entries are non-zero and multiply.


 ### The functions `New.weightMinors w` 

### `DiscreteSeries.neg_sum_abs_le_and_le_sum_abs`

 Every entry `w i` of an integer vector lies between `-∑ j, |w j|` and `∑ j, |w j|`, so these
two sums can serve as the bounds `a`, `b` in `New.weightMinors_eq_det_zpow_mul_prod`. 

### `weightMinors_neg`

 For invertible `x`, the product of principal minors `weightMinors` for the weight `-w` at `x` is
the one for `w` at `x⁻¹`. 

### `weightMinors_eq_det_zpow_mul_prod`

 For invertible `x` and integers `a`, `b` with `a ≤ w i ≤ b` for all `i`: the product of
principal minors `m_w(x) = weightMinors w x` is `x.det ^ a` times the product over the levels
`a < t ≤ b` of the principal minor of `x` on `{i | t ≤ w i}`. 

### `analyticAt_weightMinors`

 The product of principal minors `m_w` is complex analytic at every invertible matrix. 

### `weightMinors_add_ite`

 For invertible x, an integer c ≥ 0 and a set p of indices with w_j ≤ w_i for i in p, j not
in p: adding c to the entries of w on p multiplies m_w(x) = `weightMinors w x` (the product over
the levels t of the principal minors on {i | t ≤ w i}, normalised by det x) by the c-th power of
the principal minor on p. 

### `DiscreteSeries.weightMinors_ite_eq_zpow`

 For invertible `x` and `c ≥ 0`, the weight that is `c` on `p` and `0` elsewhere gives the
`c`-th power of the principal minor on `p`. 

### `weightMinors_diagonal_mul`

 For invertible `x` and a diagonal matrix with non-zero entries `d i`, multiplying `x` by the
diagonal on the left multiplies the product of principal minors `weightMinors w x` by
`∏ i, d i ^ w i`. 

 ### Invertible triangular matrices 

### `DiscreteSeries.det_eq_prod_diag_of_blockTriangular`

 A matrix that is block triangular for an injective `o` (so with blocks of size one) has as
determinant the product of its diagonal entries. 

### `IsBorelMatrix.mul_apply_diag`

 For injective `o`, diagonal entries of matrices with `New.IsBorelMatrix o` multiply. 

 ## Fischer's inequality for principal minors of positive semidefinite matrices 

### `New.fischer_det_inequality`

 Fischer's inequality: for a positive semidefinite complex matrix z in 2×2 block form,
|det z| ≤ |det z₁₁| · |det z₂₂|, with z₁₁, z₂₂ the diagonal blocks. 

### `New.fischer_inequality`

 **Fischer's inequality.** Let `z` be positive semidefinite and let the index set `r` be the
disjoint union of `p` and `q`. Then the principal minor of `z` on `r` has norm at most the product
of the norms of the principal minors on `p` and `q`. 

### `New.hadamard_det_inequality`

 Hadamard's inequality: for a positive semidefinite complex matrix z, |det z| is at most the
product of the |z_ii|.

A weaker form of Hadamard's inequality as in Horn and Johnson, omitting the equality case. 


## Expansions in minors

The Cauchy–Binet formula and the Laplace expansion of a determinant along a block of columns, both
read off from the standard basis of an exterior power, and a bound for the complementary minors of
the Laplace expansion by the Cauchy–Binet formula and Hadamard's inequality.


### `enumSubset`

 The elements of a set of `k` indices (`S : Set.powersetCard I k`) in increasing order. 

### `alternatingMap_eq_sum_minors`

 The value of an alternating form `f` in `k` vectors at the columns of `X` is the sum over the
`k`-sets `S` of rows (listed in increasing order by `enumSubset S`) of the minor of `X` on `S` times
the value of `f` at the basis vectors of `S`. 

### `det_mul_eq_sum_minors`

 The Cauchy–Binet formula: the determinant of `A * X`, with `k` rows in `A` and `k` columns in
`X`, is the sum over the `k`-sets `S` of inner indices (listed in increasing order by
`enumSubset S`) of the products of the minors of `X` and `A` on `S`. 

### `exists_alternatingMap_det_fromCols`

 The determinant of the matrix with columns `(Y Z)`, made square by `e`, is an alternating form
in the `k` columns of `Y`. 

### `det_fromCols_eq_sum_minors`

 The Laplace expansion along the first `k` columns, when these are combinations, with
coefficients `X`, of the unit columns at the rows `r`. Here `e` identifies the index set `L` with
these `k` columns followed by those of `Z`, and `enumSubset S` lists a `k`-set `S` in increasing
order. The determinant is the sum over `S` of the minor of `X` on `S` times the determinant with
the unit columns at `r ∘ enumSubset S` in place of the first `k` columns. 

### `norm_det_fromCols_one_submatrix`

 If `ι` and `t` together enumerate the rows, a determinant with unit columns on `ι` has the
modulus of the minor of `Z` on the rows `t`. 

### `sum_norm_det_fromCols_sq_le`

 The complementary minors in the Laplace expansion have squared moduli with sum at most the
product of the squared lengths of the columns of `Z`. Here `e` identifies the index set `L` with
`k` columns followed by those of `Z`, and the `k` unit columns are at the rows `r ∘ enumSubset S`,
the images under the embedding `r` of the `k`-set `S` in increasing order. 
