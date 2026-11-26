---
{
  "module": "src/Lib/Adelic/Unitary/RationalPoints.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/Unitary/RationalPoints.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/Unitary/RationalPoints.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Rational points and vectors of spaces under sums, moves and block embeddings

Elementary facts on adelic unitary groups and hermitian spaces.

* `New.U.mem_range_sum_left`, `New.U.mem_range_sum_right`: which unitary matrices for a block
  diagonal form come from one block.
* `New.Space.mem_Gamma_iff_range`: `g` is a rational point iff `x g x⁻¹` has rational entries.
* `New.Space.witt`: Witt's theorem for the form of a space.
* `New.Space.stdForm_vecAtPoint`: in the coordinates of the point, the form `J` becomes
  `New.stdForm`.

A space `V` (`New.Space`) is a rational matrix `J` with an adelic point `x` such that `xᴴ J x` is
the standard form of signs `s`; `New.G E s` is the adelic unitary group of that form. Rational
unitary matrices and rational vectors are read in these coordinates by `V.ratEmbed γ = x⁻¹ γ x`,
with image `V.Γ`, and `V.vecAtPoint y = x⁻¹ y`.

Notions from other files:
* `New.G`: The adelic unitary group G = G_∞ × G_f for signs s at the infinite places and the
  identity matrix at the finite places; `g.adeleMatrix` is the adelic matrix of `g`.
* `New.Space.sum`, `New.Space.reindex`, `New.Space.move`: the block diagonal sum of two spaces, the
  relabelling of the indices, and the space `(J, x a)` for `a` in G.
* `New.signedSpace`: the standard space with matrix diag(s), defined when E has a primitive 5040th
  root of unity (`New.HasPrimitiveRoot5040`).

## Relation to the literature

Witt's extension theorem for hermitian forms is classical; `New.Space.witt` is its matrix form
`New.witt` applied to the matrix of a space.


 ### Block embeddings and continuity 

### `U.mem_range_sum_left`

 Let `J''` be the block diagonal sum of `J` and `J'` with `J'` invertible. An element `g` of the
unitary group `U J''` of the matrices that preserve the form `J''` is `diag(a, 1)` with `a` in
`U J` if and only if its second block of columns is that of the identity matrix. Here `U.sum h` is
the map `(a, b) ↦ diag(a, b)`. 

### `U.mem_range_sum_right`

 Let `J''` be the block diagonal sum of `J` and `J'` with `J` invertible. An element `g` of the
unitary group `U J''` is `diag(1, a)` with `a` in `U J'` if and only if its first block of columns
is that of the identity matrix. Here `U.sum h` is the map `(a, b) ↦ diag(a, b)`. 

### `U.exists_sum_eq_iff_toCols_eq`

 Let `J''` be the block diagonal sum of `J` and `J'`, and let `g` be in `U J''`. If `J'` is
invertible, `g` is `diag(a, 1)` with `a` in `U J` if and only if its second block of columns is
that of the identity matrix (`U.mem_range_sum_left`). If `J` is invertible, `g` is `diag(1, a)`
with `a` in `U J'` if and only if its first block of columns is that of the identity matrix
(`U.mem_range_sum_right`). 

### `G.isClosedEmbedding_sum`

 The block diagonal embedding of the product of the adelic unitary groups for signs `s` and `t`
into the one for the concatenated signs is a closed embedding. 

### `G.continuous_reindex`

 Relabelling the indices along a bijection that carries the signs `s` to `t` is continuous on
the adelic unitary groups. 

### `G.continuous_neg`

 The isomorphism of adelic unitary groups for signs `s` and `-s` that is the identity on
matrices is continuous. 

 ### Rational points and vectors of a space 

### `ext`

 Two spaces with the same signs and the same point are equal: the point determines the
matrix. 

### `mem_Gamma_iff_range`

 `g` is a rational point of `V` (an element of `V.Γ`) if and only if all entries of the adelic
matrix `x g x⁻¹`, for the point `x` of `V`, are images of elements of `E` under the diagonal
embedding `toAdele` of `E` in its adeles. 

### `witt`

 Witt's theorem. Let `J` be the matrix of `V`, and let `X` and `Y` be left invertible `n × m`
matrices over `E` with `Xᴴ J X = Yᴴ J Y`. Then `g X = Y` for some `g` in the unitary group of `J`
over `E`. 

### `ratEmbed_mulVec_vecAtPoint`

 A rational unitary matrix `γ` acts in the coordinates of the point as it does on rational
vectors. 

### `stdForm_vecAtPoint`

 The standard form on the coordinates `x⁻¹ y`, `x⁻¹ z` of rational vectors `y`, `z` at the point
`x` of `V` is the image of `yᴴ J z` in the adeles. 

### `vecAtPoint_injective`

 A rational vector is determined by its coordinates at the point of the space. 

 ### Sums, relabelling and moves 

### `sum_ratEmbed`

 The rational embedding of a block sum of spaces sends `diag(γ₁, γ₂)` to the block diagonal sum
of the images of `γ₁` and `γ₂`. 

### `sum_vecAtPoint`

 The coordinates of a concatenated rational vector at the point of a sum of two spaces are the
concatenated coordinates. 

### `sum_mem_Gamma`

 A block diagonal pair is a rational point of the sum of two spaces if and only if each
component is a rational point of its space. 

### `signedSpace_eq_reindex`

 Let `E` contain a primitive 5040th root of unity and let `e` be a bijection of indices that
carries the signs `s` to `t`. If the space `V` has the same point as the standard space
`New.signedSpace E s` of matrix `diag(s)`, then relabelling `V` along `e` gives the standard space
`New.signedSpace E t`. 

### `mem_move_Gamma`

 `g` is a rational point of the space moved by `a` if and only if `a g a⁻¹` is a rational
point of the space. 
