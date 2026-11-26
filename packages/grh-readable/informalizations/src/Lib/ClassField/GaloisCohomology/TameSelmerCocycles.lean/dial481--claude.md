---
{
  "module": "src/Lib/ClassField/GaloisCohomology/TameSelmerCocycles.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/GaloisCohomology/TameSelmerCocycles.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/GaloisCohomology/TameSelmerCocycles.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Selmer groups unramified outside a set and cocycles of tamely ramified actions

The file concerns locally constant cocycles of `Gal(Ω/E)`, where `Ω` is the fixed algebraic closure
of `ℚ` and the number field `E` is embedded in it (`EmbeddedNumberField E`), with values in `B ^ n`
for a matrix action `ρ`. It describes membership in the Selmer modules `New.selmerModule ρ S L B`
and how they depend on `S` and `L`. It then studies such cocycles at a place where `ρ` is tamely
ramified, for `B` killed by `ℓ ^ M` with `ℓ ^ M` prime to the place.

## Main definitions and results

* `New.Selmer.mem_selmerModule_iff`: membership spelled out as the cocycle identity, vanishing on
  inertia outside `S`, the relations `L` and local constancy.
* `New.Selmer.mem_selmerModule_of_eq_zero_on_inertiaAbove`: a member for `(S, L)` is a member for
  `(T, K)` when `K ⊆ L` and it vanishes on inertia at the places of `S` outside `T`. The case
  `S ⊆ T` is `New.Selmer.mem_selmerModule_of_subset`.
* `New.Selmer.cocycle_eq_zero_on_inertia_of_tameGenerator`: a cocycle that vanishes at the tame
  generator vanishes on inertia.
* `New.Selmer.length_localCocycles_le`: a bound for the length of the local cocycles
  `New.Selmer.localCocycles`.
* `New.Selmer.exists_conj_side_detects`: at a place prime to `ℓ` or at its complex conjugate, where
  `ρ` is unramified, vanishing at two elements detects vanishing on the decomposition group.

Notions from other files:
* `New.IsPlaceOver A P`: the place `A` of `Ω` lies above the place `P` of the number field.
* `New.IsPlaceOver.tameGenerator`: a chosen generator of tame inertia at `A`.
* `New.IsFrob A q φ`: `φ` fixes `A` and acts as `x ↦ x ^ q` on its residue field; `P.q` is the order
  of the residue field of `P`.
* `New.idOrConjInv b g`: `g` if `b` is true, `(conjGal g)⁻¹` otherwise, where `conjGal g` is the
  conjugate of `g` by a chosen complex conjugation.

## Relation to the literature

Known; see `Lib.ClassField.GreenbergWiles.CocycleCounts`,
`Lib.ClassField.GaloisCohomology.KummerCyclicClasses`,
`Lib.ClassField.LocalDuality.CrystallineDuality` and `Lib.ClassField.Places.LocalFields` for
sources.



## Membership and monotonicity of Selmer modules

`New.selmerModule ρ S L B` is the module of locally constant cocycles `Gal(Ω/E) → B ^ n` for the
map `ρ` to matrices. They vanish on the inertia groups outside `S` (`New.inertiaAbove`) and obey
the linear relations `L`: the function `c` is in `New.obeying L B` if it annihilates each formal
combination of group elements with matrix coefficients in `L`.


### `mem_selmerModule_iff`

 A function `c : Gal(Ω/E) → B ^ n` lies in the Selmer module exactly when four conditions hold.
It satisfies the cocycle identity `c(gh) = c(g) + ρ(g)c(h)`. It vanishes on the inertia groups above
the places outside `S`. It obeys the relations `L` and is locally constant. 

### `mem_selmerModule_of_eq_zero_on_inertiaAbove`

 Let `c` lie in the Selmer module for the places `S` and the relations `L`. If `K ⊆ L` and `c`
vanishes on the inertia groups above every place of `S` outside `T`, then `c` lies in the Selmer
module for `T` and `K`. 

### `mem_selmerModule_of_subset`

 The Selmer module grows when more places may ramify and fewer relations are imposed: a member
for the places `S` and the relations `L` is a member for `T ⊇ S` and `K ⊆ L`. 


## Cocycles of tamely ramified actions

Locally constant cocycles `c` of `Gal(Ω/E)` for a matrix representation `ρ`, with values in `n → B`,
`B` killed by `ℓ ^ M`, at a place `A` of `Ω` where `ρ` is tamely ramified. The idea is to apply the
structure of tame inertia (`New.IsPlaceOver.tame_inertia`) to the affine action
`New.Selmer.affineAction`, `v ↦ c g + ρ g • v`.


### `localCocycles`

 The module of restrictions to the decomposition group at `A` of the locally constant cocycles
for `ρ` with values in `B ^ n` that obey the relations `L`. 

### `affineAction`

 The affine action `u ↦ c g + ρ g • u` of `Gal(Ω/E)` on `B ^ n` given by a cocycle `c` for the
matrix representation `ρ`. 

### `affineAction_apply_eq`

 The affine action of a cocycle `c` sends `u` to `c g + ρ g • u`. 

### `cocycle_eq_zero_on_inertia_of_tameGenerator`

 A cocycle that vanishes at the tame generator vanishes on inertia. In detail: let `A` be a place
of `Ω` over `P` and let `c` be a locally constant cocycle for the representation `ρ` with values in
`B ^ n`, where `ℓ ^ M` kills `B`. Assume that `ρ` is trivial on inertia at `A` near `1` and on the
`m`-th powers of inertia, and that `m * ℓ ^ M` is prime to `A`. If `c` is zero at the tame generator
of `A`, it is zero at every inertia element `γ`. 

### `eq_zero_on_decompGroup`

 A locally constant cocycle `c` for `ρ` that vanishes on the inertia group of a place `A'` over
`v` and at a Frobenius element there vanishes on the decomposition group of `A'`. 

### `length_localCocycles_le`

 An upper bound on length, of the kind given by the local Euler characteristic formula and local
duality. Let `A` be a place of `Ω` over `P`, let `ℓ ^ M` kill `B`, let `ρ` be trivial on inertia at
`A` near `1` and on the `m`-th powers of inertia, and let `m * ℓ ^ M` be prime to `A`. For inertial
`γ`, the module `localCocycles ρ L A B` of restrictions to the decomposition group at `A` of the
cocycles obeying the relations `L` has length at most the length of `B ^ n` plus the length of the
kernel of `ρ γ - 1` on `B ^ n`. 

### `eq_zero_on_inertiaAbove`

 Let `A'` be a place of `Ω` over `v`, and let `ρ` be trivial on the inertia groups above `v`.
A cocycle `c` for `ρ` that vanishes on the inertia group of `A'` vanishes on every inertia group
above `v`. 

### `eq_zero_on_inertiaGroup_of_tameGenerator`

 Let `A` be a place of `Ω` over `P`, prime to `ℓ`, let `ℓ ^ M` kill `B`, let `θ` be an
endomorphism of `Gal(Ω/E)` and let `ρ ∘ θ` be trivial on inertia at `A`. A locally constant cocycle
for `ρ ∘ θ` that vanishes at the tame generator vanishes on inertia at `A`. 

### `exists_conj_side_detects`

 Let `P` be a place of the CM field `E` prime to `ℓ`, let `A` be a place of `Ω` over `P` and let
`ℓ ^ M` kill `B`. Let `v` be `P` or its complex conjugate, and let `ρ` be unramified at `v`. For a
side `b`, write `idOrConjInv b g` for `g` or `(conjGal g)⁻¹` according to `b`, where `conjGal g` is
the conjugate of `g` by complex conjugation. Then vanishing at two elements detects vanishing at
`v`. Precisely, there are a side `b` and a place `A'` over `v` such that every cocycle `c` in
`selmerModule ρ S L B` that is zero at `idOrConjInv b` of the tame generator at `A` is unramified at
`v`. If it is also zero at `idOrConjInv b φ` for a Frobenius element `φ` at `A`, it is zero on the
decomposition group at `A'`. Here `selmerModule ρ S L B` consists of the locally constant cocycles
for `ρ` in `B ^ n` that are zero on inertia above places outside `S` and obey the relations `L`. 
