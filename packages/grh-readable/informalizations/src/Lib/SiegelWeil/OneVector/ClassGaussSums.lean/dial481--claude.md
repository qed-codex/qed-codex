---
{
  "module": "src/Lib/SiegelWeil/OneVector/ClassGaussSums.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/SiegelWeil/OneVector/ClassGaussSums.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/SiegelWeil/OneVector/ClassGaussSums.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Gauss sums of classes modulo a lattice at a finite place

Let `A` be a finite place (`New.Floors.IntegralPlace`) with ring of integers `R`, modulus `modulus`
and a character `ψ` that is trivial on traces. Let `L` be the lattice of integral vectors and `g` a
unit of `A`.

Notions from other files:

* `New.Floors.IntegralPlace`: a semilocal field with conjugation, a compact open subring `R` of
  volume `1` that is self-dual for `ψ`, an integral `τ` with `τ + τ̄ = 1`, a skew unit
  `δ = skewUnit`, a modulus and a measure `skewMeasure` on the skew elements, those with `b̄ = -b`.
* `New.Floors.IntegralPlace.latticeMultiple κ g`: the lattice `g L` in `κ → A`.
* `New.IsUnimodular R J`: the matrix `J` is hermitian and invertible over `R`.
* `New.Floors.Place.IsDisintegration`: the measures `l t`, indexed by skew `t`, disintegrate a
  measure along `x ↦ x* J x`, with `l t` living over the value `δ⁻¹ t`.

Main definition and results:

* `New.Floors.IntegralPlace.classGaussSum`: the Gauss sum of a hermitian form on a class modulo
  `g L`.
* `New.Floors.IntegralPlace.enorm_classGaussSum_sq_le`: Weyl differencing bounds it, for a
  unimodular form, in terms of the denominator of the frequency.
* `New.Floors.IntegralPlace.integral_classGaussSum`,
  `New.Floors.IntegralPlace.measure_residueClass_le_lintegral`: by Fourier inversion, the mass of a
  class on a quadric is the integral of its Gauss sums over the skew frequencies if they are
  integrable, and it is always at most the integral of their modulus.

## Relation to the literature

Known result: bounds for local densities of hermitian forms by Gauss sums, part of Siegel's formula
for representing a number by a hermitian form. See `Lib.SiegelWeil.OneVector.SiegelClassSum`.


### `classGaussSum`

 The Gauss sum of the class `x₀ + g L` at the frequency `b`: the integral over the class of
`ψ (τ b (x* J x - α))`, where `τ + τ̄ = 1`. 

### `psi_mul_trace`

 If `ψ` is trivial on traces and `b` is skew, then `ψ (τ b (s + s̄)) = ψ (b s)`, where
`τ + τ̄ = 1`. 

### `conj_psi_mul_psi_add`

 The phase of Weyl differencing. For hermitian `J`, skew `b` and `ψ` trivial on traces, the
quotient of the values of `x ↦ ψ (τ b (x* J x - α))` at `x + d` and `x` is
`ψ (τ b d* J d) ψ (b x* J d)`. 

### `smul_mem_intVectors_of_psi_eq_one`

 Duality for a unimodular form `J`: if the character `y ↦ ψ (b y* J d)` is trivial on the lattice
`g L`, where `L` is the lattice of integral vectors, then `b ḡ d` is an integral vector. 

### `mem_latticeMultiple_mul_of_psi_eq_one`

 Let `J` be unimodular over the ring of integers `R` and let `w` be a unit such that `w R`
contains every integral `c` for which `g ḡ b c` is integral. If the character `y ↦ ψ (b y* J d)` is
trivial on `g L`, where `L` is the lattice of integral vectors and `d ∈ g L`, then `d ∈ g w L`. 

### `enorm_classGaussSum_sq_le`

 Weyl differencing, with the volumes expressed by the modulus `P.modulus`: the lattice `g L` of
vectors has volume `P.modulus g ^ card κ`. Let `J` be unimodular over the ring of integers `R`, `b`
skew and `ψ` trivial on traces. Let `w` be a unit such that `w R` contains every integral `c` for
which `g ḡ b c` is integral. Then the squared modulus of `classGaussSum J g x₀ α b` is at most the
volume of `g L` times the volume of `g w L`, where `L` is the lattice of integral vectors.
`classGaussSum J g x₀ α b` is the integral over the class `x₀ + g L` of `ψ (τ b (x* J x - α))`, with
`τ` the fixed integral element satisfying `τ + τ̄ = 1`. 

### `integrable_classGaussSum`

 For a unit `g`, a vector `x₀` and `α : A`, the Gauss sums of the class `x₀ + g L` at level `α`
are integrable in the skew frequency `b` for the measure `P.skewMeasure` as soon as their modulus
has a finite integral. 

### `integral_classGaussSum`

 Fourier inversion for a class. Let the measures `l t` disintegrate Haar measure along the
hermitian form of `J`, and let `ψ` be trivial on traces. If the Gauss sums of the class
`residueClass g x₀ = x₀ + g L` are integrable over the skew frequencies for the measure
`P.skewMeasure`, their integral is the mass of the class on the quadric `x* J x = δ⁻¹ t`, where
`δ = P.skewUnit`. 

### `measure_residueClass_le_lintegral`

 Let the measures `l t` disintegrate Haar measure along the hermitian form of `J`, and let `ψ` be
trivial on traces. The mass of the class `residueClass g x₀ = x₀ + g L` on the quadric
`x* J x = δ⁻¹ t`, where `δ = P.skewUnit`, is at most the integral of the modulus of its Gauss sums
over the skew frequencies, for the measure `P.skewMeasure`. 
