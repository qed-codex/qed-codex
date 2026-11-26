---
{
  "module": "src/Lib/ClassField/GreenbergWiles/SelmerRelations.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/GreenbergWiles/SelmerRelations.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/GreenbergWiles/SelmerRelations.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Relations at split primes and their number (Greenberg–Wiles)

Relations are families of additive maps `n i` on `M` such that `∑ i, n i (x (γ i)) = 0` for all
Selmer cocycles `x`, with `γ i` elements at auxiliary split primes. They take the place of the dual
Selmer group.

* `New.selmerZ1.card_mul_pow_le`: a bound for trivialised cocycles gives a bound for Selmer
  cocycles.
* `New.selmerZ1.exists_splitPlaces_frob_mem_coset`, `New.selmerZ1.exists_three_values`: split primes
  with Frobenius elements in given cosets, and trivialised cocycles with given values at them.
* `New.selmerZ1.card_relations_ge`: a lower bound for the number of relations.

Notions from other files:
* `New.DiscreteUnits`: The multiplicative group Ω^×, written additively. Here Ω is an algebraic
  closure of ℚ that contains each `EmbeddedNumberField` K, and a `ClosurePlace` is a finite place of
  Ω.
* `New.unitsRep`: the ℤ-linear representation of `G` on Ω^× (written additively) coming from the
  action of `G` on the field Ω by ring automorphisms.
* `New.DiscreteModule`: A discrete Γ-module over R: an R-module with the discrete topology and a
  continuous R-linear action of the topological group Γ.
* `New.IsLargeLevel.fixedSUnits`: The N-units of the fixed field of U: the N-units of Ω that are
  fixed by U.
* `New.IsLargeLevel.SplitPlaces`: Split places for `U`: distinct primes `s.v i` not dividing `N`,
  each with a Frobenius element `s.φ i` in `U`, where `U` fixes the `m`-th roots of unity and
  `m ∣ N`. The set `I` is the union of the inertia groups over the other primes not dividing `N`.
* `New.DiscreteModule.trivialisedCocycles`: pairs of f : X → V and continuous z : G → V vanishing on
  I, with g f(g⁻¹x) = f(x) + z(g) for all g, x. Here X is `New.PlaceAboveLevel q`, the places of Ω
  above q and infinity.

## Relation to the literature

Known; see `Lib.ClassField.GreenbergWiles.CocycleCounts` for sources.


### `exists_trivialisation_of_mem`

 Let `N` lie in every prime of `S`, let `A v` lie over `v`, let complex conjugations act
trivially on `M`, and let `y` be a Selmer cocycle (`selmerZ1`) that may ramify at the split primes
of `s` and is, for each prime `v` dividing `N`, the coboundary of `a v` on the decomposition group
of `A v`. Then `y` vanishes on the set `I` of `s` and is trivialised above `N` and infinity by a map
with the values `a w` at the chosen places over the primes dividing `N` and the infinite places
`w`. 

### `card_mul_pow_le`

 Selmer cocycles against trivialised cocycles. Let the discrete module `M` be unramified outside
`S`, let complex conjugations act trivially on it, let `A v` lie over `v`, and let `L v` contain
the local coboundaries for `v ∈ S`. If `N` lies in every prime of `S` and there are at most `#M ^ k`
cocycles that vanish on `I` and are trivialised above `N` and infinity, then the number of Selmer
cocycles that may ramify at the split primes of `s`, times `#M ^ (#S + #(infinite places of K))`,
is at most `#M ^ k * ∏ v ∈ S, #Z_v`. Here `M` is finite, `Z_v` is the group of the local cocycles in
`L v`, and the Selmer cocycles (`selmerZ1`) are those in `L v` at `v ∈ S` that vanish at complex
conjugations and on inertia outside `S` and the split primes.

It replaces part of the Greenberg–Wiles formula: an upper bound on Selmer cocycles only, with no
dual Selmer group. 

### `_root_.New.natCast_notMem_of_coprime`

 A prime does not divide two coprime integers. 

### `exists_dvd_coprime_sup_idelesUnitOff_eq_top`

 Let `p ≠ 0` be prime to `m` and lie in no prime of `S`, and let the primes dividing `p` be
unramified in the field of `U`. There is a multiple `q ≠ 0` of `m`, prime to `p`, that lies in all
primes of `S` and in all primes ramified in the field of `U`, and such that the primes dividing `q`
generate the class group of every number field between `K` and the field of `U`. 

### `exists_fix_roots_of_units`

 There is an open normal subgroup `O` such that the action of `g` on the `m`-th roots of the
`q`-units of the fixed field of `U` (the `y` with `m • y ∈ fixedSUnits q U`) depends only on the
coset of `g` modulo `O`. 

### `exists_splitPlaces_frob_mem_coset`

 Let `U` fix the `m`-th roots of unity, that is, the cyclotomic character modulo `m` is trivial
on `U`, and let `p ≠ 0` be prime to `m`, lie in no prime of `S`, and have its primes unramified in
the field of `U`. There is a `q ≠ 0`, prime to `p` and in all primes of `S`, such that for every
open normal subgroup `O` there is a family of split places (`SplitPlaces`: primes of `K` not
dividing `q` with Frobenius elements `s.φ` in `U`) indexed by the cosets of `O`, none dividing
`p`, such that the Frobenius element at the coset of `g ∈ U` lies in that coset. 

### `exists_three_values`

 Let `M` be a `ZMod m`-module fixed by `U`, let `U` contain no complex conjugation, and let `s`
be split places for `U` (`SplitPlaces`) with Frobenius elements `s.φ`; `I` is the union of the
inertia groups above the other primes not dividing `q`. Let each `γ i` be a tame inertia generator
at level `m` (`IsTameGeneratorFor m`) at `s.valuationSubring i`, and let `s.φ j * (g * s.φ k * g⁻¹)`
act like `s.φ i` on the `m`-th roots of `fixedSUnits q U` (the `q`-units fixed by `U`). Then some
trivialised cocycle `P` exists, i.e. a continuous cocycle `P.2` vanishing on `I` and a map `P.1` on
places above `q` and infinity with `g • P.1 x = P.1 (g x) + P.2 g`, such that `P.2` has the values
`a`, `-a`, `-χ(g) g⁻¹ a` at `γ i`, `γ j`, `γ k` (added where these indices agree) and `0` at the
other `γ n`; here `χ` is the cyclotomic character modulo `m`. 

### `trivialised_mem_selmer`

 Let `M` be unramified outside `S`, let complex conjugations act trivially on `M`, let `A v` lie
over `v`, and let `L v` contain the local coboundaries for `v ∈ S`. If `q` lies in every prime of
`S`, the part `P.2` of a cocycle `P` trivialised above `q` and infinity and zero on the inertia set
`I` of `s` is a Selmer cocycle (in `L v` at each `v ∈ S`, zero at complex conjugations) that may
ramify at the split primes of `s`. 

### `card_relations_ge`

 Counting relations. Here `s` gives distinct primes `s.v i` of `K` not dividing `q`, each with a
place above it whose Frobenius lies in `U`; `U` fixes the `m`-th roots of unity, `m ∣ q`, and `I` is
the union of inertia groups above the other primes not dividing `q`. Let `M` be unramified outside
`S`, let complex conjugations act trivially on `M`, let `A v` lie over `v`, and let `L v` contain
the local coboundaries for `v ∈ S`. Assume that `q` lies in every prime of `S`, that at most
`#M ^ (#ι + 1)` cocycles zero on `I` are trivialised above `q` and infinity, and that the Selmer
cocycles without extra ramification lie among those that may ramify at the `s.v i` and vanish at all
`γ i`. Then the number of families `n` of maps into `QZ` (ℚ/ℤ) with `∑ i, n i (x (γ i)) = 0` for all
Selmer cocycles `x` that may ramify at the `s.v i`, times `#M` and the orders of the groups of local
cocycles in `L v`, `v ∈ S`, is at least `#M ^ (#S + #(infinite places of K))` times the number of
Selmer cocycles without extra ramification. 
