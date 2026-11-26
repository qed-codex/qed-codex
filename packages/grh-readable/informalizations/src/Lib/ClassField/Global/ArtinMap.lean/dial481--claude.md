---
{
  "module": "src/Lib/ClassField/Global/ArtinMap.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/Global/ArtinMap.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/Global/ArtinMap.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The global Artin map: product of local symbols, continuity, splitting and norms

Γ is the Galois group of an algebraic closure Ω of a number field K (`New.IsProGalois`), and
`New.QZChar.abelianLift χ` is a continuous character χ : Γ → ℚ/ℤ seen on Γ^ab, written
multiplicatively. `New.artinAt` and `New.artinMap` are the local and global Artin maps with values
in Γ^ab; `New.decompGroup` and `New.inertiaGroup` are the decomposition and inertia groups of a
valuation subring A.

* `New.IsPlaceOver.range_abelianLift_comp_artinAt`,
  `New.IsPlaceOver.artinAt_units_trivial_iff_inertiaGroup_le`: the local symbols at v give the
  values of χ on the decomposition group; those of units vanish iff χ kills inertia.
* `New.IsPlaceOver.q_eq_and_comap_ne_self_of_decompGroup_le`: v splits completely in a Galois
  extension L of K whose group Gal(Ω/L) contains the decomposition group.
* `New.abelianLift_artinMap_eq_finprod`: the global symbol is the product of the local symbols.
* `New.continuous_artinMap`: the global Artin map is continuous.
* `New.artinMap_map_adeleNorm`: the Artin maps of K and of an extension L are compatible with the
  norm.

Notions from other files:
* `New.IsPlaceOver A v`: the valuation subring A of Ω lies over the finite place v of K.
* `New.ideleAt v a` is the component at v of a finite idele a; `New.locIdele v x` is the finite
  idele with component x at v and 1 elsewhere; `New.idelesUnitOff S` is the group of finite ideles
  that are units at every place outside S.

## Relation to the literature

Known; see `Lib.ClassField.Global.AlbertBrauerHasseNoether` for sources.


### `QZChar.toHom_eq_abelianLift`

 The character χ, as a homomorphism on Γ, takes at g the value of `abelianLift χ` at the class
of g. 

### `QZChar.mem_ker_iff_abelianLift_eq_one`

 g lies in the kernel of χ exactly when `abelianLift χ` kills the class of g. 

 ### One place: splitting and the local symbol 

### `ncard_above_mul_relIndex_eq_finrank`

 Let `L / K` be Galois with `U = Gal(Ω/L)`, and let `A` be a place of `Ω` over `v`. The number of
places of `L` over `v` times the index of `U ⊓ D` in the decomposition group `D` of `A` is
`[L : K]`. 

### `q_eq_and_comap_ne_self_of_decompGroup_le`

 Let `L / K` be Galois with `U = Gal(Ω/L)`, and let `A` be a place of `Ω` over `v` whose
decomposition group lies in `U`. Then `v` splits completely: a place `u` of `L` over `v` has the
residue cardinality of `v`, and no nontrivial element of `Gal(L/K)` fixes `u`. 

### `range_abelianLift_comp_artinAt`

 Let `A` be a place of `Ω` over `v`. The values of a character `χ` on the local symbols at `v`
are its values on the decomposition group of `A`. 

### `artinAt_trivial_iff_decompGroup_le`

 Let `A` be a place of `Ω` over `v`. A character `χ` kills all local symbols at `v` exactly when
it is trivial on the decomposition group of `A`. 

### `artinAt_units_trivial_iff_inertiaGroup_le`

 Let `A` be a place of `Ω` over `v`. A character `χ` kills the local symbols of the units of
`K_v` exactly when it is trivial on the inertia group of `A`.

This is one side of the mutual annihilation of unramified classes (Milne, Arithmetic Duality
Theorems, I.2.6), for global characters. 

### `abelianLift_artinAt_of_inertiaGroup_le_ker`

 The local symbol of an unramified character. Let `A` be a place of `Ω` over `v`, let `χ` be
trivial on the inertia group of `A`, and let `φ` be a Frobenius element at `A`. Then `χ` takes the
local symbol at `v` of `x ∈ Kˣ` to `(v.valuation K x).log • χ φ`, that is `-(ord_v x • χ φ)` where
`ord_v x = -(v.valuation K x).log`.
This is a form of the local reciprocity map in the unramified case (Serre, Local Fields).
Uniformisers go to geometric Frobenius, hence the minus sign. 

 ### The global Artin map 

### `QZChar.eventually_artinAt_eq_one`

 Let `χ` be a character of the Galois group `Γ` of `Ω` over the number field `K`. A finite idele
`a` of `K` close enough to `1` is a unit at every place, and `χ` kills all local symbols of `a`. 

### `abelianLift_artinMap_eq_finprod`

 A character `χ` of `Γ` takes the global Artin symbol of a finite idele `a` to the product over
the finite places `v` of its values on the local symbols of the components of `a`. 

### `continuous_artinMap`

 The global Artin map on the finite ideles of `K` is continuous. 

### `artinMap_locIdele`

 The global Artin symbol of the idele with component `x` at `v` and `1` elsewhere is the local
symbol of `x` at `v`. 

### `artinMap_map_adeleNorm`

 Norm compatibility of the Artin map. Let `L / K` be an extension of number fields embedded in
`Ω`, let `Γ` and `Γ'` be their absolute Galois groups (topological groups acting on `Ω`), let `j` be
an endomorphism of `Ω` that extends `K → L`, and let `j` carry the action of `g ∈ Γ` to that of
`g' ∈ Γ'`. If the Artin symbol of the finite idele `y` of `L` is the class of `g'`, then the Artin
symbol of the norm of `y` to `K` is the class of `g`. 
