---
{
  "module": "src/New/Spanning/MainTerm/FillingLevel.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/MainTerm/FillingLevel.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/MainTerm/FillingLevel.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The place and level of a set of primes, orbit sums and the set of entries

This file sets up the local theory at a finite set `T` of finite places, stable under conjugation.
It defines the projection `New.Filling.toPlaces` of the finite adelic unitary group to `T` and the
condition `New.Filling.IsIntegralOff` of being integral off `T`. It also defines the orbit sums
`New.Filling.cosetAmplitude`, the finite set `New.Filling.entrySet` of entries and the condition
`New.Filling.IsFillingData`. It shows that the product `New.LocProd T` of the completions at `T` is
a finite place that carries such a datum.

## Main definitions and results

* `New.Filling.exists_isIntegralOff_toPlaces_eq`: every point of the unitary group at `T` is the
  projection of a finite adelic point that is integral off `T`.
* `New.Filling.exists_isFillingData`: `New.LocProd T` is a finite place (`New.Floors.IntegralPlace`)
  with a place datum satisfying `New.Filling.IsFillingData`.

Notions from other files:
* `New.Filling.latticeStabilizer`, `New.Filling.principalLevel`: The group `K` of integral points of
  the finite adelic unitary group, and the kernel `K(M)` of its reduction modulo `M`;
  `New.Floors.PlaceData.congruenceSubgroup` is the group `K(M)` at `T`.
* `New.Filling.amplitude`: The integral of β_c(y) β_c'(γ⁻¹y) W(y) ⊗ W(γ⁻¹y)^* over the infinite
  points y, with β_c the cutoff `New.Filling.classCutoff` and W the full or the cut Bessel function
  at infinity, according to the argument `side`.

## Relation to the literature

See `New.Spanning.MainTerm.EnergyEstimate` for related work.


 ### Orbit sums, the set of entries and the projection to `T` 

### `IsIntegralOff`

 The element `x` of the finite adelic unitary group and its inverse have entries integral at
every place outside `T`. 

### `cosetAmplitude`

 The sum of the amplitudes of `u γ u'⁻¹`, for the Bessel function named by `side` (full or cut),
over the pairs `(u, u')` of rational points of the unipotent group 𝖴 for which `u γ u'⁻¹` lies over
the block `(c, s, c')`. 

### `boundedNonzeroIntegers`

 The nonzero integers `δ` of `E` with `‖δ‖ ^ 2 ≤ b ^ (270 n ^ 2)` at every infinite place. The
nonzero leading minors of a term with nonzero cut amplitude are such integers
(`New.Filling.leadingMinor_mem_boundedNonzeroIntegers`). 

### `finite_boundedNonzeroIntegers`

 The set `S.boundedNonzeroIntegers` is finite. It consists of the nonzero integers `δ` of `E`
with `‖δ‖ ^ 2 ≤ b ^ (270 n ^ 2)` at every infinite place of `E`. 

### `finite_quotient_boundedNonzeroIntegers`

 There are finitely many quotients of two elements of `boundedNonzeroIntegers`. 

### `entrySet`

 The finite set 𝒯 of entries: the quotients of two elements of `boundedNonzeroIntegers`. 

### `toPlaces`

 The homomorphism from the finite adelic unitary group (lattice basis) to the unitary group
over the product of the completions at T, taking components at T. 

### `IsFillingData`

 The place datum `F` on the product of the completions at `T` is built on the Gram matrix
`New.Filling.latticeMiddle`, with 3ϱ + 6 further hyperbolic pairs and an orthonormal part of size
`k - (6ϱ + 13)`. It is a large lattice datum for the chosen place structure, its modulus is the
component of `M` at `T`, and the character of the place is `New.Filling.charOnPlaces`. 

### `IsFillingData.psi_eq`

 The character of the place is the character of `S` at `T`. 

### `IsFillingData.levelUnit_eq`

 The modulus of `F` is the component of `M` at `T`. 

### `eventually_mem_integralOff`

 A finite adele is integral off T for all sufficiently large finite sets T of finite places. 

### `exists_places_integralOff`

 For a finite set `T₀` of nonzero elements of `E` there is a finite set `T` of places, stable
under conjugation, off which the elements of `T₀` are units and the following are integral: the
inverse of the modulus `M`, the lattice basis with its inverse, and the inverse of the natural
number `S.N`. Here `ratIntegralOff T` is the ring of `T`-integers of `E`. 

### `ratToInf_weylElem`

 Let `w_p = weylElem 𝔰.ϱ p` be the Weyl element with `e_a ↦ p_a e*_a` and `e*_a ↦ e_a / p̄_a` on
the `𝔰.ϱ` hyperbolic pairs of the hermitian space of `S`. At an infinite place `v` with chosen
embedding `Φ v`, its rescaled image `ratToInf` is `w_q`, where `q i` is `Φ v (p i)` times the square
`frameScaleSq v i` of the scale of the `i`-th frame vector, read as a unit by `unitOrOne`. 

### `ratToInf_weylElem_mul`

 At an infinite place `v`, the rescaled image of `w_p σ` is `w_q` times the rescaled image of
`σ`, where `q i` is `Φ v (p i)` times the squared scale `frameScaleSq v i`. 

### `exists_isIntegralOff_toPlaces_eq`

 Every element `y` of the unitary group over the completions at `T` is the projection of a finite
adelic element `x` that is integral off `T`. Moreover, `x` lies in the unipotent group
`New.Shape.Form.besselU` if `y` does. It lies in `New.Shape.Form.besselH` if `y` does. 

### `mem_unitaryLevel_iff`

 Let `u` be a finite idele with `u⁻¹` integral off `T`. A finite adelic point `x` is integral and
congruent to `1` modulo `u` if and only if it is integral off `T` and its projection to `T` is
integral and congruent to `1` modulo the projection of `u`. 

### `mem_latticeStabilizer_iff`

 A finite adelic point `x` lies in the group `K` of integral points if and only if it is integral
off `T` and its projection to `T` is integral. 

 ### The product of the completions at `T` as a finite place 

### `exists_isAddHaarMeasure_skewAdjoint`

 Let `i` and `τ` be integral at `T`, with `i² = -1`, `star i = -i` and `τ + star τ = 1`. There is
a Haar measure `ν` on the skew elements, of mass one on the integral ones, such that
`(a, b) ↦ τ i a + b` takes `ν.prod ν` to the volume. 

### `exists_plancherel_kernel`

 If the integers at `T` are self-dual for the character `ψ`, then there is a kernel `G` for
Plancherel's inequality. It is continuous, integrable and nonnegative, with `G 0 = 1`, and its
transform has mass at most one. 

### `forall_charOnPlaces_mul_eq_one_iff`

 The integers at `T` are self-dual for the character `charOnPlaces`: `a` is integral if and only
if the character is trivial on the integral multiples of `a`. 

### `locallyIntegrable_prod_one_add_sqrt`

 The product over the places `w` of `T` of the functions `1 + √(‖x w‖⁻¹ - 1)` is locally
integrable. 

### `ofReal_genIndex_le_enorm_prod_sq`

 Let `x` lie in the product `LocProd T` of the completions of `E` at the places `w` of `T`. The
generalized index of `x`, the inverse of `∏ w, ‖x w‖`, is at most the square of the product over
`w ∈ T` of the numbers `1 + √(‖x w‖⁻¹ - 1)`. 

### `exists_integralPlace`

 The product of the completions of `E` at `T` carries the structure of a finite place whose
additive character is `S.charOnPlaces T`. This is `x ↦ ψ_f(-x / ϖ)` read at `T` through extension by
zero, where `ψ_f = ψf E` is the standard character of the finite adeles and `ϖ = S.deltaE` is the
generator of the different of `E` in the data `S`. 

### `isMulLeftInvariant_haar_inv`

 Let `(S.latticeMiddle (LocProd T)).G` be the unitary group, over the product of the completions
at `T`, of `ϱ` hyperbolic planes plus the space `X₀ ⊕ E z` with its Gram matrix `S.latticeMiddle` in
the lattice basis. This group is unimodular: the inverse of a left Haar measure is left invariant.
Here `P` is any structure of a finite place on that product; its character plays no part. 

### `star_neg_inv_deltaE`

 The image in the finite adeles `𝔸f E` of `-ϖ⁻¹`, where `ϖ = S.deltaE`, is skew: its conjugate
under `star` is its negative. 

### `charOnPlaces_apply_eq_ψf`

 The character `S.charOnPlaces T` at `x` is `ψf E`, the standard character of the finite adeles,
at `-ϖ⁻¹` times `adeleOfLocal T x`, the extension of `x` by zero. Here `ϖ = S.deltaE`. 

### `charOnPlaces_add_star`

 The character `S.charOnPlaces T` is trivial on the traces `x + star x` for `x` in `LocProd T`.
This is because it reads a fixed character of the finite adeles through multiplication by the skew
element -ϖ⁻¹. 

### `exists_isFillingData`

 Let `ϱ = 𝔰.ϱ` be the number of hyperbolic planes, `k = 𝔰.k` the dimension of the definite
summand `X₀`, and `S.latticeMiddle` the Gram matrix of `X₀ ⊕ E z` in the lattice basis. The product
of the completions at a conjugation-stable finite set `T` is a finite place `P` with a place datum
`F`, with 3ϱ + 6 further hyperbolic pairs and an orthonormal part of size `k - (6ϱ + 13)`, that
satisfies `New.Filling.IsFillingData`. 
