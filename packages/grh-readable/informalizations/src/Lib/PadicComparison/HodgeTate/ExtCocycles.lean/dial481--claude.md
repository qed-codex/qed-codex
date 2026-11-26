---
{
  "module": "src/Lib/PadicComparison/HodgeTate/ExtCocycles.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/PadicComparison/HodgeTate/ExtCocycles.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/PadicComparison/HodgeTate/ExtCocycles.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Ext¹ classes of cocycles of functors, and contraction on exterior algebras

For functors `N`, `F` from `C` to abelian groups (`New.Variety.AbFunctor C`),
`New.Variety.TotalH N F = ⨁ₙ Extⁿ(N, F)` is the total Ext group. Its Yoneda product is
`New.Variety.TotalH.comp x y`, with `x` first. A morphism `f` gives the class
`New.Variety.TotalH.homClass f` of degree 0, and `New.Variety.TotalH.map Φ` applies an exact functor
`Φ` degree by degree. The file proves a sign rule for connecting classes and attaches to a 1-cocycle
a class in `Ext¹`. For a semilinear map `φ = (φ₀, φ₁) : M → T' × M'`, it also defines
`New.Variety.contraction φ : ⋀ M → ⋀ M'`, which contracts with `φ₀` and applies `φ₁` to the
remaining factors, and proves a product rule for it.

## Main definitions and results

* `New.Variety.TotalH.extClass_sign_comm`: the connecting classes of a short exact sequence of
  functors `Ψ → Ξ → Φ` commute with a class of degree `a` up to the sign `(-1) ^ a`.
* `New.Variety.Cocycle`, `New.Variety.Cocycle.cohomClass`: a 1-cocycle from `F` to `G` twists
  `G × F` into an extension of `F` by `G`, hence a class in `Ext¹(F, G)`.
* `New.Variety.contraction_mul`: `New.Variety.contraction φ` is a graded derivation along
  `New.Variety.exteriorMapSnd φ`, the ring map of `φ₁`.

Notions from other files:
* `New.Variety.abTensor`: The pointwise tensor product over ℤ of two such functors, as a bifunctor.
* `New.Variety.restrictAlong`: For φ: C' → C, the functor N ↦ N∘φ from functors on C to functors on
  C', with values in D.

## Relation to the literature

Known; see `Lib.PadicComparison.HodgeTate.PeriodMap` for sources.



## Ext¹ classes of 1-cocycles and signs of connecting classes

* `New.Variety.abTensor_shortExact`: tensoring with a short exact sequence of functors whose
  quotient is flat gives a short exact sequence.
* `New.Variety.Gm`: the unit group of a commutative ring, as a functor to abelian groups.


 ### The sign rule for connecting classes 

### `exists_cokernel_map_extClass`

 Let `S` be a short exact sequence of functors, `α : A ⟶ B` a monomorphism, and `a : S.X₁ ⟶ A`,
`b : S.X₂ ⟶ B` with `a ≫ α = S.f ≫ b`. Then there is a map `c : S.X₃ ⟶ cokernel α` that
commutes with the quotient maps, and the class of `S` followed by `a` is `c` followed by the class
of the sequence `A → B → cokernel α`. 

### `extClass_anticomm`

 Let `0 → Ψ K → Ξ K → Φ K → 0` (maps `i`, `p`) be short exact for every `K`, with `Φ`, `Ψ`
exact and `Ξ` additive, and let `T` be a short exact sequence of functors. In the 3 × 3 diagram
with these rows for the three terms of `T`, the two composites of connecting classes from
`Φ T.X₃` to `Ψ T.X₁` in `Ext²` differ by a sign. 

### `TotalH.extClass_sign_comm`

 Let `Φ`, `Ψ` be exact functors and `Ξ` an additive functor to `AbFunctor C`, with natural maps
`i : Ψ ⟶ Ξ` and `p : Ξ ⟶ Φ` such that `0 → ΨK → ΞK → ΦK → 0` is short exact for every `K`. For `x`
in `Ext^a(F,G)`, `Φ(x)` followed by the extension class at `G` equals `(−1)^a` times the extension
class at `F` followed by `Ψ(x)`, in total Ext. 

### `abTensor_flip_map_app_comp_eq_zero`

 If `f ≫ g = 0`, the maps `f` and `g` tensored pointwise with `K` also compose to zero. 

### `abTensor_shortExact`

 A short exact sequence 0 → G' → E → G → 0 of functors to abelian groups, G with flat values,
stays short exact after pointwise tensor product with any K. 

### `Gm`

 The multiplicative group: the functor sending a commutative ring R to its unit group R^×,
written additively. `liftCoeff` wraps each value in `ULift`, so for `u : Gm A` the underlying unit
is `u.down`. 

 ### Cocycles and their extension classes 

### `Cocycle`

 A 1-cocycle from F to G: homomorphisms D(f): F(c) → G(d) for f: c → d, with
D(gf) = G(g)D(f) + D(g)F(f). 

### `Cocycle.component`

 The homomorphism `F(c) → G(d)` attached to a morphism `c ⟶ d`. 

### `Cocycle.cocycle_comp`

 The cocycle rule `D(gf) = G(g) D(f) + D(g) F(f)`. 

### `extension`

 For a cocycle D, the sequence G → E → F with E(c) = G(c) × F(c), where f acts by (y,x) ↦
(G(f)y + D(f)x, F(f)x). 

### `cohomClass`

 For a cocycle D from F to G, the class in Ext^1(F,G) of its extension G → E → F, viewed in
the total Ext group. 

### `cohomClass_comp_eq_extClass`

 The class of a cocycle `D` compared with that of a short exact sequence `S`. Let
`α : F ⟶ S.X₃` and `β : G ⟶ S.X₁`, and let `σ c : F(c) → S.X₂(c)` lift `α` at each object `c`.
If the failure of `σ` to be natural along `f : c ⟶ d` is `D(f)` carried into `S.X₂(d)` by `β`
and `S.f`, then the class of `D` followed by `β` is `α` followed by the class of `S`. 

### `cohomClass_naturality`

 If `α : F ⟶ F'` and `β : G ⟶ G'` intertwine the cocycles `D` and `D'`, the class of `D`
followed by `β` is `α` followed by the class of `D'`. 

### `map_cohomClass_restrict`

 Restricting the class of `D` along a functor `φ : C ⥤ C` gives the class of the cocycle
`f ↦ D(φ f)`. 


## Contraction of exterior algebras along a semilinear map

* `New.Variety.contraction_one`, `New.Variety.contraction_ι_mul`: the recursion that determines
  `New.Variety.contraction φ`.


### `algebraMapInv_exteriorMap`

 The map `exteriorMap m` acts on the scalar (degree zero) part through the ring map `a`. 

### `contraction`

 Contraction with `φ₀` for a semilinear map `φ = (φ₀, φ₁) : M → T' × M'`. It is the map
`⋀ M → ⋀ (T' × M')` induced by `φ`, followed by contraction with the first projection and then the
map to `⋀ M'`. 

### `exteriorMapSnd`

 For semilinear φ: M→T'×M', the map of exterior algebras ΛM→ΛM' induced by the second
component M→M' of φ. 

### `contraction_ι_mul`

 The recursion: contracting `m ∧ x` gives `φ₀ m` times the image of `x`, minus `φ₁ m ∧` the
contraction of `x`. 

### `contraction_mul`

 The graded Leibniz rule for `contraction φ` along the ring map `exteriorMapSnd φ`. The sign
when the contraction passes `x` comes from the grade involution `exteriorMap s`, induced by the
map `s = -1` on `M'`. 
