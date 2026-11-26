---
{
  "module": "src/Lib/Adelic/QuotientMeasure/Basic.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/QuotientMeasure/Basic.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/QuotientMeasure/Basic.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Quotient measures via cutoffs: unfolding, covolume, unimodularity, periodic means

A group `H` with a measure `ν` acts on a measure space `(X, μ)`. Integration over `H \ X` is done on
`X` itself. A cutoff (`New.IsCutoff ν β`) is a measurable `β : X → [0, ∞]` with
`∫ β (h • x) dν(h) = 1` for every `x`. For a discrete subgroup `Γ` of a group `G` with counting
measure, and a Haar measure `μ` on `G`, `Γ.quotMeasure μ` integrates over `Γ \ G`, and its total
mass is the covolume of `Γ`.

## Main definitions and results

* `New.orbitMeasure`: the measure `β μ` on `X`, for the chosen weight `β = New.chosenCutoff ν`. It
  is meant for `H`-invariant integrands, and for actions where a cutoff exists (`New.HasCutoff`);
  then `β` is a cutoff (`New.isCutoff_chosenCutoff`).
* `New.IsCutoff.measurePreserving`, `New.measurePreserving_orbitMeasure`: the map `(x, h) ↦ h • x`
  carries `(β μ) × ν` to `μ`; the other results on unfolding follow from this and Fubini's theorem.
* `New.identDistrib_orbitMeasure_of_unfold`, `New.identDistrib_orbitMeasure`: invariant functions
  have the same distribution for every measure that unfolds to `μ`. So the choice of cutoff does not
  matter when `ν` is inversion invariant and `μ` is invariant, both s-finite.
* `New.integral_quotMeasure_tsum`: `∫_{Γ\G} ∑_γ f(γ g) = ∫_G f`.
* `New.isMulRightInvariant_of_finite_covolume`: a group with a discrete subgroup of finite covolume
  is unimodular.
* `New.quotMean_tsum_eq_integral`: the mean of `x ↦ ∑ γ, F (γ + x)` is `∫ F dμ` divided by the
  covolume.

## Relation to the literature

Known result: Invariant integration on a quotient (Weil's formula), unfolding and unimodularity.
Here the quotient integral is integration against a measurable weight of total mass one on each
orbit, so no orbit space or section is needed to define it; existence is proved for proper actions
and for discrete subgroups. Source: O. Kallenberg, Invariant measures and disintegrations with
applications to Palm and related kernels, Probab. Theory Related Fields 139 (2007) 285-310 (as
cited in D. Gentner, G. Last, Math. Z. 267 (2011), §2); for the classical form, N. Bourbaki,
Intégration VII, 1963.



## Cutoff weights and the quotient measure

* `Subgroup.IsCocompact`: every element of `G` has a translate by the subgroup in a fixed compact
  set.

The definitions have additive versions, except `Subgroup.FixesLeft`.


### `Subgroup.IsCocompact`

 The subgroup N of G is cocompact: there is a compact C ⊂ G such that every g has a translate
γg in C with γ ∈ N. 

### `Subgroup.FixesLeft`

 The function F on G is left invariant under the subgroup N: F(γg) = F(g) for all γ ∈ N and g
∈ G. 

### `IsCutoff`

 The property that β: X → [0, ∞] is measurable and ∫_H β(hx) dν(h) = 1 for every x in X. 

### `chosenCutoff`

 A chosen weight for the action of `H`, with measure `ν`, on `X`. It is a cutoff when the action
has one (`New.isCutoff_chosenCutoff`); otherwise it is an unspecified function. 

### `orbitMeasure`

 The measure βμ on X for the weight β = `New.chosenCutoff ν`. When a cutoff exists
(`New.HasCutoff`), ν is inversion invariant and μ is H-invariant, both s-finite, integrating an
H-invariant function against it gives the integral over H\X, for every choice of cutoff. 

### `HasCutoff`

 The hypothesis that the action of H, with measure ν, on X admits a cutoff: a measurable
weight with integral one over each orbit. 

### `isCutoff_chosenCutoff`

 If the action of `H`, with measure `ν`, on `X` has a cutoff, the chosen weight is a cutoff. 

### `measurable_chosenCutoff`

 If the action has a cutoff, the chosen weight is measurable. 

### `lintegral_chosenCutoff_smul`

 If the action has a cutoff, the chosen weight has integral one over each orbit. 

### `instance (priority`

 Shortcut: the `MulAction` instance of a subgroup `N` on its ambient group `G`. 

### `instance (priority`

 Shortcut: the `SMul` instance of a subgroup `N` on its ambient group `G`. 

### `_root_.Subgroup.quotMeasure`

 The measure on G that computes integrals over N\G, when N with counting measure has a cutoff
(for example when N is discrete) and μ is invariant under N. It is μ weighted by a cutoff chosen for
the action of N, with counting measure, on G. By default μ is `volume`. 


## Independence of the cutoff and unfolding

* `New.lintegral_orbitMeasure_lintegral`: unfolding for lower integrals,
  `∫_{H\X} ∫_H f(h • x) = ∫_X f`.


### `identDistrib_orbitMeasure_of_unfold`

 A measure that unfolds to `μ` computes the quotient measure. Suppose that the action of `H` on
`X` has a cutoff for `ν` (a weight with integral one over each orbit), let `σ` carry `ρ` to `ν`, and
let `(z, l) ↦ σ l • T z` carry `m × ρ` to `μ`, with `T` measurable. Then a measurable `H`-invariant
function `F` has the same distribution under `New.orbitMeasure ν μ` (`μ` weighted by a chosen
cutoff) as `F ∘ T` under `m`. 

 ### Unfolding with a given cutoff 

### `measurePreserving_smul_prod`

 Let a group H act measurably on X, ν an s-finite measure on H, μ an s-finite H-invariant
measure on X, β : X → [0,∞] measurable. Then (x,h) ↦ hx pushes (βμ) × ν forward to the measure
with density x ↦ ∫ β(h⁻¹x) dν(h) with respect to μ. 

### `IsCutoff.measurePreserving`

 Unfolding: for an inversion invariant s-finite measure `ν` on `H`, an s-finite invariant measure
`μ` on `X` and a cutoff `β`, the map `(x, h) ↦ h • x` carries `(β μ) × ν` to `μ`. 

### `identDistrib_orbitMeasure`

 Independence of the cutoff. Let `ν` be an s-finite, inversion-invariant measure on the group `H`
and `μ` an s-finite, `H`-invariant measure on `X`. If `β` is a cutoff (measurable, with
`∫⁻ h, β (h • x) ∂ν = 1` for every `x`), then every measurable `H`-invariant `F` has the same
distribution under `μ.withDensity β` as under `orbitMeasure ν μ`, which is `μ` weighted by a fixed
chosen cutoff and stands in on `X` for the quotient measure on `H \ X`. 

### `IsCutoff.ae_cutoff_lt_top`

 A cutoff `β` for an inversion invariant s-finite measure `ν` on `H` is finite almost everywhere
for every s-finite `H`-invariant measure `μ` on `X`. 

### `IsCutoff.integral_orbitMeasure`

 Let a group `H` act measurably on `X`, with `ν` an s-finite, inversion-invariant measure on `H`
and `μ` an s-finite, `H`-invariant measure on `X`. Let `β` be a cutoff, meaning a measurable
`β : X → [0, ∞]` with `∫ β (h • x) dν(h) = 1` for every `x`. Then for any measurable, `H`-invariant
`f` with values in a real normed space, the integral of `f` against the quotient measure
`orbitMeasure ν μ` (the measure `μ` weighted by a chosen cutoff) equals `∫ β(y) • f(y) dμ`. 

 ### Unfolding with the chosen cutoff 

### `measurePreserving_orbitMeasure`

 Unfolding for the quotient measure (Weil's formula): let `ν` be an s-finite, inversion-invariant
measure on `H`, and `μ` an s-finite, `H`-invariant measure on `X`. Suppose the action of `H` on `X`
has a cutoff, meaning a measurable weight on `X` whose `ν`-integral over each orbit is one. Then
`(x, h) ↦ h • x` carries `orbitMeasure ν μ × ν` to `μ`. Here `orbitMeasure ν μ` is `μ` weighted by a
chosen cutoff, a measure on `X` standing in for the quotient measure on `H \ X`. 

### `dense_of_ae_orbitMeasure`

 Let the action of H on X have a cutoff for the inversion invariant measure ν and let the
invariant measure μ be positive on nonempty open sets. An H-stable property that holds almost
everywhere for the quotient measure `New.orbitMeasure` holds on a dense subset of X. 

### `lintegral_orbitMeasure_lintegral`

 Unfolding for `lintegral`: let `ν` be an s-finite, inversion-invariant measure on `H`, and `μ`
an s-finite, `H`-invariant measure on `X`. Suppose the action has a cutoff, meaning a measurable
weight on `X` whose `ν`-integral over each orbit is one. Then for measurable `f : X → [0, ∞]`,
integrating the orbit integral `x ↦ ∫⁻ h, f (h • x) ∂ν` against `orbitMeasure ν μ` gives
`∫⁻ x, f x ∂μ`. Here `orbitMeasure ν μ` is `μ` weighted by a chosen cutoff, a measure on `X`
standing in for the quotient measure on `H \ X`. 


## Existence of cutoffs and unfolding a sum over a discrete subgroup

* `New.hasCutoff_of_proper`: a proper action on a σ-compact Hausdorff space has a cutoff.
* `New.hasCutoff_count`: a discrete subgroup `Γ` acting on `G` by left translation has a cutoff.


 ### Counting measure and sums of weights 

### `integral_count_eq_tsum`

 The integral of a complex function against the counting measure of a countable set is its sum
(both are zero when the function is not summable). 

### `tsum_toReal_smul_of_tsum_eq_one`

 If nonnegative weights `f x` in `[0, ∞]` sum to one, the sum of their multiples of a complex
number `z` is `z`. 

 ### Existence of cutoffs 

### `hasCutoff_of_proper`

 A proper action of `H` on a σ-compact Hausdorff space `X` has a cutoff (a measurable weight with
integral one over each orbit) for every nonzero s-finite right-invariant measure `ν` on `H` that is
finite on compact sets. 

### `instance [DiscreteTopology H] : IsHaarMeasure (count (α`

 On a discrete group `H` with measurable singletons, the counting measure is a Haar measure. 

### `to_additive (anonymous instance)`

 On a discrete additive group with measurable singletons, the counting measure is
a Haar measure. 

 ### Cosets of a subgroup and subgroups of discrete subgroups 

### `cosetProdEquiv`

 For a subgroup `N` of `G`, the bijection `(G ⧸ N) × N ≃ G` sending `(q, u)` to `u * r⁻¹`,
where `r = q.out` is the chosen representative of the left coset `q`. The elements `r⁻¹`
represent the right cosets of `N`. 

### `cosetProdEquiv_symm_apply_fst`

 The coset component of `γ` is the left coset of `γ⁻¹`. 

### `cosetProdEquiv_symm_apply_snd`

 The `N`-component of `γ` is `γ` times the chosen representative of the left coset of
`γ⁻¹`. 

### `locallyCompactSpace_of_isClosed`

 A closed set `N` in a locally compact space is locally compact, as a subspace. 

 ### Discrete subgroups of a locally compact group 

### `hasCutoff_count`

 A discrete subgroup `Γ` of `G`, with counting measure, acting on `G` by left translation has a
cutoff. 

### `quotMeasure_bot`

 For the trivial subgroup of `G` and a left Haar measure `μ`, the quotient measure is `μ`. 

### `integrable_quotMeasure_tsum`

 For a discrete subgroup `Γ` of `G`, a left Haar measure `μ` and an integrable `f`, the sum
`g ↦ ∑' γ, f (γ * g)` is integrable for the quotient measure on `Γ \ G`. 

### `integral_quotMeasure_tsum_eq`

 For a discrete subgroup `Γ` of `G`, a left Haar measure `μ` and an integrable `f`, the
integral of `g ↦ ∑' γ, f (γ * g)` over `Γ \ G` is `∫ f dμ`. 

### `integral_quotMeasure_tsum`

 Unfolding of a sum over a discrete subgroup `Γ` of `G`, for a left Haar measure `μ` and an
integrable `f`: `g ↦ ∑' γ, f (γ * g)` is integrable for the quotient measure on `Γ \ G`, and its
integral is `∫ f dμ`. This is Weil's integration formula for a discrete subgroup. 


## Transport along equivariant measure preserving maps

Integrals over a quotient `H \ X` are integrals against the measure `New.orbitMeasure ν μ`, which is
`μ` weighted by a chosen cutoff. It depends on that choice, so only invariant functions have a well
defined distribution; results are stated with `IdentDistrib`.

* `New.identDistrib_orbitMeasure_comp`: change of variables along an equivariant measure preserving
  map.


### `New.identDistrib_orbitMeasure_comp`

 Change of variables on quotients. Let `σ : H → H'` and `T : X → Y` preserve the measures, with
`T (h • x) = σ h • T x`. For a measurable `H'`-invariant `F` on `Y`, the function `F ∘ T` on `H \ X`
and the function `F` on `H' \ Y` have the same distribution. 

### `New.identDistrib_orbitMeasure_mul_right`

 If `μ` is right invariant on the group `X` and `(h • x) * g = h • (x * g)`, then right
translation by `g` does not change the distribution on `H \ X` of a measurable `H`-invariant
function. 


## Unimodularity and finite covolume of cocompact discrete subgroups

* `New.isFiniteMeasure_quotMeasure_of_cocompact`: a cocompact discrete subgroup has finite covolume.


### `isMulRightInvariant_of_finite_covolume`

 A group with a lattice is unimodular: if Γ is discrete in the locally compact second
countable Hausdorff group G and Γ\G has finite volume for the left Haar measure μ, then μ is
right invariant. 

### `isFiniteMeasure_quotMeasure_of_cocompact`

 A cocompact discrete subgroup `Γ` of `G` has finite covolume: if some compact set `C` meets
every orbit `Γ g`, the quotient measure of the left Haar measure `μ` on `Γ \ G` is finite. 

### `exists_eq_smul_haar`

 If the left Haar measure `μ` is also right invariant, every s-finite right invariant measure
is `d • μ` for some `d` in `[0, ∞]`. 


## The mean of a periodic function over a compact quotient

The mean of a periodic function on a topological abelian group `B` over a compact quotient `B ⧸ B₀`,
for the Haar probability measure. Functions stay on `B`; they are read on the quotient through
chosen representatives `q.out`.

* `New.quotMean_quotMean`: the mean may be computed in two steps, along a continuous homomorphism
  from a product `A × A'` onto `B`.


### `IsContPeriodic`

 The property that a function F on a topological abelian group B is continuous and satisfies
F(γ+x)=F(x) for all γ in the subgroup B₀ and all x. 

### `IsDualFamily.quotMeasurableSpace`

 The Borel σ-algebra on the quotient B/B₀ of a topological abelian group B by a subgroup B₀. 

### `quotMean`

 The mean of a complex-valued function `F` over the compact quotient `B ⧸ B₀`. It is the integral
of `F q.out` against the Haar probability measure, where `q.out` is a chosen coset
representative. 

### `norm_quotMean_le`

 A bound for `F` bounds its mean, the measure being a probability measure. 

### `IsContPeriodic.apply_out_mk`

 A continuous `B₀`-periodic function takes at the chosen representative of the coset of `x`
the same value as at `x`. 

### `IsContPeriodic.continuous_out`

 A continuous `B₀`-periodic function, read at coset representatives, is continuous on
`B ⧸ B₀`. 

### `IsContPeriodic.integrable_out`

 A continuous `B₀`-periodic function, read at coset representatives, is integrable on the
compact quotient `B ⧸ B₀`. 

### `quotMean_translate`

 A translate of a continuous `B₀`-periodic function has the same mean over `B ⧸ B₀`. 

### `quotMean_quotMean`

 Let `φ : A × A' → B` be a continuous surjective homomorphism that sends `A₀ × A₁` into `B₀`; all
three quotients are compact and `A` is second countable. For `F` continuous and `B₀`-periodic, the
mean of `F (φ (a, a'))` over `A' ⧸ A₁` and then over `A ⧸ A₀` is the mean of `F` over `B ⧸ B₀`. 

### `quotMean_comp`

 The mean of a continuous `B₀`-periodic function may be computed after pull-back along a
continuous surjective homomorphism `φ : A → B` that sends `A₀` into `B₀`. 


## The periodic mean as an average against the quotient measure

Let `B₀` be a discrete cocompact subgroup of a locally compact abelian group `B` with Haar measure
`μ`. The measure `B₀.quotMeasure μ` on `B`, assumed finite, plays the role of the restriction of
`μ` to a fundamental domain; its mass is the covolume of `B₀`.

* `New.average_quotMeasure_eq_quotMean`: the mean `New.quotMean` of a continuous periodic function
  over `B ⧸ B₀` is its average against `B₀.quotMeasure μ`.


### `average_quotMeasure_eq_quotMean`

 Here `B₀.quotMeasure μ` is μ weighted by a cutoff for the action of B₀, a measure on B that
computes integrals over B ⧸ B₀. `quotMean B₀ F` is the integral of F over B ⧸ B₀ against the Haar
probability measure. For B₀ discrete and cocompact in B, μ a Haar measure with `B₀.quotMeasure μ`
finite, and F continuous and B₀-periodic, the average of F against `B₀.quotMeasure μ` equals
`quotMean B₀ F`. 

### `quotMean_tsum_eq_integral`

 Unfolding: if `F` is integrable on `B` and `G x = ∑_{γ ∈ B₀} F (γ + x)` converges everywhere
and is continuous and `B₀`-periodic, then the mean of `G` over `B ⧸ B₀` is `∫ F dμ` divided by the
covolume of `B₀` (the mass of `B₀.quotMeasure μ`). 
