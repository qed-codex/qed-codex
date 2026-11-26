---
{
  "module": "src/New/Appendix/DiscreteSeries/PositionGroup.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Appendix/DiscreteSeries/PositionGroup.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Appendix/DiscreteSeries/PositionGroup.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The group of a position

The elements `g` of `U(ε)` for which `g - 1` lowers the flag of a position form a closed subgroup
`R`. It maps to `U(η)` by the action `g'` on the image of `i₀` modulo `A_{≤ j₀ - 1}`, and it
carries an additive sum `σ`.

* The period over `R` in a stationary position is bounded below by Laplace's method
  (`IsStationary.integrable_periodIntegrand_and_measure_le`). The bound passes to a group that maps
  properly onto `R` (`IsStationary.period_lower_bound_of_surjective`).
* The pairing over `U(ε)` of a coefficient of `U(ε)` with a conjugated coefficient of `U(ε ⊕ 1)` is
  bounded below (`IsSteep.exists_volume_le_mul_norm_integral_dsCoeff`). This is the period in a
  stationary position with one vector `v₁`, where `R` is the stabilizer of `v₁` in `U(ε ⊕ 1)`, a
  conjugate of `U(ε)`.

Notions from other files:
* `USign ε` is the unitary group `U(ε)` of the diagonal matrix `signMatrix ε` of signs, and
  `formAdjoint ε η A` is the adjoint `A†` of `A : (ℂ^m, η) → (ℂ^n, ε)` for these forms.
* `IsPosition ε η d v i₀`: the columns `v₁, …, v_{j₀}` of `v`, `j₀ = d + 1`, are independent, their
  products vanish except that `v_{j₀}` has norm `±1`, `i₀` is an isometry into their orthogonal
  complement, and `card n = card m + 2 d + 1`.
* `LowersFlag d v Y σ`: `Y` maps the span `A_{≤ j}` of `v₁, …, v_j` into `A_{≤ j - 1}` for `j ≤ j₀`,
  and `σ` is the sum of the coefficients of `v_j` in `Y v_{j + 1}`.
* `InducesOn d v i₀ Y Y'`: `Y i₀ = i₀ Y'` modulo `A_{≤ j₀ - 1}`.
* `IsSteep l B e`: for `e : X ⊕ Fin M ≃ n`, the weight of the lowest `K`-type of `l` is `0` on `X`
  and decreases in `[-3 B, -B]` on the other coordinates, with alternating signs there.
* `IsLaplaceDatum` collects the hypotheses of Laplace's method on a map into `U(ε) × U(η)`.


### `mul_initCols`

 Multiplying on the left commutes with taking the first `d` columns. 

### `mul_initCols_eq`

 Let `initCols` take the first `d` of `d + 1` columns. If `g - 1` maps the columns of `v` into
the span of the first `d` columns with the matrix `N`, then `g` maps this span into itself, with
the matrix `1 + initCols N`. 

### `LowersFlag.inv`

 Let `g` be invertible and let `g - 1` lower the flag of the columns `v₁, …, v_{d + 1}` of `v`:
it sends each `v_j` to a combination of `v₁, …, v_{j - 1}`, and `σ` is the sum over `j ≤ d` of the
coefficients of `v_j` in `(g - 1) v_{j + 1}`. Then `g⁻¹ - 1` lowers the same flag, with some sum of
coefficients `σ'`. 

### `positionGroup`

 The group `R` of the `g` in `U(ε)` with `(g - 1) A_{≤ j} ⊆ A_{≤ j - 1}` for `j ≤ j₀ = d + 1`,
where `A_{≤ j}` is the span of the first `j` columns of `v`. 

### `positionSum`

 The sum of the coefficients of `v_j` in `g v_{j + 1}` over `j ≤ d`, where `v_j` are the columns
of `v` and `g` lies in the group `R = positionGroup ε v`. The choice is unique if the `v_j` are
independent, see `IsPosition.lowersFlag_unique`. 

### `lowersFlag_positionSum`

 The matrix `g - 1` lowers the flag of the columns of `v`, with coefficient sum
`positionSum g`. 

### `exists_sub_one_mul_eq_initCols_mul`

 For `g` in `positionGroup ε v`, the matrix `g - 1` maps the columns of `v` into the span of
the first `d` columns. 

### `positionSum_mul`

 For a position `(v, i₀)`, the sum of the coefficients of `v_j` in `g v_{j + 1}` is additive on
the group `positionGroup ε v`. 

### `isClosed_positionGroup`

 For a position `(v, i₀)`, the group `positionGroup ε v` of the `g` for which `g - 1` lowers the
flag of the columns of `v` is closed in `U(ε)`. 

### `vec_orthogonal_sub_one_mul`

 For a position `(v, i₀)` and `g` in the group `positionGroup ε v`, the image of `(g - 1) i₀` is
orthogonal to the columns of `v` for the form of signs `ε`. 

### `inducesOn`

 Let `(v, i₀)` be a position: the `d + 1` columns of `v` are independent, their products for the
form of signs `ε` vanish except that the last has norm `±1`, `i₀` is an isometry of `(ℂ^m, η)` into
their orthogonal complement, and `card n = card m + 2 d + 1`. Let `g` lie in `positionGroup ε v`, so
`g` is in `U(ε)` and `g - 1` maps each column of `v` into the span of the earlier ones. Then `g`
acts by `i₀† g i₀` on the image of `i₀` modulo the span of the first `d` columns of `v`. 

### `formAdjoint_conj_mul`

 Let `(v, i₀)` be a position: the `d + 1` columns of `v` are independent, their products for the
form of signs `ε` vanish except that the last has norm `±1`, `i₀` is an isometry of `(ℂ^m, η)` into
their orthogonal complement, and `card n = card m + 2 d + 1`. Then `g ↦ i₀† g i₀` is multiplicative
on the group `positionGroup ε v` of the `g` in `U(ε)` such that `g - 1` maps each column of `v` into
the span of the earlier ones. 

### `isometry_formAdjoint_conj`

 For a position `(v, i₀)` and `g` in `positionGroup ε v`, the matrix `i₀† g i₀` preserves the
form of signs `η`, where `i₀† = formAdjoint ε η i₀`. 

### `inducedHom`

 The map `g ↦ g' = i₀† g i₀` from the group `positionGroup ε v` of a position `(v, i₀)` to
`U(η)`, where `i₀† = formAdjoint ε η i₀`. 

### `inducedHom_eq`

 For a position `(v, i₀)`, if `g` in `positionGroup ε v` acts by `y` on the image of `i₀` modulo
the span of the first `d` columns of `v`, then `y` is the image `i₀† g i₀` of `g` in `U(η)`. 

### `periodIntegrand`

 The function `θ g = c_l g * conj (c_k g') * exp (conj (σ g) - σ g)` on the group of a position
`(v, i₀)`. Here `l` and `k` are integer vectors, doubled Harish-Chandra parameters for `U(ε)` and
`U(η)`; `c_l`, `c_k` are their discrete series coefficients `HCParam.dsCoeff`, given by
Flensted-Jensen's normalised integral over the maximal compact subgroup (`HCParam.flenstedJensen`);
`g' = inducedHom g = i₀† g i₀`; and `σ` is the sum `positionSum`. 

### `exists_inducedHom_eq`

 Let `(v, i₀)` be a position: the `d + 1` columns of `v` are independent, their products for the
form of signs `ε` vanish except that the last has norm `±1`, `i₀` is an isometry of `(ℂ^m, η)` into
their orthogonal complement, and `card n = card m + 2 d + 1`. Every `y` in the unitary group
`U(η) = USign η` of the form of signs `η` is the image `i₀† g i₀` of an element `g` of
`positionGroup ε v` that acts by `y` on the image of `i₀` and fixes its orthogonal complement. 

### `IsStationary.isLaplaceDatum`

 Let `(v, i₀)` be a stationary position for the parameters `l` and `k`, where `e` and `e'` place
the common coordinates `X` in `n` and `m`, and let `l` be steep: on `X` its sign is `+1` and its
weight is `0`, and on the other coordinates the signs alternate and the weight decreases strictly in
`[-3 B, -B]`. On `X` let `η = 1` and the weight of the lowest `K`-type of `k` vanish; let this
weight be nonnegative, and at most `3 B` unless `U(η)` is compact.

For `g` in the group `positionGroup ε v` let `g' = inducedHom g = i₀† g i₀`, and let `σ g` be
`positionSum g`, the sum over `j ≤ d` of the coefficient of `v_j` in `(g - 1) v_{j + 1}`. Then
`g ↦ (g, g')` and `φ = σ - conj σ` satisfy the hypotheses `IsLaplaceDatum` of Laplace's method:
`φ` is additive and imaginary and is the difference of the phases at `(g - 1, g' - 1)`, the traces
of `g - 1` and `g' - 1` agree, the conditions above on the weights hold, and the image of the map
contains `U(X)`, embedded diagonally. 

### `IsStationary.integrable_periodIntegrand_and_measure_le`

 **Lower bound for the period over the group of a position.** Let the integer vectors `l = 2 λ`
and `k = 2 λ'` be doubled Harish-Chandra parameters for `U(ε)` and `U(η)`. The weight of `l` is
`l.lowestKType = λ + ρ - 2 ρ_c`, the highest weight of the lowest `K`-type, and likewise for `k`.
Take a stationary position `(v, i₀)` of `U(η)` in `U(ε)`: the weight `μ` of `l`, as a diagonal
matrix, takes each of the first `d` columns of `v` to the next, `i₀† μ i₀` is the weight of `k`, and
`i₀` is the identity on the coordinates `X`, placed in `n` and `m` by `e` and `e'`. Let `l` be steep
with `B ≥ 1`. Let the weight of `k` vanish on `X`, where the signs are `+1`, be nonnegative, and be
at most `3 B` unless `U(η)` is compact. Let `L` bound the entries of `l` and `k`, let `β ≥ 10 ^ 12`
be at least `N + L`, where `N = card n + card m`, and let `h ≥ 10 ^ 30 (N² log β)³`. Let
`l.HasLargeGap h` hold: the entries of `l` are distinct, congruent to `card n - 1` mod 2, and
`|λ i - λ j| ≥ 500 (card n)³ + h` whenever `ε i ≠ ε j`. Let `k.HasLargeGap h` hold, the same
condition for `λ'`, `η` and `m`. Then `periodIntegrand` is integrable for every right invariant
measure `ν` on `positionGroup ε v` that is finite on compact sets, and the volume of the set of `g`
with operator norms `‖g‖, ‖i₀† g i₀‖ ≤ β + 1` is at most `β ^ (20 N²)` times the norm of its
integral.

Here `positionGroup ε v` is the group of the `g` in `U(ε)` such that, for `j ≤ d + 1`, `g - 1` maps
the span of `v_1, …, v_j` into that of `v_1, …, v_{j - 1}`. 

### `IsStationary.period_lower_bound_of_surjective`

 **The period over a group that maps onto the group of a position.** Let `(v, i₀)` be a
stationary position of `U(η)` in `U(ε)` for the parameters `l = 2 λ` and `k = 2 λ'`: the columns
`v₁, …, v_{d + 1}` of `v` are independent, their products vanish except that the last has norm
`±1`, `i₀` is an isometry into their orthogonal complement and the identity on the common
coordinates `X` (placed by `e`, `e'`), the weight `μ = l.lowestKType`, as a diagonal matrix, takes
`v_j` to `v_{j + 1}`, and `i₀† μ i₀` is `μ' = k.lowestKType`. Let `l` be steep with `B ≥ 1`: on
`X` the signs are `+1` and `μ = 0`, and off `X` the signs alternate and `μ` decreases strictly in
`[-3 B, -B]`. Let `μ'` vanish on `X`, where the signs are `+1`, be nonnegative, and be at most `3 B`
unless `U(η)` is compact. Let `HasLargeGap h` hold for `l` and `k`: the entries are distinct, of
the parity of the dimension minus one, and entries of `λ` (resp. `λ'`) of opposite signs differ by
at least `500 (dimension)³ + h`, the dimension being `card n` (resp. `card m`). Let `L` bound the
entries of `l` and `k`, `N = card n + card m`, `β ≥ 10 ^ 12`, `β ≥ N + L` and
`h ≥ 10 ^ 30 (N² log β)³`.

Let `j : S →* U(ε) × U(η)` and write `j s = (g, g')`.
Let `s ↦ g` be proper and onto `positionGroup ε v`, let `g - 1` take each `v_j` into the span of
the earlier ones, with `σ s` the sum of the coefficients of `v_j` in `(g - 1) v_{j + 1}`, and let
`g` act by `g'` on the image of `i₀` modulo `v₁, …, v_d`. For a right invariant measure `ν` on `S`
that is finite on compact sets, the volume of the set where `‖g‖, ‖g'‖ ≤ β + 1` is at most
`β ^ (20 N²)` times the norm of the integral of
`laplaceIntegrand = c_l g * conj (c_k g') * exp (conj (σ s) - σ s)`, with the discrete series
coefficients `c_l`, `c_k`. 

 ## Restriction to `U(ε)` 

### `IsPosition.gram_fromCols`

 Let `(v, i₀)` be a position of `U(ε)` in `U(ε ⊕ 1)` with one vector `v₁`, the only column of
`v`. If `v₁` has norm `1` for the form `ε ⊕ 1`, the matrix `(i₀, v₁)` preserves that form. 

### `conj_inl_sub_one`

 For `w` in `U(ε ⊕ 1)` and `g` in `U(ε)`: `w (g ⊕ 1) w⁻¹ - 1 = w ((g - 1) ⊕ 0) w⁻¹`. 

### `norm_conj_inl_le`

 If `g` in `U(ε)` is within `1` of the identity, then `‖w (g ⊕ 1) w⁻¹‖ ≤ 1 + ‖w‖²` for `w` in
`U(ε ⊕ 1)`, in the `L²` operator norm. 

### `conj_inl_sub_one_mul`

 For `w` in `U(ε ⊕ 1)` and `g` in `U(ε)`: `(w (g ⊕ 1) w⁻¹ - 1) w = w ((g - 1) ⊕ 0)`. 

### `lowersFlag_conj_inl_sub_one`

 Let `w = (i₀, v₁)` lie in `U(ε ⊕ 1)`, where `v₁` is the only column of `v`. For `g` in `U(ε)`
the element `w (g ⊕ 1) w⁻¹` fixes `v₁`: its difference with `1` lowers the flag of `v`, with sum of
coefficients `0`. 

### `inducesOn_conj_inl_sub_one`

 Let `w = (i₀, v₁)` lie in `U(ε ⊕ 1)`, where `v₁` is the only column of `v`. For `g` in `U(ε)`,
`InducesOn 0 v i₀` holds: `w (g ⊕ 1) w⁻¹ - 1` acts on the image of `i₀` as `g - 1`. So
`(w (g ⊕ 1) w⁻¹ - 1) i₀ = i₀ (g - 1)`. 

### `IsPosition.exists_conj_inl_eq`

 Let `(v, i₀)` be a position of `U(ε)` in `U(ε ⊕ 1)` with `d = 0`: `v` has a single column `v₁`,
of norm `±1` for the form `ε ⊕ 1`, and `i₀` is an isometry of `(ℂ^n, ε)` into its orthogonal
complement. Let `w = (i₀, v₁)` lie in `U(ε ⊕ 1)`. Every element `g` of `positionGroup (ε ⊕ 1) v`,
the stabilizer of `v₁`, has the form `w (y ⊕ 1) w⁻¹` with `y` in `U(ε)`. 

### `IsSteep.lowestKType_neg_mem`

 If `l` is steep (so its weight is `0` on `X` and in `[-3 B, -B]` elsewhere) and has a large gap,
the weight of the lowest `K`-type of `-l` lies in `[0, 3 B]`. 

### `sq_norm_fromCols_le`

 If the entries of `i₀` and of the only column of `v` have norm at most `R`, then the square
matrix `(i₀, v)` of size `card n + 1` has squared operator norm at most `(card n + 1)⁴ R²`. 

### `IsSteep.exists_isStationary_conjTranspose_mul_mul_eq_one`

 Let the integer vectors `l = 2 λ` for `U(ε)` and `-l'` for `U(ε ⊕ 1)` be steep with `B ≥ 1`: on
`X` the signs are `+1` and the weight of the lowest `K`-type is `0`; on the other `M`, resp.
`M + 1`, coordinates the signs are `+, -, +, …` and the weight decreases strictly in `[-3 B, -B]`.
Let `M` be even and let `λ` be a Harish-Chandra parameter with gap `500 (card n)³ + h` between
entries of opposite signs. Then `-l'`, `-l` have a stationary position with one vector `v`: an
isometry `i₀` of `(ℂ^n, ε)` into the orthogonal complement of `v`, the identity on `ℂ^X`, with
`i₀† μ' i₀ = μ` for the weights `μ'`, `μ` of `-l'`, `-l` as diagonal matrices. The form of signs
`ε ⊕ 1` has value `1` at `v`, and the entries of `v`, `i₀` have modulus at most `(6 B) ^ (M + 1)`.


### `IsSteep.exists_volume_le_mul_norm_integral_dsCoeff`

 **Restriction.** Let the parameter `l = 2 λ` of `U(ε)` be steep for `(X, M, B)` with `M` even
and `B ≥ 1`, and let `l' = 2 λ'` be a parameter of `U(ε ⊕ 1)` with `-l'` steep for `(X, M + 1, B)`.
With `n = card n`, let `HasLargeGap h` hold for both: the entries of `l` (resp. `l'`) are distinct
and of the parity of `n - 1` (resp. `n`), and two entries of `λ` (resp. `λ'`) at coordinates of
opposite sign differ by at least `500 n³ + h` (resp. `500 (n + 1)³ + h`). Let the entries of `l`,
`l'` be bounded by `L`, let `β ≥ 10¹²` bound `2 n + 1 + L` and `(n + 1)⁴ (6 B) ^ (2 M + 2)`, and let
`h ≥ 10³⁰ ((2 n + 1)² log β)³`.

Let `c_l`, `c_l'` be the discrete series coefficients `HCParam.dsCoeff`, given by Flensted-Jensen's
integral over the maximal compact subgroup, divided by the squared norm of the lowest `K`-type. The
measure `volume` on `U(ε)` is the Haar measure `haarU` made from Lebesgue measure by a Cayley chart,
with the compact dual normalisation. Then some `y` in `U(ε ⊕ 1)` with `‖y‖² ≤ β` has:
`β ^ (20 (2 n + 1)²)` times the modulus of the integral over `U(ε)` of
`c_l g * conj (c_l' (y⁻¹ (g ⊕ 1) y))` is at least the volume of `{g | ‖g - 1‖ ≤ 1}`. 
