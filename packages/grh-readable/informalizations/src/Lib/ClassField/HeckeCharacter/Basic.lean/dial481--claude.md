---
{
  "module": "src/Lib/ClassField/HeckeCharacter/Basic.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/HeckeCharacter/Basic.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/HeckeCharacter/Basic.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Characters of U(1) of a CM field: existence, weights and conjugates

This file studies characters of the idele group and of the unitary group `U(1)` of a CM field `E`.
Here `U(1)(𝔸)` is `unitary (𝔸 E)`, the group of adeles `u` with `u ū = 1`, and `(u : 𝔸 E).fst` and
`(u : 𝔸 E).snd` are the archimedean and finite components of `u`. `New.integralU1 S` denotes the
points with integral finite part that are 1 modulo the places of a finite set `S`. `μ.HasWeight e ψ`
says that `μ(u) = ∏_v u_v^{e(v)} · ∏_w ψ_w(u mod w)` for integral `u` and that `ψ_w = 1` for almost
all `w`.

## Main definitions and results

* `New.AutChar`: continuous unitary characters of `U(1)(𝔸) = {u | u ū = 1}` trivial on the elements
  that come from `E`.
* `New.AdelicU1ClassGroup`, `New.finite_u1_classGroup`: the class group of level `S`, the quotient
  of `U(1)(𝔸)` by the join of the rational points `New.rationalU1` and `New.integralU1 S`, is
  finite.
* `New.AutChar.exists_hasWeight_of_prod_eq_one`: a character of weight `e` and tame part `ψ` exists
  if the formula defining `μ.HasWeight e ψ` is trivial on the integers of `E` of norm one (these
  integers are roots of unity, by `New.pow_torsionOrder_eq_one`).
* `New.AutChar.tameChars`, `New.AutChar.exists_mem_tameChars`,
  `New.AutChar.exists_classGroup_char_eq_of_hasWeight_zero`, `New.AutChar.finite_tameChars`: the
  characters of weight 0 and level `S` are those of the class group, and they are finitely many.
* `New.AutChar.finite_setOf_hasWeight`: there are finitely many characters of a given weight and
  tame part.
* `New.AutChar.HasWeight.exists_conj`: for an automorphism σ of ℂ that permutes the embeddings of
  the CM type, σ ∘ μ on points with archimedean component 1 extends to a character with permuted
  weight and tame part σ ∘ ψ.

Notions from other files:
* `New.𝔸`: The ring ℂ^f × 𝔸_f, one copy of ℂ for each infinite place of E times the ring `𝔸f E` of
  finite adeles (whose units are the finite ideles): the adele ring of E when E is totally complex.
* `New.Ô`: The ring of finite adeles of E that are integral at every finite place.

## Relation to the literature

Known; see `Lib.ClassField.Global.CMSplittingCharacters` for sources.



## Hecke characters and characters of U(1), with base change

* `New.HeckeChar`: unitary Hecke characters, trivial on principal ideles.


### `charsTrivialOnPrincipal`

 The group of continuous circle-valued characters of a topological monoid `G` that are trivial at
every `x` whose image under `f` lies in the diagonal copy of `E` in its adeles. 

### `HeckeChar`

 The group of unitary Hecke characters of E: continuous circle-valued characters of the idele
group trivial on principal ideles. 

### `AutChar`

 The group of continuous circle-valued characters of U(1)(𝔸), the norm-one adeles of the CM
field E, trivial on elements coming from E. 

### `HeckeChar.finPart`

 The homomorphism sending a unitary Hecke character of E to its restriction to the finite
ideles, with values in ℂ^×. 

### `HeckeChar.atUniformizer`

 The value of the Hecke character χ at the local idele given by the chosen uniformiser at the
finite place w. 

### `divStar`

 The continuous homomorphism x ↦ x/x̄ from the units of a commutative topological monoid R
with involution to the elements u with uū = 1. 

### `comp_divStar_mem_charsTrivialOnPrincipal`

 If `μ` is trivial on the rational points of `U(1)`, then `x ↦ μ(x / x̄)` is trivial on the
rational ideles. 

### `AutChar.baseChange`

 Base change: the homomorphism sending a character μ of U(1)(𝔸), trivial on rational points,
to the Hecke character x ↦ μ(x/x̄) of E. 

### `AutChar.baseChange_toUnits`

 On a unitary adele `w`, where `w / w̄ = w * w`, the base change of `ν` is `ν (w * w)`. 

### `AutChar.HasWeight`

 μ has weight e and tame part ψ: almost all residue characters ψ_w are trivial, and μ(u) = ∏_v
u_v^{e(v)} · ∏_w ψ_w(u mod w) whenever u has integral finite part. 

### `AutChar.HasWeight.finite_ramification`

 Only finitely many of the residue characters `ψ w` are nontrivial. 

### `AutChar.HasWeight.apply_eq`

 If `u` has integral finite part, then `μ u` is the product of the powers `u_v ^ e v` over the
  infinite places and of the values of `ψ w` at the reductions `reduceAt w` of the finite part of
  `u` modulo the finite places `w` (in the residue field `ResField w`). 


## Rational and integral points of U(1) and its class group

* `New.integralU1`: the points with integral finite part that are 1 modulo each place of a finite
  set S; an open subgroup (`New.isOpen_integralU1`).
* `New.exists_snd_div_divStar_finIdeleIncl_eq_one`: by Hilbert 90, the finite part of every point is
  y / ȳ for a finite idele y.
* `New.exists_eq_mul_star`, `New.divStar_surjective`: Hilbert 90 for a field with an involution,
  and for the ideles.


### `rationalU1`

 The subgroup of rational points of U(1)(𝔸): the adeles u with uū = 1 that come from E. 

### `integralU1`

 For a finite set S of finite places, the subgroup of U(1)(𝔸) of elements whose finite part is
integral and congruent to 1 modulo every place of S. 

### `mem_integralU1_iff`

 Membership in `integralU1 S`: the finite part of `u` is integral and reduces to `1` modulo every
place of `S`. 

### `isOpen_integralU1`

 The subgroup `integralU1 S` of U(1)(𝔸) is open. 

### `mem_integralU1_of_snd_eq_one`

 A point of U(1)(𝔸) with finite part `1` lies in `integralU1 S`. 

### `exists_snd_div_divStar_finIdeleIncl_eq_one`

 Every `u` in U(1)(𝔸) has a finite idele `y` such that `u / divStar (finIdeleIncl y)` has finite
part `1`. In other words, the finite part of `u` equals y / ȳ; here `finIdeleIncl y` is the idele
with archimedean part 1 and finite part `y`.

A consequence of Hilbert's Theorem 90. Only finite parts are matched, for norm-one adeles of a CM
field over its real subfield. 

### `divStar_eq_of_eq_mul_star`

 If an idele `y` satisfies `y = u * ȳ` for some `u` in `U(1)(𝔸)`, then `y / ȳ = u`. 

### `exists_eq_mul_star`

 Hilbert's Theorem 90 for a field with an involution that negates some nonzero element `j`: an
element `a` with `a * star a = 1` satisfies `b = a * star b`, that is `a = b / star b`, for some
nonzero `b`. 

### `divStar_surjective`

 Hilbert's Theorem 90 for the ideles: every `u` with `u ū = 1` is `y / ȳ` for an idele `y`. 

### `AutChar.baseChange_injective`

 Base change is injective: a character `μ` of `U(1)(𝔸)` is determined by `x ↦ μ(x / x̄)`, since
every point of `U(1)(𝔸)` is of the form `y / ȳ` (`divStar_surjective`). 

### `reduceU1`

 Reduction modulo w: the homomorphism from the elements of U(1)(𝔸) with integral finite part
to the multiplicative group of the residue field at w. 

### `divStar_principalIdele_mem_sup`

 For `x` in `Eˣ` with finite idele `y`, the point `y / ȳ` of U(1)(𝔸) is a rational point times a
point that has integral finite part and is 1 modulo the places of `S`. 

### `divStar_mem_integralU1_empty`

 If a finite idele `y` is a unit at every place, then `y / ȳ` has integral finite part. 

### `AdelicU1ClassGroup`

 The class group of `U(1)` of tame level `S`: the quotient of U(1)(𝔸) by the subgroup generated
by the rational points and the points with integral finite part that are 1 modulo every place of
the finite set `S`. 

### `exists_mk_divStar_eq`

 Every class in the class group of `U(1)` of tame level `S`, the quotient of U(1)(𝔸) by the join
of `New.rationalU1` and `New.integralU1 S`, is the class of `y / ȳ` for a finite idele `y`. 

### `finite_u1_classGroup`

 The class group of `U(1)` of tame level `S` is finite.

This is the analogue for `U(1)` of a CM field of the finiteness of ray class groups of a number
field, for a tame level given by a finite set of finite places. 

### `card_u1_classGroup_dvd_classNumber`

 The class group of `U(1)` of tame level `∅`, the quotient of U(1)(𝔸) by its rational points and
its points with integral finite part, has order dividing the class number of `E`. 


## Characters of given weight and tame part

* `New.AutChar.HasWeight.exists_pow_eq_prod`: a power of a value at a finite idele is algebraic,
  explicitly.


 ### Elements of norm one 

### `mem_integralU1_empty_of_snd_mem_Ô`

 A point `u` of `U(1)(𝔸)` with integral finite part lies in `New.integralU1 ∅`. 

### `snd_mem_Ô_of_mem_integralU1`

 The finite part of a point `u` of `New.integralU1 S` is integral. 

### `reduceAt_eq_one_of_mem_integralU1`

 A point `u` of `New.integralU1 S` reduces to `1` modulo every place `w` of `S`. 

### `val_reduceU1`

 The unit `New.reduceU1 w u` of the residue field at `w` is the reduction modulo `w` of the
finite part of `u`. 

### `isUnit_reduceAt_unitary`

 If the finite part of `u` in `U(1)(𝔸)` is integral, its reduction modulo `w` is a unit of the
residue field at `w`. 

### `norm_map_unitary`

 Every complex embedding `φ` of `E` sends an element `γ` of `E` with `γ γ̄ = 1` to the unit
circle. 

### `norm_unitary_fst`

 At every infinite place `v`, the component of a point `u` of `U(1)(𝔸)` has absolute value 1. 

### `pow_torsionOrder_eq_one`

 Kronecker's theorem in a CM field `E`: an algebraic integer `γ` of `E` with `γ γ̄ = 1` satisfies
`γ ^ n = 1`, where `n = torsionOrder E` is the number of roots of unity in `E`. 

### `finprod_tame_eq_prod_reduceU1`

 If `ψ` is trivial outside `S`, the product of the `ψ_w(u mod w)` over all finite places is the
finite product over `S`, with `u mod w` written as the unit `New.reduceU1 w u`. 

### `exists_unitary_of_mem_rationalU1`

 A rational point `u` of `U(1)(𝔸)` is the image of an element `y` of `E` with `y ȳ = 1`. 

 ### Weight and tame part under the group operations 

### `eq_of_mem_integralU1`

 Let `ψ` be a family of residue characters, trivial outside the finite set `S` of places. If
`f u = g u * ∏_w ψ_w(u mod w)` for all `u` with integral finite part, then `f u = g u` for `u` in
`New.integralU1 S`. 

### `HasWeight.one`

 The trivial character has weight 0 and trivial tame part. 

### `HasWeight.mul`

 If `μ` has weight `e` and tame part `ψ`, and `ν` has weight `e'` and tame part `ψ'`, then `μ ν`
has weight `e + e'` and tame part `ψ ψ'`. 

### `HasWeight.inv`

 If `μ` has weight `e` and tame part `ψ`, then `μ⁻¹` has weight `-e` and tame part `ψ⁻¹`. 

### `HasWeight.zpow`

 The `n`-th power of a character has `n` times the weight and the `n`-th power of the tame
part. 

 ### Existence and finiteness 

### `exists_hasWeight`

 Let ψ be trivial off a finite set S. A homomorphism χ : U(1)(𝔸) → ℂ, trivial on rational
points and equal to ∏_v u_v^{e(v)} · ∏_w ψ_w(u mod w) on integral u, is a continuous unitary
character of weight e and tame part ψ. 

### `exists_hasWeight_of_prod_eq_one`

 Let ψ be trivial off a finite set S. If ∏_v Φ_v(u)^{e(v)} · ∏_{w∈S} ψ_w(u mod w) = 1 for every
integer u of E with uū = 1 (Φ_v the embedding of E chosen at v), then some character of U(1)(𝔸),
trivial on rational points, has weight e and tame part ψ. 

### `tameChars`

 For a finite set S of finite places, the group of pairs (μ, ψ): μ a character of U(1)(𝔸) of
weight 0 with tame part ψ, and ψ trivial outside S. 

### `exists_mem_tameChars`

 Let `χ` be a complex character of the class group `U(1)(𝔸) / (rationalU1 ⊔ integralU1 S)` of
level `S`. Its pullback to `U(1)(𝔸)` is a continuous unitary character of weight 0 whose tame part
is trivial outside `S`. That is, some pair `(μ, ψ)` in `New.AutChar.tameChars S` has `μ u = χ ↑u`
for all `u`, where `↑u` is the class of `u`. 

### `exists_classGroup_char_eq_of_hasWeight_zero`

 Let `μ` be a character of `U(1)(𝔸)` of weight 0 whose tame part `ψ` is trivial outside a finite
set `S` of finite places. Then `μ` is the pullback of a character `χ` of the class group
`U(1)(𝔸) / (rationalU1 ⊔ integralU1 S)` of level `S`: `χ ↑u = μ u` for all `u`, where `↑u` is the
class of `u`. This is the converse of `New.AutChar.exists_mem_tameChars`. 

### `finite_tameChars`

 There are finitely many characters of weight `0` and given tame level. 

### `finite_setOf_hasWeight`

 There are finitely many characters `μ` of `U(1)(𝔸)` of a given weight `e` and tame part `ψ`.
These satisfy `μ u = ∏_v u_v^{e(v)} · ∏_w ψ_w(u mod w)` for all `u` with integral finite part. 

### `HasWeight.isOfFinOrder_apply`

 The values of a character of `U(1)(𝔸)` of weight 0 are roots of unity. 

### `HasWeight.exists_pow_eq_prod`

 Let `μ` have weight `e` and tame part `ψ`, and let `u` in `U(1)(𝔸)` have archimedean part 1.
There are `n > 0` and `γ` in `E` with `γ γ̄ = 1` such that (a) `uⁿ γ` is a unit at every finite
place, and (b) `μ(u)ⁿ = ∏_v Φ_v(γ)^{e v}`, with `Φ` the CM type. 

 ## Galois conjugates of characters of U(1) 

### `exists_conj`

 Let μ have weight e and tame part ψ, and let σ be an automorphism of ℂ that permutes the
embeddings of the CM type through a permutation p of the infinite places: σ ∘ Φ_v = Φ_{p(v)}.
Then some character ν has weight e ∘ p⁻¹ and tame part w ↦ σ ∘ ψ_w, and ν(u) = σ(μ(u)) for every
u with archimedean component 1. 
