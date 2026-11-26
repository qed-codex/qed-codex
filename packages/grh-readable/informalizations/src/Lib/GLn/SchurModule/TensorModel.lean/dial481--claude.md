---
{
  "module": "src/Lib/GLn/SchurModule/TensorModel.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GLn/SchurModule/TensorModel.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GLn/SchurModule/TensorModel.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The Weyl module inside the tensors of its diagram

A tensor in the product of exterior powers, one factor for each column of the diagram, is written as
a function on the column fillings `New.ColumnFilling`, which index the basis tensors.

* `New.fillingMatrix`: the integral matrix that embeds the Weyl module into tensors. Its row at a
  column filling holds the coordinates, in the standard basis, of the product of minors
  `New.fillingPoly` of that filling.
* `New.fillingMatrixOver_mul_schur`: the Schur matrix of a family of square matrices, one for each
  place `τ`, is the restriction of their action `New.minorsMatrix` on tensors.
* `New.span_fillingPoly`: the products of minors span the module of Borel semi-invariants, whose
  dual is the Weyl module.
* `New.exists_fillingMatrix_leftInverse`: the Weyl module is a direct summand of the integral
  tensors.
* `New.exists_fillingMatrix_mulVec_eq_iff_mem_span`: the Weyl module over `ℤ` consists of the
  integral tensors in the span over `ℚ` of the tensors of rational matrices.

Notions from other files:
* A `Tableau` lists the entries of each column; `tableauPoly R e T` is the product, over the columns
  of the tableau `T`, of the `minor` whose rows are the images under `e` of the entries. Here
  `minor R I` is the determinant of the variables `y` in the rows `I` and the first columns;
  `MatrixPoly ι R` is the ring of polynomials in these variables `y`, indexed by `ι × ℕ` (a row and
  a column number).
* `nablaBasis R n κ`, the standard basis, is a chosen basis of products of minors of the module
  `nablaFamily R n κ`, indexed by `WeylIndexFamily n κ`; `nablaCombination κ` takes a coordinate
  vector to its combination of this basis. A vector of the Weyl module is given by its coordinates
  `WeylIndexFamily n κ → R` in the dual basis.
* `rowSubst z` substitutes `z y` for `y`, and row `i` of `schur κ z` holds the coordinates of
  `rowSubst z` of the basis element `i`; so `schur κ z` acts on the Weyl module.

## Relation to the literature

Known result: the Weyl module over `ℤ` as a direct summand as a ℤ-module of a tensor product of
exterior powers. Source: Akin, Buchsbaum and Weyman, Schur functors and Schur complexes.


### `IncreasingMap`

 The strictly increasing sequences of length `h` in `Fin N`. 

### `det_mul_eq_sum_increasing`

 The Cauchy–Binet formula as a sum over increasing sequences: the determinant of the product of
an `h × N` and an `N × h` matrix is the sum, over the increasing sequences `I` of length `h`, of
the products of the two minors at `I`. 

### `det_sum_smul_X`

 For an `h` by `n τ` matrix `c`, the determinant of `c y`, where `y` consists of the first `h`
columns of the variables at the place `τ`, is the sum over increasing row numbers `I` of the minor
of `c` with columns `I` times the minor of `y` with rows `I`. Here `rankAt n τ` is the number of
elements of `n τ`, and the row numbers are read as elements of `n τ` through their numbering
`rowEquivFin n τ`. 

### `ColumnFilling`

 The index set of the basis tensors for the diagram with `κ τ h` columns of height `h` at `τ`,
for the heights below the rank `rankAt n τ`, the number of elements of `n τ`: an increasing sequence
of `h` row numbers for each column. 

### `fillingRows`

 The tableau of a column filling at `τ`, with row numbers read as rows through `rowEquivFin n τ`,
the numbering of `n τ` by `Fin (rankAt n τ)`. 

### `fillingPoly`

 The product of the minors of the variables on the columns of a filling: a column of height `h`
gives the minor with the rows of its entries and the first `h` columns of variables. 

### `minorsMatrix`

 The matrix by which `z` acts on tensors: the entry at `(T, T')` is the product, over the
columns of the diagram, of the minor of `z τ` with rows from `T` and columns from `T'`, where `τ`
is the place of the column. 

### `minorsMatrix_transpose`

 The action `minorsMatrix` of transposed matrices on tensors is the transpose of the action. 

### `rowSubst_minor_comp_sigmaMk`

 Substituting `z y` for the variables `y` in the minor with rows `J` at the place `τ` gives the
sum, over increasing row numbers `I`, of the minor of `z τ` with rows `J` and columns `I` times the
minor of `y` with rows `I`. 

### `rowSubst_prod_tableauPoly`

 For a family of tableaux `U`, substituting `z y` for the variables `y` in the product of the
minors on the columns of `U` gives the sum over column fillings `T` of the product of minors
`fillingPoly` of `T`, times the product over the columns of the minor of `z τ` with rows from `U`
and columns from `T`, where `τ` is the place of the column. 

### `rowSubst_fillingPoly`

 Substituting `z y` for `y` in the product of minors `fillingPoly` of a column filling `T` gives
the combination of these products with row `T` of the matrix `minorsMatrix` as coefficients. 

### `fillingMatrix`

 The integral matrix of the embedding of the Weyl module into tensors: row `T` holds the
coordinates, in the standard basis, of the product of minors of `T`. 

### `fillingMatrixOver`

 The matrix `fillingMatrix` with its entries mapped into `R`. 

### `nablaCombination_fillingMatrixOver`

 For a column filling `T` (an increasing sequence of rows in each column of the diagram `κ`), the
row `T` of the embedding `fillingMatrixOver` of the Weyl module into tensors is the coordinate
vector of the product of minors `fillingPoly R T`: the map `nablaCombination`, which takes
coordinates to the combination of the standard basis of products of minors, sends it to that
product. 

### `fillingMatrixOver_mulVec_weylEval`

 The embedding `fillingMatrixOver` of the Weyl module into tensors sends the vector `weylEval`,
of the values at `y` of the standard basis of products of minors, to the vector whose coordinate at
a column filling `T` is the value at `y` of the product of minors `fillingPoly R T`. 

### `nablaCombination_transpose_mulVec`

 For a tensor `v`, given by its values on column fillings, the transposed embedding
`(fillingMatrixOver R n κ)ᵀ` takes `v` to the coordinates of the combination with coefficients `v`
of the products of minors `fillingPoly`. Here `nablaCombination` takes coordinates to the
combination of the standard basis of products of minors. 

### `nablaCombination_schur_row`

 For a family `z` of square matrices, `nablaCombination`, which takes coordinates to the
combination of the standard basis, sends row `i` of the Schur matrix `schur κ z` to the basis
polynomial `nablaBasis R n κ i` with `z y` substituted for the variables `y`. 

### `fillingMatrixOver_mul_schur`

 For a family `z` of square matrices, the embedding `fillingMatrixOver` of the Weyl module into
tensors intertwines the Schur matrix `schur κ z`, the action of `z` on the Weyl module, with
`minorsMatrix κ z`, the action of `z` on tensors by products of minors. 

### `span_fillingPoly`

 The module `nablaFamily R n κ` of Borel semi-invariants is the span of the products of minors
`fillingPoly R T` over all column fillings `T`, the coordinates of the tensor of the variables. 

### `exists_fillingMatrix_leftInverse`

 The integral matrix `fillingMatrix`, which embeds the Weyl module of the diagram `κ` (with basis
indexed by `WeylIndexFamily n κ`) into tensors (with basis indexed by column fillings), has an
integral left inverse. So the Weyl module is a direct summand of the integral tensors. 

### `range_fillingMatrixOver_eq_span`

 Over an infinite field `K`, the image of the Weyl module in tensors under `fillingMatrixOver`
is the span of the tensors of the arrays `y` over `K`. The coordinate of the tensor of `y` at a
column filling `T` is the value at `y` of the product of minors `fillingPoly K T`. 

### `exists_fillingMatrix_mulVec_eq_iff_mem_span`

 The Weyl lattice inside the tensors. An integral tensor `v` is the image of an integral vector
of the Weyl module under the embedding `fillingMatrix` if and only if it lies in the span over `ℚ`
of the tensors of rational arrays `y`, whose coordinates are the values at `y` of the products of
minors `fillingPoly`. 
