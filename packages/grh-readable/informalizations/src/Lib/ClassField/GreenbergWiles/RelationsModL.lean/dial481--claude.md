---
{
  "module": "src/Lib/ClassField/GreenbergWiles/RelationsModL.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/GreenbergWiles/RelationsModL.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/GreenbergWiles/RelationsModL.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Relations modulo ℓ

A lower bound for the number of reductions modulo `ℓ` of the relations off a finite set `T` of
primes, for a module whose submodule of points killed by `ℓ` has order `ℓ`. Here the forms on the
points killed by `ℓ` are lifted to relations, and the cocycles killed by `ℓ` are bounded by the
count for `M[ℓ]`.

* `New.RelationSetting.reductions`: the reductions modulo `ℓ` of the relations off `T`.
* `New.RelationSetting.exists_pow_le_card_reductions`: the lower bound for their number.

Notions from other files:
* `New.RelationSetting`: a module `M` over `Gal(Ω/K)`, where `Ω` is the fixed algebraic closure in
  which the number field `K` is embedded (`EmbeddedNumberField K`), unramified outside a finite set
  `S` of primes and with trivial complex conjugations, with a chosen place `D.place v` above each
  prime `v`, with local conditions at `S` on its decomposition group that contain the coboundaries,
  and an open normal subgroup `U` that fixes `M` and the `m`-th roots of unity;
* `New.RelationSetting.cocycles`: the cocycles that satisfy the local conditions, vanish at complex
  conjugations and are unramified outside `S` and a given set of primes;
* `New.RelationSetting.relations`: the functions, supported on `U`, with values in the characters of
  `M`, that have the properties of restrictions of dual cocycles; those off `T` satisfy the
  reciprocity law with the cocycles ramified at finitely many split primes outside `T`;
* `New.IsLargeLevel.SplitPlaces`: a family of primes prime to the level that split in the field of
  an open normal subgroup, with places above them and Frobenius elements.

## Relation to the literature

Known; see `Lib.ClassField.GreenbergWiles.CocycleCounts` for sources.


### `card_torsionBy_le_of_surjective`

 The image of a finite abelian group has no more points killed by `ℓ` than the group. 

### `reductions`

 The reductions modulo `ℓ` of the relations off `T`, with values in `M* / ℓ M*`. 

### `finite_reductions`

 If `M` is finite, then `D.reductions ℓ T` is finite, as the image of the finite set
`D.relations T`. 

### `apply_eq_of_mkQ_eq`

 Two characters of `M` that are congruent modulo `ℓ` agree on the points killed by `ℓ`. 

### `pow_le_card_reductions_mul`

 In the relation setting `D` with `M` finite, let `P` be a finite set of finite places, and let
`γ` and `φ` be families of Galois elements indexed by `ι`. Let `D.cocycles P` be the cocycles
allowed at `S`, vanishing at complex conjugations and unramified outside `S ∪ P`. Suppose every
family `ν` of characters of `M` that kills the families `i ↦ z (γ i)` for all `z` in `D.cocycles P`
is the family of values at the `φ i` of a relation off `T` (an element of `D.relations T`). Then
`#M[ℓ] ^ #ι` is at most the number of reductions modulo `ℓ` of the relations off `T` (with values in
`M* / ℓ M*`), times the number of cocycles in `D.cocycles P` killed by `ℓ`. 

### `exists_add_two_primes`

 Let `ℓ` divide `m` and let `O ⊇ U` fix the `ℓ`-th roots of unity. A family `s` of primes not
dividing `N` and split for `U` and `m` extends by two new primes to such a family for `O` and `ℓ`,
whose new Frobenius elements lie in the cosets `(x j)⁻¹ U` of two given elements `x j` of `O`. The
sets `I` and `I'` are the unions of the inertia groups above the other primes not dividing `N`. 

### `le_stabilizer`

 Descent of root detection from `m` to a divisor `ℓ`. Let `U ≤ O` and let the Frobenius elements
of `s` detect `m`-th roots: whatever they fix among the `m`-th roots of `N`-units of the field of
`U` is fixed by `U`. Then `U` also fixes every `ℓ`-th root `y` of an `N`-unit of the field of `O`
that they all fix. 

### `DiscreteModule.torsion`

 The submodule `M[ℓ]` of the points killed by `ℓ`. 

### `torsionAction`

 The action of the Galois group on `M[ℓ]` and on the `ℓ`-th roots of unity. 

### `cyclotomicCharMod_eq_one_of_mem_ker_torsionAction`

 An element of the kernel of the action on `M[ℓ]` and `μ_ℓ` fixes the `ℓ`-th roots of unity. 

### `trivialOn_ker_torsionAction`

 The kernel of the action on `M[ℓ]` and `μ_ℓ` acts trivially on `M[ℓ]`. 

### `le_ker_torsionAction`

 If `ℓ ∣ m`, the subgroup `U` of the setting acts trivially on `M[ℓ]` and on the `ℓ`-th roots of
unity. 

### `coprime_index_ker_torsionAction`

 If `M[ℓ]` has order `ℓ`, the kernel of the action on `M[ℓ]` and `μ_ℓ` has index prime to `ℓ`:
the index divides `(ℓ - 1) ^ 2`. 

### `allowedTorsion`

 The local condition for `M[ℓ]`: the functions on the decomposition group of the chosen place
`D.place v` above `v`, with values in `M[ℓ]`, that are allowed for `M`. 

### `card_torsionBy_cocycles_le`

 Let `P ⊆ P'` with `P'` finite. A cocycle in `D.cocycles P` killed by `ℓ` takes its values in
`M[ℓ]`, so there are at most as many of them as Selmer cocycles (`selmerZ1`) of `M[ℓ]` for `P'`:
cocycles in the local conditions at `S`, zero at complex conjugations and unramified outside
`S ∪ P'`. 

### `exists_generator_mod_ker`

 Let `κ` be continuous with values in `1 + 4 ℤ_ℓ`, so that the image of a closed subgroup `H` is
procyclic. Some `γ ∈ H` and `H ⊓ ker κ` generate `H` topologically: every open subgroup of `H` that
contains both is all of `H`. 

### `card_allowedTorsion_le`

 Let `κ` be continuous with values in `1 + 4 ℤ_ℓ`. Suppose the local condition at each prime `v`
consists of the functions that vanish on the whole decomposition group if `v` is not above `ℓ`, and
on its intersection with `ker κ` if `v` is above `ℓ`. Then there is at most one allowed local
cocycle with values in `M[ℓ]` if `v` is not above `ℓ`, and at most `#M[ℓ]` if it is, as a cocycle
that vanishes on the kernel of `κ` is determined by one value. 

### `exists_hasFewCocycles_torsion`

 Let `κ` be continuous with values in `1 + 4 ℤ_ℓ`, let `ℓ ∣ m`, let `M[ℓ]` have order `ℓ`, and
let `ker κ` lie in `U ∪ U c⁻¹`. Adding two split primes to a family `s` whose Frobenius elements
detect roots gives a family `s'` of split primes for some open normal subgroup `O`. The primes of
`s` are among those of `s'`, and `M[ℓ]` has few cocycles for `s'`: at most `ℓ ^ (#ι + 3)`
cocycles trivialised above the level and infinity and on the inertia groups of the other primes.
That the Frobenius elements detect roots means that `U` fixes every `m`-th root of a `q`-unit of
its field that they all fix. 

### `card_torsionBy_cocycles_mul_pow_le`

 Let `κ` be continuous with values in `1 + 4 ℤ_ℓ` and kernel in `U ∪ U c⁻¹`, let `ℓ ∣ m`, let
`M[ℓ]` have order `ℓ`, let the local conditions be zero away from `ℓ` and vanishing on `ker κ`
above `ℓ`, and let `K` have at least four infinite places. Then the cocycles unramified outside `S`
and the split primes have few points killed by `ℓ`, if the primes of `S` divide the level `q` and
the Frobenius elements of the split primes detect the roots of `q`-units: the number of these
points times `ℓ ^ (k + 1)` is at most `ℓ ^ #ι`, where `k` counts the primes of `S` that are not
above `ℓ`. Indeed the bound `ℓ ^ (#ι + 3)` of `exists_hasFewCocycles_torsion` loses one factor `ℓ`
for each of four infinite places and for each of these `k` primes. 

### `exists_pow_le_card_reductions`

 Relations modulo `ℓ`. Let `ℓ ∣ m`, and let `M[ℓ]` have order `ℓ`. Let `κ` be a continuous
character with values in `1 + 4 ℤ_ℓ` (so its image is procyclic) whose kernel lies in `U ∪ U c⁻¹`.
Let the local condition be zero at the primes not above `ℓ` and vanishing on `ker κ` above `ℓ`. If
`K` has at least four infinite places, then for some `T ⊇ S` the reductions modulo `ℓ` of the
relations off `T` form a group of order at least `ℓ ^ (k + 1)`, where `k` counts the primes of `S`
not above `ℓ`. A relation off `T` is a continuous equivariant map from `U` to `M* = Hom(M, ℚ/ℤ)`,
unramified outside `T`, whose Frobenius values give linear relations among cocycle values at tame
generators. This is weaker than the count given by the formula of Greenberg and Wiles, which grows
with the number of infinite places; here only four of these places are used. 
