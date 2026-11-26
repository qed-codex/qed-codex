---
{
  "module": "src/Lib/GLn/SchurModule/LeadingRows.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GLn/SchurModule/LeadingRows.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GLn/SchurModule/LeadingRows.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Fillings whose columns begin with the leading rows

At each place `τ` the rows `n τ`, in the order `rowEquivFin`, are `q τ` leading rows followed by as
many later rows as `m τ` has. A filling of the later rows, for the diagram without its first `q τ`
rows, becomes a filling of all rows: the leading rows go on top of each column, and a column of
height `h < q τ` gets the first `h` rows. The hook number of the smaller diagram times the product
of minors of this filling is the polynomial of an integral vector of the Weyl module.

* `New.leadingWedge`: puts the first `q τ` rows on top of a filling of the later rows.
* `New.aeval_fillingPoly_leadingWedge`: where the top blocks of `y` are invertible, its product of
  minors at `y` is a factor independent of the filling times the product of minors of the given
  filling at the Schur complement of `y`.
* `New.leadingWedgeMatrix_mulVec_weylEval`: the induced map on tensors sends the tensor of the
  evaluation vector at an integer array `y` to that at `diag(1, y)`.
* `New.exists_fillingMatrix_mulVec_eq_leadingWedgeMatrix_mulVec`: hence it maps the smaller Weyl
  module into the larger one.
* `New.exists_toPoly_eq_hookNumber_smul_leadingWedge`: the integrality statement.

The integrality statement follows from `New.GL.exists_toPoly_eq_hookNumber_smul` for the smaller
diagram, carried over by the map of tensors above, and the formula for the determinant of a block
matrix by the Schur complement (`Matrix.det_fromBlocks₁₁`).

Notions from other files:
* `rankAt n τ` is the number of rows at `τ`, and `rowEquivFin n τ` numbers them by
  `Fin (rankAt n τ)`.
* `ColumnFilling n κ`: for each of the `κ τ h` columns of height `h < rankAt n τ`, an
  `IncreasingMap (rankAt n τ) h`, that is a strictly increasing sequence of `h` row numbers.
* `fillingPoly ℤ T`: the product of the minors that the columns of the filling `T` cut out of the
  array of variables `X (row, column)`, as an element of `MatrixPoly`.
* `WeylIndexFamily n κ` indexes the standard basis of the Weyl module for the column counts `κ`,
  `toPoly n κ` sends a coordinate vector in this basis to its polynomial, `fillingMatrix n κ`
  embeds this module into the tensors, and `hookNumber` is the Fock pairing of the product of
  leading minors with itself.

## Relation to the literature

Part of a known result, the branching rule from GL(n+1) to GL(n), for any number of removed rows.


 ### Increasing sequences 

### `strictMono_append_natAdd`

 Let `f` be an increasing sequence of `k` of the numbers below `M` (an `IncreasingMap`). The
numbers below `p`, followed by `p + f 0, p + f 1, …`, form an increasing sequence. 

### `le_val_of_increasingMap`

 In an increasing sequence of numbers below `N` (an `IncreasingMap`), the term of index `a` is at
least `a`. 

### `val_eq_of_forall_exists_val_eq`

 Let `f` be an increasing sequence of `h` numbers below `N` (an `IncreasingMap`) that takes each
value less than both `p` and `h`. Then each term of index less than `p` is equal to its index. 

 ### Putting the leading rows on top 

### `flatColumns`

 The column counts after deleting the first `q τ` rows of the diagram with `κ τ h` columns of
height `h` at the place `τ`: the columns of height `h` are the old columns of height `q τ + h`. 

### `leadingWedge`

 A column filling gives for each column an increasing sequence of row numbers. The filling
`leadingWedge h_rank T` of the rows `n τ` puts the first `q τ` of them on top of each column of a
filling `T` of the later rows `m τ`, and fills each column of height `h < q τ` with the first `h`
rows. 

### `leadingWedge_castAdd`

 Let `T` be a filling of the later rows, where `n τ` has `q τ` rows more than `m τ`. In
`leadingWedge h_rank T`, which puts the first `q τ` rows on top of `T`, a column of height
`h < q τ` is filled with the first `h` rows: its entry of index `s` is `s`. 

### `leadingWedge_natAdd`

 Let `T` be a filling of the later rows, where `n τ` has `q τ` rows more than `m τ`. In
`leadingWedge h_rank T`, which puts the first `q τ` rows on top of `T`, a column of height
`q τ + k` consists of those rows followed by the entries of `T`, shifted by `q τ`. 

### `leadingWedge_injective`

 The map `leadingWedge h_rank`, which puts the first `q τ` rows on top of a filling of the later
rows, is injective: the filling is recovered from the later entries of each column. 

### `mem_range_leadingWedge`

 A filling `U` is in the range of `leadingWedge h_rank`, which puts the first `q τ` rows on top
of a filling of the later rows, if in every column of `U` the entry of index `a < q τ` is row
`a`. 

 ### The Schur complement of the top block 

### `positionEntry`

 The entry of the array `y` in column `t` and in the row of `n τ` whose position, in the order
`rowEquivFin`, is `p`. The first `q τ` positions are the leading rows, the others the later ones. 

### `topBlock`

 The square block of the array `y` in the first `q τ` rows and the first `q τ` columns. 

### `eq_of_aeval_eq_of_isUnit_topBlock`

 Two integral polynomials in the entries of an array (`MatrixPoly`) are equal if, over every
commutative ring, they agree at every array whose top blocks, the squares in the first `q τ` rows
and columns (`topBlock`), are all invertible. 

### `schurComplementArray`

 The Schur complement of the top block: with `y = (A, B; C, D)` and `A` the top block, the array
`D - C A⁻¹ B` of the later rows and columns. The inverse is the adjugate one (`Matrix.inv`), so
this is the true Schur complement only where `A` is invertible. 

### `det_positionEntry_append`

 At the place `τ` the rows are read in the order `rowEquivFin` through `positionEntry`, and the
top block is the one in the first `q τ` rows and columns. If this block of `y` is invertible, the
minor on the first `q τ` rows, the later rows `I` and the first `q τ + k` columns is its determinant
times the minor of the Schur complement (`schurComplementArray`) on the rows `I` and the first `k`
columns. 

### `blockArray`

 The array `diag(1, y)`: an array `y` of the later rows, moved to the later columns and completed
by the unit matrix in the first `q τ` rows and columns. 

### `leadingFactor`

 The product of the leading `h × h` minors of `y` over the columns of height `h < q τ`, times the
determinant of the top block for each column of height `h` with `q τ ≤ h < rankAt n τ`. 

### `aeval_fillingPoly_leadingWedge`

 Let `leadingWedge h_rank T` be the filling that begins each column of height `h` with the first
`min h (q τ)` rows and goes on as the filling `T` of the later rows `m τ`, whose column counts
`flatColumns q κ` are those of the diagram without its first `q τ` rows. At an array `y` with
invertible top blocks, its product of minors `fillingPoly` is the product of minors of `T` at the
Schur complement of the top blocks times `leadingFactor h_rank y κ`, a product of leading minors and
top determinants which does not depend on `T`. 

 ### The tensor of `diag(1, y)` 

### `aeval_fillingPoly_blockArray`

 The product of minors `fillingPoly` of `leadingWedge h_rank T` (the first `q τ` rows on top of
the columns of a filling `T` of the later rows `m τ`, whose column counts `flatColumns q κ` are
those of `κ` without the first `q τ` rows), evaluated at the block array `diag(1, y)`, is the
product of minors of `T` at `y`. 

### `exists_row_eq_of_aeval_blockArray_ne_zero`

 Let `U` be a filling of all rows `n τ`, by their positions. If its product of minors
`fillingPoly` does not vanish at the block array `diag(1, y)`, whose unit block has size `q τ`, then
the column `j` of height `h` of `U` at `τ` holds each row `s < q τ` with `s < h`. 

### `mem_range_leadingWedge_of_aeval_blockArray_ne_zero`

 A filling `U` of all rows `n τ` whose product of minors `fillingPoly` does not vanish at the
block array `diag(1, y)` is `leadingWedge h_rank T` for a filling `T` of the later rows `m τ`: in
each column of height `h` at `τ` it begins with the first `min h (q τ)` rows. 

### `leadingWedgeMatrix`

 The matrix of the map on tensors that sends the basis tensor of a filling `T` of the later rows
to the basis tensor of `leadingWedge h_rank T`. 

### `sum_leadingWedgeMatrix_mulVec_smul`

 For an integral tensor `x` indexed by the fillings of the later rows `m τ`, pairing its image
under `leadingWedgeMatrix` with the products of minors `fillingPoly` is the same as pairing `x` with
the products of minors of the fillings `leadingWedge h_rank T`, which have the first `q τ` rows on
top of the columns of `T`. 

### `fillingMatrix_mulVec_weylEval_int`

 Over the integers, the image under `fillingMatrix n κ` of the evaluation vector `weylEval n κ y`
at an integer array `y` (a vector indexed by `WeylIndexFamily n κ`) has as coordinates the products
of minors `fillingPoly` of the fillings, evaluated at `y`. 

### `leadingWedgeMatrix_mulVec_weylEval`

 Here `fillingMatrix` embeds the Weyl module into tensors, with basis the fillings, and
`weylEval` is its vector of evaluations at an integer array. Putting the first `q τ` rows on top of
the fillings of the rows `m τ` (the map `leadingWedgeMatrix`) sends the tensor of the evaluation
vector at `y`, for the column counts `flatColumns q κ` of the diagram without its first `q τ` rows,
to the tensor of the evaluation vector at `diag(1, y)` for the column counts `κ`. 

### `exists_fillingMatrix_mulVec_eq_leadingWedgeMatrix_mulVec`

 Let `fillingMatrix` be the embedding of the integral Weyl module into tensors. The map
`leadingWedgeMatrix`, which puts the first `q τ` rows on top of the fillings of the later rows
`m τ`, maps the Weyl module for the column counts `flatColumns q κ` (the diagram without its first
`q τ` rows) into that for `κ`: the image of the tensor of every `ζ` is the tensor of some `η`. 

### `exists_toPoly_eq_hookNumber_smul_leadingWedge`

 Let `T₀` be a filling of the later rows `m τ` for the column counts `flatColumns q κ`, that is,
for the diagram without its first `q τ` rows, and let `leadingWedge h_rank T₀` be the filling of all
rows `n τ` that begins each column of height `h` with the first `min h (q τ)` rows and goes on as
`T₀`. Then the product of minors `fillingPoly` of this filling, times the hook number of the smaller
diagram (`hookNumber`, the Fock pairing of its product of leading minors with itself), is the
polynomial `toPoly` of an integral coordinate vector of the Weyl module for `κ`. 
