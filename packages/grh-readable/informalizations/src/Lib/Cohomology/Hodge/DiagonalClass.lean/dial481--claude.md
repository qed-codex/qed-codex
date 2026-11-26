---
{
  "module": "src/Lib/Cohomology/Hodge/DiagonalClass.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Cohomology/Hodge/DiagonalClass.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Cohomology/Hodge/DiagonalClass.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The Hodge class of the diagonal of a variety with an atlas, with its local description

The class of the diagonal in Hodge cohomology, for a functor of points `X` on `k`-algebras.

* `New.Variety.exists_diagonal_class`: if `k` has characteristic zero and `X` has an atlas of
  dimension `d`, there is a class `δ` of degree `d` on `X × X` relative to the complement of the
  diagonal that is, near the diagonal, the symbol `[df / f]` of the differences of chart
  coordinates. It is glued from such symbols.

`New.Variety.HasAtlas d X`: `X` is separated and its field points lie in finitely many affine charts
`New.Variety.EtaleChart d X` with `d` étale coordinates. `HodgeH (relFreeAb U) q` is Hodge
cohomology relative to the subfunctor `U`. `New.Variety.IsLocalSymbol ξ y P g m` says three things:
`g` cuts out `P` at the point `y`; `y` maps the part of `Spec R` off the preimage of `P` into `U`;
and `ξ` pulls back along `y` to `m • [dg / g]`. Here `[dg / g]` is the pull-back of
`New.Variety.symbolClass` along `g`. `P` is a predicate on points, not the subfunctor that `ξ` is
relative to; that subfunctor is the implicit `U`. For the diagonal class, `P` is the diagonal
`x.1 = x.2`, while `δ` is relative to its complement.

Notions from other files:
* `New.Variety.CutsOutLocus`: The elements `f i` of `R` cut out the locus where the point `x` of
  `X(R)` satisfies `P`: a map `α : R ⟶ C` kills every `f i` exactly when the image of `x` in `X(C)`
  satisfies `P`.
* `New.Variety.IsOpenSubfunctor`: V is an open subfunctor of X: each x ∈ X(A) has an ideal I of A
  such that, for φ: A → B, φ(x) ∈ V(B) iff φ(I)B = B.
* `New.Variety.EtaleChart`: A chart of X: a k-algebra R with finitely many étale coordinates and a
  point y in X(R) that embeds Spec R as an open subfunctor, its `locus`.
* `New.Variety.offDiagonal`: The complement of the diagonal in X × X: pairs of points whose values
  in every field are distinct.
* `New.Variety.relFreeAb`: For a subfunctor U of a set-valued functor V, the functor to abelian
  groups ℤ[V]/ℤ[U].
* `New.Variety.HodgeH`: Hodge cohomology: for a functor N from k-algebras to abelian groups, Ext^q
  from (A, M) ↦ N(A ⊕ M) to (A, M) ↦ ⋀_A M, in functors on pairs.

## Relation to the literature

Known; see `Lib.Cohomology.Hodge.FixedPointFormula` for sources.


### `EtaleChart.isCohomEquiv_relFreeAb_map_pointMap`

 Excision to a chart. Let `c` be a chart of `X` whose image `c.locus` is `W`, and `U` a
subfunctor of `X`. Pull-back along the point of `c`, seen as a point of `W`, is a bijection on Hodge
cohomology relative to `U`: classes on `W` relative to `U` are determined by, and may be prescribed
through, their pull-back to `c.point`. `pointMap` sends `χ : c.coordRing ⟶ B` to the image of
`c.point`; `IsCohomEquiv hodgeCoeff` (on functors whiskered by `HodgeTest.sqZeroExt`) means
bijective in every degree. 

### `EtaleChart.subsingleton_hodgeH_offDiagonal`

 Let `c` be a chart of `X × X` on which the differences of the first `d` and the last `d`
coordinates cut out the diagonal. Then the Hodge cohomology of its image relative to the
complement of the diagonal vanishes in degrees below `d`. 

### `IsDiagonalSymbolOn`

 On the subfunctor `O` of `X × X`, the class `δ` is the symbol of the differences of the
coordinates of the chart `a`: every point of `O` is a pair of points `φ`, `ψ` of the chart, the
differences `f i = φ (a.coordinate i) - ψ (a.coordinate i)` cut out the diagonal there, and `δ`
pulls back to `[df / f]`. 

### `IsDiagonalSymbolOn.fst_mem_locus`

 The first component of a point of `O` lies in the chart `a`. 

### `IsDiagonalSymbolOn.snd_mem_locus`

 The second component of a point of `O` lies in the chart `a`. 

### `IsDiagonalSymbolOn.isLocalSymbol`

 At a point `p` of `O` given by `φ` and `ψ` in the chart, the differences of the coordinates
  cut out the diagonal and `δ` is their symbol. 

### `EtaleChart.exists_chart_near_diagonal`

 A chart `a` of `X` gives a chart `V` of `X × X` near the diagonal. The point of `V` is a pair of
points `φ`, `ψ` of `a`, its coordinates are those of `φ` and `ψ`, their differences cut out the
diagonal, and `V` contains `(z, z)` for every point `z` of `a`. 

### `exists_isLocalSymbol_of_charts_near_diagonal`

 Let `X` be separated (`IsSeparatedFunctor`; here it makes `offDiagonal X` open), and let `V i`
be finitely many étale charts of `X ⊗ X` with `d + d` coordinates, such that every diagonal point
`(z, z)` with values in a field lies in some `V i`. Suppose that on each `V i` the differences of
the first `d` and last `d` coordinates cut out the diagonal. Then there is a class `δ` in degree-`d`
Hodge cohomology of `X ⊗ X` relative to `offDiagonal X` which, for every `i`, is a local symbol
(`IsLocalSymbol`) with multiplicity `1` at the point of `V i` for these coordinate differences. 

### `exists_diagonal_class`

 The class of the diagonal. If `X` has an atlas of dimension `d`, there is a Hodge class `δ` of
degree `d` on `X × X` relative to the complement of the diagonal, such that every point `z` of
`X` in a field has a chart `a` and an open `O ∋ (z, z)` on which `δ` is the symbol of the
differences of the coordinates of `a`. 
