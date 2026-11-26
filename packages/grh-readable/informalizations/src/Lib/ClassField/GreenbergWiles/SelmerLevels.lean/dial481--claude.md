---
{
  "module": "src/Lib/ClassField/GreenbergWiles/SelmerLevels.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/GreenbergWiles/SelmerLevels.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/GreenbergWiles/SelmerLevels.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Selmer cocycles, N-units, split places and the equivariant S-unit theorem

This file prepares the counting of Selmer groups over a number field `K`. Here `G` is the profinite
Galois group of an algebraically closed field `Ω` over `K`, and finite places of `Ω` are valuation
subrings (`ClosurePlace`), and `B N` is the valuation of `N` at `B`. `New.DiscreteUnits Ω` is `Ωˣ`
written additively, and `New.Z1` are the continuous 1-cocycles.

## Main definitions and results

* `New.IsLargeLevel.sUnits`, `New.IsLargeLevel.fixedSUnits`, `New.IsLargeLevel.fixedSUnitsRep`: the
  `N`-units of `Ω`, those fixed by an open normal subgroup `U`, and the latter as a representation
  of `G ⧸ U`.
* `New.selmerZ1`: cocycles with local conditions.
* `New.IsLargeLevel.SplitPlaces`: a family of distinct primes outside `N`, each with a Frobenius
  element in `U`. Here `N` is adapted to `U`: inertia above primes not dividing `N` lies in `U`, and
  the primes dividing `N` generate the class groups of the number fields between `K` and the fixed
  field of `U`.
* `New.IsLargeLevel.dirichlet_fixedSUnits`: for an open normal subgroup `Q` of `G`, the `N`-units of
  the fixed field of `Q`, times `ℤ`, form a finitely generated group of rank at most the number of
  places of that field above `N` and infinity, and have linearly independent equivariant additive
  maps to `ℝ` indexed by these places.

Notions from other files:
* `New.IsProGalois`: a profinite group acts on the Galois extension Ω/K as its Galois group, with
  open stabilisers.
* `New.IsPlaceOver`: the valuation subring A of Ω lies over the prime w of E: an integer of E is in
  the maximal ideal of A exactly when it lies in w.
* `New.IsFrob`: for a given q, σ stabilises A and σx ≡ x^q modulo the maximal ideal of A for every x
  in A.
* `New.inertiaAbove`: for a set S of primes of K, the union of the inertia groups in Gal(Ω/K) of all
  valuation subrings of Ω over a prime in S.

## Relation to the literature

Known; see `Lib.ClassField.GreenbergWiles.CocycleCounts` and `Lib.ClassField.Places.LocalFields` for
sources.


 ### Inertia, places above `N` and cocycles 

### `IsTameGeneratorFor`

 The element `γ` of `G` acts as a standard generator of tame inertia of order `m` at the
valuation subring `A`: it lies in the inertia group of `A`, and, for some uniformiser `π` of `K`
for `A` and some `m`-th root `y` of `π`, the quotient `γ y / y` is the fixed primitive `m`-th root
of unity `New.rootPowHom Ω m 1`. 

### `exists_isTameGeneratorFor`

 Let the profinite group `G` act on `Ω` as the Galois group of `Ω/K`, and let the valuation
subring `B` of `Ω` lie over the prime `v` of `K`. Then, for every `m ≠ 0`, some `γ ∈ G` is a tame
generator of order `m` at `B`. That is, `γ` lies in the inertia group of `B`, and for some
uniformiser `π` of `K` for `B` and some `m`-th root `y` of `π`, the quotient `γ y / y` is the fixed
primitive `m`-th root of unity `rootPowHom Ω m 1`. 

### `PlaceAboveLevel`

 The places of Ω above N and infinity: valuation subrings in which N has valuation below 1,
together with the infinite places. 

### `DiscreteModule.Z1.eq_zero_on_decompGroup`

 A continuous 1-cocycle that vanishes on the inertia group and at a Frobenius element of a
place `B` above the prime `v`, whose residue field has `v.q` elements, vanishes on the
decomposition group of `B`. 

 ### Selmer cocycles, `N`-units and split places 

### `selmerZ1`

 The Selmer cocycles: the submodule of continuous 1-cocycles `x : Gal(Ω/K) → V` that satisfy
three conditions. (a) `x g = 0` for every `g` in the inertia group of a place over a prime outside
`S ∪ P`. (b) For every prime `v ∈ S`, the restriction of `x` to the decomposition group of the
chosen valuation subring `A v` lies in the given submodule `L v` of functions on that group.
(c) `x c = 0` for every complex conjugation `c`. The conditions are put on cocycles, not on
cohomology classes. 

### `finite_cocycles_unramified_outside`

 Let `G` be a Galois group of `Ω` over a number field `K`, for instance an open subgroup of
another such group, and `S` a finite set of primes of `K`. For a finite discrete `G`-module, only
finitely many continuous cocycles vanish on the inertia group of every valuation subring of `Ω`
that lies over a prime outside `S` (`New.IsPlaceOver`). This is usually deduced from the
Hermite–Minkowski theorem; the proof here uses class field theory. 

### `selmerZ1.finite_unramified_cocycles`

 For a finite discrete module `V` of `Gal(Ω/K)` and a finite set `S` of primes of `K`, only
finitely many continuous 1-cocycles with values in `V` vanish on all inertia groups above the primes
outside `S`. This is the case `G = Gal(Ω/K)` of `finite_cocycles_unramified_outside`.

Compare the finiteness of Galois cohomology with restricted ramification in Milne's Arithmetic
Duality Theorems. Here only degree one is treated, for cocycles rather than classes, and `V` itself
need not be unramified outside `S`. 

### `sUnits`

 The N-units of Ω: elements of Ω^× that are units in every valuation subring in which N does
not have valuation below 1. 

### `fixedSUnits`

 The N-units of the fixed field of U: the N-units of Ω that are fixed by U. 

### `fixedSUnitsRep`

 The `N`-units of the fixed field of `U`, as a representation of `G ⧸ U` over `ℤ`. 

### `SplitPlaces`

 Split places for `U`. The subgroup `U` fixes the `m`-th roots of unity, and `m` divides `N`. The
primes `v i` are distinct and do not divide `N`. Each has a place above it with a Frobenius element
in `U`. The set `I` is the union of the inertia groups above the other primes not dividing `N`.
Inertia above every prime not dividing `N` lies in `U`. The primes dividing `N` generate the class
group of every number field between `K` and the fixed field of `U`. 

### `SplitPlaces.cyclotomicCharMod_eq_one`

 `U` fixes the `m`-th roots of unity: the cyclotomic character modulo `m` is trivial on it. 

### `SplitPlaces.dvd_level`

 `m` divides `N`. 

### `SplitPlaces.v`

 The chosen primes of `K`. 

### `SplitPlaces.v_injective`

 The chosen primes are distinct. 

### `SplitPlaces.level_notMem`

 No chosen prime divides `N`. 

### `SplitPlaces.valuationSubring`

 A place of `Ω` for each chosen prime. 

### `SplitPlaces.isPlaceOver`

 The place `valuationSubring i` lies over `v i`. 

### `SplitPlaces.φ`

 An element of `G` for each chosen prime. 

### `SplitPlaces.isFrob`

 `φ i` is an arithmetic Frobenius at `valuationSubring i` and lies in `U`. 

### `SplitPlaces.mem_inertia_iff`

 `I` is the union of the inertia groups of the places over the primes of `K` that are not
  chosen and do not divide `N`. 

### `SplitPlaces.inertiaGroup_le`

 The inertia group of every place over a prime not dividing `N` lies in `U`. 

### `SplitPlaces.principal_sup_idelesUnitOff`

 For each number field `F` between `K` and the fixed field of `U`, the principal ideles and the
  ideles that are units away from the primes dividing `N` generate all finite ideles. 

 ### `N`-units of `K` and split primes 

### `ofBase_mem_sUnits`

 An element `x` of `Kˣ`, sent to `Ωˣ` by `DiscreteUnits.ofBase`, is an `N`-unit of `Ω` exactly
when it is an `S`-unit of `K` (`Set.unit`) for `S` the set of primes that divide `N`, that is, a
unit at every prime of `K` that does not divide `N`. 

### `SplitPlaces.FrobeniiDetectRoots`

 The property that the Frobenius elements `s.φ i` detect `m`-th roots: every `y` in `Ωˣ` whose
`m`-th power is an `N`-unit of the fixed field of `U`, and which every `s.φ i` fixes, is fixed by
all of `U`. 

### `mem_sUnits_of_nsmul_mem`

 For `m ≠ 0`, an element of Ωˣ whose `m`-th power is an `N`-unit of the fixed field of `U` is
itself an `N`-unit of Ω. 

### `SplitPlaces.decompGroup_le`

 Let `s : SplitPlaces m N I U ι` be split places for the open normal subgroup `U`, with chosen
primes `s.v i` indexed by a type `ι`. If the valuation subring `B` lies over a chosen prime `s.v i`,
then its decomposition group lies in `U`. 

### `SplitPlaces.liftToSubgroup`

 Given split places `s : SplitPlaces m N I U ι`, with chosen primes indexed by a type `ι`, pass
to an open subgroup `B` that contains `U`. Let `Q` be an open normal subgroup of `B` that contains
`U` and fixes the `m`-th roots of unity. Let `σ` pick a representative of each coset of `B`. Take
the places `(σ x)⁻¹ • s.valuationSubring i`, the primes below them in the fixed field of `B`, and
the conjugated Frobenius elements. They form split places for `Q`, indexed by `ι × G ⧸ B`. Their
inertia set is the preimage of `I` in `B`. 

### `SplitPlaces.mem_and_conj_mem`

 For split places `s : SplitPlaces m N I U ι`, with chosen primes indexed by a type `ι`, the set
`I` (the union of the inertia groups above the primes that are not chosen and do not divide `N`)
lies in `U` and is stable under conjugation. 


## Places above N and infinity and the equivariant unit theorem

For an open normal subgroup `Q` of `G`, `New.IsLargeLevel.fixedSUnits N Q` is the group of `N`-units
of `Ω` fixed by `Q`, written additively, with its action of `G ⧸ Q`. The unit theorem is stated for
its product with `ℤ`: this summand shifts all the logarithms at infinity at once and makes up for
the `- 1` in Dirichlet's rank.


### `finrank_prod_int_le_of_surjective`

 If an abelian group `B` is the image of a finitely generated one `A`, the rank of `B × ℤ` is
at most that of `A` plus one. 

### `linearIndependent_sUnit_log`

 Let `M` give, for each place in `S` or at infinity, a function on pairs of an `S`-unit `u` and
an integer `n`: at `v ∈ S` it vanishes exactly when `u` is a unit at `v`, and at an infinite place
`w` it is `log |u|_w + n`. These functions are linearly independent over ℝ. For logarithms at all
places this is the nonvanishing of the `S`-regulator. 

### `PlaceAboveLevel.bijective_orbits`

 Let the profinite group `G` act on `Ω` as the Galois group of `Ω` over the number field `K`,
let `N ≠ 0`, and let the valuation subring `A v` of `Ω` lie over `v` for each prime `v` of `K`.
Lift each prime `v` dividing `N` to `A v`, and each infinite place of `K` to a chosen infinite
place of `Ω` over it. The lifts lie in `PlaceAboveLevel N`: the valuation subrings of `Ω` in which
`N` has valuation below one, together with the infinite places of `Ω`. Then sending a place of `K`
above `N` or infinity to the orbit of its lift is a bijection onto the `G`-orbits of
`PlaceAboveLevel N`. 

### `exists_surjective_sUnit_to_fixedSUnits`

 For an open normal subgroup `Q`, the units of the fixed field `F` of `Q` away from the primes
dividing `N` map onto the `N`-units of `Ω` fixed by `Q`, by the inclusion of `Fˣ` in `Ωˣ`. 

### `ordRat_inv_smul`

 The order, normalised on `K`, of `g⁻¹ y` at a place `B` above `N` is the order of `y` at
`g • B`. 

### `IsLargeLevel.dirichlet_fixedSUnits`

 Dirichlet's theorem for the group `E = fixedSUnits N Q` of `N`-units of the fixed field of `Q`,
with the action of `G ⧸ Q` (`fixedSUnitsRep`). Let `X` be the set of `Q`-orbits of
`PlaceAboveLevel N`, the places of `Ω` above `N` and infinity. Then `E` is finitely generated, and
there are additive maps `Λ z` from `E × ℤ` to `ℝ`, for `z : X`, such that (a) `G ⧸ Q`, acting
trivially on `ℤ`, permutes the `Λ z` as it permutes the `z`, and (b) the `Λ z` are linearly
independent over `ℝ`. Moreover (c) the rank of `E × ℤ` is at most `#X`. 
