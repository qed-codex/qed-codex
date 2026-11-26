---
{
  "module": "src/Lib/Weil/Periods/Unfolding.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Periods/Unfolding.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Periods/Unfolding.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# One step of the seesaw unfolding of the theta integral over the Bessel group

This file unfolds the period of an equivariant function `W` (`New.Grading.IsEquivariant`) on the
Bessel group `New.Grading.besselGroup` of `Y` against the theta kernel, where the strings of `Y`
and `Y'` have lengths `s` and `s - 1`. The theta kernel at `(r, h)` is `θ` of the translate
`twistedPairWeil α (r, h) Φ`; it is expanded in constant terms indexed by rational maps `V → V'`
modulo those of degree at least zero (`New.Grading.nonnegMaps`). Over a set of classes that is
stable under the rational points of the Bessel group and in which no chosen representative survives
(`New.Grading.Survives`), the sum of the terms integrates to zero. Hence only the translates of
`𝒞 = New.Grading.agreeingClasses` by the rational points of `U(V')` contribute. This writes the
period as a sum of values of `New.Grading.unfoldStep`, and its integral against a rapidly decreasing
automorphic `y` as an integral of `New.Grading.unfoldStep` times `y`.

## Main definitions and results

* `New.Grading.hasSum_unfoldStep`: for `W` equivariant, the period of `W` against the theta kernel
  at `h` is the sum of the values of `New.Grading.unfoldStep` at `γ h` over the rational points `γ`
  of `U(V')`, modulo those of `Y'.besselGroup` on the left.
* `New.Grading.integral_besselGroup_unfold`: the period of `W` against the theta integral of a
  rapidly decreasing automorphic `y` unfolds to the integral of `New.Grading.unfoldStep` times `y`
  modulo the rational points of `Y'.besselGroup`.

Notions from other files:
* `New.𝒮`: The Banach space 𝒮(V) of integrable functions c on 𝔸^n with c(x) = ∫ c(y)β(y,x)e(x−y) dy,
  under the L¹ norm; β is the adelic bicharacter and e the vacuum function `New.vacuumFn`.
* `New.Grading.ratBessel`: The rational points of U(V) that lie in the Bessel (Fourier–Jacobi)
  subgroup of the grading Y.
* `New.Grading.constTerm`: the constant term of `f` at `w` along the maps of positive degree.
* `New.Grading.unfoldStep`: the function `h ↦ ∫ W(r) * Y.constTermAtStringMap Y' α f r h dr` on
  U(V′)(𝔸), integrated over the Bessel group of `Y` modulo its rational points.
* `New.Grading.agreeingClasses`: the set `𝒞` of classes whose chosen representative agrees with
  `T = Y.stringMap Y'` (`New.Grading.AgreesWithStringMap`).

## Relation to the literature

Transfer of Bessel and Fourier–Jacobi periods under a theta lift (one unfolding step).
Here the setting is unitary pairs and hook orbits with a definite complement, and the Bessel and
Fourier–Jacobi cases are treated together. The period is taken against any continuous automorphic
function with the generic unipotent character, for a rapidly decreasing form, and the unfolded
integral converges absolutely. Source: B. Wang Peng Jun, Global theta lifting and automorphic
periods associated to nilpotent orbits, J. Number Theory 271 (2025) 122–149, Prop. 3.2 and Thm. 4.5;
for the local case, R. Gomez, C.-B. Zhu, GAFA 24 (2014) 796–853; for unitary hooks, M. Furusawa, K.
Morimoto, Math. Ann. 391 (2025) §3.


### `New.exists_equiv_quotient_prod_block`

 Suppose that for every `y` in `C`, the point `γ • y` lies in `C` exactly when `γ` lies in `S`,
and let `D` be the union of the translates of `C`. Then `(q, y) ↦ q.out • y` is a bijection from the
pairs of a left coset of `S` and a point of `C` onto `D`. 

### `ratSubst`

 For a pair `p = (γ, δ)` of rational points, the substitution `w ↦ δ w γ⁻¹` on rational maps
`V → V'`, with `γ` and `δ` in rational coordinates. 

### `nonnegMaps_le_comap_ratSubst`

 The substitution `w ↦ δ w γ⁻¹` keeps the maps of degree `≥ 0`. 

### `noncomputable instance : MulAction (Y.ratBessel × V'.ratParabolic d) (ratMatrices E ι' ι ⧸ Y.nonnegMaps d)`

 A pair `(γ, δ)` acts on the classes of rational maps by `w ↦ δ w γ⁻¹`. 

### `mk_out_smul`

 The chosen representative of `(γ, δ) • w` lies in the class of `δ w γ⁻¹`, formed with the
chosen representative of `w`. 

### `agreesWithStringMap_out_smul`

 If `d ≤ Y'.gradeOf ⊔ 0`, the class `(γ, δ) • w` agrees with `T = Y.stringMap Y'` exactly if
`δ w γ⁻¹` does. 

### `classTerm`

 The term of the class `w`: the value `W r` times the constant term, at the chosen
representative of `w`, of the twisted Weil translate of `Φ` by `(r, h)`. For weights `d` odd under
`Y'.stringReversal` any representative gives the same value (`constTerm_out`). 

### `continuous_classTerm`

 For `W` equivariant and `d` odd, the term of a class is jointly continuous in `(h, r)`. 

### `classTerm_smul`

 For `W` equivariant and `d` odd, rational pairs permute the terms: the term of `(γ, δ) • w` at
`(δ h, γ r)` is the term of `w` at `(h, r)`. 

### `exists_tsum_enorm_classTerm_le`

 Let `W` on the Bessel group of `Y` be equivariant (`New.Grading.IsEquivariant`) and let the
weights `d` be odd under `Y'.stringReversal`. The sum of the norms of the terms
`classTerm α Φ W w h r` over any set `S` of classes of rational maps is at most a constant times the
operator norm of the Weil action of `(1, δ h)`, for every `δ` in `V'.ratParabolic d` (the rational
points that do not lower `d`), uniformly in `r`. 

### `lintegral_tsum_enorm_classTerm_lt_top`

 For `W` equivariant and `d` odd, the sum of the norms of the terms has finite integral for
`Y.besselMeasure`. 

### `hasSum_integral_classTerm`

 For `W` equivariant and `d` odd, the terms can be integrated one by one: their integrals add up
to the integral of the sum. 

### `exists_classTerm_mul_eq_of_not_survives`

 Let `W` be equivariant and `d` odd. If the chosen representative of `w` does not survive
(`New.Grading.Survives`), left translation by some `u` multiplies the term of `w` by a constant
`c ≠ 1` of modulus one. 

### `integral_tsum_classTerm_eq_zero`

 Let `W` on `Y.besselGroup` be equivariant (`New.Grading.IsEquivariant`) and let `d` be odd under
`Y'.stringReversal`. Let `S` be a set of classes of rational matrices modulo `Y.nonnegMaps d` that
is stable under `Y.ratBessel` and such that no chosen representative survives
(`New.Grading.Survives`). Then for every `h`, the sum over `S` of the terms `classTerm α Φ W w h`
(`W r` times a constant term of the Weil translate of `Φ`) has integral `0` for
`Y.besselMeasure`. 

### `tsum_integral_eq_of_not_survives`

 Let `W` be equivariant and `d` odd. Let `A ⊆ B` be sets of classes such that `B \ A` is stable
under `Y.ratBessel` and no chosen representative of a class in `B \ A` survives
(`New.Grading.Survives`). Then `B \ A` may be dropped: the sum over `A` of the integrals of the
terms is the integral of the sum over `B`. 

### `agreeingTranslates`

 For the weights `d = 0`, the union of the translates of `𝒞` by the rational points of `U(V')`:
the classes that some rational `δ` moves into `𝒞`. 

### `smul_mem_agreeingClasses_iff`

 For `d ≤ Y'.gradeOf ⊔ 0`, a pair `p = (γ, δ)` keeps a class of `𝒞 = Y.agreeingClasses Y' d`
in `𝒞` exactly if `δ` lies in the Bessel group of `Y'`. 

### `tsum_classTerm`

 For the weights `d = 0`, the terms of all classes add up to `W r` times the theta kernel. 

### `tsum_agreeingTranslates`

 Take the weights `d = 0` and `W` equivariant. Only the classes in `Y.agreeingTranslates Y'`, the
rational translates of the classes that agree with `T = Y.stringMap Y'`, contribute: the integrals
of their terms `classTerm α Φ W w h` add up to the period of `W` against the theta kernel. 

### `tsum_integral_classTerm_agreeingClasses`

 For `W` equivariant, the integrals of the terms of `𝒞` add up to `Y.unfoldStep Y' α Φ W h`:
expanded again for the weights `Y'.gradeOf`, only the class of `T` survives. 

### `exists_equiv_agreeingTranslates`

 Let `W` be equivariant and `𝒞 = Y.agreeingClasses Y' 0`. The union of the translates of `𝒞` is
in bijection with the pairs of a left coset `q` of `Y'.ratBessel` in `V'.Γ` and a class `w` of `𝒞`,
such that the term of `(q, w)` at `h` is the term of `w` at `γ⁻¹ h`, where `γ` is the chosen
representative of `q`. 

### `hasSum_unfoldStep`

 For `W` equivariant and every `h`, the period of `W` against the theta kernel at `h` is the sum
of the values of the unfolded function `Y.unfoldStep Y' α Φ W` at `γ h`, over `γ` in
`Y'.ratBessel \ V'.Γ`. Here `γ` is the inverse of the chosen representative of a left coset `q`. 

### `exists_tsum_enorm_classTerm_mul_le`

 For the weights `d = 0`, an equivariant `W` and a rapidly decreasing `y`, the sums of the norms
of the terms times `y h` are bounded, uniformly in `h`, `r` and the set of classes. 

### `exists_tsum_enorm_unfoldStep_mul_le`

 For an equivariant `W` and a rapidly decreasing `y`, the sum over `γ` in `Y'.ratBessel \ V'.Γ`
of the norms of `Y.unfoldStep Y' α Φ W (γ h) * y h` is at most a constant, independent of `h`, times
the (finite) total mass of `Y.besselMeasure`. 

### `integral_besselGroup_unfold`

 Let `W` be a `ψ_U`-equivariant function on the Bessel group of `Y`, and let `y` be an
automorphic function of rapid decay on `U(V')(𝔸)`. Write `Y.unfoldStep Y' α Φ W h` for the integral
of `W r * Y.constTermAtStringMap Y' α Φ r h` over the Bessel group of `Y` modulo its rational
points. Then `h ↦ Y.unfoldStep Y' α Φ W h * y h` is integrable over `Y'.ratBessel \ U(V')(𝔸)`, and
its integral there equals `∫ W(r) ∫ θ(ω(r, h) Φ) y(h) dh dr`, where `ω = twistedPairWeil α`, `h`
runs over `V'.Γ \ U(V')(𝔸)` and `r` over the Bessel group of `Y` modulo its rational points. 
