---
{
  "module": "src/Lib/ClassField/GreenbergWiles/Relations.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/GreenbergWiles/Relations.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/GreenbergWiles/Relations.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Relations at split primes

Let `M` be a discrete Galois module with local conditions at a finite set `S` of primes; `Z(P)`
(`cocycles P`) is the group of cocycles allowed at each prime of `S`, zero at complex conjugations,
unramified outside `S ∪ P`. A relation is a function on an open normal subgroup `U` with values in
the dual of `M` that has the properties of the restriction of a dual cocycle, among them the
reciprocity law at primes that are split for `U`. The module of relations takes the place of the
dual Selmer group: at a split prime where the relation `y` is unramified, `y(φ)(z(γ))` is the local
pairing of `y` with a cocycle `z`.

* `New.SplitPrime`, `New.RelationSetting`: split primes, and the module with its local conditions.
* `New.RelationSetting.relations`: the relations off a finite set `T`; there are finitely many if
  `M` is finite.
* `New.RelationSetting.exists_splitPlaces_forall_exists_mem_relations`: one family of split primes
  gives relations at all split primes.
* `New.RelationSetting.exists_card_cocycles_le`: a lower bound for the number of relations.

Notions from other files:
* `New.IsLargeLevel.SplitPlaces`: a family `s` of distinct primes `s.v i` prime to a level `q`, with
  Frobenius elements `s.φ i` in `U` at places `s.valuationSubring i` above `s.v i`; inertia at the
  primes prime to `q` lies in `U`, and `I` is the union of the inertia groups above those primes not
  in the family. Its property `FrobeniiDetectRoots` says that an `m`-th root of a `q`-unit of the
  field of `U` that all `s.φ i` fix is fixed by `U`.
* `New.IsLargeLevel.fixedSUnits q U`: the `q`-units of the field of `U`; `New.unitsRep` is the
  Galois action on `Ωˣ`, written additively.
* `New.cyclotomicCharMod`: the cyclotomic character modulo `m`.

## Relation to the literature

Part of a known result: Greenberg–Wiles formula, as a lower bound for the dual side. See
`Lib.ClassField.GreenbergWiles.CocycleCounts`. Source: Darmon, Diamond, Taylor, Fermat's Last
Theorem, Theorem 2.19; the case that is used is proved here.


### `SplitPrime`

 A place above a prime of `K`, with a Frobenius element in the open normal subgroup `U` and a
tame generator of inertia modulo `m`. The Frobenius element is arithmetic; passing to its inverse
only changes the sign of each relation. That the prime avoids a given finite set is imposed where
the structure is used. 

### `SplitPrime.prime`

 The prime of `K`. 

### `SplitPrime.place`

 The place of `Ω` above it. 

### `SplitPrime.isPlaceOver`

 The place lies above the prime. 

### `SplitPrime.frob`

 The Frobenius element. 

### `SplitPrime.isFrob`

 `frob` is a Frobenius element at the place. 

### `SplitPrime.frob_mem`

 `frob` lies in `U`; where inertia above `prime` lies in `U`, this says that `prime` splits in
  its field. 

### `SplitPrime.tameGenerator`

 The inertial element. 

### `SplitPrime.isTameGeneratorFor`

 `tameGenerator` multiplies an `m`-th root of a uniformiser by the fixed root of unity. 

### `RelationSetting`

 The setting for relations among values of cocycles at split primes: a module `M` killed by `m`
and fixed by complex conjugations, an open normal subgroup `U` (`subgroup`) that fixes `M` and the
`m`-th roots of unity, and local conditions on a finite set `S` (`localPrimes`) of primes outside
which `M` is unramified. In addition `U` contains no complex conjugation. The number `m` need not be
a prime power, `S` need not contain the primes above `m`, and a local condition is a module of
functions, whose cocycles form the group `A_v`. 

### `RelationSetting.nsmul_eq_zero`

 The module is killed by `m`. 

### `RelationSetting.subgroup`

 The open normal subgroup. 

### `RelationSetting.apply_eq_of_mem`

 `U` fixes the module. 

### `RelationSetting.cyclotomicCharMod_eq_one`

 `U` fixes the `m`-th roots of unity. 

### `RelationSetting.notMem_of_isComplexConj`

 `U` contains no complex conjugation. 

### `RelationSetting.ρ_eq_one_of_isComplexConj`

 Complex conjugations fix the module. 

### `RelationSetting.localPrimes`

 The finite set of primes with local conditions. 

### `RelationSetting.unramified`

 The module is unramified outside `S`. 

### `RelationSetting.place`

 A place of `Ω` above each prime. 

### `RelationSetting.isPlaceOver`

 The place lies above the prime. 

### `RelationSetting.allowed`

 The local condition: the functions on the decomposition group that are allowed. 

### `RelationSetting.coboundary_le`

 Local coboundaries are allowed. 

### `cocycles`

 The group `Z(P)` of the cocycles that are allowed at each prime of `S`, vanish at complex
conjugations and are unramified outside `S ∪ P`. 

### `localCocycles`

 The group `A_v` of the local cocycles that are allowed at `v`. 

### `IsRelation`

 A relation off the finite set `T`: a continuous equivariant homomorphism `y` from `U` to
`Hom(M, ℚ/ℤ)`, extended by zero and unramified outside `T`, whose values at Frobenius elements give
a linear relation among the values of cocycles at tame generators. By global duality, the
restriction to `U` of a dual cocycle has these properties if `T` contains `S` and the primes above
`m`. 

### `IsRelation.isLocallyConstant`

 `y` is continuous for the discrete topology. 

### `IsRelation.eq_zero_of_notMem`

 `y` is extended by zero outside `U`. 

### `IsRelation.map_mul`

 `y` is a homomorphism on `U`. 

### `IsRelation.map_conj`

 `y (g u g⁻¹) = cyc(g) · y u ∘ g⁻¹`. 

### `IsRelation.unramified`

 `y` is unramified outside `T`. 

### `IsRelation.sum_eq_zero`

 Reciprocity at every finite family of distinct split primes outside `T`. 

### `relations`

 The module of relations off `T`. It takes the place of the group `Z*` of dual cocycles: only the
restrictions to `U` of dual cocycles are used, and only through the properties in `IsRelation`; the
set `T` may be larger than `S`. 

### `mem_relations`

 Membership in `relations T` is the predicate `IsRelation T`. 

### `finite_relations`

 There are finitely many relations off `T`, by the finiteness of cocycles with bounded
ramification for the group `U`. 

### `apply_eq_zero_of_notMem`

 Let the primes of `S` divide `q`. A cocycle in `Z(P)` vanishes at a tame generator at the split
prime `s.v i` when `s.v i ∉ P`, since it is unramified there. 

### `exists_cocycle_three_values`

 Let the primes of `S` divide `q`, let the split primes `s` have tame generators `γ n`, and let
`s.φ j * (g * s.φ k * g⁻¹)` act like `s.φ i` on the `m`-th roots of the `q`-units fixed by `U`.
Then some cocycle in `Z(range s.v)` has the values `a`, `-a`, `-cyc(g) g⁻¹ a` at `γ i`, `γ j`,
`γ k` (added where indices coincide) and `0` at the other `γ n`. 

### `form_eq_add`

 Let the primes of `S` divide `q`, let the split primes `s` be indexed by the cosets of `O`, and
let `ν`, a character of `M` for each coset of `O`, kill the values at their tame generators `γ i` of
the cocycles in `Z(range s.v)`. If `s.φ j * (g * s.φ k * g⁻¹)` acts like `s.φ i` on the `m`-th roots
of the `q`-units fixed by `U`, then `ν i = ν j + cyc(g) · (ν k ∘ g⁻¹)`. 

### `form_one_eq_zero`

 Let the primes of `S` divide `q`, let elements in one coset of `O` act alike on the `m`-th roots
of the `q`-units fixed by `U`, let the split primes `s` be indexed by the cosets of `O`, let the
Frobenius element at the coset of `g ∈ U` lie in that coset, and let `ν` kill the values at the tame
generators `γ i` of the cocycles in `Z(range s.v)`. Then the coefficient of `ν` at the trivial coset
is zero. 

### `form_eq_zero_of_mem_inertiaGroup`

 Let the primes of `S` divide `q`, let elements in one coset of `O` act alike on the `m`-th roots
of the `q`-units fixed by `U`, let the split primes `s` be indexed by the cosets of `O` with
`s.φ g ∈ g O` for `g ∈ U`, and let `ν` kill the values at the tame generators `γ i` of the cocycles
in `Z(range s.v)`. Then the coefficient of `ν` at the coset of an element `τ` of the inertia group
at a place `A` above a prime `v` that does not divide `q` is zero. 

### `form_sum_eq_zero`

 In the relation setting `D` (with `M` killed by `m`, the subgroup `U`, and local conditions at
the finite set `S`), write `Z(P)` for the cocycles that are allowed at each prime of `S`, vanish at
complex conjugations and are unramified outside `S ∪ P`. Let the primes of `S` divide `q`, let
elements in one coset of `O` act alike on the `m`-th roots of the `q`-units fixed by `U`, let the
split primes `s` be indexed by the cosets of `O` with `s.φ g ∈ g O` for `g ∈ U`, and let `ν` kill
the values at the tame generators `γ i` of the cocycles in `Z(range s.v)`. Then for any family `p`
of distinct split primes, prime to `q` and different from those of `s`, and any cocycle `x` in `Z`
of the primes of `p`, we have `∑ j, ν (p j).frob (x (p j).tameGenerator) = 0` (`ν` taken at the
coset of `(p j).frob` modulo `O`). 

### `isRelation_ite_form`

 Let the primes of `S` (of `D`) divide `q`, let elements in one coset of `O` act alike on the
`m`-th roots of the `q`-units fixed by `U`, and let the split primes `s` be indexed by the cosets of
`O` with `s.φ g ∈ g O` for `g ∈ U`. Let `ν` kill the values at the tame generators `γ i` of the
cocycles in `Z(range s.v)`, which are allowed on `S`, zero at complex conjugations, and unramified
off `S` and the `s.v i`. Then `g ↦ ν (g O)` on `U`, zero off `U`, is a relation off any finite `T`
containing the primes dividing `q` and those of `s`: a continuous equivariant map to `Hom(M, ℚ/ℤ)`,
unramified off `T`, whose Frobenius values give linear relations among cocycle values at tame
generators. 

### `form_frobenius_eq`

 Let the primes of `S` divide `q`, let elements in one coset of `O` act alike on the `m`-th roots
of the `q`-units fixed by `U`, let the split primes `s` be indexed by the cosets of `O` with
`s.φ g ∈ g O` for `g ∈ U`, and let `ν` kill the values at the tame generators `γ i` of the cocycles
in `Z(range s.v)`. Then the coefficient of `ν` at the coset of the Frobenius element `s.φ i` is the
coefficient at `i`. 

### `Avoids`

 The natural number `p` can be avoided: it is prime to `m`, no prime of `S` divides it, and the
primes dividing it are unramified in the field of `U`. 

### `Avoids.coprime`

 `p` is prime to the modulus. 

### `Avoids.notMem`

 No prime of `S` divides `p`. 

### `Avoids.inertiaGroup_le`

 The primes dividing `p` are unramified in the field of `U`. 

### `exists_splitPlaces_forall_exists_mem_relations`

 One family of split primes gives relations at all split primes. Let `p` be a natural number
that can be avoided. There are a level `q`, a finite family `s` of split primes with Frobenius
elements `s.φ i` and tame generators `γ i`, and a finite set `T ⊇ S` of primes not dividing `p`,
such that every linear form `ν` that kills the values at the `γ i` of the cocycles in
`Z(range s.v)` consists of the values of a relation off `T` at the `s.φ i`. Moreover the primes of
`S` divide `q`, and an `m`-th root of a `q`-unit of the field of `U` that all `s.φ i` fix is fixed
by `U`. The set `I` is the union of the inertia groups above the primes that are prime to `q` and
not in the family. The proof rests on Artin's reciprocity law for Kummer characters of units, in
place of the reciprocity law for local pairings. 

### `exists_card_cocycles_le`

 A case of the formula of Greenberg and Wiles (Darmon–Diamond–Taylor, Theorem 2.19), giving only
a lower bound. Let `K` be totally complex, `M` finite and killed by `ℓ ^ r` with `r ≠ 0`, and let
`σ` fix the `ℓ`-power roots of unity, be central modulo `U` and fix no nonzero element of `M`. If
`p` can be avoided, there is a finite set `T ⊇ S` of primes not dividing `p` with `#Z(∅) · #M ^
(#S + r₂) ≤ #(relations off T) · #M · ∏_{v ∈ S} #A_v`, where `A_v` (`localCocycles v`) is the group
of allowed local cocycles at `v` and `r₂` is the number of infinite places. The factor `#M` comes
from the `#M` coboundaries, which are the dual cocycles vanishing on `U`. 
