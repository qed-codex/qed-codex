---
{
  "module": "src/New/Congruences/Lifting/CutExponentBounds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Lifting/CutExponentBounds.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Lifting/CutExponentBounds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Exponent bounds by cuts for paired sides of a Kummer chart: sparse thick letters, two sizes

This file concerns two paired sides `S`, `S'` over a Kummer chart, whose distinguished element is
written `E`. Letters `i : k.Letter` are permuted by Frobenius `k.letterFrob`. The jumps
`S.jumpSet i`, `S'.jumpSet i` lie in `[-η, η] ∪ ∓ε i • [β i, β i + V]` (`New.Lift.FitsWindows`),
with opposite far windows, and `V + 4η ≤ W`. A cut a bounded number of letters back from each
letter then gives the bound for the exponent in `New.Lift.Pairing.IsScaledCupCoboundary`; two
choices of cuts treat the cases of two sizes of far windows: one where the thick letters, those
with the larger size, are sparse, and one where they form any pattern.

## Main definitions and results

* `New.Lift.KummerChart.PairingSide.killsCokernel_of_isKillingCut`: at a cut `i`, `p ^ κ * E ^ s i`
  kills the cokernel.
* `New.Lift.KummerChart.PairingSide.SidePairing.exists_stop_of_hasSignBefore`,
  `New.Lift.KummerChart.PairingSide.SidePairing.exists_stop_of_isLongGap`: the stop of the walk at a
  plain cut and at a cut with a long gap.
* `New.Lift.KummerChart.PairingSide.SidePairing.isScaledCupCoboundary_of_cut_windows`: the scheme.
  It derives the bound from a cut 1 to `2J + 1` letters back from each letter.
* `New.Lift.KummerChart.PairingSide.SidePairing.isScaledCupCoboundary_sparse_thick`,
  `New.Lift.KummerChart.PairingSide.SidePairing.isScaledCupCoboundary_any_pattern`: two choices of
  cuts and constants.

Notions from other files:
* `New.Lift.KummerChart`: a ring `k.S` = Λ⟦z⟧ in A_inf, where Λ = `WittFq k.f` = W(𝔽_{p^f}), and a
  subgroup Γ' of Γ of index prime to p that fixes Λ. It is unramified (`IsUnramified`) if E = z + p
  and the ramification index `k.e` is 1. The number `k.differentBound` is 0 if `k.e = 1` and
  v_p(e) + 1 otherwise.
* `New.Lift.KummerChart.Coeffs`: a ring of coefficients O, a finite free Z_p-algebra with an element
  ζ such that ζ^{p^f−1} = 1; ζ cuts out the letters.
* `New.Lift.KummerChart.Letter`: the letters of a Kummer chart, that is, the multiplicative group of
  the field with p^f elements in the tilt of the ring of integers of C_p; `i.stepBack a` is the
  letter `a` Frobenius steps back.
* `New.Lift.KummerChart.PairingSide`, `New.Lift.KummerChart.PairingSide.KillsCokernel`: one side
  of a pairing: lattices Y and C (`paramLattice`), an O-linear map `cocycleMap` from C to the
  crystalline cocycles Z_f(Y), and for each letter a finite set of integers that contains 0, the
  jumps. The extension `extensionLattice` of C by Y maps by `projTrivial` to `trivialLattice`, the
  lattice C with trivial action. `KillsCokernel`: `p ^ κ * E ^ s` multiplies the part of A_inf ⊗ C
  at a letter into the image of the standard module of level 0 of the extension.
* `New.Lift.KummerChart.PairingSide.pointsOver`: `S.pointsOver c i e o d` is the set of the vectors
  `x` of the Kisin module of the extension, with all φ^a E inverted, that lie over `p ^ e c` at `i`,
  have the orders `o` and have the depth `d`: every `g • x - x` with `g` in Γ' has exponents `d`.
* `New.Lift.raisedOrdersAtZero`: the orders `raisedOrdersAtZero t` are `-u` on the jump `u`, raised
  by `t` at E. The vectors with orders `raisedOrdersAtZero (-s)` have a pole of order at most `s` at
  E.
* `New.Lift.Pairing.IsSafeMoveFst`, `New.Lift.Pairing.IsSafeMoveSnd`: one side moves by a vector
  while the other rests at a point `x`. The move is safe for `κ` if, for all `g` in Γ', `p ^ κ`
  times the pairing of `g • x - x` with the move (for the second side, with `g` times the move) lies
  in the image of W(𝔪^♭).

## Relation to the literature

Take crystalline lattices with weights in short windows near 0 and near large weights, in the cases
of no small negative weight, two sizes, or sparse large weights. For these, an explicit power of p,
independent of the rank, makes crystalline classes cup to zero with those of congruent dual
lattices. This bounds the loss at the places above p in the Selmer bound. The case of small weights
and a rank-free factorial torsion bound by Sen operators are known in the literature. Related work:
Gao–Liu, Integral filtered Sen theory and applications, 2024; Iovita–Marmora, Continuity of the
finite Bloch–Kato cohomology, 2015; Y. Min, Congruences of first syntomic cohomology groups, 2026.


### `Letter.IsNearestCut`

 The letter `i.stepBack l` is the nearest cut before `i`. 

### `Letter.IsNearestCut.pos`

 The cut is at least one step back. 

### `Letter.IsNearestCut.cut_stepBack`

 The letter `l` steps back is a cut. 

### `Letter.IsNearestCut.not_cut`

 No letter strictly between it and `i` is a cut. 

### `Letter.HasSignBefore`

 Each of the `l` letters `i.stepBack a` with `a < l` has the sign `ρ`, or its far window
`[β, β + V]` ends at or below `η`. 

### `Letter.IsLongGap`

 A long gap at the pivot `i.stepBack t`, one of the `l` letters after `i.stepBack l` up to `i`:
the far window of the pivot starts far out, and the other letters have the opposite sign or small
far windows. The number `ω` bounds the low window and the far windows before the pivot. 

### `Letter.IsLongGap.isUnramified`

 The chart is unramified. 

### `Letter.IsLongGap.five_le`

 The prime is at least `5`. 

### `Letter.IsLongGap.shift_eq_zero`

 The letter `l` steps back has shift `0`. 

### `Letter.IsLongGap.pivot_add`

 The pivot is `J + 1` letters after `i.stepBack l`. 

### `Letter.IsLongGap.lt_far_pivot`

 The far window of the pivot starts beyond `s₀ + ω (1 + p + ⋯ + p ^ J)`. 

### `Letter.IsLongGap.sign_ne_or_far_le`

 The other letters have the opposite sign, or a far window that ends at or below `η`. 

### `Letter.IsLongGap.low_le`

 The low window ends at or below `ω`. 

### `Letter.IsLongGap.far_le`

 The far windows of the letters before the pivot end at or below `ω`. 

### `Letter.HasThinSuccessors`

 None of the `J` letters after `i` satisfies `T`. 

### `Letter.hasThinSuccessors_stepBack_add`

 Suppose that no three letters with `T` follow one another with both gaps between `1` and `J`.
If `i.stepBack r` satisfies `T` and does not have thin successors, that is, one of the `J` letters
after it satisfies `T` too, then `i.stepBack (r + (J + 1))` has thin successors: none of the `J`
letters before `i.stepBack r` satisfies `T`. 

### `Letter.IsKillingCut`

 The two kinds of letters `i` at which `p ^ κ * E ^ s i` is shown to kill the cokernel. 

### `Letter.IsKillingCut.of_thin`

 The shift is `0` and the next `J` letters have `β + W ≤ G`. 

### `Letter.IsKillingCut.of_isUnramified`

 The chart is unramified, `p ≥ 5`, and the shift lies in `[s₀ - κ, β i)`. 

### `CutSizes`

 The size conditions of the scheme of cuts, for shifts `s i`, far windows that start at `β i`
and a width `W`. The shifted far windows end at or below `2 b`, and `G` bounds `β + W` at the `J`
letters after a thin cut (`Letter.IsKillingCut.of_thin`). The number `n` bounds `G / (p - 1)`, and
`s₀` bounds `(β i + W) / (p - 3)` if `p ≥ 5`. The number `X` is the cost of one letter or level,
`δ` the cost of the depth `2 b`, and `p ^ κ` is the killer at a cut. Here `k.differentBound` is `0`
if the ramification index `k.e` is `1`, and `v_p(k.e) + 1` otherwise. 

### `CutSizes.le_cost`

 The unit of cost `X` is large against `n`, `log_p (2 b)`, `W` and `G`. 

### `CutSizes.cost_lt`

 The exponent `κ` exceeds `12 ((J + 1) X + δ)`. 

### `CutSizes.ramification_mul_le`

 The depth `2 b` times the ramification index is at most `p ^ (J + 1) δ`. 

### `CutSizes.ramification_le`

 The ramification index is at most `p ^ (J + 1) / 8`. 

### `CutSizes.far_le`

 The shifted far windows end at or below `2 b`. 

### `CutSizes.thin_le`

 The bound `G` is at most `(p - 1) n`. 

### `CutSizes.far_le_of_five_le`

 For `p ≥ 5` the far windows end at or below `(p - 3) s₀`. 

### `Letter.IsKillingCut.shift_eq_zero_or_lt`

 If `i` satisfies `i.IsKillingCut s β W J G s₀ κ`, then either the shift `s i` is `0`, or
`s i < β i` and `k.differentBound = 0`. 

### `cutOrders`

 The exponents of the standard point at a cut with shift `s`, where the cut before is `l` steps
back. The point has the exponents `raisedOrdersAtZero (-s)` (`-u`, lowered by `s` at the level `0`)
and the depth `standardDepth s η (l + 1)` (`-u`, raised by `s` at the level `0` and by `η` at the
levels up to `l`). This depth improves the exponents: they become the depth where they were
positive, and the minimum of the depth and `0` elsewhere (`JumpLattice.improvedOrders`). 

### `longGapDepth`

 The depth of the point at which a side rests when the walk meets a cut with a long gap: `r` at
the level `t` of the pivot, `1` at the other levels below `l`, and `-u` beyond. 

### `Letter.windowSteps`

 The steps that may be needed to deepen a point at `i` of a side whose far windows have the
signs `σ`: two windows, around `0` and `∓ β`, at each of the first `2 J + 2` levels. 

### `CutSizes.sum_cost_windowSteps_le`

 The steps `i.windowSteps σ s β W J` are the pairs `(a, m)` of a level `a < 2 J + 2` and an
integer `m` near `0` or near `-σ j • β j`, where `j = i.stepBack a` and `σ j` is any sign; near
means within `s i + W` at the level `0` and within `W` at the others. The step `(a, m)` costs
`k.cost a m = v_p(m) + d + 3 a`, with `v_p(0) = 0` and `d = k.differentBound`, which is `0` if the
ramification index `k.e` is `1` and `v_p(k.e) + 1` otherwise. Assume the size conditions `CutSizes`:
they make the cost `X` of a level large against `n`, `log_p (2 b)`, `W` and `G`, make `κ` exceed
`12 ((J + 1) X + δ)`, and bound every `β j + s j + W` by `2 b`. With `W ≥ 4` and `s i + W ≤ p n`,
and if `s i` or `d` is `0`, the steps then cost at most `24 κ - 4 δ` together. 

### `_root_.New.Lift.FitsWindows.le_add`

 A set that lies in the union of the low window `[-η, η]` and a far window `± [b, b + V]` is
bounded above by `b + W` if `V + η ≤ W`. 

### `killsCokernel_zero_of_next_le`

 Let `S` be a side whose jumps at each letter `i` are at most `β i + W`. Let the size conditions
`CutSizes` hold: `β + s + W ≤ 2 b` for the shifts `s`, the cost `X` is large against `n`, `W` and
`G`, with `G ≤ (p - 1) n`, the depth `2 b` costs `δ` over `J + 1` letters, and
`κ > 12 ((J + 1) X + δ)` (`s₀` plays no part). If `β + W ≤ G` at the `J` letters after `i`, then
`p ^ κ` kills the cokernel at `i`: it multiplies `A_inf ⊗ C`, for the lattice
`C = S.paramLattice`, into the image of the extension of level `0`. 

### `killsCokernel_of_isKillingCut`

 The cokernel at a cut of the side `S`. Let its jumps at each letter `i` be at most `β i + W`,
for shifts `s i`, and let the size conditions `CutSizes` hold. Then `p ^ κ * E ^ s i`, with `E` the
distinguished element, kills the cokernel of the extension over `S.paramLattice` at every letter `i`
with `IsKillingCut`: `s i = 0` and the next `J` letters have `β + W ≤ G`, or the chart is
unramified, `p ≥ 5` and `s₀ - κ ≤ s i < β i`. 

### `pointsOver_nonempty_of_sum_cost_le`

 The points `S.pointsOver c i e o₁ o₀` are the vectors of the extension of `C = S.paramLattice`
at the letter `i` over `p ^ e c` that have the orders `o₁` (divisibility by `t ^ (o₁ a u)` at
`φ^a E` on the jump `u`) and the depth `o₀` (the orders of all `g • x - x`, `g` in `Γ'`). Let `x` be
one. Let `steps` contain every pair `(a, m)` with `o₀ a u ≤ m < o a u` for a jump `u` at
`i.stepBack a`, the letter `a` steps before `i`, and let `e'` be at least `e` plus the costs
`k.cost a m = v_p(m) + k.differentBound + 3 a` of the steps. Then there is a point over `p ^ e' c`
of depth `o` with any orders `o'` that are at most `o` where `o₁` is positive and at most `min o 0`
elsewhere. 

### `pointsOver_cutOrders_nonempty`

 The standard point of a side `S` at a cut `i`. Let the jumps of `S` lie in `[-η, η]` and in the
far windows `σ j • [β j, β j + V]` of signs `σ j`. Let `η ≥ 1`, `V + 4 η ≤ W`, let the shifts `s`
have `s i + W ≤ p n`, let the size conditions `CutSizes` hold, let the cut be of a kind at which the
cokernel is killed, and let `l ≤ 2 J + 1` be its distance to the cut before. Then for `c` in
`S.paramLattice` the extension has a point at `i` over `p ^ (25 κ) c` with the orders
`cutOrders (s i) η l` and with depth `standardDepth (s i) η (l + 1)`: `-u`, raised by `s i` at the
level `0` and by `η` at the levels up to `l`. 

### `mem_pointsOver_plainDepth_of_cutOrders`

 Let the jumps of the side `S` at the letter `i` lie in `[-η, η]` and in the far window
`σ • [β i, β i + V]`, and let `i` be a cut of a kind at which the cokernel is killed, with shift
`s i`. Let `x` be a standard point at `i` over `p ^ e c`: the depth (the orders of all `g • x - x`)
is `standardDepth (s i) η (l + 1)`, that is `-u` raised by `s i` at the level `0` and by `η` at the
levels up to `l`, and the orders `cutOrders (s i) η l` are `-u - s i` at the level `0` and `-u`
above, improved by this depth. As no jump lies in `[-s i, -η)`, the point `x` has the orders
`raisedOrdersAtZero (-η)`, a pole of order at most `η` at the distinguished element `E`, and it has
the depth `plainDepth (s i) η l η` that a cut without long gap asks. 

### `pointsOver_longGapDepth_nonempty`

 The stop at `i` when the nearest cut before it, `i.stepBack l` (`l` letters back), is followed
by a long gap. Let `S` have its jumps in `[-η, η]` and in far windows of width `V` at `β` with signs
`σ`. The long gap at the pivot `i.stepBack t`, `J + 1` letters after the cut, means that its far
window starts beyond `s₀ + ω (1 + ⋯ + p ^ J)`, where `ω` bounds the windows before it; its signs
`ε` are not tied to `σ`. Let `σ` be `-1` at the pivot, and let the jumps at the other letters after
the cut be at least `-η`. Let the size conditions hold: `2 b` bounds the shifted far windows
`β + s + W`, `G` the windows of the `J` letters after a thin cut, `n` bounds `G / (p - 1)`, and
`κ` is large against the costs. Let `η ≥ 1`, `V + 4 η ≤ W`, `s i + W ≤ p n`, `l ≤ 2 J + 1`, and let
the cut be of a kind at which the cokernel is killed. Then `S` has a point over `p ^ (25 κ) c` at
which it can rest (a stop): its orders `stopOrders η l` are `max 0 (-u - η)` below the level `l` and
`-u` from `l` on, and its depth `longGapDepth l t (2 b)` is `2 b` at the level `t`, `1` at the
others below `l` and `-u` from `l` on. 

### `ruleBound_le_inf_add_longGapDepth`

 The inequality that makes a move safe at a cut with a long gap. The move has the minimum of the
exponents `cutOrders s η l` and of `cutOrders 0 η l₀` shifted up by `l` levels (`0` below `l`).
The side at rest has the depth `longGapDepth l t r`, where `t < l` and `0 < r`. At the level `a` let
`u ≤ η` if `t ≠ a < l` and `u < η + r` if `a = t`. Then for every `v` the exponent at `u` and the
depth at `v` add up to at least `ruleBound l 0 a (u + v)`, which is `1` for `a < l` and `-(u + v)`
for `a ≥ l`. 

### `exists_mem_pointsOver_ruleBound_le_of_isLongGap`

 Let the side `R`, which moves first to a stop and rests there, have jumps in `[-η, η]` and in
far windows `σ j • [β j, β j + V]`, and let the other side `R'` have those of signs `-σ`. Let
`η ≥ 1`, `V + 4 η ≤ W`, `s i + W ≤ p n`, let the size conditions hold, and let the letter
`l ≤ 2 J + 1` steps before `i` be a cut at which the cokernel is killed, followed by a long gap with
pivot `i.stepBack t` where `σ` is `-1`. Let the far windows at the levels `a ≠ t` below `l` be small
or of the sign opposite to that at the pivot. Then `R` has a point `q` over `p ^ (25 κ) c` with
orders `stopOrders η l` and depth `longGapDepth l t (2 b)` that has this property: `R'` moves from
`φ ^ l` of its standard point at that cut, whose own cut before is any `l₀` letters back, to its
standard point at `i`, so the move has the minimum of the two systems `cutOrders`; at each jump `u`
of `R'` this order and the depth at any `v` add up to at least `ruleBound l 0`. 

### `SidePairing.exists_stop_of_isLongGap`

 Let the sides `S`, `S'`, paired by `h`, have jumps in `[-η, η]` and in opposite far windows
`∓ε j • [β j, β j + V]`. Let the cut `i.stepBack l` have shift `0` and be followed up to `i` by a
long gap: the far window at the pivot `i.stepBack t` starts far out and the others have the opposite
sign or are small. Let `x`, `x'` at `i` and `x₀`, `x₀'` at `i.stepBack l` be points of the two sides
over `p ^ (25 κ) c`, `p ^ (25 κ) c'` with the orders `cutOrders` of standard points at these cuts
and any depths `d`, `d₀`. Let `h_cut` say that the cut is of a kind at which the cokernels of `S`
and `S'` are killed, and `h_kill` that `p ^ κ` kills that of the Tate dual side, with lattice
`Hom(Y ⊗ Y', O(1))`, there. Let the size conditions `CutSizes` hold with `η ≥ 1`, `V + 4 η ≤ W`,
`s i + W ≤ p n` and `l ≤ 2 J + 1`. Then one side has a stop, at which it rests while the other side
moves from `φ ^ l` of its point at `i.stepBack l` to its point at `i`, and this move is safe:
`p ^ κ` times its pairing with all `g • q - q` (`q` the stop) lies in the image of `W(𝔪^♭)`. 

### `SidePairing.exists_stop_of_hasSignBefore`

 Let the paired sides have their jumps at each letter `j` in `[-η, η]` and in opposite far
windows `∓ε j • [β j, β j + V]`. Let `i` be a plain cut: `0 < l`, and the `l` letters after
`i.stepBack l` share the sign `ρ`, up to far windows that end at or below `η`. Let `x`, `x'` at `i`
and `x₀`, `x₀'` at `i.stepBack l` be points of the two sides over `p ^ e c`, `p ^ e c'` with orders
`-u` on each jump `u`, lowered by `η` at the distinguished element `E` (level `0`). Let `x`, `x'`
have the depth `plainDepth s η l η`: `-u`, raised by `s` at the level `0` and by `η` at the levels
up to `l`. Let `p ^ κ * E ^ s` kill the cokernel at `i` of the Tate dual side, with lattice
`Hom(Y ⊗ Y', O(1))`. Then one side has a stop, at which it rests while the other side moves from
`φ ^ l` of its point at `i.stepBack l` to its point at `i`, safely: `p ^ κ` times the pairing of
this move with all `g • q - q` (`q` the stop) lies in the image of `W(𝔪^♭)`. 

### `SidePairing.jumps_le_of_fitsWindows`

 Upper bounds on the jumps of three sides: two paired sides `S`, `S'` and the Tate dual side of
the pairing, with lattice `Hom(Y ⊗ Y', O(1))`, whose jumps are `0` and the `-(u + u') - 1` for jumps
`u` of `S` and `u'` of `S'`. If at the letter `i` the jumps of the paired sides lie in the low
window `[-η, η]` and in opposite far windows `∓ε i • [β i, β i + V]`, and `V + 4 η ≤ W`, then the
jumps of all three sides at `i` are at most `β i + W`. 

### `SidePairing.isScaledCupCoboundary_of_cut_windows`

 The scheme of cuts, a chosen set of letters. Let paired sides have their jumps in the low window
`[-η, η]` and in opposite far windows `∓ε i • [β i, β i + V]`. Suppose that `η ≥ 1`, `V + 4 η ≤ W`,
that the shifts have `s i + W ≤ p n`, and that the size conditions `CutSizes` hold: `2 b` bounds all
`β i + s i + W`, `n` bounds `G / (p - 1)`, `s₀` bounds `(β i + W) / (p - 3)` for `p ≥ 5`, and `κ` is
large against the cost `X` of one of `J + 1` levels and the cost `δ` of the depth `2 b`. Let each
cut `i` be of a kind at which the cokernel is killed (`IsKillingCut`): `s i = 0` and `β + W ≤ G` at
the next `J` letters, or the chart is unramified, `p ≥ 5` and `s₀ - κ ≤ s i < β i`. Let every letter
have a cut at most `2 J + 1` steps back. Suppose also that the letters after the nearest cut share
the sign of some `i.stepBack t`, up to small far windows, or have a long gap with pivot
`i.stepBack t`. Then, for every `e ≥ 51 κ` and `c`, `c'` in the lattices `paramLattice` of the
sides, the cup product of the cocycles of `c` and `p ^ e c'` is a coboundary. 

### `_root_.New.Lift.KummerChart.cutSizes_zero_shift`

 The size conditions `CutSizes` of the scheme of cuts (letters at which the exponent bound is
anchored) with all shifts `0`, for far windows of the jumps that start at `β i ≤ max b W` at each
letter `i`. They ask that the cost `X` of a level dominate `n`, `log_p (2 b)`, `W` and `G`, that
`κ` exceed `12 ((J + 1) X + δ)`, that `β i + W ≤ 2 b`, and that `G`, `β i + W` and `2 e b` be at
most `(p - 1) n`, `(p - 3) s₀` (if `p ≥ 5`) and `p ^ (J + 1) δ`. Let `8 e ≤ p ^ (J + 1)`,
`2 e (b + W) ≤ p ^ (J + 1) δ` and
`4 (J + 1 + d) W + ⌊log_p (2 (b + W))⌋ ≤ X`, where `e = k.e` is the ramification index and
`d = k.differentBound` is `0` if `e = 1` and `v_p(e) + 1` otherwise. Then the conditions hold with
`κ = 12 ((J + 1) X + δ) + 1`, with `b + W` in place of `b`, with `n = G = 2 W` and with
`s₀ = ⌊(b + 2 W) / (p - 3)⌋ + 1`. 

### `_root_.New.Lift.KummerChart.IsUnramified.eight_mul_e_le_sq`

 On an unramified chart the ramification index `k.e` is `1`, so `8 e ≤ p ^ 2` if `p ≥ 3`. 

### `_root_.New.Lift.KummerChart.Letter.hasSignBefore_or_isLongGap`

 Let the far windows `± [β i, β i + V]` start at `b` at the b-letters, or thick letters (those
with `T`), and at `G` at the others, the thin ones, where `η ≥ 1` and `G + V ≤ η`. Among the letters
`i.stepBack r` with `r < l`, let only those with `r = 0` or `r + (J + 1) = l` be possibly thick. Let
the chart be unramified with `p ≥ 7` and `10 p ^ J η ≤ b`, or let the sign `ε` be constant. Then for
some pivot `i.stepBack t` these `l` letters have the sign of the pivot or a far window that ends at
or below `η` (`HasSignBefore`), or there is a long gap among them: the pivot is `J + 1` steps after
`i.stepBack l`, its window starts beyond `s₀ + ω (1 + ⋯ + p ^ J)` and the others have the opposite
sign or small windows (`IsLongGap` with all shifts `0`, `s₀ = ⌊(b + 10 η) / (p - 3)⌋ + 1` and
`ω = η`). 

### `_root_.New.Lift.KummerChart.Letter.exists_hasThinSuccessors_stepBack`

 Suppose that no three letters with `T` follow one another with both gaps between `1` and `J`.
Then one of the `2 J + 1` letters before `i` is followed by `J` letters without `T`. 

### `_root_.New.Lift.KummerChart.Letter.IsNearestCut.eq_zero_or_add_eq_of_hasThinSuccessors`

 Suppose that no three letters with `T` follow one another with both gaps between `1` and `J`.
Let `i.stepBack l` be the nearest letter before `i` that is followed by `J` letters without `T`.
Then a letter `i.stepBack r` with `T` and `r < l` is `i` itself or lies `J + 1` steps after
`i.stepBack l`. 

### `SidePairing.isScaledCupCoboundary_sparse_thick`

 Sparse b-letters. Let the sides `S`, `S'` of a Kummer chart be paired by `h`; each side has
lattices Y and `C = paramLattice`, a map `cocycleMap` from C to the crystalline cocycles of Y, and a
finite set of jumps at each letter. The b-letters, or thick letters, are those with `T i`. At each
b-letter `i`, let each jump of `S` lie in `[-η, η]` or in the far window `-ε i [b, b + V]`, and each
jump of `S'` in `[-η, η]` or in `ε i [b, b + V]`. At the other letters `G` replaces `b`. Here
`η ≥ 1` and `G + V ≤ η`. Suppose that no three b-letters follow one another under Frobenius with
both gaps between `1` and `J ≥ 1`. Suppose also that the chart is unramified with `p ≥ 7` and
`10 p ^ J η ≤ b`, or that the sign `ε` is constant and `8 e ≤ p ^ (J + 1)`. Let
`2 e (b + 5 η) ≤ p ^ (J + 1) δ` and `20 (J + 1 + d) η + ⌊log_p (2 (b + 5 η))⌋ ≤ X`. Here `e = k.e`
is the ramification index, and `d = k.differentBound` is `0` if `e = 1` and `v_p(e) + 1` otherwise.
Then for `c` in `S.paramLattice` and `c'` in `S'.paramLattice`, the cup product of the cocycles
`S.cocycleMap c` and `p ^ (10³ (δ + (J + 1) X)) • S'.cocycleMap c'` is a coboundary
(`IsScaledCupCoboundary`). 

### `_root_.New.Lift.KummerChart.cutSizes_of_isUnramified`

 The size conditions `CutSizes` of the scheme of cuts with `J = 1`, on an unramified chart with
`p ≥ 7`. Here `β i` is the start of the far window of the jumps at the letter `i` and `s i` its
shift, the pole order at `E` allowed if `i` is a cut; let `β i ≤ b` and `s i ≤ ⌊b / p⌋ - 7 K`. Let
`b < K p ^ 2`, `2 G < K p` and `W ≤ K`. Then they hold with the costs
`X = 3 K + ⌊log_p (2 (b + W))⌋` and `δ = 4 K`, with `κ = 12 (2 X + δ) + 1`, `n = K` and
`s₀ = ⌊b / p⌋ + 12 K`, and with `b + W` and `G + W` in place of `b` and `G`. 

### `_root_.New.Lift.KummerChart.Letter.isLongGap_two_zero`

 A long gap of length `2`, on an unramified chart with `p ≥ 7`. Let the far window of the jumps,
of width `V` beside the low window `[-η, η]`, start at `b` at `i`, and at `G` with
`G + 7 K ≤ ⌊b / p⌋` at the letter before `i`, which has the opposite sign; let `s`, the shift, be
`0` at the letter two steps back. If `b < K p ^ 2` and `V + 4 η ≤ W ≤ K`, then the gap is long with
`J = 1`, `s₀ = ⌊b / p⌋ + 12 K` and `ω = G + W`: the windows before `i` end at or below `ω`, and `b`
exceeds `s₀ + ω (1 + p)`. 

### `_root_.New.Lift.KummerChart.Letter.letterFrob_stepBack_succ`

 Frobenius sends the letter `a + 1` steps before `i` to the letter `a` steps before `i`. 

### `_root_.New.Lift.KummerChart.Letter.cut_stepBack_one_or_two`

 Suppose `cut` holds at every letter `i` with `T i` and at every letter `i` with
`¬T (k.letterFrob i)`, where `k.letterFrob` sends a letter `x` to `x ^ p`. Then `cut (i.stepBack 1)`
or `cut (i.stepBack 2)` holds, that is, `cut` holds at one of the two letters before `i`. 

### `_root_.New.Lift.KummerChart.Letter.IsNearestCut.hasSignBefore_or_isLongGap_of_two_sizes`

 On an unramified chart with `p ≥ 7`, let the far windows start at `b` at the b-letters (those
with `T`) and at `G` at the others, the thin ones. Let the shifts be at most `⌊b / p⌋ - 7 K`, and
`0` at the letters with a thin successor, where `0 < G`, `b < K p ^ 2` and `V + 4 η ≤ W ≤ K`. The
cuts are the letters whose shift is less than the start of their far window; let the b-letters and
the letters with a thin successor be cuts. If `i.stepBack l` is the nearest cut before `i`, then
each of the `l` letters after it has the sign of `i` or a far window that ends at or below `η`
(`HasSignBefore`), or there is a long gap with pivot `i` (pivot index `0`): its window starts beyond
`s₀ + ω (1 + p)`, for `s₀ = ⌊b / p⌋ + 12 K` and `ω = G + W`, and the letter before has the opposite
sign. 

### `SidePairing.isScaledCupCoboundary_any_pattern`

 Let the Kummer chart `k` over `Γ` be unramified, and let the fixed prime `p` be at least `7`.
Let the sides `S`, `S'`, paired by `h`, have their jumps at each letter `i` in `[-η, η]` and in
opposite far windows of signs `∓ε i` and width `V`, which start at `b` at the b-letters (those with
`T i`) and at `G` at the others, where `0 < G ≤ b`, `η ≥ 1` and `V + 4 η ≤ W`. If `b < K p ^ 2`,
`2 G < K p` and `W ≤ K`, then the cup product of the cocycles `S.cocycleMap c` and `p ^ (10⁴
(K + ⌊log_p (2 (b + W))⌋)) • S'.cocycleMap c'` is a coboundary. 
