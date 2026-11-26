---
{
  "module": "src/Lib/Adelic/QuotientMeasure/UnfoldingInStages.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/QuotientMeasure/UnfoldingInStages.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/QuotientMeasure/UnfoldingInStages.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Pushing forward quotient measures, unfolding in stages and vanishing criteria

This file studies integrals over a quotient `Γ \ G` by a discrete subgroup `Γ`, with `μ` a Haar
measure. For a `Γ`-invariant `F`, `(Γ.quotMeasure μ)[F]` is the integral of `F` over `Γ \ G`. Such
integrals are compared with integrals over a quotient `Λ \ H` of a second group mapping to `G`, and
are written as iterated integrals with inner integral over `Λ \ H`. From this follow two criteria
for the integral of a continuous left `Γ`-invariant function to vanish.

## Main definitions and results

* `New.exists_integral_comp_quotMeasure_eq_smul`: for a continuous surjection `H → G` of unimodular
  groups taking `Λ` into `Γ`, the integral over `Λ \ H` of a pulled-back invariant function is a
  fixed multiple of its integral over `Γ \ G`. Unimodular means the Haar measures are also right
  invariant.
* `New.integral_quotMeasure_stages`: the integral over `Γ \ G` is an iterated integral whose inner
  integral is over `Λ \ H`.
* `New.integral_quotMeasure_eq_integral_cosetMeasure`: the case of a closed subgroup, with the outer
  integral over `i(H) \ G` (`New.cosetMeasure`).
* `New.Exchange.exists_integral_stages_eq_mul`: for a subgroup `L × H`, if the inner integrals
  through every `g` are `ρ g * c`, with `re ρ` nonnegative and nonzero near some point, then the
  integral over `Γ \ G` is `R * c` for a fixed `R ≠ 0`, with `Γ` the image of `Λ ≤ H`.
* `New.integral_quotMeasure_eq_zero_of_mean`: the integral vanishes if an average of translates of
  `F` by elements of a closed subgroup `H ≥ Γ` is `a • F` and these elements scale the Haar measure
  of `H` by `d ≠ a`.
* `New.integral_quotMeasure_eq_zero_of_twist`: the integral vanishes if `F (u * y) = c • F y` with
  `‖c‖ = 1` and `c ≠ 1`.

## Relation to the literature

Known; see `Lib.Adelic.QuotientMeasure.Basic` for sources.


 ## Pushing forward quotient measures and unfolding in stages 

### `New.exists_integral_comp_quotMeasure_eq_smul`

 Let `π : H → G` be a continuous surjective homomorphism with `π Λ ≤ Γ` (both discrete), and let
`μ` and `ν` be Haar measures on `G` and `H` that are also right invariant. There is a real `c` such
that, for all measurable left `Γ`-invariant `F`, the integral of `F ∘ π` over `Λ \ H` is `c` times
the integral of `F` over `Γ \ G`. 

### `New.integral_quotMeasure_stages`

 Unfolding in stages. Let `i : H → G` be an injective homomorphism with `i Λ = Γ` (both
discrete), `ν` a Haar measure on `H`, and let `(z, h) ↦ i h * T z` carry `m ⊗ ν` to `μ`. Let `F`
be measurable, left `Γ`-invariant and integrable on `Γ \ G`. Then (a) the integral of
`a ↦ F (i a * T z)` over `Λ \ H` is `m`-integrable in `z` and (b) its integral against `m` is the
integral of `F` over `Γ \ G`. 

### `New.cosetMeasure`

 The quotient measure on `i(H) \ G`, carried by `G`, of the Haar measures `μ` on `G` and `ν` on
`H`, for `H` acting on `G` by left translation through `i`; it is used for closed embeddings
`i : H → G`. 

### `New.integral_quotMeasure_eq_integral_cosetMeasure`

 Integration in stages. Let `i : H → G` be a closed embedding, `Λ` a discrete subgroup of the
unimodular group `H`, and `F` measurable, left `i(Λ)`-invariant and integrable on `i(Λ) \ G`. Then
(a) the integral of `a ↦ F (i a * g)` over `Λ \ H` is integrable in `g` on `i(H) \ G` and (b) its
integral there is the integral of `F` over `i(Λ) \ G`. 

### `New.dense_eq_zero_of_integral_cosetMeasure_eq_zero`

 Let `i : H → G` be a closed embedding of a unimodular group and `ρ ≥ 0` a function on `G`,
invariant under left translation by `i(H)`, integrable and with integral zero for the quotient
measure `New.cosetMeasure` on `i(H) \ G`. Then `ρ` vanishes on a dense set. 

### `New.eq_zero_of_integral_cosetMeasure_eq_zero`

 Let `i : H → G` be a closed embedding of a unimodular group and `ρ ≥ 0` a continuous function
on `G`, invariant under left translation by `i(H)` and integrable for the quotient measure
`New.cosetMeasure` on `i(H) \ G`. If its integral is zero, then `ρ = 0`. 

### `New.dense_re_eq_zero_of_integral_cosetMeasure_eq_zero`

 Let `i : H → G` be a closed embedding of a unimodular group and `ρ : G → ℂ` invariant under
left translation by `i(H)`, with nonnegative real part, integrable and with integral zero for the
quotient measure `New.cosetMeasure` on `i(H) \ G`. Then the real part of `ρ` vanishes on a dense
set. 

### `New.integral_integral_quotMeasure_translate`

 Let `i : L × H → G` be a continuous homomorphism, `κ` a right invariant measure on `L`, `ν` a
right invariant Haar measure on `H`, and `F` continuous, left invariant under the image of the
discrete `Λ ≤ H`. The integral of `F (i (l, a) * g)` over `a` in `Λ \ H` and then over `l` in `L`
is unchanged if `g` is replaced by `i k * g`. 

### `New.integral_quotMeasure_eq_integral_cosetMeasure_prod`

 Let `i` embed `L × H` as a closed subgroup of `G`, with `L` and `H` unimodular, and let `Λ ≤ H`
be discrete with image `Γ`. For `F` continuous, left `Γ`-invariant and integrable on `Γ \ G`, the
integral of `F (i (l, a) * g)` over `a` in `Λ \ H` and then over `l` in `L` is integrable in `g` on
the quotient of `G` by `L × H`, and its integral there is the integral of `F` over `Γ \ G`. 

### `New.Exchange.exists_integral_stages_eq_mul`

 Let `i` embed `L × H` as a closed subgroup of `G`, with `L` and `H` unimodular, let `Λ ≤ H` be
discrete, and write `Γ` for the image of `Λ` under `a ↦ i (1, a)`. Let `ρ : G → ℂ` have real part
that is nonnegative, and nonzero near some point `g₀`. There is `R ≠ 0`, independent of `F` and
`c`, with the following property. Suppose (a) `F` is continuous, left `Γ`-invariant and integrable
on `Γ \ G`. Suppose (b) each `g` has a `k` in `L × H` for which the integral of
`F (i (l, a) * (i k * g))` over `a` in `Λ \ H` and then over `l` in `L` is `ρ g * c`. Then the
integral of `F` over `Γ \ G` is `R * c`. 


## Vanishing of quotient integrals by averaging or by a twist

The first criterion is proved by unfolding the integral along `H`
(`New.integral_quotMeasure_stages`). The second follows from the first, applied to a closed
subgroup built from the twist.


### `New.integral_quotMeasure_eq_zero_of_mean`

 Let `Γ ≤ H ≤ G` with `Γ` discrete and `H` closed, and let `F` be continuous and left
`Γ`-invariant. Let `κ` be a probability measure and `translator x b` elements of `H`, measurable in
`b`, such that right translation by `translator x b` carries the Haar measure of `H` to `d` times
itself and the `κ`-average over `b` of `F (s * translator x b * x)` is `a • F (s * x)` for all `s`
in `H`. If `a ≠ d`, the integral of `F` over `Γ \ G` vanishes. 

### `New.integral_quotMeasure_eq_zero_of_twist`

 Let `F` be continuous and left invariant under the discrete subgroup `Γ`. If left translation
by some `u` multiplies `F` by a constant `c ≠ 1` of modulus one, the integral of `F` over
`Γ \ G` vanishes. 
