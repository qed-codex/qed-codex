---
{
  "module": "src/Lib/Shimura/ThetaModuli/ThetaFamilyRigidity.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Shimura/ThetaModuli/ThetaFamilyRigidity.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Shimura/ThetaModuli/ThetaFamilyRigidity.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Theta objects of PEL moduli problems, their pull-backs, and rigidity over local rings

The moduli problem for a PEL datum `D : New.PEL E` is studied through one family `New.ThetaFamily`.
An object is rigid if it satisfies a constancy and spanning condition over Noetherian local rings.
Over a local Noetherian ring, rigidity yields a criterion for points in the kernel of the
polarisation to vanish. It also yields the identification of objects related by compatible
homomorphisms.

## Main definitions and results

* `New.ThetaFamily`: an abelian scheme with `𝓞 E`-action, theta coordinates and level points.
* `New.ThetaObject`: a point of the base; its abelian scheme, bundle and level points are
  pull-backs.
* `New.ThetaObject.FullLevelStructure`, `New.ThetaObject.FullLevelStructure.exists_pullback`:
  trivialisations of all torsion, and their pull-back along a local homomorphism to `ℂ`.
* `New.ThetaObject.HasSpanningCoords`: constant functions and spanning coordinates on every
  pull-back to a Noetherian local ring; such an object is called rigid.
* `New.ThetaObject.HasSpanningCoords.eq_zero_of_pairing_eq_zero`: a criterion, in characteristic
  `l`, for a point in the kernel of the polarisation to be zero.
* `New.ThetaObject.HasSpanningCoords.eq_and_comp_toFamily_eq_of_hom`: for two objects with the same
  map `𝓞 E → B`, a homomorphism that respects the action, the pairing and the level points
  identifies them.

Notions from other files:
* `New.PEL.levelTorsion`: the level module: the O_E-submodule of (𝔸_f / Ô)^rank of elements killed
  by the level 𝔑.
* `New.Pic.pairing`: for c in Pic A and T-points x, y of A, the class
  ⟨x, y⟩ = (x + y)^*c − x^*c − y^*c + 0^*c in Pic T.
* `New.Variety.IsSectionLift`: a map H⁰(L) → H⁰(L') that is pull-back along f followed by some
  isomorphism f^*L ≅ L'; `New.Variety.IsTranslationLift` is the case of a translation, L' = L.

## Relation to the literature

Known; see `Lib.Shimura.ThetaModuli.UniversalFamily`,
`Lib.Cohomology.ProjectiveLine.ConstantLineFormula` and `Lib.Shimura.IntegralModel.UniversalFamily`
for sources.


 ## Theta objects of a family and their pull-backs along base morphisms 

### `ThetaFamily`

 A family for the PEL data `D`: an abelian scheme `total` with `𝓞 E`-action over an
`𝓞 E`-scheme `S`, of relative dimension `New.Variety.abelianDim E D.Index`, with a line bundle
`lineBundle` whose coordinates separate points and with level points `levelPoints`. Over local
rings the coordinates are theta coordinates (`theta_law`), and the action on the Lie algebra
satisfies a rank one condition (`signature`). An affine point of `S` over `𝓞 E` is determined by
the coordinates of its level points (`eq_of_level_coords_eq`). No universal property is asked
for. 

### `ThetaFamily.total`

 The total space `A`, a scheme over `S`. 

### `ThetaFamily.isAbelianScheme`

 `total` is an abelian scheme over `S`. 

### `ThetaFamily.moduleObj`

 The action of `𝓞 E` on `total` by endomorphisms. 

### `ThetaFamily.lineBundle`

 The line bundle 𝒩 on `total`, with cover and coordinates indexed by `D.dualTorsion`. 

### `ThetaFamily.embeds`

 `total` is proper over `S`, and `lineBundle` is a linear system whose coordinates separate
  the points of `total` over `S`. 

### `ThetaFamily.levelPoints`

 The level points: an `𝓞 E`-linear map from the 𝔑-torsion to the sections of `total`. 

### `ThetaFamily.theta_law`

 The theta law: take any base change to a local ring. Restrict the pulled-back level points to
  `D.dualTorsion`. Then the coordinates of `lineBundle` are theta coordinates for the Lagrangian
  `D.lagrangian` and some bicharacter `c`. 

### `ThetaFamily.class_laws`

 The class of `lineBundle` satisfies the three identities of `PEL.HasClassLaws`. 

### `ThetaFamily.signature`

 The signature condition: over a local ring there are coordinates at `0` in which `c` acts on
  the Lie algebra by a matrix `m c`, and `m (β̄ - b) - (β - b)` has its image on a line on which
  `𝓞 E` acts by scalars, through the structure map. 

### `ThetaFamily.relative_dim`

 `total` is smooth over `S` of relative dimension `abelianDim E D.Index`. 

### `ThetaFamily.eq_of_level_coords_eq`

 A point of `S` over `𝓞 E` with affine source is determined by its list, the coordinates of the
  level points. 

 ### Objects and their data 

### `ThetaObject`

 An object of the family X over a scheme T: a morphism from T to the base of X. 

### `groupScheme`

 The group scheme with O_E-action of an object x over S: the pull-back of the abelian scheme
of the family along x : S → base. 

### `toFamily`

 The projection from the abelian scheme of an object x to that of the family X, as a morphism
over the base of X. 

### `isGroupBaseChange`

 The projection `x.toFamily` is a base change of the abelian scheme of the family along `x` that
respects the group law and the `𝓞 E`-action. 

### `smoothOfRelativeDimension`

 The abelian scheme of an object is smooth of relative dimension
`New.Variety.abelianDim E D.Index`. 

### `lineBundle`

 The line bundle, with its coordinates, on the abelian scheme of an object: the pull-back of the
bundle `X.lineBundle` of the family along the projection. 

### `isProjEmbedding`

 The line bundle of an object is a linear system whose coordinates separate points over `S`. 

### `levelPoints`

 The level points of an object: the O_E-linear map from the 𝔑-torsion of (𝔸_f / Ô)ⁿ to
sections of its abelian scheme, pulled back from those of the family. 

### `levelPoints_comp_toFamily`

 The level points of an object lie over those of the family. 

### `hasClassLaws`

 The class of the line bundle of an object satisfies the identities of `PEL.HasClassLaws`. 

### `pairing_pow_smul_adjoint`

 For the class of the line bundle of an object, `(β - b) ^ k` is adjoint to `(β̄ - b) ^ k`,
where `β̄ = star β`: `⟨(β - b) ^ k • y, z⟩ = ⟨y, (β̄ - b) ^ k • z⟩` for the pairing of the class. 

 ### Pull-backs of objects 

### `IsPullbackAlong`

 The object x' is the pull-back of the object x along b: x' is x∘b. 

### `schemeMap`

 For x' the pull-back of x along b, the S-morphism from the abelian scheme of x' to that of x
that commutes with the projections to the family. 

### `isGroupBaseChange`

 For x' the pull-back of x along b, the map `New.ThetaObject.IsPullbackAlong.schemeMap` is a base
change along b that respects the group law and the `𝓞 E`-action. 

### `levelPoints_eq_pullSection`

 The level points of the pull-back `x'` are the pull-backs of those of `x`. 

### `exists_isPullbackAlong`

 Every object has a pull-back along `b`, namely `b ≫ x`. 

 ### Objects over a ring: full structures and logarithms on infinitesimal points 

### `baseHom`

 For an object y over Spec R, the ring homomorphism O_E → R induced by y and the structure
morphism of the base of the family to Spec O_E. 

### `FullLevelStructure`

 A full structure on an object `y` over `R`: an injective `𝓞 E`-linear map from `(𝔸_f / Ô)ⁿ` to
the sections of `y.groupScheme` that extends the level points. The field `weil_pairing` prescribes
the commutator pairing: for each `ι : R → ℂ` there is a unit `ε` of `Ẑ` such that, for `m`-torsion
points `x`, `z`, lifts of the two translations to `y.lineBundle.pow m` commute on coordinates up to
a scalar `c` with `ι c = ψ_f (ε m ξ zᴴ x)`. 

### `FullLevelStructure.torsionPoint`

 The `𝓞 E`-linear map from all torsion, `(𝔸f E / Ô E)ⁿ`, to the sections of `y.groupScheme`. 

### `FullLevelStructure.injective`

 The map `torsionPoint` is injective. 

### `FullLevelStructure.levelPoints_eq`

 The map `torsionPoint` extends the level points of `y`. 

### `FullLevelStructure.weil_pairing`

 For each `ι` there is a unit `ε` of Ẑ with this property: for `m`-torsion points `x`, `z`,
  lifts of the two translations to `y.lineBundle.pow m` commute on coordinate sections up to a
  scalar `c`, where `ι c = ψf (ε * m * xiForm D.ξ x z)`. 

### `IsPullbackAlong.baseHom_eq_comp`

 If `y` over `K` is the pull-back of `x` over `R` along `φ : R → K`, then the homomorphism from
`𝓞 E` given by `y` is that given by `x` followed by `φ`. 

### `IsTangentLogAt`

 The properties of a logarithm at one point. Here `ω` maps the `C`-points of `y.groupScheme` to
`C` for all rings `C`, `x` is a `C`-point, `ψ : C → C'` is a ring map and `b` is an integer.
`New.ThetaObject.IsTangentLog` asks these properties when `ψ` is onto with square-zero kernel and
`x` vanishes modulo that kernel. 

### `IsTangentLogAt.map_smul`

 `ω` turns `c •` into multiplication by `y.baseHom c`. 

### `IsTangentLogAt.smul_eq_zero_of_eq_zero`

 A zero of `ω` is killed by `star β - b`. 

### `IsTangentLogAt.map_add`

 `ω` is additive on the points that vanish modulo the kernel of `ψ`. 

### `IsTangentLogAt.infinitesimal`

 The value of `ω` lies in the kernel of `ψ`. 

### `IsTangentLogAt.naturality`

 `ω` commutes with a change of rings `χ : C → C₁`. 

### `IsTangentLog`

 `ω` is a logarithm of `y` along the line of the signature for `b`: it satisfies
`New.ThetaObject.IsTangentLogAt` at every point that vanishes modulo a square-zero kernel. 

### `exists_isTangentLog`

 Let `y` be an object of the family over a local ring `R` such that the ring map
`y.baseHom : 𝓞 E → R` induced by `y` kills `β - b` for an integer `b`. Then `y` has a logarithm
along the line of the signature for `b` (`New.ThetaObject.IsTangentLog`), the line of the Lie
algebra that contains the image of `star D.β - b` (field `signature` of the family). This is a map
`ω` that sends, for every ring `C` and every `t : Spec C ⟶ Spec R`, each `C`-point over `t` of the
group scheme `y.groupScheme` to an element of `C`, and that satisfies
`New.ThetaObject.IsTangentLogAt` at every point that vanishes modulo a square-zero kernel. 

### `exists_tangent_log`

 The five properties of a logarithm (`New.ThetaObject.exists_isTangentLog`) as one conjunction:
(a) equivariance, (b) kernel, (c) additivity, (d) infinitesimal values, (e) naturality. 

### `FullLevelStructure.exists_isTranslationLift`

 Let the object be over a local ring. Then the translation by an `m`-torsion point of a full
structure lifts to `y.lineBundle.pow m`, the `m`-th power of the line bundle of `y`. 

### `FullLevelStructure.exists_pullback`

 Let `y` be an object of the family `X` over a local ring `R`, `φ : R → ℂ` a local homomorphism,
and `y'` the pull-back of `y` along `φ` (`h_pb`). A full structure `e` on `y` is an injective
`𝓞 E`-linear map `torsionPoint` from `(𝔸_f / Ô)ⁿ` to the sections of the group scheme that extends
the level points and has the prescribed commutator pairing (`weil_pairing`). The claim is that there
is a full structure `e'` on `y'` whose map is `e.torsionPoint` followed by pulling sections back
along the base change. 

 ## Rigid objects; the theta structure of an object over a local ring 

### `HasSpanningCoords`

 On every pull-back of x to a noetherian local ring B, global functions on the abelian scheme are
constant and the coordinate sections of `y.lineBundle` span its H⁰ over B. Such an object is called
rigid. 

### `thetaConstants`

 The constants of the theta structure of an object `x` over a local ring: the family of
characters `c s` chosen by the field `theta_law` of the family for `x`. 

### `isThetaStructure`

 Over a local ring, the linear system of an object is a theta structure for the restriction of
the level points to the group `D.dualTorsion` and the Lagrangian `D.lagrangian ∩ D.dualTorsion`,
with the constants `x.thetaConstants`. 


## Consequences of rigidity: the polarisation kernel and compatible maps

Two consequences of rigidity for objects of a family `New.ThetaFamily` of abelian schemes embedded
by theta coordinates, over a local noetherian ring.

For a class `c`, `c.atPoint y` is `y^* c`.


### `eq_zero_of_pairing_eq_zero`

 Let `x` be a rigid object (`New.ThetaObject.HasSpanningCoords`) over a field `k` of prime
characteristic `l`: on every pull-back of `x` to a noetherian local ring, the global functions on
the abelian scheme are constant and the coordinates span the sections of the line bundle. Let `w` be
a pull-back of `x` to `S`, and `y` a point of `w.groupScheme` with values in a local noetherian ring
`B`. Suppose that (a) `l ^ m` kills the restriction of `y` to some nonempty affine scheme over
`Spec B`, and (b) `y` is in the kernel of the polarisation: it pairs to zero (`New.Pic.pairing`)
with every point, after any base change. Then `y = 0`. 

### `eq_and_comp_toFamily_eq_of_hom`

 Rigidity. Let x be a rigid object (`New.ThetaObject.HasSpanningCoords`) over the field k, x₁ its
pull-back along b to a local noetherian ring B, and x₂ another object over B. Let j : x₁ → x₂ be an
O_E-linear homomorphism of the group schemes that respects the maps from O_E (`h_baseHom`), the
pairings of the line bundles (`h_pairing`) and the level points (`h_levelPoints`). Then x₁ = x₂, and
j commutes with the projections to the family. 
