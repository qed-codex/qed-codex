---
{
  "module": "src/Lib/ClassField/Places/Ideles.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/Places/Ideles.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/Places/Ideles.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Finite ideles, principal ideles and the class group; finite index of open subgroups

The finite ideles of a number field `K` are the units `(𝔸f K)ˣ` of the finite adeles. They embed in
the units of the adeles `New.𝔸 K`, the pairs of a map `NumberField.InfinitePlace K → ℂ` and a finite
adele, with component `1` at the infinite places. `New.FinPlace K` is the set of finite places, and
`New.LocField v` is the completion at `v`. The file defines principal, local and S-unit ideles and
proves their basic properties. It then relates the finite ideles to fractional ideals and the class
group, and deduces that every open subgroup containing the totally positive elements of `Kˣ` has
finite index.

## Main definitions and results

* `New.principalIdele`, `New.locIdele`, `New.ideleAt`: the principal idele of an element of `Kˣ`,
  the idele with one given component and `1` elsewhere, and the component at a place.
* `New.idelesUnitOff`: the ideles that are units outside `S`; open (`New.isOpen_idelesUnitOff`), and
  compact for `S = ∅` (`New.isCompact_idelesUnitOff_empty`).
* `New.exists_idele_divisor_hom`: the divisor map, with kernel the ideles that are units everywhere.
* `New.exists_idele_classGroup_hom`: a map to the class group whose kernel is `Kˣ` times these
  units.
* `New.exists_sup_idelesUnitOff_eq_top`: for a suitable finite `S`, every idele is a principal idele
  times a unit outside `S`.
* `New.finiteIndex_idele_subgroup_of_isOpen`: an open subgroup that contains the totally positive
  elements of `Kˣ` has finite index.

Notions from other files:
* `New.Ô K`: the integral finite adeles, whose component at every place lies in its ring of
  integers; `New.uniformizer w` is a chosen uniformiser of the completion at `w`.
* `S.unit K` (Mathlib): the `S`-units, the `x` in `Kˣ` of valuation `1` at every finite place
  outside `S`.

## Relation to the literature

Known; see `Lib.ClassField.Places.LocalFields` for sources.



## Finite ideles: principal and local ideles, S-unit ideles, positivity

`New.mem_of_locIdele_mem` and `New.eventually_unramified` rest on
`New.exists_finset_cover_mulSupport_ideleAt`, which comes from the compactness of
`New.idelesUnitOff ∅`.


 ### Principal ideles, local ideles, components and ideles that are units outside `S` 

### `principalIdele`

 The diagonal homomorphism from K^× to the finite ideles of K. 

### `locIdele`

 The homomorphism sending x ∈ K_v^× to the finite idele with component x at v and 1
elsewhere. 

### `finIdeleIncl`

 The homomorphism from the finite ideles of K to the units of `New.𝔸 K` sending a to (1, a), with
component 1 at every infinite place. 

### `locFullIdele`

 For a finite place v, the homomorphism from K_v^× to the units of `New.𝔸 K` placing the element
at v and 1 at all other places, finite and infinite. 

### `ideleAt`

 The homomorphism sending a finite idele to its component in K_v^×. 

### `idelesUnitOff`

 The group of finite ideles of K whose components at all places outside S are units. 

 ### First properties: membership, openness and compactness 

### `finite_setOf_valued_val_ne_one`

 A finite idele `a` is a unit at all but finitely many places. 

### `idelesUnitOff_empty`

 The ideles that are units at every place are the units of the ring of integral adeles. 

### `principalIdele_mem_idelesUnitOff`

 The principal idele of `x` is a unit outside `S` exactly when `x` is an `S`-unit. 

 ### Approximating an idele by finitely many components 

### `exists_finset_cover_mulSupport_ideleAt`

 For an open neighbourhood `U` of `1` there is a finite set `T` of places such that an idele
that is a unit everywhere and lies outside `U` has a component `≠ 1` at some place of `T`.
Equivalently, the ideles that are units everywhere and `1` on `T` lie in `U`. 

### `mem_of_locIdele_mem`

 A closed subgroup H of the finite ideles contains a as soon as it contains, for every place
v, the idele with component a_v at v and 1 elsewhere. 

### `locIdele_mem_idelesUnitOff`

 The idele with component `x` at `v` and `1` elsewhere is a unit outside any `S` when `x` is a
unit of the integers at `v`. 

### `eventually_unramified`

 A homomorphism ψ with open kernel from the finite ideles of K to a commutative group is
trivial on the local units at all but finitely many finite places. 

 ### Totally positive elements 

### `IsTotallyPositive`

 An element x of K is totally positive if φ(x) > 0 for every ring homomorphism φ : K → ℝ. 


## Ideles, fractional ideals and the class group

Here `v` is `Valued.v`, the multiplicative valuation of a completion, so the order of an element
at a place is `-log (v _)`.


### `fractionalIdeal_count_ext`

 Two nonzero fractional ideals with the same exponent at every prime are equal. 

### `exists_idele_divisor_hom`

 The divisor map: a homomorphism `d` from the finite ideles to the nonzero fractional ideals such
that (a) an idele `a` is integral at `w` exactly when the exponent of `w` in `d a` is nonnegative,
(b) the kernel is the group of ideles that are units everywhere, (c) the chosen uniformiser at `w`
goes to the prime `w`, and (d) the idele of `x ∈ Kˣ` goes to the principal fractional ideal
`(x)`. 

### `exists_idele_classGroup_hom`

 There is a homomorphism from the finite ideles to the class group whose kernel is generated by
the principal ideles and the ideles that are units everywhere. 

### `pow_classNumber_mem_principal_sup`

 For every finite idele a of K, the power a^h, with h the class number of K, is a principal
idele times an idele that is a unit at every prime. 

### `exists_valuation_eq_of_mem_sup`

 A principal idele times a unit outside `S` has, at the places outside `S`, the valuations of an
element of `Kˣ`. 

### `exists_sup_idelesUnitOff_eq_top`

 For finite sets `R`, `R'` of finite places there is a finite set `T` that contains `R`, meets
`R'` only inside `R`, and is such that every finite idele is a principal idele times an idele
that is a unit outside `T`. 

### `exists_superset_sup_idelesUnitOff_eq_top`

 Every finite set of places `R` lies in a finite set `S` such that every finite idele is a
principal idele times an idele that is a unit outside `S`. 

### `finiteIndex_idele_subgroup_of_isOpen`

 An open subgroup `H` of the finite ideles that contains the principal ideles of the totally
positive elements of `Kˣ` has finite index. 

### `instance : NonarchimedeanGroup (𝔸f K)ˣ`

 The finite ideles form a nonarchimedean group: they have the compact open subgroup
`idelesUnitOff ∅`. 
