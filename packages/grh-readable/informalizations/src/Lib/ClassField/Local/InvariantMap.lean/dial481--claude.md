---
{
  "module": "src/Lib/ClassField/Local/InvariantMap.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/Local/InvariantMap.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/Local/InvariantMap.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The local invariant Br(k) ≅ Q/Z and its behaviour under restriction and maps of local fields

The invariant map of local class field theory, for a henselian local field `k` of characteristic `0`
with absolute Galois group `Γ` acting on `Ω` (`New.IsLocalGalois`).

* `New.IsLocalGalois.isClassOfInvariant_classOfInvariant`: the chosen map
  `New.Cohomology.classOfInvariant` from ℚ/ℤ to H²(Γ, Ωˣ) is injective and computes the cyclic
  classes of unramified characters.
* `New.IsLocalGalois.classOfInvariant_bijective`: `New.Cohomology.classOfInvariant` is bijective, so
  it identifies ℚ/ℤ with H²(Γ, Ωˣ).
* `New.Cohomology.resH2_classOfInvariant`, `New.IsLocalGalois.exists_resH2_classOfInvariant_eq`:
  restriction to an open subgroup multiplies the invariant by the index and is onto.
* `New.IsLocalGalois.pairMapH2_classOfInvariant_of_ordRat_eq`,
  `New.IsLocalGalois.pairMapH2_classOfInvariant`: a map of local fields with ramification index `e`
  and residue degree `f` multiplies the invariant by `e * f`.

Notions from other files:
* `New.unitsModule`, `New.unitsRep`: `Ωˣ` written additively (`New.DiscreteUnits`) with the action
  of `Γ`, as a discrete module and as a representation; `H0` are its `Γ`-invariants, the units
  of `k`.
* `New.DiscreteModule.resH2`: restriction of a class in `H²(Γ, M)` to a subgroup of `Γ`; a class is
  split by `V` when its restriction to `V` is zero.
* `New.cyclicClass`: the cyclic class (symbol) `(χ, w) = δχ ∪ w` of a character `χ : Γ → ℚ/ℤ` and
  an invariant `w`.

## Relation to the literature

Known; see `Lib.ClassField.Local.ArtinMap` for sources.


### `Nat.eq_of_pow_sub_one_mul_eq_mul_pow`

 If `R ^ (l - 1) * (l * c ^ l) = (l * c) ^ l` in `ℚ`, with `l` prime and `l * c ≠ 0`, then
`R = l`. 

### `mem_zmultiples_of_index_prime`

 Let `V` be an open normal subgroup of prime index in `Γ`. If `β ≠ 0` in `H²(Γ, Ωˣ)` is split
by `V` (its restriction to `V` is zero), then every class `x` split by `V` is an integer multiple
of `β`.

This is the case of prime index of `mem_zmultiples_of_resH2_eq_zero`: the classes split by `V` are
the symbols `(ψ, y)` with `ker ψ = V` and `y ∈ kˣ`, and they form a quotient of `kˣ` modulo
norms, a group of prime order `[Γ : V]`. 

### `mem_zmultiples_of_resH2_eq_zero`

 If the class `β` in `H²(Γ, Ωˣ)` is split by the open normal subgroup `V` (its restriction to
`V` is zero) and is killed only by multiples of `[Γ : V]`, then every class `x` split by `V` is an
integer multiple of `β`. 

 ### The class attached to an element of `ℚ/ℤ` 

### `exists_isClassOfInvariant`

 Let `Γ = Gal(Ω/k)` with `Ω` algebraically closed of characteristic 0, and let `A` be stable
under `Γ` with `A ∩ k` a discrete valuation ring with finite residue field (`IsLocalGalois Γ k A`).
Then there is an additive map `b : ℚ/ℤ → H²(Γ, Ωˣ)` satisfying `IsClassOfInvariant`. That is, `b` is
injective, and `b` sends `n • χ(φ)` to the cyclic class of `χ` and `w`, whenever `χ` is a continuous
unramified character `Γ → ℚ/ℤ`, `φ` is a Frobenius element, and `w ∈ Ωˣ` is invariant of normalised
order `n`. 

### `isClassOfInvariant_classOfInvariant`

 The chosen map `classOfInvariant` from `ℚ/ℤ` to `H²(Γ, Ωˣ)` is injective, and the cyclic class
of an unramified character `χ` and an invariant `w` of order `n` is
`n • classOfInvariant Γ k A (χ φ)` for a Frobenius `φ`.

This is the normalisation of the invariant map on the Brauer group of a local field in
characteristic 0, expressed through the inverse map and an arithmetic Frobenius. 

### `pairMapH2_classOfInvariant_of_ordRat_eq`

 Let `k'` be a second local field, with Galois group `Γ'` acting on `Ω'` and valuation ring `A'`,
and let `j : Ω → Ω'` be a field map compatible with `φ : Γ' → Γ` (`hj`) with `A'` pulling back to
`A` (`hA`). Suppose the `Γ`-fixed unit `w` of `Ωˣ` has normalised order `1` over `k` (`hw_ord`),
`j w` has order `e` over `k'` (`he`, so `e` is the ramification index), and the residue field of
`k'` has `q ^ f` elements, where `q` is that of `k` (`hf`). Then the map `H²(Γ, Ωˣ) → H²(Γ', Ω'ˣ)`
induced by `φ` and `j` sends `classOfInvariant Γ k A r`, the class with invariant `r ∈ ℚ/ℤ`, to the
class with invariant `(e * f) • r`. 

### `pairMapH2_classOfInvariant`

 For two local Galois data `Γ, k, A` and `Γ', k', A'`, let `φ : Γ' →ₜ* Γ` be continuous and
`j : Ω →+* Ω'` a ring map with `A'.comap j = A` and `j (φ g • x) = g • j x`. Suppose a `Γ`-invariant
unit `w` of `Ω` has normalised order `1` on `k`, its image under `j` has normalised order `e` on
`k'`, and `residueCard k' A' = residueCard k A ^ f`; then the map `H²(Γ, Ωˣ) → H²(Γ', Ω'ˣ)` induced
by `φ` and `j` sends the class of invariant `r` to the class of invariant `(e * f) • r`. This is the
form of `pairMapH2_classOfInvariant_of_ordRat_eq` with the two conditions on the orders of `w` in
one hypothesis `he`. 

### `_root_.New.Cohomology.resH2_classOfInvariant`

 Restriction to an open subgroup `V`, the Galois group of `Ω` over the fixed field
`fixedFieldOf V`, sends the class of `r` to the class of `[Γ : V] • r`.

Part of the functoriality of the local invariant: in characteristic 0, restriction to an open
subgroup multiplies the invariant by the degree, expressed through the inverse map ℚ/ℤ → H². 

 ### The invariant 

### `classOfInvariant_bijective`

 For a henselian local field `k` of characteristic `0` with absolute Galois group `Γ`, the map
`New.Cohomology.classOfInvariant` from `ℚ/ℤ` to `H²(Γ, Ωˣ)` is bijective. So the Brauer group of `k`
is `ℚ/ℤ`.

This is the invariant isomorphism, stated for the inverse map ℚ/ℤ → H²(Γ, Ωˣ) and for `k` henselian
and discretely valued with finite residue field, complete or not. 

### `exists_resH2_classOfInvariant_eq`

 Restriction to the open subgroup `V` (a finite extension of `k`) is onto on the classes of
`ℚ/ℤ`: every class `y` in `H²(V, Ωˣ)` is the restriction of the class of some `r`. 
