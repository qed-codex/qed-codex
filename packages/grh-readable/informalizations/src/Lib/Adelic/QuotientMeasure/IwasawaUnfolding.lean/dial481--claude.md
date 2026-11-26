---
{
  "module": "src/Lib/Adelic/QuotientMeasure/IwasawaUnfolding.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/QuotientMeasure/IwasawaUnfolding.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/QuotientMeasure/IwasawaUnfolding.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Unfolding over orbits and integration in Iwasawa coordinates

This file proves integration formulas on a quotient `Γ \ G` by a discrete subgroup `Γ`. An integral
over `Γ \ G` of a sum over translates is unfolded to an integral over the quotient by the subgroup
that keeps a block, in particular by the stabiliser of a point. Integrals of functions invariant
under a closed subgroup `N` are then written in Iwasawa coordinates `G = N · i(M) · K`.

* `Γ.quotMeasure μ`: the measure on `G` that integrates left `Γ`-invariant functions over `Γ \ G`.
* `N.FixesLeft F`: `F (γ * g) = F g` for all `γ ∈ N` and `g ∈ G`.

## Main definitions and results

* `New.integral_tsum_eq_integral_tsum_block`: the integral over `Γ \ G` of the sum over all
  translates of a block `C` is the integral over `S \ G` of the sum over `C`, where `S` is the
  group that keeps `C`. `New.integral_tsum_block` adds integrability and termwise integration.
* `New.integral_tsum_orbit_eq_integral_stabilizer`: the case of one orbit, with `S` the image of the
  stabiliser of a point.
* `New.lintegral_iwasawa`: `dn dm dk` in the coordinates `i m * n * k` is a multiple of Haar
  measure.
* `New.integral_quotMeasure_iwasawa`: the integral over `Γ \ G` of a function `F` invariant under
  `N` and `Γ` is a nonzero constant times the integral of `w m * F (i m * k)`, where conjugation by
  `i m` scales the Haar measure of `N` by `w m`.

## Relation to the literature

Known result: The unfolding trick and the integration formula in Iwasawa coordinates on a quotient
by a discrete subgroup. Weil's formula for invariant integration on a quotient is in
`Lib.Adelic.QuotientMeasure.Basic`.



## Unfolding a sum over an orbit

The unfolding trick for sums over a countable set `Y` with an action of a group `Λ`, which `i`
identifies with a discrete subgroup `Γ` of `G`. The summands `k y : G → ℂ` are measurable and
equivariant: `k (γ • y) (i γ * x) = k y x`.


### `New.tsum_cutoff_smul_mem_eq_one`

 Let `i` be injective, and let `γ` carry a point of `C` into `C` exactly when `i γ` lies in the
subgroup `S` of the range of `i`. If `β` has sum `1` over each `S`-orbit in `G`, then the sum of
`β (i γ * x)` over the `γ` that carry `y` into `C` is `1`, provided that there is such a `γ`. 

### `New.integrable_prod_count_of_lintegral_lt_top`

 If the `k y` are measurable and `∑ ‖k y‖` has finite integral for `ν`, then `(x, y) ↦ k y x` is
integrable for the product of `ν` with the counting measure. 

### `New.integrable_tsum_of_lintegral_lt_top`

 If the `k y` are measurable and `∑ ‖k y‖` has finite integral, then `∑ k y` is integrable. 

### `New.hasSum_integral_of_lintegral_tsum_lt_top`

 If the `k y` are almost everywhere strongly measurable and `∑ ‖k y‖` has finite integral, then
the integrals of the `k y` sum to the integral of `∑ k y`. 

### `New.tsum_cutoff_smul_mem_block`

 Let `i` map `Λ` isomorphically onto `Γ`, let `γ` carry a point of `C` into `C` exactly when
`i γ` lies in the subgroup `S` of `Γ`, and let `D` be the union of the translates of `C`. If `β` has
sum `1` over each `S`-orbit in `G`, then the sum of `β (i γ * x)` over the `γ` that carry `y` into
`C` is `1` if `y ∈ D` and `0` otherwise. 

### `New.lintegral_tsum_block`

 Unfolding of a sum of nonnegative terms over the translates of a block. Let `i` map `Λ`
isomorphically onto the discrete subgroup `Γ`, let `γ` carry a point of `C` into `C` exactly when
`i γ` lies in `S ≤ Γ`, and let `D` be the union of the translates of `C`. For measurable `g y` with
`g (γ • y) (i γ * x) = g y x`, the integral of `∑_D g y` over `Γ \ G` (that is, against
`Γ.quotMeasure μ`) is the integral of `∑_C g y` over `S \ G`. 

### `New.lintegral_tsum_enorm_block`

 Let `i` map `Λ` isomorphically onto the discrete subgroup `Γ`, let `γ` carry a point of `C` into
`C` exactly when `i γ` lies in `S ≤ Γ`, and let `D` be the union of the translates of `C`. For
measurable `k y` with `k (γ • y) (i γ * x) = k y x`, the integral of `∑_D ‖k y‖` over `Γ \ G` is
the integral of `∑_C ‖k y‖` over `S \ G`. 

### `New.integral_tsum_eq_integral_tsum_block`

 Unfolding of the integral of a sum over the translates of a block. Let `i` map `Λ`
isomorphically onto the discrete subgroup `Γ`, let `γ` carry a point of `C` into `C` exactly when
`i γ` lies in `S ≤ Γ`, and let `D` be the union of the translates of `C`. Let the `k y` be
measurable with `k (γ • y) (i γ * x) = k y x`. If `∑_C ‖k y‖` has finite integral over `S \ G`,
then the integral of `∑_D k y` over `Γ \ G` is the integral of `∑_C k y` over `S \ G`. 

### `New.tsum_integral_eq_integral_tsum_block`

 Unfolding of a sum of integrals over the translates of a block. Let `i` map `Λ` isomorphically
onto the discrete subgroup `Γ`, let `γ` carry a point of `C` into `C` exactly when `i γ` lies in
`S ≤ Γ`, and let `D` be the union of the translates of `C`. Let the `k y` be measurable with
`k (γ • y) (i γ * x) = k y x`. If `∑_C ‖k y‖` has finite integral over `S \ G`, then the sum over
`D` of the integrals of `k y` against the measure of `Γ \ G` is the integral of `∑_C k y` over
`S \ G`. 

### `New.integral_tsum_block`

 Unfolding of a sum over the translates of a block. The group `Λ` acts on `Y` and `i` maps it
isomorphically onto the discrete subgroup `Γ` of `G`; the terms are measurable and satisfy
`k (γ • y) (i γ * x) = k y x`. The block `C ⊆ Y` is such that `γ` carries a point of `C` into `C`
exactly when `i γ` lies in `S ≤ Γ`, and `D` is the union of the translates of `C`. Suppose that
`∑_D ‖k y‖` has finite integral over `Γ \ G` or that `∑_C ‖k y‖` has finite integral over `S \ G`.
Then `∑_C k y` is integrable over `S \ G`. Its integral equals the integral of `∑_D k y` over
`Γ \ G`. It also equals the sum over `D` of the integrals of `k y` against the measure of `Γ \ G`.


### `New.fixesLeft_map_stabilizer`

 If `k (γ • y) (i γ * x) = k y x`, then the term `k y` is invariant on the left under the image
`S` of the stabiliser of `y`. 

### `New.integral_tsum_orbit_eq_integral_stabilizer`

 Unfolding of a sum over an orbit. Let `i` be injective with discrete range `Γ`, let the terms
`k z` be measurable and equivariant, and let `S` be the image under `i` of the stabiliser of `y`.
Suppose that the sum of the `‖k z‖` over the orbit of `y` has finite integral over `Γ \ G`, or that
`k y` is integrable over `S \ G`. Then `k y` is integrable over `S \ G`, and its integral equals the
integral over `Γ \ G` of the sum of the `k z` over the orbit, and also the sum of their
integrals. 

### `New.integral_tsum_orbit_of_lt_top_or_integrable`

 Unfolding of a sum over an orbit, with the subgroups and the orbit given by equations: `Γ` is
the discrete range of the injective map `i`, `S` the image of the stabiliser of `y`, and `D` the
orbit of `y`. Here `Γ.quotMeasure μ` is the measure on `G` that computes integrals over `Γ \ G`: the
Haar measure `μ` weighted by a cutoff for `Γ`, and likewise for `S`. The terms `k z` are measurable
and equivariant. Suppose that `∑ ‖k z‖`, over all `z : Y`, has finite integral over `Γ \ G` or that
`k y` is integrable over `S \ G`. Then `k y` is integrable over `S \ G`, and its integral equals the
integral of `∑_D k z` over `Γ \ G` and also the sum over `D` of the integrals of `k z` against
`Γ.quotMeasure μ`. 

### `New.integral_tsum_orbit`

 Left invariance of `k y` and unfolding over the orbit `D` of `y`, as one statement. Here `i`
maps `Λ` isomorphically onto the discrete subgroup `Γ`, `S` is the image under `i` of the stabiliser
of `y`, and the `k z` are measurable and equivariant. The conclusion has two parts. The first says
that `k y` is left `S`-invariant (`S.FixesLeft (k y)`). The second is the implication proved in
`integral_tsum_orbit_of_lt_top_or_integrable`: if `∑ ‖k z‖` has finite integral over `Γ \ G` or
`k y` is integrable over `S \ G`, then `k y` is integrable over `S \ G`, and its integral equals
both the integral of `∑_D k z` over `Γ \ G` and the sum over `D` of the integrals of the `k z`. 


## Iwasawa integration formula

Integration in Iwasawa coordinates on a unimodular group `G = N · i(M) · K`, with `N` closed, `K`
compact and `i : M →* G` continuous. It is used for constant terms along a unipotent radical `N`.


### `New.exists_measurable_mul_eq_of_scale`

 Let `J f x` be measurable in `x`, and let `J f x₀` be obtained from `J f y` by a finite nonzero
factor that depends on `y` only. Then this factor can be absorbed into a measurable weight: for
measurable `β` there is a measurable `g` with `g y * J f y = β y * J f x₀`. 

### `New.ae_eq_zero_of_integrable_top_smul`

 A function that is integrable for `∞ • q` vanishes `q`-almost everywhere. 

### `New.exists_integral_eq_mul_of_smul_measure`

 Division of an integral formula by a factor `c ∈ (0, ∞]` of the measure. For finite nonzero `V`
there is `a ≠ 0` such that, if `F` is measurable and integrable for `c • q` with integral `V * I`,
then `F` is integrable for `q` with integral `a * I`. 

### `New.exists_equiv_prod_subgroupOf`

 Let `i a` lie in `N` only for `a = 1`, let `δ` be injective, and let `Γ` contain every `i (δ d)`
and lie in the union of the `N · i (δ d)⁻¹`. Then every element of `Γ` is uniquely `i (δ d) * γ`
with `γ ∈ Γ ∩ N`. 

### `New.ofReal_mul_lintegral_iwasawa_translate`

 Let `N` be unimodular, and let conjugation by `i m` multiply integrals over `N` by `w m`. The
integral of `f (i a * u * (n * i m * k) * l⁻¹)` over `K × M × N`, times `w m`, is the integral of
`f (i a * u * l⁻¹)`. 

### `New.lintegral_iwasawa_inv_mul_translate`

 Suppose that conjugation by `i m` multiplies integrals over `N` by `w m`. The integral of
`g ((i a * u)⁻¹ * (x * l))` over `K × M × N` is the same for `x = n * i m * k` as for `x = 1`. 

### `New.lintegral_iwasawa`

 Iwasawa integration formula. Let `G`, `M` and the closed subgroup `N` be unimodular, `K`
compact, and `i : M →* G` and `w : M → ℝ` continuous. Suppose that `G = N · i(M) · K` and that
conjugation by `i m` multiplies integrals over `N` by `w m > 0`. Then the measure `dn dm dk` in the
coordinates `i m * n * k` is `d` times the Haar measure `μ` on `G`, for some `d ∈ [0, ∞]` (`d` may
be infinite, for instance if `i` has noncompact kernel). Here `lam`, `ν`, `κ` are Haar measures on
`N`, `M`, `K`. 

### `New.ofReal_mul_lintegral_quotMeasure_tsum`

 Let `i a` lie in the closed unimodular subgroup `N` only for `a = 1`, let `δ` be injective, and
let the discrete group `Γ` contain every `i (δ d)` and lie in the union of the `N · i (δ d)⁻¹`.
Suppose that conjugation by `i m` multiplies integrals over `N` by `w m`. Then `w m` times the
integral over `(Γ ∩ N) \ N` (that is, against `quotMeasure lam`) of a sum over `Γ` unfolds to a sum
over `d` of integrals over `N` against the Haar measure `lam`. 

### `New.integral_quotMeasure_iwasawa`

 Unfolding in Iwasawa coordinates. Let `μ`, `ν`, `κ`, `lam` be Haar measures on the unimodular
group `G`, the unimodular group `M`, the compact subgroup `K` and the closed subgroup `N`, and let
`i` and `w` be continuous. Suppose that `G = N · i(M) · K`, that conjugation by `i m` multiplies
integrals over `N` by `w m > 0`, and that `i a` lies in `N` only for `a = 1`. Let `δ` be injective,
and let `Γ` be discrete, contain every `i (δ d)` and lie in the union of the `N · i (δ d)⁻¹`, with
`Γ ∩ N` cocompact in `N` (`IsCocompact`: every element of `N` has a left translate by `Γ ∩ N` in a
fixed compact set). Let `α` be a measure on `M` that unfolds to `ν` along `δ`. There is `c ≠ 0` such
that for measurable `F`, left invariant under `N` and `Γ` (`FixesLeft`): if
`(m, k) ↦ w m * F (i m * k)` is integrable for `α × κ`, then `F` is integrable over `Γ \ G` (against
`Γ.quotMeasure μ`), and its integral is `c` times the integral of `w m * F (i m * k)`. 
