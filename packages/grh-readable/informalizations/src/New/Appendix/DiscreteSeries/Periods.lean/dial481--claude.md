---
{
  "module": "src/New/Appendix/DiscreteSeries/Periods.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Appendix/DiscreteSeries/Periods.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Appendix/DiscreteSeries/Periods.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Lower bounds for periods by Laplace's method

This file proves lower bounds for periods of discrete series coefficients. Let
`j : S →* U(ε) × U(η)` be a homomorphism and write `θ` for the function `laplaceIntegrand` on `S`.
Laplace's method bounds the volume of a large ball by a power of `β` times `‖∫ θ‖`, where `β` bounds
the dimensions and the entries of the parameters.

## Main definitions and results

* The values of `θ` lie in a cone about the positive real axis, up to an exponentially small error
  (`IsLaplaceDatum.norm_laplaceIntegrand_le_mul_re_add`). With the decay of the coefficients, `θ` is
  integrable and the volume of a large ball is at most a power of `β` times `‖∫ θ‖`
  (`IsLaplaceDatum.laplace_method`). The file `PositionGroup` applies this to the group of a
  stationary position.

Notions from other files:
* `USign ε` is the unitary group `U(ε)` of the diagonal form with signs `ε`, and
  `U.sum (signMatrix_sum ε η)` is the block embedding `(g, g') ↦ g ⊕ g'` of `U(ε) × U(η)`.
* `l.dsCoeff g` is the discrete series coefficient with doubled Harish-Chandra parameter
  `l = 2λ : HCParam ε`, given by Flensted-Jensen's integral and normalised to take the value `1`
  at the identity; `l.lowestKType` is the highest weight of its lowest `K`-type. On the maximal
  compact subgroup it is the coefficient at the highest weight vector of this `K`-type
  (`New.dsCoeff_of_mem_maxCompactU`).
* A parameter `l = 2λ` indexed by `n` has gap `A` if its entries are distinct and congruent to
  `card n - 1` mod 2, and `|λ a - λ b| ≥ A` whenever `ε a ≠ ε b`; `l.HasLargeGap h` says that `l`
  has gap `500 (card n)³ + h`.
* `l.laplaceIntegrand k j φ s` is the coefficient of `l` at the first component of `j s`, times the
  conjugate of the coefficient of `k` at the second, times `exp (-φ s)`.
* `IsLaplaceDatum l k j τ B e φ` collects the hypotheses of Laplace's method. Let `μ`, `μ'` be the
  weights `l.lowestKType`, `k.lowestKType` and let `j s = (g, g')`.
  - The parameter `l` is steep (`IsSteep`) for the splitting `e : X ⊕ Fin M ≃ n`: on `X` the sign is
    `+1` and `μ` is `0`; on the other `M` indices the signs are `+, -, +, …` and `μ` decreases
    strictly in `[-3 B, -B]`.
  - The weight `μ'` is nonnegative, at most `3 B` if `η` takes both signs, and `0` on the image of
    `τ : X → m`, where the sign is `+1`.
  - The phase `φ s = tr (μ (g - 1)) - tr (μ' (g' - 1))` is additive and imaginary, and
    `tr (g - 1) = tr (g' - 1)`.
  - For each unitary `u` indexed by `X` there is an `s` such that `g - 1` and `g' - 1` are `u - 1`
    extended by zero along `e` and along `τ`.

## Relation to the literature

This file is the step of Laplace's method that makes restriction periods explicitly large. Near 1 a
discrete series coefficient of U(p,q) is an explicit phase times a number close to the interval
[0,1], up to a tenth of its size and an exponentially small error, so that the losses at the
archimedean places are at most powers of the weights. The integral formula for coefficients,
non-vanishing of periods and fixed-rank asymptotics for coherent states are known in the literature.
Related work: Nelson–Venkatesh, The orbit method and analysis of automorphic forms, 2021; H. He, On
the Gan–Gross–Prasad conjecture for U(p,q), 2017; B. Sun, Matrix coefficients of cohomologically
induced representations, 2007.


### `norm_mul_sub_mul_le`

 Let `a, c, t ∈ [0, 1]`. If `u` is within `a / 10 + t` of `a` and `v` within `c / 10 + t` of `c`,
then `u v` is within `0.21 a c + 4 t` of `a c`. 

### `norm_le_two_mul_re_add`

 A complex number `z` within `0.21 p + 4 t` of a real number `p ≥ 0` lies in the cone
`‖z‖ ≤ 2 re z + 12 t`. 

### `inv_one_add_sq_pow_le_exp_pow_four`

 If `T ≥ 1`, `T ρ = 10⁻¹³` and `h ≥ 10³⁰ T³`, then `(1 + ρ²) ^ (-h) ≤ exp (-100 T) ^ 4`. 

### `le_pow_mul_of_le`

 Let `β ≥ 16`, `N ≥ 1` and `V, I ≥ 0`; in the application `V` and `W` are the volumes of a large
and a small ball and `I` is the norm of an integral. If `V ≤ β ^ (16 N) W` and
`W / 4 ≤ 2 I + 6 β ^ (-50 N) 16 ^ (9 N) V`, then `V ≤ β ^ (20 N) I`, as the error term contributes
at most `V / 2`. 

### `eighteen_mul_le_of_mul_pow_three_le`

 If `N ≥ 1`, `t ≥ 1` and `h ≥ 10³⁰ (N t)³`, then `h ≥ 18 N`. 

### `IsLaplaceDatum.norm_laplaceIntegrand`

 Under `IsLaplaceDatum` the phase `φ` is imaginary, so the factor `exp (-φ s)` of
`laplaceIntegrand` has modulus one, and the modulus at `s` is the product of the moduli of the
discrete series coefficients at the two components of `j s`. 

### `IsLaplaceDatum.norm_laplaceIntegrand_le_of_far`

 **Away from the maximal compact subgroup.** Let `j` and `φ` satisfy `IsLaplaceDatum` (so `φ` is
imaginary), let `T ≥ 1` and `T ρ = 10⁻¹³`, and let both doubled parameters `l`, `k` have gap
`500 · (dimension)³ + h` with `h ≥ 10³⁰ T³`. If the noncompact parts `y`, `y'` of the components of
`j s` (the entries that join indices of opposite signs) have `‖y‖² + ‖y'‖² ≥ ρ²` in the Frobenius
norm, then `laplaceIntegrand` has modulus at most `exp (-100 T)` at `s`. 

### `coe_sum_eq_fromBlocks`

 The matrix of the block sum `U.sum (signMatrix_sum ε η) g` of `g.1` in `U(ε)` and `g.2` in
`U(η)` is the block diagonal matrix `fromBlocks g.1 0 0 g.2`. 

### `norm_coe_sum_eq_max`

 The operator norm of the block sum `g.1 ⊕ g.2` of elements of the unitary groups `U(ε)` and
`U(η)` is the larger of the two norms. 

### `norm_sum_sub_one`

 The distance to `1`, in the operator norm, of the block sum `g.1 ⊕ g.2` of elements of the
unitary groups `U(ε)` and `U(η)` is the larger of the two distances to `1`. 

### `isProperMap_sum`

 Let `j s = (g, g')` in `U(ε) × U(η)`. If `s ↦ g` is proper and `s ↦ g'` is continuous, then the
block diagonal sum `s ↦ g ⊕ g'` is a proper map to `U(ε ⊕ η)`. 

### `IsLaplaceDatum.one_div_four_le_norm_laplaceIntegrand`

 Let `j` and `φ`, defined on a group `S`, satisfy `IsLaplaceDatum` (so `φ` is imaginary). Let the
doubled parameters `l`, `k` have gap `500 · (dimension)³ + h` and entries bounded by `L`, with
`card n + card m + L ≤ β`. Suppose `j s = (g, g')` and the block diagonal sum `g ⊕ g'` is within
`(200 β⁵)⁻¹` of `1` in the operator norm. Then `laplaceIntegrand` at `s` has norm at least `1 / 4`,
as each coefficient has norm at least `1 / 2`. 

### `IsLaplaceDatum.norm_laplaceIntegrand_le_mul_re_add_of_near`

 **The cone near the identity.** Let `j` and `φ` satisfy `IsLaplaceDatum`: in particular `φ` is
additive, and for `(g, g') = j s` it is `φ s = tr (μ (g - 1)) - tr (μ' (g' - 1))`. Let both
parameters have gap `500 · (dimension)³ + h` and entries bounded by `L`, let
`card n + card m + L ≤ β` and `log β ≥ 1`, put `T = (card n + card m)² log β` and let `δ T ≤ 10⁻¹²`.
If `g - 1` and `g' - 1` have Frobenius norm at most `δ`, then `z = laplaceIntegrand s` lies in the
cone `‖z‖ ≤ 2 re z + 12 exp (-100 T)`. 

### `IsLaplaceDatum.norm_laplaceIntegrand_le_mul_re_add`

 **The cone.** Let `j` and `φ` satisfy `IsLaplaceDatum` with `B ≥ 1`: the weight of the lowest
`K`-type of `l` is `0` on `X` and decreases in `[-3 B, -B]` elsewhere, that of `k` is nonnegative
and `0` on `X`, the difference `φ` of the two phases is additive and imaginary, and the image of `j`
contains `U(X)`, placed in the two factors by `e` and `τ`. Let the entries of `l` and `k` be bounded
by `L`, let `card n + card m + L ≤ β` and `log β ≥ 1`, and put `T = (card n + card m)² log β`. Let
both doubled parameters have gap `500 · (dimension)³ + h` with `h ≥ 10³⁰ T³`. Then every value `z`
of `laplaceIntegrand` at an `s`, with `j s = (g, g')`, satisfies
`‖z‖ ≤ 2 re z + 12 exp (-100 T)`. 

### `IsLaplaceDatum.norm_laplaceIntegrand_le_pow`

 **Decay.** Let `j` and `φ` satisfy `IsLaplaceDatum` (so `φ` is imaginary). Let `l` and `k`
satisfy `HasLargeGap h`, i.e. have gap `500 · (dimension)³ + h`. Let `c ≤ h` and `j s = (g, g')`,
and write `g ⊕ g'` for the block diagonal sum `U.sum (signMatrix_sum ε η) (j s)` in `U(ε ⊕ η)`. Then
the norm of `laplaceIntegrand` at `s` is at most `(2 / ‖g ⊕ g'‖) ^ c`, where `‖g ⊕ g'‖` is the
operator norm. 

### `norm_le_two_mul_re_add_mul`

 If `‖z‖ ≤ 2 re z + 12 E²` and `‖z‖ ≤ G²` with `E, G ≥ 0`, then `‖z‖ ≤ 2 re z + 6 E G`: this is
the geometric mean of the bounds `12 E²` and `3 G²` for `‖z‖ - 2 re z`. 

### `IsLaplaceDatum.norm_laplaceIntegrand_le_two_mul_re_add_mul_pow`

 **The cone with a decaying error.** Let `j` and `φ` satisfy `IsLaplaceDatum` with `B ≥ 1`. Let
the entries of `l` and `k` be bounded by `L`, let `log β ≥ 1` and `card n + card m + L ≤ β`, and put
`N = (card n + card m)²`. Let both doubled parameters have gap `500 · (dimension)³ + h`, with
`h ≥ 10³⁰ (N log β)³`. Write `j s = (g, g')` and `z` for the value at `s` of `laplaceIntegrand`.
Then `‖z‖ ≤ 2 re z + 6 β ^ (-50 N) (2 / ‖g ⊕ g'‖) ^ (9 N)`. 

### `IsLaplaceDatum.norm_laplaceIntegrand_le_two_mul_re_add`

 **The pointwise bounds.** Let `j` and `φ` satisfy `IsLaplaceDatum` with `B ≥ 1`, let the entries
of `l` and `k` be bounded by `L`, let `β ≥ 3` and `card n + card m + L ≤ β`, put
`N = (card n + card m)²`, and let both parameters have gap `500 · (dimension)³ + h` with
`h ≥ 10³⁰ (N log β)³`. Write `j s = (g, g')`, `G = (2 / ‖g ⊕ g'‖) ^ (9 N)` in the operator norm and
`z` for the value at `s` of `laplaceIntegrand`. Then `‖z‖ ≤ G` and
`‖z‖ ≤ 2 re z + 6 β ^ (-50 N) G`. 

### `measureReal_div_four_le`

 Integration of the bound `‖f‖ ≤ 2 re f + c G`: if moreover `‖f‖ ≥ 1 / 4` on `A`, then
`ν(A) / 4 ≤ 2 ‖∫ f‖ + c ∫ G`. 

### `norm_le_add_one_of_norm_sub_one_le`

 If a square matrix `A` has `‖A - 1‖ ≤ 1` in the operator norm and `r ≥ 1`, then
`‖A‖ ≤ r + 1`. 

### `measure_large_ball_le_pow_mul_small_ball`

 The covering bound for two radii, for a right invariant measure `ν` on `S` and the `L²` operator
norm: for `J : S →* U(ζ)` with `ζ` indexed by `ι` and `β ≥ 10¹²`, the volume of `{‖J s‖ ≤ β + 1}` is
at most `β ^ (16 (card ι)²)` times that of `{‖J s - 1‖ ≤ (200 β⁵)⁻¹}`. 

### `IsLaplaceDatum.laplace_method`

 **Laplace's method.** Let `j : S →* U(ε) × U(η)` and `φ` satisfy `IsLaplaceDatum` with `B ≥ 1`:
the weight of the lowest `K`-type of `l` is `0` at the indices `e (inl x)`, `x : X`, and decreases
in `[-3 B, -B]` elsewhere, that of `k` is nonnegative and `0` on the image of `τ`, the difference
`φ` of the two phases is additive and imaginary, and the image of `j` contains `U(X)`, placed in the
two factors by `e` and `τ`. Let the first component of `j` be proper and the second continuous, and
let `ν` be a right invariant measure on `S` that is finite on compact sets. Let the entries of the
Harish-Chandra parameters `l = 2λ`, `k` (doubled) be bounded by `L`, let `β ≥ 10¹²` bound
`card n + card m + L`, and let both have gap `500 · (dimension)³ + h` with
`h ≥ 10³⁰ ((card n + card m)² log β)³`. Then the function `θ = laplaceIntegrand` is integrable, and
the volume of the set of `s` at which both components of `j s` have operator norm at most `β + 1` is
at most `β ^ (20 (card n + card m)²) ‖∫ θ‖`. 
