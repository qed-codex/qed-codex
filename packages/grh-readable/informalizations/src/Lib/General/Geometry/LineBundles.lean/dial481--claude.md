---
{
  "module": "src/Lib/General/Geometry/LineBundles.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Geometry/LineBundles.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Geometry/LineBundles.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Line bundles on schemes via ring-valued points: descent and the Picard group

Line bundles on a scheme `X` are described through ring-valued points `t : Spec A ⟶ X`, so that
restriction maps disappear. A function `f : New.PointFn X` gives an element of `A` for every such
point. `New.LandsIn t U` says that `t` lands in the open `U`, and `f` is regular on `U` when it is
natural in `A` on the points of `U`. The file shows that regular functions come from sections and
that functions, sections and frames descend along flat, surjective, quasi-compact morphisms, and it
defines the Picard group with its pull-back.

## Main definitions and results

* `New.LineBundle`: a line bundle as an open cover with a cocycle of regular functions, with the
  operations `New.LineBundle.pull`, `New.LineBundle.one`, `New.LineBundle.inv`,
  `New.LineBundle.mul`.
* `New.LineBundle.IsSection`, `New.LineBundle.IsFrame`, `New.LineBundle.IsIsomorphic`,
  `New.LineBundle.H0`: sections, nowhere vanishing sections, isomorphism, and the module of
  sections.
* `New.PointFn.exists_ofSection_glue`: descent of functions along a flat, surjective, quasi-compact
  morphism.
* `New.LineBundle.exists_isSection_eq_mul`, `New.LineBundle.exists_isFrame_of_fpqc`: descent of
  sections and of frames along a flat, surjective, quasi-compact morphism.
* `New.Pic`, `New.LineBundle.picClass`, `New.Pic.pull`: the Picard group, written additively, the
  class of a line bundle, and the pull-back along a morphism.
* `New.Pic.eq_zero_of_isLocalRing`: the Picard group of the spectrum of a local ring is trivial.

## Relation to the literature

These are standard facts on line bundles and faithfully flat descent, in the language of ring-valued
points.


 ## Functions on points, line bundles as cocycles, sections and frames 

 ### Functions on ring-valued points 

### `specMap`

 For a ring homomorphism `φ : R →+* B`, the induced morphism of schemes `Spec B ⟶ Spec R`. 

### `LandsIn`

 The morphism `t : Y ⟶ X` lands in the open `U`, that is, `t ⁻¹ᵁ U` is all of `Y`. 

### `PointFn`

 Functions on ring-valued points of `X`: rules attaching an element of `A` to every point
`Spec A ⟶ X`, for every ring `A`, with no compatibility required. 

### `PointFn.IsRegularOn`

 The function `f` is regular on `U`: for points `t : Spec A ⟶ X` landing in `U`, its value
commutes with all ring maps `φ : A ⟶ B`. 

### `PointFn.evalSection`

 For a point `t : Spec A ⟶ X` landing in `U`, the ring map `Γ(X, U) ⟶ A` evaluating sections
at `t`. 

### `PointFn.ofSection`

 The function on points given by a section `s` over `U`: its value at `t` is the pull-back of
`s` along `t` if `t` lands in `U`, and `0` otherwise. 

### `LineBundle`

 A line bundle on X as an open cover U_i with transition functions g_ij regular on U_i ∩ U_j,
satisfying g_ii = 1 and g_ij g_jk = g_ik (`opens i` is U_i, `transition i j` is g_ij). 

### `LineBundle.opens`

 The open sets on which the bundle is trivialised. 

### `LineBundle.transition`

 The transition functions, as functions on ring-valued points of `X`. 

### `LineBundle.cover`

 The open sets cover `X`. 

### `LineBundle.regular`

 The transition function g_ij is regular on U_i ∩ U_j. 

### `LineBundle.transition_self`

 The function g_ii is 1 at the points of U_i. 

### `LineBundle.transition_trans`

 The cocycle condition g_ij g_jk = g_ik at the points of U_i ∩ U_j ∩ U_k. 

### `PointFn.pull`

 For `p : Y ⟶ X` and a function `f` on ring-valued points of `X`, the function
`t ↦ f (t ≫ p)` on ring-valued points of `Y`. 

### `instance : Algebra R (PointFn X)`

 For a scheme `X` over `R`, a point `t : Spec A ⟶ X` makes `A` an `R`-algebra, and a scalar
`r : R` gives the function sending each such `t` to the image of `r` in `A`. 

 ### Operations on line bundles 

### `pull`

 The pull-back of the line bundle (U_i, g_ij) along p: Y → X, with cover p⁻¹U_i and
transition functions p*g_ij. 

### `one`

 The trivial line bundle on X: the single open set X and the transition function 1. 

### `inv`

 The dual line bundle: the same cover, with (i, j) transition function g_ji. 

### `mul`

 The tensor product L ⊗ M: the cover by the intersections of an open of L with an open of M, with
products of transition functions. 

 ### Sections 

### `IsSection`

 The family (s_i) is a global section of L: each s_i is regular on U_i, and s_i = g_ij s_j at
points landing in U_i and U_j. 

### `IsFrame`

 The family s is a nowhere vanishing global section of L: a section with s_i a unit at every
point landing in U_i. 

### `IsIsomorphic`

 The line bundles L and M are isomorphic: L ⊗ M⁻¹ has a nowhere vanishing global section. 

### `H0`

 The R-module of global sections of L, for a scheme X over R. Each s_i is normalised to be zero
at the points that do not land in U_i. 


## Gluing of morphisms, evaluation of sections and fpqc descent

* `New.PointFn.IsRegularOn.ext_of_dominant_of_isOpenCover`: regular functions are determined by
  their pull-backs along a quasi-compact, scheme-theoretically dominant morphism.


 ### Points that land in an open 

### `landsIn_iff_mem`

 For a local ring `B`, a point `z : Spec B ⟶ X` lands in `U` exactly when the image of the closed
point lies in `U`. 

### `exists_landsIn_of_isOpenCover`

 For a local ring `B`, a point `t : Spec B ⟶ Y` lands in some member of an open cover `V` of
`Y`. 

### `LineBundle.exists_landsIn`

 For a local ring `B`, a point `t : Spec B ⟶ Y` lands in some member of the open cover
`M.opens` of `Y`. 

### `landsIn_fromSpec`

 A morphism that factors through `Spec Γ(X, U) ⟶ X`, for an affine open `U`, lands in `U`. 

### `landsIn_opensRange`

 A point lands in the image of an open immersion `c : Spec R ⟶ X` exactly when it factors
through `c`. 

### `landsIn_comp_incl`

 A morphism that factors through the inclusion of `U` lands in `U`. 

 ### Testing and gluing on a cover 

### `isOpenCover_inf`

 The intersections of the members of two open covers form an open cover. 

### `hom_ext_of_isOpenCover`

 Two morphisms from `Y` are equal if they agree on every ring-valued point that lands in a member
of an open cover `V` of `Y`. 

### `hom_ext_of_cover`

 Two morphisms from `Y` are equal if they agree on every ring-valued point that lands in a
trivialising open of a line bundle `M` on `Y`. 

### `exists_hom_of_cover`

 Gluing on an open cover `V` of `Y`. Attach to each point `t : Spec A ⟶ Y` landing in
`V i` (that is, with image inside it) a morphism `F i A t _ : Spec A ⟶ X`, compatibly with
ring maps `φ : A ⟶ B` and change of the index `i`. Then some `f : Y ⟶ X` has `t ≫ f = F i A t _`
for all such `t`. 

### `le_of_cover`

 `U ≤ W` holds if every ring-valued point that lands in `U` and in a member of an open cover
`V` of `Y` lands in `W`. 

 ### Effective epimorphisms 

### `instance [EffectiveEpi p] [QuasiCompact p] : IsSchemeTheoreticallyDominant p`

 A quasi-compact effective epimorphism of schemes is scheme-theoretically dominant. 

 ### Evaluation of sections 

### `ofSection_eq`

 At a point `t` that lands in `U`, the function of a section `s` is evaluation of `s` at `t`. 

### `ofSection_appLE`

 Let `W ≤ p ⁻¹ᵁ U`, let `s` be a section over `U`, and let the point `x` land in `W`. The value
at `x` of the pull-back of `s` along `p`, restricted to `W`, is the value of `s` at `x ≫ p`. 

### `ofSection_map`

 At a point that lands in `V`, a section over `U` and its restriction to `V` have the same
value. 

### `landsIn_fromSpecStalk`

 For `x ∈ U`, the point `Spec 𝒪_x ⟶ X` lands in `U`. 

### `map_evalSection_fromSpec`

 A point of an affine open `U` is `Spec` of its evaluation map, followed by
`Spec Γ(X, U) → X`. 

### `point_eq_of_ofSection_eq`

 Two `A`-valued points of an affine open `U` are equal if all sections over `U` have the same
value at them. 

### `ofSection_map_fromSpec`

 At the point of an affine open `U` given by a ring map `φ : Γ(X, U) ⟶ A`, the value of `s` is
`φ s`. 

### `ofSection_fromSpecStalk`

 For `x ∈ U`, the value of a section `s` over `U` at the point `Spec 𝒪_x ⟶ X` is the germ of
`s` at `x`. 

### `landsIn_basicOpen`

 A point of `U` lands in the basic open of the section `s` exactly when the value of `s` there
is a unit. 

### `ofSection_appTop`

 The value at `t` of the pull-back of a global section `c` along `p : Y ⟶ X` is the value of `c`
at `t ≫ p`. 

### `ofSection_ΓSpecIso_inv`

 An element `r` of a ring `B`, read as a global section of `Spec B`, has the value `φ r` at the
point given by a ring map `φ : B ⟶ A`. 

### `ofSection_topIso_hom`

 A global section `c` of the open subscheme `U`, read as a section of `X` over `U`, has at
`x ≫ U.ι` the value of `c` at `x`. 

### `exists_ofSection_glue`

 Descent of functions along a flat, surjective, quasi-compact `p : Y ⟶ X`. Let `V` be an open
cover of `Y`. If the functions `f a`, regular on `p ⁻¹ᵁ U ⊓ V a`, agree at points with the same
image in `X`, they are pull-backs of one section over `U`. 

 ### Regular functions 

### `exists_ofSection`

 A function that is regular on `U` agrees, at the points of `U`, with the function of a section
over `U`. 

### `pull`

 If `f` is regular on `U`, its pull-back along `p : Y ⟶ X` is regular on the preimage of `U`. 

### `ext_of_dominant_of_isOpenCover`

 Let `p : Y ⟶ X` be quasi-compact and scheme-theoretically dominant, and let `V` be an open
cover of `Y`. Functions `f`, `g` regular on `U` agree at the points of `U` if their pull-backs
agree at the points of each `p ⁻¹ᵁ U ⊓ V a`. 

### `ext_of_dominant`

 Let `p : Y ⟶ X` be quasi-compact and scheme-theoretically dominant, and let `M` be a line
bundle on `Y`. Functions `f`, `g` regular on `U` agree at the points of `U` if their pull-backs
agree at the points of each `p ⁻¹ᵁ U ⊓ M.opens a`. 


## Descent of sections and frames, the Picard group and its pull-back

* `New.LineBundle.IsIsomorphic.exists_isFrame`, `New.LineBundle.IsIsomorphic.mul`: having a frame
  is invariant under isomorphism, and isomorphism is compatible with tensor products.


### `transition_mul_transition`

 At the points of `K.opens i ⊓ K.opens j` the transition functions `K.transition i j` and
`K.transition j i` of a line bundle are inverse to each other. 

### `isUnit_transition`

 A transition function `K.transition i j` of a line bundle is a unit at the points of
`K.opens i ⊓ K.opens j`. 

### `exists_isSection_eq_mul`

 Let `π : Y ⟶ X` be flat, surjective and quasi-compact, and let `u` be a section of the
pullback of `M ⊗ L⁻¹` along `π` whose value at a point of `Y` depends only on its image in `X`.
Then the product of `u` with a section `s` of `L` descends to a section `r` of `M`, with `r i`
zero at the points that do not land in `M.opens i`. 

### `IsSection.isFrame_of_eq_mul`

 Let `p : Y ⟶ X` be surjective. A section `r` of `M` is a frame if its pullback along `p` is
the product of a frame `u` of the pullback of `M ⊗ L⁻¹` and the pullback of a frame `s` of `L`. 

### `exists_section_mul`

 Let `π : Y ⟶ X` be flat, surjective and quasi-compact, and let `u` be a section of the
pullback of `M ⊗ L⁻¹` along `π` whose value at a point of `Y` depends only on its image in `X`.
Then the product of `u` with a section `s` of `L` descends to a section `r` of `M`, with `r i`
zero off `M.opens i`, which is a frame if `u` and `s` are frames. 

### `exists_isFrame_of_fpqc`

 fpqc descent: a line bundle L on X has a nowhere vanishing global section if its pull-back
along a flat, surjective, quasi-compact π: Y → X has one whose values at ring-valued points
depend only on their images under π. 

### `IsIsomorphic.refl`

 Every line bundle is isomorphic to itself. 

### `IsIsomorphic.exists_isFrame`

 A line bundle `L` that is isomorphic to a line bundle `M` with a frame has a frame itself. 

### `IsSection.pull`

 Pulling back a section of a line bundle gives a section of the pulled-back bundle. 

### `IsFrame.pull`

 Pulling back a frame of a line bundle gives a frame of the pulled-back bundle. 

### `IsFrame.inv`

 The pointwise inverse of a frame `u` of `L` is a frame of the dual bundle `L.inv`. 

### `IsFrame.mul`

 The products of the values of a frame of `L` and a frame of `M` form a frame of `L.mul M`. 

### `IsFrame.comp_of_le`

 Let `e : κ → ι` send each open of `M` into an open of `L`, and let the transition function
`M.transition a b` agree with `L.transition (e a) (e b)` at the points of
`M.opens a ⊓ M.opens b`. Then a frame `u` of `L` restricts to the frame `u ∘ e` of `M`. 

### `IsIsomorphic.mul`

 Isomorphism of line bundles is compatible with tensor products: if `L ≅ M` and `N ≅ P`, then
`L.mul N` is isomorphic to `M.mul P`. 

### `IsFrame.exists_eq_mul`

 If `u` is a frame of `L`, every section `s` of `L` is `c * u` at the points of the cover, for a
global function `c` on `X`. 

### `LineBundle.IsIsomorphic.symm`

 Isomorphism of line bundles is symmetric: inverting a frame of `L ⊗ M⁻¹` gives `L⁻¹ ≅ M⁻¹`,
so `M ⊗ L⁻¹ ≅ M ⊗ M⁻¹`, and the latter has a frame. 

### `LineBundle.IsIsomorphic.trans`

 Isomorphism of line bundles is transitive: `L ≅ M` gives `L ⊗ N⁻¹ ≅ M ⊗ N⁻¹`, and the latter
has a frame if `M ≅ N`. 

 ### The Picard group 

### `Pic`

 The Picard group of `X`: line bundles given by a cover and a cocycle, modulo isomorphism. The
group law is written additively. 

### `LineBundle.picClass`

 The class of the line bundle K in the Picard group of X. 

### `LineBundle.picClass_eq_iff`

 Two line bundles have the same class in the Picard group if and only if they are isomorphic. 

### `LineBundle.picClass_eq_of_le`

 Let `e : κ → ι` send each open of `M` into an open of `L`, that is, `M.opens a ≤ L.opens (e a)`.
Suppose that at every point in `M.opens a` the transition functions agree:
`M.transition a b = L.transition (e a) (e b)`. Then `L` and `M` have the same class in the Picard
group. 

### `LineBundle.picClass_mul_assoc`

 The tensor product of line bundles is associative up to isomorphism. 

### `LineBundle.picClass_mul_comm`

 The tensor product of line bundles is commutative up to isomorphism. 

### `LineBundle.picClass_mul_one`

 The trivial line bundle is neutral for the tensor product up to isomorphism. 

### `LineBundle.picClass_mul_inv`

 The tensor product of a line bundle with its dual is isomorphic to the trivial bundle. 

### `instance : Add (Pic X)`

 The sum in the Picard group is the tensor product of line bundles. 

### `instance : Neg (Pic X)`

 The negative in the Picard group is the dual line bundle. 

### `instance : Zero (Pic X)`

 Zero in the Picard group is the class of the trivial line bundle. 

### `LineBundle.exists_isFrame_of_picClass_eq_zero`

 A line bundle with zero class in the Picard group has a nowhere vanishing section. 

### `pull`

 For p: Y → X, the homomorphism Pic X → Pic Y sending the class of a line bundle to the class
of its pull-back. 

### `pull_comp`

 Pull-back along `q ≫ p` is pull-back along `p` followed by pull-back along `q`. 

### `eq_zero_of_isLocalRing`

 The Picard group of the spectrum of a local ring `A` is trivial. 
