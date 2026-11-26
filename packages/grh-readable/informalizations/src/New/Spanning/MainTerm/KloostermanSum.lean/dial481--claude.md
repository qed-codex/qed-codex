---
{
  "module": "src/New/Spanning/MainTerm/KloostermanSum.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/MainTerm/KloostermanSum.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/MainTerm/KloostermanSum.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The orbital integral at the finite places is a Kloosterman sum

Let `𝖴` be the unipotent group `New.Shape.Form.besselU` over a finite place, or a product of finite
places, let `K(M)` be the principal congruence subgroup of a level `M`, and let `ψ_𝖴` be the
character of `𝖴`. The finite Bessel function `χ` is `ψ_𝖴(u)` on `u K(M)` and zero off `𝖴 K(M)`.

* `New.Floors.PlaceData.kloostermanSum`: the sum of `ψ_𝖴(u) conj ψ_𝖴(u')` over the pairs `u`, `u'`
  in `𝖴 / (𝖴 ∩ K(M))` with `u⁻¹ x u' ∈ s K(M)`.
* `New.Floors.IntegralPlace.IsLargeLatticeData.besselOrbitalIntegral_besselVector_apply`: the entry
  `(a, b)` of the orbital integral of the finite Bessel vector at `x` is the volume of `K(M)` times
  the Kloosterman sum of `x` at `s = a b⁻¹`.

Notions from other files:
* `New.Shape.Form.splitGram`: the Gram matrix of `𝔰.ϱ` hyperbolic planes and a middle space with
  Gram matrix `T`. The group `T.G` is its unitary group.
* `New.Floors.PlaceData ι T (m + 1)`: the data of a place. They include the level `M = F.levelUnit`
  and a basis of the middle space made of `m + 2` hyperbolic pairs and orthonormal vectors indexed
  by `ι`.
* `New.Floors.IntegralPlace.IsLargeLatticeData`: these data come from the lattice of vectors
  integral over `P.integers`, with conditions on the rank, the character of the place and the group.
* `New.Floors.IntegralPlace.extendedBesselChar`: the finite Bessel function `χ`.
* `New.Floors.PlaceData.IntermediateGroup.besselVector`: for a group `Z` between `K(M)` and the
  integral points, the vector of the translates of `χ` by the cosets of `K(M)` in `Z`.
* `New.besselOrbitalIntegral μ W x`: the orbital integral of `W(y) ⊗ W(x⁻¹ y)^*` over `y`.

## Relation to the literature

See `New.Spanning.MainTerm.EnergyEstimate` for related work.


### `New.integral_comp_quotientMk`

 Let `μ` be a left invariant measure on a group `G` and `J` an open subgroup of finite volume.
The integral of a function on the cosets `y J` is the volume of `J` times its sum over the cosets.
If the sum does not converge, both sides are zero. 

### `PlaceData.UnipotentCosets`

 The cosets `u (𝖴 ∩ K(M))` in the unipotent group `𝖴 = T.besselU`, where
`K(M) = F.congruenceSubgroup` is the principal congruence subgroup of the place data `F`. In the
type of `F`, `ι` and `m + 1` give the shape of the basis of the middle space in `F`: `m + 2`
hyperbolic pairs and orthonormal vectors indexed by `ι`. 

### `PlaceData.kloostermanSum`

 The Kloosterman sum of `x` at `s`: the sum of `χ(u) conj χ(u')` over the pairs of cosets
`u`, `u'` in `𝖴 / (𝖴 ∩ K(M))` with `u⁻¹ x u' ∈ s K(M)`, each coset being read through its chosen
representative. Here `𝖴 = T.besselU` is the Bessel unipotent group, `K(M) = F.congruenceSubgroup` is
the principal congruence subgroup of level `M = F.levelUnit`, and
`χ = extendedBesselChar F.levelUnit` is the finite Bessel function, which on `𝖴` is the character
`ψ_𝖴`. 

### `PlaceData.unipotentCosets_eq_of_inv_mul_mem`

 Let `𝖴 = T.besselU` be the Bessel unipotent group (the block upper unitriangular elements of the
unitary group `T.G`) and `K(M) = F.congruenceSubgroup` the principal congruence subgroup of level
`M = F.levelUnit`. Two cosets in `F.UnipotentCosets = 𝖴 / (𝖴 ∩ K(M))` whose chosen representatives
lie in one left coset of `K(M)` in `T.G` are equal. 

### `PlaceData.exists_out_inv_mul_mem`

 Let `𝖴 = T.besselU` be the Bessel unipotent group and `K(M) = F.congruenceSubgroup` the
principal congruence subgroup of level `M = F.levelUnit`. If `y ∈ 𝖴 K(M)`, then `y ∈ w K(M)` for the
chosen representative `w` of some coset in `F.UnipotentCosets = 𝖴 / (𝖴 ∩ K(M))`. 

### `PlaceData.inv_mul_mem_congruenceSubgroup_iff`

 An integral point `s` of the unitary group normalises `K(M) = F.congruenceSubgroup`, so the
cosets `s K(M)` and `K(M) s` agree. 

### `PlaceData.mem_unitaryLevel_one_of_inv_mul_mul_inv_mem`

 If `s⁻¹ a b⁻¹` lies in `K(M) = F.congruenceSubgroup` and `a`, `b` are integral points of the
unitary group, then `s` is an integral point. 

### `IntegralPlace.extendedBesselChar_eq_of_inv_mul_mem`

 For a unit `g` let `K(g)` be the subgroup of points integral over `P.integers` and congruent to
`1` modulo `g`, and let `𝖴 = T.besselU` be the Bessel unipotent group. The finite Bessel function
`extendedBesselChar g` is zero off `𝖴 K(g)`; at a point of `𝖴 K(g)`, written as `u k` with a chosen
`u` in `𝖴`, its value is `ψ(σ(u) / g)`, where `ψ = P.ψ` is the additive character of the place and
`σ(u)` is the sum of the entries of `u` at the simple roots. It takes the same value at two points
of a coset `y K(g)`. 

### `PlaceData.tsum_extendedBesselChar_mul_star_extendedBesselChar`

 Let `F` be place data for `T` at the finite place `P`, with level `M = F.levelUnit`, principal
congruence subgroup `K(M) = F.congruenceSubgroup` and finite Bessel function
`χ = extendedBesselChar F.levelUnit`. Let `x` be a point of `T.G` and `s` an integral point. Then
the sum of `χ(y s⁻¹) conj χ(x⁻¹ y)` over the cosets `y K(M)`, with `y` the chosen representative, is
the Kloosterman sum of `x` at `s`: the sum of `χ(u) conj χ(u')` over the pairs `u`, `u'` in
`𝖴 / (𝖴 ∩ K(M))` with `u⁻¹ x u' ∈ s K(M)`. 

### `IntegralPlace.IsLargeLatticeData.besselOrbitalIntegral_besselVector_apply`

 Assume `P.IsLargeLatticeData F`, which says, with `R = P.integers`, that: the form is unimodular
over `R`, and the basis and the level `M = F.levelUnit` are integral;
* the compact set, the close pairs, the positions and the measures of `F` are those given by the
lattice of integral vectors, and some isotropic vector is dual to the last frame vector;
* the rank is large: `ζ_R(m) ^ 𝔰.n ≤ 1 + 2⁻¹ ^ 𝔰.n` for the ideal zeta function `ζ_R`,
`m < 9 * 𝔰.n`, and `ι` has at least `53 * 𝔰.n` elements;
* the character of the place is trivial on traces, and the unitary group `T.G` is unimodular.

Then `μ = F.groupMeasure`, the measure on `T.G` built from `F`, is a Haar measure. Let `Z` be a
group between the principal congruence subgroup `K(M) = F.congruenceSubgroup` and the integral
points, and `a`, `b` cosets of `K(M)` in `Z` whose representatives satisfy `a b⁻¹ ∈ s K(M)`. Let `W`
be the Bessel vector of `Z`, with coordinates `W_a(y) = χ(y a⁻¹)` for the finite Bessel function
`χ = extendedBesselChar F.levelUnit`. Then `∫ W_a(y) conj W_b(x⁻¹ y) dμ(y)` is `μ(K(M))` times the
Kloosterman sum of `x` at `s`. 
