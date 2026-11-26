---
{
  "module": "src/New/UpperBound/Seesaw/IntegralAsCosetSum.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/IntegralAsCosetSum.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/IntegralAsCosetSum.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Integrals over a quotient as finite sums over cosets with controlled multiplicity

A finite set of cosets serves as a weighted fundamental domain. For subgroups `S`, `A`, `J` of `H`
and a finite `T ⊆ H ⧸ J`:
* `New.Seesaw.coverMultiplicity`: the number of classes in `S ⧸ (S ⊓ A)` that have a
  representative `r` with `t ∈ r • T` (zero if infinite).
* `New.Seesaw.exists_finset_coverMultiplicity_dvd_pow`: for `H = New.Gf E ι`, levels `J ≤ A` and a
  compact `D` on which the `q ^ n`-th powers of conjugates of `J` fall into `A`, a `T` stable under
  `S ⊓ A` whose multiplicities divide powers of `q` at the points of `T` and at the points with a
  given property that forces their `S`-orbit to meet `D`.
* `New.Grading.exists_integral_eq_sum_over_cut`: if the periods of a function over the Bessel
  subgroup factor over `T` and the multiplicities are non-zero on its support, its integral over the
  quotient of the adelic group `New.G E ε` by the rational points of `New.Grading.besselGroup` is a
  constant times a sum over `T` weighted by the inverse multiplicities.

In these names, a "cut" is such a finite set `T` of cosets.

Notions from other files:
* `New.G E ε = New.GInf E ε × New.Gf E ι`: the adelic unitary group, with its infinite and finite
  parts.
* `New.IsLevel J`: `J` is an open subgroup of the compact open subgroup `New.stdLevel E ι` of
  integral points of `New.Gf E ι`; its index there is `New.stdLevelIndex J`.
* `New.Grading.besselGroup`: the Bessel (Fourier–Jacobi) subgroup of `New.G E ε` attached to a
  grading, with finite part `New.Grading.besselFin` and rational points `New.Grading.ratBessel`.
* `Subgroup.quotMeasure`: the measure on a group that computes integrals over the quotient by a
  subgroup acting on the left; `New.Grading.besselMeasure` is this measure for the quotient of the
  Bessel subgroup by its rational points.

## Relation to the literature

See `New.UpperBound.Seesaw.SeesawIdentity` for related work.


### `coverMultiplicity`

 The multiplicity with which the translates of `T` under `S`, counted modulo `S ⊓ A`, cover `t`:
the number of classes in `S ⧸ (S ⊓ A)` that have a representative `r` with `r⁻¹ • t ∈ T`, and zero
if there are infinitely many. 

### `coverMultiplicity_smul`

 The number `coverMultiplicity S A T t` of classes of `r ∈ S` modulo `S ⊓ A` with `r⁻¹ • t ∈ T`
is constant on the `S`-orbit of the coset `t ∈ H ⧸ J`. 

### `exists_index_dvd_pow_of_pow_mem`

 If the `q ^ n`-th power of every element lies in a subgroup `K` of finite index, then the index
of `K` divides a power of `q`: in the finite quotient by the normal core of `K`, the order of every
element divides `q ^ n`. 

### `coverMultiplicity_eq_index_stabilizer`

 Let `C ⊆ H ⧸ J` meet each `S`-orbit in at most one point, and let `T` be the union of the
translates of `C` under `S ⊓ A`. At a point `t` of `C`, the number `coverMultiplicity S A T t` of
classes of `r ∈ S` modulo `S ⊓ A` with `r⁻¹ • t ∈ T` is the index of `Z ⊓ A` in the stabiliser `Z`
of `t` in `S`. 

### `measure_union_cosets`

 A union of `n ≥ 1` left cosets of a measurable subgroup `J` has measure `n * μ J` for any left
invariant measure `μ`. 

### `exists_index_stabilizer_dvd_pow`

 Let `S`, `A` and `J ≤ A` be subgroups of the finite adelic unitary group `Gf E ι` with `A` a
level, and suppose `(x * u * x⁻¹) ^ q ^ n ∈ A` for all `u ∈ J`. Then the index of `Z ⊓ A` in the
stabiliser `Z` in `S` of the coset `x J` divides a power of `q`. 

### `exists_finset_coverMultiplicity_dvd_pow`

 Let `S` and `J ≤ A ≤ B` be subgroups of the finite adelic unitary group `Gf E ι` with `J` and
`A` levels, and `q` a natural number. Let `D` be compact, such that each `x ∈ D` lies in `B` and has
an `n` with `(x * u * x⁻¹) ^ q ^ n ∈ A` for all `u ∈ J`. Let `W` be a property of points that forces
their `S`-orbit to meet `D`: if `W x` then `r * x ∈ D` for some `r ∈ S`. Then some finite set `T` of
cosets of `J` (a "cut") has three properties: (a) it is stable under `S ⊓ A`; (b) every `x` with
`x J ∈ T` lies in `B`; (c) whenever `x J ∈ T` or `W x`, the multiplicity
`coverMultiplicity S A T x`, the number of classes of `r ∈ S` modulo `S ⊓ A` with `r⁻¹ x J ∈ T`,
divides a power of `q`. 

### `lintegral_indicator_inv_coverMultiplicity`

 Let `A` and `J` be levels in the finite adelic unitary group `Gf E ι`, let `η` be a left
invariant measure on the subgroup `S` giving `S ⊓ A` mass one, and let the finite set `T` of cosets
of `J` be stable under `S ⊓ A`. Let `m x = coverMultiplicity S A T x` be the number of classes of
`r ∈ S` modulo `S ⊓ A` with `r⁻¹ • x ∈ T`. The function equal to `1 / m` on `T` and zero off `T`,
evaluated at `u⁻¹ • t` and integrated over `u` in `S` against `η`, gives one if `m t ≠ 0` and zero
otherwise. 

### `integral_indicator_smul_quotient`

 Let `J` be a level in the finite adelic unitary group `Gf E ι` (an open subgroup of the group
`stdLevel E ι` of integral points, which has volume one), `T` a finite set of cosets of `J`, and
`c`, `b` functions on `Gf E ι ⧸ J`. The integral over `Gf E ι` of `c • b` cut off to `T` is its sum
over `T` divided by the index `stdLevelIndex J` of `J` in `stdLevel E ι`. 

### `lintegral_besselGroup_cutoff_mul`

 Let `Y` be a grading of the hermitian space `V`, `Y.besselGroup` its Bessel subgroup of `G E ε`
with Haar measure `haar`, and `Y.besselFin` the group of `u ∈ Gf E ι` with `(1, u)` in
`Y.besselGroup`. Let `β` be measurable on `G E ε`, of integral one over each orbit of
`Y.besselGroup`, let `η` be a left invariant measure on `Y.besselFin`, and let `φ` be measurable on
`Gf E ι`. The integral of the weight `g ↦ (∫ u, β (g.1, u) ∂η) * φ g.2` over the orbit of `t` under
`Y.besselGroup` is the integral of `u ↦ φ (u⁻¹ * t.2)` against `η`. 

### `integral_quotMeasure_eq_integral_withDensity`

 Let `Y` be a grading of the hermitian space `V`, `Y.besselGroup` its Bessel subgroup of the
adelic unitary group `G E ε = GInf E ε × Gf E ι`, and `Y.ratBessel` the rational points of that
subgroup. Let `w` be a measurable weight on `G E ε` such that the integral of `r ↦ w (r * t)` over
`Y.besselGroup`, against its Haar measure `haar`, is one for `t` in the measurable set `U` and zero
otherwise. Let `f` vanish off `U` and be measurable, left invariant (`FixesLeft`) under
`Y.ratBessel` and integrable on the quotient of `G E ε` by it. Then the integral of `f` over this
quotient is the `w`-weighted integral over `t` of the period of `r ↦ f (r * t)` over `Y.besselGroup`
modulo `Y.ratBessel`. 

### `integral_withDensity_mul_eq_mul`

 For a product weight `α g.1 * ψ g.2` on `G E ε = GInf E ε × Gf E ι`, the weighted integral of a
product function `a g.1 * b g.2` is the product of the weighted integrals over the two factors. 

### `_root_.New.Grading.exists_integral_eq_sum_over_cut`

 Let `Y` be a grading of the hermitian space `V`, with Bessel subgroup `Y.besselGroup` of
`G E ε`, finite part `Y.besselFin` and rational points `Y.ratBessel`. Given a level `A` and a
function `a` on `GInf E ε`, there is a constant `κ` with the following property. For every level
`J`, finite set `T ⊆ Gf E ι ⧸ J` (the "cut"), function `f` on `G E ε` and function `b` on
`Gf E ι ⧸ J`, the integral of `f` over the quotient of `G E ε` by `Y.ratBessel` is
`κ * ∑ t ∈ T, b t / m t`, where `m t = coverMultiplicity Y.besselFin A T t` counts the classes of
`r ∈ Y.besselFin` modulo `A` with `r⁻¹ • t ∈ T`, whenever:
* `hf_cont`, `hf_rat`, `hf_int`: `f` is continuous, left invariant under `Y.ratBessel` (`FixesLeft`)
  and integrable for `Y.ratBessel.quotMeasure`, the measure of integration over the quotient;
* `hT_stable`: `T` is stable under `Y.besselFin ⊓ A`;
* `hf_supp`: `m ≠ 0` at the finite part of each point where `f ≠ 0`;
* `h_period`: at each `t` with finite part in `T`, the integral of `r ↦ f (r * t)` over
  `Y.besselGroup` modulo `Y.ratBessel` is the index `stdLevelIndex J` of `J` in `stdLevel E ι` times
  `a t.1 * b t.2`. 
