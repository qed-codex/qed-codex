---
{
  "module": "src/New/Spanning/MainTerm/GlobalToLocal.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/MainTerm/GlobalToLocal.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/MainTerm/GlobalToLocal.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Class sums as orbit sums, and unfolding at a set of primes

This file links the global sums of the filling argument to the local theory at a finite set `T` of
finite places, stable under conjugation. A finite adelic point is studied through its projection
`New.Filling.toPlaces` to `T` and the condition `New.Filling.IsIntegralOff` of being integral off
`T`. This file writes a class sum as a finite sum of orbit sums over the terms in the big cell. It
compares levels, moduli and characters with those at `T`, and it counts images modulo `M` by
measures. It unfolds each orbit sum to a Kloosterman sum at `T` times an orbital integral at
infinity.

With `h_c` the representative `New.Filling.classRep c` of the class `c`,
`New.Filling.translateByClassReps c c' γ` is `h_c⁻¹ γ h_c'`, `New.Filling.termsOver c s c'` the set
of rational `γ` for which it is integral of reduction `s` modulo `M`, and
`New.Floors.FloorGroups.weylElem ϱ p` the Weyl element `w_p`. `New.Filling.boundedNonzeroIntegers`
is the finite set of bounded nonzero integers that contains the nonzero leading minors of
contributing terms. `New.Filling.entrySet` is the set 𝒯 of quotients of two of its elements. The
number `New.Filling.termDisc γ` is formed from the last two leading minors of the frame products of
`γ`.

## Main definitions and results

* `New.Filling.exists_amplitudeSum_eq_sum_cosetAmplitude`: a class sum for the cut function is a
  finite sum over the heads with entries in the finite set `New.Filling.entrySet`. Let these entries
  be units off `T` and let all terms over `(c, s, c')` lie in the big cell. If the terms with
  `termDisc γ ≠ 0` and one link have a nonzero sum, those that contribute lie in the double cosets
  of the `w_p σ` for one `σ`. These cosets carry the orbit sums `New.Filling.cosetAmplitude`, over
  the `u γ u'⁻¹` with `u`, `u'` in the unipotent group `New.Shape.Form.besselU`.
* `New.Filling.IsFillingData.card_reducedImage_mul_measure_congruenceSubgroup_eq`: let `B` be a
  subgroup of the finite adelic group and `μ` an s-finite measure at `T`, carried by the projections
  of elements of `B` integral off `T` and right invariant under the projections of `B`. Then the
  order of the image of `B ∩ K` modulo `M` times `μ K(M)` is the `μ`-measure of the integral points.
* `New.Filling.IsFillingData.cosetAmplitude_eq_kloostermanSum_smul`: for `γ = w_p σ` with
  `σ ∈ floorGroup ϱ`, and with `h_c⁻¹ γ h_c'` and the inverses of the entries of `p` integral off
  `T`, the orbit sum is a Kloosterman sum at `T` times an orbital integral at infinity. Each double
  coset unfolds to one integral, the double cosets correspond to the pairs in the Kloosterman sum,
  and the values of the extended Bessel character are its terms.
* `New.Filling.IsFillingData.scaledOrbitalIntegral_smul_eq_cosetAmplitude`: so the orbit sum times
  `headDensity` and the mass of `K(M)` is an entry of the integral at `T` times the integral at
  infinity.

Notions from other files:
* `New.Filling.latticeStabilizer`, `New.Filling.principalLevel`: The group `K` of integral points of
  the finite adelic unitary group, and the kernel `K(M)` of its reduction modulo `M`;
  `New.Floors.PlaceData.congruenceSubgroup` is the group `K(M)` at `T`.
* `New.Filling.amplitude`: The integral of β_c(y) β_c'(γ⁻¹y) W(y) ⊗ W(γ⁻¹y)^* over the infinite
  points y, with β_c the cutoff `New.Filling.classCutoff` and W the full or the cut Bessel function
  at infinity, according to the argument `side`.
* `New.Floors.IntegralPlace.extendedBesselChar`: The finite Bessel function, a character of u on u
  K(M) for u in 𝖴 = `New.Shape.Form.besselU`, and 0 off 𝖴 K(M).
* `New.Filling.IsFillingData` (in `New.Spanning.MainTerm.FillingLevel`): the place data at `T` is
  large lattice data for the chosen place structure, with modulus the component of `M` at `T`.
* `New.Filling.cosetAmplitude` (in `New.Spanning.MainTerm.FillingLevel`): the sum of the amplitudes
  of the `u γ u'⁻¹` over the pairs of rational points of 𝖴 for which it is a term over `(c, s, c')`.

## Relation to the literature

See `New.Spanning.MainTerm.EnergyEstimate` for related work.


 ### Terms in the big cell and class sums 

### `translateByClassReps_inv_mul_mul`

 For classes `c`, `c'`, the translate `translateByClassReps c c'` (h_c⁻¹ γ h_c') of
`u⁻¹ * γ * u'` equals the inverse of the translate of `u` by `c, c`, times the translate of `γ` by
`c, c'`, times the translate of `u'` by `c', c'`. 

### `translateByClassReps_mem_floorGroup`

 If `σ` fixes the vectors `e_a`, `e*_a` of the `ϱ` hyperbolic pairs (`floorGroup 𝔰.ϱ`), so does
its translate `h_c⁻¹ σ h_c'` by class representatives. 

### `orbitPoint_top_translateByClassReps_inv`

 Let `σ` fix the vectors `e_a`, `e*_a` of the `ϱ = 𝔰.ϱ` hyperbolic pairs (`floorGroup 𝔰.ϱ`). Let
`L = h_c⁻¹ σ h_c'` be its translate by the representatives of the classes `c`, `c'`, and let `z` be
the last frame vector, of index `𝔰.top`. Then `L z = orbitPoint 𝔰.top L⁻¹` is the vector
`c.out⁻¹ ω - (t / N) z` in the lattice basis, where `N = π π̄` with `π = S.piN`. Here
`t = h(z, σ z)` is the last diagonal entry of `S.frameProducts σ`, `ω` holds the coordinates of
`σ z` at the basis vectors `𝔰.indexX₀ j` of `X₀`, and `c.out ∈ U(X₀)` is the chosen representative
of `c`. 

### `mul_star_dotProduct_eq_last_frameProducts`

 The norm equation. Let `σ` be an isometry of the hermitian form `h` over `E`, and let it fix the
vectors `e_a`, `e*_a` of the `ϱ = 𝔰.ϱ` hyperbolic pairs (`floorGroup 𝔰.ϱ`). Let `z` be the basis
vector `𝔰.z`, the last frame vector (index `𝔰.top`), with `h(z, z) = -N` for the prime `N = S.N`.
Then `N ω̄ · ω = t t̄ - N²`, where `ω` holds the coordinates of `σ z` in the basis of `X₀` indexed
by `𝔰.κ` and `t = h(z, σ z)` is the last diagonal entry of `S.frameProducts σ`. 

### `translateByClassReps_weylElem_mul`

 Weyl elements move to the left of the translate: `h_c⁻¹ (w_p σ) h_c' = w_p (h_c⁻¹ σ h_c')`, with
the entries `p` read in the finite adeles on the right. 

### `leadingMinor_mem_boundedNonzeroIntegers`

 Let `S` satisfy the standing hypotheses `New.Filling.IsAdmissible`. Let `γ` be a term over
`(c, s, c')` (`termsOver`). Suppose that its amplitude for the cut Bessel function W♭, the integral
of `W♭(y) ⊗ W♭(γ⁻¹ y)^*` against the cutoffs of `c`, `c'` over the points `y` at infinity, is
nonzero. Then each nonzero leading minor `δ` of the matrix `S.frameProducts γ = (h(f_j, γ f_l))` of
products of the frame `f` with its image lies in `S.boundedNonzeroIntegers`: it is an integer of `E`
with `‖δ‖ ^ 2 ≤ b ^ (270 n ^ 2)` at every infinite place. Here `b = S.b` is the size parameter of
`S` and `n = 𝔰.n = ϱ + 1`. 

### `entry_mem_entrySet`

 Let `S` satisfy the standing hypotheses `New.Filling.IsAdmissible`. Let `u`, `u'` be rational
points of the group 𝖴 = `besselU` of block upper unitriangular isometries. Let `σ` fix the vectors
`e_a`, `e*_a` of the `ϱ = 𝔰.ϱ` hyperbolic pairs (`floorGroup 𝔰.ϱ`). Let `p ϱ = h(z, σ z)` be the
last diagonal entry of `S.frameProducts σ`. Write `w_p` for the Weyl element `weylElem 𝔰.ϱ p`. Let
`γ = u⁻¹ (w_p σ) u'` be a term over `(c, s, c')` (`S.termsOver c s c'`): `h_c⁻¹ γ h_c'` lies in `K`
and has reduction `s`. Suppose that its amplitude `S.amplitude .cut c c' γ` for the cut Bessel
function W♭ is nonzero. Then for every `a ≤ ϱ` the entry `p a` lies in 𝒯 = `S.entrySet`, the finite
set of quotients of two elements of `S.boundedNonzeroIntegers`. 

### `isStarStable_integralOff`

 For a star-stable set of places `T`, `integralOff T` is closed under `star`. 

### `isIntegralOff_of_mem_termsOver`

 Let `T` be a finite set of finite places, stable under conjugation; integral off `T` means
integral at every finite place outside `T`. Let `u`, `u'` be rational points of the unipotent group
`besselU`. Let `σ` fix the vectors `e_a`, `e*_a` of the `ϱ = 𝔰.ϱ` hyperbolic pairs
(`floorGroup 𝔰.ϱ`). Let the inverses of the entries `p a`, `a < ϱ`, be integral off `T`. Suppose
`γ = u⁻¹ (w_p σ) u'` is a term over `(c, s, c')` (`S.termsOver c s c'`): `h_c⁻¹ γ h_c'` lies in `K`
and has reduction `s`. Then the translates `h_c⁻¹ u h_c` and `h_c⁻¹ σ h_c'` (`translateByClassReps`)
are integral off `T`. 

### `isIntegralOff_weylElem_mul`

 Suppose the entries `p a`, `a < ϱ`, and their inverses are integral off `T`, and `h_c⁻¹ σ h_c'`
(`translateByClassReps c c' σ`) is integral off `T`. Then so is `h_c⁻¹ (w_p σ) h_c'`, where
`w_p = weylElem 𝔰.ϱ p`. 

### `NamesLink`

 The properties of the element `σ` that names the link `Λ` over `(c, s, c')`: it fixes the
hyperbolic planes, the last diagonal entry `t` of its frame products lies in 𝒯 with `t t̄ - N²`
totally positive, and its translate is integral off `T`. The element `k` is a lift of `s`. 

### `NamesLink.mem_floorGroup`

 `σ` fixes the hyperbolic planes. 

### `NamesLink.frameProducts_top_top`

 `t` is the last diagonal entry of the frame products of `σ`. 

### `NamesLink.sq_lt_norm_sq`

 `t t̄ - N²` is totally positive. 

### `NamesLink.reduction_eq`

 `k` reduces to `s`. 

### `NamesLink.link_eq`

 `Λ` is the link of `w_1 σ`, which is that of `w_p σ` for every head `p`. 

### `NamesLink.mem_entrySet`

 The last entry lies in 𝒯. 

### `NamesLink.isIntegralOff`

 The translate `h_c⁻¹ σ h_c'` is integral off `T`. 

### `sq_lt_norm_sq_last_frameProducts`

 Let `σ` fix the vectors `e_a`, `e*_a` of the `ϱ = 𝔰.ϱ` hyperbolic pairs (`floorGroup 𝔰.ϱ`), and
let `θ = h(z, σ z)` be the last diagonal entry of the matrix `S.frameProducts σ` of products of the
frame with its image under `σ`. Let `N = S.N` be the prime with `h(z, z) = -N`. If `θ θ̄ ≠ N²`, then
`N² < |θ|²` at every infinite place `v`, read through its chosen embedding `Φ v`. 

### `injective_bigCellTerm`

 For `σ` fixing the `ϱ` hyperbolic pairs, the map `(p, u, u') ↦ u (w_p σ) u'⁻¹` is injective,
where `u`, `u'` are rational points of 𝖴 = `besselU` and `p` is a `ϱ`-tuple with entries in 𝒯 =
`S.entrySet`, completed by the last entry `t` (`padTuple`). 

### `weylElem_padTuple`

 The Weyl element depends only on the entries of its tuple below `ϱ`, so these may be completed
by any last entry `t`. 

### `head_and_last_mem_entrySet`

 Let `S` satisfy the standing hypotheses `New.Filling.IsAdmissible`. Let `σ` fix the vectors
`e_a`, `e*_a` of the `ϱ = 𝔰.ϱ` hyperbolic pairs (`floorGroup 𝔰.ϱ`), let `t` be the last diagonal
entry of `S.frameProducts σ`, and let `u`, `u'` lie in the unipotent group `besselU`. Let
`γ = u⁻¹ (w_p σ) u'` be a term over `(c, s, c')`, and suppose that its amplitude for the cut Bessel
function W♭, the integral of `W♭(y) ⊗ W♭(γ⁻¹ y)^*` against the cutoffs of `c`, `c'` over the points
`y` at infinity, is nonzero. Then `t` and the entries `p a`, `a < ϱ`, lie in 𝒯 = `S.entrySet`, the
finite set of quotients of two elements of `S.boundedNonzeroIntegers`. 

### `mem_termsOfLink_bigCell`

 Let `σ` fix the vectors `e_a`, `e*_a` of the `ϱ = 𝔰.ϱ` hyperbolic pairs (`floorGroup 𝔰.ϱ`). Let
`θ = h(z, σ z)` be the last diagonal entry of the matrix `S.frameProducts σ` of products of the
frame with its image, and suppose `θ θ̄ ≠ N²` for `N = S.N = -h(z, z)`. Let `u`, `u'` lie in the
group 𝖴 = `besselU` of block upper unitriangular isometries, and take the Weyl element
`w_p = weylElem 𝔰.ϱ p`, with `e_a ↦ p_a e*_a` and `e*_a ↦ e_a / p̄_a` for `a < ϱ`. Then
`γ = u (w_p σ) u'⁻¹` lies in `S.termsOfLink Λ` for the link `Λ` (`New.link`) of `w_1 σ`: the link of
`γ` is `Λ`, and `termDisc γ = D D̄ - N² D' D̄'` is nonzero, with `D`, `D'` the last two leading
minors of `S.frameProducts γ`. 

### `exists_amplitudeSum_eq_sum_cosetAmplitude`

 A sum of amplitudes is a finite sum of orbit sums over 𝖴 × 𝖴, with 𝖴 = `besselU`. Let `S`
satisfy the standing hypotheses `New.Filling.IsAdmissible`, and let the elements of the finite set
𝒯 = `S.entrySet` be units off the set of places `T`. The terms over `(c, s, c')` are the rational
`γ` with `h_c⁻¹ γ h_c'` in the group `K = S.latticeStabilizer` of integral points and of reduction
`s`; let the leading minors `D_0, …, D_ϱ` of their matrices `S.frameProducts γ` be nonzero. Let `A`
be the sum `amplitudeSum` of the amplitudes, for the cut Bessel function, of the terms with
`termDisc γ = |D_{ϱ+1}|² - N² |D_ϱ|² ≠ 0` and link `Λ`, and suppose `A ≠ 0`. Then there are `t ∈ 𝒯`,
`σ` and `k ∈ K` with the properties `NamesLink`: `σ` fixes the `ϱ` hyperbolic pairs, `t` is the
last diagonal entry of `S.frameProducts σ`, `t t̄ - N²` is totally positive, `Λ` is the link of
`w_1 σ`, `h_c⁻¹ σ h_c'` is integral off `T`, and `k` reduces to `s`. Moreover `A` is the sum, over
the `ϱ`-tuples `p` in 𝒯 followed by `t` (`padTuple`), of the sums `cosetAmplitude` of the amplitudes
of the terms `u w_p σ u'⁻¹` with `u`, `u'` in 𝖴. 

 ### Global against local: levels, moduli and characters 

### `vectorOfLastEntry_evalPlaces`

 For a finite adele `t` and a tuple `x` of finite adeles, the vector `vectorOfLastEntry` of their
projections to `T`, formed with the projection of `S.piN`, is the projection of their vector
`vectorOfLastEntry`. 

### `toPlaces_translateByClassReps_weylElem_mul`

 The projection to `T` of h_c⁻¹ w_p σ h_c' is w_p times the projection of h_c⁻¹ σ h_c'. 

### `_root_.New.Floors.IntegralPlace.modulus_evalPlaces_rpow_half`

 Let `P` be a structure of a finite place on the product of the completions at `T`, with modulus
`P.modulus`. Let `x` and `x⁻¹` lie in the ring `ratIntegralOff T` of `T`-integers of `E`. Then the
square root of `P.modulus` at the component `evalPlaces T x` of `x` at `T` is the inverse of the
product of the absolute values `‖Φ v x‖` over the infinite places `v`, with `Φ v` the chosen
embedding. 

### `IsFillingData.mem_principalLevel_iff`

 Let `F` be a filling datum at `T` (`hF`): a large lattice datum on the completions at `T` whose
modulus `F.levelUnit` is the component of `M = p₀p₁ = S.ideleM`. Let `M⁻¹` be integral off `T`
(`hM_inv`). A finite adelic point `x` lies in the principal level `K(M)` exactly when it is integral
off `T` and its projection to `T` lies in the group `K(M) = F.congruenceSubgroup`. 

### `IsFillingData.reduction_eq_iff`

 Let `F` be a filling datum at `T` (`hF`): a large lattice datum on the completions at `T` whose
modulus `F.levelUnit` is the component of `M = p₀p₁ = S.ideleM`. Let `M⁻¹` be integral off `T`
(`hM_inv`). Two elements `k`, `l` of the group `K` of integral points have the same reduction modulo
`M` exactly when their projections to `T` are in the same left coset of
`K(M) = F.congruenceSubgroup`. 

### `IsFillingData.psi_simpleRootSum_eq_unipotentChar`

 Let `F` be a filling datum at `T` (`hF`): a large lattice datum on the completions at `T` whose
modulus `F.levelUnit` is the component of `M = p₀p₁ = S.ideleM`. Let `M⁻¹` be integral off `T`
(`hM_inv`). For a finite adelic point `x` integral off `T`, the character `P.ψ` at the sum of the
simple root coordinates of its projection, divided by `F.levelUnit`, is the unipotent character of
`S` at `x`. 

### `IsFillingData.modulus_levelUnit`

 Let `F` be a filling datum at `T` (`hF`): a large lattice datum on the completions at `T` whose
modulus `F.levelUnit` is the component of `M = p₀p₁ = S.ideleM`. Let `M⁻¹` be integral off `T`
(`hM_inv`). Then `P.modulus F.levelUnit` is `(M ^ f)⁻¹ ^ 2`, with `M` read as the natural number
`S.M` and `f` the number of infinite places of `E`. 

### `IsFillingData.unipotentOrder_mul_unipotentMass_eq_one`

 Let `F` be a filling datum at `T` (`hF`): a large lattice datum on the completions at `T` whose
modulus `F.levelUnit` is the component of `M = p₀p₁ = S.ideleM`. Let `M⁻¹` be integral off `T`
(`hM_inv`). Let 𝖴 = `besselU` be the group of block upper unitriangular isometries. The order
`S.unipotentOrder` of the reduction modulo `M` of the integral points of 𝖴, times the measure
`F.unipotentMass` of 𝖴 ∩ K(M) at `T`, is one. Here `K(M) = F.congruenceSubgroup` consists of the
integral points congruent to `1` modulo `M`. 

 ### Counting images modulo `M` by measures 

### `IsFillingData.card_reducedImage_mul_measure_congruenceSubgroup_eq`

 Let `F` be a filling datum at `T` (`hF`): a large lattice datum on the completions at `T` whose
modulus `F.levelUnit` is the component of `M = p₀p₁ = S.ideleM`. Let `M⁻¹` be integral off `T`
(`hM_inv`). Let `B` be a subgroup of the finite adelic unitary group and `μ` an s-finite measure on
the unitary group over the product `LocProd T` of the completions at `T`. Suppose that almost every
point for `μ` is the projection (`toPlaces`) of an element of `B` integral off `T`, and that `μ` is
invariant under right translation by the projections of the elements of `B`. Then the order of the
image `S.reducedImage B` modulo `M` of the integral points of `B`, times the measure of the
principal congruence subgroup `K(M) = F.congruenceSubgroup`, is the measure of the group
`unitaryLevel P.integers 1 _` of integral points at `T`. 

 ### Double cosets and the Kloosterman sum 

### `hasSum_besselOrbitalIntegral_cosetAmplitude`

 Let `γ = w_p σ` with `σ` fixing the `ϱ` hyperbolic pairs of the basis. Let 𝖴 = `besselU` be the
unipotent group and `𝖴_c(M) = S.classUnipotent c` the group of its rational points `u` with
`h_c⁻¹ u h_c ≡ 1` modulo `M`. Let `r` and `r'` list rational points of 𝖴 without repetition, with
exactly one in each of the cosets `u 𝖴_c(M)` and `u' 𝖴_c'(M)` for which `u⁻¹ γ u'` is a term. Let
`W = S.besselFn side` be the full or the cut Bessel function on the points at infinity. Then the sum
`cosetAmplitude` of the amplitudes of the terms `u γ u'⁻¹` is the sum, over the pairs of
representatives that give a term `δ`, of the orbital integrals `∫ W(y) ⊗ W(δ⁻¹ y)^* dy`. 

### `IsFillingData.mem_termsOver_iff`

 Let `F` be a filling datum at `T` (`hF`), that is, a large lattice datum on the completions at
`T` whose modulus `F.levelUnit` is the component of `M = p₀p₁ = S.ideleM`. Let `M⁻¹` be integral off
`T` (`hM_inv`). Let `k` be a point of `S.latticeStabilizer`, with reduction `S.reduction k` modulo
`M`. Let `γ` be a rational element whose translate `S.translateByClassReps c c' γ = h_c⁻¹ γ h_c'` is
integral off `T` (`h_off`). Then `γ` lies in `S.termsOver c (S.reduction k) c'` exactly when the
projection of its translate to `T` lies in `S.toPlaces T k · K(M)`, with
`K(M) = F.congruenceSubgroup`. Lying in `S.termsOver` means the translate is integral with reduction
`S.reduction k`. 

### `IsFillingData.exists_injective_mem_besselU_and_isIntegralOff`

 Let `F` be a filling datum at `T` (`hF`): a large lattice datum on the completions at `T` whose
modulus `F.levelUnit` is the component of `M = p₀p₁ = S.ideleM`. Let `M⁻¹` be integral off `T`
(`hM_inv`). Let `S` satisfy the standing hypotheses `New.Filling.IsAdmissible`, let 𝖴 = `besselU` be
the group of block upper unitriangular isometries, and put `K(M) = F.congruenceSubgroup` and
`𝖴_c(M) = S.classUnipotent c`. The translate `S.translateByClassReps c c u = h_c⁻¹ u h_c`, read at
`T`, matches the cosets `u 𝖴_c(M)` of the points `u` of 𝖴 over `E` whose translate is integral off
`T` with the cosets of `𝖴 ∩ K(M)` in 𝖴 at `T`. This is stated by a list `r` of rational
representatives, one for each coset at `T`. 

### `IsFillingData.extendedBesselChar_toPlaces_translateByClassReps`

 Let `F` be a filling datum at `T` (`hF`): a large lattice datum on the completions at `T` whose
modulus `F.levelUnit` is the component of `M = p₀p₁ = S.ideleM`. Let `M⁻¹` be integral off `T`
(`hM_inv`). For a rational point `u` of 𝖴 = `besselU` whose translate `h_c⁻¹ u h_c` is integral off
`T`, the finite Bessel function `P.extendedBesselChar F.levelUnit` at the projection of the
translate is the character `S.unipotentChar` at the finite part of `u`. 

### `besselOrbitalIntegral_ratToInf_besselU_mul`

 Phases at the infinite places. Let `W = S.besselFn side` be the full or the cut Bessel function
at infinity (`side : FullOrCut`), and `J(γ) = ∫ W(y) ⊗ W(γ⁻¹ y)^* dy` the orbital integral
`besselOrbitalIntegral`. Let `u`, `u'` be rational points of the group 𝖴 = `besselU` of block upper
unitriangular isometries, and let `γ` be rational. Then `J(S.ratToInf (u⁻¹ γ u')) = ψ(u) conj ψ(u')
J(S.ratToInf γ)`, where `ψ(u) = S.unipotentChar (S.ratToFin u)` is the character of 𝖴 at the image
of `u` at the finite places. 

### `IsFillingData.cosetAmplitude_eq_kloostermanSum_smul`

 Let `F` be a filling datum at `T` (`hF`): a large lattice datum on the completions at `T` whose
modulus `F.levelUnit` is the component of `M = p₀p₁ = S.ideleM`. Let `M⁻¹` be integral off `T`
(`hM_inv`). Let `γ = w_p σ`, with the inverses of the entries `p a`, `a < ϱ`, integral off `T`, `σ`
fixing the `ϱ` hyperbolic pairs and `h_c⁻¹ γ h_c'` integral off `T`. Let `x` and `s` be the
projections to `T` of `h_c⁻¹ γ h_c'` and of the integral point `k`, and `k̄` the reduction of `k`.
The Kloosterman sum `F.kloostermanSum x s` is the sum of `χ(u) conj χ(u')` over the cosets `u`, `u'`
in `𝖴 / (𝖴 ∩ K(M))` at `T` with `u⁻¹ x u' ∈ s K(M)`, where `χ` is the character of 𝖴 = `besselU`.
Then the orbit sum `New.Filling.cosetAmplitude` of `γ` over `(c, k̄, c')` is this sum times the
orbital integral of `γ` at the infinite places, for the full or the cut Bessel function
`S.besselFn side`. 

### `IsFillingData.scaledOrbitalIntegral_smul_eq_cosetAmplitude`

 Unfolding, for either of the Bessel functions at infinity. Let `S` be admissible, and let `F` be
a filling datum at `T` (`hF`): a large lattice datum on the completions at `T` whose modulus
`F.levelUnit` is the component of `M = p₀p₁ = S.ideleM`. Let `M⁻¹` be integral off `T` (`hM_inv`).
Put `K(M) = F.congruenceSubgroup`. Let `γ = w_p σ`, with `w_p = weylElem 𝔰.ϱ p`. Suppose the
inverses of the entries `p i`, `i < ϱ`, are integral off `T`, `σ` fixes the `ϱ` hyperbolic pairs,
and `h_c⁻¹ γ h_c'` is integral off `T`, for class representatives `h_c`, `h_c'` of `c`, `c'`. Let
`Z` be a group between `K(M)` and the integral points at `T`. Let `k ∈ S.latticeStabilizer`, and let
the cosets `a`, `b` of `Z.Cosets` satisfy `k⁻¹ a b⁻¹ ∈ K(M)`. Let `q` and `l` be the projections to
`T` of `p` and of `h_c⁻¹ σ h_c'`, and let `κ = F.headDensity 𝔰.ϱ q 1` be the density, a product of
powers of the `P.modulus (q i)`, `i < ϱ`. Then `F.scaledOrbitalIntegral Z q l⁻¹` is `κ` times the
orbital integral of the finite Bessel vector of `Z` at `w_q l`. Its entry `(a, b)` times the
integral `New.besselOrbitalIntegral` of `γ` at the infinite places is `κ` times the measure of
`K(M)` times the orbit sum `New.Filling.cosetAmplitude` of `γ` over `(c, k̄, c')`, with `k̄` the
reduction of `k`. 
