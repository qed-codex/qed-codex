---
{
  "module": "src/New/Spanning/MainTerm/FiniteSieveSystem.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/MainTerm/FiniteSieveSystem.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/MainTerm/FiniteSieveSystem.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The sieve system at the finite places

The finite half of the input of the sieve `New.Filling.sieve`.

* `New.Filling.IsFillingData.exists_intermediateGroup_sieveSystem`: read the completions at a finite
  set `T` of places as one ring `LocProd T`. There is a subgroup `Z` of the unitary group over it
  that contains the components at `T` of the integral elements fixing given vectors at a set `Sg` of
  chosen places, and for which the forms `New.Floors.PlaceData.floorForm` and the density
  `New.Floors.PlaceData.lastEntryDensity`, divided by `Z.massRatio`, satisfy `New.SieveSystem`.

The subgroup is that of `New.Filling.IsFillingData.exists_intermediateGroup_norm_floorForm_div_le`,
which bounds the form of floor `0`: it saves the power `b ^ (6 * 𝔰.k)` of the base `b` of the
filling for each place in a given set `Sg` of chosen places.

Notions from other files:
* `New.Filling.IsAdmissible`: the standing hypotheses on the level and the sizes of a filling `S`.
* `New.Filling.IsFillingData`: `F` is a large lattice datum over `LocProd T`, its modulus
  `g = F.levelUnit` is the component at `T` of `S.ideleM` (the product `S.M` of the two level primes
  as a finite idele), and the character is that of `S` at `T`.
* `New.Floors.PlaceData.massIntegral`: `ϰ(Z) = ∫ |∫_Z phase(y x y⁻¹) dy| ^ 2 dx`.
* `New.Floors.PlaceData.IntermediateGroup.massRatio`: `vol(Z) vol(K(g)) / unipotentMass ^ 2`, where
  `vol` is `New.Floors.PlaceData.groupMeasure` and `Z` lies between `K(g)` and the integral points.
* `New.SieveSystem`: the recursion, positivity, continuity and bounds that the sieve asks of a
  family of forms at a place.

## Relation to the literature

See `New.Spanning.MainTerm.EnergyEstimate` for related work.


### `two_mul_M_pow_sq_pow_le`

 Let `S` be admissible filling data over the CM field `E`. Let `b = S.b` be the real number in
whose powers sizes are measured, `M = S.M` the product of the two level primes, `f = numInfPlaces E`
the number of infinite places, and `n = 𝔰.n = ϱ + 1` with `ϱ` the number of hyperbolic planes. Then
`(2 (M ^ f) ^ 2) ^ (n ^ 6) ≤ b ^ (n ^ 9 * f)`. 

### `IsFillingData.massIntegral_full_le`

 Let `S` be admissible filling data, `T` a conjugation-stable finite set of finite places, and
`F` a filling datum at `T`: measures and a modulus `g` for the unitary group `G` of the hermitian
form of `S` over the product `LocProd T` of the completions. Let `K` be the group of integral points
of `G`, `K(g) = F.congruenceSubgroup` its principal congruence subgroup and `vol = F.groupMeasure`
the Haar measure. Then `F.massIntegral K = ∫_G |∫_K χ(y x y⁻¹) dy| ^ 2 dx`, with
`χ = phase F.levelUnit` the generic character of the unipotent group `U` extended to `U K(g)` and by
zero, is at most `vol(K) vol(K(g)) (1 + b⁻¹ ^ 6)`, where `b = S.b` is the size parameter of `S`. 

### `norm_div_massRatio_le`

 Let `Z` be a group between the congruence subgroup of the place datum `F` and the integral
points, and let `c = Z.massRatio` be its normalising constant in `ℝ≥0∞`. A bound `‖x‖ₑ ≤ c * D` with
`D` finite gives `‖x / c.toReal‖ ≤ D.toReal`. 

### `IsFillingData.norm_floorForm_div_massRatio_le`

 Let `F` be a filling datum with modulus `g = F.levelUnit` on the unitary group over `LocProd T`,
the product of the completions at `T`, with integers `O`; let both level primes be units off `T`.
Let `Z` lie between `K(g)` and the integral points, `j ≤ ϱ`, let `p`, `q` be sequences of units and
`ξ` a unit. Let the weight `ω` be either `x ↦ P.ψ (ξ * G x j j)`, with `P.ψ` the additive character
of the place and `G x` the matrix of products of the frame with its image under `x`, or the constant
`1` with `j = i + 1` and `ξ = g⁻¹ * ((p i)⁻¹ - (q i)⁻¹)`. Take the orbital integral
`F.floorForm j p q` of floor `j` of `Z.besselVector` and divide it by `Z.massRatio = vol(Z)
vol(K(g)) / F.unipotentMass ^ 2`. The norm is at most `S.frequencyDecay T ξ = [O : ξ O] ^ ((k -
n⁷) / 2) / [O : O ∩ ξ⁻¹ O] ^ 3 * b ^ (n⁹ f)` times the weights `finHeadWeight (n ^ 6) j` of `p` and
`q`; that of `p` is the product over `l < j` of `[O : D O] ^ (n⁶ / 2)` for `D = p 0 * ⋯ * p l`, and
`0` if some `D` is not integral. Here `n = 𝔰.n = ϱ + 1`, `k = 𝔰.k`, `b = S.b`, `f` is the number of
infinite places, and `[O : ξ O]` is the generalised index `genIndex ξ`. 

### `IsFillingData.enorm_floorForm_zero_mul_le`

 Let `F` be a filling datum with modulus `g` on the unitary group `G` over the completions at
`T`, and let `Z` lie between the congruence subgroup `K(g)` and the integral points. Take the
orbital integral `F.floorForm 0` of `Z.besselVector`, the vector of the translates of the generic
character `χ = phase F.levelUnit` by the cosets of `K(g)` in `Z`. Its norm times the square of
`F.unipotentMass` is at most `F.massIntegral Z = ∫_G |∫_Z χ(y x y⁻¹) dy| ^ 2 dx`. 

### `IsFillingData.norm_floorForm_zero_div_massRatio_le`

 Let `F` be a filling datum with modulus `g` on the unitary group `G` over the completions at
`T`, `K` the integral points, `vol = F.groupMeasure` the Haar measure, and `K(g) ≤ Z ≤ K`. Write
`ϰ(Z) = F.massIntegral Z = ∫_G |∫_Z χ(y x y⁻¹) dy| ^ 2 dx` with `χ = phase F.levelUnit` the generic
character, `b = S.b` for the size parameter and `k = 𝔰.k` for the rank of the definite summand. If
`ϰ(Z) vol(K) (b ^ (6 k)) ^ s ≤ ϰ(K) vol(Z)` for a natural number `s`, then the orbital integral
`F.floorForm 0` of `Z.besselVector`, divided by `Z.massRatio = vol(Z) vol(K(g)) / F.unipotentMass ^
2`, has norm at most `(1 + b⁻¹ ^ 6) / (b ^ (6 k)) ^ s`. 

### `IsFillingData.exists_intermediateGroup_norm_floorForm_div_le`

 Let `S` be admissible and `F` a filling datum (a large lattice datum on the unitary group over
the completions at `T`, whose modulus `g` is the component of `S.ideleM`, the product of the two
level primes of `S`), and let `S.ideleM⁻¹` be integral off `T`. Let `Sg` be a set of chosen places
above the first level prime, and for each such place `w` let `d w` be a nonzero vector of the span
of the frame modulo `w` or its conjugate. There is a subgroup `Z` between the congruence subgroup
`K(g)` and the integral points such that (a) `Z` contains the component at `T` of each integral
adelic element whose reduction lies in `S.fixer Sg d`, that is, fixes `d w` for all `w ∈ Sg`; (b)
the orbital integral `F.floorForm 0` of `Z.besselVector` (the translates of the generic character by
the cosets of `K(g)` in `Z`), divided by `Z.massRatio = vol(Z) vol(K(g)) / F.unipotentMass ^ 2`, is
a real number between `0` and `(1 + b⁻¹ ^ 6) / (b ^ (6 k)) ^ #Sg`, where `b = S.b` is the size
parameter and `k = 𝔰.k` the rank of the definite summand. 

### `IsFillingData.posSemidef_lastEntryDensity`

 Let `F` be a filling datum on the unitary group over the completions at `T`, and let `Z` lie
between its congruence subgroup and the integral points. Let `S.piNAt T` be the component at `T` of
the idele `π_N` with `π π̄ = N`, where `N = S.N` is the split rational prime of `S`. For sequences
of units `p`, `q`, the density `F.lastEntryDensity (S.piNAt T) Z p q` integrates the pairing of the
scaled orbital integrals of `p` and `q` over the vectors of the top quadric with last entry `p ϱ`.
On finitely many sequences `a i` with the same entry `t` at position `ϱ = 𝔰.ϱ`, the number of
hyperbolic planes, it is a positive semidefinite matrix. 

### `IsFillingData.exists_intermediateGroup_sieveSystem`

 Let `F` be a filling datum of admissible data `S` on the unitary group over `LocProd T`, the
product of the completions at the finite places `T`. Its modulus `g = F.levelUnit` is the component
at `T` of `S.ideleM`, the product `M = S.M` of the two level primes as a finite idele; let
`S.ideleM⁻¹` be integral off `T`. Let `Sg` be a set of chosen places above the first level prime and
`d w` a nonzero vector of the span of the frame modulo `w` or its conjugate. There is a subgroup `Z`
between the congruence subgroup `K(g)` and the integral points such that (a) `Z` contains the
component at `T` of each integral adelic element whose reduction lies in `S.fixer Sg d`, that is,
fixes `d w` for all `w ∈ Sg`; (b) the forms `J j p q` in two sequences of units, given by the
orbital integral `F.floorForm j` for `j ≤ ϱ` (the number of hyperbolic planes) and by the density
`F.lastEntryDensity` at the prime `S.piNAt T` above `S.N` for `j > ϱ`, divided by the ratio of
volumes `Z.massRatio`, are a `SieveSystem`. That is: `J j` is the integral of `J (j + 1)` over a
common entry `unitOrOne c` at position `j ≤ ϱ`; the same integral twisted by `ψ (ξ * c)` at a unit
`ξ`, and also `J (j + 1) p q` if `j < ϱ` and `ξ = M⁻¹ (p j)⁻¹ - M⁻¹ (q j)⁻¹` is a unit, are bounded
by `S.frequencyDecay T ξ` times the weights `finHeadWeight (n ^ 6)` of `p` and `q`; `J (ϱ + 1)` is
continuous, and positive semidefinite on sequences with a common entry at `ϱ`; and
`‖J 0 p q‖ ≤ (1 + b⁻¹ ^ 6) / (b ^ (6 k)) ^ #Sg`. Here `ψ = S.charOnPlaces T` is the additive
character of `S` restricted to `T`, `b = S.b` is the size parameter, `n = 𝔰.n = ϱ + 1` and `k = 𝔰.k`
is the rank of the definite summand. 
