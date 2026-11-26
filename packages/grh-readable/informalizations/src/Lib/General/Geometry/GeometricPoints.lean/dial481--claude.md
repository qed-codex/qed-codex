---
{
  "module": "src/Lib/General/Geometry/GeometricPoints.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Geometry/GeometricPoints.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Geometry/GeometricPoints.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Geometric points, specialisation, separating products and integral abelian varieties

Let `k` be an algebraically closed field. For schemes and morphisms locally of finite type, points
with values in `k` detect nonempty locally closed sets and images of morphisms, and this is used to
spread properties over commutative group schemes.
Smooth morphisms are shown to be geometrically reduced, and abelian schemes over `k` are shown to be
integral. The file also records that flat morphisms are injective on stalks. Finally it gives
criteria for families of complex points to be separating over a stalk of the base and on a product
of flat schemes.

## Main definitions and results

* `New.exists_section_mem`, `New.exists_point_mem`: a nonempty locally closed set in a scheme
  locally of finite type over `k` contains a `k`-point.
* `New.IsDenseFamily.of_fibres`: if the complex points `η i` are dense in `S` and `A` is smooth over
  `S`, a family containing every complex point of `A` over the `η i` is dense in `A`.
* `New.AddObj.property_of_isOpenImmersion`: take a commutative group scheme (`New.AddObj`) locally
  of finite type over `k`. A property induced by a property of ring maps spreads from a nonempty
  open part to the whole scheme, by translation.
* `New.AddObj.smoothOfRelativeDimension_of_fibres`: the relative dimension of an abelian scheme can
  be read off the fibres through a dense family of points.
* `New.isSeparatingFamily_stalk`: for `A` and `S` reduced and dense points of `A` with finitely many
  images in `S`, the lifts of those that factor through a stalk of `S` separate the base change of
  `A` to that stalk.
* `New.IsSeparatingFamily.prod`: separating points of `B`, paired with dense points of the fibres of
  `A` over their images in `S`, separate `A ×_S B`, for `A`, `B` flat and locally of finite type,
  `A` reduced, and `S` reduced, locally noetherian, with finitely many dense complex points.

Notions from other files:
* `New.IsDenseFamily`: the images of a family of complex points are dense.
* `New.IsSeparatingFamily`: the family is dense and the scheme is reduced.
* `New.IsAbelianScheme`: a smooth proper commutative group scheme on which multiplication by every
  `m ≠ 0` is surjective.
* `New.translation`: translation x ↦ x + z by a section z of a commutative group scheme.

## Relation to the literature

Known; see `Lib.Shimura.AbelianScheme.IsogenyFlatness` for sources.


 ## Points over algebraically closed fields 

### `exists_section_mem`

 A nonempty locally closed subset of a scheme `X` locally of finite type over an algebraically
closed field `k` contains the image of a `k`-point, that is, of a section `x : Spec k ⟶ X` of the
structure morphism `s`. 

### `exists_point_mem`

 Let `X` be a scheme over `Spec k`, locally of finite type, with `k` an algebraically closed
field. A nonempty locally closed subset `S` of `X` contains the image of a `k`-point, that is, of a
morphism over `Spec k` from the unit object `𝟙_` (`Spec k` over itself) to `X`. This is
`New.exists_section_mem` in the category of schemes over `Spec k`. 

### `exists_point_over`

 Let f : X → S be locally of finite type, k algebraically closed and t a k-point of S. If the
image of t lies in the image of f, then there is a k-point y of X over t, that is, y ≫ f = t. 

### `IsDenseFamily.of_fibres`

 Let `f : A ⟶ S` be smooth and `η i` complex points with dense images in `S`
(`New.IsDenseFamily`). If every complex point of `A` over some `η i` is one of the points `ξ z`,
then the `ξ z` have dense images in `A`. 

### `AddObj.property_of_isOpenImmersion`

 Let `X` be a commutative group scheme (`grp`, a `New.AddObj` structure) locally of finite type
over an algebraically closed field `k`, with structure morphism `s`, and let `P` be a property of
morphisms of schemes induced by a property `Q` of ring maps. If a nonempty open subscheme
`i : Y ⟶ X` has `P` over `k`, so does `X`. 

### `exists_isStandardSmoothOfRelativeDimension`

 A standard smooth ring map is standard smooth of some relative dimension. 

### `smoothOfRelativeDimension_fromSpec_comp`

 Let `f : X ⟶ S` map the affine open `V` into the affine open `U`. If the ring map
`Γ(S, U) ⟶ Γ(X, V)` is standard smooth of relative dimension `n`, then `Spec Γ(X, V) ⟶ S` is smooth
of relative dimension `n`. 

### `AddObj.smoothOfRelativeDimension_of_fibres`

 Let `A` be an abelian scheme over `S` (`New.IsAbelianScheme`) with complex points `y i` over
`η i` whose images are dense in `A`. If `g` is the only possible relative dimension of each fibre
over `η i`, then `A` is smooth of relative dimension `g` over `S`. 


## Geometric reducedness of smooth morphisms and integral abelian varieties

Two instances. A smooth morphism of schemes is geometrically reduced (locally it is étale over a
polynomial ring, `New.Variety.isReduced_of_algebra_etale`). An abelian scheme over an algebraically
closed field is integral. Here `New.IsAbelianScheme` asks a commutative group scheme to be smooth,
proper and divisible (multiplication by each `m ≠ 0` is onto); divisibility takes the place of the
usual connectedness of the fibres, and the second instance recovers it.


### `isReduced_of_algebra_etale`

 An étale algebra over an integral domain is reduced. 

### `isReduced_of_etale`

 The form of `New.Variety.isReduced_of_algebra_etale` in which étaleness of `B` over the domain
`A` is an explicit hypothesis, from which the algebra structure is inferred. 

### `instance {X Y : Scheme.{0}} (s : X ⟶ Y) [hs : Smooth s] : GeometricallyReduced s`

 A smooth morphism of schemes is geometrically reduced. 

### `instance {k : Type} [Field k] [IsAlgClosed k] (A : Over (Spec ⟨k⟩)) [hA : IsAbelianScheme A] : AlgebraicGeometry.IsIntegral A.left`

 An abelian scheme (`New.IsAbelianScheme`: smooth, proper and divisible) over an algebraically
closed field is integral. 


## Specialisation to geometric points and flat morphisms on stalks

`New.Variety.AllSpecializeTo S Q` says that every point of `S` specialises to a geometric point with
the property `Q`.


### `New.Variety.AllSpecializeTo`

 Every point of `S` specialises to the image of the closed point under some `t : Spec k ⟶ S` with
`k` algebraically closed and `Q t`. 

### `instance {Z : Scheme} (s : Z) : Flat (fromSpecStalk Z s)`

 For a point `s` of a scheme `Z`, the morphism from the spectrum of the stalk at `s` to `Z` is
flat. 

### `New.stalkMap_injective_of_flat`

 A flat morphism of schemes is injective on stalks. 


## Separating families of points over a stalk and on products of flat schemes

A family of complex points of a scheme is separating (`New.IsSeparatingFamily`) if the scheme is
reduced and the points are dense (`New.IsDenseFamily`); regular functions are then determined by
their values there.


### `eventually_specializes_of_finite`

 The points of a finite set `C` that lie near `s` specialise to `s`. 

### `isSeparatingFamily_stalk`

 Let `S` and `A` be reduced, `z : A ⟶ S`, `s` a point of `S`, and `x w` complex points of `A`
with dense images and with finitely many composites `x w ≫ z`. Consider the pairs of an index `w`
and a map `ψ` from the stalk `𝒪_{S,s}` to `ℂ` such that `x w ≫ z` factors through `Spec 𝒪_{S,s}`
via `Spec.map ψ`. The points `(x w, Spec.map ψ)` of `A ×_S Spec 𝒪_{S,s}` form a separating family:
this scheme is reduced and the images of these points are dense. 

### `stalk_eq_zero_of_forall_factor`

 Let `S` be reduced with finitely many complex points `ξ i` whose images are dense. An element
`a` of the stalk at `x` is zero if `ψ a = 0` for every map `ψ` from the stalk to `ℂ` such that
some `ξ i` factors through the spectrum of the stalk via `Spec.map ψ`. 

### `stalk_eq_zero_of_dense`

 The form of `New.stalk_eq_zero_of_forall_factor` in which the index `i`, the map `ψ` from the
stalk to `ℂ` and the factorisation of `ξ i` via `Spec.map ψ` are bundled into one triple `p` (so
that `p.snd.fst` is `ψ`): for `S` reduced with finitely many dense complex points `ξ i`, an element
`a` of the stalk at `x` is zero if `ψ a = 0` for every such triple. 

### `dense_smoothLocus_of_isDenseFamily`

 Let X be reduced, locally noetherian, flat and locally of finite type over a reduced locally
noetherian scheme S with finitely many complex points whose images are dense. Then the smooth
locus of X over S is dense in X. 

### `IsSeparatingFamily.prod`

 Let S be reduced and locally noetherian, with a finite family of complex points whose images are
dense. Let A and B be flat and locally of finite type over S, with A reduced. Let η_w be complex
points of S, and let y_w be complex points of B over η_w that separate B, meaning B is reduced and
the images of the y_w are dense. Suppose that for each w the complex points e_w(v) of A over η_w
have dense image in the fibre A ×_S Spec ℂ over η_w. Then the complex points (e_w(v), y_w) separate
A ×_S B: it is reduced and their images are dense (`New.IsSeparatingFamily`). 
