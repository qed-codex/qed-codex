---
{
  "module": "src/New/Reduction/MainInequality.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/MainInequality.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/MainInequality.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The main inequality

One covolume, corrected by an index, is bounded from both sides. Write `dim` for the dimension of
the target (`targetDim`), `mainAmount` for the main amount and `rem` for the total remainder
(`totalRemainder`), weighted sums over primes less their expected values. Theorems A and B give a
family of `n ≤ dim` target forms, a bound `V` for the logarithm of the squared covolume of its lifts
(`TwistedLattice.CovolumeLe`) and a bound `δ` for its index (`TwistedLattice.IndexLe`). Up to
errors,

    mainAmount ≤ (V + 2 δ) / dim ≤ mainAmount - (n / dim) m rem,

where the lower bound is Theorem C. The main amount cancels.

Notions from other files:

* `Data P`: the data for the parameters `P` (a modulus `q₀` and a prime `d`). They bundle
  scales `x`, `x₁`, `b` in prescribed ranges (`D.logB = log b`), the number `D.m` of lifts, a set
  of places of the CM field `D.E`, the `b`-places, which carry the weight `b`, and primes for the
  levels. `D.a = x b`, and `D.f` is the number of infinite places of `D.E`.
* `D.normalizedPoincare g`: the translate `g 𝔭` by `g : D.chosenGL` of a fixed linear map `𝔭` from
  the source `D.ramifiedSourceForms` to the target `D.targetForms`.
* `D.integralRamified`: the source forms that are integral at every `ι : PrimePadicIso`.
* `D.errorUnit`: the unit of loss `f a log³ b`.

## The inputs

* Theorem A: (a) `span_short_integralRamified_eq_top` (size) and (b) `indexLe_normalizedPoincare`
  (index).
* Theorem B: `enough_forms`.
* Theorem C: `integral_forms_long`, from a twist for each prime
  (`TwistedLattice.covolume_add_index_nonneg`) and the height of `Z(1) / Z(ξ_ι)`
  (`heightLe_chainDeterminant_one_div`).
* Hadamard's bound for the covolume: `TwistedLattice.covolumeLe_of_normSqAt_le`.
* The sign of the main amount: `mainAmount_nonneg`.

## What cancels, and where

* The main amount, between the upper and the lower bound: the comparison step of
  `star_inequality`.
* The gains `∑ gain_l log l` in the size of the chain, against `log c_B`:
  `span_short_integralRamified_eq_top`.
* The constant `c₁ = (logDerivMean d 1 1).re`, between the period and the expected value
  `a (log (a / κ̄) + c₁)` of the prime sums:
  `jetSize_sub_mainPrimeSum_le`.
* The excesses `a log (κ̄ M rd_E / 2π)` of the `m` lifts, against `a log N`, up to `O(a log b)`.
  Here `κ̄` is the geometric mean of the weights `κ` over the `f` places and `rd_E` is the root
  discriminant of `E`:
  `mul_jetSize_sub_mainPrimeSum_sub_le`.
* The main terms `log x`, `log x₁` and `c₁` of the prime sums, against their expected value:
  `totalRemainder_eq`.
* A constant that depends on `q₀`, between the two cut-offs: `sum_aPlaces_primeSum`.

## The errors per dimension

| source   | where             | amount                              |
|----------|-------------------|-------------------------------------|
| size     | Theorem A (a)     | `f a log⁴ b`                        |
| index    | Theorems A (b), B | `20 log (1 + 2 b²) · f a log³ b`    |
| covolume | Theorem C         | `3 f a log⁴ b`                      |

The index enters twice, and the table shows the doubled amount. The family has `n ≥ dim / 2`
members, so `m rem` is at most twice the sum, and twice the sum is at most `f a log⁵ b`. The scales
are listed in `New.Reduction.Data.Sizes`.

## Relation to the literature

Earlier bounds for sums over primes by size against divisibility: Pritsker, The Gelfond–Schnirelman
method in prime number theory, 2005; Granville–Stark, ABC implies no Siegel zeros for L-functions of
characters with negative discriminant, 2000; Bombieri, Counting points on curves over finite fields,
Sém. Bourbaki 430, 1973; van Frankenhuijsen, The Riemann hypothesis for function fields over a
finite field, 2008.


### `star_inequality`

 **Main inequality.** For the data `D` we have `m rem ≤ f a log⁵ b`.

The parameters `P` are a multiple `q₀` of `18480` and a prime `d ≡ q₀/2 - 1 mod q₀`. The scales are
integers with `(log b) ^ 100 ≤ x`, `x ^ 10⁶ ≤ x₁`, `x₁ ^ 10⁶ ≤ b` and
`log log b ≥ 10¹² P.constantBound`. 
