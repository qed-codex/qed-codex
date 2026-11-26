---
{
  "module": "src/New/Spanning/MainTerm/GlobalSieve.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/MainTerm/GlobalSieve.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/MainTerm/GlobalSieve.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# One-sided Poisson summation, sums over frequencies, and the sieve over all places

The sieve over the infinite places of the CM field `E` and a finite set `T` of finite places, which
bounds the main term.

* `New.Filling.charOnPlaces`, `New.Filling.globalChar`: the character of the product of the
  completions at `T`, and its product with the characters at the infinite places.
* `New.Filling.sum_ratPoint_le_mul_add_integral_of_fourier_le`: one-sided Poisson summation over the
  infinite places and `T`, at rational points integral off `T`.
* `New.Filling.entryDensity`, `New.Filling.densitySum`: the sum of densities at a common next entry,
  and the sums of densities in which the first `i` entries are summed over `A`.
* `New.Filling.densitySum_succ_le_mul_densitySum_add`: each sum of densities is bounded by the one
  before plus an error, up to the constant of Poisson summation (`New.Filling.poissonConst`).
* `New.Filling.densitySum_le`: the bound after all entries are removed in turn.
* `New.Filling.sieve`: the sieve for the product of one system for each infinite place and one
  system at `T`, read at rational points (`New.Filling.ratPoint`).

Conventions: `𝔰.k` and `𝔰.n = 𝔰.ϱ + 1` are parameters of the shape `𝔰`; in
`New.Filling.frequency_term_le` and `New.Filling.sum_frequencies_le`, `k` is any natural number.
`Φ v` is the chosen embedding of `E` at the infinite place `v`.

Notions from other files:
* `New.Filling`: the data `S`, among them the size parameter `b = S.b`, the level `M = S.M`, the
  prime `N = S.N` and a generator `ϖ = S.deltaE` of the different of `E`.
* `New.Filling.IsAdmissible`: the standing hypotheses on `S`, among them `1 ≤ |S.realM v| ≤ b ^ 23`
  and `N ≤ b ^ (60 n)`.
* `New.ψf E`, written `ψ_f`: the character of the finite adeles with `ψ_f(x) = exp (2πi Tr a)` for
  any `a ∈ E` with `x - a` integral. `New.stdAddChar E` is the standard character of the adeles, and
  `New.Filling.selfDualChar` is `x ↦ ψ_f(-x / ϖ)`.
* `New.LocProd T`: the product of the completions at `T`, with integers `New.SemilocalField.O`;
  `New.evalPlaces T` and `New.ratToPlaces T` map the finite adeles and `E` to it.
* `New.integralOff T`, `New.Filling.ratIntegralOff T`: the finite adeles and the elements of `E`
  (the `T`-integers) that are integral at every finite place outside `T`.
* `New.genIndex a`, `New.denomIndex O a`: the generalised index `[O : a O]` and the denominator
  `[O : O ∩ a⁻¹ O]`.
* `New.SieveSystem`: the axioms of the sieve for a family of forms `J i` on pairs of heads, at a
  place or a product of places.

## Relation to the literature

A system of positive kernels, of one kind at archimedean and finite places, has each kernel the
integral of the next over a common last entry. Systems multiply over places, and one-sided Poisson
summation, entry by entry, bounds the sum over rational points by the mass times a factor near 1, up
to the constants of summation and a small error, as the main term of the second moment requires.
Inductive Fourier transforms of Kloosterman integrals and spectral large sieves losing a constant or
X^ε are known in the literature. Related work: Jacquet, Smooth transfer of Kloosterman integrals,
2003; Jacquet, Kloosterman identities over a quadratic extension, 2004; Blomer–Buttcane, Global
decomposition of GL(3) Kloosterman sums and the spectral large sieve, 2015; Deshouillers–Iwaniec,
Kloosterman sums and Fourier coefficients of cusp forms, 1982.


### `selfDualChar_apply`

 The character `S.selfDualChar` is `x ↦ ψ_f(-x / ϖ)`, where `ψ_f = ψf E` is the standard
character of the finite adeles and `ϖ = S.deltaE` generates the different of `E`. 

### `charOnPlaces`

 The character `S.selfDualChar` of the finite adeles, `x ↦ ψ_f(-x / ϖ)`, read on the product of
the completions at `T` through extension by zero (`adeleOfLocal`). Here `ψ_f = ψf E` is the standard
character of the finite adeles, and `ϖ = S.deltaE` generates the different of `E`. 

### `charOnPlaces_evalPlaces`

 At a finite adele that is integral off `T`, the character `S.selfDualChar` depends only on the
components at `T`: it equals `S.charOnPlaces T` there. 

### `globalChar`

 The character of the product of the infinite places and the completions at `T`: the product of
the characters `wave c = exp (c - conj c)` at the infinite places and of `S.charOnPlaces T`. 

### `frequencyDecay`

 The decay factor at the places of `T` for a transform at the frequency `ξ`: the number
`[O : ξ O] ^ ((k - n⁷) / 2) / [O : O ∩ ξ⁻¹ O] ^ 3 * b ^ (n⁹ f)`, with `f` the number of infinite
places of `E`. 

### `ratPoint`

 The number `t`, read at the infinite places with the scales `l v` and at `T`: the point with
components `l v * Φ v t` and the image of `t` in the product of the completions at `T`. 

### `absNorm_denominator_le`

 For `y` integral off `T`, the norm of the denominator ideal `{a ∈ 𝓞 E | a y ∈ 𝓞 E}` is at most
the index `[O : O ∩ y⁻¹ O]`, where `O` is the ring of integers of the completions at `T`. 

### `frequency_term_le`

 Let `y ≠ 0` be integral off `T`, and let `‖c v‖⁻¹ ≤ |x v| ≤ B` with `1 ≤ B`. Take the product of
the decay factors of `y` at the infinite places (`dampedPower k r = r ^ k * min 1 r ^ 6` at
`r = ‖c v * Φ v y‖⁻¹`, `Φ v` the embedding at `v`) and at `T`. It is at most
`∏ v, |x v| ^ k * B ^ 6` times the inverse cube of the height of `y`, whose finite part is the norm
of the denominator ideal. 

### `sum_frequencies_le`

 Let `X` be a finite set of nonzero elements of `E` that are integral off `T`, and let
`‖c v‖⁻¹ ≤ |x v| ≤ B` with `1 ≤ B`. The sum over `y ∈ X` of the product of the decay factors at the
infinite places and at `T` is at most `∏ v, (|x v| ^ k * (b B²)³)`. 

### `measurePreserving_scale_evalPlaces`

 Scaling by `r > 0` at the infinite places and projecting to `T` maps the measure on the adeles
that are integral off `T` to `volÔ E / ∏ v, r v ^ 2` times the product measure, where `volÔ E` is
the volume of the integral finite adeles. 

### `coe_stdAddChar_apply`

 The standard character of the adeles at `x` is `exp (-2πi ∑ v, 2 Re x_v)`, with `x_v = x.1 v`
the components at the infinite places, times the standard character `ψf E` of the finite adeles at
the finite part `x.2`. 

### `wave_two_pi_I_mul`

 The character `wave c = exp (c - conj c)` at `c = 2πi w` is `exp (2πi * 2 Re w)`. 

### `stdAddChar_div_deltaE`

 Let `ϖ = S.deltaE` be the generator of the different of `E` in the filling data `S`. For `y ∈ E`
and an adele `z`, both integral off `T`, the standard adelic character at `-y z / ϖ` is the product
of the characters `wave c = exp (c - conj c)` at the infinite places and of `S.charOnPlaces T`, the
character `x ↦ ψ_f(-x / ϖ)` on the product of the completions at `T`. 

### `mem_ratIntegralOff_of_transform_ne_zero`

 Let `G` be a function on the adeles that is invariant under the integral finite adeles that
vanish at `T`, written `a - adeleOfLocal T (evalPlaces T a)` (`a ∈ Ô E` integral, with its
components at `T` removed). If the Fourier transform of `G` at `y / ϖ` is not zero, then `y` is
integral off `T`. 

### `extendToAdeles`

 The function on the adeles that reads `F` after scaling by `r` at the infinite places and
projecting to `T`, on the adeles that are integral off `T`, and is zero elsewhere. 

### `extendToAdeles_toAdele`

 At the diagonal image `toAdele y` of a number `y` that is integral off `T`, the extension of `F`
is the value of `F` at the point with components `r v * Φ v y` and the image of `y` at `T`. 

### `extendToAdeles_sub_adeleOfLocal_add`

 Let `F` be a real function on the product of the infinite places and the completions at `T`, and
let `r v` be real scales. The extension `extendToAdeles T r F` reads `F` after scaling by `r` at
infinity and projecting to `T`, and is zero at adeles that are not integral off `T`. It is invariant
under the integral finite adeles that vanish at `T`, written `a - adeleOfLocal T (evalPlaces T a)`
with `a ∈ Ô E` integral. 

### `integrable_extendToAdeles`

 For positive scales `r`, the extension of an integrable function to the adeles is integrable. 

### `lowerSemicontinuousAt_extendToAdeles`

 Let `F` be a real function on the product of the infinite places and the completions at `T`, let
`r v` be real scales, and let `y ∈ E` be integral off `T`. Suppose `F` is lower semicontinuous at
the point (`ratPoint`) with components `r v * Φ v y` and the image of `y` at `T`. Then the extension
of `F` to the adeles is lower semicontinuous at the diagonal image `toAdele y`. 

### `integral_stdAddChar_mul_extendToAdeles`

 Let `T` be a finite set of finite places of `E`, let `r > 0`, let `F` be integrable and let `y`
be integral off `T`. Extend `F` to the adeles. The Fourier transform of the extension at `y / ϖ`,
with `ϖ = S.deltaE` the generator of the different, is `volÔ E / ∏ v, r v ^ 2` times the transform
of `F` at the point `ξ` given by `y` and the scales `2πi / (Φ v ϖ * r v)`. 

### `sum_ratPoint_le_mul_add_integral_of_fourier_le`

 One-sided Poisson summation over the infinite places and a finite set `T` of finite places. Let
the elements of `V` be integral off `T`, read as points (`ratPoint`) scaled by `r > 0` at infinity.
Let `F ≥ 0` be integrable and lower semicontinuous at these points. Let its Fourier transform at
each unit `ξ` have modulus at most `β ξ * M` with `0 ≤ M`. Let `ε` bound the finite sums of `β` over
nonzero `T`-integers, scaled by `2πi / (Φ v ϖ * r v)`. Then the sum of `F` over the points is at
most `volÔ E / ∏ v, r v ^ 2` times `ε * M + ∫ F`, with `volÔ E` the volume of the integral finite
adeles. 

### `GlobalHead`

 A head is a sequence of entries on which the forms of the sieve are evaluated. Here each entry
is a unit at every infinite place together with a unit of the product of the completions at `T`. 

### `unitOrOneAtPlaces`

 A point of the product of the infinite places and `T` as a unit. A component at an infinite
place that is zero is replaced by `1`, and so is the component in `LocProd T` if it is not a
unit. 

### `IsGlobalSieveSystem`

 A sieve system on the product of the infinite places and `T`, for the character
`S.globalChar T`. The density `J i` pairs two heads and, for `i ≤ n`, is the integral of `J (i + 1)`
over a common entry at position `i`. The density at the last entry `J (n + 1)` is continuous, and
positive semidefinite on heads with a common entry at position `n`; the mass `J 0` has modulus at
most `En`. The transform of `J (i + 1)` in the common entry at a unit `ξ` has modulus at most the
decay `β ξ` times the weights `Λ i` of the two heads. For `i < n`, the same bound with weights
`Λ (i + 1)` holds for `J (i + 1)` at two heads with entries `t`, `s` at position `i`, if
`ξ = 1 / t - 1 / s` (divided by the level `M = S.M` at `T`) is a unit. 

### `BoundsDecay`

 `ε` bounds the sums of the decay `β` over nonzero frequencies that are integral off `T`, at all
scales `c v / frameScaleSq v a` with `‖c v‖⁻¹ ≤ |realM v| / M`. These cover the frequencies of
Poisson summation (`c v = 2πi / Φ v ϖ`) and, when `1 ≤ |realM v|`, of two heads with different last
entries (`c v = M`). Here `M` is the level, `realM v` is the real number `M * Φ v ϖ / (2πi)`, and
`frameScaleSq v a = realM v ^ (2 (ϱ - a)) / N` scales the entry `a`. 

### `scaledEntry`

 The number `t` as the entry `a` of a head: scaled at the infinite place `v` by
`S.frameScaleSq v a = κ_v ^ (2 (ϱ - a)) / N`, with `κ_v = S.realM v`, and read at `T`. 

### `scaledHead`

 The head with first entries `p`, next entry `t` and later entries `1`, read in the scaled frame
at the infinite places and at `T`. 

### `poissonConst`

 The constant of Poisson summation in the entry `a`: the volume of the integral finite adeles
divided by the Jacobian of the scaling at the infinite places. 

### `entryDensity`

 The sum of the densities `J (i + 1)` over the pairs of heads of length `i` with entries in `A`,
at the common next entry `x`. 

### `densitySum`

 The sum of densities in which `i` entries are still summed over `A`, the last of them common
to the two heads: the real part of the mass for `i = 0`, and of the sum of `entryDensity (i - 1)`
over `A` for `i > 0`. 

### `entryDensity_scaledEntry`

 At the point `scaledEntry T i t` (the unit `t` as entry `i`, scaled at each infinite place `v`
by `frameScaleSq v i` and read at `T`), the entry density `entryDensity T A J i` is the sum of
`J (i + 1)` over the pairs of heads `scaledHead T p t`, `scaledHead T q t`. These heads have first
entries `p`, `q : Fin i → A`, common next entry `t`, and later entries `1`. 

### `scaledHead_snoc`

 A head whose first entries are `p` followed by `t`, and whose later entries are `1`, is the head
with first entries `p` and next entry `t`. 

### `entryDensity_nonneg`

 For a sieve system of length `n` with densities `J` and `i ≤ n`, the sum of `J (i + 1)` over the
pairs of heads with a common entry at position `i` is a nonnegative real number. 

### `lowerSemicontinuousAt_entryDensity`

 Let `K` be a sieve system of length `n` with densities `J`, let `A` be a finite set of units of
`E`, and let `i ≤ n`. The entry density at `x` (`entryDensity`) is the sum of `J (i + 1)` over the
pairs of heads with first `i` entries in `A` and common entry `x` at position `i`. Its real part is
lower semicontinuous in `x` at each point `scaledEntry T i t`, which is the unit `t` scaled at each
infinite place `v` by `frameScaleSq v i = κ_v ^ (2 (ϱ - i)) / N` and read at `T`. 

### `densitySum_succ_le`

 Poisson summation in the entry `i ≤ n`. Let `S` satisfy the standing hypotheses
(`IsAdmissible`). Let `J` be the densities of a sieve system of length `n` with weights `Λ` and
decay `β`, summed to at most `ε` over nonzero frequencies (`BoundsDecay`), and let the elements of
`A` be integral off `T`. The head `scaledHead T p 1` has first entries `p` and later entries `1`,
with the entry `a` scaled at the infinite place `v` by `frameScaleSq v a = κ_v ^ (2 (ϱ - a)) / N`.
The left side is the real part of the sum of `J (i + 1)` over the pairs of heads of length `i + 1`
with entries in `A` and a common last entry. Up to the constant `poissonConst i = volÔ E / ∏ v,
frameScaleSq v i ^ 2`, with `volÔ E` the volume of the integral finite adeles, the frequency `0`
gives the sum of `J i` over all pairs of heads of length `i`, and the other frequencies give at most
`ε` times the squared sum of the weights of these heads. 

### `re_le_of_last_entries_ne`

 Let `J`, `Λ ≥ 0`, `β` be the densities, weights and decay of a sieve system of length `n`: for
`i < n`, the modulus of `J (i + 1)` at two heads is at most `β ξ` times their weights `Λ (i + 1)` if
the difference `ξ` of the inverses of their entries at position `i` (divided by the level `M = S.M`
at `T`) is a unit. Let `β` sum to at most `ε` over nonzero frequencies (`BoundsDecay`), and let the
inverses of `M` and of the elements of `A` be integral off `T`. At two heads with different entries
`t`, `s` at position `i < n`, the frequency comes from the nonzero `T`-integer
`(1 / t - 1 / s) / M`, so the real part of `J (i + 1)` is at most `ε` times the two weights. 

### `re_sum_sum_le_densitySum_add`

 Let `J`, `Λ ≥ 0`, `β` be the densities, weights and decay of a sieve system of length `n`. Let
`β` sum to at most `ε ≥ 0` over nonzero frequencies (`BoundsDecay`), and let the inverses of the
level `M = S.M` and of the elements of `A` be integral off `T`. For `i ≤ n`, sum the real part of
`J i` over the pairs of heads of length `i` with entries in `A`. The pairs with equal last entries
give `densitySum T A J i`, by definition, and the others give at most `ε` times the squared sum of
the weights. 

### `densitySum_succ_le_mul_densitySum_add`

 Let `J` be the densities of a sieve system with weights `Λ` and decay `β`, summed to at most
`ε`, and let `1 / M` and both `t` and `1 / t` for `t ∈ A` be integral off `T`. Up to the constant of
Poisson summation, each sum of densities is at most the one before plus an error from the nonzero
frequencies and from the pairs of heads with different last entries; each part of the error is at
most `ε` times the squared sum of the weights. 

### `densitySum_le`

 Let `J` be the densities of a sieve system `K` (`IsGlobalSieveSystem`, so `massBound` bounds the
mass `J 0`) with weights `Λ` and decay `β` summed to at most `ε` (`BoundsDecay`), and let `1 / M`
and `t`, `1 / t` for `t ∈ A` be integral off `T`. Let `Γ` bound the squared sums of the weights,
relative to the constants of Poisson summation. Then the `i`-th sum of densities is at most the
product of the first `i` constants times `massBound + 2 i Γ ε`. 

### `frameScaleSq_le_realM_pow`

 Under the standing hypotheses `IsAdmissible`, each scale
`frameScaleSq v a = κ_v ^ (2 (ϱ - a)) / N`, where κ_v is the real number `realM v`, is at most
`|realM v| ^ (2 ϱ) / N`. 

### `prod_abs_realM`

 The product of the absolute values of the numbers `κ_v = M Φ v ϖ / (2πi)` over the infinite
places is `(M rd / (2π)) ^ f`, because `ϖ` generates the different. Here `rd` is the root
discriminant of `E`, and `f` is the number of infinite places. 

### `decayConst`

 The product over the infinite places of the constants in the decay: `scaledVolumeRatio`, a
constant of the shape, times the power `k - n⁷` of `|κ_v| ^ (2 ϱ + 1) / (M N)`, where
`κ_v = S.realM v` is the real number `M * Φ v ϖ / (2πi)`. For admissible `S`, the base of this power
bounds the inverses of the scales of the frequencies in `BoundsDecay`. 

### `boundsDecay_prod`

 Let `κ_v = S.realM v` be the real number `M Φ v ϖ / (2πi)`, with `ϖ` the generator of the
different. Let `S` satisfy the standing hypotheses (`IsAdmissible`), among them
`1 ≤ |κ_v| ≤ b ^ 23`. For a frequency `ξ`, with components `ξ.1 v` at the infinite places `v` and
`ξ.2` in `LocProd T`, the product of the completions at `T`, let the decay at `ξ` be the product
over `v` of `scaledVolumeRatio * b ^ (2000 n⁹) * dampedPower (k - n⁷) ‖ξ.1 v‖⁻¹`, times
`frequencyDecay T ξ.2`. Its sum over any finite set of nonzero `T`-integers, read with the scales
`c v / frameScaleSq v a` for any entry `a` and any `c` with `‖c v‖⁻¹ ≤ |κ_v| / M` (`BoundsDecay`),
is at most `decayConst` times `b ^ (2002 n⁹ f)`, with `f` the number of infinite places. 

### `headProduct`

 The product of the first `j` entries of a head `p` with entries in `A`. 

### `headProduct_injective`

 A head `p : Fin i → A` (a tuple of `i` units from `A`) is determined by the products
`headProduct p (j + 1)` of its first `j + 1` entries, for `j < i`. 

### `prod_max_inv_norm_mul_sqrt_genIndex_le`

 The product formula for the weights. Let `δ ≠ 0` be integral off `T`, and let `r` bound
`‖Φ v δ‖` and `‖c v‖⁻¹` at all infinite places. Then the product of the numbers
`max 1 ‖c v * Φ v δ‖⁻¹` and of the square root of the index `[O : δ O]` at `T` is at most `r ^ f`,
with `f` the number of infinite places. 

### `inv_norm_prod_frameScaleSq_le`

 Let `S` satisfy the standing hypotheses (`IsAdmissible`), among them `1 ≤ |κ_v|` and
`N ≤ b ^ (60 n)` for the prime `N = S.N`, the size parameter `b = S.b` and `n = ϱ + 1`. For `j ≤ ϱ`,
the inverse of the product of the scales `frameScaleSq v a = κ_v ^ (2 (ϱ - a)) / N`, `a < j`, is at
most `b ^ (60 n²)`. 

### `globalWeight`

 The weight of a head `p` of length `i`, read at the infinite places and at `T`: a product over
the partial products `δ = p 0 * ⋯ * p l`, `l < i`. At an infinite place the factor (`headWeight`) is
`max 1 ‖δ‖⁻¹ ^ n⁶` if `‖δ‖ ≤ b ^ (60 n²)` and `0` otherwise. At `T` the factor (`finHeadWeight`) is
`[O : δ O] ^ (n⁶ / 2)` if `δ` lies in `O` and `0` otherwise. 

### `globalWeight_scaledHead`

 Let `S` satisfy the standing hypotheses (`IsAdmissible`), with size parameter `b = S.b` and
`n = ϱ + 1`. The head `scaledHead T p 1` has first entries `p` and later entries `1`. The entry `a`
is scaled at the infinite place `v` by `frameScaleSq v a = κ_v ^ (2 (ϱ - a)) / N`, where
`κ_v = S.realM v` and `N = S.N`. Its weight (`globalWeight`) is a product over the products
`δ = headProduct p (j + 1)` of the first entries of `p`. At an infinite place `v`, let `Φ v` be the
chosen complex embedding inducing `v`, and let `c j v` be the product of the scales of these
entries. There the factor is `max 1 ‖c j v * Φ v δ‖⁻¹ ^ n⁶` if `‖c j v * Φ v δ‖ ≤ b ^ (60 n²)`, and
`0` otherwise. At `T` the factor is `[O : δ O] ^ (n⁶ / 2)` if `ratToPlaces T δ` lies in `O`, and `0`
otherwise. Here `O` is the ring of integers of the product of the completions at `T`. 

### `isIntegral_headProduct_and_norm_le`

 Let `S` satisfy the standing hypotheses (`IsAdmissible`), and let `p` be a head of length
`i ≤ ϱ` with entries in a finite set `A` of numbers integral off `T`. Suppose the weight
(`globalWeight`) of `scaledHead T p 1`, the head with first entries `p` and later entries `1` read
in the scaled frame, is not zero. Then the products of the first entries of `p` are integers of `E`
of modulus at most `b ^ (120 n²)` at all infinite places. 

### `globalWeight_scaledHead_le`

 The largest weight. Let `S` satisfy the standing hypotheses (`IsAdmissible`), and let `p` be a
tuple of length `i ≤ ϱ` with entries integral off `T`. The head `scaledHead T p 1` has first entries
`p` and later entries `1`, with the entry `a` scaled at the infinite place `v` by
`frameScaleSq v a = κ_v ^ (2 (ϱ - a)) / N` (`κ_v = S.realM v`, `N = S.N`). Its weight
(`globalWeight`) is a product over the partial products `δ` of its first `i` entries, of
`max 1 ‖δ‖⁻¹ ^ n⁶` or `0` at each infinite place and of `[O : δ O] ^ (n⁶ / 2)` or `0` at `T`, with
`O` the integers at `T`. This weight is at most `b ^ (120 n⁸ f i)`. Here `b = S.b` is the size
parameter, `n = ϱ + 1`, and `f` is the number of infinite places. 

### `sum_globalWeight_le`

 The sum of the weights of the heads of length `i ≤ ϱ` with entries in a finite set `A` of
numbers integral off `T` is at most `b ^ (130 n⁹ f)`: the number of heads whose products are small
integers, times the largest weight. Here `b = S.b` is the size parameter of the admissible filling
data `S`, `n = ϱ + 1`, and `f` is the number of infinite places. 

### `one_le_pow_mul_prod_poissonConst`

 For `i ≤ ϱ`, the product of the first `i` constants of Poisson summation is at least
`b ^ (-100 n² f)`, with `f` the number of infinite places. 

### `sq_sum_globalWeight_le`

 Let `S` satisfy the standing hypotheses `IsAdmissible`. Let `b = S.b`, `ϱ = 𝔰.ϱ`, `n = ϱ + 1`,
and let `f` be the number of infinite places. Let `A` be a finite set of units of `E` integral off
`T`, and let `i ≤ ϱ`. Sum, over heads `p` of length `i` with entries in `A`, the weight
`globalWeight T i` of the head `scaledHead T p 1`. The square of this sum is at most
`b ^ (400 n⁹ f)` times the product of the first `i` constants `poissonConst a` of Poisson
summation. 

### `sieve`

 The sieve. Let `b = S.b`, `M = S.M` and `N = S.N` be the size parameter, the level and the prime
of the admissible filling data `S`, let `k`, `ϱ`, `n = ϱ + 1` be the parameters of its shape `𝔰`,
and let `f` be the number of infinite places. Let `U ⊆ A`, and let `1 / M` and `t`, `1 / t` for
`t ∈ A` be integral off `T`. Let the forms `J_T i` on pairs of heads (sequences of units) at `T`
satisfy the axioms of the sieve (`SieveSystem`) in length `ϱ`: for `i ≤ ϱ`, `J_T i` is the integral
of `J_T (i + 1)` over a common entry at position `i`, read as a unit (`unitOrOne`); the top form
`J_T n` is continuous, and positive semidefinite on heads with a common entry at position `ϱ`; the
mass `J_T 0` has modulus at most `mass_T`; and the decay `frequencyDecay` times the weights
`finHeadWeight` bounds the transforms for `S.charOnPlaces T` and the forms at heads with entries
`w`, `w'` whose frequency `(1 / w - 1 / w') / M` is a unit. Multiply `J_T` by the forms `bandLimit`
that are part of the Bessel systems `S.besselSystem v` at the infinite places: they satisfy the same
axioms over `ℂ`, with mass at most `(1 + b ^ (-10)) / deg`.

The real part of the sum of the products of the top forms `bandLimit n` and `J_T n` over all pairs
of heads with entries in `A` and a common last entry in `U` is at most the product of the constants
of Poisson summation times the sum of the product of the bounds for the masses and of the error
`b ^ (2403 n⁹ f) * decayConst`. The heads have first entries `p`, then `t`, then `1` (`padTuple`).
At `T` they are `y p t`; at the infinite place `v` they are `x v p t`, with the entry `i` scaled by
`frameScaleSq v i = κ_v ^ (2 (ϱ - i)) / N`, where `κ_v = S.realM v`. The constants are `poissonConst
i = volÔ E / ∏ v, frameScaleSq v i ^ 2`, with `volÔ E` the volume of the integral finite adeles, and
`decayConst = ∏ v, scaledVolumeRatio * (|κ_v| ^ (2 ϱ + 1) / (M N)) ^ (k - n⁷)`. 
