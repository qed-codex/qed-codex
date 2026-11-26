---
{
  "module": "src/Lib/Analytic/PrimeNumberTheorem/Tauberian.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/PrimeNumberTheorem/Tauberian.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/PrimeNumberTheorem/Tauberian.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A Tauberian theorem with a power of the logarithm

Let `R` be measurable and Lipschitz on `v ≥ 0`, and let its transform `∫₀^∞ R(v) e^{(1 - s) v} dv`
be `(F s - F 1) / (s - 1)` in `re s > 2`. Suppose that for all large `l` the function `F` is
holomorphic and at most `l ^ A` on `re s ≥ 1 - l ^ (-A)`, `|s| ≤ e ^ l`. Then `R(v) = O(v ^ (-B))`
for every `B`. The theorem is meant for the remainder in the prime number theorem for a sum over
prime powers with weights that vanish at the cutoff `x`: at `x = e ^ v` it is Lipschitz in `v`.

The proof reads one Taylor coefficient of the transform at a far point `1 + H` in two ways. It is a
mean of `R` against a Gamma density that is concentrated at the given point `u`, hence close to
`R(u)`; and it is small by Cauchy's estimate on a disc that reaches left of the line `re s = 1`.

## Relation to the literature

Known result: the passage from a zero-free region to the error term of the prime number theorem.
Source: Montgomery and Vaughan, Multiplicative Number Theory I, 2007, Section 6.2, where a contour
integral is used in place of the Taylor coefficient.


### `iteratedDeriv_transform`

 Differentiation under the integral sign. Let `R` be measurable with `|R v| ≤ C e^v` for
`v ≥ 0`, and let `Φ s` be its transform `∫₀^∞ R(v) e^{(1 - s) v} dv` in `re s > 2`. Then, for such
`s`, the function `(-v)^k R(v) e^{(1 - s) v}` is integrable on `(0, ∞)`, and its integral is the
`k`-th derivative of `Φ` at `s`. 

### `integrableOn_and_integral_pow_mul_exp_neg_mul`

 For `H > 0` the moments of `e^{-H v}` on `(0, ∞)` exist: the function `v ^ j e^{-H v}` is
integrable there, with integral `j! / H ^ (j + 1)`. 

### `integrableOn_and_integral_gamma_mul_quadratic`

 For `H > 0` and the mean `u = (k + 1) / H` of the Gamma density
`H ^ (k + 1) v ^ k e^{-H v} / k!`, the function `v ^ k e^{-H v} (a + b (v - u)²)` is integrable on
`(0, ∞)`, with integral `k! / H ^ (k + 1) (a + b (k + 1) / H²)`. 

### `norm_taylorCoeff_transform_sub_le`

 Let `R` be measurable with `|R v| ≤ C e^v` for `v ≥ 0`, let `Φ s` be its transform
`∫₀^∞ R(v) e^{(1 - s) v} dv` in `re s > 2`, and let `H > 1`. The number
`(-H) ^ k H Φ⁽ᵏ⁾(1 + H) / k!` is the mean of `R` for the Gamma density
`H ^ (k + 1) v ^ k e^{-H v} / k!`, which has mean `(k + 1) / H` and variance `(k + 1) / H²`. So if
`|R v - c| ≤ a + b (v - (k + 1) / H)²` for all `v > 0`, it is within `a + b (k + 1) / H²` of `c`. 

### `norm_iteratedDeriv_dslope_le`

 Cauchy's estimate for the derivatives of the slope `(F s - F 1) / (s - 1)`, written
`dslope F 1`, at `1 + H`: if `F` is holomorphic and at most `M` in norm on the disc of radius
`H + η` about `1 + H`, the `k`-th one is at most `k! (2 M / η) / (H + η) ^ k`. Indeed
`|s - 1| ≥ η` on the boundary of the disc. 

### `norm_taylorCoeff_dslope_le`

 The normalised Taylor coefficient `(-H) ^ k H / k! · g⁽ᵏ⁾(1 + H)` of the slope `g = dslope F 1`,
that is `(F s - F 1) / (s - 1)`, is at most `4 M H / η · exp (-(k + 1) η / (2 H))` in norm if `F`
is holomorphic and at most `M` in norm on the disc about `1 + H` that reaches to `1 - η`, with
`0 < η ≤ H`. The exponential bounds the gain `(H / (H + η)) ^ (k + 1)`. 

### `abs_sub_le_of_unit_steps`

 If `|R v - R u| ≤ L (v - u)` for all steps `0 ≤ u ≤ v ≤ u + 1`, then `R` is Lipschitz with
constant `L` on `[0, ∞)`. 

### `norm_taylorCoeff_transform_sub_le_of_lipschitz`

 Let `R` be measurable and Lipschitz with constant `L` on `[0, ∞)`, with transform
`Φ s = ∫₀^∞ R(v) e^{(1 - s) v} dv` in `re s > 2`, and let `u, δ > 0` and `H = (k + 1) / u > 1`. The
number `(-H) ^ k H Φ⁽ᵏ⁾(1 + H) / k!` is within `L (δ + u² / ((k + 1) δ))` of `R(u)`, because the
Gamma density has mean `u` and variance `u² / (k + 1)`. 

### `eventually_log_pow_le_and_pow_le_exp_sqrt`

 For large `u` an even power of `c log u` is at most `u`, and a power of `u` is at most
`exp (√u / 2)`. 

### `one_sub_le_re_and_norm_le_of_mem_closedBall`

 Every point `s` of the disc of radius `H + η` about `1 + H` has `re s ≥ 1 - η` and
`|s| ≤ 2 H + η + 1`, for `H ≥ 0`. 

### `norm_taylorCoeff_dslope_le_inv_pow`

 Let `l ≥ 1`, let `H = (k + 1) / u > 1` with `4 H ≤ u ^ (2 B + 5)`, and let `F` be holomorphic
and at most `l ^ A` on the disc of radius `H + l ^ (-A)` about `1 + H`. If `l ^ (2 A) ≤ u` and
`u ^ (3 B + 7) ≤ exp (√u / 2)`, the normalised Taylor coefficient of `dslope F 1` at `1 + H` is at
most `u ^ (-(B + 1))`: the gain is `exp (-u / (2 l ^ A)) ≤ exp (-√u / 2)`. 

### `eventually_abs_le_inv_pow_of_transform`

 **Tauberian theorem.** Let `R` be measurable and Lipschitz on `v ≥ 0` (it suffices to test steps
of length at most `1`), with transform `∫₀^∞ R(v) e^{(1 - s) v} dv = (F s - F 1) / (s - 1)` in
`re s > 2`. Suppose that for all large `l` the function `F` is holomorphic and at most `l ^ A` on
`re s ≥ 1 - l ^ (-A)`, `|s| ≤ e ^ l`. Then `|R(u)| ≤ u ^ (-B)` for every `B` and all large `u`. 
