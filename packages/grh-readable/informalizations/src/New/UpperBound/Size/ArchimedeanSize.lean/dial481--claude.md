---
{
  "module": "src/New/UpperBound/Size/ArchimedeanSize.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Size/ArchimedeanSize.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Size/ArchimedeanSize.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Archimedean size of the composite lift, and passage to target forms by the good projection

The composite lift of a chain datum is `New.Data.restrictedChain` of the expansion of its glued
tensor, so its size (`New.Data.weylNormSq_compositeLift_le`) follows from the bound for
`New.Data.restrictedChain`. This map sends source forms (algebraic forms on `X_0`) to forms on
`Y_m`. Separately, a form `z` of principal level on `Y₀` (the side of the target forms) is replaced
by its good part `|𝖦| e₀ s z`. For the lift to `Y_m` (`lowerChainAtLevel`), this replacement keeps
integrality of any scalar multiple `c •` of it, and it enlarges the bound `exp B` on its values to a
bound `exp (x ^ 99 + B)` on the class sum.

## Main definitions and results

* `New.Data.rowSizeSum`, `New.Data.chainSize`: the size of the rows of one lift diagram, and the
  main term of the size of the chain.
* `New.Data.weylNormSq_restrictedChain_le`, `New.Data.weylNormSq_compositeLift_le`: the size bounds
  for the restricted chain and for the composite lift.
* `New.Data.lowerChain_goodProjTranslate_apply`: the lift of `|𝖦| e₀ s z` is a combination of right
  translates of the lift of `z`, with the coefficients of `|𝖦| e₀`.

Notions from other files:
* `New.Data.jetSize`: The size `s_∞(j) = log j! + j log (M / Ω)` of a derivative of order `j`.
* `New.Data.restrictedChain`: For coefficients `Ψ` on translations of the integral vacuum, the
  combination of the chains of `m` lifts of these translates, restricted to `Y_m`. `Ψ` is a weak
  chain datum (`New.Data.IsWeakChainDatum`) if the combined tensor is invariant and the coefficients
  are admissible.
* `New.Data.gain`: The divisibility at a prime `p` that is asked of the chain.
* `New.LevelPlaces.LevelForm.integralForms`: The forms φ whose value φ(g) has gauge `New.weylGauge`
  at most 1 for every g.
* `New.LevelPlaces.LevelForm.normSqAt`: The class sum of the squared Gram norms `New.weylNormSq` of
  the vectors σ(φ(g)).

## Relation to the literature

The untwisted chain of lifts enlarges squared norms of all conjugates by at most an explicit factor,
which gives the size side of the product formula. Related work on algebraic modular forms as values
on lattice classes: Gross, Algebraic modular forms, 1999; Greenberg–Voight, Lattice methods for
algebraic modular forms on classical groups, 2014.



## Archimedean size bound for the composite of theta lifts on source forms

The map `New.Data.restrictedChain` is a combination, with coefficients `Ψ`, of chains of `m` theta
lifts `X_0 → X_1 → … → X_m`, followed by the restriction `New.Data.restrictToY` to `Y_m`. The proof
of `New.Data.weylNormSq_restrictedChain_le` multiplies four bounds: those for the single lifts
(`New.Parameters.sqrt_weylNormSq_schurJet_le_of_isVacuumCombination`), the class numbers, the size
of the coefficients and the bound for the restriction.


 ### The level compensates the excess 

### `jetSize_sub_mainPrimeSum_le`

 The excess of one lift: `s_∞(a) - s_main ≤ a log (κ̄ M rd_E / 2π) + 1 + (log a) / 2`. Here
`a = D.a` is the product `x b` of the integer scales `x` and `b` of the data `D`, `M = D.M` is the
product of the two primes of the principal level, `rd_E` is the root discriminant of the CM field
`E = D.E`, and `log κ̄` is the mean of `log κ(τ)`, with `κ = D.weight`, over the set `D.Φ` of the
`f = D.f` infinite places of `E`. Further `s_∞(a) = D.jetSize a = log a! + a log (M / Ω)`, with the
period `Ω = P.bigOmega D.towerExp`, and `s_main = D.mainPrimeSum = a (log (a / κ̄) + c₁)`, with `c₁`
the real part of `logDerivMean P.d 1 1`. 

### `mul_jetSize_sub_mainPrimeSum_sub_le`

 The level compensates the excess of the `m` lifts:
`m (s_∞(a) - s_main) - a log N ≤ 32 a log b`. Here `m = D.m` is the number of theta lifts in the
chain, `a = D.a` is the product `x b` of the integer scales `x` and `b` of the data `D`,
`log b = D.logB`, and the level `N = D.N` is a prime. Further
`s_∞(a) = D.jetSize a = log a! + a log (M / Ω)`, with `M = D.M` the product of the two primes of the
principal level and `Ω` the period `New.Parameters.bigOmega` of the field `D.E`, and
`s_main = D.mainPrimeSum` is the expected mean of the prime sums `D.primeSum a τ` over the infinite
places `τ ∈ D.aPlaces`. 

### `card_aPlaces_mul_excess_le`

 The level compensates the excess at all `a`-places together:
`#Φ_a (m (s_∞(a) - s_main) - a log N) ≤ 32 f a log b`. Here `Φ_a = D.aPlaces` is a set of infinite
places of `D.E`, `f = D.f` is the number of all infinite places, `s_∞ = D.jetSize` and
`s_main = D.mainPrimeSum`. 

 ### The exponent in the size bound 

### `two_mul_sum_gain_mul_log`

 The gains add up to the prime sums: over the primes `p < x₁` that do not split in
`K = ℚ(√-d)`, with `d = P.d` and the cut-off `x₁ = D.x₁`,
`2 ∑ gain_p log p = m ∑_{τ ∈ Φ_a} s_fin(a, τ) + m k ∑_τ s_fin(κ(τ), τ)`. Here `gain_p = D.gain p` is
the divisibility at `p` asked of the chain of `m = D.m` theta lifts, `k = D.k` is the rank of the
source of the chain, `κ(τ) = D.weight τ` is the weight at the infinite place `τ` of `D.E`, and
`Φ_a = D.aPlaces` is the set of places `≡ 1` modulo `P.q₀`. The prime sum `D.primeSum y τ` is
`s_fin(y, τ) = ∑_{1 ≤ ν ≤ a} Λ(ν) (1 - χ_K(ν)) (y / ν - κ(-ν τ))₊`, with `a = D.a`. 

### `mainAmount_sub_add_two_mul_sum_gain`

 The prime sums cancel in the exponent of the size bound:
`h_main - m rem + 2 ∑ gain_p log p = m #Φ_a s_main + m k ∑_τ s_∞(κ(τ))`. Write `s_∞ = D.jetSize` for
the size `log j! + j log (M / Ω)` of a derivative of order `j`, `s_fin = D.primeSum` for the prime
sums, `s_main = D.mainPrimeSum` for the expected mean of `s_fin(a, τ)` over `τ ∈ Φ_a = D.aPlaces`,
and `κ(τ) = D.weight τ` for the weight at an infinite place `τ`. Then the main amount is
`h_main = m k ∑_τ (s_∞(κ(τ)) - s_fin(κ(τ), τ))`, with `m` the number of lifts and `k` the rank of
the source, the total remainder is `rem = ∑_{τ ∈ Φ_a} (s_fin(a, τ) - s_main)`, and
`gain_p = D.gain p` is the divisibility asked at a prime `p < x₁` that does not split in
`ℚ(√-d)`. 

 ### One kernel 

### `rowMainLength_add_rowSlack_le`

 For row `i` of the Young diagram of the weight of a lift at the infinite place `τ`, the main
length plus the slack is at most `2 a`, where `a = D.a` is the product `x b` of two scales. The main
length is `a` or `0` for `i = 0`, the weight `D.weight τ` for `0 < i < D.k`, and `0` otherwise; the
slack is the number of boxes by which the row may exceed its main length. 

### `rowSizeSum`

 The sum of `s_∞ = D.jetSize` over the lengths of the first `n_j = D.n j` rows, at all infinite
places `τ`, of the Young diagrams of the weight of the lift from `X_j` to `X_{j+1}`. The diagram at
`τ` has `D.columnCount τ h` columns of height `h`. 

### `chainSize`

 The main term `m (#Φ_a s_∞(a) + k ∑ τ, s_∞(κ(τ)))` of the size of the chain of `m` lifts, where
`s_∞ = D.jetSize`, `κ = D.weight`, `k` is the rank of the source and `Φ_a = D.aPlaces` is the set of
`a`-places, the places at which the diagrams have `a` columns of height `1`. 

### `sqrt_weylNormSq_jetMap_le`

 **One kernel.** Let `j < m`, let `X_j` be the definite hermitian space over `E = D.E` with basis
`D.X j`, and let `Gf` denote the finite adelic points of its unitary group. The theta kernel
`D.liftKernel TameChar.one j` of the lift from `X_j` to `X_{j+1}`, for the trivial twisting
character, acts through the Weil representation `ω` on Schwartz functions. Apply `ω (g, g')` to the
translate `D.translateDatum t j` by `t` of the normalised vacuum function; `jetMap` turns the result
into a linear map between the Weyl modules with column numbers `D.columnCount`, whose coordinates
are indexed by `WeylIndex`. For `σ ∈ Aut ℂ`, this map multiplies the norm √`weylNormSq` of
`σ`-conjugates by at most `exp (x ^ 50 + rowSizeSum j / 2)`. Here `x = D.x` is the scale and
`rowSizeSum j` is the sum of `D.jetSize` over the row lengths of the weight. 

 ### The rows 

### `sum_range_jetSize_add_eq`

 Sum, over the `n_j = D.n j` rows of the Young diagram of lift `j` at the infinite place `τ`, the
size `s_∞ = D.jetSize` of the main length of the row plus `25 log b` times its slack. The main
lengths are `D.columnCount τ 1` for the first row, the weight `κ(τ) = D.weight τ` for the next
`k - 1` rows, with `k = D.k` the rank of the source, and `0` otherwise. The slacks add up to
`b + offWeight + n_j halfGap ^ 2`, where `b = D.natB` and `offWeight` are the two values of `κ` and
`halfGap = D.r ^ 8`. 

### `sum_rowSizeSum_le`

 The chain has `m = D.m` lifts, and `rowSizeSum j` adds the sizes `s_∞ = D.jetSize` of the row
lengths of the Young diagrams of the weight of lift `j`. The sum over `j < m` is at most
`chainSize = m (#Φ_a s_∞(a) + k ∑ τ, s_∞(κ(τ)))` plus half of `errorUnit = f a log³ b`. Here
`Φ_a = D.aPlaces`, `k = D.k` is the rank of the source, `κ(τ) = D.weight τ` is the weight at the
infinite place `τ`, `f` is the number of infinite places, and `a = x b` for the scales `x`, `b`. 

### `chainSize_sub_le`

 The main term `chainSize = m (#Φ_a s_∞(a) + k ∑ τ, s_∞(κ(τ)))` of the size of the chain of `m`
lifts, less the saving `#Φ_a a log N` from the restriction, is at most
`h_main - m rem + 2 ∑ gain_p log p + 32 f a log b`. Here `s_∞ = D.jetSize`, `κ = D.weight`,
`Φ_a = D.aPlaces` is a subset of the `f` infinite places, the level `N` is a prime, and `a = x b`
for the scales `x`, `b`. With `s_fin = D.primeSum`, the main amount is
`h_main = m k ∑_τ (s_∞(κ(τ)) - s_fin(κ(τ), τ))` and the total remainder is
`rem = ∑_{τ ∈ Φ_a} (s_fin(a, τ) - D.mainPrimeSum)`. 

 ### The terms and the restriction 

### `weylNormSq_restrictedChain_le`

 Let `X_j`, `Y_m` be the hermitian spaces over the CM field `E = D.E` of the chain of `m = D.m`
theta lifts; `Gf` denotes finite adelic points of their unitary groups and `D.FormX j` the forms on
`X_j`. Let `Ψ` be a weak chain datum for the trivial twist: coefficients of translates of the vacuum
function whose sum is invariant, with `∑ t, |σ (Ψ t)| ≤ exp (D.x ^ 60)` among the conditions.
`restrictedChain TameChar.one Ψ φ` lifts the form `φ` from `X_0` to `X_m` with these translates,
combines the results by `Ψ` and restricts to `Y_m`. If the values of `σ φ` have squared norm at most
`exp B`, then those of the `σ`-conjugate of the lift have squared norm at most `exp (B + β)`, where
`β = h_main - m rem + 2 ∑ gain_p log p + f a log³ b`. Here `h_main = D.mainAmount` is a difference
of archimedean sizes and prime sums, and `rem = D.totalRemainder` one of prime sums and their
expected mean `D.mainPrimeSum`, `gain_p` is the divisibility asked at a prime `p < D.x₁` that does
not split in `ℚ(√-d)`, `f` is the number of infinite places of `E`, and `a = x b` for the scales
`x`, `b`. 

### `weylNormSq_compositeLift_le`

 **Size of the composite lift.** Let `Ψ` be a chain datum for the trivial twist and `σ` an
automorphism of `ℂ`. `compositeLift TameChar.one Ψ φ` lifts the form `φ` from the hermitian space
`X_0` over `E = D.E` to `X_m` by `m = D.m` theta lifts, with the glued tensor as Schwartz data, and
restricts to `Y_m`; `Gf` denotes finite adelic points. If the values of `σ φ` have squared norm at
most `exp B`, then those of the `σ`-conjugate of the lift have squared norm at most `exp (B + β)`,
where `β = h_main - m rem + 2 ∑ gain_p log p + f a log³ b`. Here `h_main = D.mainAmount` is a
difference of archimedean sizes and prime sums, and `rem = D.totalRemainder` one of prime sums and
their expected mean `D.mainPrimeSum`, `gain_p` is the divisibility asked at a prime `p < D.x₁` that
does not split in `ℚ(√-d)`, `f` is the number of infinite places of `E`, and `a = x b` for the
scales `x`, `b`. 


## Passage to target forms by the good projection

A form `z` of principal level on `Y₀` is replaced by the target form `|𝖦| e₀ s z`, its good part
(`New.Data.goodProjTranslate s z`, for `s ∈ 𝖦`).

Here `𝖦 = New.Data.chosenGL` is a finite product of groups `GL_r` over residue fields, `New.Data.e₀`
is an element of its group algebra, and `New.Data.lowerChain`, `New.Data.lowerChainAtLevel` are the
same lift with two target types.


### `lowerChain_goodProjTranslate_apply`

 Let `𝖦 = D.chosenGL` be the finite group `∏ GL_r(𝔽_w)` over the chosen places `w` above `p₀`,
`p₁`, let `e₀ = D.e₀` be the good idempotent in `ℂ[𝖦]`, and let `ι = lowerChain ϑ` be the composite
of the `m` lifts from `Y₀` to `Y_m` for the tame character `ϑ`. For `s ∈ 𝖦` and a form `z` of
principal level on `Y₀`, the value at `g` of `ι (|𝖦| e₀ s z)` is the sum over `t ∈ 𝖦` of `|𝖦| e₀(t)`
times the value of `ι z` at `g * firstBlockLift ϑ (t * s)`. 

### `goodProjTranslate_mem_integralForms`

 Passage to the good part keeps integrality. Let `j : ℂ → ℂ_l` be a ring homomorphism; a form is
integral at `j` if each value `φ(g)`, mapped by `j` and moved by `g⁻¹`, has coordinates of `l`-adic
absolute value at most `1`. Let `ι = lowerChainAtLevel ϑ` be the composite of the `m` lifts from
`Y₀` to `Y_m` for the tame character `ϑ`, with values in the forms of given level and character.
Let `𝖦 = D.chosenGL` be a finite product of groups `GL_r` over residue fields and `e₀ = D.e₀` the
central idempotent of `ℂ[𝖦]` that cuts out the good part. For `c ∈ ℂ`, `s ∈ 𝖦` and `z` of principal
level on `Y₀`, if `c • ι z` is integral at `j`, so is `c • ι (|𝖦| e₀ s z)`. 

### `normSqAt_goodProjTranslate_le`

 Size of the good part, for the trivial twist, `σ ∈ Aut ℂ` and `s ∈ 𝖦`. The map `lowerChain` is
the composite of the `m` lifts from forms of principal level on `Y₀` to algebraic forms on `Y_m`. If
every value of `lowerChain TameChar.one z`, conjugated by `σ`, has squared norm at most `exp B`,
then the lift `φ` of `D.goodProjTranslate s z`, that is of `|𝖦| e₀ s z`, has
`normSqAt φ σ ≤ exp (x ^ 99 + B)`. Here `x = D.x` is the scale, `𝖦 = D.chosenGL` is a finite product
of groups `GL_r` over residue fields and `e₀ = D.e₀` is the central idempotent of `ℂ[𝖦]` that cuts
out the good part. 
