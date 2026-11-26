---
{
  "module": "src/Lib/Cohomology/PointClass/LinearIndependence.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Cohomology/PointClass/LinearIndependence.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Cohomology/PointClass/LinearIndependence.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The Hodge–Tate map keeps classes of points on a projective variety linearly independent

Let `k` be an algebraically closed field with a map to `Q̄_p`, and let `Y` be a projectively
embedded scheme whose points over `k`-algebras (`New.Variety.algPointsOf`; `PointsIn Y A` is the set
of points of `Y` with values in a `k`-algebra `A`, and `structureMap` is the map `k ⟶ A`) are
covered by charts with `d` étale coordinates (`New.Variety.HasAtlas`). The Hodge–Tate map
`New.Variety.hodgeTateMap d` sends the distinct classes of `k`-points of `Y` to linearly independent
elements.

* `New.Variety.linearIndepOn_hodgeTateMap_pointClass`: the main result.
* `New.Variety.exists_map_separating_class`: for a `k`-point `z₀` and finitely many other points, a
  map `j` to `Y` whose pull-back kills the classes that differ from that of `z₀` and keeps the
  Hodge–Tate image of the class of `z₀` non-zero.

The map `j` is an open part of the graph of a linear projection of the component of `z₀` to
projective space, chosen by Noether normalisation (`New.Variety.exists_generic_chart`,
`New.Variety.exists_etale_projection`). Over a suitable `k`-point `Q` of projective space the
projection is étale and its fibre consists of points with the class of `z₀`. Pull-back along the
projection is injective and the Hodge–Tate image of the class of `Q` is non-zero, so the Hodge–Tate
image of the class of `z₀` is non-zero too.

Notions from other files:
* `New.Variety.pointClass d z`: the class of the `k`-point `z` in the Hodge cohomology of degree
  `d`.
* `New.Variety.IsCoordsWithUnit L x v`: `v` is a vector of homogeneous coordinates of the point `x`
  for the embedding `L`, and some entry of `v` is a unit.
* `New.Variety.CutsOutLocus.IsHomogeneousSolution k g v`: every homogeneous polynomial over `k` that
  vanishes at `g` vanishes at `v`, that is, `v` lies on the cone cut out at `g`.
* `New.Variety.CutsOutLocus.IsNoetherNormalization Λ g`: the values `evalForms Λ g` of the linear
  forms `Λ j` satisfy no non-zero homogeneous relation, and the cone of `g` is integral over them.
* `New.Variety.EtaleChart d X`: a `k`-algebra `c.coordRing` with `d` étale coordinates and a point
  `c.point` of `X` with values in `c.coordRing`, whose images `c.locus` (the points
  `X.map φ c.point`) make its spectrum an open subfunctor of `X`.

## Relation to the literature

Known result: Hodge–Tate images of point classes are non-zero and detect degrees of zero-cycles.
This file proves only that the Hodge–Tate images of the distinct point classes are linearly
independent, without duality or a trace map. Non-vanishing on projective space is imported
(`New.Variety.projSpace.hodgeTateMap_pointClass_ne_zero`) and carried to a smooth projective variety
by transfer along a finite linear projection. Source: Faltings, p-adic Hodge theory, JAMS 1 (1988)
(compatibility with traces and cycle classes); for transfer, Suslin–Voevodsky, Singular homology of
abstract algebraic varieties, Invent. Math. 123 (1996), §§4–6.


### `New.Variety.IsGenericChart`

 The chart `c` with coordinates `w`, embedded in a field by `κ`, is a generic point of the
component of the `k`-point `z` (coordinates `v`), with a Noether normalisation `Λ` of `κ ∘ w`. 

### `New.Variety.IsGenericChart.injective`

 `κ` is injective. 

### `New.Variety.IsGenericChart.isCoordsWithUnit_point`

 `w` are homogeneous coordinates of the point of the chart, with a unit entry. 

### `New.Variety.IsGenericChart.evalForms_zero`

 The form `Λ 0` takes the value `1` at `w`. 

### `New.Variety.IsGenericChart.isNoetherNormalization`

 `Λ` is a Noether normalisation of the image of `w` in the field. 

### `New.Variety.IsGenericChart.isCoordsWithUnit_z`

 `v` are homogeneous coordinates of `z`, with a unit entry. 

### `New.Variety.IsGenericChart.isHomogeneousSolution`

 `z` lies on the cone of the generic point. 

### `New.Variety.exists_generic_chart`

 Let `k` be a field of characteristic zero and an `R`-algebra, and let `Y` be a scheme over
`Spec R` with an atlas of dimension `d` on its points (`HasAtlas`), projectively embedded by the
line bundle `L` with sections indexed by the finite type `ι` (`IsProjEmbedding`, which includes
that `Y → Spec R` is proper). For every `k`-point `z` of `Y` there are an étale chart `c`, a field
extension `F` of `k` with a map `κ : c.coordRing ⟶ F`, coordinates `w : ι → c.coordRing`, linear
forms `Λ 0`, …, `Λ n` over `k` in the variables `ι` and coordinates `v : ι → k` of `z` with
`IsGenericChart L z c κ w Λ v`: the map `κ` is a generic point of a component of `Y` containing
`z`, and `Λ` is a Noether normalisation of `κ ∘ w`. 

### `New.Variety.injective_aeval_of_isNoetherNormalization`

 If `Λ` is a Noether normalisation of the image of `w` in a field and `Λ 0` is `1` at `w`, then
the values of `Λ 1`, …, `Λ n` at `w` are algebraically independent. 

### `New.Variety.exists_fibre_mem_of_isOpenSubfunctor`

 The fibre of a linear projection over a general point lies in a given open set. Let `L` embed
`Y` (over `Spec R`) in projective space, and let the field point `η` of `Y` have `L`-coordinates
`κ ∘ w`, where `κ` embeds `A` in a field. Let `Λ 0` be `1` at `w`, and let every non-zero element of
`A` be a root of a polynomial over `k[X₁, …, Xₙ]` (`Xᵢ` acting as `Λ i` at `w`) with non-zero
constant term. If an open `V` contains `η`, then for some `q`, every field point `x` of `Y` lies in
`V` when its `L`-coordinates `v` lie on the cone of `κ ∘ w` (homogeneous polynomials vanishing at
`κ ∘ w` vanish at `v`) and satisfy `Λ v = [1 : q]`. 

### `New.Variety.EtaleChart.apply_mem_of_coords_mem`

 Let `w` be coordinates, with a unit entry, of the point of the chart `c`, and `κ` a map of its
ring to a field. The values `κ r` lie in any intermediate field `M` that contains every `κ (w i)`:
the point of `c` over the field comes from a point of `c` over `M`. 

### `New.Variety.IsEtaleProjection`

 `U` is an étale projection chart for `Λ` on the cone of `g`: its étale coordinates are the
values of `Λ 1`, …, `Λ n`, and it contains the field points of the cone over `[1 : q]`. 

### `New.Variety.IsEtaleProjection.isCoordsWithUnit`

 `w'` are homogeneous coordinates of the point of `U`, with a unit entry. 

### `New.Variety.IsEtaleProjection.isHomogeneousSolution`

 `w'` lies on the cone cut out by the homogeneous equations of `g`. 

### `New.Variety.IsEtaleProjection.evalForms_zero`

 The form `Λ 0` takes the value `1` at `w'`. 

### `New.Variety.IsEtaleProjection.coordinate_eq`

 The étale coordinates of `U` are the values of `Λ 1`, …, `Λ n` at `w'`. 

### `New.Variety.IsEtaleProjection.mem_locus`

 `U` contains the field points on the cone of `g` that `Λ` sends to `[1 : q]`. 

### `New.Variety.exists_etale_projection`

 Let `k` have characteristic zero and let `Y` over Spec `R` be embedded in projective space by
`L`. Let `c` be an étale chart of `Y` (a `k`-algebra `c.coordRing` with `d` étale coordinates and a
point of `Y` with values in it that embeds Spec `c.coordRing` as an open subfunctor). Let `κ` embed
`c.coordRing` in a field, let `w` be homogeneous coordinates for `L` of the chart's point with some
entry a unit, and let `Λ` be a Noether normalisation of `κ ∘ w` with `Λ 0` equal to `1` at `w`. Then
`n = d`, and there is an `n`-dimensional chart `U` whose étale coordinates are the values of `Λ 1`,
…, `Λ n` (at coordinates `w'` of its point) and which contains the field points of the cone of
`κ ∘ w` over some point `[1 : q]` (`IsEtaleProjection`). 

### `New.Variety.pointClass_eq_of_isHomogeneousSolution`

 Points on one component have one class. Let `g` be the coordinates of a point `η` over a
field, `k` algebraically closed. Let `z₀` be a `k`-point with coordinates `v₀` on the cone of `g`,
and `y` a `k`-point whose image over a non-zero `k`-algebra `K` has coordinates `v` on that cone.
Then `y` and `z₀` have the same class, since global functions are constant on the cone. 

### `New.Variety.map_pointClass_eq_sum`

 Let `W` be separated and covered by charts of dimension `d`. If `s` is the finite reduced fibre
of `u : W ⟶ X` over the `k`-point `x` (`IsCoincidenceSet` of `u` and the constant map at `x`: the
points of `s` lie over `x`, every field point over `x` comes from `s`, and every `k[ε]`-point over
`x` comes from its `k`-point), then `u` pulls the class of `x` back to the sum of the classes of the
points of `s`. 

### `New.Variety.isChartCovered_graph_projection`

 Let `Γ` be the graph of the projection of `Y` to projective space by the linear forms `Λ`:
the pairs `(x, [Λ(v)])` where `v` are coordinates of `x` with a unit entry and the values `Λ(v)`
generate the unit ideal (`hΓ`). If the first projection `Γ → Y` is a monomorphism, then `Γ` is
covered by charts of the dimension `d` of `Y`. 

### `New.Variety.isOpenSubfunctor_fieldLocus_eq_imp_mem`

 Let `u` and `u'` be maps to a separated `X` and `V` an open subfunctor of `W`. The points `x` of
`W` whose values in fields lie in `V` wherever `u` and `u'` agree (the `fieldLocus` of this
condition: points all of whose images in fields satisfy it) form an open subfunctor. 

### `New.Variety.mem_offPoints_of_isHomogeneousSolution`

 A point `x` with coordinates `v` on the cone of `g`, the coordinates of a field point `η`,
avoids the `k`-points of `T` whose class differs from that of `z₀`, if `z₀` has coordinates `v₀` on
that cone: no value of `x` in a field comes from such a point. 

### `New.Variety.map_pointClass_eq_sum_of_injective`

 Pull-back along a map `u` injective on points sends the class of `x` to the sum of the classes
of the points of `s`, if `u` sends the points of `s` to `x` and every field point over `x` comes
from a point of `s`. 

### `New.Variety.map_pointClass_app_of_injective`

 Pull-back along a map `u` that is injective on points sends the class of the image `u y` of a
`k`-point `y` to the class of `y`. 

### `New.Variety.map_pointClass_eq_zero_of_injective`

 Pull-back along a map `u` that is injective on points kills the class of a `k`-point `z` over
which `u` has no field point. 

### `New.Variety.hodgeTateMap_ne_zero_of_isCoincidenceSet`

 Let `O` be separated and covered by charts of dimension `n`, with a map `proj` to projective
space `ℙⁿ` such that pull-back along `proj` is injective on the `genericCoeff` classes of degree
`n + n` (`h_inj`). If the fibre of `proj` over a `k`-point `Q` is a finite reduced set `t` of points
whose classes all equal `c`, then the Hodge–Tate map does not kill `c`. 

### `New.Variety.isSeparatedFunctor_of_injective`

 A functor with a map `j` to a separated functor `X` that is injective on points is separated. 

### `New.Variety.exists_map_separating_class`

 Let `k` be algebraically closed of characteristic zero with an embedding in Q̄_p, and let `Y` be
a scheme over Spec `R`, embedded in projective space by `L` and having an atlas of étale charts of
dimension `d`. Let `pointClass d z` denote the class of a `k`-point `z` of `Y` in degree-`d` Hodge
cohomology. Then for a `k`-point `z₀` and a finite set `T` of `k`-points, there are a functor `W`
from `k`-algebras to sets and a map `j : W ⟶ Y` with two properties: pull-back along `j` kills the
class of every point of `T` whose class differs from that of `z₀`, and the Hodge–Tate map
`hodgeTateMap d` does not kill the pull-back of the class of `z₀`. 

### `New.Variety.linearIndepOn_hodgeTateMap_pointClass`

 Let `k` be an algebraically closed field with a map to `Q̄_p` and `Y` a projectively embedded
scheme over `R` whose points in `k`-algebras have an atlas of dimension `d`. Then the Hodge–Tate
map of weight `d` sends the distinct classes of `k`-points to linearly independent elements. 
