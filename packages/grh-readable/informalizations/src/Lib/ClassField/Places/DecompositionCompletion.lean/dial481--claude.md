---
{
  "module": "src/Lib/ClassField/Places/DecompositionCompletion.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/Places/DecompositionCompletion.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/Places/DecompositionCompletion.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Decomposition groups of places above p as Galois groups of local fields in ℚ̄_p

Let `Ω` be an algebraic closure of a number field `K` and `Γ` its Galois group. A place of `Ω` is a
valuation subring `A` of `Ω` (the type `ClosurePlace`), and `New.IsPlaceOver A v` says that it lies
over the prime `v` of `K`.

`New.decompGroup Γ A` is the stabiliser of `A`, `New.Gp p` is `Gal(ℚ̄_p/ℚ_p)`, and `New.intQpBar p`
is the valuation ring of `ℚ̄_p`. Every place above `p` is induced by an embedding `Ω → ℚ̄_p`, and
the decomposition group then embeds as an open subgroup of `New.Gp p`, acting as the Galois group
over the completion at `v`.

## Main definitions and results

* `New.Period.isLocalGalois_of_isOpenEmbedding`: let `j` be an open embedding of a group in
  `Gal(ℚ̄_p/ℚ_p)`. Then the group is the absolute Galois group of the subfield of `ℚ̄_p` fixed by
  the image of `j`.
* `New.exists_comap_intQpBar_eq`: every place of an algebraic closure of `ℚ` above `p` is induced by
  an embedding in `ℚ̄_p`.
* `New.IsCompletionEmb`: the decomposition group of `A` acts on `ℚ̄_p` as the Galois group over the
  completion at `v`, compatibly with an embedding `j : Ω → ℚ̄_p` that induces `A`.
* `New.IsPlaceOver.exists_isCompletionEmb`: such data exist for every place `A` of `Ω` over `v`.
* `New.IsPlaceOver.isLocalGalois_and_residueCard_eq_and_isUniformiser`: the fixed field is local
  (`New.IsLocalGalois`), with the same residue order, and uniformisers of `K` remain uniformisers.
* `New.IsPlaceOver.ramification_in_tower`: ramification index and residue degree in a finite
  extension of `K`.

Notions from other files:
* `New.IsLocalGalois Γ K A`: `Γ` acts as the profinite Galois group of the algebraically closed
  field `Ω` over `K` and stabilises the valuation ring `A`, and `A ∩ K` (`New.valRingBelow`) is a
  discrete valuation ring with finite residue field.
* `New.PadicField F p`: a normed field `F` that is a normed algebra over `ℚ_p`, not necessarily
  complete.
* `New.residueCard K A`: the number of elements of the residue field of the valuation ring of `K`
  induced by `A` (zero if infinite).
* `New.IsProGalois`: a profinite group acts on the Galois extension Ω/K as its Galois group, with
  open stabilisers.
* `New.ordRat K A`: the order normalised on `K`: a chosen additive f : Ω^× → ℚ with n f(x) = a
  exactly when x^n and π^a have equal valuation, for uniformisers π of `K`.

## Relation to the literature

Known; see `Lib.ClassField.Places.LocalFields` for sources.



## Decomposition groups above p as open subgroups of the Galois group of ℚ_p


 ### The local field `ℚ_p` 

### `valuation_comap_intQpBar_lt_one`

 The place of `Ω` induced by `ι : Ω → ℚ̄_p` lies above `p`. 

### `toSubring_valRingBelow_intQpBar`

 The valuation ring that `ℚ̄_p` induces on `ℚ_p` is `ℤ_p`: both consist of the elements of norm
at most `1`. 

### `valRingBelowEquivPadicInt`

 The valuation ring that `ℚ̄_p` induces on `ℚ_p`, identified with `ℤ_p`. 

### `Selmer.residueCard_padic`

 The residue field of `ℚ_p` for the valuation ring that `ℚ̄_p` induces on it (which is `ℤ_p`) has
`p` elements. 

### `isLocalGalois_padic`

 `Gal(ℚ̄_p/ℚ_p)` is the absolute Galois group of the local field `ℚ_p`: it maps the valuation
ring of `ℚ̄_p` to itself, and this ring meets `ℚ_p` in `ℤ_p`, a discrete valuation ring with
finite residue field. 

### `padic_mem_topologicalClosure`

 In a normed field F over ℚ_p, the topological closure of any subfield contains the image of
ℚ_p. 

### `denseRange_emb_padicAlgCl`

 A ring homomorphism `ι` from the algebraic closure `Ω` of `ℚ` to `ℚ̄_p` has dense image. 

 ### Open subgroups of the Galois group of `ℚ_p` 

### `Selmer.IsCompletionGroup`

 For an embedding `e : K → ℚ̄_p` of a field `K` and a homomorphism `j : Γ → Gal(ℚ̄_p/ℚ_p)` from
the topological group `Γ`: `j` is an open embedding whose image consists of the elements fixing
`e(K)` pointwise. 

### `Period.isLocalGalois_of_isOpenEmbedding`

 If `j` is an open embedding of the topological group `Γ` into `Gal(ℚ̄_p/ℚ_p)`, then `Γ`, acting
on `ℚ̄_p` through `j` (the `let` in the statement), is the absolute Galois group of the fixed field
of `j(Γ)`, in the sense of `New.IsLocalGalois` for the integers of `ℚ̄_p`. 

### `GaloisRep.InducesPlace`

 `j` is the map from the decomposition group of `A` to `Gal(ℚ̄_p/ℚ_p)` that goes with the
embedding `e : Ω → ℚ̄_p`: (a) `A` is the preimage under `e` of the valuation ring of `ℚ̄_p`,
(b) `j g` acts on the image of `e` as `g` acts on `Ω`, and (c) `j` is an open embedding whose
image consists of the automorphisms that fix `e K` pointwise. The bracketing is
`((a) ∧ (b)) ∧ (c)`. 

### `smul_eq_self_of_mem_decompGroup_of_mem_closure`

 Let `Γ` act on `Ω` as the Galois group over `K`, let `ι : Ω → ℚ̄_p`, and let `σ` lie in the
decomposition group of the place that `ι` induces on `Ω`. If `ι x` lies in the closure of `ι(K)`,
then `σ` fixes `x`. 

### `exists_inducesPlace`

 Let `Ω` be `New.Ω`, the fixed algebraic closure of `ℚ`, and let `K` be a number field inside
`Ω`, with `Γ` acting as the Galois group of `Ω/K` (`IsProGalois`). An embedding
`ι : Ω → ℚ̄_p` that pulls the integers of `ℚ̄_p` back to the place `A` induces an open embedding `j`
of the decomposition group of `A` in `Gal(ℚ̄_p/ℚ_p)`, with `j(g)(ι x) = ι(g x)`, whose image
consists of the automorphisms fixing `ι(K)` pointwise (`GaloisRep.InducesPlace`). 


## Places of number fields from p-adic embeddings

`New.placeOfEmb σ` is the prime induced by an embedding `σ`, and `New.LocField v` is the completion
at `v`.


### `EmbeddedNumberField`

 A number field K together with a chosen embedding into the fixed algebraic closure `New.Ω`
of ℚ, given as an algebra structure. 

### `instance {K : Type*} [Field K] [NumberField K] [Algebra K Ω] : EmbeddedNumberField K`

 A number field with an algebra map into `Ω` is an embedded number field. 

### `IsPadicAt`

 An embedding of the completion `K_v = LocField v` in `ℚ̄_p` (the algebra structure) and an
embedding `j : Ω → ℚ̄_p` that fit together: the first is continuous and induces the integers of
`K_v`, `j` agrees with it on `K`, and `j` pulls the integers of `ℚ̄_p` back to `A`. 

### `IsPadicAt.continuous`

 The map from `K_v` to `ℚ̄_p` is continuous. 

### `IsPadicAt.valRingBelow_eq`

 The integers of `ℚ̄_p` meet `K_v` (the `_`) in its ring of integers `LocInt v`. 

### `IsPadicAt.comap_eq`

 The integers of `ℚ̄_p` pull back under `j` to `A`. 

### `IsPadicAt.map_algebraMap`

 On `K`, the embedding `j` agrees with the map through `K_v`. 

### `IsCompletionEmb`

 The decomposition group of `A` acts on `ℚ̄_p` as its Galois group over the completion
`LocField v`. The embedding of `LocField v` in `ℚ̄_p` is continuous and induces the integers
`LocInt v`. The map `j : Ω → ℚ̄_p` is an equivariant `K`-embedding that induces `A`. 

### `IsCompletionEmb.equivariant`

 The embedding `j` commutes with the action of the decomposition group. 

### `isPlaceOver_placeOfEmb`

 The place of `Ω` induced by an embedding `j` in `ℚ̄_p` lies over the prime of `K` induced by the
restriction of `j`. 

### `exists_comap_intQpBar_eq`

 For `Ω` an algebraic closure of `ℚ`, every valuation subring `A` of `Ω` in which `p` has
valuation below `1` (`A p` is the valuation of `p` at `A`) is the preimage of the integers of
`ℚ̄_p` under some embedding `Ω → ℚ̄_p`. 

### `nonempty_isCompletionEmb_of_isPadicAt`

 Let `Ω` be `New.Ω`, the algebraic closure of `ℚ`, let `Γ` be the Galois group of `Ω` over the
number field `K`, and let `A` be a place of `Ω`. Suppose the completion `LocField v` embeds
continuously in `ℚ̄_p` (the algebra instance `a`), and the integers of `ℚ̄_p` pull back to
`LocInt v`. Suppose also that `j : Ω → ℚ̄_p` agrees with this embedding on `K` and induces `A`
(together: `IsPadicAt`). Then the decomposition group of `A` acts on `ℚ̄_p`, compatibly with `j`,
as the Galois group of `ℚ̄_p` over `LocField v` (`IsCompletionEmb`). 

### `IsPadicAt.residueCard_eq`

 If the embedding of `LocField v` in `ℚ̄_p` and `j` fit together as in `IsPadicAt`, then the
residue field of `LocField v` for the integers of `ℚ̄_p` has `v.q` elements, the norm of `v`. 

### `IsPadicAt.isUniformiser_iff`

 Suppose the embedding of `LocField v` in `ℚ̄_p` and `j` fit together as in `IsPadicAt`. Then an
element of the completion at `v` is a uniformiser for the integers of `ℚ̄_p` exactly when its
`v`-adic valuation (written multiplicatively) is `exp (-1)`. 

### `IsPlaceOver.exists_isCompletionEmb`

 If the place `A` of `Ω` lies over the prime `v` of `K`, then for some prime `p` there are
embeddings of `K_v = LocField v` and of `Ω` in `ℚ̄_p`, the second inducing `A`, that make the
decomposition group of `A` the absolute Galois group of `K_v` (`IsCompletionEmb`). 


## The decomposition group as a local Galois group; orders and towers

For a map `x : G → M` with `x(gk) = x(g) + a(g)x(k)`, the zero set of `x` is a subgroup when `a` is
a monoid homomorphism (`New.cocycleKer`).

For a place `A` of `Ω` over the prime `v` of `K`, the field fixed by `decompGroup Γ A` is a local
field with the residue field of `v`.


 ### Maps with the cocycle relation 

### `cocycleKer`

 For x : G → M with the cocycle relation c : x(gk) = x(g) + a(g)x(k), where a : G → R is a
monoid homomorphism, the subgroup of the g with x(g) = 0. 

### `sah`

 Sah's lemma. Let x : G → M satisfy the cocycle relation c : x(gk) = x(g) + a(g)x(k), with
scalars a(g) in the ring R. If x vanishes at (γg)⁻¹(gγ), then (a(γ) − 1)x(g) = (a(g) − 1)x(γ). 

### `cocycle_conj_eq_smul`

 Let x : G → M satisfy the cocycle relation c : x(gk) = x(g) + a(g)x(k), with scalars a(g) in
the ring R. If a(g) fixes x(γ⁻¹), then x(γgγ⁻¹) = a(γ)x(g). 

 ### The decomposition field 

### `isLocalGalois_and_residueCard_eq_and_isUniformiser`

 Let the place A of Ω lie over the prime v of K (an integer of K is in the maximal ideal of A
exactly when it lies in v), and let F be the field fixed by the decomposition group of A, its
stabiliser in Γ. Then F is a henselian local field for A (`IsLocalGalois`), whose residue field has
`v.q` elements, the norm of v, and uniformisers of K (`IsUniformiser A`: uniformisers of the
valuation ring `A ∩ K`) stay uniformisers of `A ∩ F`. 

### `isLocalGalois_decompGroup`

 If A lies over v, the decomposition group of A is the Galois group of Ω over its fixed field F,
and F is a henselian local field for A: A ∩ F is a discrete valuation ring with finite residue
field. 

### `residueCard_fixedFieldOf_decompGroup`

 If A lies over v, the residue field of the field fixed by the decomposition group of A has
`v.q` elements, as many as that of v. 

### `isUniformiser_map_fixedFieldOf_decompGroup`

 If A lies over v, an element of K that is a uniformiser for A is still a uniformiser in the
field fixed by the decomposition group of A. 

### `exists_uniformiser`

 If A lies over v, some π in Kˣ has v-adic valuation `exp (-1)` and is a uniformiser for A in
the field fixed by the decomposition group of A. 

### `ordRat_fixedFieldOf_decompGroup`

 If A lies over v, the order on Ωˣ normalised on the field fixed by the decomposition group of A
agrees with the order normalised on K. 

### `exists_isFrob`

 If A lies over v, then Γ contains an arithmetic Frobenius at A: an element that stabilises A
and acts as x ↦ x ^ v.q modulo the maximal ideal of A (`IsFrob`). 

 ### The normalised order 

### `ordRat_eq_zero_iff`

 If A lies over v, an element x of Ωˣ (written additively) has order 0 at A, for the order
normalised on K, exactly when its valuation at A is 1. 

### `ordRat_nonneg_iff`

 If A lies over v, an element x of Ωˣ (written additively) has nonnegative order at A, for the
order normalised on K, exactly when x lies in the valuation ring A. 

### `ordRat_ofBase`

 Let `K` be a number field inside the field `Ω` (the fixed algebraic closure of ℚ), `Γ` the
Galois group of `Ω/K`, and `A` a place of `Ω` over the prime `v` of `K`. For x in Kˣ, the order
at A, normalised on K, of the image `ofBase` of x in Ωˣ is minus the logarithm of the v-adic
valuation of x. 

### `ordRat_smul`

 Let A lie over v. For g ∈ Γ and x ∈ Ωˣ, the order (normalised on K) of gx (`unitsRep g x`) at
the place gA equals the order of x at A. 

### `exists_ordRat_eq_intCast`

 Let A lie over v. If x in Ωˣ is fixed by every element of the inertia group of A, then the
order of x at A, normalised on K, is an integer. 

 ### Towers and generation of the decomposition group 

### `ramification_in_tower`

 Let `L / K` be number fields embedded in `Ω` (`EmbeddedNumberField`), with `U`, open in `Γ`, the
Galois group of `Ω / L`; let `A` lie over `v` in `K` and over `w` in `L`; `e` and `f = inertiaDeg`
are the ramification index and residue degree of `w` over `K`. If the decomposition group lies in
`U`, the residue fields have the same order and `ordRat L A = ordRat K A`, where `ordRat K A` is a
chosen additive order `Ωˣ → ℚ` for the valuation of `A`, normalised so that uniformisers of `K` have
order 1. If inertia lies in `U`, then `e = 1`. The index of `U ⊓ decompGroup Γ A` in
`decompGroup Γ A` is `e * f`. 

### `ramificationIdx_eq_one_of_inertiaGroup_le`

 Let `A` lie over `v` in `K` and over `w` in `L`, where `U`, open in `Γ`, is the Galois group of
`Ω / L`. If `U` contains the inertia group of `A`, then `w` is unramified over `K`. 

### `relIndex_decompGroup_eq`

 Let `A` lie over `v` in `K` and over `w` in `L`, where `U`, open in `Γ`, is the Galois group of
`Ω / L`. The index of `U ⊓ decompGroup Γ A` in `decompGroup Γ A` is the ramification index times
the residue degree of `w` over `K`. 

### `decompGroup_le`

 Let A lie over v. An open subgroup of `Γ` that contains the inertia group of `A` and a
Frobenius element `φ` at `v` (`IsFrob A v.q φ`: `φ` stabilises `A` and acts as x ↦ x ^ v.q modulo
its maximal ideal) contains the whole decomposition group. 
