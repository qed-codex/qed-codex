---
{
  "module": "src/New/Congruences/LocalLoss/TateDualBound.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/LocalLoss/TateDualBound.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/LocalLoss/TateDualBound.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A bound for non-crystalline cocycles modulo `ℓ ^ m` by the Tate dual lattice

This file proves a local estimate at a place above `ℓ`, by Tate duality. The group `Γ` maps to the
absolute Galois group of `ℚ_ℓ` (`OverGp Γ ℓ`), `R` is the integer ring of a finite extension of
`ℚ_ℓ` (`PadicIntegerRing R ℓ`), and `L = R ^ d` is the lattice of a matrix representation of `Γ`
(`matrixLattice`). `QuotSpan a` is the ring `R / a`.

* `New.Selmer.ComesFromClass`: a map with values modulo `ℓ ^ m` is the image of a crystalline
  cocycle of a lattice of a given class.
* `New.Selmer.relLength_le_of_comesFromClass`: if the map of `Γ` to the Galois group is an open
  embedding and `L` lies in the class, a module of maps that come from the class, modulo the
  reductions of the crystalline cocycles of `L`, is at most as long as the crystalline cocycles of
  the Tate dual of `L` modulo those orthogonal to the class.
* `New.Selmer.comesFromClass_of_mem_ribetCocycles`: let `η : Γ →* G`, and let the lattices of all
  `u x ∘ η` lie in the class. Then the restriction along `η` of a cocycle in `ribetCocycles u ρ`
  comes from the class.
* `New.Selmer.relLength_ribetCocycles_le`: if the map of `Γ` to the Galois group is an open
  embedding and the lattices of `ρ ∘ η` and of all `u x ∘ η` lie in the class, the same bound holds
  for `ribetCocycles u ρ` modulo the cocycles whose restriction along `η` obeys the linear
  relations that hold on the crystalline cocycles of the lattice `L` of `ρ ∘ η`.

Notions from other files:
* `New.Lift.InClass F K U`: the class of `Γ`-lattices `Y` over `R` (`GalLattice R Γ`) with three
  properties: the periods of `Y` that are fixed by almost all elements of `Γ` near `1` and along the
  filter `F` on `Γ` span; at each algebra map `ι : R → ℂ_ℓ` the Hodge–Tate jumps of `Y` lie in the
  finite set `U ι`; and on the periods of `Y` the polynomial `Q` over `R`, evaluated at the action
  of an element `s` of `Γ`, is zero whenever `s` is in inertia and `K s Q` holds. Such lattices
  are potentially crystalline.
* `New.Period.crysCocycles`: the module `Z_f(T)` of maps `c : Γ → T` that become coboundaries in
  `Bmax ⊗ T`.
* `New.Lift.cupOrthogonal 𝒬 L`: the maps `c : Γ → L` whose cup product with every crystalline
  cocycle of every `Y` in `𝒬` is a coboundary, for every `k` and every pairing `Y × L → ℤ/ℓᵏ(1)`
  given by a `New.Lift.Pairing`.
* `New.Selmer.ribetCocycles u ρ a`: the cocycles for `ρ` with values modulo `a` that obey the
  linear relations among the families `(u x g - 1)_x`.

The estimate bounds the non-crystalline defect above `ℓ` of the cocycles used in
`New.Congruences.FirstOrder.RibetElement`.

## Relation to the literature

See `New.Congruences.FirstOrder.RibetElement` for related work.


### `New.Selmer.ComesFromClass`

 Let `Γ` be a group with a map to the absolute Galois group of `ℚ_ℓ` with open image
(`OverGp Γ ℓ`), let `R` be the integer ring of a finite extension of `ℚ_ℓ`, and let `Γ` act through
the matrix representation `σ` on vectors over `R / ℓ ^ m`. A map `s` from `Γ` to such vectors comes
from the class of lattices `𝒬` if `s = t ∘ a` for a lattice `Y` in `𝒬`, a `Γ`-equivariant `R`-linear
map `t : Y → (R / ℓ ^ m) ^ d` and a crystalline cocycle `a` of `Y` (a map `Γ → Y` that becomes a
coboundary after tensoring with `Bmax`). 

### `New.Selmer.ker_compLeft_mkQ_eq_pPowMultiples`

 A vector over `R` reduces to `0` modulo `ℓ ^ m` exactly if it lies in `ℓ ^ m R ^ d`. 

### `New.Selmer.exists_crysCocycles_pow_smul_eq_coboundary`

 Let `Y` and `L` be `R`-lattices with an action of `Γ`, and let the `R`-linear map `q : Y → L` be
equivariant modulo `ℓ ^ m L` (`pPowMultiples L m`). Let `ψ` be the form `y ⊗ φ ↦ φ (q y)` on
`Y ⊗ L^∨(1)`. Then the coboundary `g ↦ g ψ - ψ` is `ℓ ^ m` times a crystalline cocycle of the Tate
dual of `Y ⊗ L^∨(1)`. 

### `New.Selmer.relLength_le_of_comesFromClass`

 Let the map `𝒥.toGp` from `Γ` to the absolute Galois group of `ℚ_ℓ` be an open embedding, and
let `R` be the integer ring of a finite extension of `ℚ_ℓ`. Let `InClass F K U` be the class of
potentially crystalline `Γ`-lattices `Y` over `R` such that `Bmax ⊗ Y` is spanned by the periods
fixed near `1` and along the filter `F`, the Hodge–Tate jumps at each `ι : R → ℂ_ℓ` lie in `U ι`,
and `Q(s) = 0` on the periods for `s` in inertia with `K s Q`. Let the lattice `L = R ^ d` of
`σ` lie in the class. Let `N` be a module of maps `Γ → L / ℓ ^ m`, each of the form `t ∘ a` for a
crystalline cocycle `a` of a lattice `Y` of the class and a `Γ`-equivariant `R`-linear map
`t : Y → L / ℓ ^ m` (`ComesFromClass`). Then the length of `N` modulo the reductions of the
crystalline cocycles of `L` is at most the length of the crystalline cocycles of the Tate dual
`L^∨(1)` modulo those whose cup products with the crystalline cocycles of all lattices of the class
are coboundaries (`dualDefect`). Here `relLength S T` is the length of `S / (S ∩ T)`. 

### `New.Selmer.comesFromClass_of_mem_ribetCocycles`

 Let `Γ` be a group with a map to the absolute Galois group of `ℚ_ℓ` with open image
(`OverGp Γ ℓ`), and let `R` be the integer ring of a finite extension of `ℚ_ℓ`. Let `InClass F K U`
be the class of potentially crystalline `Γ`-lattices `Y` over `R` such that `Bmax ⊗ Y` is spanned by
the periods fixed near `1` and along the filter `F`, the Hodge–Tate jumps at each `ι : R → ℂ_ℓ` lie
in `U ι`, and `Q(s) = 0` on the periods for `s` in inertia with `K s Q`. Let `η : Γ →* G`, let `u x`
be matrix representations of `G` of size `n`, and let the lattices `R ^ n` of all `u x ∘ η` lie in
the class. Let `w` be a cocycle of `G` for the matrix representation `ρ`, with values in
`(R / ℓ ^ m) ^ d`, that obeys the linear relations among the families `(u x g - 1)_x`
(`ribetCocycles`). Then `w ∘ η` is the image of a crystalline cocycle of a lattice `Y` of the class
under an `R`-linear map `Y → (R / ℓ ^ m) ^ d` that is equivariant for `ρ ∘ η` (`ComesFromClass`). 

### `New.Selmer.relLength_ribetCocycles_le`

 Let the map `𝒥.toGp` from `Γ` to the absolute Galois group of `ℚ_ℓ` be an open embedding, let
`R` be the integer ring of a finite extension of `ℚ_ℓ`, and let `η : Γ →* G`. Let `u x` (`x : X`)
and `ρ` be matrix representations of `G` over `R` of sizes `n` and `d`. Let the lattices of all
`u x ∘ η` and the lattice `L` of `ρ ∘ η` lie in `InClass F K U`, the class of potentially
crystalline `Γ`-lattices `Y` such that `Bmax ⊗ Y` is spanned by the periods fixed near `1` and along
the filter `F`, the Hodge–Tate jumps at each `ι : R → ℂ_ℓ` lie in `U ι`, and `Q(s) = 0` on the
periods for `s` in inertia with `K s Q`. Take the cocycles of `G` for `ρ` with values modulo `ℓ ^ m`
that obey the linear relations among the families `(u x g - 1)_x` (`ribetCocycles`), modulo those
whose restriction along `η` obeys (`obeying`) all linear relations that hold on the crystalline
cocycles of `L` (`relationsOn`). The length of this quotient is at most that of the crystalline
cocycles of the Tate dual `L^∨(1)` modulo those whose cup products with the crystalline cocycles of
all lattices of the class are coboundaries (`dualDefect`). 
