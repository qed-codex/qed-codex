---
{
  "module": "src/New/Spanning/Frames/BesselVector.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Frames/BesselVector.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Frames/BesselVector.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The Bessel vector at the finite places

Let `A` collect finitely many finite places, with integers `R` and character `ψ`, and let `F` be a
large lattice datum of modulus `g` for the unitary group `T.G`. Write `𝖴 = T.besselU`, `K(g)` for
the principal congruence subgroup and `K = K(1)`, and let `K(g) ≤ Z ≤ K`. This file constructs a cut
Bessel function from the translates of the Bessel character by the cosets of `K(g)` in `Z`, and
computes its correlations and norms.

## Main definitions and results

* `New.Floors.IntegralPlace.extendedBesselChar`: the Bessel character of `𝖴`, extended to `𝖴 K(g)`
  and by zero outside it.
* `New.Floors.PlaceData.IntermediateGroup.besselVector`,
  `New.Floors.IntegralPlace.IsLargeLatticeData.isCut_besselVector`: the vector of its translates by
  the cosets of `K(g)` in `Z`; it is a cut Bessel function.
* `New.Floors.IntegralPlace.IsLargeLatticeData.unipotentMass_mul_inner_besselVector`: its
  correlations as integrals over `𝖴` of the extended character, cut off by `Z`.
* `New.Floors.IntegralPlace.IsLargeLatticeData.lintegral_enorm_sq_besselVector`,
  `New.Floors.IntegralPlace.IsLargeLatticeData.pairingNormSq_mul_le_massRatio`: its norms.

Notions from other files:
* `New.Shape.Form.besselU`: the Bessel unipotent group `𝖴` of the block upper unitriangular
  isometries of `T.splitGram`.
* `New.simpleRootSum`: the sum `σ(s)` of the entries of `s` just above the diagonal of its block on
  the frame vectors.
* `New.unitaryLevel`: `unitaryLevel R g J` is the group `K(g)` of integral isometries of `J` that
  are congruent to `1` modulo the unit `g`.
* `New.Floors.PlaceData`: the data `F` of a place, among them the modulus `F.levelUnit`, the compact
  set `F.boxSet` and the measures whose product over all floors is `F.groupMeasure`.
* `New.Floors.PlaceData.IsCut`: a Bessel function of frequency `F.levelUnit⁻¹` that vanishes off the
  translates of `F.boxSet` by `𝖴`.

## Relation to the literature

See `New.Spanning.MainTerm.EnergyEstimate` for related work.


### `IntegralPlace.extendedBesselChar`

 The function χ_g on the unitary group: equal to ψ(σ(u) / g) on u K(g) for `u` in the Bessel
unipotent group 𝖴 = `besselU`, and to 0 off 𝖴 K(g). Here ψ is the character of the place,
σ = `simpleRootSum` is the sum of the entries at the simple roots, and K(g) is the principal
congruence subgroup of level `g`. The value does not depend on the chosen `u`: see
`extendedBesselChar_eq`. 

### `IntegralPlace.extendedBesselChar_eq_zero`

 The function χ_g = `extendedBesselChar g` vanishes off 𝖴 K(g), the product of the Bessel
unipotent group and the principal congruence subgroup of level `g`. 

### `IntegralPlace.exists_besselU_of_extendedBesselChar_ne_zero`

 A point where χ_g = `extendedBesselChar g` does not vanish lies in 𝖴 K(g), the product of the
Bessel unipotent group and the principal congruence subgroup of level `g`. 

### `IntegralPlace.norm_extendedBesselChar_le_one`

 The values of χ_g = `extendedBesselChar g` have absolute value at most 1. 

### `IntegralPlace.extendedBesselChar_eq`

 If `y` lies in u K(g), with `u` in the Bessel unipotent group and K(g) the principal congruence
subgroup, then χ_g = `extendedBesselChar g` has the value ψ(σ(u) / g) at `y`, where σ =
`simpleRootSum`. 

### `IntegralPlace.extendedBesselChar_besselS_mul`

 Let `x` lie in the Bessel subgroup `besselS`, which contains and normalises the Bessel unipotent
group 𝖴, and in u K(g), with `u` in 𝖴 and K(g) the principal congruence subgroup. Then left
translation by `x` multiplies χ_g = `extendedBesselChar g` by ψ(σ(u) / g). 

### `IntegralPlace.extendedBesselChar_mul_of_mem_unitaryLevel`

 The function χ_g = `extendedBesselChar g` is invariant under right translation by the principal
congruence subgroup K(g). 

### `IntegralPlace.extendedBesselChar_besselU_mul`

 Left translation by an element `u` of the Bessel unipotent group multiplies χ_g =
`extendedBesselChar g` by ψ(σ(u) / g), where ψ is the character of the place and σ =
`simpleRootSum`. 

### `IntegralPlace.continuous_extendedBesselChar`

 The function χ_g = `extendedBesselChar g`, the Bessel character extended to 𝖴 K(g) and by zero
outside it, is continuous. 

### `IntegralPlace.unitaryLevel_le_unitaryLevel_one`

 The principal congruence subgroup K(g) = `unitaryLevel integers g T.splitGram` of level `g` lies
in the integral unitary group K(1) = `unitaryLevel integers 1 T.splitGram`. 

### `PlaceData.IntermediateGroup`

 The type of all subgroups Z with K(g) ≤ Z ≤ K. Here K(g) = `F.congruenceSubgroup` is the
principal congruence subgroup of the place datum `F` and K is the integral unitary group. 

### `PlaceData.unipotentMass`

 The product fl over the floors l < ϱ of the volumes `F.floorModulus l`. At a large lattice datum
it is the mass of 𝖴 ∩ K(g) in the Bessel unipotent group 𝖴, where K(g) = `F.congruenceSubgroup`. 

### `PlaceData.massIntegral`

 The number ϰ(Z) = ∫_G |∫_Z χ_g(y x y⁻¹) dy|² dx for a subgroup `Z` of the unitary group G, both
integrals for the measure `F.groupMeasure`, with χ_g = `New.Floors.IntegralPlace.extendedBesselChar
F.levelUnit`. 

### `PlaceData.IntermediateGroup.le_unitaryLevel_one`

 Every intermediate group `Z` of the place datum `F` lies in
`unitaryLevel integers 1 T.splitGram`, the group of unitary elements with integral entries. 

### `PlaceData.IntermediateGroup.Cosets`

 The cosets K(g) a of K(g) = `F.congruenceSubgroup` in a group `Z` with K(g) ≤ Z ≤ K, for a in
`Z`. 

### `instance : Fintype Z.Cosets`

 The group K(g) has finitely many cosets in `Z`. 

### `PlaceData.IntermediateGroup.massRatio`

 The number vol(Z) · vol(K(g)) / fl² for a group `Z` with K(g) ≤ Z ≤ K, where
vol = `F.groupMeasure`, K(g) = `F.congruenceSubgroup` and fl = `F.unipotentMass`. 

### `PlaceData.IntermediateGroup.besselVector`

 The finite Bessel vector of `y`: its coordinate at the coset K(g) z in `Z` is χ_g(y z⁻¹), with
χ_g = `extendedBesselChar F.levelUnit`. The definition uses a chosen representative z of each
coset. 

### `PlaceData.unipotentMass_ne_zero_and_ne_top`

 The product `F.unipotentMass` of the floor volumes of a place datum `F` is positive and
finite. 

### `PlaceData.exists_mem_congruenceSubgroup_of_inner_ne_zero`

 Let `Z` be a group with K(g) ≤ Z ≤ K. If the values at `x` and `y` of the finite Bessel vector
of `Z` are not orthogonal, there are `u`, `v` in the Bessel unipotent group such that `u x` lies in
K and `v y` lies in the coset `u x K(g)`. 

### `PlaceData.IntermediateGroup.isOpen`

 A group `Z` with K(g) ≤ Z ≤ K is open, since it contains the open subgroup K(g). 

### `PlaceData.IntermediateGroup.exists_forall_mul_inv_mem_congruenceSubgroup_iff_eq`

 Let K(g) ≤ Z ≤ K, with K(g) = `F.congruenceSubgroup`. For `y` in `Z` there is exactly one coset
`c` of K(g) in `Z` whose chosen representative `c.out` satisfies `y * c.out⁻¹ ∈ K(g)`. 

### `IntegralPlace.inv_modulus_eq_sqrt_genIndex_sq`

 The inverse modulus of a unit `u` is its generalised index `genIndex u` (the inverse of the
factor by which `u` scales Haar measure), written as the square of its square root. 

### `IntegralPlace.exists_unit_leadingCoord_iff_mem_integers`

 Leading coordinates of a lattice. Let the matrix `X` over `A` have a left inverse, and let the
index `i` be alone in its weight `wt i`. Consider the vectors `v` that vanish at the indices of
larger weight and such that `X *ᵥ v` has entries in the ring of integers R = `integers`. Their
coordinates at `i` form the set c R for some unit c of `A`. 

### `box_eq`

 The compact set `F.boxSet` of a large lattice datum is the integral unitary group. 

### `groupMeasure_ne_top`

 For a large lattice datum `F` (hypothesis `IsLargeLatticeData F`), a subgroup `S` of the
integral unitary group `unitaryLevel integers 1 T.splitGram` has finite measure `F.groupMeasure S`,
for the convolution measure `F.groupMeasure` on the unitary group. 

### `massRatio_ne_zero_and_ne_top`

 For a large lattice datum and K(g) ≤ Z ≤ K, the number `Z.massRatio` = vol(Z) · vol(K(g)) / fl²,
with fl = `F.unipotentMass`, is positive and finite. 

### `setLIntegral_congruenceSubgroup_integral_sq`

 For a large lattice datum `F` (hypothesis `IsLargeLatticeData F`) and a group `Z` with
K(g) ≤ Z ≤ K, the contribution of K(g) = `F.congruenceSubgroup` to the integral `F.massIntegral Z`
is vol(Z)² · vol(K(g)), where vol = `F.groupMeasure`. 

### `isCut_besselVector`

 For a large lattice datum `F` (hypothesis `IsLargeLatticeData F`) and `Z` with K(g) ≤ Z ≤ K, the
finite Bessel vector W = `Z.besselVector` is a cut Bessel function (`F.IsCut`). That is: W is
bounded and measurable; W(u x) = ψ(σ(u) / g) W(x) for u in the Bessel unipotent group 𝖴, where
σ = `simpleRootSum` and g = `F.levelUnit`; and W vanishes off the translates by 𝖴 of the compact set
`F.boxSet`. 

### `leadingMinor_mem_of_besselOrbitalIntegral_ne_zero`

 For a large lattice datum and K(g) ≤ Z ≤ K, let the orbital integral J(γ) = ∫_G W(y) ⊗ W(γ⁻¹y)^*
dy (`besselOrbitalIntegral`, for the Haar measure `F.groupMeasure`) of the finite Bessel vector
`W = Z.besselVector` be non-zero. Then all leading minors of `T.frameGram γ`, the matrix of the
products h(f_a, γ f_b) of the frame vectors f_a under the form h = `T.splitGram`, are integral. 

### `unipotentMass_mul_inner_besselVector`

 The pairing of two translates of the finite Bessel vector as an integral over the Bessel
unipotent group 𝖴. For a large lattice datum and K(g) ≤ Z ≤ K, let fl = `F.unipotentMass` be the
mass of 𝖴 ∩ K(g), let W_Z = `Z.besselVector`, and let χ_g = `extendedBesselChar F.levelUnit` be the
Bessel character of 𝖴, extended to 𝖴 K(g) and by zero outside it. Then fl·⟨W_Z(y), W_Z(yx)⟩ is the
integral of 1_Z(uy)·χ_g(uyx(uy)⁻¹) over u for `ascConv heisenbergMeasure (𝔰.ϱ + 2)`. This is the
convolution η_0 ∗ ⋯ ∗ η_{ϱ+1} of the measures η_l = `heisenbergMeasure l`, where ϱ = `𝔰.ϱ` is the
number of hyperbolic planes of the shape 𝔰. It is carried by 𝖴. 

### `card_cosets_mul_groupMeasure`

 For a large lattice datum `F` and a group `Z` with K(g) ≤ Z ≤ K, the Haar measure of `Z` is the
number of cosets of K(g) = `F.congruenceSubgroup` in `Z` times the measure of K(g). 

### `ascConv_setOf_mul_mem_le_one`

 For a large lattice datum `F` and a group `Z` with K(g) ≤ Z ≤ K, the set of `u` with `u y ∈ Z`
has mass at most one for the convolution of the measures `heisenbergMeasure`, which is carried by
the Bessel unipotent group 𝖴. 

### `enorm_sq_besselVector_mul_unipotentMass`

 For a large lattice datum and K(g) ≤ Z ≤ K, let `fl = F.unipotentMass` be the mass of 𝖴 ∩ K(g)
and `W_Z = Z.besselVector`. Then `fl ‖W_Z y‖²` is the mass of the `u` with `u y ∈ Z` for
`ascConv heisenbergMeasure (𝔰.ϱ + 2)`. This is the convolution η_0 ∗ ⋯ ∗ η_{ϱ+1} of the measures
η_l = `heisenbergMeasure l`, where ϱ = `𝔰.ϱ` is the number of hyperbolic planes of the shape 𝔰. It
is carried by the Bessel unipotent group 𝖴. 

### `enorm_sq_besselVector_mul_le_one`

 For a large lattice datum `F` and a group `Z` with K(g) ≤ Z ≤ K, the normalised Bessel vector
`√fl W_Z` has norm at most one at every point, where `fl = F.unipotentMass` is the mass of 𝖴 ∩ K(g)
and `W_Z = Z.besselVector`. 

### `lintegral_enorm_sq_besselVector`

 For a large lattice datum `F` and a group `Z` with K(g) ≤ Z ≤ K, let `fl = F.unipotentMass` be
the mass of 𝖴 ∩ K(g) and `W_Z = Z.besselVector`. The squared norm of `√fl W_Z` on 𝖴∖G is the measure
of `Z`; by `card_cosets_mul_groupMeasure` this is the number of cosets of K(g) in `Z` times the
measure of K(g). Functions on 𝖴∖G are integrated against `F.quotientMeasureFrom 0`, the product of
the measures of all floors. 

### `lintegral_inner_besselVector_sq_mul_le`

 For a large lattice datum `F` and a group `Z` with K(g) ≤ Z ≤ K, let `fl = F.unipotentMass` be
the mass of 𝖴 ∩ K(g) and `W_Z = Z.besselVector`. For fixed `x`, the integral of |⟨W_Z(x), W_Z(y)⟩|²
over `y` in 𝖴∖G, that is against `F.quotientMeasureFrom 0`, times fl², is at most
‖W_Z(x)‖² · vol(K(g)). 

### `pairingNormSq_mul_le_massRatio`

 For a large lattice datum `F` and a group `Z` with K(g) ≤ Z ≤ K, let `fl = F.unipotentMass` be
the mass of 𝖴 ∩ K(g) and `W_Z = Z.besselVector`. The integral `F.pairingNormSq` of |⟨W_Z(x),
W_Z(y)⟩|² over (𝖴∖G)², times fl, is at most `Z.massRatio`, the number vol(Z) · vol(K(g)) / fl² for
the Haar measure vol = `F.groupMeasure`. 

### `enorm_integral_extendedBesselChar_eq_enorm_mul`

 For a large lattice datum `F`, a group `Z` with K(g) ≤ Z ≤ K and `x` in the unitary group `T.G`,
write χ_g = `extendedBesselChar F.levelUnit` and W_Z = `Z.besselVector`. The absolute value of ∫_Z
χ_g(y x y⁻¹) dy for `F.groupMeasure`, the inner integral of `F.massIntegral Z`, is the absolute
value of an integral times the mass `F.unipotentMass` of 𝖴 ∩ K(g). That integral is the integral of
⟨W_Z(z), W_Z(z x)⟩ over z for `F.quotientMeasureFrom 0`. 
