---
{
  "module": "src/Lib/DiscreteSeries/Bessel/SchurBound.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Bessel/SchurBound.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Bessel/SchurBound.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Traces and L² bounds for Bessel functions

This file collects tools for estimating integrals of Bessel functions. It writes σ(u) + conj σ(u⁻¹),
for the sum σ(u) of simple root entries, as a trace against a fixed matrix. It proves abstract `L²`
bounds for convolutions on a unimodular group, and shows that norms of Bessel functions are
invariant under the Bessel subgroup `S = New.Shape.Form.besselS`.

## Main definitions and results

* `New.Filling.besselCharMatrix`, `New.Filling.trace_besselCharMatrix_mul`: a fixed matrix C with
  tr(C u) = σ(u) + conj σ(u⁻¹) for every isometry u of the form `New.Shape.Form.splitGram`.
* `New.IsBoundedMeasurable.integral_inner_translate`: if `F * ψ = F` for an idempotent kernel `ψ`
  with `ψ 1 = d`, the inner products of the right translates of `F` are values of `ψ / d` times
  `‖F‖²`.
* `New.IsIdempotentKernel.enorm_integral_convolve_sq_le`: Schur's bound for a family of vectors of a
  Hilbert space with these inner products.
* `New.IsBoundedMeasurable.lintegral_sq_convolve_convolve_le`: the bound for `F * x` convolved once
  more with an integrable function.
* `New.IsBesselFunction.enorm_besselS_mul`: the norm of `W (s y)` equals that of `W y` for `s` in
  `S`.

Notions from other files:
* `New.convolve F x`: The function `y ↦ ∫ x a⁻¹ • F (y * a)`.
* `New.IsIdempotentKernel ψ`: `ψ` is continuous and integrable, `ψ g⁻¹ = conj (ψ g)`, `ψ 1 ≠ 0`,
  and `ψ * δ_t * ψ = (ψ t⁻¹ / ψ 1) ψ`.
* `New.orbitMeasure ρ volume`: A measure on `G` against which a left `S`-invariant function has the
  same integral as on `S \ G`.

## Relation to the literature

Known; see `Lib.DiscreteSeries.Bessel.UnipotentHaarMeasure` and `Lib.DiscreteSeries.CuspKernel` for
sources.



## The sum of the simple root entries as a trace against a fixed matrix

Let σ(u) = `New.simpleRootSum` u be the sum of the entries of u just above the diagonal on the frame
(e_0, …, e_{ϱ-1}, z) (`New.Shape.besselFrame`). Here A is a commutative star ring.


### `besselCharMatrix`

 The matrix C, indexed by the Bessel index set, for which tr(C u) is the sum of the entries
u_{j,j+1} on the frame (e_0, …, e_{ϱ-1}, z) plus the entries of J u in row `besselFrame a.succ` and
column `eStar a`, for a : Fin ϱ. Here J = `New.Shape.Form.splitGram` T. 

### `trace_besselCharMatrix_mul`

 For u in `T.G`, an isometry of the form, so J u = (u⁻¹)ᴴ J for J = `New.Shape.Form.splitGram` T,
tr(Cu) = σ(u) + conj σ(u⁻¹), where C = `New.Filling.besselCharMatrix` T and σ = `New.simpleRootSum`
sums the entries u_{j,j+1} on the frame. 

### `simpleRootSum_inv`

 On the Bessel subgroup S (`New.Shape.Form.besselS`), σ(u⁻¹) = −σ(u), where σ is the sum
`New.simpleRootSum` of the entries just above the diagonal on the frame. 


## Schur orthogonality and L² bounds for convolutions

Let `G` be a unimodular group. Write `F * x` for `New.convolve F x`, the function
`y ↦ ∫ x a⁻¹ • F (y * a)`.


 ### General facts on integrals and the convolution 

### `lintegral_enorm_sq`

 If `F` is integrable and essentially bounded for `ν`, the lower integral of `‖F‖ₑ ^ 2` is the
Bochner integral of `‖F‖ ^ 2`. 

### `IsIdempotentKernel.integral_inv_mul_translate`

 Schur's orthogonality relation for an idempotent kernel `ψ`:
`∫ ψ a⁻¹ * ψ (g * (a * y)) da = ψ g / ψ 1 * ψ y`, where `ψ a⁻¹ = conj (ψ a)`. 

### `convolve_star`

 For an idempotent kernel `ψ` and a function `x` with `ψ * x = x`, the function
`x⋆ y = conj (x y⁻¹)`, written `⟪x y⁻¹, 1⟫` here, satisfies `x⋆ * ψ = x⋆`. 

### `integrable_convolve`

 The convolution of two integrable functions is integrable. 

### `IsBoundedMeasurable.continuous_convolve`

 On a second countable locally compact group G with two-sided Haar measure, for F : G → E
bounded and strongly measurable, E a Hilbert space, and x integrable, y ↦ ∫ x(a⁻¹) F(ya) da
is continuous. 

### `IsBoundedMeasurable.convolve_right`

 The convolution of a bounded strongly measurable function with an integrable function is
bounded and strongly measurable. 

### `IsBoundedMeasurable.integrable_smul`

 For bounded strongly measurable `F` and integrable `x`, the function `a ↦ x a • F (y * a)` is
integrable. 

### `IsBoundedMeasurable.convolve_assoc`

 Convolution is associative, `(F * x) * z = F * (x * z)`, for bounded strongly measurable `F`
and integrable `x` and `z`. 

### `IsBoundedMeasurable.identDistrib_norm_translate`

 Let `F` be bounded and strongly measurable, with `F (s * y) = c s • F y` for `s` in the subgroup
`S`, where `|c g| = 1` for all `g : G`. Then a right translation does not change the distribution
of `‖F‖` for the measure `ν` on `G` that integrates over `S \ G` (`New.orbitMeasure`). 

### `IsBoundedMeasurable.integrable_prod_translate`

 If `x` is integrable and `F` is bounded, transforms under `S` by factors `c s` of modulus one
and is integrable for the measure `ν` of `S \ G`, then `(a, y) ↦ x a⁻¹ • F (y * a)` is integrable
for `volume.prod ν`. 

### `IsBoundedMeasurable.integral_inner_convolve`

 Let `F` be bounded, integrable for the measure `ν` of `S \ G` and transform under `S` by
factors `c s` of modulus one, and let `x` be integrable. Then the `ν`-pairing with a bounded
strongly measurable function `h` commutes with the convolution `F * x` (`New.convolve`):
`∫ ⟪h y, (F * x) y⟫ ∂ν = ∫ x a⁻¹ * (∫ ⟪h y, F (y * a)⟫ ∂ν) da`. 

### `IsBoundedMeasurable.integral_inner_translate`

 Let `F * ψ = F` for an idempotent kernel `ψ` with `ψ 1 = d`, where `F` is bounded, transforms
under `S` by factors `c s` of modulus one and is integrable for the measure `ν` of `S \ G`. Then
the inner product in `L²(ν)` of the right translates of `F` by `a` and `b` is `ψ (a⁻¹ b) / d`
times the squared norm of `F`. 

### `IsBoundedMeasurable.integral_smul_convolve`

 The average of the values of `F * x` against an integrable function `z` is the value at `1` of
the convolution of `F` with `x * (a ↦ z a⁻¹)`. 

### `IsBoundedMeasurable.inner_convolve`

 For bounded strongly measurable `F` and integrable `x`, the inner product with a fixed vector
commutes with the integral `convolve F x g = ∫ x a⁻¹ • F (g * a)`. 

### `continuous_of_inner_eq`

 A map `w` of the group `G` into an inner product space with `⟪w a, w b⟫ = k (a⁻¹ * b)` for a
continuous function `k` is continuous. 

### `IsIdempotentKernel.integral_mul_conj_translate`

 Schur's orthogonality relation on `G`: if `ψ` is a bounded idempotent kernel with `ψ 1 = d` and
`x` is integrable with `ψ * x = x`, then `∫ x (a⁻¹ g) * conj (x (b⁻¹ g)) dg` is
`ψ (a⁻¹ * b) / d` times the squared `L²` norm of `x`. 

 The vectors `w a` below stand for the translates `π(a) v₀` of a vector `v₀` of a unitary
representation with `∫ ψ a⁻¹ • π(a) v₀ = v₀` and `‖v₀‖ ^ 2 = q`; only their inner products are
used. The vectors `convolve w x g = ∫ x a⁻¹ • w (g * a)` are the translates of one vector in the
closed span of the `w a`. 

### `IsIdempotentKernel.isBoundedMeasurable_of_inner_eq`

 If `⟪w a, w b⟫ = ψ (a⁻¹ * b) / d * q` for an idempotent kernel `ψ` with `ψ 1 = d`, then `w` is
strongly measurable and bounded: it is continuous and `‖w a‖ ^ 2 = q`. 

### `IsIdempotentKernel.inner_convolve_eq`

 Let `ψ` be an idempotent kernel with `ψ 1 = d`, `x` integrable with `ψ * x = x`, and
`⟪w a, w b⟫ = ψ (a⁻¹ * b) / d * q`. Then the coefficient of `convolve w x g` with `w a` is
`q / d * x (a⁻¹ * g)`. 

### `IsIdempotentKernel.norm_convolve_sq`

 For an idempotent kernel `ψ` with `ψ 1 = d`, an integrable `x` with `ψ * x = x` and vectors
with `⟪w a, w b⟫ = ψ (a⁻¹ * b) / d * q`, the squared norm of `convolve w x 1` is
`‖x‖₂ ^ 2 * q / d`. 

### `IsIdempotentKernel.integrable_inner_convolve`

 Let `ψ` be an idempotent kernel with `ψ 1 = d`, `x` integrable with `ψ * x = x`, and
`⟪w a, w b⟫ = ψ (a⁻¹ * b) / d * q`. For `u` in the span of the `w a`, the coefficient
`g ↦ ⟪u, convolve w x g⟫` is integrable. 

### `IsIdempotentKernel.integral_inner_convolve_mul`

 Schur's orthogonality relation for the translates of `v = convolve w x 1` and finite
combinations `u`, `u'` of the vectors `w a`: `∫ ⟪u, convolve w x g⟫ * ⟪convolve w x g, u'⟫ dg` is
`‖v‖ ^ 2 / d * ⟪u, u'⟫`. Here `ψ` is a bounded idempotent kernel with `ψ 1 = d`, `x` is integrable
with `ψ * x = x`, and `⟪w a, w b⟫ = ψ (a⁻¹ * b) / d * q`. 

### `enorm_sq_le_of_forall_mem_inner_sq_le`

 If a vector `V` of an inner product space lies in the closure of a subspace `H` and
`‖⟪u, V⟫‖ ^ 2 ≤ B * ‖u‖ ^ 2` for every `u` in `H`, then `‖V‖ ^ 2 ≤ B`. 

### `IsIdempotentKernel.enorm_integral_convolve_sq_le`

 **Schur's bound.** Let `ψ` be a bounded idempotent kernel with `ψ 1 = d`, `x` integrable with
`ψ * x = x`, and `⟪w a, w b⟫ = ψ (a⁻¹ * b) / d * q`. The average of the translates of
`v = convolve w x 1` against an integrable function `z` has squared norm at most
`‖v‖ ^ 2 ‖z‖₂ ^ 2 / d`. 

 ### Schur's bound in `L²(S ∖ G)` 

### `IsBoundedMeasurable.memLp_two`

 A bounded measurable function that is integrable for `ν` is square integrable for `ν`. 

### `IsIdempotentKernel.apply_one_nonneg`

 The value at `1` of an idempotent kernel, if real, is nonnegative: it is the integral of the
squared absolute value of the kernel. 

### `IsBoundedMeasurable.lintegral_sq_convolve_convolve_le`

 Schur's bound in `L²(S ∖ G)`, for the vector `F * x` in the closed span of the right translates
of `F`, where `G` is a locally compact Polish group with Haar measure `volume`. Here
`ν = orbitMeasure ρ volume` is a measure on `G` that integrates over `S ∖ G`, for an s-finite,
inversion-invariant measure `ρ` on the subgroup `S` admitting a cutoff. The bounded measurable `F`
is integrable for `ν` and transforms under `S` by factors `c s` of modulus one; `ψ` is a bounded
idempotent kernel with `ψ 1 = d` and `F * ψ = F`; the integrable `x` has `ψ * x = x`; and `z` is any
integrable function on `G`. The squared `ν`-norm of `(F * x) * (a ↦ z a⁻¹)` is then at most
`‖x‖₂ ^ 2 ‖F‖₂ ^ 2 ‖z‖₂ ^ 2 / d ^ 2`. 


## Left invariance of norms of Bessel functions under the Bessel subgroup

A Bessel function (`New.IsBesselFunction rep W`) is a bounded strongly measurable vector-valued
function on `New.Shape.G₁` that transforms on the left by a character under the unipotent group
`New.Shape.Form.besselU` and by the unitary representation `rep` under `New.RealPlace.embedH`.
Together these generate the Bessel subgroup `S = New.Shape.Form.besselS`.


### `enorm_integral_besselS_mul`

 For `s` in the Bessel subgroup `besselS` and a Bessel function `W` (a bounded function with
values in a unitary representation that transforms under `besselS`), replacing `g` by `s * g` does
not change the norm of a weighted integral of right translates of `W`. 

### `enorm_besselS_mul`

 The norm of a Bessel function `W` is invariant under left multiplication by the Bessel
subgroup. 
