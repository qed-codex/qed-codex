---
{
  "module": "src/Lib/SiegelWeil/OneVector/SemilocalDensityBounds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/SiegelWeil/OneVector/SemilocalDensityBounds.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/SiegelWeil/OneVector/SemilocalDensityBounds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Bounds for local densities at finitely many finite places

Let `A` be a finite place in the sense of `New.Floors.IntegralPlace`, which may be a product of
several completions, with ring of integers `R` and modulus `modulus`. Let `L` be the lattice of
integral vectors, let the character `ψ` be trivial on traces, and let `ζ_R(μ) = New.idealZeta R μ`
be at most `2`. No uniformizer is assumed: the Gauss sums are summed over the ideals of `R`.

* `New.Floors.IntegralPlace.measure_residueClass_le_idealZeta`: for a unimodular hermitian form of
  rank at least `2 μ + 1`, a class modulo `g L` has mass at most `ζ_R(μ) (modulus g)⁻¹` times its
  volume on each quadric.
* `New.Floors.IntegralPlace.one_add_enorm_measure_intVectors_sub_one_le`: on an integral quadric the
  mass of `L` differs from `1` by at most `ζ_R(μ) - 1`.

Notions from other files:
* `IntegralPlace A`: the data `integers`, `ψ`, `element`, `skewUnit`, `skewMeasure` and `modulus` of
  the place; `element` has trace `1`, and `skewMeasure` is a measure on the skew elements `b`, those
  with `b̄ = -b`. `skewUnit` is a unit of `A` with integral inverse, and
  `(a, b) ↦ element skewUnit⁻¹ a + b` carries `skewMeasure ⊗ skewMeasure` to Haar measure.
* `IsUnimodular R J`: the matrix `J` is hermitian and lies in `GL_n(R)`.
* `IsDisintegration volume J l`: the measures `l t`, on the quadrics `x* J x = skewUnit⁻¹ t`,
  disintegrate the Haar measure.
* `classGaussSum J g x₀ α b`: the integral of `ψ (element b (x* J x - α))` over the class
  `x₀ + g L`.

## Relation to the literature

Known result: bounds for local densities of hermitian forms by Gauss sums, part of Siegel's formula
for representing a number by a hermitian form. See `Lib.SiegelWeil.OneVector.SiegelClassSum`.


### `skewMeasure_setOf_mul_mem_sq_le`

 At a finite place `A` with ring of integers `R`, let `u` be a unit of `A`, and let `skewMeasure`
be the measure of the place on the skew `b` (those with `b̄ = -b`). Then the square of the measure
of the set of the skew `b` with `u b ∈ R` is at most `(modulus u)⁻¹`, where `modulus x` is the
factor by which multiplication by `x` scales Haar measure. 

### `exists_unit_sub_mem`

 A generator of `R + ν R`. For every `ν` there is a unit `η` of `A` that is congruent to `ν`
modulo the ring of integers `R` and such that `η c` is integral exactly when `c` and `ν c` are. So
`η⁻¹` generates the ideal of the `c ∈ R` with `ν c ∈ R`. 

### `lintegral_enorm_classGaussSum_le_idealZeta`

 Let `ζ_R(μ) ≤ 2`, where `ζ_R(μ) = idealZeta R μ` is the sum of `[R : I] ^ (-μ)` over the ideals
of finite index. Let `J` be unimodular of rank at least `2 μ + 1` and let `ψ` be trivial on traces.
The Gauss sum `classGaussSum J g x₀ α b` is the integral of `ψ (τ b (x* J x - α))` over the class
`x₀ + g L`, where `τ = element` is the place's fixed integral element with `τ + τ̄ = 1` (independent
of `b`) and `L` is the lattice of integral vectors. Over the skew frequencies `b`, its absolute
value has integral at most `ζ_R(μ) (modulus g)⁻¹` times the volume `modulus g ^ card κ` of the
class, where `modulus g` is the factor by which multiplication by `g` scales Haar measure. 

### `measure_residueClass_le_idealZeta`

 The mass of a class `x₀ + g L` on a quadric, for any unit `g`, where `L` is the lattice of
integral vectors and `modulus g` is the factor by which multiplication by `g` scales Haar measure.
Let `ζ_R(μ) ≤ 2`, where `ζ_R(μ) = idealZeta R μ` is the sum of `[R : I] ^ (-μ)` over the ideals of
finite index. Let `J` be unimodular of rank at least `2 μ + 1`, let the measures `l t`, on the
quadrics `x* J x = skewUnit⁻¹ t` for skew `t`, disintegrate Haar measure, and let `ψ` be trivial on
traces. Then the class has mass at most `ζ_R(μ) (modulus g)⁻¹` times its volume for every `l t`. 

### `classGaussSum_one_zero_eq_one`

 At the unit class, the Gauss sum at an integral frequency is `1`: let `J` be unimodular, let `α`
and `b` be integral, and recall that `classGaussSum J 1 0 α b` is the integral of
`ψ (element b (x* J x - α))` over the integral vectors `x`. Then this integral is `1`. 

### `one_add_enorm_measure_intVectors_sub_one_le`

 The mass of the lattice on an integral quadric. Let `ζ_R(μ) ≤ 2`, where
`ζ_R(μ) = idealZeta R μ` is the sum of `[R : I] ^ (-μ)` over the ideals of finite index. Let `J` be
unimodular of rank at least `2 μ + 1`, let the measures `l t`, on the quadrics
`x* J x = skewUnit⁻¹ t` for skew `t`, disintegrate Haar measure, and let `ψ` be trivial on traces.
For integral `t`, the mass of the lattice `intVectors R κ` of integral vectors for `l t` differs
from `1` by at most `ζ_R(μ) - 1`. 
