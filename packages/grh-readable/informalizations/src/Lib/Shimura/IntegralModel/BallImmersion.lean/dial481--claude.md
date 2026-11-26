---
{
  "module": "src/Lib/Shimura/IntegralModel/BallImmersion.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Shimura/IntegralModel/BallImmersion.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Shimura/IntegralModel/BallImmersion.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Balls immerse; holomorphy, arcs and complex points of the covers

This file gives a local and global description of the covers
`New.Variety.UniversalFamily.GraphClosure`. These are reduced closures `C.scheme` of the complex
points `C.point a`. Here `a = (x, ℓ, P)` (`New.Variety.ModuliPoint`) is an adelic frame, a
reflection (1 on a line, −1 on a complement) and marked vectors.

* `New.Variety.AnalyticFamily.isHolomorphicImmersionAt_of_holomorphicAt`: let the objects `x b'`
  have models of the tori of an analytic family. Let `b` be in its domain. Suppose the uniformised
  points are holomorphic at `(b, z)` for every `z`. Then `x` is a holomorphic immersion at `b`.
* `New.Variety.ModuliPoint.exists_finite_analyticFamily_isLevelIso`: at each nonzero level, finitely
  many analytic families reach every point up to isomorphism.
* `New.Variety.UniversalFamily.isHolomorphicImmersionAt_datumPoint`,
  `New.Variety.UniversalFamily.GraphClosure.holomorphicAt_point`: the points of an analytic family
  depend holomorphically, and immersively, on the parameter.
* `New.Variety.UniversalFamily.GraphClosure.exists_arc`,
  `New.Variety.UniversalFamily.GraphClosure.exists_arc_centre_eq`: every point of `C.scheme`, and
  every complex point, is the centre of an arc of objects.
* `New.Variety.UniversalFamily.GraphClosure.point_surjective`: suppose some map `c` sends each
  `C.point a` to `U.datumPoint 1 a`. Then every complex point of `C.scheme` is some `C.point a`.

`New.HolomorphicAt φ w` says that regular functions pull back along `φ` to functions analytic at
`w`.

Notions from other files:
* `New.Variety.AnalyticFamily`: tori with a fixed frame over a domain `f.domain` in ℂⁿ⁻¹, with
  period maps `Q_b` analytic in `b`; the derivative of `Q` along `v` is ℂ-linear for the complex
  structure given by `Q_b` only if `v = 0` (`eq_zero_of_linear`).
* `New.Variety.ModuliPoint.act`: `a.act g α = (x g, ℓ, α i • P i)` for `a = (x, ℓ, P)`.
* `New.Variety.UniversalFamily.datumPoint`: for `a = (x, ℓ, P)`, a chosen complex point over `R` of
  the fibre power of the family: an object modelled on `(x, ℓ)`, with its non-zero `𝔪`-torsion
  points and the points `P`.

## Relation to the literature

Known; see `Lib.Shimura.IntegralModel.TowerExistence` and `Lib.Shimura.ThetaModuli.UniversalFamily`
for sources.


### `fderiv_apply_eq_neg_of_eventually_eq_zero`

 Let `g` be a function on a complex normed space whose derivative has the derivative `D₂` at
`w₀`. Suppose that, for all large `k`, the derivative of `g` at `w₀ + k⁻¹ • a` vanishes in the
direction `u + k⁻¹ • c`. Then the derivative of `g` at `w₀` sends `c` to `-D₂ a u`. 

### `eq_of_forall_torsionClass_mulVec_eq`

 Two invertible finite adelic matrices that induce the same map on torsion classes are equal. 

### `ModuliPoint.isLevelIso_act_of_inv_eq`

 Let `a`, `a'` be points and `g` an element of `GUPlus E D.Index`. Suppose `z` carries the
reflection of `a` to that of `a'` and the marked points of `a` to those of `a'`, and
`g⁻¹ = a'.frame⁻¹ * z * a.frame`. Then `z` is an isomorphism from `a.act g` to `a'` at every level
`K`: it matches reflections and marked points, and `a'.frame⁻¹ * z * (a.act g).frame ∈ K`. 

### `AnalyticFamily.isHolomorphicImmersionAt_of_holomorphicAt`

 Balls immerse. Let `f` be an analytic family of theta tori over `f.domain`, and `X` a theta
family (an abelian scheme with `𝓞 E`-action and theta coordinates) over `Z`. Let each `x b'` be a
complex point of `Z` with a model `m b'`, a uniformisation of the fibre of `X` at `x b'` by the
torus `f.torus b'`. Let `ψ (b', z)` be the image of `z` under this uniformisation, a complex point
of `X`. If `b ∈ f.domain` and `ψ` is holomorphic at every `(b, z)`, then `x` is a holomorphic
immersion at `b` as a family of complex points of `Z`: it is holomorphic there, and constant to
first order only in the direction `0`. 

### `ModuliPoint.exists_finite_analyticFamily_isLevelIso`

 For `𝔪 ≠ 0` there are finitely many analytic families `f k`, `k : κ`, with this property: every
point `a : ModuliPoint E D.Index ν` is isomorphic at level `levelGU D.Index 𝔪`, by some
`z : GL D.Index E`, to a point `(f k).ballPoint 0 p` (the member of `f k` at `p.1`, with marked
points `p.2`) with `p.1` in the domain of `f k`. 

### `UniversalFamily.isHolomorphicImmersionAt_datumPoint`

 Let `f` be an analytic family and `P` marked vectors. The map sending a parameter `p` to the
point `U.datumPoint 𝔪 (f.ballPoint P p)` of the fibre power of the universal family `U` (the member
of `f` at `p`, with its non-zero `𝔪`-torsion points and the points `P` translated by `p.2`) is a
holomorphic immersion at every `p` whose base coordinate `p.1` lies in the domain of `f`. 

### `holomorphicAt_point`

 Let `C` be the cover (the reduced closure of the points `C.point a`, whose component `j` is
`U.datumPoint (γ j).1 (a.act (γ j).2)`), `f` an analytic family and `P` marked vectors. The map
sending a parameter `p` to the complex point `C.point (f.ballPoint P p)` of `C` is holomorphic at
every `p` whose base coordinate `p.1` lies in the domain of `f`. 

### `exists_arc`

 Let `C` be the cover (the reduced closure of the points `C.point a`) and `z` a point of
`C.scheme`. There are a valuation subring `V` of `ℂ`, an arc `α : Spec V ⟶ C.scheme`, a point `b`
and a map `ρ` from the residue field of `z` to the residue field of `V` with two properties. (a) The
closed point of `α` is `z`, through `ρ`. (b) Whenever `C.point b ≫ u` is the point
`U.datumPoint 𝔪 a`, the composite of `α` and `u` is a point of the universal family for `a` at level
`𝔪`. 

### `exists_arc_centre_eq`

 Let `C` be the cover (the reduced closure of the points `C.point a`) and `t` a complex point of
`C.scheme` over `R`. There are a valuation subring `V` of `ℂ`, an arc `α : Spec V ⟶ C.scheme`, a
point `b` and a ring map `φ` from the residue field of `V` to `ℂ` with two properties. (a) The
closed point of `α`, seen through `φ`, is `t`. (b) Whenever `C.point b ≫ u` is the point
`U.datumPoint 𝔪 a`, the composite of `α` and `u` is a point of the universal family for `a` at level
`𝔪`. 

### `point_surjective`

 Let `C` be the graph closure for the pairs γ_j = (𝔪_j, g_j) and ν. Here `C.scheme` is the
reduced closure, in a product of fibre powers of the universal family `U`, of the tuples over j of
`U.datumPoint 𝔪_j (a.act g_j)`, and `C.point a` is its complex point for a point a = (x, ℓ, P) at
infinite level: an adelic matrix x, a reflection ℓ for which x is a signed frame, and marked
vectors P i in (E ⊗ ℝ)ⁿ.
Suppose a morphism `c` from `C.scheme` to the fibre power of the abelian scheme of `U` indexed by
the nonzero 1-torsion and `Fin ν` sends each `C.point a` to `U.datumPoint 1 a`, the chosen complex
point given by an object modelled on (x, ℓ) with the images of the P i. Then every complex point
over `R` of `C.scheme` is `C.point a` for some a. 
