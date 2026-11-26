---
{
  "module": "src/Lib/Adelic/Reduction/MinkowskiTheorems.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/Reduction/MinkowskiTheorems.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/Reduction/MinkowskiTheorems.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Adelic Minkowski theorems and counts of rational points in boxes

This file proves Minkowski's first theorem and the upper bound in his second theorem over the
adeles, for the lattice attached to `y : GL n (𝔸 E)`. This lattice consists of the rational vectors
`ξ` with `y⁻¹ ξ` integral at the finite places, measured by `y⁻¹ ξ` at the infinite places. Here
`New.𝔸 E` is `ℂ ^ f × 𝔸f E` with `f = New.Core.numInfPlaces E`; here `[CMType E]` makes `E` a number
field whose infinite places are all complex, each place `w` with a chosen embedding `Φ w : E → ℂ`.
`New.toAdele` is the diagonal embedding, `New.ideleAbs` the adelic absolute value and `New.Ô` the
ring of integral finite adeles, and the unit box is `ball 0 1 ×ˢ Ô E` (sup norm) in each coordinate.

## Main definitions and results

* `New.minkowski_first`: a lower bound for the number of rational `ξ` with `y⁻¹ ξ` in the unit box.
* `New.Core.twoAtInfinity`, `New.Core.dyadicDiag`, `New.Core.profileBases`: the idele that is `2` at
  infinity, the diagonal matrices `D` of its powers, and the rational bases `Y` with `y⁻¹ Y D⁻¹` in
  a given set.
* `New.Core.frameLattice`, `New.Core.frameLength`: the lattice of `y` and the Euclidean length of
  `y⁻¹ ξ` at infinity.
* `New.Core.minkowski_second_theorem`: the second theorem. The lattice contains a basis of `E ^ n`
  for which `|det y|` times the product of the `2 f`-th powers of the lengths is bounded in terms of
  `f`, `n` and the discriminant. The proof takes successive minima and applies the first theorem to
  a box without nonzero lattice vectors.
* `New.exists_basis_frameLength_le_two_zpow`: a bound of the same kind, with a larger constant, for
  the lengths rounded up to powers `2 ^ x j`.
* `New.Core.encard_le_of_dyadic_box`: at most `C * 4 ^ (f * ∑ i, (x i)⁺)` rational vectors `ξ` have
  the vector of the `twoAtInfinity E ^ (-x i) * ξ i` in a given compact set.
* `New.Core.exists_eq_zero_of_zpow_mul_mem`: for a compact set `B` of adeles and all large `m`, no
  nonzero `a` in `E` has `twoAtInfinity E ^ m * a` in `B`.

Notions from other files:
* `New.ratVectors`: the image of `E ^ n` in `𝔸 E ^ n` under the diagonal embedding, as an additive
  subgroup.

## Relation to the literature

Part of a known result: Reduction theory, here the adelic Minkowski theorems. For Mahler-Godement
compactness and finite covolume see `Lib.Adelic.Reduction.FiniteVolume`.


 ## Minkowski's first theorem with multiplicity 

### `lintegral_encard_rat_points`

 Unfolding: the number of rational `ξ` with `y⁻¹ (ξ + x) ∈ S`, integrated over the quotient of
`𝔸 ^ n` by the subgroup `E ^ n = ratVectors E n`, is `|det y| * volume S`. The integral over the
quotient is taken against `quotMeasure`, the measure on `𝔸 ^ n` given by `volume` weighted by a
cutoff for this subgroup; its total mass is the covolume `1`. 

### `volume_pi_ball_prod_integral`

 The box of radius `r`, the adelic vectors with all entries of absolute value below `r` at the
`f = numInfPlaces E` infinite places and integral at the finite places, has volume
`((r ^ 2 * π * (2 / rd)) ^ f) ^ card n`, where `rd = rootDiscr E` is the root discriminant. 

### `minkowski_first`

 Minkowski's first theorem with multiplicity: for `y` in `GL n (𝔸 E)`, the adelic absolute value
`|det y|` is at most `(2 rd) ^ (f n)` times the number of `ξ` in `E ^ n` with `y⁻¹ ξ` integral at
the finite places and all its entries of absolute value below `1` at the infinite places. Here
`rd = rootDiscr E` is the root discriminant, `f` the number of infinite places and `n` stands for
`card n`. 

### `exists_ne_zero_inv_mulVec_mem`

 Minkowski's first theorem: if `|det y| > (2 * rootDiscr E) ^ (f * n)`, with `f` the number of
infinite places, some nonzero rational `ξ` has `y⁻¹ ξ` integral at the finite places and all
its entries of absolute value `< 1` at the infinite places. 

 ## Minkowski's second theorem and counts of rational points in boxes 

 ### Isometries, determinants and powers of two at infinity 

### `twoAtInfinity`

 The idele of `E` that is `2` at all infinite places and `1` at the finite places. 

### `sum_norm_sq_mulVec_of_isometry`

 A matrix `Q` with orthonormal columns, that is `Qᴴ * Q = 1`, preserves the sum of the squared
absolute values of the entries of a vector. 

### `ideleAbs_det_mkAdelicGL`

 The adelic absolute value of the determinant of the adelic matrix with components `a w` at the
infinite places `w` and finite part `b` (`mkAdelicGL`) is the product of the `‖det (a w)‖ ^ 2` and
of the absolute value `finIdeleAbs` of the finite idele `det b`. 

### `dyadicDiag`

 For an integer vector `x`, the diagonal adelic matrix whose `i`-th entry is `2 ^ x i` at the
infinite places and `1` at the finite places. 

### `profileBases`

 The set of `Y` in `GL n E` with `y⁻¹ Y D⁻¹` in `M`, where `D = dyadicDiag x` is diagonal with
entries `2 ^ x i` at infinity and `1` at the finite places. 

### `isCompact_closedBall_prod_integral`

 The adeles with components of absolute value at most `r` (by default `1`) at the infinite places
and integral at the finite places form a compact set. 

### `ideleAbs_det_dyadicDiag`

 The matrix `dyadicDiag x`, with diagonal entries `2 ^ x i` at the infinite places and `1` at
the finite ones, has determinant of adelic absolute value `(2 ^ (2 f)) ^ ∑ i, x i`, with `f` the
number of infinite places. 

### `ideleAbs_det_dyadicDiag_natCast`

 The matrix `dyadicDiag x` for natural exponents `x i` has determinant of adelic absolute value
`((2 ^ f) ^ ∑ i, x i) ^ 2`, with `f` the number of infinite places. 

### `dyadicDiag_inv_mem`

 For natural exponents `x i`, all entries of the inverse of `dyadicDiag x` (the diagonal matrix
with entries `2 ^ x i` at the infinite places and `1` at the finite ones) have absolute value at
most `1` at the infinite places and lie in the ring `Ô E` of integral finite adeles. 

### `dyadicDiag_inv_mulVec_apply`

 The inverse of `dyadicDiag x` multiplies the `i`-th entry of an adelic vector by
`twoAtInfinity E ^ (-x i)`. 

### `ideleAbs_det_map_toAdele`

 An invertible matrix with entries in `E` has, over the adeles, a determinant of absolute value
`1`: this is the product formula for `det Y`. 

 ### Successive minima 

### `exists_min_of_finite_le`

 A real function `len` attains its minimum on a nonempty set `S` that has only finitely many
points below each bound. 

### `exists_successive_minima`

 Successive minima. Let `L` be a spanning set of a vector space `V` with finitely many vectors
below each bound for the length `len`. For `k` at most the dimension of `V` there are `k`
independent vectors in `L`, each of least length among the vectors of `L` outside the span of the
earlier ones. 

### `frameLattice`

 The lattice `E ^ n ∩ z_f Ô ^ n` of an adelic frame `z`: the rational vectors `ξ` such that
`z⁻¹ ξ` is integral at the finite places. 

### `frameLength`

 The length of a rational vector `ξ` at an adelic frame `z`: the Euclidean norm of the
coordinates of `z⁻¹ ξ` at all infinite places together. 

### `norm_apply_le_frameLength`

 Each coordinate of `z⁻¹ ξ` at an infinite place `w` has absolute value at most the length
`frameLength z ξ`, the Euclidean norm of all these coordinates together. 

### `span_frameLattice`

 The lattice `frameLattice z` of the rational `ξ` with `z⁻¹ ξ` integral at the finite places
spans `E ^ n` over `E`. 

### `finite_frameLattice_of_frameLength_le`

 Only finitely many vectors of the lattice `frameLattice z` have length `frameLength z` at most
`r`, that length being the Euclidean norm of `z⁻¹ ξ` at all infinite places together. 

### `frameLength_pos`

 A nonzero rational vector `ξ` has positive length `frameLength z ξ`, the Euclidean norm of
`z⁻¹ ξ` at all infinite places together. 

### `sum_norm_sq_mulVec_lt_of_blockTriangular`

 Let `b` be triangular for the weight `wt` (`b k l = 0` if `wt l < wt k`) and `X * b` unitary, so
that `b⁻¹ c` gives the coordinates of `X c` in the orthonormal basis formed by the columns of
`X * b`. If `c` vanishes at the weights above `wt j` and the coordinates of weight at most `wt j`
have absolute value below `ρ > 0`, then the squared Euclidean norm of `X c` is below
`card n * ρ ^ 2`. 

### `frameLength_sq`

 The square of the length `frameLength z ξ` is the sum over the infinite places `w` of the
squared Euclidean norm of `z_w⁻¹ ξ_w`, where `z_w` is the component of `z` at `w` and `ξ_w` the
image of `ξ` under the embedding `Φ w`. 

### `frameLength_sq_lt_of_blockTriangular`

 At each infinite place `w` let `b w` be triangular for the weight `wt` and make the columns of
`g_w⁻¹ * b w` orthonormal, with `g_w` the component of `g` at `w`. Let the rational vector `c`
vanish at the weights above `wt j`. If at every `w` the coordinates of `(b w)⁻¹ c` of weight at
most `wt j` have absolute value below `ρ > 0`, then the length `frameLength g c` (the Euclidean norm
of `g⁻¹ c` at infinity) has square below `f * card n * ρ ^ 2`, with `f` the number of infinite
places. 

### `norm_det_eq_of_orthonormal_inv_mul`

 If the columns of `A⁻¹ * b` are orthonormal, then `det A` and `det b` have the same absolute
value. 

### `norm_det_sq_eq_of_orthonormal_inv_mul`

 If the columns of `A⁻¹ * b` are orthonormal, then `det A` and `det b` have the same squared
absolute value. 

### `ideleAbs_det_mul_prod_eq`

 Let `b w` make the columns of `g_w⁻¹ * b w` orthonormal at each infinite place `w`, with `g_w`
the component of `g` at `w`, and let `c ^ n * ‖det D‖ ^ 2 = ∏ j, α j ^ 2`. Then
`|det g| * ∏ j, α j ^ (2 f)` is `c ^ (f n)` times the adelic absolute value of the determinant of
the adelic matrix with the components `b w * D` at infinity and the finite part of `g`. Here `f` is
the number of infinite places and `n` stands for `card n`. 

### `ideleAbs_det_mul_prod_le_of_le_frameLength`

 The volume bound from a box without nonzero lattice vectors. Let the numbers `α j > 0` increase
with the weight `wt j`. Suppose that every rational `c` in `frameLattice g` (that is, with `g⁻¹ c`
integral at the finite places) has length `frameLength g c` (the Euclidean norm of `g⁻¹ c` at
infinity) at least `α j` whenever `j` has the largest weight among the indices with `c j ≠ 0`. Then
`|det g| * ∏ j, α j ^ (2 f) ≤ (2 f n rd) ^ (f n)`, where `|det g|` is the adelic absolute value,
`f` the number of infinite places, `n` stands for `card n` and `rd` is the root discriminant. 

### `minkowski_second_theorem`

 Minkowski's second theorem over `E`. For `z` in `GL n (𝔸 E)` the lattice `frameLattice z`, of
the rational `ξ` with `z⁻¹ ξ` integral at the finite places, contains a basis `y 0, …, y (n - 1)`
of `E ^ n`, ordered by length, with `|det z| * ∏ j, ‖y j‖ ^ (2 f) ≤ (2 f n rd) ^ (f n)`. Here
`‖ξ‖ = frameLength z ξ` is the Euclidean norm of `z⁻¹ ξ` at all infinite places together, `f` is
the number of infinite places, `n` stands for `card n`, `rd` is the root discriminant and
`|det z|` the adelic absolute value. Only the upper bound of the theorem is proved. 

### `_root_.New.exists_basis_frameLength_le_two_zpow`

 Minkowski's second theorem with dyadic bounds. For `y` in `GL n (𝔸 E)` there are an invertible
matrix `Y` over `E` and integers `x j` such that each row `Y j` lies in `frameLattice y` (the
vectors `ξ ∈ Eⁿ` with `y⁻¹ ξ` integral at all finite places) and has `frameLength` at most
`2 ^ x j`, and `|det y| * (2 ^ (2 f)) ^ ∑ j, x j ≤ (8 f n rd) ^ (f n)`. Here `frameLength y ξ` is
the Euclidean norm of the coordinates of `y⁻¹ ξ` at all infinite places together, `f` is the number
of infinite places, `n` stands for `card n`, `rd` is the root discriminant and `|det y|` is the
adelic absolute value. 

 ### Counting rational points 

### `tsum_prod_le_prod_tsum`

 The sum over all tuples `x : n → α` of the product of the `f (x i)` is at most the product over
`n` of the sums of `f`. 

### `dyadicDiag_toNat_inv_mulVec_add_mem`

 Let `box` be the set of adelic vectors with entries of size at most `1` at infinity and
integral at the finite places, and let `t = twoAtInfinity E` be the idele that is `2` at infinity
and `1` at the finite places. If the vector of the `t ^ (-x i) * u i` lies in `B` and `v` lies in
`F`, then `u + v` multiplied by the inverse of the diagonal matrix of the `t ^ max (x i) 0` lies in
`box * B + box * F`. 

### `encard_le_of_dyadic_box`

 Counting rational points in a box. For a compact set `B` of adelic vectors there is a finite `C`
with the following property. For every `x : n → ℤ`, let `f a` (`a ∈ S`) be a family of distinct
rational vectors such that the vector with entries `twoAtInfinity E ^ (-x i) * f a i` lies in `B`
for every `a`, where `twoAtInfinity E` is the idele that is `2` at infinity and `1` at the finite
places. Then the family has at most `C * ((2 ^ r) ^ ∑ i, max (x i) 0) ^ 2` members, with
`r = numInfPlaces E` the number of infinite places. 

 ## Rational elements scaled into a compact set of adeles 

### `New.Core.exists_eq_zero_of_zpow_mul_mem`

 For a compact set `B` of adeles there is an integer `c` such that, for every integer `e < c`, an
element `a` of `E` (embedded diagonally by `toAdele`) that lies in `B` after multiplication by
`2 ^ (-e)` at the infinite places, that is by `twoAtInfinity E ^ (-e)`, is zero. 
