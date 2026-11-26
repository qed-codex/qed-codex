---
{
  "module": "src/Lib/General/Measure/IdempotentKernel.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Measure/IdempotentKernel.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Measure/IdempotentKernel.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Fubini and convolution lemmas; idempotent kernels

General lemmas of measure and integration, and the notion of an idempotent kernel on a group.

* `New.IsBoundedMeasurable`: a strongly measurable function whose norm is bounded by a constant.
* `MeasureTheory.MeasurePreserving.integral_integral_comp`: Fubini's theorem along a
  measure-preserving map from a product; `MeasureTheory.MeasurePreserving.fubini` adds the
  integrability on the product.
* `New.integrable_integral_skew_product`, `New.integral_integral_skew_product`: Fubini's theorem
  after a substitution that preserves the measure on the space where it acts;
  `New.integral_skew_product` is the conjunction of the two.
* `New.integral_smul_integral_swap`, `New.integral_smul_integral_eq_integral_conv_smul`: the
  integral `∫ x, k x • ∫ g, α g • F (j x * g)`, for `g` in a group, in the opposite order and as a
  pairing with a convolution; `New.integral_conv` is the conjunction of the two.
* `New.IsIdempotentKernel`: a continuous integrable function `e` on a group with
  `e g⁻¹ = conj (e g)`, `e 1 ≠ 0` and `∫ e z * e ((z * x)⁻¹ * y) dz = e x⁻¹ / e 1 * e y`; in
  particular `e * e = e` (`New.IsIdempotentKernel.convolution_self`).

## Relation to the literature

The results of this file are standard. The lemmas on iterated integrals and on convolution on a
group are forms of Fubini's theorem, and `New.sq_lintegral_le` is the Cauchy–Schwarz inequality for
lower integrals, deduced from Hölder's inequality.


### `IsBoundedMeasurable`

 The function `F : Z → X` is strongly measurable, and its norm is bounded by one constant on all
of `Z`. 

### `IsBoundedMeasurable.stronglyMeasurable`

 `F` is strongly measurable. 

### `IsBoundedMeasurable.bounded`

 The norm of `F` is bounded by a constant. 

### `instance : Fact ((1 : ℝ≥0∞) ≠ ∞)`

 The extended nonnegative reals satisfy `1 ≠ ∞`, as a fact for instance search. 

### `IsBoundedMeasurable.of_continuous`

 A continuous function with bounded norm on a second countable Borel space is bounded and
strongly measurable. 

### `IsBoundedMeasurable.comp`

 The composition of a bounded strongly measurable function with a measurable map is bounded and
strongly measurable. 

### `IsBoundedMeasurable.memLp_top`

 A bounded strongly measurable function lies in `L^∞` for every measure. 

### `IsBoundedMeasurable.integrable_mul_comp`

 If `F` is strongly measurable and bounded, `c` is `ν`-integrable and `j` is measurable, then
`a ↦ c a * F (j a)` is `ν`-integrable. 

### `sq_lintegral_le`

 Cauchy–Schwarz inequality for lower integrals of functions with values in `[0, ∞]`: if `f`,
`g` are almost everywhere measurable and `h² ≤ f g` pointwise, then `(∫ h)² ≤ ∫ f * ∫ g`. 

### `_root_.MeasureTheory.MeasurePreserving.integral_integral_comp`

 Fubini's theorem along a map `T` carrying `ν × μ` (both s-finite) to `ρ`: for a `ρ`-integrable
`f`, one has `∫∫ f (T (k, g)) dμ(g) dν(k) = ∫ f dρ`. 

### `_root_.MeasureTheory.MeasurePreserving.fubini`

 Fubini's theorem along a map `T` carrying `ν × μ` (both s-finite) to `ρ`: for a `ρ`-integrable
`f`, the function `f ∘ T` is integrable and `∫∫ f (T (k, g)) dμ(g) dν(k) = ∫ f dρ`. 

### `integrable_integral_skew_product`

 Let `μ`, `ν` be s-finite, `T` jointly measurable with each `T k` preserving `μ`, and `f`
integrable for `ν × μ`. Then `g ↦ ∫ f (k, T k g) dν(k)` is `μ`-integrable. 

### `integral_integral_skew_product`

 Let `μ`, `ν` be s-finite, `T` jointly measurable with each `T k` preserving `μ`, and `f`
integrable for `ν × μ`. Then `∫∫ f (k, T k g) dν(k) dμ(g) = ∫∫ f (k, g) dμ(g) dν(k)`. 

### `integral_skew_product`

 Let `μ`, `ν` be s-finite, `T` jointly measurable with each `T k` preserving `μ`, and `f`
integrable for `ν × μ`. Then `g ↦ ∫ f (k, T k g) dν(k)` is `μ`-integrable, and its integral is
`∫∫ f (k, g) dμ(g) dν(k)`. 

### `integrable_mul_smul_comp_mul`

 For integrable `k` and `α`, strongly measurable bounded `F` and measurable `j : W → Z` into a
group, the function `(x, g) ↦ (k x * α g) • F (j x * g)` is integrable on the product. 

### `integral_smul_integral_swap`

 For integrable `k` and `α`, strongly measurable bounded `F` and measurable `j : W → Z` into a
group, the iterated integral of `k x • α g • F (j x * g)` does not depend on the order of
integration. 

### `integral_smul_integral_eq_integral_conv_smul`

 Let `μ` be left invariant on the group `Z`, `j : W → Z` measurable, `k` and `α` integrable and
`F` strongly measurable and bounded. Then `∫ k(x) ∫ α(g) F(j(x) g) dμ(g) dν(x)` equals
`∫ β(g) F(g) dμ(g)`, where `β(g) = ∫ k(x) α(j(x)⁻¹ g) dν(x)` is the convolution of `k`, carried
along `j`, and `α`. 

### `integral_conv`

 For left invariant `μ`, the double integral `∫ k(x) ∫ α(g) F(j(x) g) dμ(g) dν(x)` equals both
the integral in the opposite order and the integral of `F` against the convolution of `k`, carried
along `j`, and `α`. 

### `IsIdempotentKernel`

 The function `e` is a continuous integrable idempotent kernel on the group `G`: `e g⁻¹` is the
conjugate of `e g`, `e 1 ≠ 0`, and `∫ e z * e (x⁻¹ z⁻¹ y) dz = e x⁻¹ * e y / e 1`, the integral
being against `volume` on `G`. 

### `IsIdempotentKernel.continuous`

 `e` is continuous. 

### `IsIdempotentKernel.integrable`

 `e` is integrable. 

### `IsIdempotentKernel.apply_inv`

 The value of `e` at `g⁻¹` is the complex conjugate of its value at `g`. 

### `IsIdempotentKernel.apply_one_ne_zero`

 `e` does not vanish at the identity. 

### `IsIdempotentKernel.convolution_eq`

 With `δ_x` the point mass at `x`, the convolution `e * δ_x * e` is `e x⁻¹ / e 1` times `e`. 

### `IsIdempotentKernel.convolution_self`

 Let `e : G → ℂ` be an idempotent kernel on the group `G` (`IsIdempotentKernel`): it is
continuous and integrable for `volume`, `e g⁻¹` is the conjugate of `e g`, `e 1 ≠ 0`, and
`∫ e z * e ((z * x)⁻¹ * y) dz = e x⁻¹ * e y / e 1` for all `x`, `y`. Then for every `y`,
`∫ e z * e (z⁻¹ * y) dz = e y`, that is `e * e = e`; this is the defining identity at `x = 1`. 
