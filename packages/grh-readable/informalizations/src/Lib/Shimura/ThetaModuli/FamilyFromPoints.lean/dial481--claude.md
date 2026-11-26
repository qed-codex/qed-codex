---
{
  "module": "src/Lib/Shimura/ThetaModuli/FamilyFromPoints.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Shimura/ThetaModuli/FamilyFromPoints.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Shimura/ThetaModuli/FamilyFromPoints.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Linear systems and theta families from dense complex points carrying theta tori

This file builds objects from their values at a dense family of complex points. A linear system is a
line bundle whose transition functions are the ratios `s j / s i`, that is, a map to projective
space. `New.Variety.ThetaNull.exists_isLinearSystem` extends coordinates given at a dense family `ξ`
of complex points of a reduced scheme (`New.IsSeparatingFamily`) to a linear system. It needs a
linear system `M` with homogeneous coordinates `m a` at each `ξ a`. It also needs each of `w`, `m`
to be locally a regular function times sums of the other. The result has the Picard class of `M`.
The second part builds a family of theta-embedded abelian schemes `New.ThetaFamily D` over a base
`S` from complex points `η k` of `S` that carry theta tori `x k`. The scheme `A` is the closure of
the theta points. The group law, the action and all identities extend from these points by density,
using Riemann's relation for theta functions.

## Main definitions and results

* `New.exists_isAbelianScheme`: group and module axioms pass from dense families of vector spaces to
  `A`.
* `New.Variety.exists_maps_of_riemann_relation`: the extension step along Riemann's relation.
* `New.Variety.exists_add_and_intAction`: the addition and the action of `𝓞 E` extend to `A`.
* `New.Variety.exists_isThetaStructure`: the theta law on base changes to local rings.
* `New.Variety.exists_thetaFamily_of_points`: the family exists, modelled on `x i` at each `η i`.
  The remaining lemmas of the second part are steps of its proof.

Notions from other files:
* `New.LineBundle.IsHomogeneousCoords`: a vector `v` gives homogeneous coordinates of a point `t`
  for a line bundle: `v j` is a unit exactly when `t` lands in chart `j`, and there the transitions
  from chart `j` are the ratios `v k / v j`.
* `New.LineBundle.IsLinearSystem`: a line bundle whose transitions are regular on their charts,
  vanish off them, and are homogeneous coordinates of every point of the chart.
* `New.PointFn.IsRegularOn`: a function `f` is regular on an open `U`: at points `t : Spec A → X`
  that land in `U`, its value commutes with all ring maps `φ : A → B`.
* `New.Variety.AllSpecializeTo S Q`: every point of `S` specialises to the image of a point over an
  algebraically closed field with the property `Q`.
* `New.ThetaTori.ThetaTorus.IsRiemannTuple`: coefficient tuples for Riemann's relation.

## Relation to the literature

Known; see `Lib.Shimura.ThetaModuli.UniversalFamily` for sources.


 ## Linear systems from coordinates at dense points 

### `New.Variety.ThetaNull.IsLocalCombination`

 The family `w` is a local combination of the family `m`: for every index `j` and every point
`s` of `Z` there are an open `U` containing `s`, indices `e : Q → J` and a function `c` regular
on `U` such that `w a j = c (ξ a) * ∑ q, m a (e q)` at every complex point `ξ a` that lands in `U`.
Here `w a` and `m a` are vectors of complex coordinates attached to the point `ξ a`. 

### `New.Variety.ThetaNull.exists_isLinearSystem`

 Let the points `ξ a` separate `Z`, with homogeneous coordinates `m a` for the linear system
`M`. If each of the families `w` and `m` is a local combination of the other, then the `w a` are
homogeneous coordinates of the `ξ a` for a linear system `N` in the class of `M`. 


## Theta families from dense complex points carrying theta tori

Smoothness and the group axioms by density, the level coordinates of a theta torus, padding tuples,
and the extension of the group law and of the theta structure from the points `η i` to `A`.


### `LineBundle.IsHomogeneousCoords.pi`

 Homogeneous coordinates for a product of line bundles: if for each factor `l : K` the values
`θ k (w l)`, `k : ι`, are homogeneous coordinates of `t` for `M l`, then the products
`∏ l, θ (μ l) (w l)`, indexed by `μ : K → ι`, are homogeneous coordinates of `t` for the product
bundle `LineBundle.pi M`. Here `V` is any type. 

### `smooth_of_allSpecializeTo_isReduced`

 A flat proper commutative group scheme A over a locally noetherian S is smooth if every point of
S specialises to the image of a point over an algebraically closed field along which the fibre of A
is reduced. 

### `exists_isAbelianScheme`

 Group and module laws by density. Let `V` be a finite-dimensional complex space, `O` a
commutative ring and `S` reduced and locally noetherian with complex points `η i`, the finite
subfamily `η ∘ j` being dense. Let `A` be flat and proper over `S` with a reduced geometric fibre at
a specialisation of every point, and let maps `e i : V → A(η i)` be such that all points `e i z`
separate `A` and, for each `i`, the `e i v` separate the fibre of `A` over `η i`. If the addition,
the zero and the action `F i` of `O` on `V` extend to morphisms `m`, `o` and `f c` of `A`, then `A`
is an abelian scheme with an `O`-module structure, each `e i` is additive, and
`c • e i z = e i (F i c z)`. 

### `Variety.ThetaNull.IsNonvanishingIndex`

 The index `a` of the subgroup `D.dualTorsion` of level torsion does not vanish at the point `t`
of `S`: `c` gives a line bundle on `S` with charts indexed by `D.dualTorsion` for each level torsion
point, and for all `l k : D.dualTorsion` with `l + k = a` the point `t` lies in chart `k` of the
bundle `c l`. 

### `ThetaFamily.IsModelledOn`

 The fibre of the theta family `X` at the complex point `t` is modelled on the theta torus `x`:
it has a torus model (a uniformisation by `V` along `t` with theta coordinates) for the period map
of `x`, whose theta coordinates are the theta functions of `x`. 

### `ThetaTori.ThetaTorus.isCutOutAt_range_thetaCoord`

 Let `t` be a complex point of `S` at which, for each level torsion point `ω`, the theta values
of `x` at the lift of `ω` are homogeneous coordinates for the line bundle `c ω`. Then at `t` the
bundles `c ω` cut out the set of all theta vectors of `x`: in every choice of charts through `t`,
the rank conditions `thetaRanks` on the transition values define that set (`IsCutOutAt`). 

### `ThetaTori.ThetaTorus.thetaCoord_add_torsionLift`

 Translation by the lift to `V` of `l ∈ D.dualTorsion` shifts the index `k` of a theta function
of `x` by `l`, up to an exponential factor, the multiplier of `x` and the value at `k` of the
bicharacter (the additive character of `D.dualTorsion` attached to the lift of `l`). 

### `ThetaTori.ThetaTorus.sum_bicharacter_sq_eq_zero`

 For `s` in `D.dualTorsion` outside the Lagrangian subgroup, the square of the bicharacter of `s`
(an additive character of `D.dualTorsion`) sums to zero over the Lagrangian, as it is a non-trivial
character there. 

### `ThetaTori.ThetaTorus.exists_eigenline`

 Let `b` be an integer. There is a nonzero `Y : V` on which `𝓞 E` acts through `ρ`, that is,
through the embedding `Φ v₀`, such that the map `w ↦ x.intAction (star β - b) w - ρ (β - b) • w`
takes its values in the line through `Y`: it is `w ↦ ξ w • Y` for a linear form `ξ`. 

### `ThetaTori.ThetaTorus.map_eq_zero_of_mem_periodLattice`

 Let `N` embed `A` in projective space over `S`, and let `e : V →+ A(t)` be an additive map to
the points of `A` over the complex point `t` whose coordinates for `N` are the theta vectors of `x`.
Then `e` vanishes on the period lattice of `x`. 

### `isRiemannTuple_paddingTuple`

 The padding tuple of `a` and `d` (two pairs `(1, 0)`, the pairs `(d, 1)` and `(1, - star d)`,
and the pairs `(a l, 0)`) is a Riemann tuple for `D` when
`star d * d + 3 + ∑ l, star (a l) * a l = D.paddedNorm`. 

### `PEL.hasClassLaws_of_riemann_relation`

 Let `A` over `S` be a commutative group scheme with an action of `𝓞 E`, and `c` a class in
`Pic A.left` satisfying Riemann's relation: for all `d` and `a : Fin (D.paddedNorm - 3) → 𝓞 E` with
`d̄ d + 3 + ∑ ā_l a_l = D.paddedNorm`, and all `T`-points `y`, `z`, the pull-backs satisfy
`c(d y + z) + c(y - d̄ z) + ∑ c(a_l y) + c(0) = c(z) + c(-d̄ z) + c(y) + (D.paddedNorm - 3) c(y)`.
Then `c` satisfies the class laws `D.HasClassLaws`: (a) the parallelogram law;
(b) `⟨β x, y⟩ = ⟨x, (1 - β) y⟩` for the pairing `Pic.pairing`, where `β` is the integer of `D` with
`star β = 1 - β`; and (c) the pull-back of `c` along `y` is `⟨β y, y⟩` plus its pull-back along
`0`. 

### `Variety.exists_isRegularOn_bicharacter`

 Suppose `c` attaches to each class `ω` in `D.levelTorsion` a linear system on `S` with charts
indexed by `D.dualTorsion`, whose homogeneous coordinates at each `η i` are the theta coordinates of
`x i` at the torsion lift of `ω`, and that for each point `t` and each `s : D.dualTorsion` some `a`
makes `a`, `-a` and `s - a` nonvanishing indices at `t` (`IsNonvanishingIndex c t a`: `t` lies in
the chart `k` of `c l` whenever `l + k = a`). Then the bicharacters of the theta tori are regular
functions near each point. A point `t` of `S` with values in a local ring lands in an open `W` with
regular functions `r l m`, whose value at each `η i` in `W` is the bicharacter of `x i` at the
torsion lift of `l`, evaluated at `m`. 

### `Variety.exists_isRegularOn_riemann_coefficient`

 Riemann's relation has regular coefficients near every point `t` of `S`. Let `c` have
nonvanishing indices, let `#D.dualTorsion` be a unit in `R`, and let `p`, `q` be Riemann tuples (`q`
starting with `(1, 0), (1, 0)`). Then there are indices `μ' s` and a function `r` regular near `t`
with the following property at each `η i` near `t`. The theta product of `x i` (the product of theta
coordinates `θ_{μ l}(a_l z + b_l y)`) for the pairs `doubledCoeffs p q` (the `(0, b)` of `q`, then
`p`) is `r` times the sum over `s` of those for `doubledCoeffs q p` at `μ' s`. 

### `Variety.exists_maps_of_riemann_relation`

 Maps of a projective scheme extend along Riemann's relation: if for each pair `(a, b)` of
`doubledCoeffs q p` the map `(z, y) ↦ a z + b y` of the tori extends to `ψ l : A ⊗ A ⟶ A`, then the
maps for `doubledCoeffs p q` extend to morphisms `G l`, and the pull-backs of `N` along the `G l`
and along the `ψ l` have products of the same class. 

### `paddingTuple_inl`

 The first two pairs of a padding tuple are `(1, 0)`. 

### `Variety.exists_add_and_intAction`

 The addition of `V` and the action of `𝓞 E` on the tori `x i` extend to `A`. Assume the linear
systems `c ω` have the theta values of `x i` at the torsion lifts as coordinates at `η i`, that
nonvanishing indices exist at every point of `S`, and that `#D.dualTorsion` is a unit in `R`. Let
`A` over `S` be embedded by `N`, and let `e i z` be points of `A` over `η i` whose homogeneous
coordinates are the theta functions of `x i` at `z` and whose pairs separate `A ⊗ A`. Let the zero
extend to a section `o` of `A`. Then there are a morphism `add : A ⊗ A ⟶ A` with `e i (y + z)` equal
to `add` applied to `(e i y, e i z)`, and for each `d : 𝓞 E` an endomorphism `f` of `A` with
`e i z ≫ f = e i ((x i).intAction d z)`, where `intAction d` is the action of `d` on the torus. 

### `Variety.hasClassLaws_picClass`

 Let the `c ω` be linear systems on `S` with the theta constants of `x i` at `ω` as coordinates
of `η i` and the index condition `h_index`, and let #`D.dualTorsion` be a unit in `R`. Let `A` over
`S` be a commutative group scheme with an action of `𝓞 E`, embedded by `N`. Let `e i` be additive
maps from `V` to the points of `A` over `η i` that respect the action (`he_smul`), whose homogeneous
coordinates are the theta functions of `x i` and whose pairs separate `A ⊗ A`. Then the class of `N`
satisfies `D.HasClassLaws`: the parallelogram law and the two pairing laws for `β`. 

### `Variety.exists_isThetaStructure`

 The theta law on base changes to local rings. Assume the following: the linear systems `c ω` on
`S` have, at the separating complex points `η i`, the theta coordinates of `x i` at lifts of `ω`;
they satisfy `h_index`; and `#D.dualTorsion` is a unit in `R`. Also `N` embeds the `𝓞 E`-group `A`
projectively with theta coordinates at the separating points `e i z`, and `σ` lifts the level
torsion. Then for a base change `T` of `A` along `t : Spec B ⟶ S`, `B` local, the pull-backs of `N`
and `σ` on `D.dualTorsion` form a theta structure (`IsThetaStructure`) for the Lagrangian, with some
characters `C s`. 

### `Variety.exists_linearMap_coe_eq_of_comp_eq_torsionLift`

 Sections of `A` that restrict at each `η i` to `e i` of the lift of the level point are the
function of an `𝓞 E`-linear map `ς`, when the `e i` respect the action of `𝓞 E` and vanish on the
period lattices. 

### `Variety.fibrePointMap`

 The points of `A` over a point `η` of `S`, seen as points of the fibre of `A` over `η`; the map
is `𝓞 E`-linear. 

### `Variety.fibrePointMap_left`

 The point of the fibre given by `fibrePointMap A η u` is the pair of `u` and the point `η`. 

### `Variety.exists_uniformisation_pullback_of_isSeparatingFamily`

 The torus `x` uniformises the fibre of `A` over the complex point `η`: the fibre has a
uniformisation `u` with exponential map `e` followed by `fibrePointMap A η`, lattice the period
lattice of `x`, and the theta functions of `x` as theta coordinates of the pull-back of `N`; and
its relative dimension `d` is `abelianDim E D.Index`. 

### `Variety.exists_isLieChart_hasSignature`

 The signature condition for `A`: at every point `s` of `S` with values in a local ring there are
coordinates of `A` at `0` in which `𝓞 E` acts on the Lie algebra by matrices `m` with the signature
given by `β` and `b` (`HasSignature`). `Φ v₀` is the embedding of `E` into `ℂ` at the base place
`v₀`. 

### `Variety.exists_thetaFamily_of_points`

 A theta family from dense complex points: if `S` is embedded by the linear systems `c ω` whose
coordinates at the complex points `η i` are the theta functions of the theta tori `x i`, then `S`
is, under the further hypotheses of the statement, the base of a theta family whose object at each
`η i` is modelled on `x i`. Here `S` is reduced and locally noetherian, `V` is a finite-dimensional
complex space, and `Φ v₀` is the embedding of `E` into `ℂ` at the base place `v₀`. 
