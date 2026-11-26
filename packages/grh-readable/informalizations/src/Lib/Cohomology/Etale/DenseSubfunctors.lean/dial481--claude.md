---
{
  "module": "src/Lib/Cohomology/Etale/DenseSubfunctors.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Cohomology/Etale/DenseSubfunctors.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Cohomology/Etale/DenseSubfunctors.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Dense subfunctors, Mayer–Vietoris and partitions along idempotents

This file studies the cohomology Hⁿ(Y) = Extⁿ(ℤ[Y], F) of a set-valued functor Y on a category C
with coefficients in a functor F : C → Ab, where ℤ[Y] = `New.Variety.freeAb` Y. A map is an
equivalence for F (`New.Variety.IsCohomEquiv`) if it induces bijections on all Extⁿ(-, F). A
subfunctor U of Y is dense (`New.Variety.IsCohomDense`) if, over every point h_A → Y with h_A =
Hom(A,−), the inclusion of the preimage of U is an equivalence. The Mayer–Vietoris sequence, the
calculus of dense subfunctors and closed classes of functors are used to cut functors into pieces.
When ι attaches commutative rings to objects and `New.Variety.HasPartitions ι F` holds, partitions
along idempotents are dense. Locally constant coefficients on test rings satisfy
`New.Variety.HasPartitions`.

## Main definitions and results

* `New.Variety.mayer_vietoris_shortExact`: 0 → ℤ[U ∩ V] → ℤ[U] ⊕ ℤ[V] → ℤ[U ∪ V] → 0 is short exact.
* `New.Variety.IsCohomDense.isCohomEquiv`: the inclusion of a dense subfunctor is an equivalence.
* `New.Variety.IsClosedClass.freeAb_iSup`: if a closed class contains ℤ[V] for all V in a set of
  subfunctors closed under intersection, it contains ℤ[-] of their finite unions (Mayer–Vietoris).
* `New.Variety.HasPartitions.isCohomDense_partition`: for an idempotent `e`, the maps that kill `e`
  or `1 - e` are dense.
* `New.Variety.HasPartitions.hasZariskiDescent`: Zariski descent for rings `κ` that receive an
  injective map from `ι`, when any two elements of `κ` are comparable for divisibility after a cut
  along an idempotent of `ι`.
* `New.Variety.IsCohomDense.isCohomEquiv_of_fromPreimage`: a map is an equivalence if it is one over
  a dense subfunctor.

Notions from other files:
* `New.Variety.freeAb`: The functor sending a set-valued functor Y to ℤ[Y], whose value at A is the
  free abelian group on Y(A).
* `New.Variety.IsClosedClass`: a class of functors C → Ab that contains every zero functor and, for
  a short exact sequence whose first term lies in it, contains the middle term exactly when it
  contains the last.
* `New.Variety.HasPartitions`: Each idempotent e ≠ 1 of ι(A) has a `New.Variety.IsQuotientByElem`
  A → B, and ι(A) ≅ ι(B₁) × ι(B₂) via maps A → B₁, B₂ implies F(A) ≅ F(B₁) × F(B₂).

## Relation to the literature

Known; see `Lib.Cohomology.Etale.FilteredLimits` for sources.


 ## Mayer–Vietoris sequence and the calculus of dense subfunctors 

### `mayer_vietoris_shortExact`

 Mayer–Vietoris: for subfunctors U, V of Y, the sequence 0 → ℤ[U∩V] → ℤ[U] ⊕ ℤ[V] → ℤ[U∪V] →
0, with maps x ↦ (x,−x) and (x,y) ↦ x+y, is short exact. 

### `isCohomEquiv_iff_range`

 A monomorphism g : E → Y with image U is an equivalence for F exactly when the inclusion
U → Y is one. 

 ### Dense subfunctors 

### `isCohomEquiv`

 If the subfunctor U of Y is dense for F, then the inclusion U → Y is an equivalence: it
induces bijections H^n(Y,F) → H^n(U,F) for all n. 

### `preimage`

 The preimage of a dense subfunctor `U` of `Y` under `p : E ⟶ Y` is dense in `E`. 

### `of_top_le`

 A subfunctor U that is all of Y is dense for F. The hypothesis is stated as `⊤ ≤ U`. 

### `trans`

 Let U, V be subfunctors of Y. If V is dense in Y for F (`h`) and U ∩ V, the preimage of U in V,
is dense in V (`k`), then U is dense in Y. 

### `mono`

 A subfunctor that contains a dense subfunctor is dense. 

### `of_preimage_le`

 A subfunctor W of E that contains the preimage under p : E → Y of a dense subfunctor is
dense. 


## Closed classes of functors

Properties of closed classes of functors C → Ab (`New.Variety.IsClosedClass`), used to prove a
property of ℤ[Y] for many set-valued functors Y by cutting them up.


### `IsClosedClass.freeAb_of_bijective`

 Let P be a closed class and `g : E ⟶ Y` a map of set-valued functors that is bijective at every
object. If ℤ[E] lies in P, then so does ℤ[Y]. 

### `IsClosedClass.freeAb_iSup`

 Let P satisfy `New.Variety.IsClosedClass` and S be a set of subfunctors of Y closed under
intersection (`hS`), with ℤ[V] in P for all V in S (`hPS`). Then ℤ[⋃ U_i] is in P for every finite
family U_i in S. 

### `IsClosedClass.comap`

 If P is a closed class of functors C → Ab and Φ is an exact functor from functors D → Ab to
functors C → Ab, then the class of all N with Φ(N) in P is closed. 


## Relations among pull-backs from the relation locus

For finitely many maps `f i : W ⟶ Y` of set-valued functors and integers `c i`,
`New.Variety.relationLocus c f` is the subfunctor of the points `x` of `W` at which the formal sum
`∑ c i [f i x]` vanishes. If its inclusion into `W` is an equivalence for `F`, the same relation
holds among the pull-backs along the `f i` on cohomology.


### `relationLocus`

 For finitely many f_i: W → Y and integers c_i, the subfunctor of W of the points x ∈ W(A) with ∑
c_i [f_i(x)] = 0 in ℤ[Y(A)], expressed by `New.Variety.Cancels`. 

### `relationLocus_sum_eq_zero`

 On the relation locus, the sum `∑ c i • ℤ[f i]` vanishes. 

### `H.sum_map_eq_zero_of_relationLocus`

 For finitely many f_i: W → Y and integers c_i, if the inclusion into W of the locus where ∑
c_i [f_i(w)] = 0 is an equivalence for F, then ∑ c_i f_i^* x = 0 for every x in H^n(Y,F). 


## Partitions along idempotents and Zariski descent

Here `ι` attaches a commutative ring to each object of `C`, and `New.Variety.HasPartitions ι F` says
that objects can be cut along idempotents and that `F` respects products of two rings.


### `H.push_bijective_of_points`

 If `β : F ⟶ G` is bijective at every object `A` at which `Y` has a point (the hypothesis
`Y A → …` reads: if the set Y(A) is nonempty), it is bijective on the cohomology of `Y`: `H.push` is
the map Hⁿ(Y,F) → Hⁿ(Y,G) induced by β. 

### `pointMap_bijective_of_existsUnique`

 Let U be a subfunctor of Hom(A,−) and z: A → L a member of U. If every member of U factors
uniquely through z, then z represents U: the map Hom(L,D) → U(D) is bijective for every D. 

### `exists_dvd_idempotent_of_notMem`

 Let `f : E → B` satisfy `New.Variety.IsComparableRing`: any `a`, `b` in `B` have an idempotent
`e` of `E` with `a ∣ f e * b` and `b ∣ (1 - f e) * a`. Then an element `g` outside a maximal ideal
`m` divides some `f e` outside `m` with `e` idempotent. 

### `elemKillingMaps`

 For a functor `ι` from `C` to commutative rings and `e` in `ι A`, the subfunctor of `reprBy A`
(the maps out of `A`) of the maps `f : A ⟶ B` with `ι.map f e = 0`. 

### `preimage_pointMap_elemKillingMaps_sup`

 The preimage of the maps that kill `e` or `1 - e` under the point `k : A ⟶ B` is the subfunctor
of the maps out of `B` that kill `ι k e` or `1 - ι k e`. 

### `HasPartitions.eq_zero_of_zero_ring`

 Let F satisfy `New.Variety.HasPartitions` for the rings ι(A). If ι(B) is the zero ring whenever
Y(B) is non-empty, then H^n(Y,F) = 0 for all n. 

### `bijective_map_prod_map_of_idempotent`

 Let `e` be an idempotent of the ring `ι A`, let `π : A ⟶ B` kill `e` and `ρ : A ⟶ E` kill
`1 - e`, both onto on rings, with kernels in the ideals `(e)` and `(1 - e)`. Then
`x ↦ (ι π x, ι ρ x)` is bijective: the ring of `A` is the product of the rings of `B` and `E`. 

### `HasPartitions.isCohomDense_partition`

 Let F satisfy `New.Variety.HasPartitions` for the rings ι(A). For an idempotent e of ι(A), the
maps out of A that kill e or kill 1 − e form a dense subfunctor of `reprBy A` for F. 

### `HasPartitions.hasZariskiDescent`

 Zariski descent. Let `F` satisfy `New.Variety.HasPartitions` for the rings `ι`: idempotents of
ι(A) cut A into two pieces, and F of A is the product of F over the pieces. Let `η : ι ⟶ κ` be a map
of ring-valued functors such that (a) each `η.app A` is injective (has trivial kernel) and (b) any
`a`, `b` in `κ.obj A` have an idempotent `e` of `ι.obj A` with `a ∣ η e * b` and
`b ∣ (1 - η e) * a`. Then every subfunctor that is Zariski-locally everything for the rings `κ` (for
each point y ∈ Y(A) and maximal ideal m of κ(A), some g ∉ m such that every map A → B inverting g
sends y into U) is dense for `F` (`New.Variety.HasZariskiDescent`): pulled back to any point, its
inclusion is an equivalence for `F`. 

 ## Pull-back along composites and equivalences over dense subfunctors 

### `H.map_map`

 Pull-back along `v` and then along `u` is pull-back along `u ≫ v`. 

### `IsCohomDense.isCohomEquiv_of_fromPreimage`

 Let `W` be dense in `Y`. If `u : X ⟶ Y` restricts to an equivalence from the preimage of `W`
to `W`, then `u` is an equivalence. 


## Locally constant coefficients on test rings

`New.Variety.hasPartitions_locConstCoeff`: test rings (`New.Variety.IsTest`) can be cut along
idempotents, and the coefficient `New.Variety.locConstCoeff Λ` of locally constant functions
`Spec A → Λ` turns a product of two rings into a product of groups.


### `IsTest.isRadical_span_idempotent`

 In a test ring (a ring satisfying `IsTest`; the proof uses only that such a ring is reduced) the
ideal generated by an idempotent is radical. 

### `hasPartitions_locConstCoeff`

 Here `testIncl` is the inclusion of the full category of test rings (commutative rings
satisfying `IsTest`) into commutative rings. Test rings can be cut along idempotents, and locally
constant functions on the spectrum of a product of two test rings are pairs of such functions. 
