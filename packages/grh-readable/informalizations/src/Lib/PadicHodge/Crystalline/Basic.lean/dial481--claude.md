---
{
  "module": "src/Lib/PadicHodge/Crystalline/Basic.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/PadicHodge/Crystalline/Basic.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/PadicHodge/Crystalline/Basic.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Crystalline and potentially crystalline representations and admissibility

This file concerns a representation `ρ` of a group `Γ` on an `R`-module `T`. The group `Γ` carries a
homomorphism `j` (the field `toGp` of `New.Period.OverGp`) with open image in the Galois group
`New.Gp p` of `ℚ_[p]`. Tensor products are over `ℤ_[p]` and the period ring is `New.Period.Bmax`;
the class `ThePrime p` makes `p` a prime (it supplies the `Fact p.Prime` needed by `OverGp`).

"Near `1`" means along the filter `New.Period.nearOne`, which takes the place of passing to a finite
extension. Let `B` be a `ℤ_[p]`-algebra with an action of `New.Gp p`. The diagonal action
`New.Period.tensorAction` of `g` on `B ⊗ T` is `j(g) ⊗ ρ(g)`. For a filter `F` on `Γ`,
`New.Period.fixedPeriods ρ B F` is the set of elements of `B ⊗ T` fixed by the diagonal action for
`F`-almost all `g`. `New.Period.IsAdmissible ρ F` says that for `B = Bmax` this set spans `B ⊗ T`
over `B`.

## Main definitions and results

* `New.Period.IsCrystalline`, `New.Period.IsPotentiallyCrystalline`: the vectors of `Bmax ⊗ T` fixed
  by `Γ`, or fixed near `1` (`New.Period.Dpcris`), span `Bmax ⊗ T`.
* `New.Period.crysCocycles`: the functions `Γ → T` that become coboundaries in `Bmax ⊗ T`.
* `New.Period.hodgeTateMaps`, `New.Period.HasJumps`: Hodge–Tate maps `T → ℂ_[p]` of weight `u` along
  `γ : R → ℂ_[p]`, and the multiset of weights counted with the dimensions of these spaces.
* `New.Period.IsWeilPair`, `New.Period.linearFrob`, `New.Period.IsKilledBy`: the action of `φ ^ m s`
  on `Dpcris`, extended linearly, and the polynomials over `R` that annihilate it.
* `New.Period.IsAdmissible.tate_twist`, `New.Period.isAdmissible_of_cyclotomicGp_zpow`: twists by
  powers of the cyclotomic character, through the unit of `New.Period.exists_tate_twist_unit`.
* `New.Period.equivFun_tensorAction`: in the coordinates given by a finite basis `e` of `T`, the
  diagonal action is `New.Period.coordAction`.

Notions from other files:
* `New.Period.Bmax`: the period ring B⁺[1/μ] (Colmez's B_max), used here in place of B_cris.
* `New.Period.FrobGal`: the monoid ℕ × `Gp p`; on the period rings with a Frobenius `φ`, the pair
  `(n, g)` acts as `φ ^ n ∘ g`.

## Relation to the literature

Known; see `Lib.PadicHodge.Crystalline.Regularity`, `Lib.PadicHodge.BlochKato` and
`Lib.PadicHodge.Kisin.PeriodMatrixFrame` for sources.


 ## Crystalline representations, Hodge–Tate weights and linear Frobenius 

### `OverGp`

 A group `Γ` together with a homomorphism `j` from `Γ` to `Gp p` = Gal(Q̄_p/Q_p) whose image
is open. 

### `OverGp.toGp`

 The homomorphism from the group to `New.Gp p`. 

### `OverGp.isOpen_range`

 The image of the homomorphism is open in `New.Gp p`. 

### `GroupOverGp`

 A group `G` bundled with a homomorphism from `G` to `Gp p` = Gal(Q̄_p/Q_p) whose image is
open. 

### `GroupOverGp.G`

 The group. 

### `GroupOverGp.group`

 The group structure on `G`. 

### `GroupOverGp.overGp`

 The homomorphism from `G` to `New.Gp p` with open image. 

### `instance : CoeSort (GroupOverGp p) Type`

 A bundled group over `Gp p` is read as its underlying type. 

 ### Periods and crystalline cocycles 

### `tensorAction`

 For an element `m` of a monoid `M` acting on the `ℤ_p`-algebra `B` and an endomorphism `f` of
`T`, the `ℤ_p`-linear endomorphism `b ⊗ x ↦ (m • b) ⊗ f x` of `B ⊗ T`, the tensor product taken over
`ℤ_p`. 

### `fixedPeriods`

 For a `ℤ_p`-algebra `B` with an action of `Gp p` and a filter `F` on `Γ`, the set of elements of
`B ⊗ T` (over `ℤ_p`) fixed by `j(g) ⊗ ρ(g)` for `F`-almost all `g`, where `j` is `toGp`. 

### `IsAdmissible`

 For a representation `ρ` of `Γ` on `T` and a filter `F` on `Γ`: the elements of `Bmax ⊗ T`
fixed by `j(g) ⊗ ρ(g)` for `F`-almost all `g` span `Bmax ⊗ T` over `Bmax`. 

### `IsCrystalline`

 `ρ` is crystalline: the elements of `Bmax ⊗ T` fixed by `j(g) ⊗ ρ(g)` for all `g` in `Γ` span
`Bmax ⊗ T` over `Bmax`. 

### `crysCocycles`

 The `R`-submodule of functions `c : Γ → T` that become coboundaries in `Bmax ⊗ T`: some `y` in
`Bmax ⊗ T` satisfies `1 ⊗ c g = (j(g) ⊗ ρ(g)) y - y` for all `g` in `Γ`. 

 ### Weil pairs and potentially crystalline representations 

### `IsWeilPair`

 `(s, m)` is a Weil pair: `s` in `Gp p` acts on the residue field of the valuation ring of Q̄_p
as `x ↦ x ^ (1 / p ^ m)`, that is, `s⁻¹` is a Frobenius element for `p ^ m`; `m = 0` means
inertia. 

### `isWeilPair_zero_iff`

 For `s` in `Gp p` = Gal(ℚ̄_p/ℚ_p), `(s, 0)` is a Weil pair (that is, `s` acts trivially on the
residue field of the valuation ring of ℚ̄_p) if and only if `s` lies in the inertia group of that
valuation ring. 

### `χ`

 The p-adic cyclotomic character of `Γ`: the cyclotomic character of `Gp p` composed with `j`. 

### `nearOne`

 The filter 'near 1' on `Γ`: the pull-back along `j : Γ → Gp p` of the filter of
neighbourhoods of the identity. 

### `eventually_nearOne_apply_eq`

 An element of Q̄_p is fixed by `toGp g` for `g` near `1`, as its stabiliser is open. 

### `Dpcris`

 `Dpcris ρ`: the set of elements of `Bmax ⊗ T` fixed by `j(g) ⊗ ρ(g)` for all `g` with `j(g)` in
some neighbourhood of `1` in `Gp p`. 

### `IsPotentiallyCrystalline`

 `ρ` is potentially crystalline: the elements of `Bmax ⊗ T` fixed by `j(g) ⊗ ρ(g)` for all `g`
with `j(g)` near `1` span `Bmax ⊗ T` over `Bmax`. 

### `_root_.New.HasHodgeTateWeight`

 The element `y` of `ℂ_p ⊗ T` (over `ℤ_p`) has Hodge–Tate weight `u`:
`(j(g) ⊗ ρ(g)) y = χ(j(g)) ^ (-u) • y` for all `g` in `Γ`, with `χ` the cyclotomic character. 

### `matrixRep`

 For a homomorphism `r` from `Γ` to `GL n R`, the representation on `n → R` in which `g` acts
by multiplying column vectors by `r g`. 

 ### Hodge–Tate jumps and the linear Frobenius 

### `hodgeTateMaps`

 For `γ : R → ℂ_p` and an integer `u`, the Q̄_p-space of `γ`-semilinear maps `f : T → ℂ_p` with,
for each `x`, `f (ρ g x) = χ(g) ^ (-u) • j(g) • f x` for `g` near `1`, where `χ` is the cyclotomic
character. 

### `jump`

 The multiplicity of the Hodge–Tate jump `u` at `γ`: the dimension over Q̄_p (zero if infinite)
of the space `New.Period.hodgeTateMaps ρ γ u`. 

### `HasJumps`

 The multiset `J` of integers lists the Hodge–Tate jumps of `ρ` at `γ`: for every integer `u`,
the multiplicity `jump ρ γ u` equals the number of times `u` occurs in `J`. 

### `linearFrob`

 A chosen `Bmax`-linear endomorphism of `Bmax ⊗ T` that agrees on `Dpcris ρ` with the map
`φ ^ m s ⊗ ρ s`, where `φ` is Frobenius, if one exists (`linearFrob_eq_tensorAction_of_exists`);
otherwise the value is unspecified. If `ρ` is potentially crystalline, there is at most one such map
(`IsPotentiallyCrystalline.linearFrob_eq`), and there is one when `toGp s` and `m` form a Weil pair
(`linearFrob_apply`).

This operator plays the role of Fontaine's Weil–Deligne representation: it extends the action of a
Weil pair on `Dpcris ρ` linearly to `Bmax ⊗ T`. 

### `linearFrob_eq_tensorAction_of_exists`

 If some `Bmax`-linear map agrees with `φ ^ m s ⊗ ρ s` on `Dpcris ρ`, then so does
`linearFrob ρ s m`. 

### `IsPotentiallyCrystalline.linearFrob_eq`

 For potentially crystalline `ρ`, a `Bmax`-linear map that agrees with `φ ^ m s ⊗ ρ s` on
`Dpcris ρ` is `linearFrob ρ s m`. 

### `coeffEnd`

 The ring homomorphism from `R` to the `Bmax`-linear endomorphisms of `Bmax ⊗ T` (tensor over
`ℤ_p`) sending `a` to `1 ⊗ (multiplication by a on T)`. 

### `IsKilledBy`

 The polynomial `P` over `R` kills `(s, m)`: `ρ` is potentially crystalline and `P`, evaluated
at `linearFrob ρ s m` with the coefficients acting on `T` through `coeffEnd`, is zero on
`Bmax ⊗ T`.

This is the analogue, tested on `Bmax ⊗ T`, of the vanishing of a polynomial at an element acting on
Fontaine's Weil–Deligne representation. 

### `isKilledBy_iff`

 `P` kills `(s, m)` if and only if `ρ` is potentially crystalline and `P`, evaluated at
`linearFrob ρ s m` through `coeffEnd`, is zero. 

### `IsKilledBy.isPotentiallyCrystalline`

 If `P` kills `(s, m)`, then `ρ` is potentially crystalline. 

### `IsKilledBy.eval₂_eq_zero`

 If `P` kills `(s, m)`, then `P` evaluated at `linearFrob ρ s m` through `coeffEnd` is zero. 


## The filter near 1, fixed fields and embeddings of Q̄_p in ℂ_p

* `New.Period.flat_padicInt_of_algebra_padic`: a `ℚ_p`-algebra is flat over `ℤ_p`.
* `New.Period.nearOne_eq_nhds_one`: if `toGp` is an open embedding, the filter near `1` on `Γ` is
  the filter of neighbourhoods of `1`.
* `New.Period.localFieldOf`: the subfield of Q̄_p fixed by the image of `toGp`.


### `flat_padicInt_of_algebra_padic`

 A `ℚ_p`-algebra is flat over `ℤ_p`. 

### `nearOne_eq_nhds_one`

 If `j : Γ → Gp p` is an open embedding for a topology on `Γ`, the filter near `1` on `Γ` is the
filter of neighbourhoods of `1`. 

### `localFieldOf`

 The subfield of ℚ̄_p fixed by the image of `j : Γ → Gp p`. 

### `mem_localFieldOf`

 An element of ℚ̄_p lies in `localFieldOf Γ` if and only if every `j(g)` fixes it. 

### `exists_gp_eq_algHom`

 Every `ℤ_p`-algebra map from `Q̄_p` to `ℂ_p` is an element of the Galois group `Gp p` followed
by the inclusion. 

### `nhds_one_le_map_nearOne`

 The filter of neighbourhoods of `1` in `Gp p` is finer than the image under `j` of the filter
near `1` on `Γ`: a set whose preimage under `j` is near `1` is a neighbourhood of `1`. This uses
that the image of `j` is open. 


## An order instance, and base change of bilinear pairings

The ideals of `O^♭` are linearly ordered, and a `ℤ_p`-bilinear pairing extends to `A ⊗ T`
compatibly with maps `ψ ⊗ f`.


### `noncomputable instance : LinearOrder (Ideal OFlat)`

 The ideals of `OFlat` (the tilt `O^♭`) are linearly ordered. 

### `baseChangePairing`

 The `A`-bilinear map `(A ⊗ T) × (A ⊗ T') → A ⊗ T''` obtained from a `ℤ_p`-bilinear map
`b : T × T' → T''` by extension of scalars. 

### `baseChangePairing_map_of_map_mul`

 Let `ψ : A → A'` be `ℤ_p`-linear and multiplicative (`hψ_mul`), and let the endomorphisms `f`,
`f'`, `f''` of `T`, `T'`, `T''` be compatible with `b`: `b (f t) (f' t') = f'' (b t t')`. Then the
extended pairings satisfy the same identity for the maps `ψ ⊗ f`, `ψ ⊗ f'` and `ψ ⊗ f''`. 

### `baseChangePairing_map`

 `New.Lift.baseChangePairing_map_of_map_mul` in the form in which `simp` proves the
multiplicativity `hψ_mul` of `ψ` by default. 


## Admissibility: equivariant maps, finer filters, pull-back, Tate twists

* `New.Period.periodTensorMap`, `New.Period.tensorAction_periodTensorMap`: the map `b ⊗ x ↦ b ⊗ f x`
  and the diagonal actions.
* `New.Period.fixedPeriods.periodTensorMap_mem`,
  `New.Period.IsAdmissible.periodTensorMap_mem_span_fixedPeriods`: transfer along equivariant maps.
* `New.Period.IsAdmissible.mono`, `New.Period.IsAdmissible.tate_twist`,
  `New.Period.IsPotentiallyCrystalline.comp`: finer filters, Tate twists and pull-back.


### `overZp`

 A representation over `R`, read as a representation over `ℤ_[p]`. 

### `instance : IsTorsionFree Bmax (Bmax ⊗[ℤ_[p]] T)`

 `Bmax ⊗ T` is torsion-free over `Bmax`: it is free, being `Bmax ⊗_{ℚ_p} (ℚ_p ⊗ T)`. 

### `periodTensorMap`

 The `B`-linear map `B ⊗ T → B' ⊗ T'`, `b ⊗ x ↦ b ⊗ f x`, along the algebra map `B → B'`. 

 ### The semilinear maps `tensorAction` 

### `tensorAction_smul`

 The map `b ⊗ x ↦ m b ⊗ g x` on `B ⊗ T` is semilinear for the action of `m` on `B`. 

### `tensorAction_periodTensorMap`

 Let `f : T → T'` be `ℤ_p`-linear with `f ∘ g = g' ∘ f`. Then for every `m` in `M`,
`New.Period.periodTensorMap` commutes with the actions `b ⊗ x ↦ m b ⊗ g x` on `B ⊗ T` and
`b ⊗ x ↦ m b ⊗ g' x` on `B' ⊗ T'`. This needs the action of `M` on `B'` to be compatible with the
`B`-algebra structure of `B'`. 

### `tensorAction_tensorAction`

 Applying `tensorAction` (for `(m, g)`, the map `b ⊗ x ↦ (m • b) ⊗ g x` on `B ⊗ T`) for `(n, k)`
and then for `(m, g)` is `tensorAction` for `(m * n, g * k)`. 

 ### Criteria for admissibility and its stability 

### `mem_fixedPeriods_iff`

 An element `x` of `B ⊗ T` lies in `fixedPeriods ρ B F` if and only if `j(g) ⊗ ρ(g)` fixes it
for `F`-almost all `g`. 

### `isAdmissible_of_one_tmul_mem_span`

 If `1 ⊗ x` lies in the `Bmax`-span of the periods fixed along `F` for every `x` in `T`, then
`ρ` is admissible along `F`. 

### `fixedPeriods.periodTensorMap_mem`

 If `f` intertwines `ρ g` and `ρ' g` for all `g` in a set of `F` (hypothesis `hf`), then
`b ⊗ x ↦ b ⊗ f x` sends periods of `ρ` in `B` fixed along `F` to periods of `ρ'` in `Bmax` fixed
along `F`. 

### `Bmax.pUnit`

 The prime `p` as a unit of `Bmax`: the image of `p`, which is a unit of `B⁺`. 

### `exists_tate_twist_unit`

 Let `ρ` and `σ` be representations on `T` of the group `Γ`, which maps to `Gp p` (`p` the
prime) by `j = toGp` of the instance `𝒥`; `χ g` is the cyclotomic character of `j(g)`. Let `σ` be
the twist `χ ^ c • ρ` (hypothesis `hσ`). Then some unit `t` of `Bmax` turns, by multiplication,
the action of `(n, j(g))` (that is, `φ ^ n ∘ j(g)` on `Bmax`) through `ρ` into the action through
`σ`, up to the factor `p ^ (-n c)`, with `p` the unit `Bmax.pUnit`. 

### `tensorAction_mk_one`

 `tensorAction` for the pair `(1, g)` of `FrobGal` is `tensorAction` for `g`: `φ ^ 0` is the
identity. 

### `IsAdmissible.tate_twist`

 Let `ρ` be a representation of `Γ` on `T`, where `Γ` maps to Gal(ℚ̄_p/ℚ_p) by `j`. Say `ρ` is
admissible along a filter `F` on `Γ` if the elements of `Bmax ⊗ T` fixed by `j(g) ⊗ ρ(g)` for
`F`-almost all `g` span `Bmax ⊗ T` over `Bmax`. If `ρ` is admissible along `F`, then so is every
Tate twist `σ = χ ^ c • ρ` (hypothesis `hσ`, with `χ` the cyclotomic character and `c` an integer).

For `F = ⊤` and `F = nearOne Γ`, this says that crystalline and potentially crystalline
representations are stable under twists by powers of the cyclotomic character. 

### `IsAdmissible.mono`

 Here `ρ` is admissible along a filter `F` on `Γ` when the elements of `Bmax ⊗ T` fixed by
`j(g) ⊗ ρ(g)` for `F`-almost all `g` span `Bmax ⊗ T` over `Bmax`; `j : Γ → Gp p` is the map with
open image given by `OverGp Γ p`. If `ρ` is admissible along `F`, it is admissible along every finer
filter `F' ≤ F`, because an element fixed for `F`-almost all `g` is fixed for `F'`-almost all
`g`. 

### `IsAdmissible.periodTensorMap_mem_span_fixedPeriods`

 Let `ρ` be admissible along `F` and let `f` intertwine `ρ g` and `ρ' g` for all `g` in a set of
`F` (hypothesis `hf`). Then the map `1 ⊗ f` sends `Bmax ⊗ T` into the span of the periods of `ρ'`
fixed along `F`. 

### `IsCrystalline.isPotentiallyCrystalline`

 A crystalline representation is potentially crystalline: the filter `nearOne Γ` is finer than
`⊤`. 

### `isAdmissible_of_cyclotomicGp_zpow`

 If `Γ` acts through the `c`-th power of the cyclotomic character (`χ g`, the cyclotomic
character of `j(g)`, with `j` = `toGp`), then `ρ` is admissible along every filter `F`. 

 ### Pull-back and the filter of elements near 1 

### `isAdmissible_comp_iff`

 Let `φ : Γ' →* Γ` be such that `toGp ∘ φ` has open image (`h_open`), which makes `Γ'` a group
over `Gp p`. Here a representation is admissible along a filter when the elements of `Bmax ⊗ T`
fixed by `j(g) ⊗ ρ(g)` for almost all `g` span `Bmax ⊗ T` over `Bmax`, where `j` is the map to
`Gp p` (`toGp` for `Γ`, `toGp ∘ φ` for `Γ'`). The pull-back `ρ ∘ φ` is admissible along a filter `F`
on `Γ'` if and only if `ρ` is admissible along the image filter `F.map φ`. 

### `map_nearOne`

 Let `toGp : Γ →* Gp p` be injective and let `φ : Γ' →* Γ` be such that `toGp ∘ φ` has open image
in `Gp p`. Then `φ` carries the filter `nearOne Γ'`, taken for `toGp ∘ φ`, to `nearOne Γ`. 

### `IsPotentiallyCrystalline.comp`

 The pull-back of a potentially crystalline representation along `φ : Γ' →* Γ` is potentially
crystalline, where `Γ'` maps to `Gp p` by `toGp ∘ φ`, assumed to have open image (`h_open`). This
covers restriction to the Galois group of a finite extension of the base field. 


## The action on B ⊗ T in the coordinates of a basis of T

* `New.Period.coordAction`: apply `toGp g` to each coordinate, then multiply by the matrix of `ρ g`.


### `repMatrix`

 The monoid homomorphism sending `g` in `Γ` to the matrix over `ℤ_[p]` of `ρ g` in a finite
`ℤ_[p]`-basis `e` of `T`. 

### `coordAction`

 The action on `B ⊗ T` in coordinates. `g` acts on a vector `y : ι → B` by applying `toGp g` to
each coordinate. It then multiplies by the matrix `New.Period.repMatrix ρ e g`, read over `B`. 

### `equivFun_tensorAction`

 For a `ℤ_[p]`-algebra `B` with an action of `Gp p` and a finite `ℤ_[p]`-basis `e` of `T`, the
map `b ⊗ x ↦ j(g) b ⊗ ρ(g) x` on `B ⊗ T` becomes, in the coordinates given by `e`, the action
`New.Period.coordAction` built from the matrices `New.Period.repMatrix ρ e g`. 
