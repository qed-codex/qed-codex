---
{
  "module": "src/New/Determinant/Twist/LongForms.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Twist/LongForms.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Twist/LongForms.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Theorem C: integral forms are long

The main result `New.Data.integral_forms_long` bounds from below the covolume plus twice the index
of a family of target forms that spans almost all of the target. The target forms are a twisted
lattice, and the bound follows from `New.TwistedLattice.covolume_add_index_nonneg` with four inputs:
auxiliary forms that complete a family to a basis, a family of twists `ξ_ι`, the injectivity of the
lifts `Θ_ξ`, and the height of `Z(1) / Z(ξ_ι)`.

In comments, `d` is the dimension `D.targetDim` of the target `D.targetForms`, the space of good
forms on `Y₀ = D.spaceY 0`. The letters `x, x₁, b, a, m, k, t, f` are the numbers `D.x`, `D.x₁`, …
of the data `D`; inequalities between them come from `New.Data.le_of_hasLogBound`.

Notions from other files:
* `D.targetLattice`: the target forms as a twisted lattice, with the lifts `Θ_ξ = D.Θ ξ` indexed by
  the `m`-fold twists `ξ`; the modulus `Q(ξ)` has norm `ξ.normQ`.
* `D.chainDeterminant ξ` is `Z(ξ) = det (Θ_ξ* Θ_ξ)`, and `D.liftDeterminant ξ j` is `Z_j(ξ ^ j)`,
  the same determinant for the `j`-th single lift.
* `HeightLe c y`: the family `y` of complex numbers, one for each pair `ι` of a prime `l` and an
  isomorphism `ℂ ≃ ℚ̄_l` (`PrimePadicIso`), has height at most `c`.
* `D.HasSmallRatios θ`: the `m`-fold twists `ξ_ι = θ ι` have `Nm Q(ξ_ι)` prime to the prime of `ι`
  and inverse ratios of Hecke values of height at most `x₁`.


 ### Auxiliary forms 

### `IsAuxiliaryForm`

 A target form `y` is auxiliary for the scalars `γ ϑ`, one for each `m`-fold twist `ϑ`, if its
lifts `γ ϑ • D.Θ ϑ y` are integral at primes not dividing `ϑ.normQ` and every conjugate of its lift
`D.Θ 1 y` has squared norm at most `exp (2 x₁² b²)`. 

### `IsAuxiliaryForm.smul_lift_mem_integralForms`

 The form `γ ϑ • Θ_ϑ y` is integral at `ι : ℂ ≃ ℚ̄_l` whenever the norm `ϑ.normQ` of the
  modulus of `ϑ` is prime to `l = ι.1`. 

### `IsAuxiliaryForm.normSqAt_lift_le`

 The conjugate of `Θ₁ y` by each automorphism `σ` of `ℂ` has squared norm at most
  `exp (2 x₁² b²)`. 

### `exists_span_isAuxiliaryForm_eq_top`

 **Auxiliary forms.** There are an integer `e` and numbers `γ ϑ ≠ 0`, for the `m`-fold twists
`ϑ`, such that `γ 1 = 1`, the absolute value of `γ ϑ` is the norm `ϑ.normQ` of the modulus of `ϑ` to
the power `e / 2` times the numbers `D.turnRatio i j ϑ` for `0 ≤ i, j < m`, and the space
`D.targetForms` is spanned by the forms `y` that are auxiliary for `γ`: each lift `γ ϑ • D.Θ ϑ y` is
integral at the primes not dividing `ϑ.normQ`, and every conjugate of `D.Θ 1 y` has squared norm at
most `exp (2 x₁² b²)`, for the scales `x₁`, `b` of `D`. 

### `HasSmallRatios.heightLe_inv_rpow_mul_prod_turnRatio`

 Let `ξ_ι = θ ι` be a family of `m`-fold twists, one for each `ι : ℂ ≃ ℚ̄_l`. Assume the family
has small ratios: `Nm Q(ξ_ι) = (θ ι).normQ` is prime to `l`, and the inverse ratios of Hecke
L-values have height at most `x₁`. Let `e` be an integer. Then the inverse of the product of
`Nm Q(ξ_ι) ^ (e / 2)` and the `m²` numbers `D.turnRatio i j ξ_ι` (for `i, j < m`) has height at most
`m² t x₁`. 

### `mul_completion_cost_le`

 The cost of completing a family to a basis: if `n ≥ (1 - 4 / b²) d` and `d = n + n'`, where
`d = D.targetDim`, then `n' (2 x₁² b² + b) ≤ d b`. That is, `n'` forms, each costing `2 x₁² b² + b`,
cost at most `d b` in total. 

 ### The inverse ratio 

### `exists_hasSmallRatios_heightLe_liftDeterminant_div`

 **Single lifts at good twists.** There is a family of `m`-fold twists `ξ_ι = θ ι`, one for each
prime `l` and `ι : ℂ ≃ ℚ̄_l`, with small ratios such that for `1 ≤ j ≤ m` the family
`Z_j(1) / Z_j(ξ_ι ^ j)` has height at most `d (f a log⁴ b / m - k D.directionAmount)`. 

### `exists_chainDeterminant_one_div_eq`

 The inverted factorisation of the Gram determinant `D.chainDeterminant ϑ` of the lift `D.Θ ϑ`:
for an integer `e` independent of the `m`-fold twist `ϑ`, the quotient
`D.chainDeterminant 1 / D.chainDeterminant ϑ` is the product of the same quotients for the Gram
determinants `D.liftDeterminant` of the single lifts, times the `D.targetDim`-th power of the
inverse of a scalar. The scalar is the norm `ϑ.normQ` of the modulus of `ϑ` to the power `e / 2`,
times the numbers `D.quotientRatio i j ϑ` for `1 ≤ i < j ≤ m`, each the product of `D.t` ratios of
Hecke L-values of the character `D.untwistedLiftChar j / D.untwistedLiftChar i` at `ϑ ^ (j - i)`;
the characters `D.untwistedLiftChar j` of `U(1)(𝔸)` are those of the lifts at the trivial twist. 

### `heightLe_chainDeterminant_one_div`

 **The inverse ratio.** Let the family of `m`-fold twists `ξ_ι = θ ι`, one for each
`ι : ℂ ≃ ℚ̄_l`, have small ratios, and suppose that for `1 ≤ j ≤ m` the family
`D.liftDeterminant 1 j / D.liftDeterminant ξ_ι j` of quotients of Gram determinants of the `j`-th
single lift has height at most `d (f a log⁴ b / m - k D.directionAmount)`. Then the family
`Z(1) / Z(ξ_ι)` has height at most `d (b + f a log⁴ b - D.mainAmount)`, where
`D.mainAmount = m k D.directionAmount`. 

 ### The lower bound 

### `integral_forms_long`

 **Theorem C: integral forms are long.** Let `y_1, …, y_n` be independent target forms with
`n ≥ (1 - 4 / b²) d`. Suppose that `y` has index at most `δ`: there are `δ_l ≥ 0` with
`∑ δ_l log l ≤ δ` such that for each `ι` an `ι`-integral matrix, with determinant of valuation at
most `δ_l`, takes `y` to forms integral at `ι`. Suppose that `y` has covolume at most `c`: the Gram
determinant of every conjugate of the untwisted lift `D.Θ 1 y` is at most `exp c` in absolute value.
Then `c + 2 δ ≥ d (D.mainAmount - 3 f a log⁴ b)`. 
