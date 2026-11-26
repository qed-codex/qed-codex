---
{
  "module": "src/New/Congruences/Lifting/FewLowJumps.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Lifting/FewLowJumps.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Lifting/FewLowJumps.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Few low jumps: length lost to depth and a submodule cupping to zero

For a side `S` (`New.Lift.KummerChart.PairingSide`), orders and depths are functions `o l u` of a
level `l` and a line `u`. The level `0` belongs to the prime `E` of the chart `k`.
`New.relLength S T` is the length of `S / (S ⊓ T)`. A point `x` of the extension lies in
`S.deepElements i c` if it lies over a constant at `i` and has the depth `c`: the differences
`g • x - x` have exponents `c` for all `g` in the subgroup `Γ'` of the chart. On an unramified
chart, this file bounds the length lost when the depth is raised, for a side with few jumps in the
low window. It concludes that most constants have deep points above them, and that these constants
satisfy the cup conditions with exponent `0`.

## Main definitions and results

* `New.Lift.KummerChart.PairingSide.deepConstants`: the constants below the points of the extension
  with a given pole order and depth.
* `New.Lift.KummerChart.PairingSide.exists_relLength_le_and_isScaledCupCoboundary`: the submodule of
  bounded colength that cups to zero.

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

See `New.Congruences.Lifting.CutExponentBounds` and `New.Congruences.Lifting.CupOrthogonalityBounds`
for related work.


### `deepConstants`

 The constants below the points of the extension with a pole of order at most `-t` and depth `c`
at the letter `i`: the image under `S.localizedProjTrivial` of the elements of `S.deepElements i c`
that lie in the Kisin part with exponents `raisedOrdersAtZero t` (`t - u` at the level `0`, `-u`
beyond). 

### `negativeWindowDepth`

 The depth used at a letter whose far window `-[b, b + W]` is negative, as a function of the
level `l` and the line `u`: the constant `b + W + a + η` at the level `0`, `W + 1 - u` at the level
`1` (plus `2a` on the low lines `|u| ≤ η`), and `-u` beyond. 

### `fewLowJumpsDepth`

 The depth used at a letter whose far window is `ε [b, b + W]`: it is
`raisedOrdersAtZero (2a + η)` if `ε = 1` and `negativeWindowDepth a η W b` if `ε = -1`. 

### `mem_locKisinPart_kerWithOrders_iff`

 A point lies in the Kisin part of `S.kerWithOrders i c` if and only if it has the exponents
`c` at the letter `i` and lies over `0`. 

### `mem_deepElements_iff_mem_range_and_invariantsMod`

 A point `x` of `S.extensionLattice.kisinLoc` lies in `S.deepElements i c` if and only if two
things hold. First, `S.localizedProjTrivial x` lies in the range of `S.constantAt i`. Second, `x`
lies in `invariantsMod (S.extensionLattice.withOrders i c)`: for every `g` in `Γ'`, `g x - x` has
orders `c` at the letter `i`. 

### `natCast_dvd_frobE_zero_pow_sub_frobE`

 On an unramified chart, where `E = z + p`, the element `φ ^ a E` is congruent to `E ^ p ^ a`
modulo `p`. 

### `exists_isOperatorOfCost_zero_mem_deepElements`

 Let `S` be a side on an unramified chart and `i` a letter, and suppose that no multiple of `p`
lies strictly between `c 0 v` and `c 0 v + N` for any `v`. Then some operator `A` of cost `0` on the
points of the extension (one with `A w - w` over the constant `0` and with orders `o` whenever `w`
has depth `o`) takes `S.deepElements i` for `c` raised by `1` at the level `0`, that is the
elements over constants at `i` of this depth, into those for `c` raised by `N` at the level `0`. 

### `exists_sub_mem_deepElements_of_smul_sub_mem`

 Division by `p`. Suppose the chart is unramified, and no multiple of `p` lies strictly between
`c 0 v` and `c 0 v + p ^ a` for any `v`. Let `x` have depth `c`, and let `w` lie over `0` with
orders `c` raised by `1` at the level `0`. If `p • x - w` has the depth `raiseOrder c a u` (`c` with
the value `c a u` raised by `1`), then so has `x - m` for some `m` over `0` with orders `c`. 

### `exists_isOperatorOfCost_mem_deepElements_raiseOrder`

 There is an operator `A` on `S.extensionLattice.kisinLoc` whose cost is `k.cost a (c a u)`, the
cost of the step `(a, c a u)`. It maps `S.deepElements i c` into
`S.deepElements i (raiseOrder c a u)`, so it improves the depth from `c` to `raiseOrder c a u`,
which is `c` with the value `c a u` raised by `1`. 

### `exists_sum_smul_sub_mem_deepElements`

 A primitive relation for one step. Let `S` be a side on an unramified chart `k` and `i` a
letter. Let `c a u < c a v` for the jumps `v < u` at `i.stepBack a`, and let no multiple of `p` lie
strictly between `c 0 v` and `c 0 v + p ^ a`. Take one more point `x j` of depth `c` than the
residue degree `k.f` times the multiplicity of the jump `u` there, such that each `p • x j` is the
sum of an element of depth `raiseOrder c a u` and one over `0` with orders `c`. Then a combination
of the `x j` with one coefficient equal to `1` is such a sum as well. 

### `relLength_deepConstants_raiseOrder_le`

 One step. Let `S` be a side on an unramified chart `k`, `i` a letter, and
`S.deepConstants i 0 c` the constants at `i` below elements of the extension without pole and of
depth `c`. Let `c l v ≥ -v` for the jumps `v` at `i.stepBack l`, let `c a u < c a v` for the jumps
`v < u` at `i.stepBack a`, and let no multiple of `p` lie strictly between `c 0 v` and
`c 0 v + p ^ a`. Raising `c a u` by `1` shrinks these constants by a module whose length
(`relLength`) is at most the cost `k.cost a (c a u) = v_p(c a u) + 3 a` of the step times the
residue degree `k.f` times the multiplicity of the jump `u` at `i.stepBack a`. 

### `sigma_Ico_raiseOrder`

 Raising `c a u` by `1` removes the step `⟨u, c a u⟩` from the steps `⟨v, n⟩` with `v ∈ U` and
`c a v ≤ n < d v`. 

### `relLength_deepConstants_le_sum_cost`

 All steps at one level. Let `S` be a side on an unramified chart `k`, `i` a letter, and
`S.deepConstants i 0 c` the constants at `i` below elements of the extension without pole and of
depth `c`. Suppose no multiple of `p` lies strictly between `c 0 v` and `c 0 v + p ^ a`,
`c l u ≥ -u` on the jumps `u ∈ S.jumpSet (i.stepBack l)`, and `c' ≤ c` there for `l ≠ a`. If `c' a`
is antitone on the jumps at `i.stepBack a`, then the quotient of these constants by those of depth
`c'` has length at most the sum, over the steps `⟨u, n⟩` with `c a u ≤ n < c' a u`, of the cost
`k.cost a n = v_p(n) + 3 a` times the residue degree `k.f` times the multiplicity of the jump
`u`. 

### `relLength_deepConstants_le`

 Raising the depth at one level `a` costs bounded length. Let `S` be a side on an unramified
chart `k`, `i` a letter, and `S.deepConstants i 0 c` the constants at `i` below elements of the
extension without pole and of depth `c`. Let `n j` and `r j` bound the residue degree `k.f` times
the numbers of jumps at `j` in `[-η, η]` and of all jumps, counted with multiplicity. Suppose no
multiple of `p` lies strictly between `c 0 v` and `c 0 v + p ^ a`, that `c l u ≥ -u` on the jumps at
`i.stepBack l`, and that `c' ≤ c` there for `l ≠ a`. If `c' a` is antitone on the jumps at
`i.stepBack a`, and the costs `k.cost a y = v_p(y) + 3 a` of the steps `c a u ≤ y < c' a u` add up
to at most `costAll` (plus `costLow` when `|u| ≤ η`), then the quotient of the constants of depth
`c` by those of depth `c'` has length at most
`costAll * r (i.stepBack a) + costLow * n (i.stepBack a)`. 

### `pointsOver_raisedOrdersAtZero_nonempty`

 Let the chart `k` be unramified, `p ≥ 5`, and let `p` divide no nonzero integer within
`6 (a + η + W)` of `0` or `± b j`, for every letter `j`. Let `X` be a side over the coefficients
`O`, all of whose jumps, the elements of its sets `X.jumpSet j`, are at most `(p - 3) (κ + s)`, so
that `p ^ κ * E ^ s` kills its cokernels (`E = z + p`). Let the integers in `[-s - u, t - u)` lie
within `6 (a + η + W)` of `0` or `± b i` for the jumps `u` at the letter `i`. Then `X` has an
element of the extension over `p ^ κ • x` at `i` of depth `raisedOrdersAtZero t`, that is, its
differences with its translates by the group of the chart have order `t - u` at the level `0` and
`-u` above on the line of the jump `u`. Its own orders are `t - u` at the level `0` if `u < -s`,
else `min (t - u) 0`, and `-u` above. 

### `pointsOver_raisedOrdersAtZero_nonempty_of_fitsWindows`

 Let `S` be a side on an unramified chart `k` and `p ≥ 5`; at every letter `j` let
`b j + W + η ≤ (p - 3) a`, let `p` divide no nonzero integer within `6 (a + η + W)` of `0` or
`± b j`, and let the jumps lie in `[-η, η]` or in `ε j • [b j, b j + W]`. Then there is an element
of the extension over `p ^ s • d` at the letter `i` of depth `raisedOrdersAtZero (2a + η)`: its
differences with its translates by the group of the chart have order `2a + η - u` at the level `0`
and `-u` above on the line of the jump `u`. With `a - s` taken in `ℕ`, its own orders are
`2a + η - u` at the level `0` if `u < -(a - s)`, else `min (2a + η - u) 0`, and `-u` above. 

### `pow_smul_constantAt_mem_deepConstants`

 Let `S` be a side on an unramified chart `k` and `p ≥ 5`; at every letter `j` let
`b j + W + η ≤ (p - 3) a` and `6 (a + η + W) < b j`, let `p` divide no nonzero integer within
`6 (a + η + W)` of `0` or `± b j`, and let the jumps of `S` lie in `[-η, η]` or in
`ε j • [b j, b j + W]`. Write `raisedOrdersAtZero t` for the orders that on the line of a jump `u`
are `t - u` at the level `0` and `-u` above. With `a - s` taken in `ℕ`, a point with orders
`raisedOrdersAtZero (-(a - s))` and depth `raisedOrdersAtZero (2a + η)` has the improved orders:
`2a + η - u` at the level `0` if `u < -(a - s)`, else `min (2a + η - u) 0`, and `-u` above. If
`raisedOrdersAtZero t` is at most these on the jumps, then `p ^ s` times the letter-`i` part
`S.constantAt i d` of `1 ⊗ d` lies in `S.deepConstants i t`: below an element of the extension with
orders `raisedOrdersAtZero t` and depth `raisedOrdersAtZero (2a + η)`. 

### `relLength_deepConstants_add_one_le`

 Lowering the pole order by one. Let `S` be a side on an unramified chart `k`, `i` a letter,
`t < 0` and `t < s`. `S.deepConstants i t o` consists of the constants at `i` below elements of the
extension with orders `raisedOrdersAtZero t` and depth `o`. Suppose that `p ^ a` times every
constant at `i` lies in this module for `t + 1` and the depth `raisedOrdersAtZero s`. Then its
quotient from `t` to `t + 1` has length (`relLength`) at most `a` times the residue degree `k.f`
times the multiplicity of the jump `t` at `i`. 

### `relLength_constantAt_range_deepConstants_le`

 Removing the pole. Let `S` be a side on an unramified chart `k` and `p ≥ 5`; at every letter `j`
let `b j + W + η ≤ (p - 3) a` and `6 (a + η + W) < b j`, let `p` divide no nonzero integer within
`6 (a + η + W)` of `0` or `± b j`, let the jumps of `S` lie in `[-η, η]` or in
`ε j • [b j, b j + W]`, and let `n j` bound the residue degree `k.f` times the number of jumps in
`[-η, η]`, counted with multiplicity. The constants at the letter `i` are the letter-`i` parts
`S.constantAt i d` of `1 ⊗ d`. Their quotient by those that lie below elements of the extension
without pole (orders `-u` on each jump line `u`) and of depth `raisedOrdersAtZero (2a + η)` has
length at most `a * n i`. 

### `sum_cost_zero_eq_padicValNat_factorial`

 In the unramified chart the steps `0, …, N` at the level `0` together cost `v_p(N!)`. Here the
cost of a step `n` at the level `0` is `v_p(n) + k.differentBound`. 

### `sum_cost_zero_le`

 In the unramified chart the steps `0, …, N` at the level `0` together cost at most `m` if
`N ≤ (p - 1) m`, by Legendre's formula. 

### `sum_cost_zero_Ico_multiple_le`

 Let the Kummer chart `k` of the prime `p ≥ 5` be unramified, so that the cost `k.cost 0 y` of
the step `y` at the level `0` is `v_p(y)`, with `v_p(0) = 0`. Let `β + W + η ≤ (p - 3) a`, let `p`
divide no nonzero integer within `6 (a + η + W)` of `0` or `± β`, and let `t` be the least multiple
of `p` that is at least `β + W + a + η`. For `u` in `[-η, η]` or in `-[β, β + W]`, the steps `y`
with `2a + η - u ≤ y < t` cost at most `a + 1` together, and nothing if `u` is not in
`[-η, η]`. 

### `sum_cost_one_Ico_negativeWindowDepth_le`

 Let the Kummer chart `k` be unramified, so that the cost `k.cost 1 y` of the step `y` at the
level `1` is `v_p(y) + 3`. Let `6 (a + η + W) < β`, let `p` divide no nonzero integer within
`6 (a + η + W)` of `0` or `± β`, and let `u` lie in `[-η, η]` or in `σ • [β, β + W]`. The depth
`negativeWindowDepth a η W β' 1 u` is `W + 1 - u`, plus `2a` if `|u| ≤ η`; the window start `β'`
enters this function only at the level `0`, so it is arbitrary here. The steps `y ≥ -u` below this
depth cost at most `3 (W + 1)`, plus `6a` if `|u| ≤ η`. 

### `relLength_deepConstants_negativeWindowDepth_le`

 Let `S` be a side on an unramified Kummer chart `k` and `p ≥ 5`. At every letter `j` let
`b j + W + η ≤ (p - 3) a` and `6 (a + η + W) < b j`, let `p` divide no nonzero integer within
`6 (a + η + W)` of `0` or `± b j`, let the jumps of `S` lie in `[-η, η]` or in
`ε j • [b j, b j + W]`, and let `n j` and `r j` bound the residue degree `k.f` times the numbers of
low jumps and of all jumps, counted with multiplicity. Let `ε i = -1` and let `m = i.stepBack 1` be
the previous letter. `S.deepConstants i 0 o` consists of the constants at `i` below elements of the
extension without pole (orders `-u` on the line of each jump `u`) and of depth `o`. The depth
`raisedOrdersAtZero (2a + η)` is `2a + η - u` at the level `0` and `-u` above; the depth
`negativeWindowDepth a η W (b i)` is `b i + W + a + η` at the level `0`, `W + 1 - u` (plus `2a` if
`|u| ≤ η`) at the level `1`, and `-u` above. The quotient of the constants for the first depth by
those for the second has length at most `(a + 1) n i + 3 (W + 1) r m + 6a n m`. 

### `relLength_constantAt_deepConstants_le`

 Let `S` be a side on an unramified Kummer chart `k` and `p ≥ 5`. At every letter `j` let
`b j + W + η ≤ (p - 3) a` and `6 (a + η + W) < b j`, let `p` divide no nonzero integer within
`6 (a + η + W)` of `0` or `± b j`, let the jumps of `S` lie in `[-η, η]` or in
`ε j • [b j, b j + W]`, and let `n j` and `r j` bound the residue degree `k.f` times the numbers of
low jumps and of all jumps, counted with multiplicity. The constants at the letter `i` are the
letter-`i` parts `S.constantAt i d` of `1 ⊗ d` for `d` in `S.paramLattice`. Their quotient by those
that lie below an element of the extension without pole whose differences with its translates by the
group of the chart have orders `fewLowJumpsDepth a η W (b i) (ε i)` has length at most
`(2a + 1) n i + 3 (W + 1) r m + 6a n m`, where `m = i.stepBack 1` is the previous letter. 

### `tateDualSide_jump_near`

 Let the jumps of `T` and `S` at a letter `i` lie in `[-η, η]` or in far windows `∓σ [β, β + W]`
of opposite signs. Then each jump `u` of the Tate dual side of a pairing of `T` and `S` lies near
`0`, `β` or `-β`: such a jump is `0` or `-(v + w) - 1` for jumps `v` of `T` and `w` of `S`. 

### `tateDualSide_jump_le`

 Let `b j + W + η ≤ (p - 3) a` and `6 (a + η + W) < b j` at every letter `j`. If the jumps of the
paired sides `T` and `S` lie in `[-η, η]` or in far windows `∓ε j [b j, b j + W]` of opposite signs,
then the jumps of the Tate dual side are at most `(p - 3) a`. 

### `improvedOrders_add_negativeWindowDepth_one_pos`

 The inequality for a safe move at the level `1`. Let `6 (a + η + W) < β`, let the jump `u` of
the moving side lie in `[-η, η]` or in `-σ • [β, β + W]`, and the jump `v` of the resting side in
`[-η, η]` or in `σ • [β, β + W]`; then `-u - v - 1` is the jump of the Tate dual side that pairs
with them. Write `e t w` for `improvedOrders (raisedOrdersAtZero (-a)) (raisedOrdersAtZero t) 0 w`,
which is `t - w` if `w < -a` and `min (t - w) 0` otherwise. The sum of the orders `e a (-u - v - 1)`
of the dual point and `min (-u) (e (2a + η) u)` of the move and of the depth
`negativeWindowDepth a η W β' 1 v` of the resting point is positive. 

### `isSafeMoveFst_of_negativeWindowDepth`

 Let the chart `k` be unramified, `p ≥ 5` and `η ≥ 1`; at every letter `j` let
`b j + W + η ≤ (p - 3) a` and `6 (a + η + W) < b j`, let `p` divide no nonzero integer within
`6 (a + η + W)` of `0` or `± b j`, and let the jumps of the paired sides `S` and `T` lie in
`[-η, η]` or in the opposite far windows `± ε j • [b j, b j + W]`. Let `x₀` and `x` be points of `T`
over `c` at the letter before `i` and at `i`, of depth `raisedOrdersAtZero (2a + η)`. At the level
`0` their own orders are `2a + η - u` if `u < -a`, else `min (2a + η - u) 0`, and `-u` above. Let
`x'` be a point of `S` over `d` at `i` with any orders `o'` and depth
`negativeWindowDepth a η W (b i)`: `b i + W + a + η` at the level `0`, `W + 1 - u` (plus `2a` if
`|u| ≤ η`) at the level `1`, and `-u` above. Then the move by `φ x₀ - x`, with `φ` the Frobenius, is
safe with `x'` at rest: for every `g` in the group `k.galMonoid` of the chart, `P` pairs the
components in the lattices of `T` and `S` of `φ x₀ - x` and `g • x' - x'` into the image of
`W(𝔪^♭)`, the Witt vectors of the maximal ideal of the tilt. 

### `relLength_iInf_comap_deepConstants_le`

 Let `S` be a side on an unramified chart `k` and `p ≥ 5`. At every letter `i` let
`b i + W + η ≤ (p - 3) a` and `6 (a + η + W) < b i`, let `p` divide no nonzero integer within
`6 (a + η + W)` of `0` or `± b i`, let the jumps lie in `[-η, η]` or in `ε i • [b i, b i + W]`, and
let `n i` and `r i` bound the residue degree `k.f` times the numbers of low jumps and of all jumps,
counted with multiplicity. Take the `d` in `S.paramLattice` such that at every letter `i` the
letter-`i` part `S.constantAt i d` of `1 ⊗ d` lies below an element of the extension without pole
whose differences with its translates by the group of the chart have the orders
`fewLowJumpsDepth a η W (b i) (ε i)`. They form a `ℤ_[p]`-submodule of `S.paramLattice` with
quotient of length at most `11 ∑ i, (n i (a + 1) + r i (W + 1))`. 

### `exists_relLength_le_and_isScaledCupCoboundary`

 Scaled cup coboundaries for few low jumps. Let `k` be an unramified Kummer chart with constants
`W(𝔽_{p ^ k.f})`, whose letters are the units of `𝔽_{p ^ k.f}`, and let `p ≥ 5` and `η ≥ 1`. Let
`S` be a side over the coefficients `O`: a Galois lattice `Y`, a linear map `S.cocycleMap` from a
lattice `S.paramLattice` to the crystalline cocycles of `Y`, and sets `S.jumpSet i` that contain the
Hodge–Tate jumps of `Y` at the letters `i`. Suppose that at every letter `i`
* `b i + W + η ≤ (p - 3) a` and `6 (a + η + W) < b i`;
* `p` divides no nonzero integer within `6 (a + η + W)` of `0`, `b i` or `-b i`;
* `S.jumpSet i` lies in the union of the low window `[-η, η]` and the far window
`ε i • [b i, b i + W]`;
* `n i` and `r i` bound `k.f` times the number of jumps of `Y` at `i` in `[-η, η]` and in
`S.jumpSet i`, counted with multiplicity.

Then there is a `ℤ_[p]`-submodule `V` of `S.paramLattice` such that `S.paramLattice / V` has length
at most `11 ∑ i, (n i (a + 1) + r i (W + 1))`, and `V` cups to zero. That is, let `T` be a second
side with each `T.jumpSet i` in the union of `[-η, η]` and the opposite far window
`-ε i • [b i, b i + W]`, and let `P` be a pairing of the lattices of `T` and `S`. For `c` in
`T.paramLattice` and `d` in `V`, the cup product under `P` of the cocycles `T.cocycleMap c` and
`S.cocycleMap d` is the coboundary of a continuous cochain, for every topology on `Γ` that makes
the map to `G_p` an open embedding: this is `P.IsScaledCupCoboundary 0 c d`, the exponent `0`
saying that `S.cocycleMap d` need not be multiplied by a power of `p`. 
