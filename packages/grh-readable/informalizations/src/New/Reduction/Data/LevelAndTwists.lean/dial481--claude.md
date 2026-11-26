---
{
  "module": "src/New/Reduction/Data/LevelAndTwists.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/LevelAndTwists.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/LevelAndTwists.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Weight bounds, the level N, and twists and m-fold twists for chains of lifts

The data `D` (`New.Data`) fix a CM field `E = D.E`, scales `x ≤ x₁ ≤ b`, a number `m` of lifts,
weights `κ` and `κ_j = D.liftWeight j` at the infinite places and a level `N`. The file bounds the
weight `κ` (`New.Data.weight`) and the numbers `κ_s` (`New.Data.shiftedWeight`,
`New.Data.liftWeight`). For a chain of lifts one takes powers `ϑ ^ j` of an m-fold twist `ϑ`, whose
powers of exponent `1, …, m` are all twists.

## Main definitions and results

* `New.Data.targetParameter`: the row parameter, a sequence of integers at each infinite place.
  `New.Data.targetParameter_eq` writes its later entries as `Δ / 2 - κ_j`.
* `New.Data.logLevelTarget`: the logarithm of the lower end of the range for the level, between
  `m log b` and `24 m log b`. `New.Data.log_N_mem_Icc_logLevelTarget` puts `log N` within `√(log b)`
  above it, so `log N` lies between `m log b` and `30 m log b`. `New.Data.N_modEq_one` gives `N ≡ 1`
  modulo `New.Data.cyclotomicConductor`.
* `New.Data.TameChar`, `New.Data.Twist`: characters of `U(1)(𝔸)` of weight `0` with tame part
  `tamePart` supported on a finite set `Q` of places; a twist has `tamePart w ≠ 1` on `Q`.
* `New.Data.untwistedLiftChar`, `New.Data.liftChar`: the characters `μ_j⁰` and `μ_j⁰ ϑ` of weight
  `-κ_j`.
* `New.Data.MFoldTwist`: twists whose powers of exponent `1, …, m` are twists
  (`New.Data.MFoldTwist.powTwist`).
* `New.Data.chainChar`: the character `μ_j⁰ ϑ ^ j` of lift `j` of a chain. It is given by
  `New.Data.liftChar` applied to `ϑ ^ j` and `j`.

Notions from other files:
* `New.Data.weight`: the weight `κ` of an infinite place of `E`. It is `b = a / x` at the
  `b`-places, which form a chosen finite set `D.bPlaces`, and `a / x₁` at the others; `a = x b`.
* `New.Data.shiftedWeight`, `New.Data.liftWeight`: `D.shiftedWeight i σ` is `κ_s = κ + (s + 1/2) Δ`
  at `s = i / 2`, and `D.liftWeight j σ` is `κ_j`; the gap is `Δ = D.gap = 2 * D.halfGap`.
* `New.Data.HasLogBound`: `D.HasLogBound u F l` is `|F| ≤ exp l` if `u` is true (`D.HasLogUpper`)
  and `exp l ≤ F` if `u` is false (`D.HasLogLower`).
* `New.AutChar`: the group of automorphic characters of `U(1)(𝔸)`.
* `New.AutChar.HasWeight`: `μ.HasWeight e ψ` says that the character `μ` has weight `e` and tame
  part `ψ`, that is, almost all residue characters `ψ_w` are trivial and
  `μ(u) = ∏_v u_v ^ e(v) * ∏_w ψ_w(u mod w)` whenever `u` has integral finite part.


 ## Bounds for the weights κ and κ_j 

### `weight_mem_Icc`

 The weight `κ = D.weight σ` of an infinite place `σ : D.Φ` of the field `E = D.E` satisfies
`a / x₁ ≤ κ ≤ a / x`, where `x ≤ x₁ ≤ b` are the scales of the data and `a = x b`. 

### `instance {u : Bool} : D.HasLogBound u (D.weight σ) (D.logB + if u then 0 else -D.logX₁)`

 The size of the weight: `b / x₁ ≤ κ ≤ b` (upper bound for `u` true, lower for `u` false). 

### `weight_le_b`

 The weight `κ = D.weight σ` of an infinite place is at most the scale `b`. 

### `weight_add_x_pow_le_two_mul_b`

 The weight `κ = D.weight σ` satisfies `κ + x⁴² ≤ 2 b`, for the scales `x ≤ b`. 

### `weight_le_liftWeight_sub`

 The weight `κ = D.weight σ` is at most `κ_j - Δ / 2`, where
`κ_j = D.liftWeight j σ = κ + (j + 1/2) Δ` and `Δ / 2 = D.halfGap` is half the gap. 

### `shiftedWeight_mem_Icc`

 For `i ≤ 4 m` the shifted weight `D.shiftedWeight i σ = κ + (i + 1) Δ / 2` lies between `κ` and
`κ + x⁴²`, where `κ = D.weight σ` and `Δ / 2 = D.halfGap` is half the gap. 

### `log_shiftedWeight_le`

 For `i ≤ 4 m` one has `log (D.shiftedWeight i σ) ≤ log κ + 1 / x`. 

### `liftWeight_le_weight_add`

 For `j ≤ 2 m` the shifted weight `κ_j = D.liftWeight j σ` is at most `κ + x⁴²`, with
`κ = D.weight σ`. 

### `liftWeight_le_two_mul_b`

 For `j ≤ 2 m` the shifted weight `κ_j = D.liftWeight j σ` is at most `2 b`. 

### `instance : D.HasLogUpper (D.liftWeight 0 σ) (2 + D.logB)`

 The size of `κ₀ = D.liftWeight 0 σ`: it is at most `2 b`, so at most `exp (2 + log b)`. 

### `instance {l : ℝ} [D.HasLogLower (D.weight σ) l] : D.HasLogLower (D.liftWeight j σ) l`

 A lower bound `exp l ≤ κ` for the weight `κ = D.weight σ` gives `exp l ≤ κ_j` for the shifted
weight `κ_j = D.liftWeight j σ`, because `κ ≤ κ_j`. 

### `log_liftWeight_le`

 For `j ≤ 2 m` the shifted weight `κ_j = D.liftWeight j σ` has `log κ_j ≤ log κ + 1 / x`, with
`κ = D.weight σ`. 


## The row parameter, the level N, twists and the characters of the lifts

`New.Data.le_of_hasLogBound` proves an inequality by comparing bounds `New.Data.HasLogBound`, so
sizes are recorded here as instances.


### `targetParameter`

 The row parameter `(k/2 - 1, k/2 - 2, …; -κ_{1/2}, -κ_{3/2}, …)` at the infinite place `v` of
`E`, the sequence from which the Harish-Chandra parameters at `v` of the unitary groups in the chain
of lifts are read off. Entries are numbered from `0`, with `k - 1` entries before the semicolon.
Here `k = D.k = r + 1 - m` is the rank of the source, for the rank `r = D.r` of the target and the
number `m = D.m` of lifts; `k/2` is integer division; and `κ_s = D.shiftedWeight (2 s) v` is the
shifted weight `κ + (s + 1/2) Δ`. The rank `k` is even (`New.Data.k_even`). 

### `targetParameter_eq`

 A formula for entry `i` of the row parameter `D.targetParameter v`, the integer sequence
`(k/2 - 1, k/2 - 2, …, 1 - k/2; -κ_{1/2}, -κ_{3/2}, …)` at the infinite place `v` of `E = D.E` from
which the Harish-Chandra parameters in the chain of lifts are read off. The entries with
`i < k - 1` are `k/2 - 1 - i`, and entry `i ≥ k - 1` is `Δ / 2 - κ_j` with `j = i + 2 - k`. Here the
rank `k = D.k` of the source is even (`New.Data.k_even`), so the division `k / 2` is exact;
`Δ / 2 = D.halfGap` is half the gap; and `κ_j = D.liftWeight j v = κ + (j + 1/2) Δ` is the shifted
weight, for the weight `κ` of `v`. 

### `instance {u : Bool} : D.HasLogBound u (P.bigOmega D.towerExp) (if u then 0 else -13 * D.logX)`

 The size of `Ω = exp (γ - Re L'/L(1, χ_K)) * (2 π / rd_E)`: one has `x⁻¹³ ≤ Ω ≤ 1` (upper bound
for `u` true, lower for `u` false). Here `γ` is Euler's constant, `χ_K` is the quadratic character
of `K = ℚ(√-d)` for the prime `d = P.d`, and `rd_E` is the root discriminant of the field
`E = P.E s` of the data, where `s = D.towerExp` is the exponent with `2 ^ s = m ^ 22`. 

 ### The size and the residue class of the level `N` 

### `logLevelTarget`

 The logarithm of `N₋ = κ̄ ^ m (M rd_E / 2π) ^ (m - 1) b ^ (-15 / 2)`, the lower end of the range
for the level. Here `κ̄` is the geometric mean of the weights at the `f = D.f` infinite places of
`E`, the principal level `M = D.M` is the product of the two primes `D.levelPrime 0` and
`D.levelPrime 1`, and `rd_E = D.rootDisc` is the root discriminant of `E`. 

### `logLevelTarget_eq_logLevelMin`

 The number `D.logLevelTarget` is `New.Parameters.logLevelMin` at the values given by the
data. 

### `logLevelTarget_mem_Icc`

 The prime level `N` of the data is chosen with `log N₋ ≤ log N ≤ log N₋ + √(log b)`, where
`log N₋ = D.logLevelTarget` is the logarithm of `κ̄ ^ m (M rd_E / 2π) ^ (m - 1) b ^ (-15 / 2)`. This
lower end satisfies `m log b ≤ log N₋ ≤ 24 m log b`, for the number `m = D.m` of lifts and
`log b = D.logB`. 

### `N_modEq_one`

 The level `N` is `≡ 1` modulo `n = D.cyclotomicConductor = q₁ d`. Here `d` is the prime with
`K = ℚ(√-d)` and `q₁` is the order of the root of unity that generates `E` over `K`, so `E` lies in
`ℚ(ζ_n)`. 

### `log_N_mem_Icc_logLevelTarget`

 The level `N` satisfies `log N₋ ≤ log N ≤ log N₋ + √(log b)`, where
`log N₋ = D.logLevelTarget`. 

### `log_N_mem_Icc`

 The level `N` satisfies `m log b ≤ log N ≤ 30 m log b`. 

### `instance {u : Bool} : D.HasLogBound u (Real.log D.N) (D.logX / 2 + Real.log D.logB + (if u then 32 else 0))`

 The size of `log N`: `√x log b ≤ log N ≤ e³² √x log b` (upper bound for `u` true, lower for `u`
false), from `m log b ≤ log N ≤ 30 m log b` and `√x ≤ m ≤ 2 √x`. 

### `instance : Fact D.N.Prime`

 The level `N` is prime. 

### `instance : D.HasLogLower D.N (101 * D.logB)`

 The level is large: `b¹⁰¹ ≤ N`. 

 ### Tame characters and twists 

### `TameChar`

 A character of U(1)(𝔸) of weight 0 whose tame part is supported on a finite set Q of places. The
places of Q have norm prime to M N, with M = `D.M` and N the level, and Q is disjoint from its
conjugate. 

### `TameChar.toAutChar`

 The automorphic character `ϑ` of `U(1)(𝔸)`. 

### `TameChar.Q`

 The modulus: a finite set of finite places of `E`. 

### `TameChar.tamePart`

 The tame part: one character of the residue field at each finite place. 

### `TameChar.hasWeight`

 The character has weight `0` and tame part `tamePart`. 

### `TameChar.tamePart_eq_one`

 The tame part is trivial outside `Q`. 

### `TameChar.star_notMem`

 `Q` is disjoint from its complex conjugate. 

### `TameChar.coprime`

 The places of `Q` have norm prime to `M N`, where `M = D.M` and `N` is the level. 

### `TameChar.normQ`

 The product of the norms of the places in the finite set Q of the tame character ϑ. 

### `Twist`

 A twist: a tame character (`New.Data.TameChar`) whose tame part is non-trivial at every place of
its set Q. 

### `Twist.tamePart_ne_one`

 The tame part is non-trivial at every place of `Q`. 

### `instance : One D.Twist`

 The trivial twist, with empty set Q and trivial tame part. 

### `instance : Coe D.Twist D.TameChar`

 A twist is read as its tame character. 

### `TameChar.one`

 The trivial character, as a tame character with empty set Q and trivial tame part. 

 ### The characters of the lifts 

### `untwistedLiftChar`

 The character μ_j⁰ = μ♭(υ^{−Δ}χ)^j of U(1)(𝔸). Here μ♭ = `D.chiZero` has weight −κ₀ and trivial
tame part, χ = `D.chiM` has weight 0 and tame part `D.chiMLocal`, υ is the restricted splitting
character `New.WeilData.upsilonU1` and Δ = `D.gap` is the gap. 

### `untwistedLiftChar_hasWeight`

 The character μ_j⁰ = `D.untwistedLiftChar j` of U(1)(𝔸), for the field E = `D.E`, has weight
−κ_j and tame part ω^j (`HasWeight`): almost all ω_w^j are trivial, and μ_j⁰(u) = ∏_v
u_v^{−κ_j(v)} · ∏_w ω_w^j(u mod w) whenever u has integral finite part, with v running over the
infinite places `InfinitePlace D.E` and w over the finite places of E. Here
κ_j = `D.liftWeight j` = κ₀ + jΔ for the gap Δ = `D.gap`, and μ_j⁰ = μ♭(υ^{−Δ}χ)^j, where
μ♭ = `D.chiZero` has weight −κ₀ and trivial tame part, υ = `upsilonU1` has weight 1 and trivial tame
part, and χ = `D.chiM` has weight 0 and tame part ω = `D.chiMLocal`, a family of characters ω_w of
the residue fields. 

### `liftChar`

 For a tame character ϑ and a natural number j, the character μ_j⁰ϑ of U(1)(𝔸). 

### `liftTamePart`

 The family of residue field characters ω_w^j ψ_w, with ω = `D.chiMLocal` and
ψ = `ϑ.tamePart`; it is the tame part of μ_j⁰ϑ. 

### `hasWeight_liftChar`

 For a tame character ϑ, the character μ_j⁰ϑ = `D.liftChar ϑ j` has weight −κ_j, with
κ_j = `D.liftWeight j`, and tame part `D.liftTamePart ϑ j`, the product of `D.chiMLocal ^ j` and
`ϑ.tamePart`. 

### `LiftIndex`

 The natural numbers j with 1 ≤ j ≤ m, for the number m of the data; they index the lifts. 

 ## Powers of tame characters and m-fold twists 

### `TameChar.pow`

 For a tame character ϑ and a natural number n, the tame character ϑⁿ, with the same set Q and
tame part `ϑ.tamePart ^ n`. 

### `MFoldTwist`

 An m-fold twist: a twist ϑ whose tame part has `tamePart w ^ n ≠ 1` for all w in Q and
1 ≤ n ≤ m. 

### `MFoldTwist.pow_ne_one`

 For `1 ≤ n ≤ m` the `n`-th power of the tame part is non-trivial at every place of `Q`. 

### `chainChar`

 For a tame character ϑ and a natural number j, the character μ_j⁰ϑ^j of U(1)(𝔸), used for
lift j of a chain. 

### `instance : One D.MFoldTwist`

 The trivial twist is an m-fold twist, since its set Q is empty. 

### `instance : Coe D.MFoldTwist D.Twist`

 An m-fold twist is read as its underlying twist. 

### `MFoldTwist.powTwist`

 For an m-fold twist ϑ and 1 ≤ n ≤ m, the power ϑⁿ as a twist. 
