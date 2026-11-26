---
{
  "module": "src/New/Spanning/MainTerm/Frequencies.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/MainTerm/Frequencies.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/MainTerm/Frequencies.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Sums over frequencies

The frequencies are the elements `ν` of a totally complex number field `E`. If `E` has `f` infinite
places, the sum of `∏_v [ν]_v ^ (-3)` over any finite subset of `E` is at most `C ^ f` with
`C = 64 * 38 * e ^ 4`. At an infinite place `[ν]_v` is `(max 1 |ν|_v) ^ 2`, with `|ν|_v` the usual
absolute value, and the finite places together give the norm of the denominator of `ν`. The numbers
with a given denominator `𝔟` lie in `N 𝔟` cosets of the ring of integers, each coset is counted by
small squares, and the sum over `𝔟` is at most the value at `2` of the Dedekind zeta function.

Notions from other files:
* `Φ v`: the chosen complex embedding of `E` that induces the infinite place `v`
  (`PlaceEmbedding E`).


### `denominator`

 The denominator of `ν`: the ideal of the integers `a` such that `a ν` is integral. 

### `exists_mem_algebraMap_eq_mul`

 Suppose that `(a) = 𝔟 𝔠` with `𝔟 ≠ 0` and that `r ν` is integral for all `r ∈ 𝔟`, that is,
`𝔟 ≤ denominator ν`. Then `a ν` is an integer in `𝔠`. 

### `exists_coset_label`

 For a nonzero ideal `𝔟`, the numbers `ν` whose denominator (the ideal of the integers `a`
with `a ν` integral) contains `𝔟` can be given `N 𝔟` labels so that two numbers with the same
label differ by an algebraic integer. 

### `sum_absNorm_inv_sq_le`

 The sum of `Ideal.absNorm 𝔟 ^ (-2)` over a finite set `s` of ideals of the ring of integers of
`E` is at most `exp (2 [E : ℚ])`, where `[E : ℚ] = Module.finrank ℚ E`: it is at most the value at
`2` of the Euler product with all coefficients equal to `1`, that is `ζ_E(2)`. 

### `squareCorner`

 The lower left corner `m.1 / 2 + (m.2 / 2) * I` of the square of side `1 / 2` with index
`m`. 

### `squareIndex`

 The index `(⌊2 * z.re⌋, ⌊2 * z.im⌋)` of the square of side `1 / 2` that contains `z`. The
square with index `(a, b)` is `[a / 2, (a + 1) / 2) × [b / 2, (b + 1) / 2)`. 

### `norm_sub_lt_one_of_squareIndex_eq`

 If `z` and `w` have the same index `squareIndex z = (⌊2 * z.re⌋, ⌊2 * z.im⌋)`, that is, if they
lie in the same half-open square `[a / 2, (a + 1) / 2) × [b / 2, (b + 1) / 2)` with `a` and `b`
integers, then their distance is less than one. 

### `squareIndex_squareCorner`

 The corner `squareCorner m = m.1 / 2 + (m.2 / 2) * I` lies in the square with index `m`, where
`squareIndex z = (⌊2 * z.re⌋, ⌊2 * z.im⌋)`. 

### `weight_le_weight_corner`

 The weight `(max 1 ‖z‖)⁻¹ ^ 6` of a complex number `z` is at most `64` times the weight of the
lower left corner of the square of side `1 / 2` that contains `z`. 

### `pairwise_half_le_norm_squareCorner_sub`

 For distinct index pairs `m ≠ m'` in `ℤ × ℤ`, the grid corners
`squareCorner m = m.1 / 2 + (m.2 / 2) * I` and `squareCorner m'` have distance at least `1 / 2`. 

### `sum_weight_corner_le`

 Over any finitely many indices `m`, the weights `(max 1 ‖z‖)⁻¹ ^ 6` at the grid points
`z = squareCorner m = m.1 / 2 + (m.2 / 2) * I` add up to at most `38`. 

### `sum_coset_weight_le`

 Let `X` be a finite subset of a totally complex field `E` any two elements of which differ by
an algebraic integer. Then the sum over `ν ∈ X` of the archimedean weights
`∏_v (max 1 ‖Φ v ν‖)⁻¹ ^ 6` is at most `(64 * 38) ^ f`, where `Φ v` is the chosen embedding at `v`
and `f` is the number of infinite places. 

### `sum_weight_filter_denominator_eq_le`

 Let `X` be a finite subset of a totally complex field `E`. The archimedean weights
`∏_v (max 1 ‖Φ v ν‖)⁻¹ ^ 6` of those `ν ∈ X` with a given nonzero denominator `𝔟` add up to at most
`Ideal.absNorm 𝔟 * (64 * 38) ^ Core.numInfPlaces E`, as these `ν` lie in at most `Ideal.absNorm 𝔟`
cosets of the integers. 

### `sum_height_inv_cube_le`

 Let `E` be a totally complex number field with `f = Core.numInfPlaces E` infinite places. For a
finite set `X ⊂ E`, the sum of `∏_v [ν]_v ^ (-3)` over `ν ∈ X` is at most
`(64 * 38 * e ^ 4) ^ f`. 
