---
{
  "module": "src/New/UpperBound/ElementaryDivisors/PieriCone.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/PieriCone.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/PieriCone.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The Pieri cone, the step map and the slab: interlacing and volume of the cone

Vectors `ν` are real functions on pairs `(b, j)`, with `b` in `Fin k` and `j` a letter (in `ZMod N`
for the final volume formula). The step map `New.permStep` sends `ν` to signed gaps between
consecutive letters, twisted by permutations. The cone `New.pieriCone v P` is cut out by Pieri's
inequalities, one half of the interlacing inequalities between `ν` and `P` times its shift. The slab
`New.degreeSlab k D` is the set of nonnegative vectors whose sum at each letter `j` lies in the unit
interval `[D j - 1, D j]`, a product of slices of orthants.

## Main definitions and results

* `New.detOneSubPerm`: the determinant `det (1 - τ / q)` for a permutation `τ` of coordinates.
* `New.det_interlacing_indicator`: interlacing of two decreasing sequences is the determinant of a
  matrix of indicators.
* `New.volume_real_inter_degreeSlab_eq_signed_sum`, `New.prod_mul_volume_real_inter_degreeSlab`: for
  `P > 1`, a set whose preimage under `New.permStep` (with trivial permutations) is the cone fills a
  fraction of the slab given by a signed sum over permutations, equal to
  `∏ l < k, (q - 1) / (q ^ (l + 1) - 1)` with `q = P ^ N`.

The result serves the dimension bounds mod `p` from flags in
`New.UpperBound.ElementaryDivisors.DefectCount`.

## Notation

The Boolean `v j` selects the sign of the steps at the letter `j`: `+` for true, `-` for false. In
the application `v j` is true for even `j`.

## Relation to the literature

See `New.UpperBound.ElementaryDivisors.DefectCount` for related work.


### `permStep`

 The step map. For permutations `σ j` of `Fin k`, one for each letter `j`, it is the linear map
`ν ↦ β` with `β (b, j) = ± (P * ν (b, j + 1) - ν (σ j b, j))`, the sign being `+` if `v j` is true
and `-` otherwise. The entries of `β` are the steps of `ν`. 

### `degreeSlab`

 The slab: the vectors `β ≥ 0` whose degree `∑ b, β (b, j)` lies in `[D j - 1, D j]` for every
letter `j`. 

### `pieriCone`

 The Pieri cone: the vectors `ν` such that, for all `j` and `b`,
`P * ν (b + 1, j + 1) ≤ ν (b, j)` if `v j` is true, and `ν (b + 1, j) ≤ P * ν (b, j + 1)`
otherwise. 

### `positiveStepSet`

 The set of `ν` whose steps have degrees `∑ b, permStep v P 1 ν (b, j)` in `[D j - 1, D j]` and
such that, after block `j` of `ν` is rearranged by `τ j`, the image under `permStep v P σ` has
positive entries and lies in `Y`. 

### `det_interlacing_indicator`

 For weakly decreasing `x` and `y` in `ℝ ^ k`, the matrix with `(b, c)` entry `1` if `y c < x b`
and `0` otherwise has determinant `1` if the two interlace, `x 0 > y 0 ≥ x 1 > y 1 ≥ ⋯`, and `0`
otherwise. 

### `isBounded_degreeSlab`

 The slab `degreeSlab k D` is bounded, where `D j` is a real number for each letter `j` of a
finite set `T`. 

### `isBounded_inter_degreeSlab`

 The part of any set `Y` that lies in the slab `degreeSlab k D` is bounded. 

### `detOneSubPerm`

 The determinant `det (1 - τ / q)`, where the permutation `τ` acts on `Fin k → ℝ` by permuting
coordinates, `x ↦ x ∘ τ`. 

### `det_one_sub_comp_comm`

 For linear maps `A : ℝ^ι → ℝ^κ` and `B : ℝ^κ → ℝ^ι`, the endomorphisms `1 - A B` and
`1 - B A` have the same determinant. 

### `det_permStep_ne_zero`

 For `P > 1` the step map `permStep v P σ` has nonzero determinant. 

### `exists_det_permStep_eq`

 Let `P > 1`. The step map `permStep v P σ` takes `ν` to the vector with entries
`± (P * ν (b, j + 1) - ν (σ j b, j))`, with `+` where `v j` is true, `-` where it is false, and
`j + 1` taken in `Fin (m + 1)`. Up to a constant that does not depend on `σ`, its determinant is
`detOneSubPerm (P ^ (m + 1)) σ̄ = det (1 - σ̄ / P ^ (m + 1))`, where `σ̄ = (ofFn σ).prod` is the
product `σ 0 * ⋯ * σ m`, acting by permuting coordinates. 

### `volume_positiveStepSet`

 Change of variables for `P > 1`. The degree of a vector `β` at a letter `j` is `∑ b, β (b, j)`,
and `degreeSlab k D` is the set of `β ≥ 0` whose degree at each `j` lies in `[D j - 1, D j]`. The
set `positiveStepSet v P D σ τ Y` consists of the `ν` such that `permStep v P 1 ν` has its degrees
in these intervals and `permStep v P σ` sends `ν`, with block `j` rearranged by `τ j`, to a vector
of `Y` with positive entries. Its volume is the volume of `Y ∩ degreeSlab k D` divided by
`|det (permStep v P σ)|`. 

### `sum_sign_indicator_pos_eq_indicator_pieriCone`

 Let `P ≥ 0` and let `τ j` sort block `j` of `ν` decreasingly, giving `ν'`. The step
`permStep v P σ ν (b, j)` is `± (P * ν (b, j + 1) - ν (σ j b, j))`, with `+` where `v j` is true,
`-` where it is false, and `j + 1` taken in `Fin (m + 1)`. The signs of `σ 0 * ⋯ * σ m`, summed over
the `σ` with all these steps positive, add up to `1` if the steps `permStep v P 1 ν'` are positive
and `ν'` lies in `pieriCone v P`, and to `0` otherwise. 

### `sum_indicator_positiveStepSet`

 Counting in two ways at a point `ν`, for `P ≥ 0`. The cone `pieriCone v P` requires
`P * ν (b + 1, j + 1) ≤ ν (b, j)` where `v j` is true and `ν (b + 1, j) ≤ P * ν (b, j + 1)`
elsewhere. Let `Ω` pull back to this cone under `permStep v P 1`. The set
`positiveStepSet v P D σ τ Y` consists of the `ν` with `∑ b, permStep v P 1 ν (b, j)` in
`[D j - 1, D j]` for all `j` such that `permStep v P σ` sends `ν`, with each block `j` rearranged by
`τ j`, to a vector of `Y` with positive entries. Then the number of `τ` with `ν` in
`positiveStepSet v P D 1 τ Ω` equals the number of `σ` with `ν` in `positiveStepSet v P D σ 1 univ`,
each `σ` counted with the sign of `σ 0 * ⋯ * σ m`. 

### `sum_comp_prod_ofFn`

 For `f` on permutations of `Fin k`, the sum of `f (σ 0 * ⋯ * σ m)` over all families `σ` is
`k ! ^ m` times the sum of `f`: choose `σ 1, …, σ m` and solve for `σ 0`. 

### `volume_real_inter_degreeSlab_eq_signed_sum`

 Let `P > 1` and `q = P ^ (m + 1)`. Let `Ω` be a set whose preimage under the step map is the
cone. Then `Ω` fills the fraction `|det (1 - id / q)| / k ! * ∑ τ, sign τ / |det (1 - τ / q)|` of
the volume of the slab `degreeSlab k D` of vectors `β ≥ 0` with `∑ b, β (b, j)` in `[D j - 1, D j]`
for all `j`. 

### `volume_real_degreeSlab_one_pos`

 The slab of one letter, the nonnegative vectors of `ℝ ^ k` with sum at most `1`, has positive
volume. 

### `volume_real_pieriCone_inter_degreeSlab_one`

 The case of one letter, the only element of `Fin 1`, with sign `+` (`⊤` is the constant function
`true`). For `q > 1` the cone `pieriCone ⊤ q` of vectors with `q * β (b + 1) ≤ β b` fills the
fraction `∏ b < k, (q - 1) / (q ^ (b + 1) - 1)` of `degreeSlab k 1`, the simplex of vectors `β ≥ 0`
in `ℝ ^ k` with `∑ b, β b` in `[0, 1]`. 

### `prod_mul_volume_real_inter_degreeSlab`

 Volume of the image of the cone in a slab. Let `P > 1` and `q = P ^ N`, and let `Ω` be a set
whose preimage under the step map is the cone. Then the volume of `Ω ∩ degreeSlab k D`, multiplied
by `∏ l < k, (q ^ (l + 1) - 1) / (q - 1)`, equals the volume of the slab. 
