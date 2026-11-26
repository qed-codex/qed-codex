---
{
  "module": "src/Lib/General/Geometry/EtaleCharts.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Geometry/EtaleCharts.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Geometry/EtaleCharts.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Functors of points on algebras: open subfunctors, étale charts, atlases, charted schemes

A space over `k` is a functor `X` from commutative `k`-algebras (`New.Variety.CommAlg k`) to types.
`New.Variety.reprBy A` is the functor represented by `A`, and `New.Variety.pointMap y` is the map
`reprBy A ⟶ X` given by a point `y ∈ X(A)`. The file defines open subfunctors and separated
functors. It also defines étale charts `a`, which are algebras `R` with étale coordinates and a
point `y ∈ X(R)` embedding `Spec R` as an open subfunctor `a.locus`. For `k` Noetherian it develops
the calculus of charts and shows that an atlas yields a cover by pieces étale over tori.

## Main definitions and results

* `New.Variety.IsOpenSubfunctor`, `New.Variety.IsSeparatedFunctor`: open subfunctors and separated
  functors, each defined by an ideal attached to one or two points. `New.Variety.IsAffinelyCovered`:
  separated, and covered by one affine after restriction along a functor `ι : C ⥤ CommAlg k`.
* `New.Variety.EtaleChart`, `New.Variety.IsChartCovered`, `New.Variety.HasAtlas`: affine open charts
  with étale coordinates, and covers of the field-valued points by charts.
* `New.Variety.etale_polyEval_iff`: for `k` Noetherian and `R` of finite type, coordinates are étale
  iff maps lift uniquely along square-zero extensions once the values of the coordinates are lifted.
* `New.Variety.HasAtlas.exists_isCharting`: an atlas gives a subfunctor satisfying
  `New.Variety.IsCharting`. It is found as a finite union of charts whose coordinates are units,
  that is, of pieces étale over a torus.
* `New.Variety.Comparison.isClosedClass`: for a comparison of cohomologies on categories over `D`,
  the functors on `D` for which it is bijective form a closed class
  (`New.Variety.IsClosedClass`: contains `0` and, given a short exact sequence whose first term is
  in it, contains the second term iff the third).
* `New.Variety.IsCharted`: a scheme is charted if its functor of points has a subfunctor satisfying
  `New.Variety.IsCharting`.

Notions from other files:
* `New.Variety.IsPointwiseSurjective p`: the map `p : E ⟶ Y` of functors is surjective on `A`-points
  for every object `A`.
* `New.Variety.IsZariskiLocallyTop`: every point maps into the given subfunctor once some element
  outside any given maximal ideal of the algebra is made a unit.
* `CategoryTheory.Subfunctor.whisker`: for a subfunctor `U` of `Y` and `φ : C' ⥤ C`, the subfunctor
  `φ ⋙ U` of `φ ⋙ Y`.
* `New.Variety.restrictAlg k k'`: restriction of scalars, which regards a commutative `k'`-algebra
  as a `k`-algebra.

## Relation to the literature

Known; see `Lib.Cohomology.Etale.FilteredLimits` and `Lib.PadicComparison.ToricTower` for sources.



## Open and separated functors, étale charts and atlases

* `New.Variety.fieldLocus`: the subfunctor cut out by a condition on values in fields; examples are
  `New.Variety.offPoints` (avoiding given points) and `New.Variety.offDiagonal` (off the diagonal).


### `HodgeTest`

 A test for Hodge cohomology over k: a commutative k-algebra A and a finite index set ι,
standing for the pair (A, M) with M = A^ι. 

### `HodgeTest.baseAlg`

 The commutative `k`-algebra `A`. 

### `HodgeTest.Index`

 The index set of the standard basis of the free module `M = A^ι`. 

### `HodgeTest.fintypeIndex`

 The index set is finite. 

### `HodgeTest.linearOrderIndex`

 A chosen linear order on the index set. 

### `affineSpace`

 Affine d-space: the functor A ↦ A^d on k-algebras. 

### `unimodular`

 The subfunctor of affine d-space of vectors whose entries generate the unit ideal: the
complement of the origin. 

### `structureMap`

 The structure map k → A of a k-algebra A. 

### `fieldLocus`

 The subfunctor of points x in X(A) whose image in X(K) satisfies P for every map from A to a
field K. 

### `ComesFromPoints`

 A point `x` of `X(K)` comes from `s` if it is the image of some `k`-point `z` in `s` under the
structure map `k → K`. 

### `offPoints`

 For a set s of k-points of X, the subfunctor of points none of whose values in fields comes
from s. 

### `IsOpenSubfunctor`

 V is an open subfunctor of X: each x ∈ X(A) has an ideal I of A such that, for φ: A → B,
φ(x) ∈ V(B) iff φ(I)B = B. 

### `IsSeparatedFunctor`

 X is separated: for x, y in X(A) there is an ideal J of A such that φ: A → B makes x and y
equal exactly when φ kills J. 

### `IsSeparatedFunctor.exists_ideal`

 For two points of `X(A)`, an ideal `J` of `A` such that a map `φ : A → B` makes them equal
  exactly when `φ` kills `J`. 

### `IsAffinelyCovered`

 `X` is separated and, after restriction along `ι`, covered by one affine: there are a
`k`-algebra `B` and a point `y` of `X(B)` such that, for every object `c`, each point of `X(ι c)` is
the image of `y` under some map `B → ι c`. 

### `HasCoveringPoints`

 Every k-algebra B with a map to some ι(c) has a map y : B → ι(c'), for some c', such that
`pointMap y`, the map from the functor on `C` represented by c' to `ι ⋙ reprBy B`, is surjective on
points: each map B → ι(c'') is ι(f) ∘ y for some f : c' → c''. 

### `HasCoveringPoints.exists_surjective_point`

 Each `k`-algebra with a map to some `ι(c)` has a map to some `ι(c')` through which, followed
  by some `ι(f)` with `f : c' ⟶ c''`, every map to an `ι(c'')` factors. 

### `offDiagonal`

 The complement of the diagonal in X × X: pairs of points whose values in every field are
distinct. 

### `EtaleChart`

 A chart of X: a k-algebra R (`coordRing`) with d étale coordinates (`coordinate`) and a point y
(`point`) in X(R) that embeds Spec R as an open subfunctor. 

### `EtaleChart.coordRing`

 The `k`-algebra of functions on the chart. 

### `EtaleChart.point`

 The point of `X` over `R`, that is, the map `Spec R → X`. 

### `EtaleChart.coordinate`

 The `d` coordinates on the chart. 

### `EtaleChart.etale`

 The coordinates make `R` étale over the polynomial ring in `d` variables. 

### `EtaleChart.injective`

 The map `Spec R → X` is injective on `A`-points, for every `A`. 

### `EtaleChart.isOpenSubfunctor`

 The image of `Spec R → X` is an open subfunctor. 

### `IsSquareZero`

 φ: A → B is a square-zero extension: surjective, with kernel of square zero. 

### `EtaleChart.locus`

 For a chart a of X, with ring R = a.coordRing and point y = a.point, the open subfunctor that is
the image of Spec R → X, φ ↦ φ(y). 

### `EtaleChart.mono_pointMap`

 The map `Spec R → X` given by the point of a chart is a monomorphism. 

### `EtaleChart.eq_comp_of_map_point_eq`

 Let `a` be a chart of `X` with ring `a.coordRing` and point `a.point ∈ X(a.coordRing)`. A map
`χ` out of `a.coordRing` is the composite `ψ ≫ φ` if it sends `a.point` to the image under `φ` of
the point given by `ψ`. 

 ### Properties of open subfunctors and of points 

### `map_eq_top_iff_forall_isField`

 The image of the ideal `I` of `A` under `φ : A ⟶ B` generates the unit ideal of `B` exactly when
no map from `B` to a field kills it. 

### `IsOpenSubfunctor.fieldLocus_le`

 If `V` is open, a point lies in `V` as soon as all its values in fields do. Here
`fieldLocus V` is the subfunctor of points whose values in fields lie in `V`. 

### `IsOpenSubfunctor.exists_basicOpen`

 If the image of `x ∈ X(A)` under a map `φ` to a field `B` lies in the open subfunctor `V` of
`X`, there is an `f ∈ A`, non-zero in `B`, such that `x` maps into `V` wherever `f` becomes a
unit. 

### `isOpenSubfunctor_fieldLocus`

 The subfunctor cut out by a condition `P` on values in fields is open if, for each point `x`,
`P` fails exactly on the zero locus of an ideal `J`. 

### `IsOpenSubfunctor.mem_of_isSquareZero`

 A point `x ∈ X(A)` lies in the open subfunctor `V` of `X` if its image under a square-zero
extension `φ` (a surjection whose kernel has square zero) does. 

### `IsOpenSubfunctor.inf`

 The intersection of two open subfunctors is open; its ideal is the product. 

### `IsOpenSubfunctor.whisker_restrictAlg`

 An open subfunctor stays open after base change to a `k`-algebra `E`. 

### `map_map_structureMap`

 The images of a `k`-point are compatible with maps of `k`-algebras. 

 ### Open subfunctors of separated functors, and covers 

### `isOpenSubfunctor_offPoints`

 If `X` is separated and `s` is a finite set of `k`-points of `X`, then `offPoints s`, the
subfunctor of points none of whose values in fields comes from `s`, is open. 

### `mem_offDiagonal_of_ne`

 If `X` is separated, two distinct points with values in a field `A` form a pair in the
complement of the diagonal: their images in every field over `A` are distinct. 

### `isZariskiLocallyTop_of_open_cover`

 Let `Θ : C ⥤ CommAlg k` and `T ⊆ Θ ⋙ X` be such that each field point of `X` lies in an open
`O` whose restriction along `Θ` is contained in `T`. Then `T` is locally everything: for `y` in
`X (Θ c)` and `m` maximal in `Θ c`, some `f ∉ m` has `y` in `T` wherever `f` becomes a unit. 

### `IsChartCovered`

 Every field-valued point of X lies in some chart, an affine open with d étale coordinates. 

### `IsChartCovered.exists_chart`

 Each point of `X` with values in a field lies in the locus of some chart. 

### `HasAtlas`

 X is separated and has finitely many charts, each with exactly d étale coordinates, that
contain every field-valued point. 

### `HasAtlas.exists_finite_charts`

 Finitely many charts contain every field-valued point of `X`. 


## Calculus of étale charts and covers by pieces étale over tori

* `New.Variety.EtaleChart.exists_eq_iff_coordinate_eq`: two points of a chart are equal iff their
  coordinates agree and a fixed element of `a.coordRing ⊗ a.coordRing` maps to a unit.


### `instance [IsSeparatedFunctor X] [IsSeparatedFunctor Y] : IsSeparatedFunctor (X ⊗ Y)`

 The product of two separated functors is separated. 

### `CommAlg.toAway`

 The localisation map A → A[1/g] of k-algebras. 

### `CommAlg.exists_toAway_comp_iff`

 A map `φ : A ⟶ B` factors through `toAway g`, the localization map `A ⟶ A[1/g]`, iff it sends
`g` to a unit. 

### `EtaleChart.fieldLocus_eq_of_le_locus`

 A subfunctor `V` of the image `a.locus` of a chart `a` that is open in `a.locus` is cut out by
its values in fields: a point whose values in fields lie in `V` lies in `V`. 

### `EtaleChart.isOpenSubfunctor_of_le_locus`

 A subfunctor `V` of the image `a.locus` of a chart `a` is open in `X` if it is open in
`a.locus`. 

 ### The lifting criterion for étale coordinates 

### `polyEval`

 The ring homomorphism k[X_i] → R sending X_i to x_i. 

### `EtaleChart.polyAlgebra`

 The ring of a chart a as an algebra over the polynomial ring k[X_1, …, X_d], with X_i sent
to the i-th coordinate of a. 

### `instance : Smooth k a.coordRing`

 The ring of a chart is smooth over `k`. 

### `map_aeval_of_forall_eq`

 If a map φ : R → A of k-algebras sends each x i to b i, it sends the value of a polynomial at x
to its value at b. 

### `existsUnique_lift_of_etale_polyEval`

 Let x₁, …, x_d be elements of a k-algebra R for which k[X_i] → R, X_i ↦ x_i, is étale.
Along a square-zero extension π: B → A of k-algebras each ζ: R → A lifts uniquely once lifts
b_i of the ζ(x_i) are prescribed. 

### `etale_polyEval_of_existsUnique_lift`

 Let x₁, …, x_d be elements of a k-algebra R of finite type, k Noetherian. If each ζ: R → A lifts
uniquely along square-zero extensions B → A once lifts of the ζ(x_i) are prescribed, then
k[X_i] → R, X_i ↦ x_i, is étale. 

### `etale_polyEval_iff`

 Infinitesimal criterion: for k Noetherian, R of finite type and finitely many x_i ∈ R,
k[X_i] → R, X_i ↦ x_i, is étale iff each ζ: R → A lifts uniquely along square-zero
extensions B → A of k-algebras once lifts of the ζ(x_i) are prescribed. 

### `EtaleChart.lift_unique`

 Over a Noetherian ring k, two maps out of the ring of an étale chart are equal if they agree
modulo a square-zero ideal and agree on the coordinates. 

 ### Shrinking a chart 

### `EtaleChart.restrict`

 Over a Noetherian ring k, let a be a chart with ring a.coordRing and point a.point, and φ a map
from a.coordRing to an algebra R of finite type that sends a.point to y. If y embeds Spec R as an
open subfunctor, this is the chart on R with point y and the images of the coordinates of a. 

### `EtaleChart.away`

 For k Noetherian, a chart a of X and an element g of its ring R, the chart on R[1/g] with the
images of the point and coordinates of a. 

### `EtaleChart.mem_locus_away`

 Over a Noetherian ring k, the point given by φ: a.coordRing → B lies in the part of the chart a
where g is inverted iff φ(g) is a unit. 

### `IsOpenSubfunctor.exists_mem_locus_and_point_mem`

 Charts can be shrunk, for k Noetherian: if U ⊂ X is open, charts of dimension d cover the points
of X in fields, and x ∈ U(A) with A a field, then x lies in the image of a chart of dimension d
whose point lies in U. 

 ### Products and intersections of charts 

### `tensorInl`

 For commutative k-algebras A and B, the k-algebra map A → A ⊗_k B, a ↦ a ⊗ 1, as a morphism in
`New.Variety.CommAlg` k. 

### `tensorInr`

 For commutative k-algebras A and B, the k-algebra map B → A ⊗_k B, b ↦ 1 ⊗ b, as a morphism in
`New.Variety.CommAlg` k. 

### `existsUnique_tensor_desc`

 Two maps φ: A → R and ψ: B → R of k-algebras come from a unique map
A ⊗_k B → R. 

### `range_pointMap_prod`

 Let `a` be a chart of `X` and `b` a chart of `Y`. Their points give a point of `X × Y` over
`a.coordRing ⊗ b.coordRing`. Its image in `X × Y` is the intersection of the preimages of `a.locus`
and `b.locus` under the two projections. 

### `EtaleChart.prod`

 For k Noetherian and charts a of X and b of Y, the chart of X×Y on a.coordRing ⊗ b.coordRing,
with coordinates x_i⊗1 and 1⊗y_j, where x and y are the coordinates of a and b. 

### `EtaleChart.mem_locus_prod_iff`

 The pair `(x, y)` lies in the image of the product of the charts `a` and `b` iff `x` lies in the
image of `a` and `y` in that of `b`. 

### `HasAtlas.isChartCovered`

 If `X` has an atlas of dimension d, charts of dimension d cover the field-valued points of
`X`. 

### `IsChartCovered.prod`

 Let k be Noetherian. If charts of dimension d cover the field-valued points of `X` and charts
of dimension n cover those of `Y`, then products of such charts, of dimension d + n, cover the
field-valued points of `X × Y`. 

### `EtaleChart.exists_locus_eq_inf`

 Over a Noetherian ring k, if `X` is separated, the intersection of the images of two charts `a`
and `b` is the image of a chart with as many coordinates as `b`. 

 ### Differentials, equality of points, preimages of charts 

### `EtaleChart.nonempty_basis_kaehler`

 The Kähler differentials over k of the ring of a chart with d étale
coordinates have a basis of d elements. 

### `EtaleChart.exists_eq_iff_coordinate_eq`

 Let a be a chart with ring R, point y and coordinates x_i. There is e ∈ R ⊗ R such that, for
every map χ: R ⊗ R → C, the images of y in X(C) along r ↦ χ(r ⊗ 1) and r ↦ χ(1 ⊗ r)
agree exactly when χ(e) is a unit and χ kills x_i ⊗ 1 - 1 ⊗ x_i for each i. 

### `EtaleChart.range_pointMap_eq_preimage_locus`

 For a monomorphism u: Y → X and a point y of Y over the ring of a
chart a with u(y) the point of a, the image of y is the preimage under u of the image of a. 

### `EtaleChart.comap`

 For u: Y → X injective on points and a chart a of X whose point is u(y), the chart of Y with the
same ring and coordinates and the point y. 

### `IsChartCovered.comap`

 Let u: Y → X be a monomorphism with open image, over a Noetherian ring k. If charts of dimension
d cover the field-valued points of X, the same holds for Y. 

 ### Covering by pieces étale over tori 

### `IsCharting`

 Two properties of a subfunctor `V` of `X`.
(a) `V` is locally everything: for each `y ∈ X(A)` and maximal ideal `m` of `A` there is an
`a ∉ m` such that `y` maps into `V` along every `A → B` that makes `a` a unit.
(b) `ℤ[V]` lies in every class `P` of functors to abelian groups that satisfies
`New.Variety.IsClosedClass` and contains `ℤ[Hom(R, -)]` for the ring `R` of each chart of `X` (of
any dimension) whose coordinates are all units, that is, étale over a torus. 

### `EtaleChart.etale_polyEval_coordinate_add_ite`

 Over a Noetherian ring k, the coordinates of a chart stay étale when those with index in `S` are
shifted by 1. 

### `IsClosedClass.freeAb_iSup_locus`

 Let k be Noetherian, `X` separated and `u` a finite family of charts of `X` whose coordinates
are units. Let `P` be a closed class of functors to abelian groups (it contains `0` and, given a
short exact sequence whose first term is in it, contains the second term iff the third). If `P`
contains the free abelian functor `ℤ[Hom(b.coordRing, -)]` for each chart `b` whose coordinates are
units, it contains `ℤ[⋃ (u p).locus]`. 

### `HasAtlas.exists_isCharting`

 Let `k` be Noetherian and let `X` be a functor on commutative `k`-algebras with an atlas of
dimension `d` (`HasAtlas d X`): `X` is separated and has finitely many charts, each with exactly `d`
étale coordinates, that together contain every field-valued point. Then some subfunctor `V` of `X`
satisfies `IsCharting`. (a) For each `y ∈ X(A)` and maximal ideal `m` of `A` there is an `a ∉ m`
such that `y` maps into `V` along every `A → B` that makes `a` a unit. (b) The free abelian group
functor `ℤ[V]` lies in every class of functors to abelian groups that satisfies `IsClosedClass` and
contains `ℤ[Hom(R, -)]` for the ring `R` of each chart of `X`, of any dimension, whose coordinates
are units. 


## Closed classes of bijective comparisons and charted schemes

The functors `N` (first arguments of `Extⁿ`) on which a comparison of cohomologies is bijective form
a closed class, as used in the definition of charting subfunctors; a scheme is charted if it has
such a subfunctor. A comparison `c` (`New.Variety.Comparison`) is a functor `φ : C' ⥤ C` with a map
`φ ⋙ F ⟶ F'`. `c.IsBijective α` says that `Extⁿ(N, F) → Extⁿ(N', F')` along `α : N' ⟶ φ ⋙ N` is
bijective for all `n`. Both sides lie over a category `D` through `ψ`, `ψ'` and `η : ψ' ⟶ φ ⋙ ψ`.


### `Comparison.isClosedClass`

 Let the comparison `c` consist of a functor `c.functor : C' ⥤ C` and a map of coefficients from
`F` on `C` to `F'` on `C'`. The functors `N : D ⥤ Ab` for which the maps
`Extⁿ(ψ ⋙ N, F) → Extⁿ(ψ' ⋙ N, F')` induced by `c` and `η` are bijective for all n form a closed
class: it contains `0` and, given a short exact sequence whose first term is in it, contains the
second term iff the third. 

### `Comparison.IsBijectiveOn`

 The comparison `c` is bijective on the set-valued functor `P` on `D`: the maps
`Hⁿ(ψ ⋙ P, F) → Hⁿ(ψ' ⋙ P, F')` induced along `η` are bijective for all `n`. 

### `IsCharted`

 The scheme `Y` over `R` is *charted* over the `R`-algebra `k`: the functor of points of `Y` on
`k`-algebras has a subfunctor `V` with `New.Variety.IsCharting V`. 

### `IsCharted.exists_isCharting`

 The functor of points of `Y` has a subfunctor `V` with `New.Variety.IsCharting V`. 
