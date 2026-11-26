---
{
  "module": "src/Lib/Cohomology/Hodge/FixedPointFormula.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Cohomology/Hodge/FixedPointFormula.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Cohomology/Hodge/FixedPointFormula.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Reduced coincidences and the fixed point formula in Hodge cohomology

Let `W`, `X` be functors from `k`-algebras to sets (`New.Variety.CommAlg k ⥤ Type 1`), standing for
schemes, and let `u c : W ⟶ X` be two maps. A coincidence is a point `x` of `W` with `c x = u x`.
The file proves the fixed point formula in Hodge cohomology `Hdg^d(W)`, that is
`HodgeH (freeAb.obj W) d`, computed on square-zero extensions `A ⊕ M`: a pulled-back diagonal class
is a sum of point classes `New.Variety.pointClass d w` over the coincidences, weighted by Jacobian
determinants. If `k` is algebraically closed, `X` is separated, every `k[ε]`-valued coincidence is
constant and finitely many charts of `W` contain all field-valued coincidences, then the
coincidences form a finite set of rational points, which carry these local terms.

## Main definitions and results

* `New.Variety.ConstIfCoincident`, `New.Variety.IsCoincidenceSet`: reduced coincidences, and a
  finite set of rational points that lists them all.
* `New.Variety.HasJacobianRatio`: the local term, the determinant of `(t du - dc) (du - dc)⁻¹`.
* `New.Variety.IsTangentPoly.hasJacobianRatio_eval_div`: a tangent polynomial `P` with `P 1 ≠ 0`
  gives this term as `P t / P 1`; by `New.Variety.IsTangentPoly.constIfCoincident` the coincidences
  at that point are then reduced.
* `New.Variety.scaledGraph`: the graph of `(u, c)` twisted by the scaling of `M` by `t` in the first
  factor.
* `New.Variety.exists_diagonal_local_terms`: the class `δ` of the diagonal, pulled back along this
  twisted graph, is `∑ n w • pointClass d w` over the coincidences `w` of `u` and `c`, where `n w`
  is the determinant of a matrix `N` with `t du - dc = N (du - dc)` at `w`
  (`New.Variety.HasJacobianRatio`).
* `New.Variety.IsPointSum.cup_pointClass`: the external product of the class of a point of `X` and
  the class of a point of a curve is the class of the product point.

Notions from other files:
* `New.Variety.HodgeH`: Hodge cohomology: for a functor N from k-algebras to abelian groups, Ext^q
  from (A, M) ↦ N(A ⊕ M) to (A, M) ↦ ⋀_A M, in functors on pairs.
* `New.Variety.symbolClass`: The Grothendieck symbol [dT/T] in Hdg^d(𝔸^d, 𝔸^d ∖ 0); its pull-back
  along a tuple f of functions is the symbol [df/f].
* `New.Variety.IsPointSum`: A relative class has multiplicity n z at each z in s: on some chart
  containing z it restricts to n z times the symbol [dg / g] of functions g that cut out z.
* `New.Variety.IsTangentPoly`: at a point `y ∈ W(k)`, the tangent map `dc` on the tangent space of
  dimension `d` is injective, `du = dc ∘ B`, and `P t = P 0 * det (1 - t B)`.
* `New.Variety.HasAtlas`: X is separated and has finitely many charts, each with exactly d étale
  coordinates, that contain every field-valued point.
* `New.Variety.offPoints`: for a set s of k-points of X, the subfunctor of the points none of whose
  values in fields comes from s.
* `New.Variety.exteriorAlg`, `CategoryTheory.Functor.mulPairing`: the exterior algebra ⋀_A M of a
  pair (A, M), and the pairing given by its multiplication (the wedge product of coefficients in the
  cup product).
* `New.Variety.freeAb.prod`: for set-valued functors X, Y, the map ℤ[X × Y] → ℤ[X] ⊗ ℤ[Y], [(x,
  y)] ↦ [x] ⊗ [y].

## Relation to the literature

Known result: the fixed point formula in Hodge cohomology, with local terms computed by
Grothendieck symbols. Here the setting is characteristic 0 and smooth separated varieties with a
finite atlas, with cohomology taken as Ext of functors. The class of the diagonal and Künneth
surjectivity for X×X are not proved here; they come from `exists_diagonal_class` and `kunneth` in
other files. Here the point classes are multiplied for a product with a curve, and the pull-back of
the diagonal class along reduced coincidences is given as a weighted sum of point classes. Source:
Stacks Project, tags 0BEC (Künneth) and 0G82 (Gysin maps); A. Chatzistamatiou, K. Rülling, Higher
direct images of the structure sheaf in positive characteristic, Algebra & Number Theory 5 (2011)
693-775, sections 2-3; V. Srinivas, Gysin maps and cycle classes for Hodge cohomology, Proc. Indian
Acad. Sci. Math. Sci. 103 (1993) 209-247; Hartshorne, Residues and Duality (1966) III.9 for the
symbol.

See also `Lib.Cohomology.WoodsHole` and `Lib.Cohomology.PointClass.LinearIndependence`.



## Reduced coincidences and their Jacobian determinants

A chart `New.Variety.EtaleChart d X` is an affine open of `X` with `d` étale coordinates, given by a
ring `R` and a point of `X` in `R`; its locus `New.Variety.EtaleChart.locus` is the open subfunctor
of the points that come from `R`. Tangent vectors are `k[ε]`-points; `New.Variety.SqZeroExt.fst` is
the map `k ⊕ M → k` (so `k[ε] → k`) and `New.Variety.structureMap` the structure map of a
`k`-algebra.


### `ConstIfCoincident`

 For two maps `u c : W ⟶ X`: if the `k[ε]`-valued point `x` of `W` is a coincidence of `u` and
`c`, then it is constant, that is, the image of its base point under `k → k[ε]`. 

### `IsCoincidenceSet`

 The finite set `s` of `k`-points of `W` is the set of coincidences of the maps `u c : W ⟶ X`,
and these are reduced: every `k[ε]`-valued coincidence is constant, every point of `s` is a
coincidence, and every field-valued coincidence comes from a point of `s`. 

### `exists_isCoincidenceSet`

 Let `k` be algebraically closed, `X` separated (`IsSeparatedFunctor X`) and `u c : W ⟶ X` two
maps. Suppose that every `k[ε]`-valued coincidence of `u` and `c` is constant (`h_red`) and that
finitely many charts `a i` of `W`, affine opens with `d` étale coordinates, contain all
field-valued coincidences (`h_cover`). Then there is a finite set `s` of `k`-points of `W` with
`IsCoincidenceSet u c s`: the coincidences are the points of `s`, and they are reduced. 

### `HasJacobianRatio`

 For a scalar `t` of `k`, the number `n` is `det ((t du - dc) (du - dc)⁻¹)` at `w`: in every
chart `A` of `X` that contains `c w` there is a matrix `N` of determinant `n` with
`t du v - dc v = N (du v - dc v)` for all tangent vectors `v` at `w`, where `ξ` gives the
coordinates of a tangent vector in `A`. Here `X` is a functor on `E`-algebras, and `u`, `c` map
`W` to `X` read on `k`-algebras (`restrictAlg E k ⋙ X`). 

### `jetTangent`

 The tangent vector of a jet `v`, a point of `W` with values in `k ⊕ T*`, in the direction
`φ ∈ T`: the image of `v` under the map `k ⊕ T* → k[ε]` given by evaluation at `φ`. 

### `EtaleChart.tangent_mem_range_of_jet`

 Let `v` be a jet of `X` with values in `k ⊕ T*`, where `T` has dimension `d`, whose base point
lies in a chart `A` with `d` coordinates, and whose tangent vectors in distinct directions are
distinct. Then every tangent vector at the base point is one of these, and the coordinates of the
tangent vector in the direction `φ` are `D φ` for a linear isomorphism `D : T ≃ kᵈ`. Here `X` is
a functor on `E`-algebras, read on `k`-algebras through `restrictAlg E k`. 

### `EtaleChart.mem_range_jetTangent_of_injective`

 Let `v` be a jet of `X` with values in `k ⊕ T*`, where `T` has dimension `d`, whose base point
lies in a chart `A` and whose tangent vectors in distinct directions are distinct. Then every
`k[ε]`-point `w` of `X` with the base point of `v` is a tangent vector `jetTangent v φ` of `v`. 

### `EtaleChart.exists_linearEquiv_coordinate_jetTangent`

 Let `v` be a jet of `X` with values in `k ⊕ T*`, where `T` has dimension `d`, whose base point
lies in a chart `A` and whose tangent vectors in distinct directions are distinct. Then there is a
linear isomorphism `D : T ≃ kᵈ` such that every `α` representing `jetTangent v φ` in the chart has
`ε`-parts of its coordinates equal to `D φ`. 

### `IsTangentPoly.hasJacobianRatio_eval_div`

 Let every field-valued point of `W` lie in a chart with `d` coordinates. Let `P` be a tangent
polynomial of `c`, `u` at `w`, that is `P t = P 0 * det (1 - t (dc)⁻¹ du)`, with `P 1 ≠ 0`. Then for
every `t : k`, `HasJacobianRatio u c d t (P t / P 1) w` holds: in every chart of `X` containing
`c w` there is a matrix `N` of determinant `P t / P 1` with `t du v - dc v = N (du v - dc v)` for
all tangent vectors `v` at `w`. 

### `IsTangentPoly.constIfCoincident`

 Let every field-valued point of `W` lie in a chart with `d` étale coordinates. Let `P` be a
tangent polynomial of `c`, `u` at the `k`-point `w`, that is, the algebraic form of
`P t = P 0 * det (1 - t (dc)⁻¹ du)` on the tangent space at `w`, and suppose `P 1 ≠ 0`. Then every
`k[ε]`-valued point `x` of `W` above `w` that is a coincidence of `u` and `c` is constant. 


## Local terms of the diagonal class at simple coincidences

The pull-back of the diagonal class along the twisted graph `scaledGraph t u c` is a sum of point
classes over the coincidences of `u` and `c`. Near one coincidence the computation is the
transformation law `New.Variety.symbolClass_transformation` for Grothendieck symbols.


### `scaledGraph`

 The graph of the pair `(u, c)` twisted by `t` in the first factor. For a scalar `t` of `k`
and maps `u c : W ⟶ X`, it is the natural map `W(A ⊕ M) → X(A ⊕ M) × X(A ⊕ M)` on square-zero
extensions, `w ↦ (u (s_t w), c w)`, where `s_t : A ⊕ M → A ⊕ M` is `(a, m) ↦ (a, t m)`. 

### `constMap`

 For a `k`-point `z` of `X`, the constant map `W ⟶ X` that sends every `A`-point of `W` to
the image of `z` in `X(A)`. 

### `symbolClass_baseChange`

 The universal symbol `symbolClass` in degree `d` is compatible with a change of the base
field: for a field `E` of characteristic `0` over `k`, the base change to `E` of the symbol over
`k` is the symbol over `E`. 

### `preimage_lift_le_preimage_scaledGraph`

 Let `U` be an open subfunctor of `X × X` and `x` a point of `W` with values in a square-zero
extension `A ⊕ M`. If `(u x, c x)` lies in `U`, then so does `scaledGraph t u c x`: the two pairs
agree modulo `M`, and membership in an open subfunctor is decided modulo a square-zero ideal. 

### `ker_le_of_cuts_out_coincidences`

 Let `s` be the set of coincidences of `u` and `c` (`IsCoincidenceSet`), `a` a chart of `W`
with ring `a.coordRing`, and `ζ : a.coordRing ⟶ k` a `k`-point of `a` that lies in `s` and is the
only point of `s` in `a`. Let `I` be an ideal of `a.coordRing` that cuts out the coincidences in
`a`: a map `α` from `a.coordRing` kills `I` exactly when the point `α` of `W` is a coincidence. Then
`I` contains the ideal `ker ζ` of the point `ζ`. 

### `map_comp_map_point_eq_app_map_of_map_point_eq`

 Carrying a chart expression along a map of algebras. Let `A` be a chart of `X` and `v` a map
from `W` to `X`. If `χ` expresses the point `v y` in the coordinates of `A`, then `χ` followed by
`α : B ⟶ C` expresses the point `v (α y)`. 

### `offPoints_whisker_le_preimage_scaledGraph`

 Off the coincidences, the twisted graph avoids the diagonal. Let every field-valued coincidence
of `u` and `c` come from a point of the finite set `s`. Then `scaledGraph t u c` maps the
square-zero points of the complement `offPoints s` of `s` into the complement `offDiagonal X` of
the diagonal. 

### `apply_tangent_sub_sum_eq_zero`

 The tangent step of the transformation law. `φ`, `ψ` write `u`, `c` on the chart `a` in the
coordinates `xᵢ` of `A`, `f` is their difference, `ν` a section of
`a.coordRing ⊕ a.coordRing ^ d → a.coordRing`, and `t du - dc = Q (du - dc)` at
`w = W.map ζ a.point` (as in `HasJacobianRatio`). Then `ζ` kills
`t (ν (φ xᵢ))ⱼ - (ν (ψ xᵢ))ⱼ - ∑ l, Q i l (ν (f l))ⱼ` for all `i`, `j`. 

### `map_pointMap_map_scaledGraph_eq_smul_symbolClass`

 The multiplicity at one coincidence. On `O`, the class `δ` (relative to the complement of the
diagonal) is the symbol of the coordinate differences of the chart `A`; `lift u c` maps the chart
`a` of `W`, with a point `ζ`, into `O`; `φ`, `ψ` write `u`, `c` on `a`; their difference `f` cuts
out `w = W.map ζ a.point` and generates `ker ζ`; `m` is the Jacobian ratio at `w`. Then on `a`,
relative to the complement of `w`, `δ.baseChange` (`δ` read on `E`-algebras through
`restrictAlg k E`) pulls back along `scaledGraph t u c` to `m • [df / f]`. 

### `exists_diagonal_local_terms`

 The local terms of the diagonal class. If `X` has an atlas of dimension `d`, some `δ` in
`Hdg^d(X × X)` works for every field `E` of characteristic `0` over `k`, every separated `W` over
`E` with field points in charts of dimension `d`, every `t : E` and all `u c : W ⟶ X` with reduced
coincidences `s` and `n w = det((t du − dc)(du − dc)⁻¹)` at `w ∈ s`. (a) Some class relative to
`offPoints s` (points avoiding `s`) is `n w • [dg/g]` near each `w`, where the functions `g` cut out
`w`. (b) `δ.baseChange`, the class `δ` over `k` read on `E`-algebras through `restrictAlg k E`,
pulls back to `∑ n w • pointClass d w` along `scaledGraph t u c`, the map `w ↦ (u (s_t w), c w)` on
square-zero extensions, where `s_t(a, m) = (a, t m)`. 

### `exists_diagonal_map_scaledGraph_eq_sum_pointClass`

 The fixed point formula. If `X` has an atlas of dimension `d`, some `δ` in `Hdg^d(X × X)` pulls
back, as `δ.baseChange` (`δ` read on `E`-algebras through `restrictAlg k E`), along
`scaledGraph t u c` to `∑ w ∈ s, n w • pointClass d w` whenever the coincidences of `u`, `c` are
reduced and form `s`, with Jacobian ratio `n w` at `w ∈ s`. 

### `exists_diagonal_pointClass`

 The classes of the `k`-points of `X`, where `X` has an atlas of charts with `d` étale
coordinates (`HasAtlas d X`). There is a degree-`d` Hodge class `δ` on `X × X` such that for every
`k`-point `z`: (a) some class with support `z` has multiplicity `1` at `z`; (b) the class of `z` is
the pull-back of `δ` along `x ↦ (z, x)`; (c) for every separated `W` whose field-valued points lie
in charts with `d` coordinates, and every `u : W ⟶ X` whose coincidences with the constant map at
`z` form the reduced finite set `s`, the pull-back of the class of `z` along `u` is the sum of the
classes of the points of `s`. 

### `exists_isPointSum_singleton`

 If `X` has an atlas of dimension `d`, then for every `k`-point `z` of `X` some class of degree
`d` relative to the complement of `z` has multiplicity `1` at `z`. 

### `exists_map_lift_constMap_eq_pointClass`

 If `X` has an atlas of dimension `d`, the class of every `k`-point `z` of `X` is the pull-back
of one class `δ` on `X × X` along `x ↦ (z, x)`. 

### `map_pointClass_eq_sum_of_isCoincidenceSet`

 Let `X` have an atlas of dimension `d`, `z` a `k`-point of `X`, and `u : W ⟶ X` a map from a
separated `W` covered by charts of dimension `d` whose fibre over `z` is reduced and is the finite
set `s` (`IsCoincidenceSet (constMap z) u s`). Then `u` pulls the class of `z` back to the sum of
the classes of the points of `s`. 

### `map_constMap_eq_of_forall_affine_eq`

 Let `z`, `z'` be two `k`-points of `X` at which every map from `X` to the affine line takes
the same value. Then every Hodge class `x` on `X`, of any degree `a`, has the same restriction to
`z` and to `z'`: the same pull-back along the constant maps from the one-point functor `𝟙_`. 

### `pointClass_eq_of_functions_eq`

 Two `k`-points of `X` at which all maps from `X` to the affine line take the same value have
the same class. 


## The product of a point class with a point class of a curve

`New.Variety.IsPointSum.cup_pointClass`: in Hodge cohomology (`New.Variety.HodgeH`) the external
product (`New.Variety.cup`) of the classes `New.Variety.pointClass` of a point of `X` and a point of
a curve `Y` is the class of the product point. On a product chart this is
`New.Variety.symbolClass_succ`, the product rule for the symbols `[dT / T]`; excision carries it to
`X × Y`.


### `New.Variety.pull_cup_along_pair`

 Let `x` be a class of degree `d` on `X` relative to `U`, `y` a class of degree `1` on `Y`
relative to `W`, and `s`, `t` points of `X` and `Y` with values in `R` that map `T` into `U` and
`S` into `W`. The pull-back of the external product of `x` and `y` along the point `(s, t)` of
`X × Y` is the external product of the pull-backs of `x` along `s` and `y` along `t`, pulled back
along the diagonal of `Spec R` (`lift (𝟙 _) (𝟙 _)`). 

### `New.Variety.IsPointSum.cup_pointClass`

 Over a field `k` of characteristic `0`, let `X` and `Y` have atlases of dimensions `d` and `1`.
Let `z` be a `k`-point of `X × Y`. Take the classes of `z.1` and `z.2` and multiply them with the
wedge product of coefficients. Pull the product back along `ℤ[X × Y] → ℤ[X] ⊗ ℤ[Y]`. The result is
the class of `z`, in degree `d + 1` of the Hodge cohomology of `X × Y`. 
