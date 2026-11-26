---
{
  "module": "src/Lib/Shimura/Uniformisation/TorusModel.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Shimura/Uniformisation/TorusModel.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Shimura/Uniformisation/TorusModel.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Objects modelled on complex tori and their homomorphisms as rational matrices

This file models the objects of a PEL family `X` (`New.ThetaFamily`) over a valuation ring with
fraction field ℂ on complex tori `V` modulo a lattice given by a polarised period map. It then
describes homomorphisms of modelled objects by matrices `z ∈ GL_n(E)`.

## Main definitions and results

* `New.ThetaObject.TorusModel`: `y.groupScheme` is uniformised by `V` modulo that lattice, with
  theta coordinates.
* `New.ThetaTori.PeriodMap.exists_uniformisation_of_isSeparatingFamily`: a dense map given by theta
  functions is a uniformisation.
* `New.ThetaObject.TorusModel.fullStructure`: a model trivialises all torsion, compatibly with the
  Weil pairing. `New.ThetaObject.TorusModel.exists_unit_on_roots_of_unity` supplies the unit of Ẑ
  through which a ring homomorphism `O → ℂ` acts on roots of unity.
* `New.ThetaObject.TorusModel.exists_isTranslationLift_of_dualLattice` (with its parts
  `New.ThetaObject.TorusModel.card_nsmul_mem_of_mem_dualLattice` and
  `New.ThetaObject.TorusModel.exists_isTranslationLift_of_mem_dualLattice`),
  `New.ThetaObject.TorusModel.multiplier_eq_canonicalMultiplier`: translations by the dual lattice
  lift to `y.lineBundle`, and the multiplier of the theta coordinates is the canonical one.
* `New.ThetaObject.TorusModel.exists_matrix_of_hom`: a linear `ψ` of multiplier `μ ≠ 0` comes from a
  `z`.
* `New.ThetaObject.TorusModel.exists_isIsogenyOfMatrix`,
  `New.ThetaObject.TorusModel.exists_isogeny`: a `z` with `z ℓ z⁻¹ = ℓ'` and `g'⁻¹ z g` an integral
  similitude of multiplier `μ` gives an isogeny (`New.ThetaObject.TorusModel.IsIsogenyOfMatrix`);
  objects with models have the same map from `𝓞 E`
  (`New.ThetaObject.TorusModel.baseHom_eq_baseHom`).

Notions from other files:
* `New.ThetaTori.PeriodMap`: the linear part of a model: a real isomorphism Q from (E ⊗ ℝ)ⁿ onto V,
  a form β with frame g, and a form B on V whose Riemann form pulls back to
  `New.Variety.polarisationForm`.
* `New.Variety.frameCoords`: the map y ↦ g⁻¹y from Eⁿ to n-tuples of finite adeles.
* `New.Variety.realVecAction`: the action of a matrix A over E on (E ⊗ ℝ)ⁿ, through Φ_v(A) at the
  infinite place v.

## Relation to the literature

Known; see `Lib.Shimura.Uniformisation.AppellHumbert` and `Lib.Shimura.ThetaModuli.UniversalFamily`
for sources.



## Theta uniformisation, Weil pairing and canonical multiplier

Complex tori as models of the objects of a PEL family `X` (`New.ThetaFamily`). An object `y` over a
valuation ring `O` with fraction field ℂ (`New.ValuativeArc`) is an `O`-point of the base of `X`. It
carries an abelian scheme `y.groupScheme`, a linear system `y.lineBundle` and level points
`y.levelPoints`. A polarised period map (`New.ThetaTori.PeriodMap`) is an isomorphism
`Q : (E ⊗ ℝ)ⁿ ≃ V` with a form `B`. Its lattice consists of the `Q (toRealVectors z)` for `z ∈ Eⁿ`
with `g⁻¹ z` integral.


### `ThetaObject.TorusModel`

 The object `y` is modelled on the torus of the polarised period map `Y` onto `V`. The model is a
uniformisation of `y.groupScheme` by `V`. It is compatible with the action of `𝓞 E` and the level
points. Its kernel is the period lattice. Along it, `y.lineBundle` has theta coordinates. 

### `ThetaObject.TorusModel.baseHom_eq`

 The map `𝓞 E → O → ℂ` is the embedding `Φ v₀`. 

### `ThetaObject.TorusModel.uniformisation`

 The uniformisation of `y.groupScheme` by `V`. 

### `ThetaObject.TorusModel.χ`

 The multiplier of the theta coordinates. 

### `ThetaObject.TorusModel.θ`

 The theta coordinates, indexed by `D.dualTorsion`. 

### `ThetaObject.TorusModel.hasThetaCoords`

 Along the uniformisation, `θ` are coordinates of `y.lineBundle` and theta functions of type
  `(B, χ)`. 

### `ThetaObject.TorusModel.equivariant`

 The composite of `Q` and the uniformisation commutes with the action of `𝓞 E`. 

### `ThetaObject.TorusModel.level_eq`

 The level points are the images of the chosen rational vectors. 

### `ThetaObject.TorusModel.lattice_eq`

 The kernel of the uniformisation is the period lattice. 

### `ThetaTori.PeriodMap.multiplier_eq_of_pullback`

 Let `A` be an abelian scheme over `ℂ` embedded in projective space by `N`, and let
`e : V → A(ℂ)` be additive with image dense in the reduced scheme `A`, killing `Y.periodLattice`,
along which `N` has theta coordinates `Y.thetaCoord` of type `(Y.automorphyForm, Y.multiplier)`. Let
`u` be a uniformisation of `A` by `W` along which `N` has theta coordinates of type `(B', χ')`, and
let `F : V → W` be complex linear with `u.expMap ∘ F = e`, pulling the Riemann form of `B'` back to
that of `Y.automorphyForm`. If a line bundle `M` has theta coordinates of type `(B', χ)` along `u`
and `χ ∘ F = Y.multiplier` on `Y.periodLattice`, then `χ = χ'` on `u.lattice`. 

### `ThetaTori.PeriodMap.exists_uniformisation_of_isSeparatingFamily`

 Let `A` be an abelian scheme over `ℂ`, smooth of relative dimension `d`, embedded in projective
space by `N` whose class satisfies the parallelogram law. Let the homomorphism `e : V → A(ℂ)` have
dense image in `A` (with `A` reduced), kill `Y.periodLattice` and carry `Y.thetaCoord` as
homogeneous coordinates. Then there is a uniformisation `u` of `A` by `V` with (a) theta coordinates
`Y.thetaCoord` of type `(Y.automorphyForm, Y.multiplier)`, (b) map `e` and kernel `Y.periodLattice`;
and (c) `d = New.Variety.abelianDim E D.Index`, which is `|D.Index|` times the number of infinite
places of `E`. 

 ### The full structure of a model 

### `π`

 The map `π` of a model `m` sends (E ⊗ ℝ)ⁿ to the sections of `y.groupScheme` over `O`. It is the
period map `Q` followed by the uniformisation. 

### `exists_unit_on_roots_of_unity`

 A ring homomorphism `φ : O → ℂ` acts on roots of unity through a unit of Ẑ. Here `ψf E` is the
standard additive character of the finite adeles of `E`, whose values are roots of unity. There is
a unit `ε` of Ẑ such that each value `ψf E t` is the image of some `c ∈ O` with
`φ c = ψf E (t ε)`. 

### `expMap_periodPoint_eq_iff`

 Two rational vectors `a`, `b` give the same point of `y.groupScheme` (the images of their
periods under the uniformisation of the model `m`) exactly when their torsion classes g⁻¹a and g⁻¹b
in (𝔸_f / Ô)ⁿ agree. 

### `fullStructure`

 The full structure of a model: the class of g⁻¹a in (𝔸_f / Ô)ⁿ, for a in Eⁿ, is sent to the
torsion section `expMap (Q (toRealVectors a))`, computed at the chosen rational lift `ratLift g` of
the class. 

### `fullStructure_torsionPoint_apply`

 The torsion point of a class under `New.ThetaObject.TorusModel.fullStructure` is the section at
the period of its chosen rational lift `ratLift g`. 

### `torsionPoint_frameTorsionClass`

 `New.ThetaObject.TorusModel.fullStructure` sends the class of g⁻¹z to the section at the period
of z for every z in Eⁿ, not only for the chosen representative of the class. 

 ### The dual lattice and the multiplier of a model 

### `card_nsmul_mem_of_mem_dualLattice`

 The order of `D.dualTorsion` kills the lattice dual to `m.uniformisation.lattice` (for the
Riemann form) modulo `m.uniformisation.lattice`. 

### `exists_isTranslationLift_of_mem_dualLattice`

 Let `S` be the `O`-span of the coordinates of `y.lineBundle` and `b` a vector of the lattice
dual to `m.uniformisation.lattice` for the Riemann form. Then the translation by the section
`m.uniformisation.expMap b` has a lift `Φ` to the sections of `y.lineBundle` with `Φ S ⊆ S`. 

### `exists_isTranslationLift_of_dualLattice`

 Let `S` be the `O`-span of the coordinates of `y.lineBundle` and `b` a vector of the lattice
dual to `m.uniformisation.lattice` for the Riemann form. Then `|D.dualTorsion| • b` lies in
`m.uniformisation.lattice`, and the translation by the section `m.uniformisation.expMap b` has a
lift `Φ` to the sections of `y.lineBundle` with `Φ S ⊆ S`. 

### `multiplier_eq_canonicalMultiplier`

 Let `m` model the object `y` on the torus of the polarised period map `Y`. On the period lattice
`m.uniformisation.lattice`, the multiplier `m.χ` of the theta coordinates is χ(l) = exp(πi·e(βl,
l)). Here e is the Riemann form of B = `Y.automorphyForm`, and β = `D.β` ∈ `𝓞 E` acts on V through
`Y.intAction`, the action of `𝓞 E` transported through the period map. 


## Homomorphisms of modelled objects and rational matrices

Objects `x`, `x'` over a valuation ring `O` with fraction field `ℂ` are modelled on the tori of
`(g, ℓ)` and `(g', ℓ')`, with `g`, `g'` adelic frames and `ℓ`, `ℓ'` complex matrices.


### `torsionPoint_comp`

 If `ψ` carries `m.π w` to `m'.π (z w)` for all `w`, then it carries the torsion point of the
class of `y` in (𝔸_f / Ô)ⁿ to the torsion point of the class of `g'⁻¹ z g y` (with `toFinGL z` the
image of `z` over 𝔸_f), for every finite adelic vector `y`. 

### `exists_matrix_of_hom`

 Let `x`, `x'` be objects over `O` with torus models `m`, `m'` on the polarised period maps `Y`
(frame `g`, matrix `ℓ`) and `Y'` (frame `g'`, matrix `ℓ'`), with period maps `m.π`, `m'.π` from
`(E ⊗ ℝ)ⁿ`. Let `ψ : x.groupScheme ⟶ x'.groupScheme` be an `𝓞 E`-linear homomorphism that pulls the
Picard class of `x'.lineBundle` back to `μ ≠ 0` times that of `x.lineBundle`. Then `ψ` comes from
some `z ∈ GL_n(E)`: (a) `m.π w ≫ ψ = m'.π (z·w)` for all `w`; (b) with `Y.formMatrix` the matrix of
the form β of `Y` (not the element `D.β` of `𝓞 E`), `μ` times the polarisation form of
`Y.formMatrix` is the polarisation form of `zᴴ Y'.formMatrix z`; (c) `z ℓ z⁻¹ = ℓ'` (conjugation
through `Φ v₀`). 

### `baseHom_eq_baseHom`

 Objects with models have the same map from `𝓞 E`: after the injective map `O → ℂ`, both are
the embedding `Φ v₀`. 

### `IsIsogenyOfMatrix`

 `ψ` is an `𝓞 E`-linear isogeny from `x` to `x'` of multiplier `μ` that acts on torsion by
the adelic matrix `k` and on periods by the rational matrix `z`. 

### `IsIsogenyOfMatrix.isIsogeny`

 `ψ` is an isogeny. 

### `IsIsogenyOfMatrix.isLinear`

 `ψ` commutes with the action of `𝓞 E`. 

### `IsIsogenyOfMatrix.pull_picClass`

 `ψ` pulls the class of `x'.lineBundle` back to `μ` times that of `x.lineBundle`. 

### `IsIsogenyOfMatrix.torsionPoint_comp`

 `ψ` sends the torsion point of the class of `y` to that of `k y`. 

### `IsIsogenyOfMatrix.π_comp`

 `ψ` sends `m.π w` to `m'.π (z w)`. 

### `exists_isIsogenyOfMatrix`

 Let `x`, `x'` be objects over `O` with torus models `m`, `m'` on the polarised period maps `Y`
(frame `g`, matrix `ℓ`) and `Y'` (frame `g'`, matrix `ℓ'`). Let `z ∈ GL_n(E)` satisfy `z ℓ z⁻¹ = ℓ'`
(conjugation through `Φ v₀`), and let `k = g'⁻¹ z g` have entries in `Ô E` (the integral finite
adeles of `E`) with `IsScalarFrame k⁻¹ μ`, i.e. `μ > 0` and `μ (k⁻¹)ᴴ k⁻¹ = ε·1` for a unit `ε` of
`Ẑ`. Then some `ψ : x.groupScheme ⟶ x'.groupScheme` is an `𝓞 E`-linear isogeny from `x` to `x'` of
multiplier `μ`, acting by `k` on torsion and by `z` on periods. 

### `exists_isogeny`

 Let `z ∈ GL_n(E)` satisfy `z ℓ z⁻¹ = ℓ'` (`hz`), and let `k = g'⁻¹ z g` have integral entries
with `IsScalarFrame k⁻¹ μ` (μ > 0 and `k⁻¹` is a frame for the scalar matrix μ). Then `x` and `x'`
have the same map from `𝓞 E`, and there is an `𝓞 E`-linear isogeny `ψ` that pulls the class of
`x'.lineBundle` back to `μ` times that of `x.lineBundle` and satisfies `ψ π = π' z`. It sends the
torsion point of the class of `y` to that of `k y`, for every finite adelic vector `y`. 
