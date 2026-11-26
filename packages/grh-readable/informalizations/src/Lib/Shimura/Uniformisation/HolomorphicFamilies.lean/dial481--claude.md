---
{
  "module": "src/Lib/Shimura/Uniformisation/HolomorphicFamilies.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Shimura/Uniformisation/HolomorphicFamilies.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Shimura/Uniformisation/HolomorphicFamilies.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Holomorphic families of complex points, jets, uniformisations and theta coordinates

Except in `New.Uniformisation.hasSignature_iff`, where `O` is any commutative ring acting on `A`,
`O` is a valuation ring with fraction field `ℂ` (`New.ValuativeArc`), for example `ℂ` itself. This
file develops calculus for families of complex points of schemes over `O` without an
analytification: holomorphic families, jets and a chain rule. These notions are applied to a
uniformisation `V / L ≅ A(O)` of a commutative group scheme `A`, which yields a count of its torsion
points. The file also treats linear systems whose homogeneous coordinates are theta functions, and
their behaviour under operations on line bundles.

## Main definitions and results

* `New.HolomorphicAt.exists_isJet`, `New.IsJet.unique`, `New.isJet_comp_iff`: jets exist and are
  unique, and they obey the chain rule.
* `New.HolomorphicAt.isFirstOrderConst_of_nsmul`: on a smooth commutative group scheme, if `n • φ`
  is constant to first order in a direction, for some `n ≠ 0`, then so is `φ`.
* `New.Uniformisation.hasSignature_iff`: the condition `New.HasSignature` on the matrices of the
  action of `O` in algebraic coordinates holds iff the space `V` of a uniformisation has a common
  eigenvector `Y ≠ 0` of the maps `F a`, with eigenvalues `ρ a`, such that `F b - ρ c` maps `V` into
  the line of `Y`.
* `New.Uniformisation.card_torsion`: A(O) has m^(2 dim V) points killed by m ≠ 0.
* `New.HasThetaCoords.pull`, `New.HasThetaCoords.pow`, `New.HasThetaCoords.pull_translate`,
  `New.HasThetaCoords.mul`: pull-back, power, translation and tensor product.
* `New.HasThetaCoords.riemannForm_eq_of_isFrame`: if `N ⊗ M⁻¹` has a frame, the Riemann forms and
  the multipliers of `N` and `M` agree, and along the family the frame is a constant times
  exp((B − B′)(z, z)/2)·θ′/θ.

Notions from other files:
* `New.PointFn`: a function on the points of a scheme X; it assigns to each point Spec R → X, for
  every ring R, an element of R, with no compatibility required.
* `New.LandsIn`: the point t : Spec R → X lands in the open U when all of Spec R maps into U.
* `New.IsAppellHumbert`: Appell–Humbert data (B, χ) for a lattice L: Re B is symmetric, and on L one
  has |χ| = 1 and χ(l + m) = χ(l)χ(m)·exp(πi E(m, l)), where E(u, v) = Im(B(u, v) − B(v, u))/(2π) is
  the Riemann form of B (`New.RealComplexForm.riemannForm`).
* `New.RealComplexForm.thetaSpace`: the entire functions f on V with f(z + l) = χ(l)·exp(B(l,
  z) + B(l, l)/2)·f(z) for l in L.
* `New.LineBundle.IsHomogeneousCoords`, `New.LineBundle.IsLinearSystem`: v is a vector of
  homogeneous coordinates of the point t for the line bundle N when t lands in the chart U_j exactly
  when v_j is a unit, and then g_jk(t) = v_k/v_j. N is a linear system when each transition function
  g_ij is regular on U_i and zero at the points outside U_i, and the g_ij(t), j varying, are
  homogeneous coordinates of every point t of U_i.

## Relation to the literature

Known; see `Lib.Shimura.Uniformisation.AppellHumbert` and `Lib.Shimura.ArcExtension` for sources.



## Complex points over a valuation ring, holomorphic families and uniformisations

The analytic vocabulary for schemes over a valuation ring `O` with fraction field `ℂ`
(`New.ValuativeArc`; the case `O = ℂ` is included).


 ### Valuation rings of `ℂ` and sections over them 

### `ValuativeArc`

 A valuation ring O with fraction field ℂ, given with its algebra map O → ℂ, together with the
generic point Spec ℂ → Spec O, which is the morphism induced by O → ℂ. 

### `ValuativeArc.genericPt`

 The generic point `Spec ℂ ⟶ Spec O`. 

### `ValuativeArc.genericPt_eq`

 The generic point is the morphism induced by the algebra map `O → ℂ`. 

### `ComplexPoint`

 The set of complex points of a scheme A over ℂ, that is sections of its structure morphism. 

### `bijective_restrict_genericPt`

 Valuative criterion of properness: for A proper over a valuation ring O with fraction field ℂ,
restriction to the generic point of Spec O is a bijection from the sections of A over O to the
ℂ-points of A above the generic point. 

### `atGeneric`

 For a family s of sections of A over Spec O, O a valuation ring of ℂ, the complex point of A
given by s(z) at the generic point. 

### `atGeneric_eq`

 Over `O = ℂ`, the point `atGeneric s z` is the underlying morphism of the section `s z`. 

 ### Holomorphic families of points and their jets 

### `HasGermAt`

 For a family φ : T → X(ℂ) of complex points of the scheme X, a point w₀ of the space T and a
property Q of functions T → ℂ: for each open U of X containing φ(w₀) and each function f on the
points of X that is regular on U (at the points landing in U, f is given by a section over U), φ(w)
lies in U for w near w₀, and the function f ∘ φ satisfies Q. 

### `HolomorphicAt`

 The family φ : P → X(ℂ) of complex points of the scheme X, P a finite-dimensional complex
space, is holomorphic at w₀: functions regular near φ(w₀) pull back to functions analytic at w₀. 

### `IsJet`

 τ is a jet of the family φ at w₀ for ℓ. Here τ : Spec(ℂ ⊕ M) → X is a point of X over the
trivial square-zero extension ℂ ⊕ M of ℂ by the ℂ-module M, and ℓ sends differentials on P to M. The
condition: τ lands in every open U that contains φ(w₀), and s(τ) = s(φ w₀) + ℓ(d(s ∘ φ) at w₀) for
every section s of the structure sheaf over U. 

### `IsFirstOrderConst`

 φ is constant to first order at w₀ in the direction v: the constant point φ(w₀), seen over the
dual numbers, is the jet of φ for evaluation of differentials at v. Equivalently
(`New.isFirstOrderConst_iff`), d(s ∘ φ)(v) = 0 at w₀ for every section s over an open that contains
φ(w₀). 

### `IsHolomorphicImmersionAt`

 φ is a holomorphic immersion at w₀: it is holomorphic there, and constant to first order
only in the direction 0. 

 ### Uniformisations and theta coordinates 

### `Uniformisation`

 A uniformisation of A by V, for a commutative group object A over Spec O (`New.AddObj`), O a
valuation ring of ℂ, and a finite-dimensional complex space V: a surjective homomorphism from V to
the sections of A over O whose kernel is a full-rank lattice, which is a holomorphic immersion on
complex points, and through which every homomorphism holomorphic at 0 factors ℂ-linearly. 

### `Uniformisation.expMap`

 The uniformising map, an additive map from `V` to the sections of `A` over `O`. 

### `Uniformisation.lattice`

 The period lattice. 

### `Uniformisation.isFullRankLattice`

 The lattice is discrete and spans `V` over `ℝ`. 

### `Uniformisation.surjective`

 Every section of `A` over `O` is a value of the uniformising map. 

### `Uniformisation.eq_zero_iff`

 The kernel of the uniformising map is the lattice. 

### `Uniformisation.immersive`

 On complex points the uniformising map is a holomorphic immersion at every point. 

### `Uniformisation.universal`

 Every additive map `γ` to the sections that is holomorphic at `0` factors through the
  uniformising map by a continuous `ℂ`-linear map. 

### `HasThetaCoords`

 Theta coordinates for a family φ : P → X(ℂ) of complex points and a lattice L in P: the line
bundle N is a linear system (`New.LineBundle.IsLinearSystem`), (B, χ) are Appell–Humbert data
for L, with B a form on P, and θ(z) gives homogeneous coordinates of φ(z), each θ_i being a theta
function of type (B, χ). 

### `HasThetaCoords.isLinearSystem`

 `N` is a linear system. 

### `HasThetaCoords.isAppellHumbert`

 `(B, χ)` are Appell–Humbert data for the lattice `L`. 

### `HasThetaCoords.mem_thetaSpace`

 Each coordinate of `θ` is a theta function of type `(B, χ)` for `L`. 

### `HasThetaCoords.hasFieldCoords`

 `θ z` is a vector of homogeneous coordinates of the point `φ z`. 


## Germs, jets and tangent vectors of families of complex points

Families `φ` of complex points of a scheme are treated without an analytification. Sections over an
open set are functions on ring-valued points (`New.PointFn.ofSection`), and they are pulled back
along `φ`. For `New.HolomorphicAt`, `Q` is analyticity at `w₀`.

* `New.HasGermAt.of_isHomogeneousCoords`, `New.HasGermAt.of_jointly_mono`: on a projective scheme,
  `HasGermAt` can be tested on homogeneous coordinates (`New.LineBundle.IsHomogeneousCoords`) or on
  maps that separate points.
* `New.HolomorphicAt.exists_isJet`, `New.IsJet.unique`, `New.isJet_comp_iff`: a holomorphic
  family has exactly one jet for each linear map on differentials, and jets obey the chain rule.
* `New.HolomorphicAt.isFirstOrderConst_of_nsmul`, `New.Uniformisation.hasSignature_iff`: on a
  smooth commutative group scheme, if `n • φ` is constant to first order in a direction for some
  `n ≠ 0`, so is `φ`; and the signature condition on the tangent action can be read on the space
  of a uniformisation.


 ### Germs of families of points 

### `GermClass`

 Every function in `Q` is continuous at `w₀`. `Q` also contains every function that near `w₀` is
an analytic function of finitely many functions in `Q`. 

### `GermClass.comp`

 A finite family `p` of functions in the class is continuous at `w₀`, and the class contains
  every function that agrees near `w₀` with `g ∘ p` for some `g` analytic at `p w₀`. 

### `comp_hom`

 If `φ` has a germ of class `Q` at `w₀`, so has its composite with a morphism `f : X ⟶ Y`. 

### `exists_isHomogeneousCoords`

 If `N` is a linear system, a family of class `Q` has, near `w₀`, homogeneous coordinates for `N`
of class `Q`. 

### `of_affine`

 Let `Q` be a germ class at `w₀` and `U` an affine open set. Suppose that near `w₀` the family
stays in `U`, and that every section over `U` pulls back to a function of class `Q`. Then the family
is of class `Q`. 

### `of_isHomogeneousCoords`

 Let `N` embed `X` in projective space over `Spec R`, and let all points `φ w` lie over one
complex point `b` of `Spec R`. If near `w₀` the points `φ w` have homogeneous coordinates `p w`
whose components lie in the class `Q`, then `φ` has a germ of class `Q` at `w₀`. 

### `of_jointly_mono`

 Let `W` be proper over `Spec R`, with finitely many maps `π l` to projectively embedded
schemes that together separate its points. A family `φ` of points of `W` over one complex point
`b` of `Spec R` has a germ of class `Q` at `w₀` as soon as each image `φ · ≫ π l` has one. 

### `lift`

 Two families of class `Q` in a projective scheme `A` give a family of class `Q` in `A × A`. 

 ### Jets 

### `ofSection_eq`

 The value of a section `s` at a jet of `φ` is its value at `φ w₀` plus `ℓ` of the
derivative of `s ∘ φ` at `w₀`. 

### `unique`

 A family has at most one jet for a given linear map `ℓ` on differentials. 

### `comp_hom`

 The composite of a jet `τ` of `φ` with a morphism `p : X ⟶ Y` is a jet of `w ↦ φ w ≫ p`. 

### `congr`

 A jet of `φ` at `w₀` is also a jet of every family `ψ` that agrees with `φ` near `w₀`. 

### `fst_comp`

 Reducing a jet `τ` of `φ` at `w₀` modulo the square-zero part `M` gives the point `φ w₀`. 

### `comp_base_eq`

 If all points `φ w` lie over one point `b` of `S`, a jet `τ` of `φ` lies over `b`, seen as a
point with values in `ℂ ⊕ M`. 

### `HolomorphicAt.comp`

 A family holomorphic at `g v₀`, precomposed with a map `g` analytic at `v₀`, is holomorphic
at `v₀`. 

### `HolomorphicAt.exists_isJet`

 Let `φ` be a family of complex points of `X`, parametrised by a finite-dimensional complex space
`P` and holomorphic at `w₀`, and let `ℓ` be a linear map from linear functionals on `P` to a
ℂ-module `M`. Then there is a point `τ` of `X` over the trivial square-zero extension `ℂ ⊕ M` that
is a jet of `φ` at `w₀` for `ℓ`. That is, `τ` lands in every open containing `φ w₀`, and every
regular function `s` there satisfies `s(τ) = s(φ w₀) + ℓ(d(s ∘ φ) at w₀)`. 

### `isJet_comp_iff`

 The chain rule: if `g : V → P` has derivative `g'` at `v₀`, the jet of `φ ∘ g` at `v₀` in the
direction `v : V` is the jet of `φ` at `g v₀` in the direction `g' v`. 

### `isFirstOrderConst_iff`

 `φ` is constant to first order in the direction `v` iff the following holds for every open `U`
containing `φ w₀` and every section `s` over `U`: the derivative of `s ∘ φ` at `w₀` vanishes in the
direction `v`. 

 ### Immersions and tangent vectors of group schemes 

### `Uniformisation.isHolomorphicImmersionAt_of_isPullback`

 Let `A` be the fibre of `s : X ⟶ S` at the complex point `c` of `S`, with `p : A ⟶ X` the map
of the fibre square `h_pb`. Then the uniformisation of `A` followed by `p` is still a holomorphic
immersion at every `z : V`. 

### `HolomorphicAt.isFirstOrderConst_of_nsmul`

 Let 𝒜 be a commutative group scheme over X, smooth of relative dimension d, φ a family of
complex points of 𝒜 holomorphic at w₀, and n ≠ 0. If the family w ↦ n • φ(w) is constant to first
order in the direction v, so is φ. 

### `Uniformisation.hasSignature_iff`

 The signature condition read on a uniformisation. Let `u` uniformise `A`, a group scheme over
`ℂ` on which `O` acts, by a space `V` of dimension `d`, and let `A` be the fibre at the complex
point `s` of the group scheme `𝒜`, with `p` the map of the fibre square, compatible with the action
of `O` (`h_bc`). Let `a : O` act on `V` by `F a`, compatibly with `u.expMap` (`hF`), and let `z` be
a Lie chart of `𝒜` over `s` (`h_lieChart`): étale coordinates on an open set `U` around the zero
section, in which `a` acts on tangent vectors by the matrix `m a`. Then `HasSignature ρ b c m` (the
`m a` have a common eigenvector with eigenvalues `ρ a` and a unit coordinate, and `m b - ρ c` maps
into its line) holds iff some `Y ≠ 0` in `V` has `F a Y = ρ a • Y` for all `a`, and `F b - ρ c` maps
`V` into the line of `Y`. 


## Linear lifts, lattice indices and counting torsion points

A uniformisation (`New.Uniformisation`) identifies the sections of A with V modulo its period
lattice `lattice`, the kernel of `expMap`.

* `New.Uniformisation.linear_ext`: a continuous ℂ-linear map into V is determined by its composite
  with the uniformising map.
* `New.relIndex_comap_eq_det_mul_conj_det`: for an injective ℂ-linear F preserving a lattice L, the
  index of L in F⁻¹(L) is |det F|².
* `New.Uniformisation.card_torsion`: A(O) has m^(2 dim V) points killed by m ≠ 0.


### `Uniformisation.linear_ext`

 Two continuous ℂ-linear maps into the uniformising space are equal if they agree after the
uniformisation `u.expMap`. 

### `relIndex_comap_eq_det_mul_conj_det`

 Let L be a lattice in a finite-dimensional complex space V and F an injective ℂ-linear
endomorphism of V with F(L) ⊂ L. Then the index of L in F⁻¹(L) equals det F times its
complex conjugate, that is |det F|². 

### `Uniformisation.card_torsion`

 Let O be a valuation ring with fraction field ℂ, A a commutative group scheme over O, and u a
uniformisation, with V / u.lattice ≅ A(O) and dim V = d. For m ≠ 0, exactly m^{2d} points of A(O)
are killed by m. 


## Theta coordinates under operations on line bundles

Line bundles `New.LineBundle` are given by a cover and a cocycle; a section `w` is a family of
functions on points, one for each chart, and a frame is a section that vanishes nowhere.

* `New.Uniformisation.atGeneric_add`, `New.Uniformisation.atGeneric_add_of_mem`: on complex
  points the uniformising map turns addition into translation and is periodic for its lattice.
* `New.HasThetaCoords.pull`, `New.HasThetaCoords.pow`, `New.HasThetaCoords.pull_translate`,
  `New.HasThetaCoords.mul`: theta coordinates under pull-back, powers, translation and tensor
  product.
* `New.HasThetaCoords.exists_theta_of_isSection`: a section of `N ⊗ M⁻¹` is given by a theta
  function of the quotient type.


### `Uniformisation.atGeneric_add`

 On complex points, the uniformising map at `z + a` is its value at `z` followed by the
translation by the section `u.expMap a`. 

### `atGeneric_add_of_map_eq_zero`

 If the additive map `s` from `V` to the sections of `X` kills `l`, then on complex points
`s` takes the same value at `z + l` and at `z`. 

### `Uniformisation.atGeneric_add_of_mem`

 On complex points the uniformising map is periodic for its lattice `u.lattice`. 

### `pull`

 Let `N` have theta coordinates `θ` along `e`, let `F` be a complex linear map that sends `L'`
into `L`, and let `f` send the point `e' z` to `e (F z)`. Then the pull-back of `N` along `f` has
theta coordinates `θ ∘ F` along `e'`, of the type pulled back along `F`. 

### `pow`

 If θ gives theta coordinates of type (B, χ) for N along e, then the monomials of degree m in
θ give theta coordinates of type (mB, χ^m) for the m-th power of N. 

### `pull_translate`

 Let `f : S ⟶ S` act along `e` as translation by `a`. Then the twisted translates
`thetaShift B a` of the coordinates `θ`, z ↦ exp(−(B(a, z) + B(a, a)/2))·θ(z + a), are theta
coordinates for the pull-back of `N` along `f`; the form `B` stays, and `χ l` is multiplied by
`exp (2 π i E(l, a))`, with `E` the Riemann form of `B`. 

### `mul`

 Let θ and θ' give theta coordinates of types (B, χ) for N and (B', χ') for M along e. Then the
products θ_i·θ'_a give theta coordinates for the tensor product N ⊗ M, of type (B + B', χχ'). 

### `exists_theta_of_isSection`

 Let `N` and `M` have theta coordinates `θ` and `θ'` along a family `e` of complex points,
holomorphic everywhere, for the lattice `L`, with Appell–Humbert data `(B, χ)` and `(B', χ')`
respectively. Let `w` be a section of `N ⊗ M⁻¹` whose values along `e` are unchanged by translation
by `L`. Then there is a theta function `G` of type `(B - B', χ * χ'⁻¹)` such that `w (i, a)` at
`e z` equals `G z * θ' z a / θ z i` whenever `θ z i` and `θ' z a` are both nonzero. 

### `riemannForm_eq_of_isFrame`

 Let `N` and `M` have theta coordinates `θ` and `θ'` along a holomorphic family of points `e`
that is periodic for `L`, and let `w` be a frame of `N ⊗ M⁻¹`. Then the two Riemann forms agree,
the two multipliers agree on `L`, and along `e` the frame is `c * exp ((B - B') z z / 2) * θ' / θ`
for a constant `c`. 
