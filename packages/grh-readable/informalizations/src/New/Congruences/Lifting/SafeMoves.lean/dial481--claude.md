---
{
  "module": "src/New/Congruences/Lifting/SafeMoves.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Lifting/SafeMoves.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Lifting/SafeMoves.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Safe moves and the walk for pairings of sides of a Kummer chart

This file concerns two sides of a Kummer chart with a pairing `P` modulo `p ^ m`. From numerical
conditions on orders it derives safe moves. It then walks along Frobenius orbits to derive the
condition `New.Lift.Pairing.IsScaledCupCoboundary`. It shows that at plain cuts deep enough standard
points are stops, and it sorts jumps in the windows into sides that are down or up.

## Main definitions and results

* `New.Lift.KummerChart.PairingSide.SidePairing.isSafe_of_orders`: for `w`, `y` over `0`, the
  pairs `(z τ w, y)` and `(w, z τ y)` are safe (`New.Lift.Pairing.IsSafe`) if the orders of `w`, `y`
  and a point of the Tate dual side `New.Lift.Pairing.tateDualSide` add up to a positive number.
* `New.Lift.KummerChart.PairingSide.SidePairing.isSafeMoveFst_of_killsCokernel`,
  `New.Lift.KummerChart.PairingSide.SidePairing.isSafeMoveSnd_of_killsCokernel`: the rule. A move is
  safe if a power of `p` times a power of `E` kills the cokernel of the Tate dual side and the
  orders of the move and the depth of the point at rest add up to at least `ruleBound`.
* `New.Lift.KummerChart.PairingSide.SidePairing.isScaledCupCoboundary_of_stops`: the walk. Standard
  points at the cuts are carried along by Frobenius; at each cut one side moves to a stop, rests
  there while the other side moves, and goes on to its own point.
* `New.Lift.KummerChart.PairingSide.SidePairing.exists_mem_stopPoints_isSafeMoveSnd`,
  `New.Lift.KummerChart.PairingSide.SidePairing.exists_mem_stopPoints_isSafeMoveFst`: at a plain
  cut, where one side is down and the other is up, a deep enough standard point is a stop.

Notions from other files:
* `New.Lift.KummerChart.PairingSide`: lattices Y and C with an O-linear map `cocycleMap` from C to
  the crystalline cocycles of Y, and for each letter a finite set of jumps that contains 0.
* `New.Lift.Pairing`: a pairing of Y and L modulo p^m, that is, an O-linear ψ: Y ⊗ L → O(1) with
  gψ − ψ = p^m c(g) for a crystalline cocycle c, and a Z_p-linear f: O → Z_p.
* `New.Lift.KummerChart.PairingSide.pointsOver`: points of the extension over `p ^ e c`, with
  exponents and a depth.
* `New.Lift.KummerChart.PairingSide.stopPoints`: the points over `p ^ e c` with the exponents
  `stopOrders η l` of a stop, where one side rests while the other side moves.
* `New.Lift.KummerChart.PairingSide.ruleBound`: the least sum of the orders of a move and the depth
  of the point at rest that the rule for `l` allows.

## Relation to the literature

Explicit powers of p and of the Eisenstein polynomial kill cokernels of Kisin modules on crystalline
extensions, and Galois operators buy divisibility at known cost. A walk along Frobenius orbits makes
cup products of crystalline classes vanish up to powers of p, and these tools bound the loss above p
in the Selmer bound. Zero cokernel for weights of one sign, cup products via Ext and torsion bounds
by Sen operators are known in the literature. Related work: Čoupek–Gazaki–Marmora, Exactness
property of Breuil–Kisin functors and Bloch–Kato Selmer groups, 2026; Gao–Liu, Integral Sen theory
and integral Hodge filtration, 2024; Chang–Diamond, Extensions of rank one (φ,Γ)-modules and
crystalline representations, 2011.

The file `New.Congruences.Lifting.CutExponentBounds` applies the walk to two choices of cuts.


 ### Safe pairs and the walk 

### `wittPairing_constantAt_and_extensionForm`

 The constant `1` of the Tate dual side of `P` at the letter `i` acts on `S.Ambient` as the
projector to the letter `i`, and the pairing of `n` with `w ⊗ y` by `P.extensionForm`, reduced
modulo `p ^ P.exponent` through `P.toZp`, is the pairing of the product of the projection of `n` and
`w` with `y`. 

### `antitone_shiftedOrders`

 If the orders `o` are antitone in the jump at every level, so is `shiftedOrders l n o`, which is
`n` at the levels below `l` and `o` shifted up by `l` levels from there on. 

### `z_mem_wittOfMaxIdeal`

 The coordinate `k.z` of the chart, a Teichmüller lift that is not a unit, lies in the ideal
`W(𝔪^♭)` of `Ainf`. 

### `z_smul_map_mem_smallPart`

 Reduced modulo `p ^ P.exponent` through `P.toZp` and multiplied by `k.z`, the `Ainf`-span of
`O(1)` falls into the image `smallPart P.exponent` of `W(𝔪^♭)`. 

### `SidePairing.isSafe_of_orders`

 Let `ν` be a point of the Tate dual side `P.tateDualSide` of the pairing `P` over `p ^ κ` at the
letter `i.stepBack l`, `l` steps before `i`, with orders `νOrders`, antitone in the jump, and any
depth (`pointsOver`). Let `w` and `y` be vectors of the two extensions that lie over `0` with orders
`wOrders` and `yOrders` at `i` (`kerWithOrders`). Suppose that at every level `a` and all jumps
`u ∈ S.jumpSet`, `u' ∈ S'.jumpSet` at the letter `a` steps before `i` the order of `φ ^ l • ν` at
`-u - u' - 1` plus `wOrders a u + yOrders a u'` is positive. Then `(z τ w, y)` and `(w, z τ y)` are
safe for `κ`: `p ^ κ` times the pairing of their components in `Y`, `Y'` lies in the image of
`W(𝔪^♭)`, the Witt vectors of the maximal ideal of the tilt. Here `z τ = k.zTauUnit`, for the
coordinate `z` of the chart and `τ = [ε^{1/p}] - 1`. 

### `SidePairing.isSafeMoveFst_of_orders`

 Let `ν` be a point of the Tate dual side `Hom(Y ⊗ Y', O(1))` of the pairing `P`, over `p ^ κ` at
the letter `l` steps before `i`, with orders `νOrders`, antitone in the jump. Let `w` lie over `0`
with orders `wOrders` at `i`, and let `y` be a point of the second side over `p ^ e' c'` at `i`,
with any orders, fixed by `Γ'` modulo orders `yDepth`. If at all jumps `u`, `u'` the order of
`φ ^ l • ν` at `-u - u' - 1` plus `wOrders a u + yDepth a u'` is positive, the move by `w` is safe
with `y` at rest: for all `g` in `Γ'`, `p ^ κ` times the pairing of `w` with `g • y - y` lies in the
image of `W(𝔪^♭)`. 

### `SidePairing.isSafeMoveSnd_of_orders`

 Let `ν` be a point of the Tate dual side `Hom(Y ⊗ Y', O(1))` of the pairing `P`, over `p ^ κ` at
the letter `l` steps before `i`, with orders `νOrders`, antitone in the jump. Let `x` be a point of
the first side over `p ^ e c` at `i`, with any orders, fixed by `Γ'` modulo orders `xDepth`, and let
`y` lie over `0` with orders `yOrders`. If at all jumps `u`, `u'` the order of `φ ^ l • ν` at
`-u - u' - 1` plus `xDepth a u + yOrders a u'` is positive, the move by `y` is safe with `x` at
rest: for all `g` in `Γ'`, `p ^ κ` times the pairing of `g • x - x` with `g • y` lies in the image
of `W(𝔪^♭)`. 

### `eq_ite_add_one_of_isLeast_cut`

 If `l i` is the distance back from each letter `i` to the nearest cut strictly before it, then
`l i` is `1` if the letter one step before `i` is a cut, and one more than the distance from that
letter otherwise. 

### `liesOver_of_mem_pointsOver`

 A point of the side `S` over `p ^ e c` at the letter `i` satisfies `LiesOver`: it is in the
part at `i` and projects to `p ^ e` times the constant of `c`. 

### `liesOver_phi_pow_smul`

 `φ ^ l` carries a point over `p ^ e c` at the letter `l` steps before `i` to a vector at `i`
over `p ^ e c`. 

### `projTrivial_sum_of_liesOver`

 If each `x i` lies at the letter `i` over `p ^ e` times the constant of `c` at `i`, then
`S.projTrivial.wittMap` sends `∑ i, x i` to `p ^ e • DiagTensor.mk 1 c`, as the letter projectors
sum to `1`. 

### `mem_pointsOver_of_le`

 A point over `p ^ e c` with orders `o₁` and depth `d₁` has also the orders `o₂` and the depth
`d₂` if, at all jumps, `o₂` is at most `o₁` and `d₂` is at most `d₁`. 

### `mem_pointsOver_of_exponent_le`

 A point over `p ^ e c` with orders `o₁` and depth `d` has also the orders `o₂`, with the same
depth, if `o₂` is at most `o₁` at all jumps. 

### `mem_pointsOver_raisedOrdersAtZero_of_gap`

 Let `x` lie in `S.pointsOver c i e o d`: a point over `p ^ e` times the constant of `c` at the
letter `i`, with orders `o` and depth `d`. Suppose that at all jumps `u` in `S.jumpSet` at the
letters `a` steps before `i`, `o` is at least `raisedOrdersAtZero (-t)`, and `d` is at least
`raisedOrdersAtZero 0`. The first bound means a pole of order at most `t` at `E`, the Eisenstein
polynomial of the chart: `-u`, lowered by `t` at `a = 0`. If `0 ≤ h₀` and no jump at `i` lies in
`[-t, -h₀)`, then `x` has orders `raisedOrdersAtZero (-h₀)`, a pole of order at most `h₀` at `E`,
with the same depth. 

### `mem_stopPoints_of_le`

 A point over `p ^ e c` whose exponents are at least the exponents `stopOrders η l` of a stop
lies in `stopPoints`, the set of the points with these exponents, whatever its depth. 

### `mem_stopPoints_of_mem_pointsOver`

 A point over `p ^ e c` with the exponents `stopOrders η l` of a stop lies in
`stopPoints`, whatever its depth. 

### `shiftedOrders_raisedOrdersAtZero_add_ruleBound`

 The orders of `φ ^ l` of a point of the Tate dual side with a pole of order `t`, on the line of
jump `-u - u' - 1`, and `ruleBound l t` add up to `1`. With `s = u + u'`, at the levels `a` below,
at and above `l` the first term is `0`, `s + 1 - t`, `s + 1` (`shiftedOrders l 0 o` is `0` below `l`
and `o` shifted up by `l` levels from there on) and the second is `1`, `t - s`, `-s`. 

### `antitone_raisedOrdersAtZero`

 The orders `raisedOrdersAtZero t a u`, which are `t - u` at the level `0` and `-u` above it,
decrease in the jump `u`. 

### `SidePairing.isSafeMoveFst_of_killsCokernel`

 Let `p ^ κ * E ^ t` kill the cokernel of the Tate dual side `Hom(Y ⊗ Y', O(1))` of the pairing
`P` of the sides `S`, `S'` at the letter `l` steps before `i`, `E` being the Eisenstein polynomial
of the chart. Let `y` be a vector over `0` with orders `o` at `i` (`kerWithOrders`) and `x'` a point
of the second side over `p ^ e' c'`, fixed by `Γ'` modulo orders `d'` (its depth). If at all jumps
`u`, `u'` these add up to at least `ruleBound l t`, then the move by `y` is safe with `x'` at rest:
`p ^ κ` times the pairing of `y` and `g • x' - x'` lies in the image of `W(𝔪^♭)` for all `g` in
`Γ'`. 

### `SidePairing.isSafeMoveSnd_of_killsCokernel`

 Let `p ^ κ * E ^ t` kill the cokernel of the Tate dual side `Hom(Y ⊗ Y', O(1))` of the pairing
`P` of the sides `S`, `S'` at the letter `l` steps before `i`, `E` being the Eisenstein polynomial
of the chart. Let `y'` be a vector over `0` with orders `o'` at `i` (`kerWithOrders`) and `x` a
point of the first side over `p ^ e c`, fixed by `Γ'` modulo orders `d` (its depth). If at all jumps
`u`, `u'` these add up to at least `ruleBound l t`, then the move by `y'` is safe with `x` at rest:
`p ^ κ` times the pairing of `g • x - x` and `g • y'` lies in the image of `W(𝔪^♭)` for all `g` in
`Γ'`. 

### `ruleBound_le_inf_add_shiftedOrders`

 The first move of the walk satisfies the rule for `l`: the orders of the move from `φ ^ l` of a
standard point at the cut before to a stop, and the depth of `φ ^ l` of a standard point at rest,
add up to at least `ruleBound l t₀`, on every pair of jumps `u`, `v`. A standard point at the cut
before has depth `standardDepth t₀ η l₀`, and `shiftedOrders l n o` is `n` at the levels below `l`
and `o` shifted up by `l` levels from there on. 

### `ruleBound_zero_le_inf_add_standardDepth`

 The third move of the walk satisfies the rule for `0`: the orders of the move from a stop to a
standard point, and the depth of a standard point at rest, add up to at least `ruleBound 0 t`, on
every pair of jumps `u`, `v`. 

### `SidePairing.exists_isSafePath_of_stop`

 The moves at a cut (a marked letter) `i` whose predecessor among the cuts is `l` steps back, at
`i.stepBack l`; the cut before that is `l₀` steps further back. Let `x₀`, `x₀'` and `x`, `x'` be
standard points at the two cuts, and let `p ^ κ * E ^ t₀`, `p ^ κ * E ^ t` kill the cokernels of the
Tate dual side there. If one side has a stop at which it can rest while the other moves safely, then
for some `w`, `w'` over the same constants (`LiesOver`) four safe moves, of one side with the other
at rest, lead from `(φ ^ l x₀, φ ^ l x₀')` by `(w, φ ^ l x₀')` and `(w, w')` and `(x, w')` to
`(x, x')` (`IsSafePath`). 

### `SidePairing.isSafeMoveSnd_cocycle`

 Let `P` be a pairing of the sides `S`, `S'`, and let `0 < l`. Let `x`, `x'` be standard points
(`standardPoints`) of `S`, `S'` over `p ^ e c`, `p ^ e' c'` at the letter `d` steps before `i`.
Their orders are `-u` on the line of jump `u`, lowered by `η` at the level `0`, and their depth is
`standardDepth t η l`. Let `p ^ κ * E ^ t` kill the cokernel of the Tate dual side `P.tateDualSide`
there (`KillsCokernel`), and let `φ` be the Frobenius. Then for every `g` in `k.galMonoid`,
`P.IsSafeMoveSnd κ` holds: the move of the second side by `g φ ^ d x' - φ ^ d x'` is safe while
`φ ^ d x` is at rest. 

### `isSafePath_refl`

 The path that stays at `(x, x')` is safe: its four moves are zero. 

### `isSafeMoveFst_sum`

 Let `y i` and `x' i` lie in the parts of the letter `i`. If each move of the first side by `y i`
is safe with `x' i` at rest, then so is the move by their sum with the sum of the `x' i` at rest. 

### `isSafeMoveSnd_sum`

 For a pairing `P` of the sides `S`, `S'`, let `x i` and `y' i` lie in `letterPart i`, the parts
of the letter `i`. Suppose each move of the second side by `y' i` is safe with `x i` at rest
(`P.IsSafeMoveSnd κ`). Then the move by the sum of the `y' i` is safe with the sum of the `x i` at
rest. 

### `SidePairing.isScaledCupCoboundary_of_isSafePath`

 Safety is checked letter by letter. Let `S`, `S'` be sides of the chart `k` with pairing `P`. At
each letter `i` let `y i`, `w i`, `x i` lie over `p ^ e` times the constant of `c` at `i`
(`LiesOver`), likewise `y' i`, `w' i`, `x' i` over `p ^ e' c'`, and let `φ` map `∑ x i` and
`∑ x' i` to `∑ y i` and `∑ y' i`. A pair is safe if `p ^ κ` times its pairing lies in the image of
`W(𝔪^♭)`; a move of the first side by `v` with `q'` at rest is safe if the pairs of `v` and
`g • q' - q'` are safe, and one of the second side by `v'` with `q` at rest if those of `g • q - q`
and `g • v'` are. Let the cocycles of `x i` and `x' i` pair safely, and let four safe moves lead
from `(y i, y' i)` by `(w i, y' i)`, `(w i, w' i)` and `(x i, w' i)` to `(x i, x' i)`
(`IsSafePath`). Then the cup product of the cocycles of `c` and `p ^ N c'` is a coboundary
(`IsScaledCupCoboundary`) for `N ≥ e + e' + κ`. 

### `SidePairing.isScaledCupCoboundary_of_stops`

 The walk. Let `S` and `S'` be sides of the Kummer chart `k` over the coefficient ring `O`
(lattices `Y`, `Y'` with crystalline cocycles `S.cocycleMap c`, `S'.cocycleMap c'` indexed by
lattices `C`, `C'`), and let `P` pair `Y` and `Y'` modulo `p ^ P.exponent`. Letters are elements of
`k.Letter`. Some letters are cuts (`cut`); `i.stepBack a` is the letter `a` steps before `i`, `φ` is
the Frobenius and `E` is the Eisenstein polynomial of the chart. Assume:
* `hl_least`: the last cut before each letter `i` lies `l i` steps back.
* `h_kill`: at each cut `i`, `p ^ κ * E ^ t i` kills the cokernel of the Tate dual side
  `P.tateDualSide`, which is `Hom(Y ⊗ Y', O(1))` with the cocycle of `P`: it multiplies the
  constants at `i` into the image of the vectors of the extension with the standard orders of level
  `0`.
* `hx`, `hx'`: at each cut `i`, `x i` and `x' i` are standard points. They lie in the localized
  Kisin modules of the extensions of `C` by `Y` and of `C'` by `Y'`, over `p ^ e c` and `p ^ e' c'`.
  On the line of jump `u` their order is `-u`, lowered by `η` at the level `0`, and their depth is
  `-u`, raised by `t i` at the level `0` and by `η` at the levels below `l i`.
* `h_stop`: at each cut `i` one side has a stop, a point over the same constant with orders
  `stopOrders η (l i)`, which are `max 0 (-u - η)` at the levels below `l i` and `-u` from there on.
  While it rests there, the other side moves safely from `φ ^ l i` of its point at the cut before to
  its point at `i`.

Then for `N ≥ e + e' + κ` the cup product of `S.cocycleMap c` and `p ^ N • S'.cocycleMap c'` under
`P` is the coboundary of a continuous cochain. 

### `SidePairing.isScaledCupCoboundary_of_stops_at_all_letters`

 The walk `isScaledCupCoboundary_of_stops` with a cut at every letter and the same shift `t` at
all of them, for a pairing `P` of the sides `S` and `S'`. At every letter `i`, let `p ^ κ * E ^ t`
kill the cokernel of the Tate dual side, and let `x i`, `x' i` be standard points over `p ^ e c`,
`p ^ e' c'`: their orders on the line of jump `u` are `-u`, lowered by the margin `η` at the level
`0`, and they are fixed by `Γ'` modulo orders `-u`, raised by `t + η` at the level `0`. Let one side
have a stop at `i`, a point over the same constant with orders `stopOrders η 1`, such that, while it
rests there, the other side moves safely to its point at `i` from `φ` of its point at the letter
`i.stepBack 1` before. Then for `N ≥ e + e' + κ` the cup product of `S.cocycleMap c` and
`p ^ N • S'.cocycleMap c'` is the coboundary of a continuous cochain. 

### `forall_mem_U_stepBack_of_lt_one`

 If `Q` holds at the jumps at the letter `i`, it holds at the jumps at `i.stepBack a` for all
`a < 1`, that is, for `a = 0`. 

### `mem_stopPoints_of_down`

 The case where the side `S` is down. Let `x` be a standard point over `p ^ e c` at the letter
`i`: it has orders `raisedOrdersAtZero (-η)` (`-u` on the line of jump `u`, lowered by `η` at the
level `0`) and depth `standardDepth t η l` (`-u`, raised by `t` at `0` and by `η` below `l`).
Suppose `0 < l` and all jumps of `S` (`S.jumpSet`) at the `l` letters up to `i` are at most `η`.
Then `x` lies in `stopPoints`: it has the orders `stopOrders η l`, which are `max 0 (-u - η)` below
`l` and `-u` from there on. 

### `ruleBound_zero_le_inf_add_plainDepth`

 The second move at a plain cut satisfies the rule for `0`: at a jump `u` of the side that is up
(`u ≥ -η` below the level `l`) and any jump `v`, the orders of the move and the depth
`plainDepth t η l η₀` at rest add up to at least `ruleBound 0 t`. 

### `SidePairing.isSafeMoveFst_of_neg_le_jumps`

 Plain cuts, the first side moves. Let `0 < l` and let the jumps of `S` at `i.stepBack a`,
`a < l`, be at least `-η`. Let `x₀` at `i.stepBack l` and `x` at `i` lie in `S.pointsOver` over
`p ^ e` times the constant of `c`. Let them have orders `raisedOrdersAtZero (-η₀)` and
`raisedOrdersAtZero (-η)`: `-u` on the line of jump `u`, lowered by `η₀`, `η` at level `0`. Let
`p ^ κ * E ^ t` kill the cokernel of `P.tateDualSide` at `i` (`KillsCokernel`). Let `q'` in
`S'.pointsOver c' i e'` have any orders `qOrders` and depth `plainDepth t η l η₀`. This means it is
fixed by the subgroup `Γ'` of `k` modulo orders `-u`, raised by `t` at level `0`, by `η` below `l`,
by `η₀` at `l`. Then `P.IsSafeMoveFst κ (φ ^ l • x₀ - x) q'` holds: for all `g` in `Γ'`, `p ^ κ`
times the pairing of this vector with `g • q' - q'` lies in the image of `W(𝔪^♭)`. 

### `SidePairing.isSafeMoveSnd_of_up`

 Plain cuts, the second side moves: the statement with the sides exchanged. Let `0 < l` and let
the jumps of `S'` at `i.stepBack a`, `a < l`, be at least `-η`. Let `x₀'` at `i.stepBack l` and `x'`
at `i` lie in `S'.pointsOver` over `p ^ e'` times the constant of `c'`. Let them have orders
`raisedOrdersAtZero (-η₀)`, `raisedOrdersAtZero (-η)`, with any depths `d₀'`, `d'`. Let
`p ^ κ * E ^ t` kill the cokernel of `P.tateDualSide` at `i` (`KillsCokernel`). Let `q` in
`S.pointsOver c i e` have any orders `qOrders` and depth `plainDepth t η l η₀`. This means it is
fixed by the subgroup `Γ'` of `k` modulo orders `-u`, raised by `t` at level `0`, by `η` below `l`,
by `η₀` at `l`. Then `P.IsSafeMoveSnd κ q (φ ^ l • x₀' - x')` holds: for all `g` in `Γ'`, `p ^ κ`
times the pairing of `g • q - q` with `g` applied to this vector lies in the image of `W(𝔪^♭)`. 

### `mem_standardPoints_of_plainDepth`

 A point with a pole of order at most `η` and the depth `plainDepth t η l η₀` asked at a plain
cut is standard, as this depth is at least `standardDepth t η l`. 

### `SidePairing.exists_mem_stopPoints_isSafeMoveSnd`

 A plain cut: at the `l` letters up to `i` the jumps of the first side are at most `η` (it is
down) and those of the second at least `-η` (it is up). Let `p ^ κ * E ^ t` kill the cokernel of the
Tate dual side at `i` (`E` the Eisenstein polynomial), let `x₀'`, `x'` have poles of order at most
`η₀`, `η` at `E`, and let `x` have a pole of order at most `η` and be fixed by `Γ'` modulo orders
`plainDepth t η l η₀`. Then some stop `q` of the first side can rest while the move by
`φ ^ l x₀' - x'` is safe, `φ` being the Frobenius; `x` is one. 

### `SidePairing.exists_mem_stopPoints_isSafeMoveFst`

 A plain cut: at the `l` letters up to `i` the jumps of the second side are at most `η` (it is
down) and those of the first at least `-η` (it is up). Let `p ^ κ * E ^ t` kill the cokernel of the
Tate dual side at `i` (`E` the Eisenstein polynomial), let `x₀`, `x` have poles of order at most
`η₀`, `η` at `E`, and let `x'` have a pole of order at most `η` and be fixed by `Γ'` modulo orders
`plainDepth t η l η₀`. Then some stop `q'` of the second side can rest while the move by
`φ ^ l x₀ - x` is safe, `φ` being the Frobenius; `x'` is one. 

### `low_or_far_of_fitsWindows`

 A jump `u` of `U` in the windows (`FitsWindows η σ β V`: the low window `[-η, η]` or the far
window `σ [β, β + V]`) is low, or `u` lies in `[β, β + V]`, or `-u` does. 

### `jump_le_of_fitsWindows`

 A side is down, that is, its jumps are at most `η`, at a letter where they lie in the windows
`[-η, η]` and `σ [β, β + V]` and the far window is negative or ends at or below `η`. 

### `neg_le_jump_of_fitsWindows`

 A side is up, that is, its jumps are at least `-η`, at a letter where they lie in the windows
`[-η, η]` and `σ [β, β + V]` and the far window is positive or ends at or below `η` in modulus. 
