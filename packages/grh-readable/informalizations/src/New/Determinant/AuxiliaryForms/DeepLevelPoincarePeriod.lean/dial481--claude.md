---
{
  "module": "src/New/Determinant/AuxiliaryForms/DeepLevelPoincarePeriod.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/AuxiliaryForms/DeepLevelPoincarePeriod.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/AuxiliaryForms/DeepLevelPoincarePeriod.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Steep parameters of Y₀ and Ỹ^0_0; periods of Poincaré series of deep level

At every infinite place, the parameter of `Y₀` and minus the parameter of `Ỹ^0_0 = Y₀ ⊕ E ẽ` are
steep in the sense of `New.DiscreteSeries.IsSteep`. Separately, at deep level the period over `V`
of a Poincaré series on `V ⊕ ⟨1⟩` is approximated by the term of the identity coset.

## Main definitions and results

* `New.Data.exists_isSteep`: for one numbering of the indices, the parameter of `Y₀` (`z = false`)
  and minus that of `Ỹ^0_0` (`z = true`) satisfy `New.DiscreteSeries.IsSteep` at every infinite
  place `τ`. That is, the highest weight `New.HCParam.lowestKType` of the lowest `K`-type vanishes
  on a block of indices of sign `+`. On the other indices the signs alternate and it decreases
  strictly within `[-3B, -B]`, `B = D.liftWeight 0 τ`. `New.Data.gridSigns` gives the signs and
  `New.Data.gridParam` twice these parameters.
* `New.Exchange.poincareKernel`: the function whose translates a Poincaré series sums. Its real
  factor here is `New.Exchange.translatedCoeff`, a translated product of matrix coefficients.
* `New.Space.IsLastColumn`: a rational vector of `V ⊕ ⟨1⟩` is the last column of a group element
  `γ`, that is, the vector `γ ẽ` for the last basis vector `ẽ`. Last columns index the cosets, and
  `New.Space.IsLastColumn.le_norm_archCoords_sub` separates them.
* `New.Exchange.norm_poincare_period_sub_le`: at deep level the period equals the term of the
  identity coset up to a small error.

Notions from other files:
* `New.Data.Φ`: the set of infinite places of the field `E` of the data `D`. Also, `D.ϱ` is the
  number of hyperbolic planes of `Y₀`, `D.InitIndex 0` the set of basis indices of `X₀` other than
  the last and `D.GridIndex z 0 0` the index set of `Y₀` or `Ỹ^0_0`.
* `Φ w` in the bounds `R ≤ ‖Φ w a‖`: the complex embedding of `E` at the infinite place `w`.
* `V.move x`, `vecAtPoint`, `archCoords`: the space `V` at the point `x` of the adelic group, the
  adelic coordinates of a rational vector there, and their infinite part as a Euclidean vector.
* `New.Data.liftWeight`: the number `κ_j(σ) = κ(σ) + (j + 1/2) Δ` at the infinite place `σ`, where
  `κ` is `D.weight`, `Δ = D.gap` the gap and `D.halfGap` half the gap.
* `New.GInf E s`: the product of one copy `New.USign s` of the complex unitary group `U(diag s)`
  for each infinite place of `E`. For an integer vector `l : New.HCParam s`, read as twice a
  Harish-Chandra parameter, `l.dsCoeff` is the Flensted-Jensen matrix coefficient on `U(diag s)`,
  and `l.HasLargeGap A` says that `l` has gap at least `500 n ^ 3 + A`, for `n` the rank.
* `New.signedSpace E s`: the standard space with matrix `diag(s)`; it needs a primitive root of
  unity of order `5040` in `E` (`New.HasPrimitiveRoot5040`).
* `New.Space.Γ`, `New.Space.quotMeasure`: the rational points of a hermitian space `V` inside the
  adelic unitary group `G E s`, and the measure on a fundamental domain for them.
* `New.principalLevel`: the finite adelic integral points congruent to `1` modulo an element `a`
  of the ring of integers of `E`.


 ## Steepness of the discrete series parameters at infinite places 

### `New.Data.abs_targetParameter_sub_lowestKType_le_and_eq`

 At an infinite place `τ`, let `ν` number the indices `D.GridIndex z 0 0` of the node `(0, 0)` of
the grid `Y` (`z = false`) or `Ỹ`, sending an index `y` to `i = ν y`. Assume its doubled parameter
`D.gridParam z 0 0 0 τ y` is `2 (D.targetParameter τ i) + z.toNat`. Assume its sign
`D.gridSigns z 0 0 0 y` is `entrySign 0 0 (i + 1 - k)`: `+` on the first `k - 1` entries (the near
entries, `i + 1 < k`; `k = D.k` is the rank of the source) and alternating on the others. Let `L` be
`2 (D.targetParameter τ i) + z.toNat` minus twice the weight of the lowest `K`-type at `y`, and let
`N = D.r + z.toNat` be the number of indices. Then `|L| ≤ N`. At a near entry,
`L + N = N + min N k - 1 - 2 i - (N - k) % 2`. 

### `New.Data.exists_isSteep`

 Let `D` be admissible data for the fixed parameters `P`. The parameter of the object `Y₀`
(`z = false`), of rank `D.r`, and minus that of `Ỹ^0_0 = Y₀ ⊕ E ẽ` (`z = true`, one more index),
whose doubles are `D.gridParam z 0 0 0 τ` (offset `0` at the node `(0, 0)`, lift number `0`), are
steep: for one numbering `e` of their indices, at every infinite place `τ`, the sign is `+` and the
weight of the lowest `K`-type is `0` on the block `D.InitIndex 0` of the basis indices of `X₀`
other than the last. On the other `2 ϱ + 2` (and for `Ỹ^0_0` one more) indices, `ϱ = D.ϱ` being the
number of hyperbolic planes of `Y₀`, the signs alternate and the weight decreases strictly within
`[-3 B, -B]`, where `B = D.liftWeight 0 τ` is the weight `κ + Δ / 2` for the weight `κ` and gap
`Δ` of the data. 


## Periods of Poincaré series of deep level

The cosets are indexed by their last columns. The last columns of those that meet the level
condition are well separated, so a packing bound controls the sum of the terms other than that of
the identity.


### `New.Space.hasSum_integral_translates`

 Unfolding: the translates by the rational points `V.Γ` of an integrable function on the adelic
group are integrable for the quotient measure, and their integrals sum to its integral. 

### `New.Exchange.translatedCoeff`

 The product over the infinite places `w` of the conjugate of the Flensted-Jensen matrix
coefficient `(l w).dsCoeff` of the doubled parameter `l w`, evaluated at `(α w)⁻¹ * g w * ω w`. 

### `New.Exchange.sliceConst`

 The constant in the decay of the slices of `translatedCoeff l α ω`: the product over the
infinite places `w` of `(2 (‖α w‖ ‖ω w‖)²) ^ A` and `16 ^ A` times the volume of the unit ball
around `1` in `U(s)`. 

### `New.Exchange.norm_dsCoeff_translate_le`

 Decay of a translated matrix coefficient on `U(diag s)`: if `l` has a large gap for `2 A`, then
the norm of `l.dsCoeff` at `α⁻¹ x ω` is at most `(2 (‖α‖ ‖ω‖)²) ^ A * (2 / ‖x‖) ^ A * ‖x‖⁻¹ ^ A`
in the operator norm. 

### `New.Exchange.integrable_translatedCoeff_and_integral_norm_le`

 Let `E` be a CM field. Let each parameter `l w` have a large gap for `2 A` (gap at least
`500 N ^ 3 + 2 A` for `N = card n + 1`), and let `A > 8 N²`. Let `inl s 1` be the block embedding
`r ↦ diag(r, 1)`. Let `t > 0` bound below the products over the infinite places `w` of the operator
norms of `g w * inl s 1 (r w)`. The function `translatedCoeff l α ω` is the product over the places
of the conjugates of the discrete series matrix coefficients of parameters `l w`, taken at
`(α w)⁻¹ * g w * ω w`. Its slice `r ↦ translatedCoeff l α ω (g * inl s 1 ∘ r)` is integrable on the
real group `GInf E s` (one copy of `U(diag s)` for each place). The integral of its norm is at most
`sliceConst A α ω * t⁻¹ ^ A`. 

### `New.G.inlLine`

 The embedding `h ↦ h ⊕ 1` of the unitary group of signs `s` in that of signs `s ⊕ 1`. Its
image fixes the last basis vector. 

### `New.G.inlLine_snd_mem_principalLevel_iff`

 The block matrix `h ⊕ 1` has principal level `a` if and only if `h` has. 

### `New.Space.IsLastColumn`

 The rational vector `y` of `V ⊕ ⟨1⟩` is the last column of `γ`: in the coordinates at any point
`u` it is the last column of the adelic matrix of `u⁻¹ γ (k ⊕ 1)`, for every `k`. Here `⟨1⟩` is
the standard line `signedSpace E 1`; it needs a primitive root of unity of order `5040` in `E`. 

### `New.Space.exists_isLastColumn`

 If `E` has a primitive root of unity of order `5040`, every rational point `γ` of `V ⊕ ⟨1⟩`
has a last column: a rational vector whose coordinates are those of the image under `γ` of the
last basis vector. 

### `New.Space.IsLastColumn.inv_mul_mem_range`

 If `γ` and `γ'` have the same last column `y` (`V.IsLastColumn`), then `γ⁻¹ * γ'` lies in the
image of `inlLine E s`. 

### `New.Space.IsLastColumn.le_norm_archCoords_sub`

 Separation of last columns, for `E` with a primitive root of unity of order `5040`. Let
`y ≠ y'` be the last columns of `γ` and `γ'`, and let `(x ⊕ 1)⁻¹ γ (k ⊕ 1)` and
`(x ⊕ 1)⁻¹ γ' (k' ⊕ 1)` have finite part of level `a ≠ 0`. If `|a| ≥ R ≥ 0` at all infinite
places, the distance of `y` and `y'` at the point `x ⊕ 1` is at least `R` times the first minimum
of `V` at `x`: the least length of a nonzero lattice vector there, cut off at `1`. 

### `New.Space.IsLastColumn.norm_archCoords_one_le`

 If `y` is the last column of `1` in `V ⊕ ⟨1⟩` (`hy : V.IsLastColumn 1 y`), then in the space
moved to the point `x ⊕ 1` the length of `y` (the norm of `archCoords y`) is at most the number of
infinite places of `E`. 

### `New.Space.IsLastColumn.norm_archCoords_le`

 At the point `x ⊕ 1`, the last column of `γ` has length at most the number of infinite places
times the product of the local operator norms of `(x ⊕ 1)⁻¹ γ (k ⊕ 1)`, for every `k`. 

### `New.Space.tsum_eq_tsum_cosets`

 Let `E` have a primitive root of unity of order `5040`. A sum over the rational points of
`V ⊕ ⟨1⟩` is a sum over the cosets of the rational points of `V`, embedded by
`inlLine E s : h ↦ h ⊕ 1`. Here `C` is a set of representatives, and `W ⊆ C` contains every `σ`
for which `p` is nonzero somewhere on `σ (G E s ⊕ 1)`, in adelic points. 

### `New.Space.hasSum_integral_of_summable_integral_norm`

 Unfolding of a countable family `P` of integrable functions whose `L¹` norms are summable: the
integrals of the `P i` over the group sum to the integral over the quotient of the sum of all
translates of all `P i` by `V.Γ`. 

### `New.Exchange.integrable_mul_indicator`

 The product of an integrable function on the real group and the indicator function of the level
`a ≠ 0` is integrable on the adelic group. 

### `New.Exchange.integral_norm_mul_indicator`

 The `L¹` norm of `ψ` times the indicator function of the level `a ≠ 0` is the `L¹` norm of
`ψ` on the real group times the volume of the level. 

### `New.Exchange.integral_mul_indicator_mul_eq_smul_realConv`

 For `F` of level `a`, the integral of `ψ` times the indicator function of the level against the
translate of `F` by `x` is the volume of the level times `realConv ψ F x`, the integral of
`r ↦ ψ r * F (x * (r, 1))` over the real group (right convolution). 

### `New.Exchange.poincareKernel`

 The kernel of a Poincaré series: the function `φ` of the real part of `g` times the indicator
function of the level `K` at its finite part. 

### `New.Exchange.poincareKernel_mul_inlLine`

 Let `E` be a CM field and let the finite part of `g` have principal level `a`. Then the kernel
of level `a` at `g (h ⊕ 1)` is the value of `φ` at the real part of `g (h ⊕ 1)` times the indicator
function of the level `a` at the finite part of `h`. 

### `New.Exchange.integral_norm_poincareKernel_le`

 Decay of one term of a Poincaré series over a CM field `E`. The kernel `poincareKernel φ K g` is
`φ` at the real part of `g` times the indicator function of `K` at its finite part. Here
`φ = translatedCoeff l α ω` is the product over the infinite places `w` of the conjugated discrete
series coefficients of parameters `l w` at `(α w)⁻¹ * g w * ω w`, and `K` is the principal level
`a`. Let each `l w` have a large gap for `2 A`, with `A > 8 (card n + 1)²`, and let `g (k ⊕ 1)` have
finite part of level `a ≠ 0`. Let `t > 0` bound below the products over the infinite places of the
operator norms of `g (h ⊕ 1)`. Then the kernel at `g (h ⊕ 1)` is integrable in `h`. Its `L¹` norm is
at most the volume of the principal level `a` in `Gf E n` times `sliceConst A α ω * t⁻¹ ^ A`. 

### `New.Exchange.tsum_div_norm_pow_le_of_separated`

 The packing bound. Let the points `col i` of a real normed space of finite dimension at most
`A - 2` have mutual distances at least `d²`, and let `‖col base‖ ≤ d` with `d ≥ 10`. Then the sum
of `(d / ‖col i‖) ^ A` over `i ≠ base` converges and is at most `10 / d`. 

### `New.Exchange.norm_poincare_period_sub_le`

 The period of a Poincaré series of deep level is its main term, up to a small error. Let `E`
have a primitive root of unity of order `5040` and let `F` be automorphic on `V` of level `a ≠ 0`
and bounded by `S`. Let the parameters `l w` for `V ⊕ ⟨1⟩` have a large gap for `2 A`, and let
`φ = translatedCoeff l α ω`, the product over the infinite places `w` of their conjugated discrete
series coefficients at `(α w)⁻¹ * g w * ω w`. Let `|a| ≥ R ≥ 0` at all infinite places and
`d² ≤ R λ`, where `λ = (V.move x).firstMinimum` is the least length of a nonzero lattice vector at
the point `x`, cut off at `1`. Let `d ≥ 10` be at least the number `f` of infinite places,
`A ≥ 2 f (N + 1) + 2` and `A > 8 (N + 1)²` for `N = card n`. Then the function `ψ : r ↦ φ (r ⊕ 1)`
on the real group of `V` is integrable. The period against `F` of the series with centre `x ⊕ 1`
differs from the volume of `principalLevel n a` times `realConv ψ F x` by at most that volume times
`sliceConst A α ω * S * (10 / d)`. 
