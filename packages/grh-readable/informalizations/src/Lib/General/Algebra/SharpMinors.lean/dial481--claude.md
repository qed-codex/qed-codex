---
{
  "module": "src/Lib/General/Algebra/SharpMinors.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Algebra/SharpMinors.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Algebra/SharpMinors.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Maximal minors and lengths

Let `A` be a matrix over a discrete valuation ring `O` and let `a ≠ 0`. The length of the kernel of
`A` on `(O / a) ^ k` is the least valuation of a maximal minor of the matrix formed by the rows of
`A` and of `a • 1`. The kernel is isomorphic to the module of linear maps to `O / a` from the
quotient of `O ^ k` by these rows, so it has the length of this quotient, which is computed by the
Smith normal form and the multilinearity of the determinant.

* `New.Selmer.maximalMinors`, `New.Selmer.matrixKernel`: the minors and the kernel.
* `New.Selmer.isLeast_length_matrixKernel`: the statement for a matrix over a commutative ring `Λ`
  and a ring homomorphism `ev : Λ →+* O` with `ev a ≠ 0`.

Notions from other files:

* `New.QuotSpan a`: the quotient ring `O / a O`.
* `New.intGL k R`: the invertible matrices that, with their inverses, have entries in the subring
  `R`. The Smith normal form is stated for these, and here `R` is all of `O`.

## Relation to the literature

Known result: Length of a matrix kernel modulo `a` over a discrete valuation ring via maximal
minors. A consequence of the theorem on elementary divisors.


### `maximalMinors`

 The minors of size `card k` of the matrix formed by the rows of `A` and of `a • 1`, where `k`
indexes the columns. The family of rows of `A` may be infinite. A choice of rows with a repetition
is allowed; it contributes the minor `0`. 

### `matrixKernel`

 The kernel of `A` on `B ^ k`, for an `O`-module `B`: the vectors `w` such that
`∑ j, A i j • w j = 0` for every row index `i`. 

### `rowLattice`

 The submodule of `O ^ k` spanned by the rows of `A` and of `a • 1`. 

### `image_maximalMinors`

 A ring homomorphism `ev` maps the maximal minors of the rows of `A` and `a • 1` onto those of
the rows of `A.map ev` and `ev a • 1`. 

### `mem_matrixKernel`

 A vector lies in `matrixKernel A B` exactly if every row of `A` sends it to `0`. 

### `length_matrixKernel_eq_length_linearMap`

 The kernel of `A` on `(O / a) ^ k` (`QuotSpan a` is `O / a`) has the length of the module of
linear maps to `O / a` from the quotient of `O ^ k` by `rowLattice A a`, the span of the rows of
`A` and `a • 1`: a map corresponds to its values at the standard basis. 

### `length_linearMap_quotSpan_of_dvd`

 In a discrete valuation ring let `d ∣ a ≠ 0`. The module of linear maps `O / d → O / a` has
the length of `O / d` (`QuotSpan x` is `O / x`). 

### `length_linearMap_quotSpan`

 Over a discrete valuation ring `O`, a finitely generated module `Q` that `a ≠ 0` annihilates
has the same length as the module of its linear maps to `QuotSpan a`, that is, `O / a`. This
follows from the structure theorem for such modules. 

### `mem_span_row_mul_diagonal_mul_iff`

 A vector is a combination of the rows of `U * diagonal d * V`, with `U` and `V` invertible,
exactly if `d i` divides the coordinate `i` of its product with `V⁻¹` for every `i`. 

### `length_quotient_span_row`

 Elementary divisors: over a discrete valuation ring `O`, the quotient of `O ^ k` by the rows of
a square matrix `N` has the valuation of `det N` as its length. 

### `exists_span_row_eq_rowLattice`

 Over a discrete valuation ring and for `a ≠ 0` the lattice `rowLattice A a` of the rows of
`A` and `a • 1` is free of full rank, so it is spanned by the rows of a square matrix. 

### `dvd_det_of_forall_row_mem_span`

 If every row of the square matrix `N` is a combination of the rows of `M`, then `det N` is a
combination of the determinants of choices of rows of `M`, so each common divisor `x` of these
divides it. 

### `isLeast_length_quotient_rowLattice`

 Over a discrete valuation ring and for `a ≠ 0`, the quotient of `O ^ k` by `rowLattice A a`,
the span of the rows of `A` and `a • 1`, has as its length the least valuation of a maximal minor
of these rows. 

### `isLeast_length_matrixKernel`

 Let `A` be a matrix over `Λ` with columns indexed by `k`, let `ev : Λ →+* O` be a ring
homomorphism to a discrete valuation ring (`[DVR O]`), and let `ev a ≠ 0`. The length of
`matrixKernel (A.map ev) (QuotSpan (ev a))`, the kernel of `A.map ev` on `(O / ev a) ^ k`, is the
least `addVal (ev P)`, where `P` runs over `maximalMinors A a`, the maximal minors of the matrix
formed by the rows of `A` and of `a • 1`. 
