---
{
  "module": "src/New/Appendix/DiscreteSeries/MinorSecondOrder.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Appendix/DiscreteSeries/MinorSecondOrder.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Appendix/DiscreteSeries/MinorSecondOrder.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# One minor of a product of three exponentials, to second order

For an orthogonal projection `Q` and small matrices `A₁`, `A₂`, `A₃` we expand
`log det (1 + Q (exp A₁ exp A₂ exp A₃ - 1))` to second order. The rest vanishes to order three in
the `Aᵢ` and to order two in their parts that cross `Q`; Schwarz's lemma turns this into the bound
`O(δ ζ²)`, where `δ` bounds the `Aᵢ` and `ζ` bounds the commutators `⁅Q, Aᵢ⁆`. All norms are
Hilbert–Schmidt (Frobenius) norms, and no constant depends on the dimension.

The main result is `exists_det_one_add_proj_mul_eq_exp`. The order three is obtained by direct
estimates of the exponential series and of the integral that defines the logarithm. The rest
`logMinorRemainder` is a principal logarithm, holomorphic in the factor `τ` that scales the crossing
parts, and Schwarz's lemma is applied in `τ`.

Notions from other files:
* `logOneAdd M = ∫ s in 0..1, (1 + s M)⁻¹ M` is the matrix logarithm `log (1 + M)`, used for
  `‖M‖ ≤ 1 / 2`.
* `IsStarProjection Q` says that `Q` is an orthogonal projection: self-adjoint and idempotent.

## Relation to the literature

See `New.Appendix.DiscreteSeries.Periods` for related work.


 ### Expansion of a determinant to second order 

### `exists_exp_eq_add_mul`

 For a matrix `A` of Frobenius norm at most `1 / 2`, the exponential series after its terms of
order at most two is `A` times a matrix `R` of norm at most `‖A‖ ^ 2`. 

### `norm_trace_inv_one_add_smul_mul_sub_le`

 For `‖M‖ ≤ 1 / 2` in Frobenius norm and `0 ≤ s ≤ 1`, the trace of `(1 + s M)⁻¹ M` is
`tr M - s tr M²` up to an error of at most `2 ‖M‖³`. 

### `norm_trace_logOneAdd_sub_le`

 For a matrix `M` of Frobenius norm at most `1 / 2`, the trace of the matrix logarithm
`logOneAdd M = log (1 + M)` is `tr M - tr M² / 2` up to an error of at most `2 ‖M‖³`. 

### `IsExpansion`

 `IsExpansion Q Y L S ρ` says that `Y = L + S + ⋯` is an expansion in a small quantity `ρ`:
the term `L` is of first order, `Y - L` is of second order, and the rest `Y - L - S` is of third
order when measured by the trace against `Q`, which keeps the bound free of the dimension. 

### `IsExpansion.norm_linear_le`

 The term `L` is of first order. 

### `IsExpansion.norm_sub_linear_le`

 The difference `Y - L` is of second order. 

### `IsExpansion.norm_trace_rest_le`

 The trace of `Q` times the rest is of third order. 

### `IsExpansion.norm_le`

 If `Y = L + S + ⋯` is an expansion in `ρ ≤ 1 / 3`, so that `‖L‖ ≤ ρ` and `‖Y - L‖ ≤ ρ ^ 2`,
then `‖Y‖ ≤ 4 ρ / 3`. 

### `isExpansion_exp`

 For an orthogonal projection `Q` and `‖A‖ ≤ ρ ≤ 1 / 2` in Frobenius norm, the series
`exp A - 1 = A + A² / 2 + ⋯` is an expansion in `ρ`: `‖A‖ ≤ ρ`, `‖exp A - 1 - A‖ ≤ ρ ^ 2`, and the
trace of `Q` times the rest `exp A - 1 - A - A² / 2` has norm at most `ρ ^ 3`. 

### `IsExpansion.mul`

 Expansions multiply. Let `Q` be an orthogonal projection. Let `Y - 1 = L + S + ⋯` be an
expansion in `ρ ≤ 1 / 3`, that is, `‖L‖ ≤ ρ`, `‖Y - 1 - L‖ ≤ ρ²` and
`‖tr Q (Y - 1 - L - S)‖ ≤ ρ³`, and let `Y' - 1 = L' + S' + ⋯` be one in `ρ' ≤ 1 / 3`. Then
`Y Y' - 1 = (L + L') + (S + S' + L L') + ⋯` is an expansion in `ρ + ρ'`. 

### `IsExpansion.exists_det_one_add_mul_eq_exp`

 Let `Q` be an orthogonal projection and `Y = L + S + ⋯` an expansion in `ρ ≤ 1 / 3`. Then
`det (1 + Q Y)` is the exponential of `tr Q L + tr Q S - tr (Q L)² / 2 + r` with `‖r‖ ≤ 8 ρ³`. 

### `crossTrace`

 The trace of `Q A (1 - Q) B`. For a projection `Q` it involves only the blocks of `A` and `B`
that cross `Q`, that is, that map the range of `Q` to its kernel or the kernel to the range. 

### `crossTrace_eq_trace_sub_trace`

 The crossing trace `tr Q A (1 - Q) B` is `tr Q A B - tr Q A Q B`. 

### `crossTraceSum`

 The sum of the crossing traces `crossTrace Q Aᵢ Aⱼ = tr Q Aᵢ (1 - Q) Aⱼ` over `i ≤ j`, with the
terms `i = j` halved: `∑ᵢ tr Q Aᵢ (1 - Q) Aᵢ / 2 + ∑_{i < j} tr Q Aᵢ (1 - Q) Aⱼ`. 

### `expMinor`

 The determinant `det (1 + Q (exp A₁ exp A₂ exp A₃ - 1))`. For an orthogonal projection `Q` it
is the principal minor of `exp A₁ exp A₂ exp A₃` on the range of `Q`. 

### `logMinorQuadratic`

 The terms of first and second order in `log (expMinor Q A₁ A₂ A₃)`, namely
`∑ᵢ tr Q Aᵢ + ∑ᵢ tr Q Aᵢ (1 - Q) Aᵢ / 2 + ∑_{i < j} tr Q Aᵢ (1 - Q) Aⱼ`. 

### `logMinorRemainder`

 The principal logarithm of the quotient of the minor `expMinor Q A₁ A₂ A₃` by the exponential
of the main terms `logMinorQuadratic Q A₁ A₂ A₃`. For small `Aᵢ` it is the sum of the terms of order
three and more in `log (expMinor Q A₁ A₂ A₃)`. 

### `exists_expMinor_eq_cexp`

 Let `Q` be an orthogonal projection and let `A₁`, `A₂`, `A₃` have Frobenius norm at most
`ρ ≤ 1 / 10`. Then the minor `expMinor Q A₁ A₂ A₃ = det (1 + Q (exp A₁ exp A₂ exp A₃ - 1))` is the
exponential of `logMinorQuadratic Q A₁ A₂ A₃ + r` for some `r` with `‖r‖ ≤ 216 ρ³`. 

### `expMinor_eq_cexp_logMinorQuadratic_add_logMinorRemainder`

 Let `Q` be an orthogonal projection and let `A₁`, `A₂`, `A₃` have Frobenius norm at most
`ρ ≤ 1 / 10`. Then the minor `expMinor Q A₁ A₂ A₃ = det (1 + Q (exp A₁ exp A₂ exp A₃ - 1))` is the
exponential of the traces `logMinorQuadratic` of first and second order in the `Aᵢ` plus the rest
`logMinorRemainder`, the principal logarithm of the minor divided by `exp logMinorQuadratic`. 

### `norm_logMinorRemainder_le_of_norm_le`

 Let `Q` be an orthogonal projection and let `A₁`, `A₂`, `A₃` have Frobenius norm at most
`ρ ≤ 1 / 10`. Then the rest `logMinorRemainder Q A₁ A₂ A₃`, the sum of the terms of order three and
more in `log det (1 + Q (exp A₁ exp A₂ exp A₃ - 1))`, has norm at most `216 ρ³`. 

### `expMinor_mul_mem_slitPlane`

 Let `Q` be an orthogonal projection and let `A₁`, `A₂`, `A₃` have Frobenius norm at most
`ρ ≤ 1 / 10`. Then the minor `expMinor Q A₁ A₂ A₃ = det (1 + Q (exp A₁ exp A₂ exp A₃ - 1))` divided
by the exponential of `logMinorQuadratic Q A₁ A₂ A₃ = ∑ᵢ tr Q Aᵢ + ∑'_{i ≤ j} tr Q Aᵢ (1 - Q) Aⱼ`
(the terms `i = j` halved) lies in the slit plane, away from the cut of the principal logarithm. 

### `one_add_mul_exp_sub_one`

 If `Q` is idempotent and commutes with `A`, then `1 + Q (exp A - 1) = exp (Q A)`. 

### `logMinorRemainder_eq_zero`

 If `Q` is idempotent and commutes with `A₁`, `A₂`, `A₃`, then the rest
`logMinorRemainder Q A₁ A₂ A₃` vanishes. 

### `logMinorRemainder_conj`

 The rest `logMinorRemainder`, the logarithm of the quotient of
`det (1 + Q (exp A₁ exp A₂ exp A₃ - 1))` by the exponential of the traces `logMinorQuadratic` of
first and second order, does not change when the `Aᵢ` are conjugated by an involution `U` that
commutes with `Q`. 

 ### Scaling the crossing parts 

### `crossPart`

 The crossing part `Q A (1 - Q) + (1 - Q) A Q` of `A`: for a projection `Q`, the two off-diagonal
blocks of `A` with respect to the range and the kernel of `Q`. 

### `scaleCross`

 The matrix `A` with its crossing part `Q A (1 - Q) + (1 - Q) A Q` multiplied by `τ`. 

### `commute_scaleCross_zero`

 For an idempotent `Q`, the matrix `scaleCross Q A 0`, that is `A` without its crossing part
`Q A (1 - Q) + (1 - Q) A Q`, commutes with `Q`. 

### `scaleCross_neg`

 For an idempotent `Q`, conjugation by the involution `2 Q - 1` changes the sign of the factor
`τ` by which `scaleCross Q A τ` multiplies the crossing part `Q A (1 - Q) + (1 - Q) A Q` of the
matrix `A`. 

### `norm_crossPart`

 For an orthogonal projection `Q`, the crossing part `Q A (1 - Q) + (1 - Q) A Q` has the same
Frobenius norm as the commutator `⁅Q, A⁆`. 

### `norm_sub_crossPart_le`

 For an orthogonal projection `Q`, removing from `A` its crossing part
`Q A (1 - Q) + (1 - Q) A Q` does not increase the Frobenius norm. 

### `norm_scaleCross_le`

 Let `Q` be an orthogonal projection, `‖A‖ ≤ δ` and `‖⁅Q, A⁆‖ ≤ ζ` (Frobenius norms). Multiplying
the crossing part `Q A (1 - Q) + (1 - Q) A Q` of `A` by `τ` with `‖τ‖ ζ ≤ δ` gives a matrix of norm
at most `2 δ`. 

### `differentiable_expMinor_scaleCross`

 The minor `det (1 + Q (exp A₁ exp A₂ exp A₃ - 1))` is an entire function of the factor `τ` that
multiplies the crossing parts `Q Aᵢ (1 - Q) + (1 - Q) Aᵢ Q` of the `Aᵢ`. 

### `differentiable_logMinorQuadratic_scaleCross`

 The sum `∑ᵢ tr Q Aᵢ + ∑'_{i ≤ j} tr Q Aᵢ (1 - Q) Aⱼ` (the terms `i = j` halved) is an entire
function of the factor `τ` that multiplies the crossing parts `Q Aᵢ (1 - Q) + (1 - Q) Aᵢ Q`. 

### `norm_le_mul_sq_of_even`

 Schwarz's lemma for an even function: if `f` is holomorphic and bounded by `C` on the disc of
radius `R`, even, and zero at the origin, then `‖f z‖ ≤ C (‖z‖ / R) ^ 2` on the disc. 

### `logMinorRemainder_scaleCross_neg`

 For an idempotent `Q`, multiply the crossing parts `Q Aᵢ (1 - Q) + (1 - Q) Aᵢ Q` of the `Aᵢ` by
`τ`, which gives `Bᵢ = scaleCross Q Aᵢ τ`. Then the rest `logMinorRemainder Q B₁ B₂ B₃`, the
principal logarithm of the quotient of `det (1 + Q (exp B₁ exp B₂ exp B₃ - 1))` by the exponential
of the traces `logMinorQuadratic` of first and second order, is an even function of `τ`. 

### `norm_logMinorRemainder_le`

 Let `Q` be an orthogonal projection, `0 < ζ < δ ≤ 1 / 20`, and let `A₁`, `A₂`, `A₃` have
Frobenius norm at most `δ` and commutators with `Q` of Frobenius norm at most `ζ`. Then
`logMinorRemainder Q A₁ A₂ A₃`, the sum of the terms of order three and more in
`log det (1 + Q (exp A₁ exp A₂ exp A₃ - 1))`, has norm at most `216 (2 δ)³ (ζ / δ)²`. 

### `exists_det_one_add_proj_mul_eq_exp`

 Let `Q` be an orthogonal projection, `δ ≤ 1 / 20`, and let `A₁`, `A₂`, `A₃` have Frobenius norm
at most `δ` and commutators with `Q` of Frobenius norm at most `ζ`. Then
`det (1 + Q (exp A₁ exp A₂ exp A₃ - 1))` is the exponential of
`∑ᵢ tr Q Aᵢ + ∑'_{i ≤ j} tr Q Aᵢ (1 - Q) Aⱼ + r` with `‖r‖ ≤ 10⁴ δ ζ²`, where `∑'` halves the terms
`i = j`; the second sum is `crossTraceSum Q A₁ A₂ A₃`. 
