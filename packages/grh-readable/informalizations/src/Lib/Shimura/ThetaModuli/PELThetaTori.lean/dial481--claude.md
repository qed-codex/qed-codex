---
{
  "module": "src/Lib/Shimura/ThetaModuli/PELThetaTori.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Shimura/ThetaModuli/PELThetaTori.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Shimura/ThetaModuli/PELThetaTori.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# PEL data, the adelic Riemann form and theta coordinates of polarised period maps

Let `E` be a CM field with ring of integers `𝓞 E`. The file sets up the PEL data for the moduli
problem of abelian schemes with an action of `𝓞 E`. It studies polarised period maps
`x : New.ThetaTori.PeriodMap` for such data `D`. With `T = D.dualTorsion` the kernel of the
polarisation, of odd order, and `L = D.lagrangian ≤ T` Lagrangian, the file constructs lattices over
groups of torsion classes and canonical theta coordinates `θ_t` for `t ∈ T`.

## Main definitions and results

* `New.PEL`: the data (rank, polarization type, level, theta structure) and their numerical
  conditions. `New.PEL.levelTorsion` is the torsion of the level.
* `New.PEL.HasClassLaws`: the laws required of the class of the embedding line bundle.
* `New.ThetaTori.PeriodMap`: a period map onto a complex vector space, with a polarisation whose
  Riemann form pulls back to `New.Variety.polarisationForm`.
* `New.Variety.fourierChar_polarisationForm`: if `gᴴ β g = a · 1`, its exponential is a value of
  `New.ψf` in the coordinates of `g`.
* `New.ThetaTori.PeriodMap.latticeOver`: the lattice in `V` over a group `S` of torsion classes.
  `New.ThetaTori.PeriodMap.periodLattice` is the lattice for `S = 0`, and its dual for the Riemann
  form is the lattice over `T` (`New.ThetaTori.PeriodMap.dualLattice_periodLattice`).
* `New.ThetaTori.PeriodMap.thetaCoord`: for `t ∈ T`, the normalised translate `θ_t` by a lift of `t`
  of the theta function `New.ThetaTori.PeriodMap.lagrangianTheta` for the
  lattice over `L`. That theta function is unique up to a scalar.
* `New.ThetaTori.PeriodMap.formSpan_eq_normBall`,
  `New.ThetaTori.PeriodMap.thetaCoord_vector_ne_zero`: at a valuation of good reduction, the forms
  of degree `r^j` in the `θ_t` fill a ball of theta functions. The `θ_t` have no common zero.

Notions from other files:
* `New.ψf`: the standard additive character of the finite adeles: ψ_f(x) = exp(2πi Tr_{E/ℚ}(a)) for
  any a in E with x − a integral.
* `New.Variety.toRealVectors`: the additive map E^n → (∏_v C)^n applying the CM-type embedding
  x ↦ (Φ_v(x))_v to each coordinate.
* `New.RealComplexForm.thetaSpace`: the entire functions f on V with
  f(z + l) = χ(l)·exp(B(l,z) + B(l,l)/2)·f(z) for l in L.
* `New.RealComplexForm.thetaShift`, `New.ThetaTori.normalizedShift`: the twisted translation
  f ↦ exp(−B(a,z) − B(a,a)/2)·f(z + a), and the same divided by the multiplier at a.
* `New.AdelicTorsion`, `New.Variety.frameTorsionClass`: the torsion O_E-module (𝔸_f / Ô)ⁿ of
  n-tuples of finite adeles of E modulo integral ones (an adelic model of (E / O_E)ⁿ), and the
  O_E-linear map sending y in Eⁿ to the class of the adelic vector g⁻¹y in it.

## Relation to the literature

Known; see `Lib.Shimura.IntegralModel.TowerExistence`, `Lib.Shimura.Uniformisation.AppellHumbert`
and `Lib.Shimura.ThetaModuli.UniversalFamily` for sources.



## PEL data, good primes and the class laws of a line bundle

* `New.PEL.IsGoodAt`: the ideals of `𝓞 E` at which the data are good.

`star` is complex conjugation, and `New.Pic` is written additively.


### `Variety.xiForm`

 For ξ in E and vectors x, y of finite adeles of E, the finite adele ξ·∑ᵢ ȳᵢxᵢ. 

### `Variety.HasPadding`

 `r = c̄ c + 3 + ∑ₗ āₗ aₗ` in `𝓞 E` for some `r - 3` integers `aₗ` of `E` that span `𝓞 E` over
`ℤ`: the norm of `c` and the norms of the `aₗ` add up to `r - 3`. 

### `PEL`

 PEL data over the CM field `E`. (a) An integer `β` with `star β = 1 - β` and a level `𝔑` (field
`level`) with `𝔑 ≠ 0`. (b) An element `ξ` of `E`, which gives the pairing `ψf (ξ zᴴ y)` on vectors
with `rank` coordinates; the group `T` (field `dualTorsion`) of classes that pair trivially with all
integral vectors has odd order, and the subgroup `lagrangian` is its own annihilator and contains
the `r`-torsion. (c) Natural numbers `r` (field `paddedNorm`) with `r ≥ 3` and `i` (field
`exponentBound`) with a degree bound (`isCutDegree`), a bound by the level (`mem_torsionBy_level`)
and paddings of `1` and `β` to `r`. (d) Conditions on the images of `ξ` and `β` under the embeddings
of the CM type. The number `rank` of coordinates is not zero. 

### `PEL.β`

 An integer β of E with β̄ = 1 - β (field `star_beta`). 

### `PEL.level`

 The level 𝔑, an integer of E. 

### `PEL.ξ`

 The element ξ of E that defines the form tr(ξ yᴴ x). 

### `PEL.rank`

 The number of coordinates of the vectors. 

### `PEL.paddedNorm`

 The natural number r to which the norms are padded. 

### `PEL.exponentBound`

 The bound i on the exponents j of the degrees r ^ j that have to be read. 

### `PEL.dualTorsion`

 The group T of classes that pair trivially with all integral vectors (field
  `mem_dualTorsion`). 

### `PEL.lagrangian`

 A Lagrangian subgroup L of the torsion module. 

### `PEL.star_beta`

 The conjugate of β is 1 - β. 

### `PEL.three_le_paddedNorm`

 The number r is at least 3. 

### `PEL.level_ne_zero`

 The level is not zero. 

### `PEL.isCutDegree`

 A monomial ideal in variables indexed by T that leaves at most `thetaRanks T r j` monomials of
  degree r ^ j for all j ≤ i does so for all j. Here `thetaRanks T r j` is the integer square root
  of the number of y with r ^ j • y ∈ T. 

### `PEL.mem_torsionBy_level`

 The level 𝔑 kills every y with r ^ j • y in T for some j ≤ i. 

### `PEL.odd_card`

 The group T has odd order (in particular it is finite). 

### `PEL.mem_dualTorsion`

 The class of y lies in T exactly when ψ_f(ξ zᴴ y) = 1 for every integral vector z. 

### `PEL.mem_lagrangian`

 L is its own annihilator: the class of y lies in L exactly when ψ_f(ξ zᴴ y) = 1 for every z
  whose class lies in L. 

### `PEL.torsion_mem_lagrangian`

 L contains the r-torsion. 

### `PEL.hasPadding_one`

 r is 1 + 3 plus the norms ā a of r - 3 integers that span the integers of E over ℤ. 

### `PEL.hasPadding_beta`

 r is β̄ β + 3 plus the norms ā a of r - 3 integers that span the integers of E over ℤ. 

### `PEL.nonempty`

 The rank is not zero. 

### `PEL.xi_im_pos`

 Under each embedding of the CM type, ξ has positive imaginary part. 

### `PEL.xi_re_eq_zero`

 Under each embedding of the CM type, ξ has real part zero. 

### `PEL.emb_beta_eq_of_ne`

 Away from the base place v₀, the embedding takes β to the image of β̄ at v₀. 

### `PEL.emb_star_beta_ne`

 At the base place, β and β̄ have different images. 

### `xi_im_pos_and_re_eq_zero`

 Under each embedding of the CM type, `ξ` lies on the positive imaginary axis. 

### `Index`

 The index type `Fin D.rank` of the coordinates. 

### `levelTorsion`

 The `𝓞 E`-submodule of classes in the torsion module killed by the level `𝔑`. 

### `dualTorsion_le_levelTorsion`

 Every class in `T` is killed by the level `𝔑` (the case `j = 0` of `mem_torsionBy_level`). 

### `instance : Finite D.dualTorsion`

 `T` is finite, as its order is odd and so nonzero. 

### `IsGoodAt`

 The data `D` are good at the ideal `w` of `𝓞 E` when the following hold. Neither `r` nor the
order of `T` lies in `w`. There are a prime number `p` in `w` and an integer `b` congruent to `β`
modulo `w` such that `β - b` and `star β - b` are coprime. The ideal of `𝔑` and `w` times the ideal
of `p` and `star β - b` together generate the unit ideal. Some finite place `v ≠ w` contains both
`p` and `β - b`. 

### `HasClassLaws`

 The laws of a class `c` in the Picard group of `A`, for all points `x`, `y` of `A` with values
in a scheme `T` over `S`: (a) the parallelogram law `New.Pic.ParallelogramLaw`; (b)
`⟨β x, y⟩ = ⟨x, (1 - β) y⟩` for the pairing `New.Pic.pairing`, where `1 - β = star β`; (c) the
pull-back of `c` along `y` is `⟨β y, y⟩` plus its pull-back along `0` (`x` plays no part here). The
three laws are read with `HasClassLaws.parallelogramLaw`, `pairing_smul_beta` and `atPoint_eq`. 

### `pairing_smul_beta`

 For a class with the laws `New.PEL.HasClassLaws`, `1 - β` is adjoint to `β` for the pairing. 

### `atPoint_eq`

 For a class with the laws `New.PEL.HasClassLaws`, the pull-back along `y` is `⟨β y, y⟩` plus the
pull-back along `0`. 


## The Riemann form on rational vectors and its adelic character value

* `New.Variety.polarisationForm`: the form `(y, z) ↦ Σ_v 2 Re(Φ_v(ξ) z_vᴴ Φ_v(β) y_v)`.


### `polarisationForm`

 For a matrix β over E, the real bilinear form (y, z) ↦ Σ_v 2 Re(Φ_v(ξ)·z_vᴴ Φ_v(β) y_v) on
(E ⊗ ℝ)ⁿ, with ξ from the datum D: a map
`RealVectors E D.Index →ₗ[ℝ] RealVectors E D.Index →ₗ[ℝ] ℝ`. 

### `_root_.New.ThetaTori.PeriodMap`

 A polarised period map for the frame `g` and the matrix `ℓ`: a period map Q = `realEquiv` onto
`V`, a matrix β = `formMatrix` over `E` with gᴴ β g a scalar unit of Ẑ, and a form
B = `automorphyForm` with symmetric real part whose Riemann form is positive and pulls back under Q
to `New.Variety.polarisationForm D formMatrix`. 

### `_root_.New.ThetaTori.PeriodMap.formMatrix`

 The matrix over E of the form that polarises the torus. 

### `_root_.New.ThetaTori.PeriodMap.realEquiv`

 The period map, a real linear isomorphism from (E ⊗ ℝ)ⁿ onto V. 

### `_root_.New.ThetaTori.PeriodMap.automorphyForm`

 The form in the factor of automorphy on the period lattice `classLattice g ⊥ realEquiv`: real
  linear in the first variable, complex linear in the second. 

### `_root_.New.ThetaTori.PeriodMap.isFrameFor`

 g is a frame for β: gᴴ β g is a scalar unit of Ẑ. 

### `_root_.New.ThetaTori.PeriodMap.isPeriodMap`

 Q is complex linear for the structure that is i ℓ at v₀ and i at the other places. 

### `_root_.New.ThetaTori.PeriodMap.re_symm`

 The real part of B is symmetric. 

### `_root_.New.ThetaTori.PeriodMap.riemannForm_eq`

 Through Q, the Riemann form of B is the trace form tr(ξ zᴴ β y) on (E ⊗ ℝ)ⁿ. 

### `_root_.New.ThetaTori.PeriodMap.isPosRiemann`

 The Riemann form of B is positive: its value at (u, i u) is positive for u ≠ 0. 

### `ψf_unit_mul_eq_one_iff`

 For a unit ν of `New.Ô ℚ` and a finite adele a of E, `New.ψf` is trivial at ν·a exactly when it
is trivial at a. So multiplying by a unit of Ẑ does not change the kernel of `New.ψf`. 

### `polarisationForm_toRealVectors`

 On rational vectors y, z in Eⁿ, `New.Variety.polarisationForm D β` is the trace from E to ℚ of
ξ·zᴴβy. Here ξ comes from the datum D. 

### `fourierChar_polarisationForm`

 If `gᴴ β g = a • 1` for a finite adele `a` of `E`, then for rational vectors `y, z` in `Eⁿ` the
value of `𝐞` at `polarisationForm D β y z`, that is exp(2πi Tr_{E/ℚ}(ξ zᴴ β y)), is
ψ_f(a ξ (g⁻¹z)ᴴ (g⁻¹y)). Here ξ comes from the datum `D`. 


## Lattices of polarised period maps and the theta coordinates θ_t

* `New.ThetaTori.ThetaTorus`: period maps on which `𝓞 E` acts by the standard diagonal maps.

The multiplier `New.ThetaTori.PeriodMap.multiplier` is `χ(u) = exp (π i e(β₁ u, u))`, with `e` the
Riemann form of `x.automorphyForm` and `β₁ = D.rescaledBeta`, for which `β₁ + β̄₁ = 1`. The phase
`x.automorphyForm.riemannPhase u w` is exp(2πi·e(u, w)).


 ### Lifts of torsion classes, the action of `𝓞 E` and theta tori 

### `PEL.rescaledBeta`

 The integer β₁ = |T|β − ⌊|T|/2⌋ of E. 

### `PEL.lagrangian_le_dualTorsion`

 The Lagrangian subgroup `L` lies in `T`. 

### `PEL.rTorsion`

 The `D.paddedNorm`-torsion subgroup of the torsion module indexed by `D.Index`: the classes `s`
with `D.paddedNorm • s = 0`. 

### `ratLift`

 A chosen vector `y` of `Eⁿ` with `frameTorsionClass g y = s`, normalised so that the class `0`
is represented by `0`. 

### `PeriodMap.intAction`

 The ring homomorphism from O_E to the complex endomorphisms of V given by multiplication,
transported through the period map. 

### `ThetaTorus`

 A theta torus is a polarised period map in which ℓ is a reflection and multiplication by c̄ is
adjoint to multiplication by c for B. Also, some isomorphism V ≅ `New.Variety.BallFibre` makes each
a ∈ O_E act by Φ_{v₀}(a) on the line, by its conjugate on the complement, and by Φ_w(a) at each
place w ≠ v₀. 

### `ThetaTorus.reflection`

 The matrix `ℓ` is a reflection. 

### `ThetaTorus.adjoint`

 The adjoint for `automorphyForm` of multiplication by `c ∈ 𝓞 E` is multiplication by
  `star c`. 

### `ThetaTorus.exists_std_equiv`

 In suitable coordinates `a ∈ 𝓞 E` acts diagonally: at `v₀` by `Φ v₀ a` on the line and by its
  conjugate on the complement, and by `Φ w a` at each place `w ≠ v₀`. 

### `latticeOver`

 For a subgroup S of the torsion module, the image in V under the period map of the vectors
of E^n whose class with respect to g lies in S. 

 ### Lattices over groups of torsion classes and their duals 

### `periodLattice`

 The period lattice in V: the image under the period map of the vectors y in E^n with g⁻¹y
integral. 

### `multiplier`

 The function on V sending u to exp(πi·e(β₁u, u)), where e is the Riemann form of B and β₁ =
|T|β − ⌊|T|/2⌋. 

### `periodPoint`

 For y in E^n, the point of V obtained by applying the period map of x to the image of y in the
real vectors (E ⊗ ℝ)^n. 

### `torsionLift`

 For a torsion class s, the vector of V that is the image under the period map of the chosen
representative of s in E^n. 

### `mem_latticeOver`

 The image `x.periodPoint y` of a rational vector lies in the lattice over `S` exactly when
its class `frameTorsionClass g y` lies in `S`. 

### `latticeOver_mono`

 The lattice over a group of torsion classes grows with the group. 

### `dualLattice_inf_latticeOver_top`

 For a subgroup `S` of the torsion module `(𝔸f E / Ô E)ⁿ`, `x.latticeOver S` is the image in `V`,
under the period map, of the vectors of `Eⁿ` whose class with respect to `g` lies in `S`. If `S'` is
the annihilator of `S` for the adelic pairing `(y, w) ↦ ψ_f(ξ wᴴ y)`, then the vectors of
`x.latticeOver ⊤` lying in the dual of `x.latticeOver S` for the Riemann form of `x.automorphyForm`
are exactly those of `x.latticeOver S'`. 

### `intAction_mem_periodLattice`

 Multiplication by an integer of `E` maps the period lattice into itself. 

### `nsmul_mem_latticeOver`

 For `m ≠ 0`, `m • u` lies in the lattice over `S` exactly when `u` lies in the lattice over the
classes that multiplication by `m` sends into `S`. 

### `toAddSubgroup_latticeOver`

 The lattice over `S`, as an additive subgroup, is the image under `x.realEquiv ∘ toRealVectors`
of the rational vectors whose class lies in `S`. 

### `relIndex_latticeOver`

 The index of the lattice over `S` in the lattice over `S'` is the index of `S` in `S'`. 

### `card_nsmul_mem_periodLattice`

 `|T|` times a vector of the lattice over `T` lies in the period lattice. 

### `intAction_rescaledBeta_mem_latticeOver`

 If `S ≤ D.dualTorsion`, multiplication by `β₁ = |T|β − ⌊|T|/2⌋` (`New.PEL.rescaledBeta`) maps
the lattice over `S` into itself. 

### `riemannForm_intAction_rescaledBeta`

 e(β₁u, w) + e(u, β₁w) = e(u, w) for the Riemann form e of B, where β₁ is `D.rescaledBeta`. 

### `isAppellHumbert_of_le`

 The multiplier χ is a semicharacter of every subgroup of the lattice over `D.lagrangian`. 

### `isAppellHumbert_periodLattice`

 The multiplier χ is a semicharacter of the period lattice for B. 

### `isAppellHumbert_latticeOver_lagrangian`

 The multiplier χ is a semicharacter of the lattice over `D.lagrangian` for B. 

### `dualLattice_le_latticeOver_top`

 Every vector of the dual of the lattice over `S`, for the Riemann form of `x.automorphyForm`, is
rational: it lies in the lattice over `⊤`. 

### `dualLattice_periodLattice`

 The dual of the period lattice for the Riemann form of `x.automorphyForm` is the lattice over
`T = D.dualTorsion`. 

### `discreteTopology_latticeOver_lagrangian`

 The lattice over `D.lagrangian` is discrete. 

### `sub_mem_periodLattice_iff`

 The images in `V` of two rational vectors `y` and `z` differ by a vector of the period lattice
exactly when `y` and `z` have the same torsion class. 

 ### The bicharacter on `T` and the theta coordinates 

### `riemannPhase_rescaledBeta_eq`

 Let `u` and `x.periodPoint y` lie in `x.latticeOver D.dualTorsion`, the image in V under the
period map of the vectors of Eⁿ whose class `frameTorsionClass g` in `(𝔸f / Ô)ⁿ` lies in T, and let
`frameTorsionClass g z = frameTorsionClass g y`. Then e(β₁u, y) and e(z, ⌊|T|/2⌋u) differ by an
integer, so their phases `x.automorphyForm.riemannPhase` agree. Here e is the Riemann form of B,
β₁ = |T|β − ⌊|T|/2⌋ acts on V through `x.intAction`, and y and z stand for their points
`x.periodPoint` in V. 

### `bicharacter`

 For u in the lattice over T, the additive character t ↦ exp(2πi·e(β₁u, a_t)) of T, with e
the Riemann form of B and a_t the chosen lift of t. 

### `bicharacter_neg_eq_swap`

 Let `c_s` be the character `x.bicharacter` of `T` attached to the chosen lift of `s`. Then
`c_s(-t) = c_t(s)`. 

### `mem_lagrangian_of_bicharacter_sq`

 If the character `x.bicharacter` of `T` attached to the chosen lift `x.torsionLift s` of `s` has
square `1` on the Lagrangian subgroup `D.lagrangian` (as a subgroup of `T`), then `s` lies in
`D.lagrangian`. 

### `exists_generator_thetaSpace`

 The theta functions for the lattice over the Lagrangian subgroup form a line: there is a
nonzero one of which all are complex multiples. 

### `lagrangianTheta`

 A chosen generator of the line of theta functions for the lattice over the Lagrangian
subgroup. 

### `exists_smul_lagrangianTheta_eq`

 Every theta function for the lattice over the Lagrangian subgroup is a complex multiple of
`x.lagrangianTheta`. 

### `thetaCoord`

 The theta coordinate at `t`: the normalised translate of `x.lagrangianTheta` by the chosen
lift of `t`. 

### `thetaCoord_mem_thetaSpace`

 The theta coordinate `θ_t` is a theta function of type `(B, χ)` for the period lattice. 

### `thetaCoord_mem_thetaSpace_lagrangian`

 `θ_t` is a theta function for the lattice over `L`, with the multiplier twisted by
l ↦ exp(2πi·e(l, a_t)), where e is the Riemann form of B and a_t = `x.torsionLift t` is the chosen
lift of t. 

### `thetaCoord_eq_of_mem_lagrangian`

 For `s` in the Lagrangian subgroup, `θ_s = θ_0`. 

### `thetaCoord_eq_normalizedShift`

 The theta coordinate at `t` may be computed with any rational vector `y` that represents
`t`. 

### `periodPoint_mem_latticeOver_of_frameTorsionClass_eq`

 If the rational vector `y` represents `s ∈ T`, its image in `V` lies in the lattice over `T`. 

### `thetaShift_thetaCoord`

 The theta law. If the rational vector `y` represents `s ∈ T` and `u` is its image in `V`, the
twisted translation `New.RealComplexForm.thetaShift` by `u` sends `θ_t` to `χ(u) c_u(t) θ_{s+t}`,
where χ is `x.multiplier` and `c_u` is the character `New.ThetaTori.PeriodMap.bicharacter` attached
to `u`: c_u(t) = exp(2πi·e(β₁u, a_t)), with e the Riemann form of B and a_t the chosen lift of t. 

### `exists_thetaCoord_sign_smul`

 For a unit `m = ±1` of ℤ, there is a constant `ε`, independent of `z` and `t`, with
`θ_t(m z) = ε · θ_{m t}(z)` for all `z ∈ V` and `t ∈ T`. So up to a single scalar, `-1` permutes the
theta coordinates by `t ↦ -t`. 

### `valuation_multiplier_mul_bicharacter_eq_one`

 Let `v` be a valuation on `ℂ`, let `u` lie in the lattice over `T` and let `t ∈ T`. The product
`χ(u) · c_u(t)` of the multiplier and of the character `x.bicharacter` attached to `u` has
valuation `1`: both factors are roots of unity. 

### `hasGoodReduction_one`

 At the trivial valuation `1` on ℂ, the form `x.automorphyForm` of the polarised period map `x`
and its multiplier `x.multiplier` satisfy `HasGoodReduction` of level `D.paddedNorm`. This means the
conditions of `IsAmpleType` hold, some natural `N` with `v(N) = 1` maps the dual lattice into the
lattice, the level `D.paddedNorm > 1` has `v(D.paddedNorm) = 1`, and the sup norm is
multiplicative. 

### `thetaNorm_thetaCoord`

 For a valuation `v` on `ℂ`, every theta coordinate `θ_i` has the theta norm of `θ_0`. The theta
norm of f is the supremum, over torsion points a, of the size v(exp(-B(a, a)/2)·f(a)). 

### `formSpan_eq_normBall`

 Normal generation: let `v` be a valuation of good reduction for `x.automorphyForm`,
`x.multiplier` and the level `r = D.paddedNorm`, and let `θ_t = x.thetaCoord t` be the theta
coordinates. Then, for any `c ∈ T`, the forms of degree `r^j` in the `θ_t` with coefficients in the
valuation ring are exactly the theta functions of type `(r^j B, χ^(r^j))` in the ball of
`θ_c^(r^j)`. This ball consists of those theta functions `f` whose size
`v(exp(-r^j B(a, a) / 2) · f(a))` at every torsion point `a` (a vector of finite order modulo the
period lattice) is at most the supremum of the sizes of `θ_c^(r^j)`. 

### `thetaCoord_vector_ne_zero`

 The theta functions θ_t, t in T, have no common zero: for every z in V the vector (θ_t(z))_t
is non-zero. 
