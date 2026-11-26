---
{
  "module": "src/New/Spanning/Unfolding/AmplitudeSums.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/AmplitudeSums.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/AmplitudeSums.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Sums of amplitudes over blocks

This file proves convergence, change of weight and the behaviour under the Bessel subgroup of the
block sums `S.amplitudeSum side T c s c'`. The block is the sum, over the rational `γ ∈ T` that lie
over `(c, s, c')` (`New.Filling.termsOver`), of the amplitudes
`∫ β_c(y) β_c'(γ⁻¹ y) W(y) ⊗ W(γ⁻¹ y)^* dy`. Here `β_c = S.classCutoff c` is a cutoff for the group
`S.classUnipotent c`, the argument `side : FullOrCut` selects the full or the cut Bessel function
`W`, and `ν = New.Filling.unipotentCovolume`. The listed results assume that `S` is admissible
(`New.Filling.IsAdmissible`).

## Main definitions and results

* `New.Filling.exists_tsum_classCutoff_mul_prod_enorm_le`,
  `New.Filling.tsum_amplitudeMajorant_lt_top`,
  `New.Filling.tsum_lintegral_enorm_besselKernel_sub_cut_le`: the sums are bounded and converge
  absolutely, and cutting `W` changes them little.
* `New.Filling.hasSum_amplitudeSum_of_cutoff`: for stable `T`, any measurable weight with orbit sums
  `1` may replace the product of the cutoffs `S.classCutoff c` and `S.classCutoff c'`.
* `New.Filling.amplitudeSum_mul_mul_inv`, `New.Filling.amplitudeSum_besselU_mul`: moving a block by
  the Bessel subgroup; the unipotent part acts through the character `New.Filling.unipotentChar`.
* `New.Filling.amplitudeSum_eq_zero_of_not_agrees`: the block of a stable set vanishes unless `s`
  agrees.
* `New.Filling.amplitudeSum_besselS_one_eq_ite`: for the full Bessel function only, at `s = 1` the
  Bessel subgroup contributes `S.unipotentCovolume` times the identity if `c = c'`, and `0`
  otherwise.

Notions from other files:
* `New.Filling.latticeStabilizer`, `New.Filling.reduction`, `New.Filling.ResidueGL`: the group K of
  integral elements of the finite adelic unitary group, and its reduction modulo the chosen places
  above p₀ and p₁, with values in the product `ResidueGL` of the general linear groups over the
  residue fields. The kernel is K(M) = `New.Filling.principalLevel`.
* `New.Filling.termsOver`: a rational `γ` is a term over `(c, s, c')` if h_c⁻¹ γ h_c' lies in K and
  has reduction `s`; here h_c = `S.classRep c` represents the class `c`.
* `New.Shape.Form.besselU`, `New.Shape.Form.besselS`, `New.Filling.IsStable`: the group 𝖴 of block
  upper unitriangular isometries, and the Bessel subgroup, which 𝖴 generates together with the
  unitary group of the standard form on κ; a set `T` of rational elements is stable if
  multiplication on either side by rational points of 𝖴 does not affect membership in `T`.
* `New.Filling.IsAdmissible`: the standing hypotheses. The level `sourceLevel` is the preimage of
  K(M), `reduction` is onto, and size inequalities hold between b, M and ϖ, κ_v, N, the second
  moments, the number of Bessel coordinates, an index and the constant `scaledSiegelConst`.
* `New.Filling.classUnipotent`, `New.Filling.unipotentCovolume`: the rational points u of 𝖴 with
  h_c⁻¹ u h_c in the principal congruence subgroup K(M); an explicit positive number built from M,
  N, |κ|, ϱ, the discriminant of E and the scales of the frame at the infinite places.

## Relation to the literature

The results on block sums belong to two steps: the bound for the second moment of the Poincaré
series (`New.Spanning.Unfolding.Moments`, which lists related work) and the bound for degenerate
terms and pairs with different links (`New.Spanning.RemainingTerms.Sum`).


 ### Preliminaries on cutoffs, the kernel, sums by layers and majorants 

### `isStable_besselS`

 The rational points of the Bessel subgroup `besselS` form a stable set: multiplying on either
side by rational points of `besselU` does not affect membership in `besselS`. 

### `sigmaFinite_orbitMeasure`

 The quotient measure of a unimodular Haar measure `ν` on a subgroup of `G₁` is σ-finite, as its
density, a chosen cutoff for `ν`, is almost everywhere finite. 

### `measurePreserving_pi_orbitMeasure`

 Unfolding at several places: if `ν` is a unimodular Haar measure on a subgroup of `G₁`, then
`(x, u) ↦ (u v * x v)_v` carries the product of the quotient measures and of the copies of `ν` to
the Haar measure on `P → G₁`, for a finite type `P`. 

### `tsum_integral_apply`

 Let `g j`, for `j` in a countable index set `J`, be measurable functions with values in a
finite-dimensional space `EuclideanSpace ℂ I`, and let the sum over `j` of the integrals of `‖g j‖`
be finite. Then the `i`-th coordinate of `∑' j, ∫ g j` equals the integral of `∑' j, (g j x) i`. 

### `noncomputable instance : Fintype S.ResidueGL`

 The group `S.ResidueGL`, a finite product of general linear groups over finite residue fields,
is finite. 

### `besselFn_mul_of_mem_classUnipotent`

 The Bessel function `S.besselFn side` is invariant under left translation by the image at the
infinite places of the group `S.classUnipotent c` of a class `c`. 

### `besselKernel_besselU_mul`

 Let `besselKernel γ y` be the tensor `besselFn(y) ⊗ besselFn(γ⁻¹ y)^*` of Bessel functions. Let
`u`, `u'` lie in the unipotent subgroup `besselU` of `(S.ratMiddle E).G`, the group `S.G E` of
rational isometries of the form with middle Gram matrix `S.ratMiddle E`. Then the kernel at
`(u γ u'⁻¹, u y)` is `ψ(u)⁻¹ ψ(u')` times the kernel at `(γ, y)`. Here `ψ` is `unipotentChar`
applied to the finite-adelic images `ratToFin u` and `ratToFin u'`. 

### `lintegral_classCutoff_mul_prod`

 Unfolding: let each `w v` be measurable and left invariant under the unipotent group `besselU`
(`FixesLeft`). Then the integral of the cutoff `S.classCutoff c y` of the class `c` times
`∏ v, w v (y v)` is the covolume `S.unipotentCovolume` times the product of the integrals of the
`w v` for the quotient measure `besselQuotMeasure` on `𝖴 \ G₁`. 

### `tsum_mul_inv_pow_le_of_layers`

 Summation by layers. Let `u ≥ 1` and `K ≥ 0`. If the points with `u p ≤ R` have total weight at
most `(K R ^ e) ^ d` for all `R ≥ 1`, then the weighted sum of `u p ^ (-i)` is at most `2 K ^ d` as
soon as `2 e d < i`. 

### `scaledBesselLengthProd`

 The product over the infinite places `v` of the scaled lengths of `y v`, each of which is
`max 1 (besselLength (y v) / b ^ (6 n))`. Here `besselLength x` is the infimum of `‖s x‖ + 1` over
`s` in the Bessel subgroup `besselS`, `b = S.b` and `n = ϱ + 1`. 

### `one_le_scaledBesselLengthProd`

 The product of the scaled lengths over the infinite places is at least one. 

### `scaledBesselLength_le_scaledBesselLengthProd`

 The scaled length at one infinite place is at most the product of all of them. 

### `tsum_classCutoff_mul_inv_pow_le`

 Let `S` be admissible, `T` a set of rational elements, `c` a class and `s` an element of the
finite group `S.ResidueGL`. Write `γ⁻¹ y` for `(S.ratToInf γ)⁻¹ * y`. Over all classes `d` and all
`γ` in `T ∩ S.termsOver c s d`, the cutoff `S.classCutoff d` at `γ⁻¹ y` times
`S.scaledBesselLengthProd (γ⁻¹ y) ^ (-(r ^ 3 * f))` adds up to at most `2 b ^ (12 n ^ 3 r f)`. Here
`b = S.b` is the real size parameter of `S`, `f` is the number of infinite places, `n = ϱ + 1` and
`r` is the rank of `G₁`. 

### `le_scaledBesselLengthProd_mul`

 Let `besselKernel γ y` be the tensor `besselFn(y) ⊗ besselFn(γ⁻¹ y)^*` of Bessel functions.
Where the kernel chosen by `side` differs from the cut kernel, the full and the cut Bessel function
differ at some place, at `y` or at `γ⁻¹ y`; so the product of the scaled lengths
(`scaledBesselLengthProd`) of the two points is at least the size parameter `S.b`. 

### `pow_mul_pow_mul_prod_enorm_le`

 Let `hw` say that at each infinite place `v` the function `w v` is a decay majorant
(`IsDecayMajorant`, with constants `S.b` and `a v`) of the Bessel functions
`(S.besselSystem v).besselFn`. That is, `w v` bounds their norms times the scaled length
`max 1 (besselLength x / b ^ (6 n))` to the power `3 * r ^ 3 * f`. Here `b = S.b`, `n = ϱ + 1`, `r`
is the rank of `G₁` and `f = numInfPlaces E`. Then for every `y`, the product over `v` of the norms
`‖besselFn side (y v)‖`, times `scaledBesselLengthProd y` to the power
`r ^ 3 * f + 2 * (r ^ 3 * f)`, is at most the product over `v` of `w v (y v)`. 

### `pow_mul_prod_enorm_le_majorant`

 At each infinite place `v` let the function `w v` be a decay majorant (`IsDecayMajorant`) of the
Bessel functions: it bounds their norm times the scaled length to the power `3 * r ^ 3 * f`, where
`r` is the rank of `G₁` and `f` the number of infinite places. Then the product over the places of
the norms, times the product `scaledBesselLengthProd` of the scaled lengths to the power
`2 * (r ^ 3 * f)`, is at most the product of the `w v`. 

### `pow_mul_prod_enorm_le_bound`

 At each infinite place `v` let the function `w v`, bounded by the constant `a v`, be a decay
majorant (`IsDecayMajorant`) of the Bessel functions: it bounds their norm times the scaled length
to the power `3 * r ^ 3 * f`, where `r` is the rank of `G₁` and `f` the number of infinite places.
Then the product of the norms, times the product `scaledBesselLengthProd` of the scaled lengths to
the power `2 * (r ^ 3 * f)`, is at most the product of the `a v` times `scaledBesselLengthProd` to
the power `-(r ^ 3 * f)`. 

### `enorm_besselKernel_sub_cut_le`

 At each infinite place `v` there are a Bessel function W and its cut W♭, of bounded support
modulo the Bessel subgroup. Let the function `w v`, bounded by the constant `a v`, be a decay
majorant (`IsDecayMajorant`): it bounds the norms of W and W♭ times the scaled length
`max 1 (besselLength / b ^ (6 n))` to the power `3 * r ^ 3 * f`. Then the kernel
`W(y) ⊗ W(γ⁻¹ y)^*`, built from W or W♭ as `side` says, and the kernel built from W♭ differ by at
most `2 * b ^ (-(2 * (r ^ 3 * f)))` times the product of the `w v` at `y`, the product of the `a v`
and the product of the scaled lengths of `γ⁻¹ y` (`scaledBesselLengthProd`) to the power
`-(r ^ 3 * f)`. Here `b = S.b`, `n = ϱ + 1`, `r` is the rank of `G₁` and `f` the number of infinite
places. 

### `cut_exponent_le`

 For 12 n³ + 500 ≤ k < r and f ≥ 1, the exponent 12 n³ r f + 1 + 400 r² f + 2 k f of the
losses in the tail bound plus the saving k³ f is at most the gain 2 r³ f. 

### `tsum_classCutoff_mul_const_mul_inv_pow_le`

 Let `E` contain a primitive 5040th root of unity, let `S` be admissible and let `T` be a set of
rational elements. Sum, over all classes `d` and all `γ ∈ T` that are terms over `(c, s, d)`
(`termsOver`), the cutoff of `d` at `γ⁻¹ y` times `A` times the product of the scaled lengths of
`γ⁻¹ y` (`scaledBesselLengthProd`) to the power `-(r ^ 3 * f)`. The sum is at most
`A * 2 b ^ (12 n ^ 3 r f)`. Here `b = S.b` is the size parameter of `S`, `f` is the number of
infinite places, `n = ϱ + 1` and `r` is the rank of the hermitian space of `G₁`. 

### `tsum_lintegral_classCutoff_mul_majorant_le`

 Let `S` be admissible and `T` a set of rational elements. At each infinite place `v` let `w v`
be a decay majorant of the Bessel functions (`IsDecayMajorant`); what is used is that `w v` is
measurable and left invariant under the unipotent group `besselU`, and that the constant `a v` times
the integral of `w v` over `𝖴 \ G₁` is at most `b ^ (400 r ^ 2)` times the dimension of the value
space. Let `d` run over all classes and `γ` over the terms of `T` over `(c, s, d)`. Then the sum of
the integrals of `β_c(y) β_d(γ⁻¹ y)` times the product of the `w v` at `y`, the product of the `a v`
and `scaledBesselLengthProd (γ⁻¹ y)` to the power `-(r ^ 3 * f)` is at most `ν * 2 b ^ (12 n ^ 3 r
f) * b ^ (400 r ^ 2 f) * card S.BesselCoord`. Here `β_c = S.classCutoff c`,
`ν = S.unipotentCovolume`, `b` is the size parameter of `S`, `f` is the number of infinite places,
`n = ϱ + 1` and `r` is the rank of `G₁`. 

### `inv_pow_mul_unipotentCovolume_mul_card_le`

 For admissible `S`, twice the product of `ν`, `2 b ^ (12 n ^ 3 r f)`, `b ^ (400 r ^ 2 f)` and
the number `card S.BesselCoord` of Bessel coordinates, divided by `b ^ (2 r ^ 3 f)`, is at most
`ν b ^ (-k³ f) / 2`. Here `b` is the size parameter of `S`, `f` the number of infinite places,
`ν = S.unipotentCovolume`, `k = 𝔰.k`, `n = ϱ + 1` and `r` is the rank of `G₁`. 

 ### Convergence and the tail bound 

 At each place the Bessel functions lie below an invariant majorant `w v`, bounded by a constant
`a v`, with the power `3 i` of the scaled length to spare, `i = r ^ 3 f`. At `γ⁻¹ y` the power `i`
makes the sum over `γ` converge; at `y` we unfold `classCutoff c` and integrate `w`. The power `2 i`
that is left at both points gains `b ^ (-2 i)` where the cut acts, and this beats all the losses. 

### `le_scaledBesselLengthProd_pow_mul`

 A power of the product of the scaled lengths is at least `1`, so it may be inserted as a
factor. 

### `exists_tsum_classCutoff_mul_prod_enorm_le`

 Let the CM field `E` contain a primitive 5040th root of unity, and let the data `S` satisfy the
standing hypotheses `IsAdmissible`. Let `d` run over all classes and `γ` over the elements of `T`
that are terms over `(c, s, d)`. Then the sum of `β_d(γ⁻¹ y) ∏_v ‖W_v((γ⁻¹ y)_v)‖` is at most a
finite constant `C` that does not depend on the point `y` of G_∞, the product of one copy of `G₁`
for each infinite place `v`. 

### `tsum_amplitudeMajorant_lt_top`

 Let `S` be admissible, and let `γ` run over the elements of `T` that are terms over `(c, s, d)`,
for all classes `d`. The sum of the integrals `∫ β_c(y) β_d(γ⁻¹ y) ‖W(y) ⊗ W(γ⁻¹ y)^*‖ dy`
(`amplitudeMajorant`) is finite. 

### `tsum_lintegral_enorm_besselKernel_sub_cut_le`

 Let `S` be admissible, let `d` run over all classes and `γ` over the elements of `T` that are
terms over `(c, s, d)`. The kernel `besselKernel side γ y` is `W(y) ⊗ W(γ⁻¹ y)^*`. The sum of the
integrals of `β_c(y) β_d(γ⁻¹ y)` times the norm of the difference between this kernel and the one
built from the cut function is at most `ν b ^ (-k³ f) / 2`. Here `ν = S.unipotentCovolume`,
`β_d = S.classCutoff d`, `k + 1` is the size of the middle block of the basis (`k = 𝔰.k`), `f` is
the number of infinite places and `b` is the size parameter of `S`. 

### `summable_amplitude`

 For admissible `S`, the amplitudes of the elements of `T` over `(c, s, c')` are summable. 

### `mem_termsOver_iff_mul_mul_inv_mem`

 If `σ` is a term over `(c, t, c₁)` and `σ'` one over `(c', t', c₁')`, then `γ` is a term over
`(c₁, s, c₁')` if and only if `σ γ σ'⁻¹` is one over `(c, t s t'⁻¹, c')`. 

### `tsum_classCutoff_ratToInf_mul_eq_one`

 Let `E` contain a primitive 5040th root of unity and let `S` be admissible. Let `σ` be a
rational isometry of the form with middle Gram matrix `S.ratMiddle E`. Assume that `σ` lies in the
Bessel subgroup `besselS`, generated by the unipotent group `besselU` and U(X₀), and is a term over
`(c, t, c₁)` (`termsOver`). Then `y ↦ S.classCutoff c (σ y)` has orbit sums `1` under
`S.classUnipotent c₁`, the rational points `u` of `besselU` with h_c₁⁻¹ u h_c₁ in the principal
congruence subgroup of level `S.M`. 

### `integral_classCutoff_eq_unipotentCovolume`

 For admissible `S`, every class `c` and archimedean point `x`, the integral of `u ↦ β_c(u x)`,
`β_c = S.classCutoff c`, read as a complex function, over the product of the groups `besselU` is
`S.unipotentCovolume`. 

 ### Change of weight and moving blocks 

### `mul_mul_inv_mem_inter_termsOver`

 Let `S` be a filling of shape `𝔰` over the CM field `E`. For stable `T`, the set of terms of `T`
over `(c, s, c')` is stable under `γ ↦ u γ u'⁻¹` for `u` in `S.classUnipotent c` and `u'` in
`S.classUnipotent c'`. 

### `lintegral_mul_eq_of_isCutoff`

 Let the group `H`, with an s-finite inversion invariant measure `η`, act measurably on `Z` and
preserve the s-finite measure `μ`. A cutoff (`IsCutoff η β`) is a measurable `β : Z → [0, ∞]` with
`∫ β (u • p) dη(u) = 1` for every `p`. Two cutoffs `β`, `β'` give every invariant measurable `F` the
same integral: `∫ β F dμ = ∫ β' F dμ`. 

### `hasSum_amplitudeSum_of_cutoff`

 Let `S` be admissible and `T` stable. Let `X` be the set of `γ ∈ T` with h_c⁻¹ γ h_c' integral
of reduction `s` (`termsOver`). Let `φ γ y ∈ [0, ∞]` be measurable in `y` with sum `1` on each orbit
`(u γ u'⁻¹, u y)`, `γ ∈ X`, of `classUnipotent c × classUnipotent c'`; the first factor is the group
of rational `u` in `besselU` with h_c⁻¹ u h_c in the principal congruence subgroup of level `S.M`.
Then (a) the integrals `∫ φ γ y • besselKernel side γ y dy`, `γ ∈ X`, sum to the block; (b) each
integrand is integrable; (c) `∑_γ ∫ φ ‖kernel - cut kernel‖` is at most `ν b ^ (-k³ f) / 2`. Here
`ν = S.unipotentCovolume`, `b` is the size parameter of `S`, `k + 1` is the size of the middle block
of the basis (`k = 𝔰.k`) and `f` is the number of infinite places. 

### `amplitudeSum_mul_mul_inv`

 Moving a block. Let `S` be admissible and `T` stable. Let `σ` over `(c, t, c₁)` and `σ'` over
`(c', t', c₁')` be rational elements (`(S.ratMiddle E).G` is the group `S.G E`) of the Bessel
subgroup `besselS`. Suppose that `γ ∈ T ↔ σ γ σ'⁻¹ ∈ T`. If a continuous linear map `L` takes the
kernel at `(γ, y)` to the kernel at `(σ γ σ'⁻¹, σ y)`, then `L` takes the block over `(c₁, s, c₁')`
to that over `(c, t s t'⁻¹, c')`. 

### `amplitudeSum_besselU_mul`

 Let `S` be admissible and `T` stable (`IsStable`), and let `side` choose the full or the cut
Bessel function. Let `u`, `u'` in `besselU` be integral finite adelic elements
(`latticeStabilizer`), with reductions `ū`, `ū'` modulo the chosen places (`S.reduction`). Then the
block at `ū s ū'⁻¹` is `ψ(u)⁻¹ ψ(u')` times the block at `s`. Here `ψ = S.unipotentChar` is the
additive character `S.selfDualChar` at the sum of the entries just above the diagonal on the frame
(`simpleRootSum`), divided by the level `S.M`. 

### `amplitudeSum_eq_zero_of_not_agrees`

 Let `S` be admissible. If `T` is stable (`S.IsStable T`) and `s` does not agree, that is
`unipotentChar u ≠ unipotentChar u'` for some integral unipotent `u`, `u'` whose reductions satisfy
`ū s = s ū'`, then the amplitude sum `S.amplitudeSum side T c s c'` of the elements of `T` over
`(c, s, c')` vanishes. 

 ### The identity block 

### `amplitudeSum_besselS_one_eq_ite`

 Let `E` contain a primitive 5040th root of unity and let `S` be admissible. Let `c`, `c'` be
classes, and let `i`, `j` be tuples of one coordinate index of the Bessel function at each infinite
place (`BesselCoord`). Sum, over the rational points `γ` of the Bessel subgroup `besselS` with h_c⁻¹
γ h_c' integral of reduction `1` (`termsOver`), the integrals
`∫ β_c(y) β_c'(γ⁻¹ y) W(y) ⊗ W(γ⁻¹ y)^* dy`, with `W` the full Bessel function and
`β_c = S.classCutoff c`. The `(i, j)` entry of this sum (`amplitudeSum`) is `S.unipotentCovolume`,
the covolume of `S.classUnipotent c` in the real unipotent group, if `c = c'` and `i = j`, and `0`
otherwise. 
