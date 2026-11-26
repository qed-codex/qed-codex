---
{
  "module": "src/Lib/General/LinearAlgebra/IdempotentRadical.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/LinearAlgebra/IdempotentRadical.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/LinearAlgebra/IdempotentRadical.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The unipotent radical attached to an idempotent matrix

For an idempotent matrix `ε`, the matrices `1 + ε Y (1 - ε)` form the unipotent radical of the
parabolic subgroup that keeps the image of `ε`. If a polynomial in `g` is a projection onto the
image of `ε`, then every translate of `g` by the radical is conjugate to `g` under the radical
(`semiconjBy_radicalHom_aeval_sub`).


### `upperBlocks`

 The upper right blocks with respect to `ε`: the matrices `Z` with `ε Z = Z` and `Z ε = 0`. For
an idempotent `ε` these are the maps that kill the image of `ε` and send everything into it. 

### `mul_eq_zero_of_mem_upperBlocks`

 An upper right block `Y` (that is, `ε Y = Y` and `Y ε = 0`) satisfies `Y Z = 0` for every matrix
`Z` with `ε Z = Z`. 

### `mul_mem_upperBlocks_left`

 The upper right blocks, the matrices `Z` with `ε Z = Z` and `Z ε = 0`, are stable under left
multiplication by a matrix `g` with `ε g ε = g ε` (for an idempotent `ε`: `g` keeps the image of
`ε`). 

### `mul_mem_upperBlocks_right`

 The upper right blocks, the matrices `Z` with `ε Z = Z` and `Z ε = 0`, are stable under right
multiplication by a matrix `g` with `ε g ε = g ε`. 

### `radicalHom`

 The homomorphism `Y ↦ 1 + ε Y (1 - ε)` from the additive group of matrices to `GL n k`. Its
image is the unipotent radical of the parabolic subgroup that keeps the image of the idempotent
`ε`. 

### `coe_radicalHom_of_mem`

 If `ε Z = Z` and `Z ε = 0`, that is, if `Z` is an upper right block, then the matrix
`1 + ε Z (1 - ε)` of `radicalHom` is `1 + Z`. 

### `coe_radicalHom_mul_idempotent`

 The elements `1 + ε Y (1 - ε)` of the radical fix the image of `ε` pointwise. 

### `continuous_radicalHom`

 Over a topological ring, the map `Y ↦ 1 + ε Y (1 - ε)` into `GL n k` is continuous. 

### `aeval_sub_aeval_mem_upperBlocks`

 Let `ε g ε = g ε` and let `x - g` be an upper right block (a matrix `Z` with `ε Z = Z` and
`Z ε = 0`). Then `p(x) - p(g)` is an upper right block for every polynomial `p`. 

### `mul_mul_eq_mul_of_aeval`

 If `ε p(g) = p(g)` and `p(g) ε = ε` (that is, `ε` is idempotent and `p(g)` is a projection onto
the image of `ε`), then `ε g ε = g ε` (`g` keeps the image of `ε`). 

### `semiconjBy_one_add_aeval_sub`

 Let `p(g)` be a projection onto the image of `ε` (`ε p(g) = p(g)` and `p(g) ε = ε`), and let
`x - g` be an upper right block (a matrix `Z` with `ε Z = Z` and `Z ε = 0`). Then
`D = p(x) - p(g)` satisfies `(1 + D) x = g (1 + D)`. 

### `radicalHom_mul_mul_sub_mem_upperBlocks`

 If `ε g ε = g ε`, then, with `u = radicalHom hε Y` and `u' = radicalHom hε Z`, the difference
`u g u' - g` is an upper right block: it is unchanged by `ε` on the left and killed by `ε` on the
right. 

### `semiconjBy_radicalHom_aeval_sub`

 Let `ε` be idempotent, let `p(g)` be a projection onto its image (`ε p(g) = p(g)` and
`p(g) ε = ε`), and let `x = u g u'` with `u, u'` in the image of `radicalHom`, the group of the
matrices `1 + ε Y (1 - ε)`. Then the element of that group with parameter `D = p(x) - p(g)`
conjugates `x` to `g`. 
