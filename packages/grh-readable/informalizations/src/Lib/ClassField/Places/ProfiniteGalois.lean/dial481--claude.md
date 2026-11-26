---
{
  "module": "src/Lib/ClassField/Places/ProfiniteGalois.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/Places/ProfiniteGalois.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/Places/ProfiniteGalois.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Profinite Galois groups: continuity, restriction maps and the Galois correspondence

Infinite Galois theory for an abstract group. `New.IsProGalois Γ K Ω` says that the profinite group
`Γ` acts on the Galois extension `Ω / K` as its Galois group, with open stabilisers. This covers
`Gal(Ω/K)` and its closed subgroups `H` (acting over the fixed field `New.fixedFieldOf H`) at once.
`Fact (IsOpen U)` and `IsClosed H` are used as instances on subgroups.

* `New.continuous_of_equivariant_emb`: a map between such groups that is compatible with a ring
  homomorphism of the top fields is continuous.
* `New.exists_galois_restrict`, `New.isClosedEmbedding_galois_restrict`,
  `New.isOpenEmbedding_galois_restrict`: restriction maps between Galois groups, along a map of the
  top fields or to a smaller base field. The parts of the second one are
  `New.isClosedEmbedding_of_smul_eq_smul`, `New.range_eq_fixingSubgroup_of_smul_eq_smul` and
  `New.index_range_eq_finrank_of_smul_eq_smul`.
* `New.fixedFieldOf_fixingSubgroup`, `New.fixingSubgroup_fixedFieldOf`, `New.finrank_fixedFieldOf`:
  the Galois correspondence between intermediate fields and closed subgroups, with degree equal to
  index.

Notions from other files:
* `New.DiscreteUnits.ofBase`: the homomorphism from K^× to the Γ-invariants of Ω^× (both written
  additively) induced by K → Ω.

## Relation to the literature

Known; see `Lib.ClassField.Places.LocalFields` for sources.


### `instance {K : Type*} [Field K] [CharZero K] [Algebra K Ω] : IsAlgClosure K Ω`

 `Ω` is an algebraic closure of every field `K` of characteristic zero of which it is an
algebra. 

### `Ω.fieldEmb`

 A chosen embedding of the number field K into the fixed algebraic closure `Ω` of ℚ (the constant
of the instance above, not the section variable `Ω`). 

### `instance [IsGalois K Ω] : IsProGalois Gal(Ω/K) K Ω`

 The Galois group of a Galois extension `Ω / K`, with its Krull topology, acts on `Ω` as its
profinite Galois group. 

### `instance [ContinuousMul Γ] : IsClosed (X`

 An open subgroup `U` of a topological group is closed. 

### `instance [CompactSpace Γ] : CompactSpace H`

 A closed subgroup `H` of a compact group is compact. 

### `instance : @IsProGalois H (fixedFieldOf H) Ω _ _ _ inferInstance _ _`

 A closed subgroup is the Galois group over its fixed field. 

 ### The topology of `Γ` and its action on `Ω` 

### `isLocallyConstant_smul`

 For each `x : Ω`, the orbit map `g ↦ g • x` on the profinite Galois group `Γ` is locally
constant. 

### `isClosed_setOf_smul`

 The elements `g` of the profinite Galois group `Γ` such that `g • x` satisfies a given predicate
form a closed set. 

### `continuous_of_equivariant_emb`

 Let `Γ` act as the Galois group of `Ω / K`, `Γ'` as that of `Ω' / L`, and let `j : Ω → Ω'` be a
ring homomorphism. A map `φ : Γ' → Γ` with `j (φ g • x) = g • j x` for all `g` and `x` is
continuous. 

### `toAlgAut_surjective`

 Every `K`-automorphism of `Ω` is given by an element of `Γ`. 

### `DiscreteUnits.ofBase_bijective`

 The units of `K` are exactly the `Γ`-invariant units of `Ω`. 

### `exists_apply_smul_eq_of_comp_algebraMap_eq`

 Two ring homomorphisms `j, j' : Ω → Ω'` that agree on `K` differ by an element of `Γ`:
`j (g • x) = j' x` for some `g` and all `x`. 

 ### Restriction maps 

### `exists_galois_restrict`

 Let `Γ` act as the Galois group of `Ω / K`, `Γ'` as that of `Ω' / L`, and let `j : Ω → Ω'` be a
ring homomorphism such that every element of `Γ'` fixes the image under `j` of each element of `K`.
Then there is a continuous homomorphism `φ : Γ' → Γ` with `j (φ g • x) = g • j x` for all `g` and
`x`. 

### `isClosedEmbedding_of_smul_eq_smul`

 For `K ⊆ Ω`, `L ⊆ Ω` with profinite Galois groups `Γ` of `Ω / K` (`G`) and `Γ'` of `Ω / L`
(`J`), a homomorphism `φ: Γ' →* Γ` with `φ g • x = g • x` for all `g` and `x` (such as
`AlgEquiv.restrictScalarsHom`) is a closed embedding. 

### `range_eq_fixingSubgroup_of_smul_eq_smul`

 For `K ⊆ Ω`, `L ⊆ Ω` with Galois groups `Γ` of `Ω / K` and `Γ'` of `Ω / L`, the range of a
homomorphism `φ: Γ' →* Γ` with `φ g • x = g • x` for all `g` and `x` is the subgroup of `Γ` fixing
`L` pointwise. 

### `index_range_eq_finrank_of_smul_eq_smul`

 For `K ⊆ L ⊆ Ω` with Galois groups `Γ` of `Ω / K` and `Γ'` of `Ω / L`, the range of a
homomorphism `φ : Γ' →* Γ` with `φ g • x = g • x` for all `g` and `x` has index `[L : K]` in `Γ`
(both sides are `0` if the degree is infinite). 

### `isClosedEmbedding_galois_restrict`

 Restriction to a smaller base field. For `K ⊆ L ⊆ Ω` with Galois groups `Γ` of `Ω / K` and `Γ'`
of `Ω / L`, a homomorphism `φ : Γ' →* Γ` compatible with the actions on `Ω` is (a) a closed
embedding, (b) onto the subgroup fixing `L`, (c) whose index is `[L : K]` (both sides are `0` if the
degree is infinite). 

### `isOpenEmbedding_galois_restrict`

 For `K ⊆ L ⊆ Ω` with `L / K` finite and Galois groups `Γ` of `Ω / K` and `Γ'` of `Ω / L`, a
homomorphism `φ : Γ' →* Γ` with `φ g • x = g • x` for all `g` and `x` is an open embedding. 

 ### The Galois correspondence 

### `fixedFieldOf_fixingSubgroup`

 Galois correspondence: the fixed field of the subgroup of `Γ` fixing an intermediate field `L`
of `Ω / K` pointwise is `L`. 

### `eq_fixingSubgroup_of_isProGalois`

 Let Γ act as the Galois group of Ω/K, and K ⊆ L ⊆ Ω. A subgroup V of Γ that acts as the
Galois group of Ω/L is the subgroup fixing L pointwise, and its index is [L : K] (both read as 0 if
infinite). 

### `fixingSubgroup_fixedFieldOf`

 Galois correspondence: the subgroup of `Γ` fixing the fixed field of a closed subgroup `H`
pointwise is `H`. 

### `finrank_fixedFieldOf`

 The fixed field of a closed subgroup `H` has degree the index of `H` (`0` if infinite). 

### `finiteDimensional_fixedFieldOf`

 The fixed field of an open subgroup is finite over `K`. 

### `instance [NumberField K] : NumberField (fixedFieldOf U)`

 The fixed field of an open subgroup, over a number field `K`, is a number field. 
