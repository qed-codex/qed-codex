---
{
  "module": "src/Lib/Cohomology/ProperBaseChange/PlaceSpace.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Cohomology/ProperBaseChange/PlaceSpace.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Cohomology/ProperBaseChange/PlaceSpace.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The space of places of residue fields and its properness over the base

Spaces are functors from rings to sets (`New.Variety.PointFunctor`). For `s : Z ⟶ reprBy D` and a
point `x ∈ Z(C)`, the ring map under `x` is `baseRingMap s x : D ⟶ C`. The space of places is a form
of the Riemann–Zariski space. It is used to cover a proper functor `Z` over `D`.

A place of a `D`-algebra `P` is a prime `q` of `P` together with a valuation ring of `κ(q)` over
`D`. For `α : D ⟶ P`, the ring `T = prodValuationRing α` is the product of these valuation rings.
Each `t ∈ P` is a ratio `a t / b t` in it, with `a = numerator` and `b = denominator`. The space of
places `W` of a valuative lift `z`, with `z.point ∈ Z(T)`, has as points over `C` the classes of
maps `f : T → C`. Two maps are identified if they give the same point `Z.map f z.point` of `Z(C)`
and the same ratios `(f (a t) : f (b t))`.

* `New.Variety.IsProperOver`: properness, as a closed diagonal and a valuative criterion.
* `New.Variety.ResiduePlace.placeSpace`: the space of places `W`.
* `New.Variety.ResiduePlace.exists_isLocalHom_eq_projHom_comp`: a point of `W` in a local ring comes
  from one place.
* `New.Variety.ResiduePlace.isProperOver_placeSpace`: the space of places is proper over `D`.

Notions from other files:
* `New.Variety.reprBy D`: the functor `Hom(D, −)` represented by `D`.

## Relation to the literature

Known; see `Lib.Cohomology.ProperBaseChange.Theorem` for sources.


 ### Proper functors 

### `IsProperOver`

 The functor `Z` on rings, with structure map `s : Z ⟶ reprBy D`, is proper over `D`: its
diagonal is closed, and it satisfies a valuative criterion with one ring `T` and one point
`a ∈ Z(T)` serving all valuation rings of algebraically closed fields (which includes
quasi-compactness). 

### `IsProperOver.diagonal_closed`

 The diagonal is closed: for points `x`, `y` over `C`, some ideal `I` of `C` is killed exactly
  by the maps `C ⟶ C'` that make `x` and `y` equal. 

### `IsProperOver.valuative_cover`

 For one ring `T` and one point `a` over it, each point in an algebraically closed field `K`
  that maps `D` into a valuation ring `O` of `K` is the image of `a` under some `T → O ⊆ K`. 

### `IsProperOver.ext_of_jointly_injective`

 Two points of a proper functor over `C` are equal if they become equal along a jointly
injective family of ring maps `C ⟶ K j`. 

### `IsProperOver.injective_map_valuationSubring`

 For `Z` proper over `D` and a valuation subring `U` of a field `F`, the map `Z(U) → Z(F)` is
injective. 

### `ResiduePlace`

 For `α : D → P`, a place is a prime `q` of `P` together with a valuation ring `O` of the residue
field `κ(q)` that contains the image of `D`. 

### `ResiduePlace.prime`

 A prime ideal of `P`. 

### `ResiduePlace.valuationSubring`

 A valuation ring of the residue field of that prime. 

### `ResiduePlace.base_mem`

 The valuation ring contains the image of `D`. 

### `prodValuationRing`

 For α: D → P, the product of the valuation rings O over all places (q, O) of
`New.Variety.ResiduePlace`. 

### `projHom`

 For a place j, the projection ring homomorphism from the product of all the valuation rings
to the valuation ring of j. 

### `PlaceField`

 For a place j=(q,O), the residue field κ(q) of the prime q of P. 

### `toFieldProd`

 The componentwise inclusion ∏ O → ∏ κ(q), both products over all places (q, O). 

### `denominator`

 For t∈P and a place (q,O), the element of O equal to 1 if the image of t in κ(q) lies in O,
and its inverse otherwise. 

### `numerator`

 For t∈P and a place (q,O), the element of O given by the image of t in κ(q) times the
denominator. 

### `isCoprime_denominator_numerator`

 For `f : prodValuationRing α ⟶ C` and `t ∈ P`, `f (denominator t)` and `f (numerator t)` are
coprime. 

### `fractionGraph`

 For `f : ∏ O → C`, the subring of pairs `(t, c)` in `P × C` with the following property: there
are `r`, `r'` in the product of the valuation rings such that `f r` is a unit, `r · t = r'` in
`∏ κ(q)`, and `f r · c = f r'`. 

### `ValuativeLift`

 For `ξ ∈ Z(P)`: a point of `Z` over the product of the valuation rings of all places that agrees
with `ξ` over the product of the residue fields. It comes with three facts: `Z` is proper over `D`,
`P` is absolutely flat, and all residue fields of `P` are algebraically closed. 

### `ValuativeLift.point`

 A point of `Z` over the product of the valuation rings of all places. 

### `ValuativeLift.map_point_eq`

 Over the product `∏ⱼ κ(j.prime)` of residue fields, indexed by the places `j`, the point
  agrees with `ξ`; the map on the right is the algebra map `P → ∏ⱼ κ(j.prime)`,
  `t ↦ (t mod j.prime)_j`. 

### `ValuativeLift.isProperOver`

 `Z` is proper over `D`. 

### `ValuativeLift.absolutely_flat`

 Each `a ∈ P` satisfies `y * a * a = a` for some `y ∈ P`. 

### `ValuativeLift.isAlgClosed_residueField`

 Every residue field of `P` is algebraically closed. 

### `mem_fractionGraph`

 A pair `(t, c)` lies in the graph of `f` iff `f (numerator t) = f (denominator t) * c`. 

 ### The space of places and its loci 

### `placeSpace`

 The space of places of a valuative lift `z` of `ξ ∈ Z(P)`. With `T` the product
`prodValuationRing (baseRingMap s ξ)` of the valuation rings of all places, its points over `C` are
classes of maps `f : T ⟶ C`. Two maps are identified when they send the point of `z` to the same
point of `Z(C)` and give the same ratios `f (numerator t) : f (denominator t)` for all `t ∈ P`. 

### `placeSpaceMap`

 The map from the space of places of `z` to `Z` that sends the class of `f` to `f z ∈ Z(C)`. 

### `exists_algebraMap_residueField_comp_eq`

 A ring map `g : P ⟶ F` to a field factors through the residue field of some prime `q` of
`P`. 

### `placeGraph`

 For a point `x` of the space of places over `C`, the subring of `P × C` of pairs `(t, c)` such
that `x` gives `t` the finite value `c`. For any representative `f` of `x`, these are the pairs of
`New.Variety.ResiduePlace.fractionGraph f`, that is, `f (numerator t) = f (denominator t) * c`. This
does not depend on the choice of `f`. 

### `placeGraph_map`

 If `x` gives `t` the value `c`, then the image of `x` under `k : C ⟶ C'` gives `t` the value
`k c`. 

### `killingPlaces`

 For an ideal I of P, the subfunctor of the space of places W of points that give every t ∈ I
the value 0. 

### `finiteValueSubring`

 For a maximal ideal q of P and a place y killing q, the subring of κ(q) = P/q formed by the
images of the t ∈ P finite at y, that is, of those `t` with a value at `y`: some
`(t, c) ∈ placeGraph y`. 

### `placesFiniteOn`

 For an ideal J of D and a subring B of κ(q), the subfunctor of places vanishing on q that
are finite on B and whose structure map from D kills J. 

### `placeGraph_unique`

 A point `x` of the space of places gives an element `t ∈ P` at most one finite value: if
`(t, c)` and `(t, d)` both lie in `New.Variety.ResiduePlace.placeGraph x`, then `c = d`. 

### `isRelAffine_killingPlaces`

 For an ideal `I` of `P`, the inclusion of the places that give every `t ∈ I` the value `0`
(`New.Variety.ResiduePlace.killingPlaces z I`) into the space of places is relatively affine. 

### `mem_finiteValueSubring_iff`

 Let `q` be a maximal ideal of `P` and let the class of `f : prodValuationRing → C` be a place
that kills `q`. Then the place is finite at the residue of `t ∈ P` in `κ(q)` iff `f (denominator t)`
is a unit. 

### `mem_fractionGraph_projHom`

 Through the place `j`, an element `t` with residue in the valuation ring of `j` has as value the
image of that residue. 

### `projHom_mem_killingPlaces`

 A point that factors through the place `j` kills the prime of `j`. 

### `isRelAffine_placesFiniteOn`

 For an ideal `J` of `D` and a subring `B` of `κ(q)`, the inclusion of the places that kill the
maximal ideal `q` of `P`, are finite on `B` and whose structure map kills `J`
(`New.Variety.ResiduePlace.placesFiniteOn z J B`) into the places that kill `q` is relatively
affine. 

### `baseRingMap_mem_placeGraph`

 For `d ∈ D`, the point `x` of the space of places gives the image `baseRingMap s ξ d` of `d` in
`P` the value `baseRingMap (placeSpaceMap z ≫ s) x d`, the image of `d` under the structure map
of `x`. 

 ### Points in local rings, and properness 

### `exists_isLocalHom_eq_projHom_comp`

 Let `z` be a valuative lift of `ξ ∈ Z(P)`. This is a point of `Z` over `prodValuationRing`, the
product of the valuation rings of all places `(q, O)`, and it agrees with `ξ` over the product of
the residue fields. Here a place is a prime `q` of `P` together with a valuation ring `O` of `κ(q)`
containing the image of `D` under `baseRingMap s ξ`. Let `R` be a local ring and `x` a point over
`R` of the space of places of `z`, that is, a class of maps `prodValuationRing → R`; then there is a
place `(q, O')` with two properties. (a) There is a local map `φ : O' → R`. (b) For every valuation
ring `O ⊆ O'` of `κ(q)` containing the image of `D`, `x` is the class of the composite
`prodValuationRing → O ⊆ O' → R` of the projection, the inclusion and `φ`. 

### `isProperOver_placeSpace`

 Let `z` be a valuative lift of `ξ ∈ Z(P)`: `Z` is proper over `D`, `P` is absolutely flat, the
residue fields of `P` are algebraically closed, and the point of `z` agrees with `ξ` over the
product of the residue fields. Then the space of places of `z` is proper over `D`. 

### `exists_valuationSubring_eq_finiteValueSubring`

 Let `q` be a maximal ideal of `P` and `x` a point of the space of places in a local ring `R`
that kills `q`. There are a valuation ring `V` of `κ(q)` over `D` and a map `φ : V → R` such that
`V` is the subring of `κ(q)` on which `x` is finite, and `x` is the class of
`prodValuationRing → O ⊆ V → R` for every valuation ring `O ⊆ V` over `D`. 

### `finiteValueSubring_mem_or_inv_mem`

 Let `x` be a point of the space of places in a local ring that kills the maximal ideal `q`. The
subring of `κ(q)` on which `x` is finite is a valuation ring. 

### `exists_eq_projHom_comp_of_le_finiteValueSubring`

 Let `x` be a point of the space of places in a local ring `R` that kills the maximal ideal `q`,
and `O` a valuation ring of `κ(q)` over `D` inside the subring on which `x` is finite. Then `x` is
the class of `prodValuationRing → O → R` for some map `O → R`. 
