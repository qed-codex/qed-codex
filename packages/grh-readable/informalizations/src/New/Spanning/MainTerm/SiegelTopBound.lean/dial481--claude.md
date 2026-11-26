---
{
  "module": "src/New/Spanning/MainTerm/SiegelTopBound.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/MainTerm/SiegelTopBound.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/MainTerm/SiegelTopBound.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Siegel's formula as an upper bound, and domination of class sums by the density at the last entry

Finite-place estimate of the filling theorem: global sums are bounded by integrals over the product
of the completions at a finite set `T` of places, stable under conjugation.

* `New.Filling.adelicFrequency`, `New.Filling.localFrequency`: passage between skew-adjoint
  frequencies at `T` and self-adjoint finite adeles, through multiplication by `-ϖ⁻¹` and `-ϖ`,
  where `ϖ = S.deltaE` generates the different.
* `New.Filling.normDensity_indicator_eq_mul`: the density of a test function that is `Ψ` at `T` and
  the indicator of the lattice off `T` splits into an integral of Gauss sums of the lattice and the
  density of `Ψ` at `T`.
* `New.Filling.IsFillingData.enorm_normDensity_le_mul_lintegral_normFiberMeasure`: this density is
  at most `1 + b⁻⁶` times the volume of the lattice times the integral of `Ψ` over the sphere of `β`
  at `T`.
* `New.Filling.IsFillingData.siegel_sum_le_lintegral_sphere`: Siegel's formula bounds the sum of a
  step function over rational points with last entry `t` by a constant times its integral over the
  sphere of `t`.
* `New.Filling.IsFillingData.exists_step_sum_fiberPairing`: for any matrix `R`, the positive part of
  the real part of the sum of the fiber pairings against `R` is, on the top quadric, the restriction
  of a compactly supported invariant step function.
* `New.Filling.IsFillingData.sum_mul_norm_sum_cosetAmplitude_sq_le_lastEntryDensity`: the squared
  norms of class sums with one last entry `t` are bounded by `(1 + b⁻⁶) * S.scaledSiegelConst` times
  archimedean densities and densities at `T`, divided by the normalized mass.

The `IsFillingData` results assume `S` admissible, `S.ideleM⁻¹` integral off `T` and `F` filling
data. Conventions: `Φ v` is the embedding of the CM type at `v`. The last entry of `γ` is the
product of the last frame vector with its image under `γ`.

Notions from other files:
* `New.Floors.IntegralPlace`: A structure on `LocProd T`, the product of the completions at `T`: an
  open compact self-dual subring `R` of volume one, a character `ψ`, a trace-one element `τ`, a skew
  unit and the modulus `modulus`.
* `New.Filling.IsAdmissible`: The standing hypotheses: `sourceLevel` is the preimage of K(M),
  `reduction` is onto, and size inequalities hold between b and ϖ, κ_v, N, `besselDegree`, the
  second moments, the number of Bessel coordinates, an index and the mass.
* `New.Filling.latticeStabilizer`: The group `K` of integral points of the finite adelic unitary
  group; `New.Floors.PlaceData.congruenceSubgroup` is the group `K(M)` at `T`, the kernel of
  reduction modulo `M`.

## Relation to the literature

See `New.Spanning.MainTerm.EnergyEstimate` for related work.


### `adelicFrequency`

 A skew frequency `b` at the places of `T`, as a self-adjoint finite adele: extend by zero and
multiply by `-ϖ⁻¹`, where `ϖ = S.deltaE` generates the different. 

### `localFrequency`

 The part at the places of `T` of a self-adjoint finite adele, multiplied by `-ϖ`, where `ϖ =
S.deltaE` generates the different. 

### `localFrequency_adelicFrequency_add`

 `adelicFrequency` is a section of `localFrequency`, compatibly with translations. 

### `sub_adelicFrequency_mul_adeleOfLocal`

 The difference of a self-adjoint adele `z` and `adelicFrequency (localFrequency z)` vanishes at
`T`, so it kills the adeles that vanish off `T`. 

### `ψf_adelicFrequency_mul`

 Let `b` be skew in `LocProd T`, let `b̃ = S.adelicFrequency T b` be `-ϖ⁻¹ b` extended by zero,
and let `y` be a self-adjoint finite adele. Then `ψf E (b̃ y / 2) = P.ψ (τ b y_T)`, where `y_T` is
the part of `y` at `T` and `τ = P.element` has `τ + τ̄ = 1`. `P` is a place structure on `LocProd T`
whose character `P.ψ` is `x ↦ ψf E (-x / ϖ)` (`S.charOnPlaces T`). 

### `ψf_quadric_eq_mul`

 The phase `ψf E (ζ (x* x - β) / 2)` that detects the quadric `x* x = β` is a product of a phase
off `T` and a phase at `T`. The frequency `ζ` is the sum of `S.adelicFrequency T b` and of a
self-adjoint adele `z` for which `S.localFrequency T z` is integral. The vector `x` is the sum of a
vector `y` at `T`, extended by zero (`adeleOfLocal`), and of an adelic vector `w` integral at `T`.
`P` is a place structure on `LocProd T` whose character `P.ψ` is `x ↦ ψf E (-x / ϖ)`
(`S.charOnPlaces T`). 

### `normDensity_indicator_eq_mul`

 Let `f` be the function on adelic vectors that is `Ψ` at `T` times the indicator of the vectors
integral off `T`, and let `β` be hermitian. The density `normDensity f β = ∫ z, ∫ x, f x * ψf E (z
(x* x - β) / 2)` is a product of two factors. The first is the integral of the Gauss sums of the
standard lattice over the self-adjoint `z` for which `S.localFrequency T z`, the part of `-ϖ z` at
`T`, is integral. The second is the density of `Ψ` at `T`, with `P.skewMeasure` the measure on skew
elements and `P.element` of trace `1`. `P` is a place structure on `LocProd T` whose character `P.ψ`
is `x ↦ ψf E (-x / ϖ)` (`S.charOnPlaces T`).

This is a two-factor form of the factorization of the finite adelic density into local densities,
as in Siegel–Weil theory: the density at `T` and one integral of Gauss sums, not split over the
remaining places. 

### `piNAt`

 The finite idele `π = S.piN`, with `π π̄ = N`, read at the places of `T`. 

### `IsFillingData.exists_scaledSiegelConst_eq_and_massRatio_le`

 Let the inverse of the level `M = S.ideleM` be integral off `T`, and let `F` be a filling datum
at `T`: a large lattice datum of modulus `M` for the place structure `P`, whose character is that of
`S`. Let `K(M) = F.congruenceSubgroup` be the group of integral isometries at `T` of the form
`S.latticeMiddle` congruent to `1` modulo `M`, let `Z` be a group between `K(M)` and the integral
isometries, and let `Z.Cosets` be the cosets of `K(M)` in `Z`. Write `μ = F.groupMeasure` for the
measure of the unitary group at `T` and `μ_H = F.measureH` for that of `H = besselH`, the fixer of
all basis vectors outside the definite part `X₀`. Then there is a real `D > 0` with two properties.
The constant `S.scaledSiegelConst` is `D` times the number of classes times the constant
`S.siegelConst` of Siegel's formula. The normalized mass
`Z.massRatio = μ Z * μ K(M) / F.unipotentMass ^ 2`, where `F.unipotentMass` is the product of the
floor volumes below `ϱ`, is at most `μ_H K(M) * (μ K(M) ^ 2 * card Z.Cosets) * D`. 

### `siegel_constant_eq`

 Let `N⁻¹` be integral off `T`, for the prime `N = S.N`. Let `β = (t t̄ - N²) / N` be positive
under the embeddings `Φ v` of the CM type, and let `C` be the constant of Siegel's formula in rank
`k = card 𝔰.κ` at `β`; its first factor `classSum stdRatPoints S.sourceLevel 1` is the mass of the
set `S.Classes` of double cosets of the level `S.sourceLevel` in the definite unitary group. Let `u`
be a unit at `T` with `u ū = N`, and `P.modulus u` its modulus. Then `‖C‖` times `1 + S.b⁻⁶`, the
volume `volÔ E ^ k` of the standard lattice and `P.modulus u` is
`(1 + S.b⁻⁶) * card S.Classes * S.siegelConst` times `(∏ v, (|t|_v² - N²)) ^ (k - 1)`. Here `S.b` is
the size parameter of `S` and `S.siegelConst = (π^k / ((k - 1)! N^k))^f |disc E|^(1/4) (volÔ E)^k`,
with `f` the number of infinite places. 

### `hasCompactSupport_testFunction`

 Let `Ψ` be a function of compact support on the vectors of the whole space over the product
`LocProd T` of the completions at `T`. For `x` in the definite part `X₀` (basis `𝔰.κ`) let
`vectorOfLastEntry π τ x` be `x - (π π̄)⁻¹ τ z` in the basis `besselLatticeBasis 𝔰 π`, with `z` the
last frame vector. Then the function on adelic vectors `y` of `X₀` that is
`Ψ (vectorOfLastEntry π τ y_T)`, with `y_T` the part of `y` at `T`, times the indicator of the
vectors integral off `T` has compact support. 

### `IsFillingData.testFunction_mulVec`

 Let the inverse of the level `M = S.ideleM` be integral off `T`, and let `F` be a filling datum
at `T`: a large lattice datum of modulus `M` for the place structure `P`, whose character is that of
`S`. Let `f` be the function on adelic vectors `x` of `X₀` that is `Ψ (x - N⁻¹ t z)` at `T`
(`vectorOfLastEntry`, for `N = π π̄`, `π = S.piN` and a rational `t`) times the indicator of the
vectors integral off `T`. If `Ψ` is invariant under `besselH ⊓ F.congruenceSubgroup`, then `f` is
invariant under the level `S.sourceLevel` of the finite adelic unitary group `Gf E 𝔰.κ` of `X₀`. 

### `IsFillingData.enorm_normDensity_le_mul_lintegral_normFiberMeasure`

 Let `M = S.ideleM` be the level, and let `F` be a filling datum at `T`: a large lattice datum of
modulus `M` for the place structure `P`, whose character is that of `S`. Let `Ψ ≥ 0` be continuous
of compact support on the vectors of rank `k = card 𝔰.κ` over the product `LocProd T` of the
completions at `T`, and let `β` be hermitian. Let `f` be `Ψ` at `T` times the indicator of the
vectors integral off `T`. The density `normDensity f β = ∫ z, ∫ x, f x * ψf E (z (x* x - β) / 2)`
has norm at most `1 + S.b⁻⁶` times the volume `volÔ E ^ k` of the standard lattice times the
integral of `Ψ` over the sphere `y* y = β` at `T`. The sphere carries the fiber measure
`P.normFiberMeasure` with index `δβ`, the product of `δ = P.skewUnit` and the part of `β` at `T`.

This is an upper bound form of the factorization into local densities in Siegel–Weil theory: the
factor at `T` is kept, and the remaining factor is only bounded, by `(1 + S.b⁻⁶) volÔ E ^ k`. 

### `skewUnit_inv_mul_lastEntrySphereIndex_piNAt`

 Let `t` be in `E`, read at `T` as `ratToPlaces T t`, and let `π = S.piNAt T` be the unit at `T`
with `π π̄ = N = S.N`. Then the index `lastEntrySphereIndex π t` of the sphere
`ω* ω = t t̄ / N - N`, divided by `P.skewUnit`, is the value at `T` of `β = (t t̄ - N²) / N`. 

### `IsFillingData.classes_eq_and_eq_of_inv_mul_mem_congruenceSubgroup`

 Let the inverse of the level `M = S.ideleM` be integral off `T`, and let `F` be a filling datum
at `T`: a large lattice datum of modulus `M` for the place structure `P`, whose character is that of
`S`. The space has the hyperbolic pairs `e_a, e*_a` (`a < ϱ`), a definite part `X₀` with basis `𝔰.κ`
and a vector `z`; `floorGroup 𝔰.ϱ` is the group of isometries that fix the hyperbolic pairs. Let
`γ₁`, `γ₂` be elements of this group over `E` with the same product `⟨z, γ z⟩`
(`S.frameProducts γ 𝔰.top 𝔰.top`) and the same `X₀`-part of `γ z`. Let `h_c` be the representative
of the double coset `c`, and let the left classes `c₁`, `c₂` be equal. If the translates
`h_c⁻¹ γ h_c'` (`S.translateByClassReps`) are integral off `T` and lie in one coset of
`F.congruenceSubgroup` at `T`, then `γ₁ = γ₂` and the right classes `c₁'`, `c₂'` are equal. 

### `IsFillingData.exists_step_sum_fiberPairing`

 Let `Z` be a group between the congruence group `F.congruenceSubgroup` and the integral
isometries, `R` a matrix and `ω p` finitely many heads. The fiber pairing
`F.fiberPairing Z (ω p) (ω q)` is the pairing of the orbital integrals `F.scaledOrbitalIntegral Z`
of two heads, integrated over `besselH`, the fixer of all basis vectors outside the definite part
`X₀`. On the top quadric the positive part of the real part of their sum against `R` agrees with a
function `Ψ ≥ 0` of compact support, invariant under small translations and under
`besselH ⊓ F.congruenceSubgroup`. 

### `IsFillingData.sum_sq_norm_sum_cosetAmplitude_le_headSumNormSq`

 Let the inverse of the level `M = S.ideleM` be integral off `T`, and let `F` be a filling datum
at `T`. Let `Z` be a group between the congruence group `F.congruenceSubgroup` and the integral
isometries at `T`. The heads `a p` (`p : J`) are sequences in `Eˣ`, with Weyl elements
`w_p = weylElem 𝔰.ϱ (a p)` and entries below `ϱ` that are units off `T`; `F.headDensity` is a
product of powers of the moduli of these entries at `T`. Let `W = S.besselFn side` be the Bessel
function at the infinite places or its cut, as `side` says, and let `R` be the Gram matrix of the
tensors `ρ p • ∫ W(y) ⊗ W((w_p γ)⁻¹ y)^* dy` (`besselOrbitalIntegral`). Let `ρ p` times the head
density be the same number `w` for all `p`. Let the integral elements `n i` (`i : ι`) lie in `Z` at
`T` and have distinct reductions `s i`. Then the squared norms of
`∑ p, S.cosetAmplitude side c (s i) c' (w_p γ)`, times `w ^ 2`, the number of cosets of
`F.congruenceSubgroup` in `Z` and the squared volume of `F.congruenceSubgroup`, add up to at most
`F.headSumNormSq` at `g⁻¹`, where `g = S.toPlaces T (S.translateByClassReps c c' γ)` for
`γ ∈ floorGroup 𝔰.ϱ` whose translate is integral off `T`: the pairings of the orbital integrals
`F.scaledOrbitalIntegral` at `T` of two heads, summed against `R`. 

### `IsFillingData.mul_sum_norm_sum_cosetAmplitude_sq_le_fiberPairing`

 The terms over one point `e`. Let the inverse of the level `M = S.ideleM` be integral off `T`,
and let `F` be a filling datum at `T`. Let `Z` be a group between the congruence group
`F.congruenceSubgroup` and the integral isometries at `T`. The heads `a p` (`p : J`) are sequences
in `Eˣ`, with Weyl elements `w_p = weylElem 𝔰.ϱ (a p)` and entries below `ϱ` that are units off `T`;
`F.headDensity` is a product of powers of the moduli of these entries at `T`. Let
`W = S.besselFn side` be the Bessel function at the infinite places or its cut, as `side` says. Let
the triples `(c' i, S.reduction (n i), γ i)`, `i : ι`, be distinct, with `γ i` rational and fixing
the `ϱ` hyperbolic pairs (`floorGroup 𝔰.ϱ`) and `n i` in `Z` at `T`. Let the translates
`h_c⁻¹ γ h_c'` by the class representatives be integral off `T` and send the last frame vector `z`
to `e` at `T` (`orbitPoint 𝔰.top g = g⁻¹ z`). Let the left class `c i`, the product `⟨z, γ i z⟩` and
the `X₀`-part of `γ i z` be the same for all `i`. Let `ρ p` times the head density be `w`. Let `R`
be positive semidefinite and, for every `i`, the Gram matrix of the tensors
`ρ p • ∫ W(y) ⊗ W((w_p γ i)⁻¹ y)^* dy`. Then the squared norms of the sums over `p` of
`S.cosetAmplitude` at `w_p γ i`, times `w ^ 2`, the `F.measureH`-mass and the squared
`F.groupMeasure`-mass of `F.congruenceSubgroup` and the number of its cosets in `Z`, add up to at
most the real part of `∑ p q, R p q * F.fiberPairing Z (ω p) (ω q) e`. Here `ω p` is `a p` read at
`T`, the fiber pairing is the pairing of the orbital integrals of two heads integrated over
`besselH`, and `S.cosetAmplitude side c s c' γ` is the sum of the amplitudes of the rational
`u γ u'⁻¹`, with `u`, `u'` unipotent, whose translate by the class representatives is integral with
reduction `s`. 

### `orbitPoint_toPlaces_translateByClassReps`

 The space has the hyperbolic pairs `e_a, e*_a` (`a < ϱ`), a definite part `X₀` with basis `𝔰.κ`
and a vector `z`; `floorGroup 𝔰.ϱ` is the group of isometries that fix the hyperbolic pairs. Let `γ`
be an element of this group over `E` with `⟨z, γ z⟩ = t`, and `x` the `X₀`-part of `γ z`, moved by
the inverse of the representative of the class `c`. Then at `T` the translate `h_c⁻¹ γ h_c'` sends
`z` to `vectorOfLastEntry S.piN t x = x - N⁻¹ t z`, written in the lattice basis. 

### `IsFillingData.siegel_sum_le_lintegral_sphere`

 Siegel's formula as an upper bound. Let `S` be admissible, with the inverse of the level
`M = S.ideleM` integral off `T`, let `N⁻¹` be integral off `T`, where `N = S.N`, and let `F` be a
filling datum at `T`: a large lattice datum of modulus `M` for the place structure `P`, whose
character is that of `S`. Let `Ψ ≥ 0` be a function of compact support on the vectors over the
product `LocProd T` of the completions at `T`, invariant under small translations and under the
elements of `F.congruenceSubgroup` that fix all basis vectors outside the definite part `X₀`
(`besselH`). Let `|t|_v > N` under all embeddings `Φ v` of the CM type. For a pair `z = (class, v)`
let `x` be the rational vector `v` of `X₀` moved by the inverse of the representative of the class.
If the pairs in a finite set `s` have `N (v* v) = t t̄ - N²` and `x` integral off `T`, then the
values of `Ψ` at `vectorOfLastEntry S.piN t x` (`x` minus `N⁻¹ t` times the last frame vector) add
up to at most the product of `1 + S.b⁻⁶`, the number of classes, `S.siegelConst = (π^k / ((k - 1)!
N^k))^f |disc E|^(1/4) (volÔ E)^k`, `(∏ v, (|t|_v² - N²)) ^ (k - 1)`, the inverse modulus of
`S.piNAt T` (a unit of norm `N`) and the integral of `Ψ ∘ vectorOfLastEntry` over the sphere
`y* y = (t t̄ - N²) / N`, for the fiber measure `P.normFiberMeasure` with index
`lastEntrySphereIndex`. Here `S.b` is the size parameter of `S`, `k` the rank of `X₀` and `f` the
number of infinite places. 

### `x₀Part_mem_integralOff`

 If the lattice basis and the translate `h_c⁻¹ γ h_c'` (`S.translateByClassReps`) of a rational
element `γ` of `floorGroup 𝔰.ϱ` are integral off `T`, then so is the `X₀`-part of the column of `γ`
at `z`, moved by the inverse of the representative of `c`. 

### `IsFillingData.sum_mul_norm_sum_cosetAmplitude_sq_le_lastEntryDensity`

 Siegel's step, for one last entry `t`. Let `S` be admissible, with the inverse of the level
`M = S.ideleM` integral off `T`, let `N⁻¹` and the lattice basis be integral off `T`, and let `F` be
a filling datum at `T`. Let `Z` be a group between the congruence group `F.congruenceSubgroup` and
the integral isometries at `T`. The heads `a p` (`p : J`) are sequences in `Eˣ`, with Weyl elements
`w_p = weylElem 𝔰.ϱ (a p)` and entries below `ϱ` that are units off `T`; `F.headDensity` is a
product of powers of the moduli of these entries at `T`. Let `W = S.besselFn side` be the Bessel
function at the infinite places or its cut, as `side` says. Let the terms
`(c i, c' i, S.reduction (n i), γ i)`, `i : j`, be distinct, with `γ i` rational, fixing the `ϱ`
hyperbolic pairs (`floorGroup 𝔰.ϱ`) and with `⟨z, γ i z⟩ = t`, translates by the class
representatives integral off `T` and `n i` in `Z` at `T`; there is at least one term, `i₀`. Let
`N < ‖t‖` at all infinite places, and let the heads have entry `t` at `ϱ`. Assume that `R` is, for
every `i`, the Gram matrix of the tensors `ρ p • ∫ W(y) ⊗ W((w_p γ i)⁻¹ y)^* dy`
(`besselOrbitalIntegral`), and that `ρ p` times the head density is `r * √G`, where
`G = (∏ v, (‖t‖_v² - N²)) ^ (k - 1)`. Then the squared norms of the sums over `p` of
`S.cosetAmplitude` at `w_p γ i`, times `r ^ 2`, add up to at most
`(1 + S.b⁻⁶) * S.scaledSiegelConst` times the real part of
`∑ p q, R p q * F.lastEntryDensity / Z.massRatio`. 
