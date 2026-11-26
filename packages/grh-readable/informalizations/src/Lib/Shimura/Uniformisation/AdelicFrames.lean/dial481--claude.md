---
{
  "module": "src/Lib/Shimura/Uniformisation/AdelicFrames.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Shimura/Uniformisation/AdelicFrames.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Shimura/Uniformisation/AdelicFrames.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Adelic frames over a CM field, torsion classes, period lattices and period maps

This file develops the linear algebra over a CM field `E` used to count points. `New.CMBase E` fixes
a CM type `Φ` and a base infinite place `v₀`, where the signature condition is imposed.
`New.AdelicTorsion E n` is `(𝔸f E / Ô E)ⁿ`, an adelic model of `(E / 𝓞 E)ⁿ`. Here `𝔸f E` is the ring
of finite adeles and `Ô E` the ring of integral finite adeles. `New.Variety.torsionClass` is the
class map. Adelic frames give lattices of rational vectors in `(E ⊗ ℝ)ⁿ`, which are shown to be
discrete and full. A complex matrix gives a complex structure on this space.

## Main definitions and results

* `New.Variety.IsFrameFor β x`: `xᴴ β x` is a scalar matrix `ε • 1` with `ε` a unit of `Ẑ = Ô ℚ`.
* `New.Variety.IsSignedFrame x J`: `x` is a frame of some `β` that is positive definite at every
  infinite place other than `v₀`, with `β J` positive definite at `v₀`.
* `New.Variety.ModuliPoint`: points `(x, J, P)` at infinite level, with the action
  `New.Variety.ModuliPoint.act` and the isomorphisms `New.Variety.ModuliPoint.IsLevelIso` at a level
  `K`.
* `New.Variety.IsPeriodMap`: a map onto a complex vector space that carries the complex structure
  `i J` at `v₀` and `i` at the other infinite places to multiplication by `i`.
* `New.Variety.exists_matrix_torsionClass_eq`: an `𝓞 E`-linear map `Eⁿ → AdelicTorsion E n` is
  `y ↦ torsionClass (h y)` for an adelic matrix `h`, found by compactness of `Ô`.

Notions from other files:
* `𝔸f E`, `Ô E`: the finite adeles of `E` and the integral ones (the product of the completions of
  `𝓞 E`); `finAdeleIncl ℚ E` maps the finite adeles of `ℚ` into those of `E`.
* `New.CMType E`: a CM type, a complex embedding `Φ w` for every infinite place `w` of `E`;
  `FinComplexSpace V`: `V` is a finite-dimensional complex vector space with its topology.

## Relation to the literature

Known; see `Lib.Shimura.Uniformisation.AppellHumbert` and `Lib.Shimura.IntegralModel.TowerExistence`
for sources.



## Adelic frames, the similitude group and the signature condition

* `New.Variety.GU`, `New.Variety.GUPlus`: the finite adelic similitudes, and those whose inverse is
  integral.
* `New.Variety.IsSignedFrame.mul`: `New.Variety.IsSignedFrame x J` is kept by
  `(x, J) ↦ (z x g, z J z⁻¹)` for `z ∈ GL_n(E)` and a similitude `g`.


### `CMBase`

 A choice of one complex embedding Φ_v for each infinite place v of E, together with a base
place v₀; E has at least two infinite places.
It extends `CMType E`, so E is a CM number field. 

### `CMBase.v₀`

 The base infinite place of `E`. 

### `AdelicTorsion`

 The torsion `𝓞 E`-module `(𝔸f E / Ô E)ⁿ`: `n`-tuples of finite adeles of `E` modulo integral
ones, an adelic model of `(E / 𝓞 E)ⁿ`. 

 ### Frames and similitudes 

### `IsFrameFor`

 `x` is a frame for the form `β`: `xᴴ β x = ε • 1` (`ᴴ` is the conjugate transpose for the star
of `𝔸f E`) for a unit `ε` of `Ẑ = Ô ℚ`. 

### `IsScalarFrame`

 The rational number c is positive and x is a frame for the scalar matrix c·1: c·xᴴx = ε·1
for some unit ε of Ẑ. 

### `IsFrameFor.mul_iff`

 Let `x` be a frame for `β`. Then `x g` is a frame for `c β` exactly when `g` is a frame for
the scalar form `c • 1`. 

### `abelianDim`

 The number |n| times the number of infinite places of E; for a CM field E this is
|n|·[E⁺:ℚ], with E⁺ the maximal real subfield. 

### `GU`

 The unitary similitudes: the `g ∈ GL_n(𝔸f E)` with `c • gᴴ g = ε • 1` for some rational
`c > 0` and unit `ε` of `Ẑ`, that is, the frames of the scalar forms `c • 1`. Every finite
idele of `ℚ` has the form `ε / c`, so this says that `gᴴ g` is a scalar finite idele of `ℚ`. 

### `GUPlus`

 The monoid of similitudes `g` whose inverse has integral entries, that is, which enlarge the
standard lattice. It is the intersection of `GU` with the inverse of the monoid of integral
matrices, with the carrier written out. 

### `torsionClass`

 The `𝓞 E`-linear map sending a vector of finite adeles to its class in `(𝔸f E / Ô E)ⁿ`. 

### `instance : Algebra E ℂ`

 `E` is a subfield of `ℂ` through the embedding `Φ v₀` at the base place. 

 ### Reflections and the signature condition 

### `toFinGL`

 The diagonal embedding of `GL n E` in `GL n (𝔸f E)`. 

### `IsReflection`

 A reflection: `J = u wᵀ - 1` with `w ⬝ᵥ u = 2`, so `J` is `1` on the line of `u` and `-1` on
the kernel of `w`. 

### `IsSignedFrameFor`

 `x` is a frame for `β`, the matrix `β.map (Φ w)` is positive definite for every infinite place
`w ≠ v₀`, and `β.map (Φ v₀) * J` is positive definite (the `ite` joins the two cases). 

### `IsSignedFrame`

 `x` is a frame for some form `β` over `E` with the positivity conditions of
`IsSignedFrameFor`. 

### `ratConj`

 The conjugate `Φ v₀ (z) * J * Φ v₀ (z)⁻¹` of the complex matrix `J` by `z` in `GL n E`, taken
through the embedding `Φ v₀`. 

### `IsReflection.conj`

 Every conjugate of a reflection is a reflection. 

### `IsFrameFor.conj_iff`

 Changing the form `β` to `zᴴ β z`, for `z` in `GL_n(E)`, corresponds to multiplying the frame by
`z` on the left. 

### `IsSignedFrame.mul`

 The signature condition is kept when `x` is multiplied by a rational matrix `z` on the left
and a similitude `g` on the right, and `J` is conjugated by `z` at the base place:
`ratConj z J = Φ v₀ (z) J Φ v₀ (z)⁻¹`, where `Φ w` is the complex embedding of `E` at the infinite
place `w` given by the CM type and `v₀` is the base place. 


## Torsion classes of adelic vectors

* `New.torsionClass_eq_iff`: two vectors have the same class exactly when their difference is
  integral at every entry.


### `torsionClass_induction`

 Induction on torsion classes: a property of all classes `torsionClass y` holds for every element
of `AdelicTorsion E n`. 

### `isOpen_preimage_torsionClass`

 `AdelicTorsion E n` is discrete: the preimage of every set under `torsionClass` is open. 

### `torsionClass_mulVec_eq_zero`

 An integral matrix maps vectors of torsion class zero to vectors of torsion class zero. 


## Points at infinite level, period lattices and period maps

The dictionary between adelic data and complex tori.


 ### The real space and points at infinite level 

### `RealVectors`

 The space `(E ⊗ ℝ)ⁿ`, written as `n`-tuples of elements of the product of copies of `ℂ` over
the infinite places of `E`. 

### `ModuliPoint`

 A complex point at infinite level: a finite adelic matrix `frame` (written `x` in the comments),
a complex matrix `reflection` (written `J` in the comments) that satisfies the signature condition
`New.Variety.IsSignedFrame` at `v₀` together with `x`, and marked vectors `markedPoint i` (written
`P i` in the comments) in `(E ⊗ ℝ)ⁿ`. 

### `ModuliPoint.frame`

 The finite adelic matrix `x`, which gives the lattice `Eⁿ ∩ x Ôⁿ`. 

### `ModuliPoint.reflection`

 The complex matrix `J`, which gives the complex structure at the place `v₀`. 

### `ModuliPoint.markedPoint`

 The marked points, given by representatives in `(E ⊗ ℝ)ⁿ`. 

### `ModuliPoint.isSignedFrame`

 `(x, J)` is a signed frame: `x` is a frame for some matrix `β` over `E` with `Φ_{v₀}(β) J` and
  all `Φ_v(β)`, `v ≠ v₀`, positive definite. 

### `ModuliPoint.isReflection`

 `J` is a reflection: `1` on a line and `-1` on a complement. 

 ### Rational vectors, frames and lattices 

### `cmEmbedding`

 The ring homomorphism `x ↦ (Φ_v(x))_v` from `E` to the product of copies of `ℂ` over the
infinite places `v`, given by the CM type `Φ`. 

### `realVecAction`

 The action of a matrix `β` over `E` on `(E ⊗ ℝ)ⁿ`: `Φ_v(β)` at the infinite place `v`. 

### `toRealVectors`

 The additive map `Eⁿ → (∏_v ℂ)ⁿ` applying the CM embedding `x ↦ (Φ_v(x))_v` to each
coordinate. 

### `frameCoords`

 The coordinates of a rational vector in the adelic frame `g`: the `E`-linear map `y ↦ g⁻¹ y`
from `Eⁿ` to `n`-tuples of finite adeles. 

### `frameTorsionClass`

 The `𝓞 E`-linear map sending `y` in `Eⁿ` to the class of the adelic vector `g⁻¹ y` in the
torsion module `(𝔸f / Ô)ⁿ`. 

### `classLattice`

 The image in `V`, under the CM embedding followed by `Q`, of the group of `y` in `Eⁿ` such that
the class of `g⁻¹ y` in `(𝔸f / Ô)ⁿ` lies in `S`. 

### `frameLattice`

 The lattice `Eⁿ ∩ g Ôⁿ`, as an additive subgroup of `(E ⊗ ℝ)ⁿ` through the CM embedding. 

### `IsPeriodMap`

 `Q` is a period map for the complex matrix `ℓ`: it carries the real endomorphism of
`(E ⊗ ℝ)ⁿ` given by `i ℓ` at the place `v₀` and by `i` at the other infinite places to
multiplication by `i` on `V`. 

 ### The action on points and isomorphisms at a level 

### `ModuliPoint.act`

 The action on a point `a = (x, J, P)` of an adelic similitude `g` and of integers `α i` of
`E`: the result is `(x g, J, α i • P i)`, where `α i` acts on `(E ⊗ ℝ)ⁿ` through the CM type. 

### `ModuliPoint.IsLevelIso`

 The matrix `z` in `GL n E` is an isomorphism from `a = (x, J, P)` to `b = (x', J', P')` at
level `K`: `x'⁻¹ z x` lies in `K`, `z J z⁻¹ = J'` through `Φ v₀`, and `z (P i) - P' i` lies in
the lattice of `x'`. 

### `ModuliPoint.IsLevelIso.mem_level`

 With `x`, `x'` the adelic matrices of `a` and `b`, the matrix `x'⁻¹ z x` lies in `K`. 

### `ModuliPoint.IsLevelIso.reflection_eq`

 `z` conjugates the reflection of `a` to that of `b`: `z J z⁻¹ = J'`, through `Φ v₀`. 

### `ModuliPoint.IsLevelIso.sub_mem_lattice`

 `z` carries each marked point of `a` to that of `b`, modulo the lattice of `x'`. 


## Lattices of rational vectors with given torsion class

Rational vectors `y ∈ Eⁿ` have a torsion class `New.Variety.frameTorsionClass g y`, the class of
`g⁻¹ y` in `(𝔸_f / Ô)ⁿ`, and an image `New.Variety.toRealVectors y` in `(E ⊗ ℝ)ⁿ` by the CM type.


 ### Torsion classes of rational vectors 

### `ker_frameTorsionClass_one`

 For the trivial frame `g = 1`, the vectors `y` of `Eⁿ` whose class in `(𝔸f / Ô)ⁿ` vanishes are
those with all coordinates in `𝓞 E` (the submodule `1` of `E` over `𝓞 E`). 

### `denseRange_frameCoords`

 The coordinates `g⁻¹ y` of the rational vectors `y` are dense in `(𝔸f E)ⁿ`. 

### `frameTorsionClass_surjective`

 Every class in `(𝔸f / Ô)ⁿ` is the class of `g⁻¹ y` for a rational vector `y`. 

 ### The embedding by the CM type and the lattices 

### `mem_classLattice`

 `x` lies in `classLattice g S Q` if and only if it is `Q` of the CM embedding of a rational
vector `y` whose class lies in `S`. 

### `realVecAction_mem_frameLattice`

 If `g'⁻¹ A g` is integral, then `A` maps the lattice `Eⁿ ∩ g Ôⁿ` into `Eⁿ ∩ g' Ôⁿ`. 

### `denseRange_toRealVectors`

 The image of `Eⁿ` under the CM embedding is dense in `(E ⊗ ℝ)ⁿ`. 

### `instance : DiscreteTopology (classLattice g ⊥ Q)`

 The lattice `classLattice g ⊥ Q` of rational vectors `y` with `g⁻¹ y` integral is discrete in
`V`. 

### `instance [DiscreteTopology (classLattice g S Q)] : IsZLattice ℝ (classLattice g S Q)`

 A discrete `classLattice g S Q` is a full lattice in `V`: it spans `V` over `ℝ`. 


## Period maps: dimension, conjugation and complex multiplication

Linear algebra of a period map `Q : (E ⊗ ℝ)ⁿ ≃ V`, a real isomorphism from
`New.Variety.RealVectors E n` onto a complex vector space.

* `New.Variety.IsPeriodMap.ratConj_eq`: a complex linear map induced by `z ∈ GL n E` conjugates the
  two complex structures.


### `BallBase`

 The complex vector space `ℂ ^ (n − 1)` (`n` the number of indices), which contains the parameter
domains of the families of periods. 

### `BallFibre`

 The complex vector space `ℂ × ℂ ^ (n − 1) × ∏_v ℂ ^ n`, the product over the infinite places
`v` of `E` other than `v₀`. 

### `finrank_eq_abelianDim`

 If `(E ⊗ ℝ)ⁿ` is isomorphic over `ℝ` to the complex vector space `V`, the complex dimension of
`V` is `abelianDim E n`, the number of indices times the number of infinite places of `E`. 

### `IsPeriodMap.finrank_eq_abelianDim`

 `finrank_eq_abelianDim` for a period map `Q`, for dot notation; only the real isomorphism is
used. 

### `IsPeriodMap.ratConj_eq`

 Let `Q` and `R` be period maps for the matrices `ℓ` and `J` (hypotheses `hQ`, `hR`). If a
complex linear map `F` corresponds under them to a matrix `z ∈ GL n E` (hypothesis `hF`), then
`z ℓ z⁻¹ = J` at `v₀`. 

### `IsPeriodMap.complexMul`

 Multiplication by `c ∈ E ⊗ ℝ` (a complex number `c v` at each infinite place `v`), carried to
`V` by the period map `Q`, as a complex linear map; this is a ring homomorphism in `c`. 

 ## Linear maps to the adelic torsion module 

### `New.Variety.exists_matrix_torsionClass_eq`

 An `𝓞 E`-linear map `φ` from `Eⁿ` to the torsion module `(𝔸f / Ô)ⁿ` is given by a matrix
`h` of finite adeles: `φ y` is the class of `h y`. Here `frameCoords 1 y` is `y` as an adelic
vector. 
