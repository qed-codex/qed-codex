---
{
  "module": "src/New/Congruences/FirstOrder/TateTwistCocycles.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/FirstOrder/TateTwistCocycles.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/FirstOrder/TateTwistCocycles.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Cocycles of Tate twists: the even part and the triangle cost

This file studies cocycles of `Gal(Ω/E)` with values in a twist `(O/ℓ^ν)(-e)`
(`New.Selmer.tateTwist`). It shows that the even part of a cocycle lies in the even classes.
It shows that a cocycle that obeys the crystalline relations above `ℓ` vanishes on
`New.Selmer.shaLocalSet`. It also shows that a triangle of primes gives a triangle cost.

## Main definitions and results

* `New.Selmer.add_conjGal_mem_evenClasses`: let `e ≠ 0`, and let a cocycle with values in
  `(O/ℓ^ν)(-e)` be unramified off ℓ, S and S̄ and zero on `New.Selmer.shaLocalSet`. Then its even
  part `c + c ∘ New.conjGal` lies in `New.Selmer.evenClasses`.
* `New.Selmer.hasTriangleCost_tateTwist`: let the tame generator family `w j`, with elements `τ j`,
  `φ j` and exponents `ty j`, form a triangle for `g₀` that holds up to `ℓ ^ h`
  (`New.Selmer.IsPrimeTriangle`), and let `e < t`. Let `Z` be a module of cocycles with values in
  `(O/ℓ^ν)(-e)`, unramified off `ℓ`, the `w j` and their conjugates, and let
  `cyclotomicInv g₀ ^ e - 1` kill the value at `g₀` of each member unramified off `ℓ`. Then the
  triangle cost of `Z` (`New.Selmer.HasTriangleCost`) is bounded by its length relative to the
  cocycles obeying the crystalline relations plus the length of the odd classes.

Notions from other files:
* `New.Selmer.tateTwist`: the rank-one representation `O(-e)`, given by the power `e` of the inverse
  `New.Selmer.cyclotomicInv` of the cyclotomic character. `New.conjGal`: the map g ↦ g^c = cgc,
  with c the chosen complex conjugation.
* `New.Selmer.shaLocalSet`: the union of the inertia groups above `ℓ` if `e = 0`; otherwise the
  elements of the decomposition groups above `ℓ` with trivial cyclotomic character.
* `New.Selmer.evenClasses`, `New.Selmer.shaOdd`: cocycles in `(O/ℓ^ν)(-e)` with local conditions
  above `ℓ`. Even classes are invariant under `New.conjGal`; odd classes are unramified off `ℓ` and,
  if `e ≠ 0`, change sign under it.
* `New.Selmer.IsPrimeTriangle`: a linearly ordered tame generator family `w j` with monotone
  exponents `ty j`. An even class of exponent `ty j` that kills the earlier `τ i`, and the earlier
  `φ i` of the same exponent, has its value at `τ j` killed by `ℓ ^ h`. Finitely many test points
  and `g₀` detect the cocycles unramified off `ℓ`, and `g₀` separates the characters up to `ℓ ^ h`.
* `New.Selmer.HasTriangleCost Z τ τ' φ φ' I C b`: for the members `Z₀` of `Z` that vanish on some
  set, agreement at the earlier pairs `τ i`, `τ' i` and, for `i ∈ I`, `φ i`, `φ' i` gives agreement
  at `τ j`, `τ' j` up to `C` for `j ∈ I`. The length of `Z / Z₀`, plus the length modulo `C`-torsion
  of any submodule of `Z₀` that is zero at all `τ j`, `τ' j` and agrees at the `φ j`, `φ' j` with
  `j ∈ I`, is at most `b`.

## Relation to the literature

See `New.Congruences.FirstOrder.RibetElement` for related work.


### `add_conjGal_mem_evenClasses`

 Let `e ≠ 0`, and let `c` be a continuous cocycle with values in `(O/ℓ^ν)(-e)` that is unramified
outside `ℓ` and `S ∪ S̄` and vanishes on `shaLocalSet ℓ E e`. Then the even part `c + c ∘ conjGal`,
with `conjGal` conjugation by complex conjugation, is an even class (`evenClasses`): a cocycle with
the same properties that is invariant under `conjGal`. 

### `apply_withConjInv_false_eq_neg`

 Let `τ j` be tame generators at places `w j` off `ℓ`, and let the `φ j` fix the `ℓ ^ ν`-th roots
of unity (`IsTameGeneratorFamily`), so that all of them act trivially on `(O/ℓ^ν)(-e)`. Let `z` be a
cocycle with values there. Then the value of `z` at `(conjGal (τ j))⁻¹`, which is
`withConjInv τ (j, false)`, is `-z (conjGal (τ j))`, and likewise for `φ j`. 

### `apply_eq_zero_of_mem_obeying_crysRelations`

 Let `z` be a cocycle of `Gal(Ω/E)` with values in `(O/ℓ^ν)(-e)`, the Tate twist `O(-e)` modulo
`ℓ^ν`, that obeys the linear relations `crysRelations` of the crystalline cocycles at each place
above `ℓ`. Then `z` vanishes on `shaLocalSet ℓ E e`: on the inertia groups above `ℓ` if `e = 0`, and
otherwise on the elements of the decomposition groups above `ℓ` with trivial cyclotomic
character. 

### `relLength_torsionBy_le_length_shaOdd`

 Let the places `w j` off `ℓ`, with tame generators `τ j`, elements `φ j` and exponents
`0 < ty j < t`, form a triangle of primes for `g₀` (`IsPrimeTriangle`). The following is used:
`4 (cyclotomicInv g₀ ^ e - 1) ^ 2` divides `ℓ ^ h`; there are finitely many test points in the
Galois group such that a cocycle unramified off `ℓ` that vanishes at them and at `g₀` is zero; and
at each test point twice the value of an even class of exponent `e` unramified off `ℓ`
(`evenClasses`) is its value at some `φ j` with `ty j = e`. Let `0 < e < t`, and let `S` be a module
of cocycles for `O(-e)` modulo `ℓ^ν`, unramified off `ℓ` and zero on `shaLocalSet ℓ E e`, whose
values at `g₀` are killed by `cyclotomicInv g₀ ^ e - 1` and whose even parts vanish at the `φ j`
with `ty j = e`. Then the length of `S` modulo its `ℓ^h`-torsion (`relLength`) is at most that of
`shaOdd`, the cocycles with the same local conditions that change sign under `conjGal`. 

### `hasTriangleCost_tateTwist`

 Let the places `w j` off `ℓ`, with tame generators `τ j`, elements `φ j` and monotone exponents
`ty j`, form a triangle of primes for `g₀` up to `ℓ ^ h` (`IsPrimeTriangle`): among other clauses,
`ℓ ^ h` kills the value at `τ j` of an even class of exponent `ty j` that vanishes at the earlier
`τ i` and at the earlier `φ i` of that exponent; `c` bounds `h` times the number of places and test
points. Let `e < t`, and let `Z` be a module of cocycles with values in `(O/ℓ^ν)(-e)`, unramified
off `ℓ`, the `w j` and their conjugates; let `cyclotomicInv g₀ ^ e - 1` kill the value at `g₀` of
each member that is unramified off `ℓ`. Let `b` bound the length of `Z / (Z ⊓ Zf)` (`relLength`),
where `Zf` consists of the functions that obey the linear relations `crysRelations` of the
crystalline cocycles above `ℓ`, plus the length of the odd classes `shaOdd`. Write `τ' j`, `φ' j`
for the inverses of the conjugates of `τ j`, `φ j`, and `I` for the `j` with `ty j = e`. Then
`HasTriangleCost` holds: for the members `Z₀` of `Z` that vanish on some set, (a) if `z ∈ Z₀` agrees
at `τ i`, `τ' i` for `i < j` and at `φ i`, `φ' i` for `i < j` in `I`, then `ℓ ^ h • z` agrees at
`τ j`, `τ' j` for `j ∈ I`; (b) the length of `Z / Z₀`, plus the length modulo `ℓ ^ h`-torsion of any
submodule of `Z₀` that vanishes at all `τ j`, `τ' j` and agrees at `φ j`, `φ' j` for `j ∈ I`, is at
most `b`. 
