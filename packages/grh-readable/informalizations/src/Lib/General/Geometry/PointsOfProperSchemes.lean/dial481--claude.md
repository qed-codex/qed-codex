---
{
  "module": "src/Lib/General/Geometry/PointsOfProperSchemes.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Geometry/PointsOfProperSchemes.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Geometry/PointsOfProperSchemes.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Functors of points of proper schemes: closed loci, atlases and descent of relations

Schemes over `Spec R` are studied through their functors of points. The functor of points of a
proper scheme is proper and separated. On comparable rings (`New.Variety.IsComparableRing`), its
points all come from one affine scheme. If the scheme is smooth of relative dimension `d` after base
change to `k`, it also has an étale atlas.

## Main definitions and results

* `New.Variety.exists_ideal_le_ker_iff_factors`: for a closed immersion `i : Z ⟶ X` and a point `a`
  of `X` with values in `S`, one ideal `I` of `S` describes the ring maps `γ : S →+* B` along which
  `a` lands in `Z`, namely those that kill `I`. It is finitely generated if `i` is of finite
  presentation.
* `New.Variety.exists_locallyOfFiniteType_forall_factors`: a proper scheme `X` over `Spec R`
  receives a morphism `Spec T ⟶ X` from one affine scheme, locally of finite type, through which
  every point with values in a comparable ring (`New.Variety.IsComparableRing`) factors.
* `New.Variety.isProperOver_pointsToBase`: the functor of points of `X` over `R` satisfies
  `New.Variety.IsProperOver`.
* `New.Variety.isSeparatedFunctor_algPointsOf`: for an `R`-algebra `k` and a proper scheme `W` over
  `Spec R`, the points of `W` with values in `k`-algebras form a separated functor
  (`New.Variety.IsSeparatedFunctor`).
* `New.Variety.hasAtlas_algPointsOf`: if moreover `W` is smooth of relative dimension `d` after base
  change to `k`, the functor has an atlas of dimension `d`.
* `New.Variety.isAffinelyCovered_algPointsOf`: on rings satisfying `New.Variety.IsComparableRing`,
  one affine scheme surjects onto the points of a proper `W`.
* `New.Variety.exists_hom_of_rel` builds a homomorphism A → B of commutative group objects over S
  from a homomorphism f : W → B and a relation between T-points of W and of A. The relation is
  stable under pull-back and subtraction, compatible with f, and defined on an fpqc cover of A.

Notions from other files:
* `New.Variety.IsComparableRing`, applied to the identity map of a ring: for any a, b in the ring
  there is an idempotent e with a ∣ e * b and b ∣ (1 - e) * a.
* `New.Variety.pointsToBase`: For a morphism s: X → Spec R, the map from the functor of points of X
  to the functor A ↦ Hom(R, A) that sends x ∈ X(A) to the ring map R → A of s∘x.
* `New.Variety.HasAtlas`: X is separated and has finitely many charts, each with exactly d étale
  coordinates, that contain every field-valued point.
* `New.Variety.IsOpenSubfunctor`: V is an open subfunctor of X: each x ∈ X(A) has an ideal I of A
  such that, for φ: A → B, φ(x) ∈ V(B) iff φ(I)B = B.
* `New.IsAdditive`: The morphism f : A → B of commutative group objects is a homomorphism: composing
  with f is additive on U-points for every U.

## Relation to the literature

Known; see `Lib.Cohomology.Etale.FilteredLimits` and `Lib.PadicComparison.HodgeTate.PeriodMap` for
sources.


 ## Morphisms of spectra over a base and algebra maps 

### `map`

 For an R-algebra homomorphism φ: C→D, the induced morphism Spec D → Spec C of schemes over
Spec R. 

### `map_bijective`

 Every morphism `Spec D ⟶ Spec C` over `Spec R` is induced by exactly one `R`-algebra map
`C → D`. 

 ## The ideal cutting out the locus of a closed subscheme 

### `le_ker_iff_factors`

 A ring map `γ : S →+* B` kills the ideal `I` if and only if `Spec γ` factors through
`Spec (S ⧸ I) ⟶ Spec S`. 

### `exists_ideal_le_ker_iff_factors`

 For a closed immersion i: Z → X and a: Spec S → X, there is an ideal I of S, finitely
generated if i is of finite presentation, such that a∘Spec γ factors through Z exactly when
γ: S → B kills I. 

 ## Properness of the functor of points of a proper scheme 

### `New.Variety.exists_locallyOfFiniteType_forall_factors`

 If X is proper over Spec R, there is a morphism a: Spec T → X, locally of finite type, through
which every morphism Spec O → X factors, for all rings O whose identity map satisfies
`New.Variety.IsComparableRing`: any two elements are comparable for divisibility after a partition
by an idempotent. 

### `New.Variety.isProperOver_pointsToBase`

 If `s : X ⟶ Spec R` is a proper morphism of schemes, then the functor of points `A ↦ X(A)` with
its structure map `pointsToBase s` is proper over `R` (`New.Variety.IsProperOver`). The locus where
two points agree is cut out by an ideal. There are a ring `T` and a point `a ∈ X(T)` such that each
point of `X` in an algebraically closed field `K` that maps `R` into a valuation ring `O` of `K` is
the image of `a` under some `T → O ⊆ K`. 


## Separatedness, affine covers and étale atlases for points

The passage from schemes to functors of points: for a scheme `W` over `Spec R` and an `R`-algebra
`k`, `New.Variety.algPointsOf k R W` sends a `k`-algebra `A` to `W(A)`.

* `New.Variety.isOpenSubfunctor_of_landsIn`: the points that land in an open subset form an open
  subfunctor.


### `exists_ideal_preimage_eq_top_iff`

 Every open subset `V` of `Spec A` has an ideal `I` of `A` such that, for a ring map
`φ : A → B`, the morphism `Spec φ` lands in `V` iff `φ(I)` generates the unit ideal of `B`. 

### `isOpenSubfunctor_of_landsIn`

 Let `t` send points of `W` naturally to points of a scheme `Z` (`ht`). If a subfunctor `U` of
the points of `W` consists of the points whose image lands in an open subset `V` of `Z`, then `U`
is an open subfunctor. 

### `left_comp_hom`

 A point of `W` with values in a `k`-algebra `A` lies over the composite
`Spec A ⟶ Spec k ⟶ Spec R`, so it is also a point of the base change of `W` to `k`. 

### `PointsIn.map_left`

 The image of a point `x` under `φ : A → B` has underlying morphism `Spec φ ≫ x`. 

### `exists_hom_specMap_eq`

 A ring map `u : A → B` of `k`-algebras whose spectrum commutes with the structure maps to
`Spec k` induces the same morphism of spectra as some map of `k`-algebras `A → B`. 

### `isSeparatedFunctor_algPointsOf`

 If `W` is proper over `Spec R`, its functor of points on `k`-algebras is separated: the locus
where two points of `W` with values in `A` agree is cut out by an ideal of `A`. 

### `exists_etale_coordinates_of_smooth`

 Let `f : Y ⟶ Spec k` be smooth of relative dimension `d`. Each point `z` of `Y` lies in the
image of an open immersion `Spec A ⟶ Y` over `k`, where the `k`-algebra `A` is étale over the
polynomial ring in `d` variables. 

### `exists_etaleChart_of_smooth`

 Suppose the base change `Wₖ` of `W` to `k` is smooth of relative dimension `d`, and `t` sends
each point `x` of `W` with values in a `k`-algebra `A` (`PointsIn`) to the corresponding `A`-point
of `Wₖ`, naturally in `A` and compatibly with the two projections. Then each `z` in `Wₖ` has an open
neighbourhood `V` and an `EtaleChart` of `algPointsOf k R W`. Such a chart is a `k`-algebra `S` with
`d` étale coordinates together with a point `y` of `W` in `S` that embeds `Spec S` as an open
subfunctor. Its `locus` (the points `φ(y)` for `φ : S → A`) consists exactly of the `x` with `t x`
landing in `V` (`LandsIn`). 

### `hasAtlas_algPointsOf`

 If `W` is proper over `Spec R` and its base change to `k` is smooth of relative dimension `d`,
the functor of points of `W` on `k`-algebras has an atlas of dimension `d`: it is separated, and
finitely many charts with `d` étale coordinates contain all its field-valued points. 

### `isAffinelyCovered_algPointsOf`

 Let `ι` be a functor to `k`-algebras whose values are comparable rings
(`New.Variety.IsComparableRing`). If `W` is proper over `Spec R`, its functor of points is
separated, and one point with values in a `k`-algebra `B` gives, along the maps `B → ι c`, all the
points of `W` with values in each `ι c` (`New.Variety.IsAffinelyCovered`). 


## Homomorphisms from relations total on an fpqc cover

`New.Variety.exists_hom_of_rel` uses that representable functors are sheaves for the fpqc topology.


### `New.Variety.exists_hom_of_rel`

 fpqc descent: let f : W → B be a homomorphism of commutative group objects over S and R a
relation between T-points of W and of A. Suppose R is stable under pull-back and under subtraction,
and x ≫ f = 0 whenever x is related to 0. If every member of an fpqc cover P of A is related to
some point of W, then there is a homomorphism F : A → B with y ≫ F = x ≫ f whenever x is related
to y. 
