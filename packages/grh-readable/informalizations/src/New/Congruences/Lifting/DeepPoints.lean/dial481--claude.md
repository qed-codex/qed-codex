---
{
  "module": "src/New/Congruences/Lifting/DeepPoints.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Lifting/DeepPoints.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Lifting/DeepPoints.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Deep points and scaled cup coboundaries for a gap below zero or nonpositive jumps

A side `S` (`New.Lift.KummerChart.PairingSide`) has sets `S.jumpSet i` that hold the jumps at
each letter `i`. `S.pointsOver c i κ lo o` is the set of points over `p ^ κ c` at the letter `i`,
with orders `lo` and depth `o`. The steps from a depth `o` to a depth `o'` are the integers `y`
with `o l u ≤ y < o' l u`, each taken at its level `l`. The level `0` belongs to the prime `E` of
the chart `k`, and `d = k.differentBound`. This file raises the depth of points when all steps
occur at the level `0`, and bounds the cost of this with `New.Lift.KummerChart.cost`. It deduces
the cup conditions for paired sides in two cases: when no jump lies in `[-a, 0)`, and when the
chart is unramified and all jumps of the second side lie in `[-η, 0]`.

## Main definitions and results

* `New.Lift.KummerChart.PairingSide.pointsOver_nonempty_of_noMultipleNear`: the depth can be raised
  at a cost of `p ^ ((8 n + 4) d)`. This needs every step to occur at `E` and within distance `n` of
  `0`, `b` or `-b`, and `p` to divide no nonzero integer within `n` of these.
* `New.Lift.KummerChart.PairingSide.SidePairing.isScaledCupCoboundary_of_gap`,
  `New.Lift.KummerChart.PairingSide.SidePairing.isScaledCupCoboundary_of_jumps_nonpos`: the cup
  conditions when no jump lies in `[-a, 0)`, and when all jumps of `S'` lie in `[-η, 0]`.
* `New.Lift.KummerChart.PairingSide.SidePairing.isScaledCupCoboundary_of_killsCokernel`: paired
  sides satisfy the cup conditions with exponent `H` when `3 (κ + (48 (a + η + W) + 4) d) ≤ H`. The
  hypotheses are these. The cokernels are killed. The jumps lie in opposite windows. At every `i`,
  `p` divides no nonzero integer within `6 (a + η + W)` of `0`, `b i` or `-b i`. Either no jump lies
  in `[-a, 0)`, or the chart is unramified and all jumps of `S'` lie in `[-η, 0]`.

Notions from other files:
* `New.Lift.KummerChart`: a Kummer chart `k` of the group `Γ` over `G_p`: a ring `Λ⟦z⟧` inside
  `A_inf` with a distinguished element `E` (`E = z + p` if the chart is unramified) and a subgroup
  `Γ'` of `Γ` of index prime to `p`. Its letters are the units of the residue field
  `𝔽_{p ^ k.f}`; a letter singles out embeddings of the coefficients, and `i.stepBack l` is the
  letter `l` steps of Frobenius before `i`.
* `New.Lift.KummerChart.PairingSide`: one side of a pairing: lattices `Y` and `paramLattice`, an
  `O`-linear map `cocycleMap` from `paramLattice` to the crystalline cocycles `Z_f(Y)`, and for each
  letter a finite set of integers that contains `0`. `S.extensionLattice` is the extension of the
  trivial lattice `paramLattice` by `Y` given by the cocycles of `S`, with the jump sets of `S`.
* Orders `o l u` prescribe, for every level `l` and jump `u` at `i.stepBack l`, a power of the
  uniformiser of `B_dR⁺` that divides the value of an element on the line `u` at the level `l`. An
  element has depth `o` if its differences with its translates by `Γ'` have orders `o`.
* `New.Lift.KummerChart.cost`: the cost `k.cost l n = v_p(n) + d + 3 l` of the step `n` at the level
  `l`, with `v_p(0) = 0`; here `d = 0` if the index `e` of the chart is `1`, and `d = v_p(e) + 1`
  otherwise.
* `New.Lift.KummerChart.PairingSide.KillsCokernel`: `p ^ κ * E ^ a` kills the cokernel at the letter
  `i`: it multiplies the letter-`i` part of `A_inf ⊗ C` into the image of the extension's module of
  standard exponents of level `0`.
* `New.Lift.FitsWindows`: `FitsWindows η ε b W U` says that `U` lies in the union of the low window
  `[-η, η]` and the far window `ε • [b, b + W]`.
* `New.Lift.Pairing.IsScaledCupCoboundary`: the cup conditions with exponent `H` for `c` and `c'`:
  the cup product of the cocycles `S.cocycleMap c` and `p ^ H • S'.cocycleMap c'` is a continuous
  coboundary.

## Relation to the literature

See `New.Congruences.Lifting.FewLowJumps` for related work.


### `sum_cost_le_of_noMultipleNear`

 Let `p` divide no nonzero integer within `n` of `0`, `b` or `-b`. For a Kummer chart `k`, the
cost of the step `y` at the level `0` is `k.cost 0 y = v_p(y) + k.differentBound`. These costs over
the integers within `n` of `0`, `b` or `-b` add up to at most `(8 n + 4) k.differentBound`. 

### `mem_twoWindows_union_iff`

 The integers within `n` of `0`, `b` or `-b`, described by inequalities. 

### `pointsOver_nonempty_of_steps_level_zero`

 Deepening at the level `0`. Let the side `S` have a point over `p ^ κ • c` at the letter `i`
with exponents `lo` and depth `o`. If all steps `y` from `o` to the depth `o'` are at the level `0`
and lie in a set `steps` of total cost at most `stepCost`, then `S` has a point over
`p ^ (κ + stepCost) • c` at `i` with depth `o'` and exponents `improvedOrders lo o'` (that is, `o'`
where `lo` is positive and `min o' 0` elsewhere). 

### `pointsOver_nonempty_of_noMultipleNear`

 Deepening under the gap condition. Let `p` divide no nonzero integer within `n` of `0`, `b` or
`-b`. A point of the side `S` over `p ^ κ • c` at the letter `i` is an element of the extension that
the cocycles of `S` define, mapping to `p ^ κ` times the letter-`i` part of `1 ⊗ c`. Its orders `lo`
and its depth `o` prescribe, at each level `l` and each jump `u ∈ S.jumpSet (i.stepBack l)`, the
orders of the values of the element, and of its differences with its translates by the group of the
chart. Given such a point, suppose that all steps `y` with `o l u ≤ y < o' l u` are at the level `0`
and within `n` of `0`, `b` or `-b`. Then there is a point over
`p ^ (κ + (8 n + 4) k.differentBound) • c` at `i` with depth `o'` and orders
`improvedOrders lo o'`. 

### `pointsOver_nonempty_of_gap`

 Deep points under a gap below `0`. Let `p ^ κ * E ^ a` kill the cokernel of the side `S` at the
letter `i`. Let no jump lie in `[-a, 0)`, and let the set `steps` contain `[-u - a, a + η - u)` for
every jump `u` at `i`, with sum of the costs `k.cost 0 y = v_p(y) + k.differentBound` at most
`stepCost`. Then `S` has a point over `p ^ (κ + stepCost) • c` at `i` without pole and of depth
`plainDepth a η 1 0`, which is `a + η - u` at the level `0` and `-u` at the levels above. 

### `SidePairing.isScaledCupCoboundary_of_gap`

 The scaled cup coboundary under a gap below `0`. Let `P` be a pairing of the lattices of the
sides `S` and `S'`, and `P.tateDualSide` the side on the Tate dual of their tensor product that
carries the pairing. Here a side is a lattice with a family of crystalline cocycles and, at each
letter `i` of the chart `k` (a unit of its residue field), a finite set `jumpSet i` of integers. At
every letter let `p ^ κ * E ^ a`, with `E` the distinguished element of the chart, kill the
cokernels of `S`, `S'` and `P.tateDualSide`. Let the jumps of `S` lie in `[-η, η]` or in
`-ε i • [b i, b i + W]`, those of `S'` in `[-η, η]` or in `ε i • [b i, b i + W]` for a sign
`ε i = ±1`, none of them in `[-a, 0)`. Let `steps i` contain `[-u - a, a + η - u)` for every jump
`u` at `i`, with sum of the costs `k.cost 0 y = v_p(y) + k.differentBound` at most `stepCost`. Then
for `H ≥ 3 κ + 2 stepCost` the cup product of the cocycles that `S` and `S'` attach to `c` and
`p ^ H • c'` is a continuous coboundary. 

### `pointsOver_nonempty_of_near_steps`

 Free steps. Let the Kummer chart be unramified, let `p` divide no nonzero integer within `n` of
`0`, `β` or `-β`, and let the side `S` have a point over `p ^ κ • c` at the letter `i` with orders
`lo` and depth `o`: an element of the extension over that constant whose values at each level `l`
and jump `u ∈ S.jumpSet (i.stepBack l)` have order at least `lo l u`, and whose differences with its
translates by the group of the chart have order at least `o l u`. If all steps `y` with
`o l u ≤ y < o' l u` are at the level `0` and within `n` of `0`, `β` or `-β`, then `S` has a point
over the same `p ^ κ • c` with depth `o'` and any orders `lo' ≤ improvedOrders lo o'`. 

### `pointsOver_nonempty_of_fitsWindows`

 Let the chart be unramified (`E = z + p`), let `p ^ κ * E ^ a` kill the cokernel of the side
`S` at the letter `i` (it lifts each constant at `i` to the extension with standard orders), and let
the jumps, the elements of `S.jumpSet i`, lie in `[-η, η]` or in `σ • [β, β + W]`. Let `a ≤ t`, and
let `p` divide no nonzero integer within `n ≥ a + t + η + W` of `0` or `± β`. Then `S` has a point
over `p ^ κ • c` at `i` with a pole of order at most `t` (its orders `raisedOrdersAtZero (-t)` are
`-t - u` at the level `0` on the line of a jump `u`) and of depth `plainDepth a t 1 0`, which is
`a + t - u` at the level `0` and `-u` at the levels above. 

### `pointsOver_nonempty_of_jumps_nonpos`

 Let the chart be unramified, let all jumps of the side `S` lie in `[-η, 0]`, and let `p` divide
no nonzero integer within `n ≥ a + t + η` of `0` or `± β`. Then at every letter `i` the side `S` has
a point without pole over the constant `S.constantAt i c` of `c`: on the line of each jump `u` its
orders are `-u` at every level. Its depth, the orders of its differences with its translates by the
group of the chart, is `plainDepth a t 1 0`: this is `a + t - u` at the level `0` and `-u` at the
levels above. 

### `pointsOver_stopOrders_nonempty`

 On an unramified chart let the jumps `u` of the side `S'` lie in `[-η, 0]`, and let `x₀'` be a
point over `c'` at the letter `i.stepBack 1` before `i`, without pole and of depth `a + t - u` at
the level `0`, where `η ≤ t`. Let `p` divide no nonzero integer within `n ≥ a + t + η` of `0` or
`± β`. Then `S'` has a point over `c'` at `i` that can serve as a stop, that is, rest while the
other side of a pairing moves by Frobenius: its orders `stopOrders t 1` are `max 0 (-u - t)` at the
level `0` and `-u` above, and its depth is `a + t - u`, `t - u` and `-u` at the level `0`, the level
`1` and above. 

### `SidePairing.isScaledCupCoboundary_of_jumps_nonpos`

 Let the chart be unramified, let `P` be a pairing of the lattices of the sides `S` and `S'`, and
`P.tateDualSide` the side on the Tate dual of their tensor product that carries the pairing. At
every letter `i` let `p ^ κ * E ^ a`, with `E = z + p` the distinguished element of the chart, kill
the cokernels of `S` and of `P.tateDualSide`, and let `p` divide no nonzero integer within
`6 (a + η + W)` of `0` or `± b i`. Let the jumps of `S` lie in `[-η, η]` or in
`-ε i • [b i, b i + W]` for a sign `ε i = ±1`, and let the jumps of `S'` lie in `[-η, 0]`. Then for
`H ≥ 2 κ` the cup product of the cocycles that `S` and `S'` attach to `c` and `p ^ H • c'` is a
continuous coboundary. 

### `SidePairing.isScaledCupCoboundary_of_killsCokernel`

 Let `P` be a pairing of the lattices of the sides `S` and `S'`, and `P.tateDualSide` the side on
the Tate dual of their tensor product that carries the pairing. At every letter `i` let
`p ^ κ * E ^ a`, with `E` the distinguished element of the chart, kill the cokernels of `S`, `S'`
and `P.tateDualSide`, let `p` divide no nonzero integer within `n = 6 (a + η + W)` of `0` or
`± b i`, and let the jumps of `S` and `S'` lie in `[-η, η]` or in the opposite far windows
`∓ε i • [b i, b i + W]`, where `ε i = ±1`. Suppose that no jump lies in `[-a, 0)`, or that the chart
is unramified and the jumps of `S'` lie in `[-η, 0]`. Then for
`H ≥ 3 (κ + (8 n + 4) k.differentBound)` the cup product of the cocycles of `c` and `p ^ H • c'` is
a continuous coboundary. 
