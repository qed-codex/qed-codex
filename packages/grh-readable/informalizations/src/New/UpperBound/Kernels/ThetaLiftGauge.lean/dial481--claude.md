---
{
  "module": "src/New/UpperBound/Kernels/ThetaLiftGauge.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Kernels/ThetaLiftGauge.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Kernels/ThetaLiftGauge.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# p-adic gauge bounds for one theta lift and data from functions modulo an ideal

This file derives `p`-adic bounds for one theta lift between the definite spaces with index types
`n` and `n'` from bounds on jets. A function `Ψ` on `n' × n` matrices modulo a modulus `𝔪`, put at
the places dividing `𝔪` with the integral vacuum elsewhere, gives a datum. If the values of `Ψ` are
integral away from `q`, an integer multiple of this datum is a standard datum at the primes not
dividing `q`.

## Main definitions and results

* `New.Kernel.raises`: the additive monoid of data that multiply gauges by at most `max c 0`.
* `New.Parameters.omega_mem_raises_of_schurJet_le`: a standard datum translated by `(1, x * d * y)`,
  with `d` diagonal at the places above `p` that define the gauge and `x`, `y` integral above `p`,
  raises gauges by at most `max B 0` for any bound `B` on the weighted entries of the jet matrices.
* `New.Parameters.mem_raises_of_standardData`: an explicit bound for a standard datum itself.
* `New.Parameters.smul_mem_raises_of_dvd`: if a multiple of a datum is standard and the scale is
  `p`-integral, an explicit larger multiple of the datum does not increase the gauges.
* `New.Parameters.smul_vacuumDatum_mem_standardData`: if `q * N` lies in `𝔪` and the values of `Ψ`
  are integral away from `q`, an explicit integer multiple of the datum is a standard datum at every
  prime `l` prime to `q`.
* `New.Parameters.isVacuumCombination_vacuumDatum`: the datum is a combination of translates of the
  scaled vacuum by finite adelic vectors, with coefficients of controlled size.

Notions from other files:
* `New.Kernel`: an abstract theta kernel, that is, a representation `ω` of the finite points of the
  two unitary groups on data and an equivariant map `jetMap` from data to linear maps.
* `New.thetaKernel`: the theta kernel of the definite pair `stdSpace E n`, `stdSpace E n'`; its jet
  matrix is `schurJet κ (jetSeries _ c f)`, with derivatives scaled by `c`.
* `New.weylGauge`: the `p`-adic sup norm of `g⁻¹` applied to `ιₚ ∘ ξ`, where `ιₚ : ℂ →+* ℂ_[p]` is
  the chosen `p`-adic place.
* `New.Parameters.standardData`: the span, over the ring of the complex `z` with `‖ιₚ z‖ ≤ 1`, of
  the translates of the integral vacuum `intVacuum V = vacuumScale ^ card n • V.vacElem` by the
  vectors that `δ` makes integral above `p`.
* `New.Seesaw.IsAdmissibleCombination`: a finite linear combination with conditions on the support,
  the denominators and the size of the conjugates of its coefficients.

## Relation to the literature

See `New.UpperBound.Divisibility.LocalDivisibility` and
`New.UpperBound.Kernels.JetConjugatesAndBounds` for related work.


 ## Standard data and the p-adic gauge of a theta kernel 

### `New.weylGauge_add_le_max`

 The `p`-adic gauge `New.weylGauge` is ultrametric in the vector. 

### `New.Kernel.raises`

 The data `Φ` whose kernel multiplies the `p`-adic gauge by at most `c`: for all `g`, `h` and
`ξ`, the gauge at `h * d'` of `jetMap (ω (g, h) Φ) ξ` is at most `max c 0` times the gauge at
`g * d` of `ξ`. The factor is `max c 0` so that `0` is a member for every real `c`; sums stay inside
because the gauge is ultrametric. 

### `New.Kernel.smul_mem_raises`

 Let `k` be a theta kernel with data in `S`: the pairs of finite adelic points of rank `n`, `n'`
over the CM field `P.E s` act on `S` by `k.ω`, and `k.jetMap` sends a datum to a linear map from
vectors of weight `(κ, e)` in rank `n` to vectors of weight `(κ, ea)` in rank `n'`. Thus
`Φ ∈ k.raises d d' B` says that for all points `g`, `h` and vectors `ξ` the gauge at `h * d'` of
`jetMap (ω (g, h) Φ) ξ` is at most `max B 0` times the gauge at `g * d` of `ξ`. If this holds and
`‖ιₚ z‖ * B ≤ B'` for a complex number `z`, then it holds for `z • Φ` with `B'` in place of `B`. 

### `New.Kernel.omega_mem_raises_iff`

 Translating the datum by `(g₀, h₀)` amounts to translating the two base points: the translate
`k.ω (g₀, h₀) Φ` is in `k.raises (g₀ * d) (h₀ * d') B` exactly when `Φ` is in `k.raises d d' B`. 

### `New.diagonalWeight`

 The weight of the row `i` for diagonal matrices `u τ` over `ℂ_[p]` and exponents `e τ`: the
product over the places `τ` of `‖det (diagonal (u τ))‖ ^ e τ` and of the `‖u τ b‖` over the boxes of
the filling `i τ`, where `b` is the index in the box. 

### `pairWeil_mem_standardData`

 Let `a`, `b` be automorphic characters of the CM field `E = P.E s` with exponents `ea`, `eb` at
the infinite places and tame parts `ψ`, `ψ'` at the finite ones (`AutChar.HasWeight`). The standard
data for `δ` on the space of maps between the standard definite hermitian spaces `stdSpace E n`,
`stdSpace E n'` are the combinations, with coefficients `z` such that `‖ιₚ z‖ ≤ 1`, of the
translates of the integral vacuum (`intVacuum`) by the vectors that `δ` makes integral above `p`.
The Weil action `New.pairWeil` of a pair `(g, h)` of finite adelic points integral above `p`
preserves these data. Here `(1, g)` is the adelic point with trivial infinite part and finite part
`g`. 

### `omega_mem_raises_of_schurJet_le`

 Let `E = P.E s` (a CM field) and `Gf` its finite adelic unitary group. Take the theta kernel
(`thetaKernel`) of scale `c` and level `K`, for the standard definite spaces of ranks `n`, `n'` over
`E`. Its characters `a`, `b` have exponents `ea`, `eb`, and its weight `(κ, e)` has `κ τ h` columns
of height `h` at `τ` and lifts from rank `n` to `n'` (`IsLiftWeight`). Let `Ψ`, in the span
`finitePart` of vacuum translates, be standard for `δ`: a `p`-integral combination of translates of
the integral vacuum by points that `δ` makes integral above `p`. Let `x`, `y` in `Gf` be integral
above `p`. Suppose that, for each infinite place `τ`, the embedding `z ↦ ιₚ (Φ_τ (conj z))` of `E`
(`weightEmbedding`), extended to finite adeles (`adeleExtension`) and applied entrywise, sends `d`
to the diagonal matrix `u τ`, and that for every standard `f` and entry `(i', i)` of its jet matrix,
`‖ιₚ entry‖` times `diagonalWeight ea u i'` is at most `B`.

Then the translate `ω (1, x * d * y) Ψ` lies in `raises 1 1 B`: for all finite points `g`, `h`,
applying it after translation by `(g, h)` to a vector `ξ` gives a vector of gauge at `h` at most
`max B 0` times the gauge of `ξ` at `g`. 

### `omega_mem_raises_of_jet_minorProd_le`

 Take the theta kernel (`New.thetaKernel`) of scale `c`, at any level `K`, of the standard
definite spaces of ranks `n`, `n'` over the CM field `E = P.E s`, with characters `a`, `b` of
exponents `ea`, `eb`, and weight `(κ, e)` lifting from rank `n` to rank `n'` (`IsLiftWeight`). Let
`Ψ` be a standard datum for `δ`, and let `x`, `y` be finite points integral above `p`. Suppose that,
for each infinite place `τ`, the embedding `z ↦ ιₚ (Φ_τ (conj z))` of `E` (`weightEmbedding`) sends
`d` to the diagonal matrix `u τ`, and that for every standard `f`, every filling `i'` and all
`p`-integral `w τ col l`, the jet of the Taylor series `jetSeries c f` along the polynomial
`minorProd i' w` has norm at most `B` after multiplication by `diagonalWeight ea u i'`. This
polynomial is the product, over the places and the columns of height `h < card n'` of `κ`, of the
minors of the matrices `Z τ * w τ` on the rows listed in that column of `i'` and the columns
`l < h`. The weight is the product over `τ` of `‖det (u τ)‖ ^ ea τ` and of the `‖u τ b‖` over the
entries `b` of the filling.

Then the translate of `Ψ` by `(1, x * d * y)` multiplies the `p`-adic gauge `New.weylGauge` by at
most `max B 0`. 

### `mem_raises_of_standardData`

 Take the theta kernel (`New.thetaKernel`) of scale `c * P.jetScale s`, at any level `K`, of the
standard definite spaces of ranks `n`, `n'` over the CM field `P.E s`, with characters `a`, `b` of
exponents `ea`, `eb` and weight `(κ, e)` (`IsLiftWeight`). Here `P.jetScale s` is the scale at
which Taylor series of theta functions are taken and `P.d` is the prime with `P.K = ℚ(√(-P.d))`.
For an integer `δ ≠ 0` of `P.K`, a standard datum `Φ` for `δ` is a combination, with coefficients
integral under `ιₚ`, of translates of the integral vacuum by the vectors that `δ` makes integral
above `p`. Such a `Φ` lies in `raises 1 1` of `(‖ιₚ c‖ / ‖ιₚ (star δ * P.d)‖) ^ L`, where
`L = boxes κ (card n')` counts the boxes in columns of height below `card n'`: for all finite points
`g`, `h`, its kernel translated by `(g, h)` multiplies the `p`-adic gauge (`New.weylGauge`) from
`g` to `h` by at most this factor. 

### `mem_raises_predictedDivisibility`

 One lift at a prime `p` that is not split in `P.K = ℚ(√(-P.d))`. Take the theta kernel
(`New.thetaKernel`) of weight `(κ, e)` and scale `c * P.jetScale s`, with `c` integral at `p`, at
any level `K`. A standard datum `Φ` for `δ = 1` multiplies the `p`-adic gauge by at most
`p ^ (-(D - f * N ^ 3 * (1 + log_p (max L 1))))`, in the sense of `New.Kernel.raises`. Here
`f = card (P.Φ s)` is the number of infinite places, `N = card n'` and `L` is the number of boxes of
`κ` in columns of height below `N`.

The term `D` is `New.predictedDivisibility`. 

### `smul_mem_raises_of_dvd`

 Take the theta kernel (`New.thetaKernel`) of weight `(κ, e)`, with `κ` giving the column numbers
of the diagrams, and of scale `c * P.jetScale s`, where `P.jetScale s` is the scale of Taylor series
of theta functions and `‖ιₚ c‖ ≤ 1` for the chosen embedding `ιₚ : ℂ →+* ℂ_[p]`. Let `f` be a datum
such that `d • f` is standard for the natural number `N ≠ 0`. If `d * (N * P.d) ^ L` divides `M`,
where `L` is the number of boxes of `κ` in columns of height below `card n'`, then `M • f` does not
increase the `p`-adic gauge `New.weylGauge` (`New.Kernel.raises` with bound `1`). 

 ## Functions modulo an ideal on the vacuum as combinations of translates 

### `absNorm_span_natCast_eq_pow_numInfPlaces`

 The absolute norm of the ideal of `𝓞 (P.E s)` generated by a natural number `k` is
`k ^ (2 * numInfPlaces)`, where `numInfPlaces` is the number of infinite places of the CM field
`P.E s`. 

### `_root_.New.Modulus.card_residueRing_le`

 If a positive integer `k` lies in the ideal of the modulus `𝔪`, then the residue ring
`𝔪.ResidueRing` has at most `k ^ (2 * Core.numInfPlaces (P.E s))` elements. Here
`Core.numInfPlaces (P.E s)` is the number of infinite places of the CM field `P.E s`. 

### `smul_schrodingerOp_mem_standardData`

 Let `V` be a hermitian space over the CM field `E = P.E s` with basis indexed by `n` and signs
`ε`, let `𝔪` be a modulus, that is, an ideal of `𝓞_E` prime to its conjugate, and let `N q ∈ 𝔪`.
Let `Ψ` be a function on `(𝓞_E/𝔪)ⁿ` with values in `integralAway q`, that is, integral in every
embedding into `ℂ_[l]` for `l` prime to `q`. Its lift `𝔪.liftFn Ψ` to finite adelic vectors reduces
the components at the places dividing `𝔪` modulo `𝔪` and is `0` where they are not integral. The
operator `V.schrodingerOp 𝔪.places` is the combination of Heisenberg operators at those places
which puts this function there; it is applied to the integral vacuum
`intVacuum V = vacuumScale ^ card n • V.vacElem`. Then, for a prime `l` not dividing `q`,
`N^(2f|n|)` times this datum is a standard datum for `N` at the chosen place above `l`: a
combination, with coefficients integral at that place, of translates of the integral vacuum by
vectors `y` with `N y` integral above `l`. Here `f` is the number of infinite places of `E`. 

### `vacuumScale_pow_smul_vacuumDatum`

 The vacuum datum of `Ψ`, scaled by `P.vacuumScale s ^ |n' × n|`, is the operator `schrodingerOp`
of the space of `n' × n` matrices, for the lift of `Ψ` at the places of `𝔪`, applied to
`intVacuum`. 

### `smul_vacuumDatum_mem_standardData`

 Let `q N ∈ 𝔪`, let the values of `Ψ` on matrices modulo `𝔪` be integral away from `q`
(`integralAway`), and let `l` be a prime not dividing `q`. The vacuum datum of `Ψ`, scaled to be
integral and multiplied by `N^(2f|n'||n|)`, is then a standard datum for `N` at the chosen place
above `l`: an integral combination there of translates of the integral vacuum by vectors `y` with
`N y` integral above `l`. Here `f` is the number of infinite places of `P.E s`. 

### `isAdmissibleCombination_vacuumDatum_of_sum_le`

 Let `𝔪` be a modulus of the CM field `E = P.E s` and `Ψ` a complex function on the `n' × n`
matrices modulo `𝔪`, with `∑ x, ‖σ (Ψ x)‖ ≤ B` for all automorphisms `σ` of `ℂ`. The vacuum datum of
`Ψ` (`vacuumDatum`) is the datum on the maps between the standard spaces that is `Ψ` at the places
dividing `𝔪` and the vacuum elsewhere. Multiply it by `P.vacuumScale s ^ card (n' × n)`, the factor
that turns the vacuum into the integral vacuum `intVacuum`. The result is a finite combination
`∑ y, r y • (translate of intVacuum by y)` over finite adelic vectors `y` with `∑ y, ‖σ (r y)‖ ≤ B`
for all `σ`. 

### `isAdmissibleCombination_vacuumDatum`

 Let `𝔪` be a modulus of the CM field `P.E s` and `Ψ` a complex function on the `n' × n` matrices
modulo `𝔪` with `‖σ (Ψ x)‖ ≤ M` for all automorphisms `σ` of `ℂ` and all `x`. Its vacuum datum,
scaled by `P.vacuumScale s ^ card (n' × n)`, is a combination of translates of the integral vacuum
`intVacuum` by finite adelic vectors (`finHeisenbergOp`). For each `σ` the conjugates of the
coefficients have total absolute value at most `M` times the number of matrices modulo `𝔪`. 

### `isVacuumCombination_vacuumDatum`

 Let `Ψ` be a complex function on the `n' × n` matrices modulo the modulus `𝔪` of the CM field
`P.E s`, with `‖σ (Ψ x)‖ ≤ M` for all automorphisms `σ` of `ℂ` and all `x`. Then its vacuum datum,
scaled to be integral, is a finite combination of translates of the integral vacuum, and for every
`σ` the absolute values of the conjugates of its coefficients have sum at most `M` times the number
of matrices modulo `𝔪`. 

### `isAdmissibleCombination_vacuumDatum_indicator`

 For a modulus `𝔪` of the CM field `P.E s`, let the datum be the indicator of one matrix `y₀`
modulo `𝔪` at the places dividing `𝔪` and the vacuum elsewhere (`vacuumDatum`), scaled by
`P.vacuumScale s ^ card (n' × n)`. It is a finite combination of translates of the integral vacuum
`intVacuum` by finite adelic vectors (`finHeisenbergOp`) whose coefficients `r` have `∑ ‖σ r‖ ≤ 1`
for every automorphism `σ` of `ℂ`. 
