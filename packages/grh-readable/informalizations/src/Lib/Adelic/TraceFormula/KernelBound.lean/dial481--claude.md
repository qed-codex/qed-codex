---
{
  "module": "src/Lib/Adelic/TraceFormula/KernelBound.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/TraceFormula/KernelBound.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/TraceFormula/KernelBound.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The sum of a majorant over the rational points

For a test function `φ` on the finite points, the sum of `|φ(y_fin)| ‖y_∞‖ ^ (-8 n² - 1)` over all
`y = g⁻¹ γ x`, `γ` rational, is bounded by a constant times `Ht(x) ^ (4 f n²)`, uniformly in `g`.
Here `‖y_∞‖` is the product of the operator norms at the infinite places, `Ht(x)` is `V.height x`,
`f` is the number of infinite places, and in such exponents `n` stands for the dimension `card n`.
The translates `g⁻¹ γ x B` of a small box `B` are disjoint, the majorant at the base point of each
is at most a bounded multiple of its values there, and it is integrable.

* `New.tsum_mul_measure_le_lintegral`: a sum over disjoint translates against an integral.
* `New.Space.exists_levelBox_disjoint`: the translates of the box `New.levelBox` are disjoint.
* `New.Space.exists_tsum_majorant_le`: the bound for the sum of `New.Space.majorant`.

Notions from other files:
* `G E s = GInf E s × Gf E n` is the adelic unitary group: one copy of the real unitary group
  `USign s` of the signs `s` at each infinite place, times the finite adelic group `Gf E n`.
* `stdLevel E n` is the subgroup of integral points of `Gf E n`; a level is an open subgroup of it.
* For `V : Space E n s`, a hermitian space on `Eⁿ` with a base lattice `V.baseLattice`, `U V.J` is
  the group of rational points and `V.ratEmbed` its embedding into `G E s`.
* `V.height x` is the inverse of the first minimum, cut off at `1`, of the lattice of `V` at `x`,
  that is, of the base lattice of the translate `V.move x`.
* `TestFunction (Gf E n)` is the Schwartz–Bruhat space of `Gf E n` (locally constant functions of
  compact support).

## Relation to the literature

Known result: Sum over the rational points of a majorant of a test function, bounded by a power of
the height. This is the standard estimate for the kernel of a trace formula.


### `tsum_mul_measure_le_lintegral`

 If the translates `y i * B` are disjoint and `f x ≤ c * f (x * z)` for `z ∈ B`, then the sum of
the values `f (y i)`, times the measure of `B`, is at most `c` times the integral of `f`. 

### `TestFunction.exists_isLevel_invariant`

 A test function `φ` on the finite adelic unitary group is invariant on both sides under some
level `J`, that is, under some open subgroup of the integral points. 

### `norm_le_two_of_norm_sub_one_le`

 An element of a real unitary group within distance `1` of the identity has norm at most `2`. 

### `norm_mul_inv_sub_one_le`

 The quotient of two elements of a real unitary group within distance `δ ≤ 1` of the identity is
within distance `4 δ` of it. 

### `levelBox`

 The box of the points whose real components are within distance `δ` of the identity and whose
finite component lies in `J`. 

### `mem_levelBox`

 A point lies in the box `levelBox E s δ J` if and only if each real component is within
distance `δ` of the identity and the finite component lies in `J`. 

### `measurableSet_levelBox`

 The box `levelBox E s δ J` is measurable if the subgroup `J` is open. 

### `exists_le_mul_volume_levelBox`

 For an open subgroup `J` of the finite points there is a positive constant `v` such that, for
every `D ≥ 1`, the volume of the box `levelBox E s D⁻¹ J` is at least `v (12 D) ^ (-2 n² f)`, with
`f` the number of infinite places. 

### `mulVec_eq_self_of_norm_sub_one_le`

 If, for a natural number `b`, the element `x⁻¹ γ x` is integral at the finite places and within
distance `((b + 1) Ht(x)²)⁻¹` of the identity at the infinite places, then the rational point `γ`
fixes every vector of length at most `b Ht(x)` of the lattice of `V.move x`, the translate of `V`
by `x`. Here `Ht(x) = V.height x` is the inverse of the first minimum of that lattice, this minimum
being cut off at `1` from above, so that `Ht(x) ≥ 1`. 

### `exists_eq_one_of_norm_sub_one_le`

 There is a constant `c ≥ 1` such that a rational point `γ` is trivial if `x⁻¹ γ x` is integral
at the finite places (lies in `stdLevel E n`) and within distance `(c Ht(x)²)⁻¹` of the identity at
the infinite places. Here `Ht(x) = V.height x ≥ 1` is the inverse of the first minimum, cut off at
`1` from above, of the lattice of `V` at `x`. 

### `exists_levelBox_disjoint`

 Let `J` be a subgroup of the integral finite points. There is `c ≥ 1` such that, for all adelic
points `g`, `x` and for the box `B` of points within distance `δ = (c Ht(x)²)⁻¹` of the identity at
the infinite places and in `J` at the finite ones (`levelBox E s δ J`, with `Ht(x) = V.height x`),
the translates `g⁻¹ γ x B` by the rational points `γ` are disjoint. 

### `majorant`

 The majorant `|φ(y_fin)| ‖y_∞‖ ^ (-A)`, where `‖y_∞‖` is the product of the operator norms at
the infinite places. 

### `majorant_le_mul_majorant_mul`

 If `φ` is invariant on the right under `J`, then the majorant of exponent `A` grows at most by
the factor `2 ^ (f A)`, with `f` the number of infinite places, when it is evaluated at `y` instead
of `y * z`, for `z` in a box `levelBox E s δ J` with `δ ≤ 1` (real components within distance `δ` of
the identity, finite component in `J`). 

### `integrable_majorant`

 The majorant `|φ(y_fin)| ‖y_∞‖ ^ (-A)` of a test function `φ` is integrable for the volume on
the adelic group as soon as its exponent `A` exceeds `8 n²`. 

### `exists_tsum_majorant_le`

 Let `E` be a CM field and `V` a hermitian space with a point. Let `φ` be a test function on the
finite unitary group, a locally constant, compactly supported complex function. Then there is a
constant `C ≥ 0` such that, for all adelic points `g` and `x`, the following holds with `f` the
number of infinite places and `V.height x` equal to `1/λ`, where `λ` is the first minimum, capped at
1, of the space `V` moved by `x`: the sum of the majorant `|φ(y_fin)| ‖y_∞‖ ^ (-8 n² - 1)` over all
`y = g⁻¹ · V.ratEmbed γ · x`, with `γ` running over the rational unitary group `U(V.J)` and `‖y_∞‖`
the product of the operator norms at the infinite places, is at most `C * V.height x ^ (4 f n²)`. 
