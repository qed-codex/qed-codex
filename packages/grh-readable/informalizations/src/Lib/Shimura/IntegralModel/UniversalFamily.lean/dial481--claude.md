---
{
  "module": "src/Lib/Shimura/IntegralModel/UniversalFamily.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Shimura/IntegralModel/UniversalFamily.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Shimura/IntegralModel/UniversalFamily.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The universal family: models along arcs, rigid fibres and points of linear data

This file studies the universal abelian scheme 𝒜 → S of PEL data D and describes its complex points
by linear algebra. Over an arc `O` (`New.ValuativeArc`, a valuation ring with fraction field `ℂ`), a
description of the generic fibre as a complex torus (`New.ThetaObject.TorusModel`) is also a
description of the object over `O`. The geometric fibres of such a modelled object are rigid
(`New.ThetaObject.HasSpanningCoords`): on each of their pull-backs to a noetherian local ring `B`,
global functions come from the base (`New.HasConstFunctions`), and the coordinates span the sections
of the line bundle `N` of the object over `B`. A linear datum a = (x, ℓ, P)
(`New.Variety.ModuliPoint`) consists of an adelic frame x, a reflection ℓ of ℂⁿ (1 on a line, −1 on
a complement), and vectors P_i.

## Main definitions and results

* `New.Variety.UniversalFamily`: the universal object, with the standing hypotheses.
* `New.ThetaFamily.IsPointOf`, `New.Variety.UniversalFamily.datumPoint`: the point of a fibre power
  of 𝒜 given by a fibre modelled on a, its non-zero 𝔪-torsion points and the images of the P_i.
* `New.ThetaFamily.IsPointOf.eq_iff`, `New.Variety.UniversalFamily.datumPoint_eq_iff`: two such
  points are equal exactly when the data are isomorphic (`New.Variety.ModuliPoint.IsLevelIso`) at
  level K(𝔑) ∩ K(𝔪), where K is the principal level `New.Variety.levelGU` and 𝔑 the level of D. Here
  a ≅ b via z in GL_n(E) means: b.x⁻¹ z a.x lies in the level group, z conjugates a's reflection to
  b's, and z P_i − b.P_i lies in the lattice of b.x.
* `New.Variety.UniversalFamily.GraphClosure`: the closure of the graph of finitely many translations
  a ↦ a·(g_j, 1).
* `New.Variety.UniversalFamily.smooth_and_isDenseFamily_and_exists_comp_eq_act`: at level 1 the
  fibre power is smooth over R, and the points of linear data are dense in it.

Notions from other files:
* `New.ThetaObject`: an object of the family X over a scheme T: a morphism from T to the base of X;
  `x.IsPullbackAlong f y` means x = f ≫ y, the pull-back of y along f.
* `New.Variety.ModuliPoint.act`: a·(g, α) = (x g, ℓ, α_i P_i) for a = (x, ℓ, P), an adelic
  similitude g and integers α_i of E.
* `New.ThetaObject.TorusModel.π`: for a model m, the map from (E ⊗ ℝ)ⁿ to the sections of the
  object; `m.fullStructure.torsionPoint` labels the torsion sections by `New.AdelicTorsion`.
* `New.Variety.NonzeroTorsion`: for a non-zero element 𝔪 of O_E, the set of non-zero elements of
  (𝔸_f / Ô)ⁿ ≅ (E / O_E)ⁿ killed by 𝔪.

## Relation to the literature

Known result: the sections of an ample line bundle on an abelian variety are spanned by theta
functions. Here it is stated for the coordinates of an object with a torus model, on the pull-backs
of its geometric fibres to noetherian local rings (`hasSpanningCoords_of_specMap_comp_eq`). Spanning
of the sections is proved by reduction from the complex numbers rather than by Riemann–Roch, and the
only consequence drawn is that a map of such objects respecting the pairing and the level points
lies over the family, which gives the criterion for equal points (`IsPointOf.eq_iff`). Source: D.
Mumford, On the equations defining abelian varieties I, Invent. Math. 1 (1966), §§1–2; S. W. Shin,
Abelian varieties and Weil representations, Algebra Number Theory 6 (2012), Prop. 2.12 (over a
base); M. Bolognesi, A. Massarenti, Comment. Math. Helv. 91 (2016), Lemma 4.1 (odd type).

See also `Lib.Shimura.ArcExtension` and `Lib.Shimura.IntegralModel.TowerExistence`.


 ## Models of the generic fibre as models along the arc 

### `New.ThetaObject.TorusModel.exists_torusModel_of_isPullbackAlong`

 Let `O` be a valuation ring with fraction field `ℂ`, `y` an object over `O` and `x` its
pull-back `h_pull` to the generic point. A model `m` of `x` on the period map `Y` (an isomorphism
`Y.realEquiv` of `(E ⊗ ℝ)ⁿ` with `V` and a Hermitian form `Y.automorphyForm`) gives a model `m'` of
`y` on `Y` whose sections `m'.π w` restrict to `m.π w` followed by the map of `h_pull`. A case of
the extension of homomorphisms and line bundles of abelian schemes from the generic fibre. 


## Rigidity of the geometric fibres of a modelled object

The idea: Serre's theorem `New.Variety.eventually_span_coordSection` gives the sections of
`[c]^* N ≅ N ^ (c ^ 2)` for large `c`, and the trace over the `c`-torsion brings them down to `N`.


### `atGeneric_comp_nsmul`

 Let `v z = expMap (z / c)` for a model `a` and `c ≠ 0`. Then multiplication by `c` sends the
complex point of `v z` to that of `expMap z`. 

### `New.ThetaObject.TorusModel.exists_mem_thetaSpace_of_periodic`

 Let `a` model `y` over `O` on a complex torus (uniformisation `expMap : W → y.groupScheme` with
lattice `L`, theta coordinates `a.θ z i` indexed by `i : D.dualTorsion`), `c ≠ 0` and
`v z = expMap (z / c)`. A section `ω` of `[c]^* N`, `N = y.lineBundle`, whose values along `v` are
`L`-periodic is a theta function along `v`: `ω_i (v z) = f z / θ_i z` where `θ_i z ≠ 0`, for a theta
function `f` for the Hermitian form `Y.automorphyForm` of the period map and the multiplier
`a.χ`. 

### `New.ThetaObject.TorusModel.pullSections_eq_smul_of_theta`

 In the setting of `New.ThetaObject.TorusModel.exists_mem_thetaSpace_of_periodic`, let `ω` be
given by `f` along `v`, that is, `ω_i (v z) = f z / θ_i z` where `θ_i z ≠ 0`. If a section `w` of
`N` is given by `β • f` along `expMap`, for some `β` in `O`, then its pull-back along multiplication
by `c` is `β • ω`: the two agree at the points `v z`, which are dense. 

### `New.ThetaObject.TorusModel.mem_map_span_of_periodic`

 Let `O` be a valuation ring with fraction field `ℂ` (`ValuativeArc`), and `a` a model of `y`
over `O` on a complex torus (uniformisation `expMap` with lattice `L`, line bundle
`N = y.lineBundle`). Let `c ≠ 0`, `v z = expMap (z / c)`, and `Λ` the pull-back of sections along
multiplication `[c]`. A section `ω` of `[c]^* N` whose components `ω_i`, `i : D.dualTorsion`,
evaluated at the generic ℂ-points `v z` are `L`-periodic in `z` lies in the image under `Λ` of the
`O`-span of the coordinate sections of `N`. 

### `New.ThetaObject.TorusModel.sum_pullSections_translation_mem_map_span`

 Let `a` model `y` over `O` on a complex torus, `c ≠ 0`, `F` an enumeration of the sections
`z` with `c • z = 0`, and `M = [c]^* N` (`N = y.lineBundle`), which `h_transl` identifies with its
pull-backs along the translations by these sections. The trace of a section of `M`, the sum of these
pull-backs, is the pull-back along `[c]` of an `O`-linear combination of the coordinates of `N`. 

### `apply_mem_of_forall_apply_sectionLift_mem`

 Let `x` over `B` be the pull-back `hx` of `y`, with constant global functions on fibres, `M`
the pull-back of the line bundle along multiplication by `c`, and `Q` a lift of `hx` from sections
of `M` on `y` to those on `x`. If the pulled-back coordinates of `N ^ (c ^ 2)` span over `B`, a
`B`-linear map `T` that sends every `Q s` into a submodule `S` sends every section into `S`. 

### `New.ThetaObject.TorusModel.span_coordSection_eq_top_of_isPullbackAlong`

 Let `y` over `O` be modelled by `a` on a complex torus, and let `x` over a local ring `B` be the
pull-back of `y` along `b`, with global functions on `x.groupScheme` constant on fibres. Let `c ≠ 0`
be a unit in `B`, and suppose that the coordinates of the pull-back to `x` of `N ^ (c ^ 2)` span its
sections, where `N` is the line bundle of `y`. Then the coordinates of `x` span its sections over
`B`. 

### `New.ThetaObject.TorusModel.hasSpanningCoords_of_specMap_comp_eq`

 Rigidity of geometric fibres: let `O` be a valuation ring with fraction field ℂ, and `a` a model
of the `O`-point `y` on the complex torus of `Y` (a uniformisation of its group scheme compatible
with the `𝓞 E`-action, level points and theta coordinates). The pull-back `x₀` of `y` along
`χ : O →+* k`, `k` algebraically closed, satisfies `HasSpanningCoords`: on its pull-backs to
noetherian local rings, global functions are constant on fibres and the coordinates span the
sections. A case of the spanning of the sections of an ample bundle by theta functions. 

 ## The universal family, its fibre powers and points of linear data 

### `Variety.UniversalFamily`

 A universal object for the PEL data D: a theta family 𝒜 → S with S projective and smooth of
relative dimension n - 1 over R, where n = `card D.Index`, and a dense set of complex points of S
whose fibres are uniformised by tori. The points are indexed by pairs a = (f, b) of an analytic
family of tori f and a parameter b; the uniformisations are holomorphic in b on the domain
`f.domain` of f. 

### `Variety.UniversalFamily.isDedekindDomain`

 The ring `R` is a Dedekind domain. 

### `Variety.UniversalFamily.base`

 The base S, a scheme over Spec R. 

### `Variety.UniversalFamily.family`

 The theta family: an abelian scheme 𝒜 = `family.total` over the base S = `base.left`. 

### `Variety.UniversalFamily.hasProjEmbedding`

 S is projective over `R`. 

### `Variety.UniversalFamily.smooth`

 S is smooth over `R` of relative dimension n - 1, where n is `card D.Index`. 

### `Variety.UniversalFamily.obj`

 The complex point of S attached to a pair (f, b) of an analytic family `f` and a parameter
  `b`. 

### `Variety.UniversalFamily.model`

 The fibre over `obj a` is modelled on the torus of the family `a.1` at the parameter `a.2`. 

### `Variety.UniversalFamily.holomorphic`

 The uniformisations give complex points of 𝒜 that are holomorphic in `(b, z)`, for `b` in the
  domain of the family. 

### `Variety.UniversalFamily.dense`

 The points `obj a` are dense in S. 

### `instance {S : Scheme} {F : Discrete κ ⥤ Over S} : HasLimit F`

 Finite products exist in `Over S`: a diagram indexed by the finite discrete category of κ has a
limit. 

 ### Fibre powers and the points of linear data 

### `ThetaFamily.fibrePower`

 For a finite set κ, the κ-fold fibre power of the abelian scheme `X.total` over its base, as a
scheme over the base. 

### `ThetaFamily.proj`

 For i in κ, the i-th projection from the κ-fold fibre power of `X.total` to `X.total`, as a
morphism of underlying schemes. 

### `ThetaObject.pointOf`

 Let y be an object of the family X over T, and Q i, for i in κ, sections of its group scheme
`y.groupScheme` over T. This is the T-point of the κ-fold fibre power of `X.total` whose i-th factor
is the section Q i followed by the map of y to the family. 

### `ThetaFamily.IsPointOf`

 Let a = (x, ℓ, P) be a point at infinite level with ν marked vectors, and t an O-point, over the
arc O, of the fibre power of `X.total` with one factor for each non-zero 𝔪-torsion class and one for
each marked vector. `IsPointOf 𝔪 a t` says that t is the point of an object over O that has a torus
model (`TorusModel`) on a period map for the frame x and the reflection ℓ: its factors are the
torsion points of the model at the non-zero 𝔪-torsion classes and the images of the vectors P i. 

### `ThetaFamily.IsPointOf.mk`

 Builds `ThetaFamily.IsPointOf` from a torus model `m` of an object `x` over the arc on a
  period map `Y` for `a.frame` and `a.reflection`. It requires a proof that `t` is the point of `x`
  given by the torsion points of `m.fullStructure` and the images under `m.π` of the vectors
  `a.markedPoint`. 

### `ThetaObject.pointOf_hom`

 The point `y.pointOf Q` lies over the base point of y. 

### `ThetaObject.pointOf_proj`

 The i-th factor of `y.pointOf Q` is the section Q i followed by the map of y to the family. 

### `Variety.UniversalFamily.exists_isPointOf`

 For every point a at infinite level there is a complex point t over R of the fibre power of the
family that is the point of a with its 𝔪-torsion (`New.ThetaFamily.IsPointOf`). 

### `Variety.UniversalFamily.datumPoint`

 For a point a = (x, ℓ, P) at infinite level, a chosen complex point over R of the fibre power of
the family that is the point of a with its 𝔪-torsion (`New.ThetaFamily.IsPointOf`): an object
modelled on (x, ℓ), with its non-zero 𝔪-torsion points and the images of the vectors P i. 

### `fibrePower_ext_iff`

 Two T-points of the κ-fold fibre power of `X.total` are equal if and only if they have the same
image in the base Z and the same projection to `X.total` for every i in κ. 

### `ThetaFamily.IsPointOf.of_generic`

 Let t be an O-point of the fibre power of `X.total` over the arc O. If its generic point
`genericPt ≫ t` is the point of a with its 𝔪-torsion (`New.ThetaFamily.IsPointOf`), then so is t. 

### `mem_Ô_of_torsionClass_mulVec_eq_zero`

 A matrix over the finite adeles that sends every vector with entries in Ô to a vector with
entries in Ô has its entries in Ô. Vectors with entries in Ô are those whose class in the torsion
module (𝔸f / Ô)ⁿ is zero. 

### `mem_levelGU_of_torsionClass_mulVec_eq`

 Let `k` be an adelic similitude (a member of `GU`) with integral entries and integral inverse,
and `𝔞` a non-zero integer of E. If `k` fixes the class in (𝔸f / Ô)ⁿ of every vector whose class is
killed by `𝔞`, then `k` is congruent to 1 modulo `𝔞`: it lies in the level group `levelGU n 𝔞`. 

### `torsionClass_mulVec_eq_of_mem_levelGU`

 A matrix `k` in the level group `levelGU n 𝔞`, congruent to 1 modulo `𝔞`, fixes the class in
(𝔸f / Ô)ⁿ of every vector whose class is killed by `𝔞`. 

### `eq_of_polarisationForm_eq`

 The polarisation form of the PEL data D determines its matrix: matrices β, β' over E with the
same polarisation form are equal. The proof compares the forms on the vectors c eⱼ and (ξ⁻¹)* eᵢ,
and uses that the trace form of E is non-degenerate and that ξ ≠ 0. 

### `ThetaObject.TorusModel.eq_and_comp_toFamily_eq_of_mem_levelGU`

 One direction of `New.ThetaFamily.IsPointOf.eq_iff`: if z in GL_n(E) is an isomorphism of level
K(𝔑) ∩ K(𝔪) from a to b (`b.frame⁻¹ * toFinGL z * a.frame` in both level groups, `ratConj z` taking
a's reflection to b's, `m'.π` equal on z·(a.markedPoint i) and b.markedPoint i) for the torus models
m of x and m' of x', then x = x' and the two models give the same points of the family at the
𝔪-torsion classes and at the marked vectors. 

### `ThetaFamily.IsPointOf.eq_iff`

 Let s and u be complex points of the fibre power of `X.total` that are the points of a and of b
with their 𝔪-torsion (`New.ThetaFamily.IsPointOf`). Then s = u exactly when some z in GL_n(E) is an
isomorphism from a to b at level K(𝔑) ∩ K(𝔪), where 𝔑 is the level of D. 

 ### Closures of graphs, smoothness and density 

### `GraphClosure`

 For a finite family γ of pairs (𝔪_j, g_j) of a non-zero integer and a similitude whose inverse
has entries in Ô (`GUPlus`), the reduced closure, in a product of fibre powers of the family, of the
tuples (over j) of the points `datumPoint 𝔪_j (a.act g_j)` of the translates of the points a at
infinite level. 

### `isPointOf_datumPoint`

 The chosen point `datumPoint 𝔪 a` is the point of a with its 𝔪-torsion. 

### `IsPointOf.eq_datumPoint`

 The point of a with its 𝔪-torsion is unique: every such point u is
`New.Variety.UniversalFamily.datumPoint 𝔪 a`, as the identity is an isomorphism from a to itself
at every level. 

### `datumPoint_eq_iff`

 The points attached to a and b with their 𝔪-torsion are equal if and only if a and b are
isomorphic at level K(𝔑) ∩ K(𝔪), where 𝔑 is the level of D. 

### `instance : HasProjEmbedding X.total.hom`

 The abelian scheme of a theta family is projective over the base, by its embedding. 

### `instance : HasProjEmbedding (X.fibrePower κ).hom`

 A fibre power of the abelian scheme of a theta family is projective over the base. 

### `instance (C : U.GraphClosure γ ν) : HasProjEmbedding C.scheme.hom`

 The closure `C.scheme` is projective over the base, as a closed subscheme of a product of fibre
powers. 

### `GraphClosure.exists_level_point_eq`

 There is a level m such that the point of the closure C attached to a depends only on the
isomorphism class of a at level K(m). 

### `smooth_fibrePower`

 For κ with m elements, the κ-fold fibre power of the abelian scheme 𝒜 over the base S is smooth
over S of relative dimension m times the dimension of 𝒜 (`New.Variety.abelianDim`). 

### `smoothOfRelativeDimension_fibrePower_one`

 At level `1` there is no non-zero torsion class, so the fibre power with one factor for each
of `ν` marked vectors is smooth of relative dimension `ν` times that of 𝒜. 

### `smoothOfRelativeDimension_fibrePower`

 The fibre power of 𝒜 with one factor for each of `ν` marked vectors is smooth over `R` of
relative dimension `card D.Index - 1 + ν * abelianDim`. 

### `isDenseFamily_datumPoint`

 The points `datumPoint 1 a` of the points `a` at infinite level with `ν` marked vectors are
dense in the fibre power of 𝒜 with one factor for each marked vector. 

### `exists_comp_datumPoint_act`

 There is, for each family `α` of integers of `E`, a self-map `m α` of the fibre power of 𝒜
with one factor for each of `ν` marked vectors that sends `datumPoint 1 (a.act g)` to
`datumPoint 1 (a.act g α)`. 

### `smooth_and_isDenseFamily_and_exists_comp_eq_act`

 Let Z be the fibre power of 𝒜 with one factor for each of ν marked vectors, over R, and
`c a = datumPoint 1 a`. Then (a) Z is smooth over R of relative dimension
`card D.Index - 1 + ν * abelianDim`; (b) the points `c a` are dense in Z; (c) for each family α of
integers of E a self-map `m α` of Z sends `c (a.act g)` to `c (a.act g α)`. 
