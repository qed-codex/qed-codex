---
{
  "module": "src/New/OneLift/HeckeValues/AlgebraicPartSize.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/HeckeValues/AlgebraicPartSize.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/HeckeValues/AlgebraicPartSize.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Archimedean bounds and heights of squared norms of rank-one theta lifts

This file bounds the absolute values of the conjugates under `Aut(ℂ/K)` of the squared norm `‖φ‖²`
of the lift `φ = New.Data.CriticalPair.trivialLift` of a critical pair for the trivial twist. It
also bounds the conjugates of `New.Data.CriticalPair.integralAlgebraicPart` for flat pairs
(`New.Data.CriticalPair.HasEmptyRow`, `c = z`). A conjugate of the squared norm is a multiple of the
squared norm of the lift for the conjugate character, and this is an `L`-value times explicit
factors. The file shows that flat pairs exist over a given character of weight zero and bounds the
range of the jet degrees of a main pair (`New.Data.CriticalPair.IsMainPair`). It bounds the height
(`New.HeightLe`) of the squared norm of the untwisted lift of a main pair.

## Main definitions and results

* `New.Data.heightLe_norm_trivialLift_sq`: for a main pair, a bound for the height of the squared
  norm of the untwisted lift.
* `New.Data.CriticalPair.norm_map_integralAlgebraicPart_le`: for a flat pair, every conjugate under
  `Aut ℂ` of `integralAlgebraicPart` at the trivial twist has absolute value at most
  `exp (x ^ 34)`.

Notions from other files:
* `New.Data.CriticalPair`: An integer 1 ≤ z ≤ t and a character ν of U(1)(𝔸) of weight −c, z ≤ c(v)
  ≤ 4b, with tame part supported on the chosen places.
* `New.Data.CriticalPair.integralAlgebraicPart`: The product of
  `n_L = chosenGroupOrder * denomBound ^ 2` and the algebraic part `‖φ‖² / N(Q) ^ (2 z - 1)`
  (`New.Data.CriticalPair.algPart`); the first factor of `n_L` clears the orders of automorphism
  groups, the second the denominators of `φ`.

## Relation to the literature

Critical Hecke L-values of CM fields as squared norms of theta lifts from U(1). See
`Lib.SiegelWeil.RallisInner.SharpData` for sources.


 ## Archimedean bounds for the algebraic part of flat pairs 

### `New.Data.CriticalPair.sqrt_weylNormSq_pointKernel_le`

 Archimedean bound for one value of the theta kernel of a flat pair `p = (ν, z)`. For
`σ ∈ Aut ℂ`, the Gram norm of the conjugate under `σ` of `pointKernel` at the trivial twist and any
point of `U(1) × U(n)` has a bound that depends on `D` and `card n` only. 

### `New.Data.CriticalPair.normSqAt_trivialLift_le`

 Let `p = (ν, z)` be a critical pair of the data `D`, let `n` have `2 z ≥ 4` elements, let
`φ = trivialLift h_rank .one` be the normalised lift of `ν` to `U(n)` at the trivial twist, and let
`σ ∈ Aut ℂ`. Suppose all `σ`-conjugates of kernel values have norm at most `C`. Then `normSqAt σ`,
the sum over the classes of `U(n)` at the level of `φ` of the squared norms of the `σ`-conjugates of
the values of `φ`, each divided by the order of its stabiliser, is at most
`exp (x ^ 30) * (exp (x ^ 30) * C) ^ 2`, where `x = D.x` is the length of the prime sum. 

### `New.Data.CriticalPair.chosenGroupOrder_mul_denomBound_sq_le`

 For a flat pair `p = (ν, z)` (`HasEmptyRow`: `ν` has weight `-z` at every infinite place), the
integer `D.chosenGroupOrder * p.denomBound ^ 2`, by which `integralAlgebraicPart` multiplies the
algebraic part `algPart`, is at most `exp (x ^ 33)`, where `x = D.x` is the length of the prime sum.


### `New.Data.CriticalPair.norm_map_integralAlgebraicPart_le`

 Archimedean bound for a flat pair. Let `p = (ν, z)` with `ν` of weight `-z` at every infinite
place, let `n` have `2 z ≥ 4` elements (`HasEmptyRow`), and let `φ` be the normalised lift of `ν` to
`U(n)`. At the trivial twist `integralAlgebraicPart` is `‖φ‖²` times the integer
`chosenGroupOrder * denomBound ^ 2`, which clears the orders of stabilisers and the denominators of
`φ`. Every conjugate of it under `Aut ℂ` has absolute value at most `exp (x ^ 34)`, where `x = D.x`
is the length of the prime sum. 


## Galois conjugates of the squared norm of the lift

`New.Data.CriticalPair.exists_log_norm_map_norm_sq_trivialLift_eq_add_sum_jetSize` estimates the
absolute values of the conjugates under `Aut(ℂ/K)` of the squared norm of the lift for the trivial
twist. A conjugate of the squared norm is a multiple of the squared norm of the lift for the
conjugate character, and this is an `L`-value times explicit factors.


### `New.Parameters.exists_eq_star_map_star_and_placePerm_eq`

 For `σ ∈ Aut(ℂ/K)` the map `star ∘ σ ∘ star` lies in `Aut(ℂ/K)`, and it permutes the infinite
places of `P.E s`, the CM field of index `s` in the tower over `K`, as `σ` does (`placePerm`). 

### `New.Data.CriticalPair.norm_trivialLift_sq_eq_mul_inner`

 Let `p = (ν, z)` be a critical pair with `card n = 2 z ≥ 4` and `ν` of weight `-p.negWeight`,
let `ϑ` be a tame character and `J = p.rowLengthSum = ∑ τ, (p.negWeight τ - z)`. Let `A` be
`jetScale ^ J` times the lift of `ν ϑ` to `U(n)` without scaling. The normalised lift
`φ = trivialLift H ϑ` is `vacuumScale ^ card n * (star piMBar) ^ J` times `A`, where `piMBar` is an
integer of `K` of norm `M = D.M`. Hence `‖φ‖² = ‖vacuumScale ^ card n‖² * M ^ J * ⟪A, A⟫`. 

### `New.Data.CriticalPair.exists_norm_map_inner_trivialLift_eq_mul`

 Let `σ` be an automorphism of `ℂ` over the imaginary quadratic field `K = ℚ(i√d)` of the
parameters `P`. There is a constant `a > 0` with the following property. Let `p = (ν, z)` be a pair
with `card n = 2 z ≥ 4` and `ν` of weight `-p.negWeight`, and let
`J = p.rowLengthSum = ∑ τ, (p.negWeight τ - z)`. Let `A` be `jetScale ^ J` times the lift for the
data of `p` at the trivial twist. Then there are lift data `Y` on the same places, with the row
lengths `p.negWeight τ - z` permuted by `σ` (`placePerm`), such that `‖σ ⟪A, A⟫‖` is `Ω ^ (-J) * a`
times the squared norm of the lift for `Y`. Here `Ω = P.bigOmega D.towerExp = exp (γ - Re L'/L(1,
χ_K)) 2π / rd_E`, with Euler's constant `γ` and the root discriminant `rd_E` of `D.E`. 

### `New.Data.exists_log_norm_inner_trivialLift_eq`

 Size of the squared norm of a lift without twist. Let `S` be level places of `D.E` without twist
places. There is a constant `c` such that for all data `Y` on `S` of a theta lift from `U(1)` to
`U(n)`, with `card n = 2 k ≥ 4`, the lift `φ = Y.trivialLift` has `⟪φ, φ⟫ ≠ 0` and
`log ‖⟪φ, φ⟫‖ = c + r + ∑ τ, log (Y.rowLength τ)!` with `-4 f ≤ r`, and `r ≤ 4 f` if all row lengths
vanish. Here `f` is the number of infinite places `τ`. 

### `New.Data.CriticalPair.exists_log_norm_map_norm_sq_trivialLift_eq_add_sum_jetSize`

 Size of the conjugates of `‖φ‖²`, where `φ = trivialLift H .one` is the normalised theta lift to
the definite `U(n)` of the character `ν` of a pair `p = (ν, z)`, without twist. Let `K P = ℚ(i√d)`
be the imaginary quadratic field of the parameters. For `σ ∈ Aut(ℂ/K)` there is a constant `c` such
that for every critical pair `p` with `card n = 2 z ≥ 4` and `ν` of weight `-p.negWeight` there is a
real `r` with (a) `-4 f ≤ r`, (b) `r ≤ 4 f` if `p.negWeight τ = z` for all `τ` (`HasEmptyRow`), and
(c) `log ‖σ ‖φ‖²‖ = c + r + ∑ τ, jetSize (p.negWeight τ - z)`. Here
`jetSize j = log j! + j log (M / Ω)` with `M = D.M` and `Ω = P.bigOmega D.towerExp`, and `f` is the
number of infinite places `τ`. 


## Critical pairs with an empty row and the height of the squared norm of the lift

* `New.Data.exists_hasEmptyRow`: critical pairs with an empty row over a given character of weight
  zero.
* `New.Data.heightLe_norm_trivialLift_sq`: the height of the untwisted value of a main pair.
* `New.Data.CriticalPair.IsMainPair.negWeight_sub_z_mem_Icc`: the range of the jet degrees of a main
  pair.


### `exists_hasEmptyRow`

 Let `card n` be even and between `4` and the number `D.t = 5 * D.r` of the data `D`. Let
`χ = (μ, ψ)` be a character `μ` of `U(1)(𝔸)` of weight zero with its tame part `ψ`, which is trivial
off the chosen places. Then some critical pair `p = (ν, z)` has an empty row on `n`, has tame part
`ψ`, and has `ν υ ^ (card n / 2) = μ`, where `υ` is the splitting character on the norm-one ideles
(`New.rankTwist`). 

### `CriticalPair.IsMainPair.negWeight_sub_z_mem_Icc`

 Let `p = (ν, z)` be a main pair for `j` (`IsMainPair`: `m < z ≤ r`, tame part `D.chiMLocal ^ j`,
and `w_j + r - t ≤ c ≤ w_j` at every infinite place, for the weight `-c` of `ν` and
`w_j = D.liftWeight j`). At every infinite place `τ`, the row length `c τ - z` lies between the
weight `κ(τ) = D.weight τ` and `κ(τ) + x ^ 42`, where `x = D.x` is the length of the prime sum. 

### `heightLe_norm_trivialLift_sq`

 Let `p = (ν, z)` be a main pair for `j`, with `m = D.m` the number of lifts, `r = D.r` the rank
of the target and `t = 5 r`. Take the squared norm `‖φ‖²` of the untwisted lift of `ν` to `U(2 z)`
as a constant family, indexed by the primes `l` with an isomorphism `ℂ ≃ ℚ̄_l`. Then it has height
(`New.HeightLe`) at most `denominatorBudget - ∑ τ, jetSize (κ τ)`. Here
`denominatorBudget = f a log³ b / (m k)`, with `f` the number of infinite places `τ`, `b = D.b` the
weight scale, `a = x b` for the length `x` of the prime sum and `k = r + 1 - m`; further
`κ τ = D.weight τ`, and `jetSize i = log i! + i log (M / Ω)` is the size of a derivative of order
`i`, with `M = D.M` and `Ω = P.bigOmega D.towerExp`. 
