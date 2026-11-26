---
{
  "module": "src/New/Reduction/ShortAndEnough.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/ShortAndEnough.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/ShortAndEnough.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Theorem A (short forms) and Theorem B (enough forms)

The source is the space `ramifiedSourceForms` of ramified source forms. It lies in the space
`SourceForm` of all source forms, whose dimension is written `D_X`. The target is the space
`targetForms`, whose dimension `D.targetDim` is written `d_T`. We define the translates `s 𝔭` of the
map `𝔭` from the source to the target and prove Theorems A and B: the source is spanned by integral
forms `φ` whose images `s 𝔭 φ` have short lifts `Θ₁ s 𝔭 φ`, these images have small index, and the
images of few translates span almost all of the target.

Notions from other files:
* `D.poincare` is the Poincaré map `𝒫` from source forms to the forms on `Y₀`, without the factor
  `poincareScale`, which the number `c_ss` (`D.seesawConst`, entering as its inverse in
  `D.scaledInclusion`) absorbs. `D.chosenGL` is the finite group `Ḡ` acting on the forms on `Y₀`,
  with the central projection `e₀` to the good part.
* `D.Θ ϑ` is the chain of lifts `Θ_ϑ` of target forms for the twist `ϑ`.
* `D.targetLattice` records which target forms are integral at each `ι`, and its `IndexLe y δ` says
  that at every `ι ∣ l` the family `y` becomes integral with loss `δ_l`, where `∑ δ_l log l ≤ δ`.
* `D.gain l` is the divisibility asked of the chain at `l`; `D.errorUnit` is `f a log³ b`, with
  `D.logB` standing for `log b`.


 ### The errors in the divisibility of the composite lift 

### `divisibilityError`

 A choice of the numbers `err_l` in the theorem on the divisibility of the composite lift,
`New.Data.exists_err_gaugeLe_compositeLift`. 

### `divisibilityError_eq_zero`

 The error `err_l` is zero if `l ≠ N` and either `l` splits in `K` (that is, the value at `l` of
the character `chiK P.d` of the imaginary quadratic field `K = ℚ(√-d)` is `1`) or `l` is at least
the cut-off `x₁`. 

### `sum_divisibilityError_mul_log_le`

 For every finite set `U` of natural numbers, the sum over `l ∈ U` of `err_l log l`, with
`err_l = D.divisibilityError l`, is at most the unit of loss `D.errorUnit = f a log³ b`. 

### `exists_colengthDvd_gaugeLe_divisibilityError`

 Fix a prime `l` and an `l`-adic place of `ℂ`, with valuation ring `𝒪 = embValRing`. Let
`gain_l = D.gain l` be the divisibility asked of the chain of lifts at `l`, and
`err_l = D.divisibilityError l` the error allowed in it. There are `j ≤ err_l · dim_ℂ D.SourceForm`
and an `𝒪`-module `S` of source forms with two properties.
* Every finite family of integral ramified source forms is carried into `S` by a square matrix over
  `𝒪` whose determinant divides `l ^ j` (`ColengthDvd`).
* For `φ ∈ S`, the form `B_ϑ φ = compositeLift ϑ Ψ φ` has valuation at least `gain_l - err_l`: the
  `l`-adic gauge at `g` of its value at each finite adelic point `g` is at most
  `l ^ (err_l - gain_l)`.

Here `ϑ` runs over the twists whose level `ϑ.normQ` is prime to `l`, and `Ψ` over their chain data
(`IsChainDatum`), which are finitely supported coefficient functions on `D.Translations`, the tuples
of translations that define a chain of lifts. 

 ### The map from source forms to target forms 

### `gainExponent`

 The integer `g_l = ⌊gain_l - err_l⌋`. For a prime `l` it vanishes unless `l` is non-split and
below `x₁` or `l = N`. 

### `invGainFactor`

 The positive rational number `c_B = ∏ l ^ (-g_l)`, the product taken over the non-split primes
below `x₁` and the level `N`. 

### `prime_of_mem_smallNonsplitPrimes_union`

 Every `l` in `D.smallNonsplitPrimes ∪ {D.N}`, the set of primes indexing the product
`c_B = D.invGainFactor`, is prime. The non-split primes below `x₁` are prime by definition, and the
level `N` is prime. 

### `sum_log_smallNonsplitPrimes_union_le`

 The sum of `log l` over the non-split primes `l` below `x₁` and `l = N` is at most the
weight `b = D.b`, which is `exp D.logB`. It bounds the loss from rounding the exponents `g_l` down
to integers. 

### `log_invGainFactor_le`

 The number `c_B = D.invGainFactor` satisfies `log c_B ≤ -∑ gain_l log l + f a log³ b + b`, the
sum taken over the non-split primes `l` below the cut-off `x₁ = D.x₁`. 

### `norm_invGainFactor`

 For a prime `l`, the absolute value in `ℂ_l` of `c_B = D.invGainFactor` is that of
`l ^ (-g_l)`. 

### `seesawConst`

 A non-zero constant `c_ss` for which the seesaw identity `New.Data.seesaw_identity` holds with
the linear form `D.besselForm` and the archimedean point `D.besselPoint`. 

### `scaledInclusion`

 The inclusion of the ramified source forms, times the number `c_ss⁻¹` of the seesaw
identity. 

### `projectedPoincare`

 The map `φ ↦ y = #Ḡ · e₀ s z`, with `z = c_ss⁻¹ 𝒫 φ`, from the source to the target. Here
`𝒫` is the Poincaré map, `Ḡ` the finite group `D.chosenGL` and `e₀` the projection to the good
part. 

### `normalizedPoincare`

 The map `φ ↦ c_B y`, with `y = #Ḡ · e₀ s c_ss⁻¹ 𝒫 φ`. It is the translate `s 𝔭` of
`𝔭 = c_B c_ss⁻¹ #Ḡ · e₀ 𝒫` (`coe_normalizedPoincare`). 

### `coe_normalizedPoincare`

 The map `normalizedPoincare s = c_B c_ss⁻¹ #Ḡ · e₀ s 𝒫` is the translate by `s` of
`𝔭 = normalizedPoincare 1`, in the representation `D.principalRep` of the finite group
`Ḡ = D.chosenGL` on the forms on `Y₀`. 

### `integralRamified`

 The ramified source forms that are integral at every `ι`, where `ι` runs over the pairs of a
prime `l` and an `l`-adic place of `ℂ` (`PrimePadicIso`). 

### `exists_lowerChain_poincare_eq`

 The seesaw identity for `z = c_ss⁻¹ 𝒫 φ = D.poincare (D.scaledInclusion φ)`. Each twist `ϑ` has
a chain datum `Ψ` (the data of the upper chain of lifts `B_ϑ = compositeLift ϑ Ψ`) with
`ι_ϑ z = B_ϑ φ` for all ramified `φ`. Here `ι_ϑ = D.lowerChain ϑ.toTameChar` is the lower chain of
lifts, from forms on `Y₀` to forms on `Y_m`, taken for the tame character `ϑ.toTameChar` underlying
the twist. 

### `normSqAt_normalizedPoincare`

 The map `D.normalizedPoincare s` is `c_B = D.invGainFactor` times `D.projectedPoincare s`, the
map `#Ḡ · e₀ s c_ss⁻¹ 𝒫` from ramified source forms to target forms. The positive rational factor
`c_B` multiplies the squared norm `‖Θ₁ ·‖_σ²` by `exp (2 log c_B)`, for every automorphism `σ` of
`ℂ`. 

 ### Theorem A 

### `span_short_integralRamified_eq_top`

 **Theorem A (a).** The source is spanned by the forms `φ` that are integral at every prime `l`
and `l`-adic place of `ℂ` and satisfy `‖Θ₁ s 𝔭 φ‖_σ² ≤ exp (main - m rem + f a log⁴ b)` for all `s`
in the finite group `D.chosenGL` and all automorphisms `σ` of `ℂ`. Here
`s 𝔭 = D.normalizedPoincare s` maps the source to the target, `Θ₁ = D.Θ 1` is the chain of `m = D.m`
lifts for the trivial twist, and `‖·‖_σ²` is the squared norm of the conjugate form. In the bound:
* `main = D.mainAmount` is `m k ∑_τ (s_∞(κ(τ)) - s_fin(κ(τ), τ))`, summed over all infinite places
  `τ`, where `k = D.k` is the rank of the source, `κ` the weight, `s_∞ = D.jetSize` the size of a
  derivative of given order and `s_fin = D.primeSum` the prime sum for its divisibility;
* `rem = D.totalRemainder` is `∑ (s_fin(a, τ) - s_main)`, summed over the `a`-places `τ`, with the
  main part `s_main = D.mainPrimeSum`;
* `f = D.f` is the number of infinite places, `a = D.a` is the long order `x b`, and
  `log b = D.logB` is the logarithm of the weight `b`. 

### `finrank_sourceForm_le_two_mul`

 The ramified source forms `D.ramifiedSourceForms` have at least half the dimension over `ℂ` of
all source forms `D.SourceForm`: `finrank ℂ D.SourceForm ≤ 2 * finrank ℂ D.ramifiedSourceForms`. 

### `normalizedPoincare_mem_integralVectors`

 Let `l = ι.1` be the prime below `ι`, let `gain_l = D.gain l` be the divisibility asked of the
chain of lifts at `l` and `err_l = D.divisibilityError l` the error allowed in it. Suppose that
`B_ϑ φ = compositeLift ϑ Ψ φ` has valuation at least `gain_l - err_l` at `ι`, for every twist `ϑ`
whose level `ϑ.normQ` is prime to `l` and every chain datum `Ψ` of `ϑ`. Then the target form
`y = s 𝔭 φ = D.normalizedPoincare s φ` is integral at `ι`: its lift `Θ_ϑ y` is integral at `ι` for
every `m`-fold twist `ϑ` of level prime to `l`. 

### `indexLe_of_mem_image_normalizedPoincare`

 Fix `s` in the finite group `D.chosenGL`. A finite family `y` of target forms
`s 𝔭 φ = D.normalizedPoincare s φ`, with each `φ` a ramified source form integral at every `ι`, has
logarithmic index at most `δ = dim src · 2 · D.errorUnit` in `D.targetLattice`. Here `src` is the
space `D.ramifiedSourceForms`, and `D.errorUnit` is the unit of loss `D.f * D.a * D.logB ^ 3`. 

### `indexLe_normalizedPoincare`

 **Theorem A (b).** A finite family `y` of target forms `s 𝔭 φ = D.normalizedPoincare s φ`, with
`s` in a set `t` of translates and `φ` in the source `src = D.ramifiedSourceForms` integral at every
`ι`, has logarithmic index at most `δ = #t · dim src · 2 f a log³ b` in the target lattice. 

 ### Theorem B 

### `range_normalizedPoincare`

 The range of `D.normalizedPoincare s` (the map `s 𝔭`) is the image of the ramified source forms
`D.ramifiedSourceForms` under `D.goodPoincare s = #Ḡ · e₀ s 𝒫`, as the scalars `c_B` and `c_ss⁻¹` in
`𝔭` do not vanish. 

### `five_halves_mul_one_add_log_le`

 The factor `(5/2) (1 + log (1 / (16 ε)))` in the number of translates is at most
`5 log (1 + 2 b²)` for `ε = b⁻² / 8`. 

### `exists_le_finrank_iSup_range_normalizedPoincare`

 There is a set `t` of elements of the finite group `D.chosenGL = ∏ GL_r(𝔽_w)` (product over the
chosen places `w` above the two level primes) with `#t · dim src ≤ 5 d_T log (1 + 2 b²)` such that
the spaces `s 𝔭 src`, `s ∈ t`, span at least `(1 - 4 / b²) d_T` dimensions. Here
`d_T = D.targetDim` is the dimension of the target, `b = D.b = exp D.logB` is the weight at the
`b`-places, `src` is the space of ramified source forms and `s 𝔭` is `D.normalizedPoincare s`. 

### `enough_forms`

 **Theorem B**, the bound on the dimension spanned by few translates. The target has dimension
`d_T = D.targetDim ≥ 1`, and there is a set `t` of elements of the finite group `D.chosenGL` with
`#t · dim src ≤ 5 d_T log (1 + 2 b²)` such that the spaces `s 𝔭 src`, `s ∈ t`, span at least
`(1 - 4 / b²) d_T` dimensions. Here `b = D.b = exp D.logB` is the weight at the `b`-places, `src`
is the space of ramified source forms and `s 𝔭` is `D.normalizedPoincare s`. 
