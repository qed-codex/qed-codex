---
{
  "module": "src/Lib/ClassField/Global/ExistenceTheorem.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/Global/ExistenceTheorem.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/Global/ExistenceTheorem.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Kummer characters, power indices and the existence theorem for totally complex fields

This file proves the existence theorem of class field theory for a totally complex number field `K`:
a continuous homomorphism from the finite ideles of `K` to a `T₁` group that is trivial on `Kˣ`
factors through the Artin map. The proof uses Kummer theory when `K` contains the `n`-th roots of
unity; otherwise it passes to a cyclic extension of `K` inside `K(μ_n)` and composes with the norm.

`Γ` is the Galois group of `Ω/K`, where `Ω` is the fixed algebraic closure of `ℚ`.
`New.idelesPowAt S n` is the group of finite ideles that are `n`-th powers at the places of `S`.

* `New.exists_comp_artinMap`: the existence theorem.
* `New.exists_kummer_chars`: Kummer characters, and the ideles killed by those of the `S`-units.
* `New.index_pow_local_le`, `New.index_idelesPowAt_ne_zero_and_le`: bounds on the index of local
  `n`-th powers.
* `New.QZChar.eq_zero_of_unramified_off`, `New.sum_ord_smul_frob_eq_zero`: consequences of the
  product formula for `New.artinMap`.
* `New.OddPart.exists_detecting_points_hom`: finitely many points of `Γ` that detect the characters
  killed by `m` and unramified off `S`.

Notions from other files:
* `New.artinMap`: the global Artin map from the finite ideles of `K` to the topological
  abelianisation of `Γ`.
* `New.QZChar.abelianLift`: the homomorphism that a character χ of Γ induces on Γ^ab, with values in
  ℚ/ℤ written multiplicatively.
* `New.idelesUnitOff S`: the finite ideles whose components at the finite places outside `S` are
  units.
* `New.cyclotomicCharMod`: the cyclotomic character Γ → (ℤ/n)^×; it is trivial iff Γ fixes μ_n.

## Relation to the literature

Known; see `Lib.ClassField.Global.AlbertBrauerHasseNoether` for sources.


### `adeleNorm_adeleNorm`

 The norm maps of finite adeles compose along a tower `K ⊆ L ⊆ M`: the norm from `M` to `L`
followed by the norm from `L` to `K` is the norm from `M` to `K`. 

### `idelesPowAt`

 For a set `S` of finite places of `K`, the group of finite ideles of `K` whose components at
all places of `S` are `n`-th powers. 

### `val_ideleAt_principalIdele`

 The component at `v` of the principal idele of `x ∈ Kˣ` is the image of `x` in `K_v`. 

### `cokerKerIndex_natCast_eq_index_range_powMonoidHom_div`

 As a rational number, the index `New.cokerKerIndex` of multiplication by `n` on `Additive Y` is
`[Y : Y ^ n] / #Y[n]`. 

### `index_range_pow_eq`

 Let `Y` be a commutative group and let `q = #(Y / Y ^ n) / #Y[n]` be the index
(`New.cokerKerIndex`) of multiplication by `n` on `Y` written additively. If `q ≠ 0` and `q = t`,
then the `n`-th powers have finite index `t * #Y[n]` in `Y`. 

 ### Indices of local powers 

### `index_pow_local_le`

 Let `n ≠ 0` and let `v` be a finite place of `K`, with completion `LocField v`. The `n`-th
powers have finite index in `(LocField v)ˣ`, at most `n ^ 2` times the absolute norm of `v ^ a`,
where `a` is the multiplicity of `v` in the ideal `(n)`; that is, at most `n ^ 2 / |n|_v`. 

### `index_idelesPowAt_ne_zero_and_le`

 For `n ≠ 0` and a finite set `S` of finite places of `K`, the ideles that are `n`-th powers at
the places of `S` have finite index, at most `n ^ (2 |S| + [K : ℚ])`. 

 ### Characters with prescribed local behaviour 

### `QZChar.sup_le_ker_abelianLift_artinMap`

 Let `Γ` be the Galois group of `Ω/K`, where `Ω` is the fixed algebraic closure of `ℚ`, let `n`
be any natural number (zero is allowed) and let `S` be a set of finite places of `K`. For a finite
place `w`, `placeOver w` is the chosen place of `Ω` over `w`. Let the character `χ` of `Γ` vanish on
the complex conjugations and on the inertia groups at `placeOver w` for `w ∉ S`, and let `n • χ`
vanish on the decomposition groups at `placeOver w` for `w ∈ S`. Then `χ` composed with the Artin
map (through `abelianLift`) kills the principal ideles and the ideles that are `n`-th powers at `S`
and units off `S`. 

### `QZChar.eq_zero_of_unramified_off`

 Let `S` be a set of finite places of `K` such that `Kˣ` and the ideles that are units outside
`S` generate the finite ideles. Let `z` be a continuous 1-cocycle of `Γ` with values in a discrete
abelian group `V` with trivial action, that is, a continuous homomorphism. If `z` vanishes on the
complex conjugations, on the decomposition groups at `placeOver w` for `w ∈ S` and on the inertia
groups at `placeOver w` for `w ∉ S`, then `z` is zero. 

### `sum_ord_smul_frob_eq_zero`

 Artin's law for the symbol `(χ, x)`, read on valuations. Let `χ` be killed by `n` and kill the
Artin symbol of `x ∈ Kˣ`; let the `w j` be distinct, and `s j` a Frobenius at a place `A j` over
`w j` where `χ` is unramified. If at every other finite place `v` either (a) the local symbol of `x`
is trivial, or (b) `x / r ^ n` is a unit at `placeOver v` for some `r ∈ Ωˣ` fixed by inertia there
and `χ` is unramified at `v`, then `∑ j, ord_{w j} x • χ (s j) = 0`, where
`ord_w x = -log (w.valuation K x)`. 

### `IsPlaceOver.smul_root_eq_of_local_pow`

 Let `x ∈ Kˣ` be an `n`-th power in `K_v`. An element of the decomposition group at a place above
`v` that fixes the `n`-th roots of unity fixes every `n`-th root of `x`. 

### `index_sup_idelesPowAt_le`

 Let `K` be totally complex and let `S` be a finite set of places such that `Kˣ` and the ideles
that are units outside `S` generate the finite ideles. Let `E` be the group of `S`-units. Suppose
that every element of `E` that is an `n`-th power at each place of `S` lies in `E ^ n`, and that
`n` divides the number of `n`-th roots of unity in `E`. Then the subgroup generated by `Kˣ` and the
ideles that are `n`-th powers at `S` and units elsewhere has finite index, at most `[E : E ^ n]`. 

### `rootPowHom_injective`

 The map `a ↦ ζ ^ a` from `ℤ/n` to `Ωˣ` of `New.rootPowHom`, for the primitive `n`-th root of
unity `ζ` chosen there, is injective. 

### `exists_kummer_hom`

 Let `Γ` be the Galois group of `Ω/K`, where `Ω` is the fixed algebraic closure of `ℚ`, and let
`Γ` fix the `n`-th roots of unity. Let `ζ` be the root of unity of order `n` chosen in
`New.rootPowHom`. There is an additive map `κ` from the invariants of `Ωˣ` to the characters
`Γ → ℤ/n` such that `ζ ^ κ x g = g a / a` whenever `a ^ n = x` (written additively in
`New.DiscreteUnits Ω`). 

### `kummerChar`

 The Kummer map, when `Γ` fixes the `n`-th roots of unity. It sends an invariant `x` of `Ωˣ` to
the character `κ x : Γ → ℤ/n` with `ζ ^ κ x g = g a / a` for every `a` with `a ^ n = x`, where `ζ`
is the root of unity of order `n` chosen in `New.rootPowHom` (`New.rootPowHom_kummerChar`). 

### `rootPowHom_kummerChar`

 The defining property of the Kummer character `κ = kummerChar K h_fix`: if `a ^ n = x`, then
`ζ ^ κ x g = g a / a`, where `ζ` is the root of unity of order `n` chosen in `New.rootPowHom`
(written additively in `New.DiscreteUnits Ω`). 

### `kummerChar_apply_eq_zero_iff`

 The Kummer character of `x` vanishes at `g` exactly when `g` fixes an `n`-th root of `x`. 

### `QZChar.mem_ker_iff_val_eq_zero`

 A point lies in the kernel of a continuous character `χ` with values in `ℚ/ℤ` exactly when `χ`
vanishes there. 

### `val_pow_eq_algebraMap_of_nsmul_eq_ofBase`

 Let `x ∈ Kˣ` and let `r` be an `n`-th root of `x` in `Ωˣ` (both written additively). Then
`r ^ n = x` in `Ω`. 

### `kummerChar_ofBase_apply_eq_zero_of_mem_inertiaGroup`

 Let `Γ` fix the `n`-th roots of unity, and let `v` be a finite place of `K` at which `n` is a
unit. If `x ∈ Kˣ` is a unit at `v`, its Kummer character vanishes on the inertia group at the
chosen place `placeOver v` of `Ω` over `v`: inertia fixes an `n`-th root of `x`. 

### `exists_unit_pow_eq_of_nsmul_eq_ofBase`

 Let `S` be a set of finite places of `K` and `u` an `S`-unit (an element of `Kˣ` that is a unit
at each place outside `S`). A `Γ`-invariant `n`-th root `y` of `u` in `Ωˣ` (both written
additively) comes from an `S`-unit `x` with `x ^ n = u`. 

### `dvd_natCard_ker_powMonoidHom_of_cyclotomicCharMod_eq_one`

 Let `Γ`, the Galois group of `Ω/K` for the fixed algebraic closure `Ω` of `ℚ`, fix the `n`-th
roots of unity, and let `S` be a set of finite places of `K`. Then `n` divides the number of `n`-th
roots of unity among the `S`-units. 

### `mem_range_powMonoidHom_of_kummerChar_eq_zero`

 Let `Γ`, the Galois group of `Ω/K` for the algebraic closure `Ω` of `ℚ`, fix the `n`-th roots of
unity and let `S` be a set of finite places of `K`. An `S`-unit `u` whose Kummer character vanishes
is the `n`-th power of an `S`-unit: `Γ` fixes an `n`-th root of `u`, which therefore lies in `K`. 

### `subgroupOf_comap_idelesPowAt_le_range_powMonoidHom`

 Let `K` be totally complex and let `Γ`, the Galois group of `Ω/K` for the algebraic closure `Ω`
of `ℚ`, fix the `n`-th roots of unity. Let `S` be a set of finite places of `K` that contains the
places above `n`, such that `Kˣ` and the ideles that are units outside `S` generate the finite
ideles. An `S`-unit that is an `n`-th power at each place of `S` is the `n`-th power of an
`S`-unit. 

### `mem_sup_of_kummerChar_artinMap_eq_one`

 Let `K` be totally complex, and let `Γ`, the Galois group of `Ω/K` for the algebraic closure `Ω`
of `ℚ`, fix the `n`-th roots of unity, so that the Kummer map `κ = kummerChar K h_fix` is defined.
Let `S` be a finite set of finite places of `K` that contains the places above `n`, such that `Kˣ`
and the ideles that are units outside `S` generate the finite ideles. Let `a` be a finite idele
whose Artin symbol is killed by `κ u` for every `S`-unit `u` (an element of `Kˣ` that is a unit at
each place outside `S`); here `κ u` is `κ (ofBase Γ Ω u)`, a map `Γ → ℤ/n`, read in `ℚ/ℤ` and lifted
to `Γ^ab`. Then `a` is a principal idele times an idele that is an `n`-th power at each place of `S`
and a unit elsewhere. 

 ### Kummer theory and the existence theorem 

### `exists_kummer_chars`

 Let `Γ`, the Galois group of `Ω/K`, fix the `n`-th roots of unity, and let `ζ` be the root of
unity of order `n` chosen in `New.rootPowHom`. There is an additive map `κ` from the `Γ`-invariant
units of `Ω` to the characters `Γ → ℤ/n` such that (a) `ζ ^ κ x g = g a / a` whenever `a ^ n = x`,
and (b) for `K` totally complex and `S` a finite set of finite places such that `Kˣ` and the ideles
that are units outside `S` generate the finite ideles and that contains the places above `n` (the
three unnamed hypotheses, in this order), an idele whose Artin symbol is killed by `κ u` (short for
`κ (ofBase Γ Ω u)`) for every `S`-unit `u` is a principal idele times an idele that is an `n`-th
power at each place of `S` and a unit elsewhere. The map is `New.kummerChar`. 

### `QZChar.apply_eq_zero_of_artinMap_eq_one`

 Let `K` be totally complex, and let `Γ`, the Galois group of `Ω/K` for the algebraic closure `Ω`
of `ℚ`, fix the `n`-th roots of unity. Let `ψ` be a continuous character of the finite ideles with
values in `ℚ/ℤ` that vanishes on `Kˣ` and is killed by `n` (`toHom ψ` is `ψ` written
multiplicatively). Then `ψ` vanishes on the kernel of the Artin map. 

### `exists_comp_artinMap_of_ker_le`

 Let `Γ` be the Galois group of `Ω/K`, and let `θ` be a continuous homomorphism from the finite
ideles of `K` to a group `C` with a topology whose kernel contains the kernel of the Artin map
`artinMap Γ`, which takes values in the abelianisation `Γ^ab`. Then there is a continuous
homomorphism `μ : Γ → C` with `μ g = θ x` whenever the class of `g` in `Γ^ab` is the Artin symbol of
`x`. 

### `QZChar.commutator_le_commutator_ker`

 Let `χ` be a continuous character of the group `G` with a topology with values in `ℚ/ℤ`, such
that `G ⧸ ker χ` is finite. Then the commutator subgroup of `G` lies in `⁅G, ker χ⁆`. 

### `QZChar.topologicalClosure_commutator_le_map_ker`

 Let `χ` be a continuous character of `Γ` with values in `ℚ/ℤ` such that `Γ ⧸ ker χ` is finite,
and let `μ` be a continuous homomorphism from `ker χ` to `ℚ/ℤ` (written multiplicatively) that is
invariant under conjugation by `Γ`. Then the closure of the commutator subgroup of `Γ` lies in the
kernel of `μ`, viewed as a subgroup of `Γ`. 

### `map_conjNormal_eq_of_forall_artinMap_eq`

 Let `Γ` be the Galois group of `Ω/K` for the algebraic closure `Ω` of `ℚ`. Let `χ` be a
continuous character of `Γ` with values in `ℚ/ℤ` such that `Γ ⧸ ker χ` is finite, let `L` be the
fixed field of `ker χ`, and let `ψ` be a continuous character of the finite ideles of `K`. A
homomorphism `μ` on `ker χ` with `μ k = ψ (N z)` whenever the class of `k` is the Artin symbol over
`L` of `z`, where `N` is the norm from `L` to `K`, is invariant under conjugation by `Γ`: the norm
does not see the action of `Γ` on `L`. 

### `QZChar.apply_eq_zero_of_pow_eq_one_of_artinMap_eq_one`

 Let `K` be totally complex and `Γ` the Galois group of `Ω/K`, and let `ψ` be a continuous
character of the finite ideles with values in `ℚ/ℤ` that vanishes on `Kˣ` and is killed by `n`.
Then `ψ` vanishes on the kernel of the Artin map. 

### `exists_comp_artinMap`

 The existence theorem for totally complex `K`. Let `Γ` be the Galois group of `Ω/K`. A
continuous homomorphism `θ` from the finite ideles to a group `C` with a `T₁` topology that is
trivial on `Kˣ` factors through the Artin map: there is a continuous homomorphism `μ : Γ → C` with
`μ g = θ x` whenever the class of `g` in `Γ^ab` is the Artin symbol of `x`. 

### `OddPart.IsUnramifiedTorsionHom`

 Let `Γ` be the Galois group of `Ω/K` and `S` a set of finite places of `K`. The map `x : Γ → B`
is a locally constant homomorphism to the additive group `B`, killed by `m`, and zero on the inertia
groups at the places off `S`. 

### `OddPart.IsUnramifiedTorsionHom.isLocallyConstant`

 `x` is locally constant. 

### `OddPart.IsUnramifiedTorsionHom.map_mul`

 `x` is a homomorphism to the additive group `B`. 

### `OddPart.IsUnramifiedTorsionHom.nsmul_eq_zero`

 `m` kills the values of `x`. 

### `OddPart.IsUnramifiedTorsionHom.unramified`

 `x` vanishes on the inertia group at the chosen place `placeOver v` of `Ω` over each finite
  place `v ∉ S`. 

### `index_map_artinMap_dvd_classNumber_mul_index`

 Let `Γ` be the Galois group of `Ω/K` and `S` a set of finite places of `K`. The image under the
Artin map of the group generated by `Kˣ` and the ideles that are `m`-th powers at the places of `S`
and units elsewhere has an index that divides the class number of `K` times the index of the ideles
that are `m`-th powers at `S`. 

### `OddPart.exists_detecting_points_hom`

 Let `K` be totally complex, `Γ` the Galois group of `Ω/K` and `S` a set of finite places of `K`,
and let the group of finite ideles that are `m`-th powers at the places of `S` have finite index.
There are finitely many points `p i ∈ Γ` and integers `n i ≥ 2`, with `∏ n i` dividing the class
number of `K` times this index, such that every locally constant homomorphism `x` on `Γ` that is
killed by `m` and unramified off `S` (`New.OddPart.IsUnramifiedTorsionHom`) has `n i • x (p i) = 0`,
and is zero if it vanishes at all `p i`. 
