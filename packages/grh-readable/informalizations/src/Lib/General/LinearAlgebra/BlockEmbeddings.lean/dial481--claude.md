---
{
  "module": "src/Lib/General/LinearAlgebra/BlockEmbeddings.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/LinearAlgebra/BlockEmbeddings.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/LinearAlgebra/BlockEmbeddings.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Extending columns, block matrices and block embeddings

For an embedding `ι : r ↪ n` of index sets, `New.inclMatrix k ι` has the standard basis vectors
`e (ι j)` as columns. Such a map splits `n` into two blocks, and the file studies the corresponding
block matrices. Over a field, independent columns extend to an invertible matrix. The embedding
`a ↦ diag(a, 1)` of unitary groups of sign matrices is a proper map, and the norm of a block
diagonal matrix is the larger of those of its blocks, for the L² operator norm.

## Main definitions and results

* `New.extendGL`: the embedding g ↦ diag(g, 1); `New.submatrix_extendGL` and
  `New.extendGL_apply_of_notMem_range` give its block g and its rows outside that block.
* `New.rangeParabolic`, `New.mem_rangeParabolic_iff`: the opposite parabolic for the two blocks, and
  its description in entries.
* `New.index_rangeParabolic_mul_card_GL`, `New.index_stabilizer_inclMatrix`: the index of the
  opposite parabolic times |GL_r(R)| is the index of the group that fixes the basis vectors of
  the first block, and over a finite field the latter index is computed.
* `New.residueDatum`: a function of adelic matrices given by their reductions at a family of
  places.
* `New.DiscreteSeries.isProperMap_inl`: the embedding `a ↦ diag(a, 1)` is a proper map.

Notions from other files:
* `New.parabolic`: the subgroup of GL_n(R) of matrices that are block upper triangular for a given
  level function on the indices.
* `New.U`, `New.U.sum`: U(J) is the group of g with gᴴJg = J; for a block diagonal sum J'' of J
  and J', `New.U.sum` is the homomorphism U(J) × U(J') → U(J'') sending (g,h) to diag(g,h).



## Extension of independent columns to an invertible matrix


### `exists_GL_mul_inclMatrix`

 A matrix b over a field with linearly independent columns extends to an invertible matrix u:
column ι(j) of u is column j of b. 


## The embedding diag(g, 1), the opposite parabolic and residue data

Here `u : r → n` is a map of index sets, mostly an embedding.


### `inclMatrix_transpose_mul`

 For an embedding u of index sets, multiplying T on the left by the transpose of
`inclMatrix R u` selects the rows of T indexed by u. 

### `inclMatrix_transpose_mul_cancel_left`

 The transpose of `inclMatrix R u` cancels `inclMatrix R u` on the left of a product. 

### `residueDatum`

 For a family of places `w i` of E, the function on finite adelic matrices x
(given as vectors on index pairs) equal to f of the family of the reductions of x at the places
`w i` if x is integral at all of them, and 0 otherwise. 

### `extendGL`

 For an embedding u of index sets, the homomorphism GL_r(R) → GL_n(R), g ↦ diag(g, 1), with g
acting on the indices in the image of u. 

### `extendGL_mul_inclMatrix`

 For the embedding g ↦ diag(g, 1), the columns indexed by u of the image of g are the columns
of g, extended by zero. 

### `submatrix_extendGL`

 The block of diag(g, 1) with rows and columns in the image of u is g. 

### `extendGL_apply_of_notMem_range`

 Outside the image of u, the rows of diag(g, 1) are those of the identity matrix. 

### `submatrix_extendGL_and_apply_of_notMem_range`

 The matrix `extendGL u g` has block g on the image of u and agrees with the identity matrix at
every entry whose row index is outside that image. 

### `mem_stabilizer_col_iff`

 An invertible matrix x fixes every column of T, seen as the family `T.col`, if and only if
xT = T. 

### `eq_inclMatrix_mul_iff`

 A matrix T is the extension by zero of its rows indexed by u exactly when its other rows
vanish. 

### `notMem_lt_notMem_iff`

 For the order `False < True` on propositions, the level `· ∉ s` of `j` is below that of `i`
exactly when `j` is in `s` and `i` is not. 

### `mem_parabolic_iff_mul_inclMatrix`

 An invertible matrix is block upper triangular, for the image of `u` as first block, exactly
when it keeps the span of the basis vectors indexed by `u`, the columns of `inclMatrix R u`. 

### `rangeParabolic`

 The opposite parabolic: the image under g ↦ (gᵀ)⁻¹ of the block upper triangular group
`New.parabolic` for the level function that is false on the image of u and true elsewhere. 

### `mem_rangeParabolic_iff`

 The opposite parabolic `rangeParabolic u` consists of the invertible matrices x whose entries
with row in the image of u and column outside it vanish. 

### `submatrix_mul_of_mem_rangeParabolic`

 For x in the opposite parabolic (entries with row in the image of u and column outside it
vanish), the rows of x T indexed by u are the u-block of x times the rows of T indexed by u; here
f selects columns of T. 

### `index_rangeParabolic`

 The opposite parabolic `New.rangeParabolic u` has the same index in GL_n(R) as the block upper
triangular group for the two blocks given by the image of u and its complement. 

### `index_rangeParabolic_mul_card_GL`

 In `GL_n(R)`, the index of `rangeParabolic u` times the order of `GL_r(R)` equals the index of
the stabilizer of the basis vectors `e_{u j}`, i.e. of the matrices fixing each basis vector indexed
by the image of `u`. Here `rangeParabolic u` is the image under `g ↦ (gᵀ)⁻¹` of the block upper
triangular group `parabolic` for the level function that is false on the image of `u` and true
elsewhere. (An infinite index or order counts as `0`.) 

### `orbit_col_inclMatrix`

 Over a field, the orbit under `GL_n` of the family of the basis vectors indexed by `u` is the
set of all linearly independent families indexed by `r`. 

### `index_stabilizer_inclMatrix`

 Over a finite field with `q` elements, the group of the matrices in `GL_n` that fix the `r`
basis vectors indexed by `u` has index `∏_{i < r} (q ^ n - q ^ i)`, the number of independent
families of `r` vectors. 

### `cast_index_stabilizer_inclMatrix`

 Over a finite field with `q` elements, the index of the group of the matrices in `GL_n` that fix
the `r` basis vectors indexed by `u` is the complex number
`q ^ (n r) ∏_{n - r < i ≤ n} (1 - q⁻¹ ^ i)`. 


## The block embedding of unitary groups

`New.U.inl` embeds `New.U (New.signMatrix ε)`, the unitary group of the diagonal matrix of signs
`ε`, into the group `New.U (New.signMatrix (Sum.elim ε η))` of the concatenated signs, by
`a ↦ diag(a, 1)`.


### `New.U.inl`

 The block embedding a ↦ diag(a, 1) of U(diag ε) into the unitary group of the concatenated
signs (ε, η). 


## Norms of block diagonal matrices and properness of block embeddings

Two facts on block diagonal matrices; all norms are `L²` operator norms.


### `New.norm_fromBlocks_zero_zero`

 The L² operator norm of diag(x, b) is the larger of the norms of x and b. 

### `New.DiscreteSeries.isProperMap_inl`

 For families of signs ε and ε', the embedding a ↦ diag(a, 1) of U(diag ε) into
U(diag(ε, ε')) is a proper map. 
