---
{
  "module": "src/Lib/DiscreteSeries/Haar/TotalMass.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Haar/TotalMass.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Haar/TotalMass.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Haar measure on U(J): U(n) has mass one, covering bounds for norm balls

The measure `volume` on `U J` is the compact dual measure `New.haarU J`, normalised by
`New.volU n = ∏ i < n, 2 π ^ (i + 1) / i!`, the product of the areas of the unit spheres of
`ℂ, …, ℂ ^ n`. The first part shows that U(n) has mass one, by computing the image of Lebesgue
measure under the Gram map in two ways. For the second part let `J` be a hermitian involution of
size `n`, `j : S →* U J` a proper homomorphism, and `ν` a right invariant measure on `S` that is
finite on compact sets. Then norm balls are compared by a covering argument, with operator norms
throughout.

## Main definitions and results

* `New.exists_hasGramDensity`: near the identity, the image of Lebesgue measure under the
  Gram map `Y ↦ Yᴴ Y` of square matrices is `volU n / 2 ^ n` times Lebesgue measure. One column
  ranges over a sphere, and the parts of the other columns orthogonal to it form a square matrix of
  size `n - 1`.
* `New.isProbabilityMeasure_haarU`: for `J = 1` the measure has mass one, by comparison with the
  polar formula `New.IsGramSection.lintegral_eq`. The same holds for the sign matrix with all signs
  equal to 1.
* `New.DiscreteSeries.measure_ball_le_covering`: for `D, R ≥ 1` the set `‖j s * y‖ ≤ R` has at most
  `(3 D R²) ^ (2 n²)` times the measure of the ball `‖j s - 1‖ ≤ 1 / D`.
* `New.DiscreteSeries.integral_decay_le`, `New.DiscreteSeries.lintegral_decay_le`: for `n ≥ 1` and a
  natural number `c > 8 n²` the function `(2 / ‖j s * y‖) ^ c` is integrable, with integral at most
  `16 ^ c` times the measure of `‖j s - 1‖ ≤ 1`.

Notions from other files:
* `New.gramCoords J Y`: the real coordinates `skewCoords (I • (Yᴴ J Y))` of the hermitian matrix
  `Yᴴ J Y`: with `x = I • (Yᴴ J Y)` they are `(x a b).re + (x a b).im`, divided by `√2` for `a ≠ b`.
* `New.U J`: the group of matrices `g` with `gᴴ J g = J`; thus `U 1` is the unitary group.
* `New.sphereDensity k r`: the number `2 π ^ k r ^ (k - 1) / (k - 1)!`.

## Relation to the literature

Known result: volume of U(n), polynomial volume growth of U(J).
Here J is any hermitian matrix with J² = 1, and the measure is normalised so that U(n) has mass one.
The covering bound for norm balls holds for any group with a right invariant measure and a
homomorphism to U(J), with an explicit crude constant. Source: L. K. Hua, Harmonic Analysis of
Functions of Several Complex Variables in the Classical Domains (1963), ch. III; I. G. Macdonald,
The volume of a compact Lie group, Invent. Math. 56 (1980); B. Gross, On the motive of a reductive
group, Invent. Math. 130 (1997).


 ## U(n) has mass one 

### `exists_unitary_mulVec_eq`

 The unitary group of `ℂ^κ` takes a vector to any vector of the same norm. 

### `volume_map_normSq_Iio`

 For nonempty `κ` with `k` elements, the set `|ω|² < a` in `ℂ ^ κ` is the ball of radius `√a`, of
volume `(√a) ^ (2 k) π ^ k / k!`. 

### `integral_sphereDensity_div_two`

 For `k > 0` the integral of `sphereDensity k r / 2` over `[0, a]` is `a ^ k π ^ k / k!`. 

### `measurePreserving_normSq_sphereDensity`

 For nonempty `κ` with `k` elements, the map `ω ↦ |ω|²` carries Lebesgue measure on `ℂ ^ κ` to
the measure on `r > 0` with density `sphereDensity k r / 2 = π ^ k r ^ (k - 1) / (k - 1)!`. 

### `outerCoords`

 The real coordinates of the hermitian matrix `w wᴴ` of rank at most one, in the same convention
as `New.gramCoords`. 

### `HasGramDensity`

 The Gram map `Y ↦ gramCoords 1 Y`, the real coordinates of `Yᴴ Y` for square matrices `Y`, has
density `c` on the set `W` of real matrices: on `W` it carries Lebesgue measure to `c` times
Lebesgue measure. 

### `HasGramDensity.lintegral_conjTranspose_mulVec`

 Let the index set `n` consist of `n'` and one further index, fix a vector `v` of squared norm
`r > 0` in `ℂ ^ n`, and let the Gram map in size `n'` have the density `c` on `W`. Let `k` be the
number of elements of `n'`. The map that sends `k` vectors `Y` of `ℂ ^ n` to the coordinates `t` of
their Gram matrix and their products `w` with `v` carries Lebesgue measure to `c / r ^ k` times
Lebesgue measure, on the set where `t - outerCoords w / r`, the coordinates of the Gram matrix
minus `w wᴴ / r`, lies in `W`. 

### `HasGramDensity.succ`

 The step from size `n'` to size `n`, one more than `n'`. Let `φ` be a volume-preserving
homeomorphism that splits the coordinates of the Gram matrix of the columns `(Y, v)` (joined by
`joinCol e`, which puts column `a` of `Y` at index `e (.inl a)` and `v` at index `e (.inr ())`) into
the block `t = gramCoords 1 Y`, the column `w = Yᴴ v` and the corner `r = |v|²`. Suppose the Gram
map `Y ↦ gramCoords 1 Y` (real coordinates of `Yᴴ Y`) carries Lebesgue measure on `W` to `c` times
Lebesgue measure in size `n'`. Then in size `n` it does so with constant `sphereDensity (card n)
1 / 2 * c = (π^k / (k−1)!) c`, where `k = card n`, on the set where `r > 0` and
`t - outerCoords w / r` lies in `W`; here `outerCoords w` is the real coordinates of `w wᴴ`. 

### `apply_gramCoords_joinCol`

 The Gram matrix of columns `(Y, v)`, joined by `joinCol e`, in the coordinates `φ` of block,
column and corner, where the column entries are read from `hermOfReal t`, the hermitian matrix with
real coordinates `t`: they are `gramCoords 1 Y`, `Yᴴ v` and `|v|²`. 

### `exists_hasGramDensity`

 There is an open set `W` of real `n × n` matrices containing `gramCoords 1 1` on which the Gram
map `Y ↦ gramCoords 1 Y` has density `volU (card n) / 2 ^ card n`. Here `gramCoords 1 Y` is the
vector of real coordinates, in the sense of `hermOfReal` (which takes real coordinates back to the
hermitian matrix), of `Yᴴ Y` for complex square matrices `Y`. Having this density means that on `W`
the map carries Lebesgue measure to that constant times Lebesgue measure, where
`volU j = ∏ i < j, 2 π ^ (i + 1) / i!`. 

### `isProbabilityMeasure_haarU`

 The compact unitary group `U(n)` has total mass one for the measure `New.haarU 1`, which is
the `volume` of `U 1`. 

### `instance : IsProbabilityMeasure (α`

 For all signs equal to one, the unitary group of the sign matrix `signMatrix 1`, which equals
`1` by `signMatrix_one`, has total mass one. 


## Covering bounds for norm balls in U(J) and integrals of (2/‖j s y‖)^c

The covering bound compares volumes of balls in the real space of matrices, of dimension `2 n²`. The
integral bound integrates it over the level sets of the norm.


### `noncomputable instance : MetricSpace (U J)`

 The distance on `U J` is the operator norm of the difference of matrices. 

### `instance : ProperSpace (U J)`

 Closed balls of `U J` are compact, as `U J` is a closed set of matrices. 

### `New.measure_sublevel_ne_zero`

 The sublevel set `{s | f s ≤ r}` of a continuous function `f` has nonzero measure when
`f 1 < r`, for a measure `ν` that is positive on nonempty open sets. 

### `measure_ball_le_covering`

 Covering bound. For `D, R ≥ 1` and `3 D R² ≤ K`, the set where `‖j s * y‖ ≤ R` has measure
at most `K ^ (2 n²)` times the measure of the set where `‖j s - 1‖ ≤ 1 / D`. Here `ν` is a
right invariant measure on `S`, `j` is a homomorphism to the unitary group `U J` of a hermitian
involution `J` of size `n`, and the norms are operator norms. 

### `measure_ball_ne_top_of_isProperMap`

 For a proper homomorphism `j` to `U J` and a measure `ν` that is finite on compact sets, the
ball `‖j s - 1‖ ≤ R` in the operator norm has finite measure. 

### `integral_decay_le`

 Let `J` be a hermitian involution of size `n ≥ 1`, let `j : S →* U J` be proper, let `ν` be
right invariant and finite on compact sets, and let `c > 8 n²` be a natural number. Then
`s ↦ (2 / ‖j s * y‖) ^ c` is integrable, and its integral is at most `16 ^ c` times the measure of
the set where `‖j s - 1‖ ≤ 1` (operator norms). The bound does not depend on `y`. 

### `lintegral_decay_le`

 The bound of `integral_decay_le` for the lower Lebesgue integral: for a proper `j : S →* U J`,
`ν` right invariant and finite on compact sets, `n ≥ 1` and `c > 8 n²`, the integral of
`(2 / ‖j s * y‖) ^ c` is at most `16 ^ c` times the measure of the set where `‖j s - 1‖ ≤ 1`. 
