---
{
  "module": "src/Lib/General/LinearAlgebra/HermiteForm.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/LinearAlgebra/HermiteForm.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/LinearAlgebra/HermiteForm.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Hermite forms over valuation pairs and integral matrices over valued fields

We reduce the columns and rows of matrices over a ring `A` by invertible matrices over a subring
`R`, under the hypothesis `New.IsValuationPair`. It says that any two elements `a, b` of `A` are
`R`-multiples of `a - e * (a - b)` for some idempotent `e` of `R`. It holds for a valuation domain
`A` with `R = ⊤`. For a field with a valuation into `ℤᵐ⁰`, we bound the entries of matrix products
and give a determinant test for integral invertible matrices.

## Main definitions and results

* `New.IsValuationPair.hermite`: Hermite form `y = U_ι * D` with `U ∈ GL_n(R)`, `D` block
  triangular.
* `New.IsValuationPair.exists_isPrimitiveMatrix_mul`: a matrix with a left inverse becomes primitive
  (`New.IsPrimitiveMatrix`) after multiplication by an invertible block triangular matrix.
* `New.IsValuationPair.exists_mul_clear_cols`: the transposed form, clearing the columns outside
  the image of `ι`.
* `New.mem_intGL_iff_det`: `g` lies in `New.intGL n 𝒪[F]` (the image of `GL n 𝒪[F]` in `GL n F`) iff
  its entries are integral and `v (det g) = 1`.

Notions from other files:
* `New.intGL n R`: the subgroup `GL_n(R)` of `GL_n(A)` of matrices that have their entries and
  those of their inverse in the subring `R`.
* `New.transvectionGL`: for distinct indices `i, j` and `a` in `A`, the element `1 + aE_{ij}` of
  `GL_n(A)`, with inverse `1 − aE_{ij}`.
* `New.IsPrimitiveMatrix R X`: `X` has entries in `R` and a left inverse with entries in `R`.

## Relation to the literature

The property `New.IsValuationPair` and the Smith normal form are in
`Lib.General.LinearAlgebra.IntegralLattices`.



## Hermite forms over valuation pairs

`New.intGL` is `GL_n(R)` inside `GL_n(A)`; `wt` orders the columns, and an embedding `ι` picks the
pivot row of each column.


### `transvectionGL_mem_intGL`

 The transvection `1 + a E_{ij}` with `a` in the subring `R` lies in `GL_n(R)`. 

### `isValuationPair_top`

 A valuation domain `A` with the subring `R = ⊤` is a valuation pair: any two elements `a`, `b`
are multiples of `a - e * (a - b)` for some idempotent `e`. 

### `IsValuationPair.exists_row_op`

 Let `(A, R)` be a valuation pair: any `u, v` in `A` are `R`-multiples of `u - e * (u - v)` for
some idempotent `e` of `R`. For rows `i₀ ≠ i` of a matrix `y` over `A` and a column `a`, some `W`
in `GL_n(R)` makes the entry `(i, a)` of `W * y` zero, changes no row other
than `i₀` and `i`, and changes no column in which both rows vanish. 

### `IsValuationPair.exists_clear_col`

 Let `(A, R)` be a valuation pair (any `u, v` in `A` are `R`-multiples of `u - e * (u - v)` for
some idempotent `e` of `R`). For a matrix `y` over `A`, a column `a`, a row `i₀` and a
finite set `t` of other rows, some `W` in `GL_n(R)` makes the entries of `W * y` in column `a` and
rows `t` zero, and changes no column in which `i₀` and all rows in `t` vanish. 

### `IsValuationPair.hermite`

 Hermite form: let `(A, R)` be a valuation pair (any `u, v` in `A` are `R`-multiples of
`u - e * (u - v)` for some idempotent `e` of `R`), and let `ι` embed `k` in `n`.
Then an `n × k` matrix `y` over `A` is `U_ι * D` with `U ∈ GL_n(R)` and `U_ι` its columns at `ι`.
Here `D` is the rows at `ι` of `U⁻¹ * y`, and it is block upper triangular for the weight `wt`. 

### `IsValuationPair.exists_isPrimitiveMatrix_mul`

 If (A, R) satisfies `New.IsValuationPair` (any u, v in A are R-multiples of u - e(u - v) for
some idempotent e of R) and the n × k matrix X over A has a left inverse, there is an invertible
b, block upper triangular for wt, such that X b has entries in R and a left inverse with entries
in R. 

### `IsValuationPair.exists_mul_clear_cols`

 Transposed Hermite form: if the subring R of A satisfies `New.IsValuationPair` (any u, v in A
are R-multiples of u - e(u - v) for some idempotent e of R), then for a k×n matrix M over A and an
injection ι: k → n, some V in GL_n(R) makes the columns of MV outside the image of ι vanish.

A weaker form of the Hermite normal form, without triangular shape, normalised pivots or
uniqueness. 


## Integral invertible matrices

A fact on matrices over a field `F` with a valuation `v` into `ℤᵐ⁰`, written multiplicatively
(`v x ≤ 1` on the integers `𝒪[F]`): a determinant test for membership in `GL_n(𝒪[F])`.


### `New.v_matrix_mul_le`

 Let `F` be a field with a valuation into `ℤᵐ⁰`. If every entry of `A` has valuation at most `c`
and every entry of `B` has valuation at most `d`, then every entry of `A * B` has valuation at most
`c * d`. 

### `New.mem_intGL_iff_det`

 Over a field F with a valuation v into ℤᵐ⁰, an invertible matrix g lies in GL_n(𝒪_F) if and
only if all its entries have valuation at most 1 and v(det g) = 1. 
