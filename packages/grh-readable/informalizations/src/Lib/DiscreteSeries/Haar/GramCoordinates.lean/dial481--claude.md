---
{
  "module": "src/Lib/DiscreteSeries/Haar/GramCoordinates.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Haar/GramCoordinates.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Haar/GramCoordinates.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Coordinates for the Gram map

Let `J` be a hermitian matrix. The Gram map sends a tuple of vectors, the columns of a complex
matrix `Y`, to the hermitian matrix `T = Yᴴ J Y`. Tuples carry Lebesgue measure `dY`, and hermitian
matrices the product `dT` of the Lebesgue measures of the entries on and above the diagonal.

* `New.joinCols`, `New.joinCol`: joining two groups of columns into one matrix; this preserves
  volume (`New.measurePreserving_joinCols`, `New.measurePreserving_joinCol`).
* `New.hermOfReal`, `New.gramCoords`: real coordinates on hermitian matrices, and the Gram map in
  these coordinates.
* `New.lintegral_eq_skewOfReal_add_hermOfReal`: Lebesgue measure on matrices `Z = S + T / 2` of size
  `n`, with `S` skew-hermitian and `T` hermitian, is `2 ^ (-n) dS dT`.
* `New.exists_measurePreserving_hermBlocks`, `New.exists_measurePreserving_hermCorner`: cutting a
  hermitian matrix into the corresponding blocks preserves volume.

Notions from other files:
* `New.skewOfReal`: the skew-hermitian matrix with given real coordinates, normalised so that
  Lebesgue measure in the coordinates is that of the entries on and above the diagonal.
* `New.skewCoords`: the real-linear left inverse of `New.skewOfReal`, inverse to it on
  skew-hermitian matrices.


 ### Columns and transposes 

### `joinCols`

 The linear isomorphism that sends a pair of matrices to the matrix with the columns of both, in
the places given by `e`. 

### `continuous_joinCols`

 Joining two groups of columns is continuous. 

### `measurePreserving_joinCols`

 Joining two groups of complex columns (`joinCols`) preserves Lebesgue measure. 

### `measurePreserving_fromRows`

 Placing one complex matrix above another preserves Lebesgue measure. 

### `mul_joinCols`

 Left multiplication by a matrix acts on each of two groups of columns separately. 

### `toCol`

 A vector as a matrix with one column. 

### `measurePreserving_toCol`

 Reading a vector as a matrix with one column (`toCol`) preserves volume. 

### `toCorner`

 A vector and a real number as a one-column matrix and a one-by-one matrix. 

### `joinCol`

 The matrix whose columns are those of `p.1` and the vector `p.2`, in the places given by `e`. 

### `measurePreserving_joinCol`

 Adjoining a complex vector as a further column (`joinCol`) preserves Lebesgue measure. 

### `mul_joinCol`

 Left multiplication by a matrix acts separately on the given columns and on the adjoined
one. 

### `toCorner_symm_apply`

 The inverse of `toCorner` reads off the column and the single entry of the corner. 

### `volume_eq_dirac_of_isEmpty`

 On the matrices without columns, which form a single point, the volume is the unit mass. 

### `measurePreserving_conjTranspose`

 The conjugate transpose preserves Lebesgue measure on complex matrices. 

 ### Measurability and linear changes of variables 

### `_root_.Measurable.matrix_mul`

 The product of two measurable families of complex matrices is measurable. 

### `lintegral_eq_abs_det_mul_comp`

 Substitution by an invertible real linear map `T` in an integral against an additive Haar
measure: the Jacobian is `|det T|`. 

### `lintegral_eq_det_mul_comp_mul_mul`

 Substitution `y ↦ P y Q` in an integral over complex matrices, for invertible `P` and `Q`: the
Jacobian is `|det P| ^ (2 |n|) |det Q| ^ (2 |ι|)`. 

 ### Hermitian coordinates 

### `hermOfReal`

 The hermitian matrix with real coordinates `t`: it is `-i` times the skew-hermitian matrix
`skewOfReal t`, so its diagonal entries are those of `t`. Lebesgue measure in `t` is the product
of the Lebesgue measures of the entries on and above the diagonal. 

### `gramCoords`

 The Gram map: the real coordinates, in the sense of `hermOfReal`, of the Gram matrix
`Yᴴ J Y` of the columns of `Y`, for a hermitian `J` (`hermOfReal_gramCoords`). 

### `hermOfReal_gramCoords`

 For a hermitian `J`, the hermitian matrix with the real coordinates `gramCoords J Y` is the
Gram matrix `Yᴴ J Y`. 

### `lintegral_eq_det_mul_comp_congruence`

 In the real coordinates `t` of hermitian matrices `T = hermOfReal t` of size `n`, the congruence
`T ↦ Cᴴ T C` has the Jacobian `|det C| ^ (2 n)`. 

### `hasFDerivAt_gramCoords`

 The derivative of the Gram matrix `σᴴ J σ` of a differentiable family `σ` of matrices is
`σᴴ J dσ + dσᴴ J σ`, read in the coordinates of `gramCoords`. 

### `contDiff_gramCoords`

 The Gram map `Y ↦ Yᴴ J Y` on square matrices, read in the real coordinates of
`gramCoords`, is continuously differentiable. 

### `skewAddHerm`

 The isomorphism `(t, s) ↦ S + T / 2` onto the complex matrices, where `S` is the skew-hermitian
matrix with coordinates `s` and `T` the hermitian matrix with coordinates `t`. The inverse reads
`T = Z + Zᴴ` and `S = (Z - Zᴴ) / 2`. 

### `exists_linearMap_scale_entries`

 Scaling the entries of a real matrix by numbers `c a b` is a linear map with determinant
`∏ c a b`. 

### `norm_sq_skewAddHerm_of_scale`

 The squared norms of the entries of `skewAddHerm (t', s')` in terms of `t` and `s`, when `t'`
and `s'` are `t` and `s` multiplied by `2 / d` and `1 / d` entrywise, with `d = 1` on the diagonal
and `d = √2` off it. 

### `lintegral_eq_comp_skewAddHerm`

 The isomorphism `skewAddHerm`, `(t, s) ↦ S + T / 2`, onto the complex matrices of size `n`
has Jacobian `2 ^ (-n)`; here `S` is the skew-hermitian matrix with coordinates `s` and `T` the
hermitian one with coordinates `t`. 

### `lintegral_eq_skewOfReal_add_hermOfReal`

 Lebesgue measure on the complex matrices `Z = S + T / 2` of size `n`, with `S = skewOfReal s`
skew-hermitian and `T = hermOfReal t` hermitian, is `2 ^ (-n) ds dt`. 

 ### Blocks 

### `exists_measurePreserving_hermBlocks`

 A hermitian matrix of size `n₁ + n₂` is given by its two diagonal blocks, which are hermitian,
and by one block off the diagonal. In the real coordinates `t`, for which the matrix itself is
`hermOfReal t`, this change of variables preserves volume. 

### `exists_measurePreserving_hermCorner`

 A hermitian matrix `hermOfReal t` of size `n₁ + 1`, with the extra index placed by `e`, is given
by a hermitian block of size `n₁`, by the rest of the column at the extra index and by the real
diagonal entry there. In the real coordinates `t` this change of variables preserves volume. 
