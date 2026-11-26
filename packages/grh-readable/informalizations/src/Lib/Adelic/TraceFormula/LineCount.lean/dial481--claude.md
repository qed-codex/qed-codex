---
{
  "module": "src/Lib/Adelic/TraceFormula/LineCount.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/TraceFormula/LineCount.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/TraceFormula/LineCount.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Lines and hyperplanes over a field

This file describes the stabilisers in `GL_n` of the line of a basis vector `e_i` and of the
complementary coordinate hyperplane. Over a finite field it counts the linear forms with value `1`
at `e_i`, and those with value `1` both at `e_i` and at a vector off its line. It shows that `0`
is a simple root of the characteristic polynomial of a matrix of block shape `(0 ∗; 0 g')`
with `g'` invertible.

Notions from other files:
* `parabolic lev`: the subgroup of `GL_n` of the matrices `g` with `g a b = 0` whenever
  `lev b < lev a`. The two stabilisers use level functions with values in `Prop`, ordered by
  implication.

## Relation to the literature

Standard linear algebra.


 ### Stabilisers and counts 

### `prop_lt_iff_not_and`

 In the order of propositions by implication, `p < q` says that `q` holds and `p` does not. 

### `mem_parabolic_iff_blockTriangular`

 An element lies in `parabolic lev` exactly when its matrix is block triangular for `lev`. 

### `mem_parabolic_ne`

 An element `g` lies in `parabolic (· ≠ i)`, the block triangular matrices for the levels
`(· ≠ i)`, exactly when `g j i = 0` for all `j ≠ i`: the group is the stabiliser of the line of
`e_i`. 

### `mem_parabolic_eq`

 An element `g` lies in `parabolic (· = i)`, the block triangular matrices for the levels
`(· = i)`, exactly when `g i j = 0` for all `j ≠ i`: the group is the stabiliser of the hyperplane
spanned by the `e_j`, `j ≠ i`. 

### `exists_eq_smul_single_iff`

 A vector is a multiple of `e_i` exactly when its other coordinates vanish. 

### `inv_mul_mem_parabolic_ne`

 The elements `g` and `h` have the same left coset of `parabolic (· ≠ i)`, the stabiliser of
the line of `e_i`, exactly when `h e_i` lies on the line of `g e_i`. 

### `mul_inv_mem_parabolic_eq`

 The elements `g` and `h` have the same right coset of `parabolic (· = i)`, the stabiliser of
the hyperplane `z i = 0`, exactly when the `i`-th row of `h` is a multiple of that of `g`. 

### `diag_ne_zero_of_col`

 If the `i`-th column of an invertible `g` vanishes off the diagonal, then `g i i ≠ 0`. 

### `diag_ne_zero_of_row`

 If the `i`-th row of an invertible `g` vanishes off the diagonal, then `g i i ≠ 0`. 

### `det_updateCol_one`

 Replacing the `j`-th column of the identity matrix by `z` gives determinant `z j`. 

### `det_updateRow_one`

 Replacing the `j`-th row of the identity matrix by `z` gives determinant `z j`. 

### `exists_col_eq`

 Every non-zero vector is the `i`-th column of an invertible matrix. 

### `card_fiber_mul_card`

 Every fibre of a surjective homomorphism `A → B` of finite groups has `#A / #B` elements. 

### `card_forms_missing_line`

 Over a field of `q` elements and in dimension `n` there are `q ^ (n - 1)` hyperplanes that do
not contain `e_i`. Each of them is the kernel of one linear form `ξ` with `ξ e_i = 1`, and these
forms are counted. 

### `card_forms_taking_one_at_two_vectors_mul_sq`

 Over a field of `q` elements and in dimension `n`, if `z j ≠ 0` for some `j ≠ i`, so that `z`
is off the line of `e_i`, then there are `q ^ (n - 2)` linear forms with value `1` at `e_i` and at
`z`. 

### `card_line`

 Over a field of `q` elements, the line of `e_i` has `q` elements. 

### `sum_forms_sum_eq_sum_card_smul`

 For a vector `z` let `N z` be the number of forms `ξ` with `ξ e_i = 1` and `ξ z = 1`. The sum
of `f z` over the pairs `(ξ, z)` with `ξ e_i = 1` and `ξ z = 1` is the sum of `N z • f z` over all
vectors `z`. 

### `card_forms_eq_zero_of_ne_single`

 A multiple `z ≠ e_i` of `e_i` has value `1` under no form `ξ` with `ξ e_i = 1`. 

### `sum_ne_zero_eq_smul_add_sum_compl_line`

 If `f` has the value `y` at the non-zero multiples of `e_i`, then its sum over the non-zero
vectors is `(q - 1) • y` plus its sum off the line of `e_i`, over a field of `q` elements. 

### `sum_sum_dotProduct_eq_one_eq_smul`

 Over a field of `q` elements and in dimension `n`, let `f` have the value `y` at the non-zero
multiples of `e_i`. Then the sum of `f z` over all forms `ξ` with `ξ e_i = 1` and all vectors `z`
with `ξ z = 1` is `q ^ (n - 2)` times the sum of `y` and all `f z` with `z ≠ 0`. Here `ξ` stands
for a hyperplane that does not contain `e_i`, and `z` for a line outside this hyperplane. 

 ### Matrices that keep a line 

### `KeepsLine`

 The matrix `M` has the block shape `(∗ ∗; 0 g')` with `g'` invertible, where the first block is
the index `i`. 

### `KeepsLine.col_eq_zero`

 The `i`-th column vanishes off the diagonal. 

### `KeepsLine.block_det_ne_zero`

 The block on the other indices is invertible. 

### `KeepsLine.mul_apply_self`

 If `KeepsLine i N`, so that the column `i` of `N` vanishes off the diagonal and its block on
the other indices is invertible, then the diagonal entry at `i` of `M * N` is the product of those
of `M` and `N`. 

### `KeepsLine.mul`

 If `M` and `N` satisfy `KeepsLine i` (their column `i` vanishes off the diagonal and their
block on the other indices is invertible), then so does `M * N`. 

### `det_eq_mul_det_block`

 If the column `i` of `M` vanishes off the diagonal, then `det M` is the product of `M i i` and
the determinant of the block on the other indices. 

### `keepsLine_of_mem_parabolic`

 An element of `parabolic (· ≠ i)`, the stabiliser of the line of `e_i`, has the block shape
`KeepsLine i`: its column `i` vanishes off the diagonal and the block on the other indices is
invertible. 

### `KeepsLine.rootMultiplicity_charpoly`

 If the column `i` of `M` is zero, also at the diagonal, and the block on the other indices is
invertible, then `0` is a simple root of the characteristic polynomial of `M`. 
