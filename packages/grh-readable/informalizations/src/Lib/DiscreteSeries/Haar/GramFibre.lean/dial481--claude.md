---
{
  "module": "src/Lib/DiscreteSeries/Haar/GramFibre.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Haar/GramFibre.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Haar/GramFibre.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The fibre measure of the Gram map

Let `J` be a hermitian involution of size `r` and `G = U(J)`. The Gram map sends a tuple of vectors,
the columns of a matrix `Y`, to the real coordinates (`New.gramCoords`) of the hermitian matrix
`T = Yᴴ J Y`.

* `New.LeGramFibre J E m`: the law of `g E` under the measure `m` on `G` is at most the fibre
  measure `dY / dT` on the tuples with the Gram matrix of `E`.
* `New.LeGramFibre.le_haar`, `New.leGramFibre_haar`: on the bases with Gram matrix `J`, which form
  the group `G`, the largest measure below the fibre measure is `vol U(r) / 2 ^ r` times the compact
  dual Haar measure `New.haarU J`, which is the `volume` of `U(J)`. Here `vol U(r)` is `New.volU r`.
* `New.LeGramFibre.append`, `New.LeGramFibre.append_vector`, `New.LeGramFibre.insert`: lower bounds
  for the fibre measure by choosing some vectors, moving them to a fixed position by an isometry,
  and choosing the others.

Notions from other files:
* `New.LeFibreMeasure μ ν π b l`: the measure `l` is at most the fibre measure of `μ / ν` for the
  map `π` over the point `b`.
* `New.gramCoords J Y`: the real coordinates of the hermitian matrix `Yᴴ J Y`; `New.hermOfReal t` is
  the hermitian matrix with coordinates `t`.
* `New.IsGramSection J V σ`: a differentiable section `σ` of the Gram map on the open set `V` of
  coordinates, with invertible values.
* `joinCols e (E₁, E₂)`, `joinCol e (E, v)`: the matrix with the columns of `E₁` and `E₂`, or of `E`
  and `v`, in the places given by `e`; `inclMatrix ℂ u` has the columns `e_{u k}`.

## Relation to the literature

Known result: the invariant measure `dY / dT` on tuples of vectors with a given Gram matrix. Source:
C. L. Siegel, Über die analytische Theorie der quadratischen Formen, Ann. of Math. 36 (1935).


 ### The fibre measure over `J` 

### `LeGramFibre`

 The image of the measure `m` under `g ↦ g E` is at most the fibre measure `dY / dT` of the Gram
map on the tuples with the Gram matrix of `E`. 

### `IsGramSection.continuousOn_mul_inv`

 For a section `σ` of the Gram map on `V`, the factor `γ = Y σ(T)⁻¹` depends continuously on
the matrix `Y` with Gram coordinates `T` in `V`. 

### `LeGramFibre.le_haar`

 A measure `m` on `U(J)` that is at most the fibre measure `dY / dT` of the Gram map on the bases
with Gram matrix `J` is at most `vol U(r) / 2 ^ r` times the compact dual Haar measure, which is
the `volume` of `U(J)`. Here `r` is the size of `J` and `vol U(r) = volU r`. 

### `leGramFibre_haar`

 The measure `vol U(r) / 2 ^ r` times the compact dual Haar measure, which is the `volume` of
`U(J)`, is at most the fibre measure `dY / dT` of the Gram map on the bases with Gram matrix `J`
(`New.LeGramFibre`). Here `r` is the size of `J` and `vol U(r) = volU r`. 

 ### Choosing vectors in turn 

### `measurePreserving_mul_add_mul`

 If the columns of `D` and `R` together form an orthonormal basis of `ℂ ^ ι`, then
`(M, x) ↦ D M + R x` preserves the volume. 

### `measurePreserving_mul_mul_add_mul`

 Coordinates adapted to the Gram products with `E`. If the columns of `J E` and `R` form an
orthonormal basis, then `(M, x) ↦ J E M + R x` preserves the volume. 

### `leFibreMeasure_conjTranspose_mul_mul`

 The fibre measure of the products with `E`. Let `J` be a hermitian involution, and suppose the
columns of `J E` and `R` form an orthonormal basis. Then the image `l` of Lebesgue measure under
`x ↦ J E M + R x` is at most the fibre measure of `y ↦ Eᴴ J y` over `M` (`New.LeFibreMeasure`). That
is, take a lower semicontinuous `K ≥ 0` with `∫_{Eᴴ J y ∈ S} K dy ≤ C·vol(S)` for all open `S` near
`M`; then `∫ K dl ≤ C`. 

### `map_joinCols_prod_volume`

 Choosing `g` with law `m` and completing `g E₁` by further columns with the Lebesgue measure, in
the places given by `e` (`joinCols`), is the same as completing `E₁` first and then moving all
columns by `g`. 

### `map_mul_joinCols_prod_eq_map_mconv`

 Let `E = joinCols e (E₁, E₂)` have the columns of `E₁` and `E₂`. If `m'` is carried by the
elements that fix `E₁`, then the law of `g (E₁, g' E₂)` under `m × m'` is the law of `g E` under
the convolution `m ∗ₘ m'`. 

### `LeGramFibre.append`

 Choosing vectors in turn. Let the tuple `E = joinCols e (E₁, E₂)` consist of `E₁` and `E₂`, in
the places given by `e`. Suppose that the law of `g E₁` under `m` is at most the fibre measure of
the Gram map (`New.LeGramFibre`), that `m'` is carried by the elements that fix `E₁`, and that the
law of `g' E₂` under `m'` is at most the fibre measure (`New.LeFibreMeasure`) of the map that sends
`y` to the products `E₁ᴴ J y` and to the coordinates `gramCoords J y` of its Gram matrix. Then the
law of `g g' E` is at most the fibre measure of the Gram map over the Gram matrix of `E`. 

### `LeGramFibre.append_vector`

 Choosing one more vector `v`: the case of `New.LeGramFibre.append` in which the second tuple
has one member. Suppose that the law of `g E` under `m` is at most the fibre measure of the Gram
map, that `m'` is carried by the elements that fix `E`, and that the law of `g v` under `m'` is at
most the fibre measure of the map that sends `y` to the vector `Eᴴ J y` and the number `y* J y`.
Then the law of `g (E, v)` under `m ∗ m'` is at most the fibre measure of the Gram map, `(E, v)`
having its columns in the places given by `e`. 

### `leGramFibre_dirac`

 For the empty tuple `E`, the law of `g E` under the unit mass at the identity of `U(J)` is at
most the fibre measure of the Gram map. 

### `subtypeInsertEquiv`

 The bijection from `p` and one more point onto `q = p ∪ {j}`, for `j` outside `p`: the point
goes to `j`. 

### `LeGramFibre.insert`

 Choosing one more basis vector, `inclMatrix ℂ Subtype.val` being the matrix with the columns
`e_i` for the `i` in a set of indices. Let `p` be a set of indices, `j` an index outside it and
`q = p ∪ {j}`. Let the law of `g (e_i)_{i ∈ p}` under `m` be at most the fibre measure of the Gram
map. Let `m'` be carried by the elements that fix these `e_i`, and let the law of `g e_j` under
`m'` be at most the fibre measure of the `J`-products of a vector `y` with them and with itself.
Then the law of `g (e_i)_{i ∈ q}` under `m ∗ m'` is at most the fibre measure of the Gram map. 
