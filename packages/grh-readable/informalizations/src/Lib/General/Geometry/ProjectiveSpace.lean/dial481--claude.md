---
{
  "module": "src/Lib/General/Geometry/ProjectiveSpace.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Geometry/ProjectiveSpace.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Geometry/ProjectiveSpace.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Projective space, linear systems and projective embeddings, with Segre and Veronese

This file treats projective space `New.ProjSpace ι = Proj ℤ[X i]` and maps to it through ring-valued
points. A linear system (`New.LineBundle.IsLinearSystem`) is a line bundle given by a cover `U i`
and functions `g i j`. Each `g i j` is regular on all of `U i` and plays the part of `s j / s i`. A
projective embedding is a linear system `L` on `X` with a proper morphism `s : X ⟶ S`. In it, two
points of one chart with the same coordinates and the same image in `S` are equal. The file shows
that such embeddings determine morphisms and pass to closed subschemes and composites.

## Main definitions and results

* `New.ProjSpace.hyperplaneBundle`, `New.ProjSpace.isLinearSystem_hyperplaneBundle`: the standard
  charts with `g i j = X j / X i` form a linear system.
* `New.LineBundle.IsHomogeneousCoords`: homogeneous coordinates of a point. Under a projective
  embedding, a point that lies in some chart is determined by its coordinates and its image in the
  base (`New.LineBundle.IsProjEmbedding.eq_of_isHomogeneousCoords`). A vector with a unit entry is a
  vector of coordinates of some point of projective space
  (`New.ProjSpace.exists_isHomogeneousCoords`).
* `New.LineBundle.IsProjEmbedding`, `New.isProjEmbedding_projSpace`: projective embeddings, by
  linear systems that separate points. Projective space over a base, with a finite index set, is
  one.
* `New.LineBundle.exists_picClass_eq_pull_hyperplane`,
  `New.LineBundle.IsLinearSystem.exists_hom_projSpace`: finite families of sections without common
  zero, and finite linear systems, come from maps to projective space.
* `New.LineBundle.IsProjEmbedding.exists_isClosedImmersion`: for finite `ι`, an embedding is a
  closed immersion into ℙ^ι × S.
* `New.LineBundle.isProjEmbedding_pi` (Segre), `New.LineBundle.IsProjEmbedding.pow` (Veronese): a
  proper scheme with finitely many jointly separating maps to embedded schemes embeds, and the
  `m`-th tensor power of a projective embedding is one for `m ≠ 0`.

Notions from other files:
* `New.PointFn`: a function on ring-valued points of X attaches an element of A to every point Spec
  A → X, for every ring A, with no compatibility required. It is regular on an open U if its value
  at Spec φ ≫ t is φ of its value at t, for every t landing in U and every ring map φ.
* `New.LineBundle.IsSection`: the family (s_i) is a global section of L: each s_i is regular on U_i,
  and s_i = g_ij s_j at points landing in U_i and U_j.
* `New.LandsIn`: the morphism t : Y → X lands in the open U, that is, t⁻¹U is all of Y.
* `New.PointFn.ofSection`: a section s over U as a function on ring-valued points: its value at t :
  Spec A → X is t*s in A if t lands in U, and 0 otherwise.


 ## Projective space, homogeneous coordinates and linear systems 

### `eval₂_mul_of_isHomogeneous`

 The value of a homogeneous polynomial `a` of degree `n`, with coefficients mapped by `f`, at the
scaled point `c • v` is `c ^ n` times its value at `v`. 

 ### Projective space and its charts 

### `ProjSpace`

 Projective space over ℤ with homogeneous coordinates X_i, i in ι: the scheme Proj ℤ[X_i]. 

### `ProjSpace.coordFraction`

 The fraction X_j/X_i in the degree-zero part of the localization of ℤ[X] at X_i. 

### `ProjSpace.coordSection`

 The fraction X_j/X_i as a section over the standard chart D₊(X_i) of projective space. 

### `ProjSpace.coordRatio`

 The function X_j/X_i on ring-valued points of projective space landing in D₊(X_i), and zero
at the other points. 

### `ProjSpace.map_coordSection_mul`

 On an open `U` contained in D₊(X_i) and D₊(X_j), the restrictions of the sections X_j/X_i and
X_k/X_j multiply to the restriction of X_k/X_i. 

### `ProjSpace.coordRatio_mul`

 At a point of projective space that lands in D₊(X_i) ∩ D₊(X_j) the functions X_j/X_i and
X_k/X_j multiply to X_k/X_i. 

### `ProjSpace.hyperplaneBundle`

 The line bundle O(1) on projective space, with the standard cover D₊(X_i) and transition
functions X_j/X_i. 

### `ProjSpace.isAffineOpen_chart`

 The standard chart D₊(X_i) of projective space is affine. 

### `ProjSpace.landsIn_chart_iff_isUnit`

 A point `t` of the chart D₊(X_i) lands in the chart D₊(X_j) exactly when the value of X_j/X_i at
`t` is a unit. 

### `IsHomogeneousCoords`

 v is a vector of homogeneous coordinates of the point t for L: t lands in U_j exactly when v_j
is a unit, and then g_jk(t) = v_k/v_j. 

### `IsHomogeneousCoords.transition_eq_mul_inverse`

 If v is a vector of homogeneous coordinates of t and v_j is a unit, then g_jk(t) = v_k/v_j. 

### `landsIn_mul_opens_iff`

 A point lands in the chart (i, k) of the tensor product of L and N exactly when it lands in the
chart i of L and in the chart k of N. 

### `IsLinearSystem`

 `L` is a linear system, that is, the data of a map to projective space. The model is
`L.transition i j = s j / s i` on the chart `L.opens i` where `s i` does not vanish, for sections
`s i` without common zero. 

### `IsLinearSystem.isRegularOn_transition`

 The function `L.transition i j` is regular on the whole chart `L.opens i`. 

### `IsLinearSystem.transition_eq_zero`

 The function `L.transition i j` vanishes at the points that do not land in `L.opens i`. 

### `IsLinearSystem.isHomogeneousCoords_transition`

 The values `L.transition i j A t`, as `j` varies, are homogeneous coordinates of every point
  `t` of the chart `L.opens i`. 

### `_root_.New.ProjSpace.isLinearSystem_hyperplaneBundle`

 The standard charts D₊(X_i) with the functions X_j/X_i form a linear system on projective
space. 

### `IsLinearSystem.ext_of_transition_eq_mul`

 Two linear systems L, M on X with one index set are equal if g^M_jk = g^M_ji · g^L_ik for all k
at every point landing in U_i of L and in U_j of M. 

### `IsLinearSystem.isSection`

 For a linear system L with transition functions g_ij and a fixed j, the family (g_ij)_i is a
global section of L: each g_ij is regular on U_i, and g_ij = g_ik g_kj on U_i ∩ U_k. 

### `IsLinearSystem.pull`

 The pull-back of a linear system along a morphism is a linear system. 

### `isHomogeneousCoords_mul_prod`

 The products v_i w_k of homogeneous coordinates v and w of a point t for L and for N are
homogeneous coordinates of t for the tensor product of L and N. 

### `IsLinearSystem.mul`

 The tensor product of two linear systems is a linear system. 

### `pull_iff`

 A vector v gives homogeneous coordinates of t for the pull-back of L along p exactly when it
gives homogeneous coordinates of t ≫ p for L. 

### `map`

 Let v be homogeneous coordinates of the point t for a linear system L, with a unit entry v_i.
For a ring map φ from A to R, the vector φ(v) gives homogeneous coordinates of the induced
R-valued point. 

### `mul`

 The products of homogeneous coordinates of a point for L and for N are homogeneous coordinates
of it for the tensor product of L and N. 

### `_root_.New.ProjSpace.exists_hom_mul_coordSection_eq`

 For a vector `v` in `A ^ ι` with a unit entry `v i` there is a ring map `φ` from the sections
over the chart D₊(X_i) to `A` that sends X_j/X_i to `v j / v i`. 

### `_root_.New.ProjSpace.exists_isHomogeneousCoords`

 A vector `v` in `A ^ ι` with a unit entry `v i` is a vector of homogeneous coordinates of an
`A`-valued point of projective space over `S` lying over any given point `b` of `S`. 

### `IsProjEmbedding`

 `L` embeds `X` in projective space over `S`: it is a linear system that separates the
ring-valued points of `X` over `S` chart by chart, and `s : X ⟶ S` is proper. 

### `IsProjEmbedding.isLinearSystem`

 `L` is a linear system. 

### `IsProjEmbedding.isProper`

 `X` is proper over `S`. 

### `IsProjEmbedding.eq_of_transition_eq`

 Two points of one chart with the same affine coordinates and the same image in `S` are
  equal. 

### `IsProjEmbedding.eq_of_isHomogeneousCoords`

 Under a projective embedding, two points a and t with the same homogeneous coordinates v and the
same image in the base are equal, provided a lands in some chart (as it does when A is a local
ring). 

### `IsProjEmbedding.of_isPullback`

 Base change: if L embeds X over S and Y is the fibre product of s : X ⟶ S and
b : T ⟶ S, with projections p : Y ⟶ X and t : Y ⟶ T, then the pull-back of L along p
embeds Y over T. 

### `_root_.New.ProjSpace.surjective_eval₂Hom_coordFraction`

 The degree-zero localization of `ℤ[X]` at `X i` is generated as a ring by the fractions
`X j / X i` (`coordFraction i j`). 

### `_root_.New.ProjSpace.hom_ext_of_coordSection_eq`

 Two ring maps from the sections over the chart D₊(X_i) that agree on all X_j/X_i are equal. 

### `_root_.New.ProjSpace.isProper_specZIsTerminal_from`

 Projective space with a finite index set is proper over `Spec ℤ`. 

### `_root_.New.isProjEmbedding_projSpace`

 For a finite index set κ and a scheme S, the pull-back of O(1) to ℙ^κ × S is a projective
embedding over S for the second projection. 

 ### Maps to projective space 

### `exists_hom_isHomogeneousCoords_of_cover`

 Gluing of points with given coordinates. Let `s j` (`j : κ`, with `κ` finite) be sections of
the line bundle `L`, where `s j i` is the function of `s j` on `L.opens i`. Let `C` be a line bundle
indexed by pairs, used only for its cover, such that `C.opens (i, j)` lies in `L.opens i` and
`s j i` is a unit on it. Then there is a map `f` from `X` to projective space such that, at each
point `t` of `C.opens (i, j)`, the values `s k i (t)` are homogeneous coordinates of `t ≫ f`. 

### `exists_landsIn_opens_iff_isUnit`

 Let `s j` (`j : κ`) be sections of the line bundle `L` on `X`, where `s j i` is the function of
`s j` on the chart `L.opens i`. Suppose that they have no common zero at the field-valued points
that factor through a surjective `p : Y ⟶ X`. Then the opens of the `L.opens i` where `s j i` is a
unit cover `X`; the cover is given as that of a line bundle `C` indexed by the pairs `(i, j)`. 

### `picClass_eq_of_isHomogeneousCoords`

 Let `s j` (`j : κ`) be sections of the line bundle `L` on `X` such that, at each point `t` of
`L.opens i`, the values `s j i (t)` are homogeneous coordinates of `t` for the line bundle `N`. Then
`L` and `N` have the same class in the Picard group. 

### `exists_picClass_eq_pull_hyperplane`

 Let `s j` (`j : κ`, with `κ` finite) be sections of the line bundle `L` on `X`, where `s j i` is
the function of `s j` on the chart `L.opens i`. Suppose that they have no common zero at the
field-valued points that factor through a surjective `p : Y ⟶ X`. Then there is a map `f` from `X`
to projective space such that (a) `L` has the same class in the Picard group as the pull-back of
O(1) = `New.ProjSpace.hyperplaneBundle κ` along `f` and (b) at each point `t` of `L.opens i` the
values `s j i (t)` are homogeneous coordinates of `t` for that pull-back. 

### `IsLinearSystem.exists_hom_projSpace`

 Let `N` be a linear system on `X` indexed by a finite set `κ`, and let `s : X ⟶ S` be any
morphism. Then `N` is the pull-back of O(1), cover and transition functions included, along some
morphism `j` from `X` to `ProjSpace κ ⨯ S` over `S`. 

### `inductive`

 The morphism `s : X ⟶ S` has a projective embedding with finitely many coordinates; then `X` is
a closed subscheme of a projective space over `S`
(`New.LineBundle.IsProjEmbedding.exists_isClosedImmersion`). 

### `inductive.mk`

 A projective embedding with finitely many coordinates. 


## Properties of projective embeddings

`New.LineBundle.IsProjEmbedding L s` says three things. The line bundle `L` on `X` is a linear
system, so that `L.transition i j` is the affine coordinate `x_j / x_i` on the chart `L.opens i`.
The morphism `s : X ⟶ S` is proper. Two ring-valued points of one chart with the same coordinates
and the same image in `S` are equal.

* `New.LineBundle.IsProjEmbedding.exists_affine_chart`: over an affine base the charts are affine,
  with coordinate rings generated by the coordinates.


### `instance [h : Variety.HasProjEmbedding s] : IsProper s`

 A morphism with a projective embedding is proper. 

### `ext`

 If `L` embeds `X` over `S`, two morphisms `a b : Y ⟶ X` that agree over `S` and pull `L` back
to the same cover and transition functions are equal. 

### `comp`

 If `L` embeds `X` projectively over `S` along `s` and `p : Y ⟶ X` is a closed immersion, then
the pull-back of `L` along `p` embeds `Y` projectively over `S` along `p ≫ s`. 

### `mul`

 Segre embedding of a tower: if `L` embeds `X` over `S` along `s`, and `N` embeds `S` over `Y`
along `b`, then the tensor product of `L` with the pull-back of `N` along `s` embeds `X` over `Y`
along `s ≫ b`. 

### `exists_isClosedImmersion`

 If `L`, with a finite set `ι` of coordinates, is a projective embedding for `s : X ⟶ S`, then
`L` is the pull-back of O(1), cover and transition functions included, along a closed immersion `j`
of `X` into `ProjSpace ι ⨯ S` over `S`. 

### `exists_affine_chart`

 Let `L`, with finitely many coordinates, embed `X` projectively over `Spec R`. Then each chart
`L.opens i` is affine and there is a ring map `φ` from `R[X_j]` to the sections over it that (a)
is surjective, (b) induces the structure map of the chart on constants (`specMap` is `Spec` of a
ring map), and (c) sends `P` to a section whose value at each ring-valued point `t` of the chart is
`P` evaluated at the coordinates `X_j = L.transition i j (t)`, the coefficients of `P` being mapped
by the ring map `preimage (t ≫ s)` that induces `t ≫ s`. 


## Tensor products and powers of line bundles

`New.LineBundle` is a line bundle given by a cover with a cocycle. `New.LineBundle.picClass` is its
class in the Picard group, written additively.

* `New.LineBundle.pi`, `New.LineBundle.pow`: the product of a family, and the `m`-th power, indexed
  by tuples.


### `pi`

 The tensor product of the line bundles `N a` over `a` in `s` (by default all `a`), on the common
refinement of all covers; for linear systems and `s` the set of all `a`, the Segre product. 

### `pow`

 The `m`-th tensor power of `L`, indexed by `m`-tuples of indices; for a linear system, the
Veronese system of all monomials of degree `m`. 

### `picClass_pi`

 The class in the Picard group of the product of the `N l`, `l ∈ s`, is the sum of their
classes. 

### `IsLinearSystem.pi`

 The Segre product of a finite family of linear systems is a linear system. 

### `isProjEmbedding_pi`

 Segre embedding: let `W` be proper over `S`, with finitely many `S`-maps `π l : W ⟶ Z l` that
jointly separate morphisms into `W` over `S`. If each `N l` is a projective embedding of `Z l` over
`S`, then the product of the pull-backs of the `N l` along the `π l` is a projective embedding of
`W` over `S`. 

### `IsProjEmbedding.pow`

 Veronese embedding: if `L` is a projective embedding of `X` over `S`, so is its `m`-th tensor
power for `m ≠ 0`. 
