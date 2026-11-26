---
{
  "module": "src/New/Congruences/Lifting/SidePoints.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Lifting/SidePoints.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Lifting/SidePoints.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Jump windows, the gap condition and points of the sides of a Kummer chart

This file defines windows of integers in which the jumps of lattices in a Kummer chart are required
to lie. It defines the gap condition that `p` divides no non-zero integer near 0, `b` or `-b`, and
it bounds sums of `p`-adic valuations over two windows. For one side it defines deep elements of
the extension, operators of a given cost and points of the extension over constants, and moves
points by Frobenius. It also defines pairings of sides and the standard points, stops and rule
bound used by the walk.

## Main definitions and results

* `New.Lift.KummerChart.PairingSide.pointsOver`: points of the extension over `p ^ e c`, with
  orders and a depth.
* `New.Lift.KummerChart.PairingSide.pointsOver_nonempty_of_killsCokernel`,
  `New.Lift.KummerChart.PairingSide.pointsOver_nonempty_of_costs`: points exist, and their depth can
  be raised at a cost in powers of `p`.

Notions from other files:
* `New.Lift.KummerChart.Letter`: the letters of a Kummer chart, that is, the multiplicative group of
  the field with p^f elements in O^♭.
* `New.Lift.KummerChart.PairingSide`: lattices Y and C with an O-linear map `cocycleMap` from C to
  the crystalline cocycles of Y, and for each letter a finite set of jumps that contains 0.
* `New.Lift.Pairing`: a pairing of Y and L modulo p^m, that is, an O-linear ψ: Y ⊗ L → O(1) with
  gψ − ψ = p^m c(g) for a crystalline cocycle c, and a Z_p-linear f: O → Z_p.
* `New.Lift.Pairing.IsSafe`: the pair (w, y) is safe for κ if p^κ times the pairing of the first
  components of w and y lies in the image of W(𝔪^♭).

## Relation to the literature

See `New.Congruences.Lifting.SafeMoves` for related work.


 ## Low and far windows of jumps, the gap condition, valuation sums 

### `FitsWindows`

 Every element of `U` lies in the low window `[-η, η]` or in the far window `ε [b, b + W]`, where
`ε` is a sign. 

### `raisedOrdersAtZero`

 The system of orders that is `-u` on the line `u` at every level `a`, raised by `t` at the
level `0`. 

### `twoWindows`

 The integers within distance `n` of `0` or of `c`. 

### `NoMultipleNear`

 The gap condition: `p` divides no nonzero integer within distance `n` of `0`, of `b` or
of `-b`. 

### `NoMultipleNear.eq_zero_of_dvd`

 Under the gap condition, the only multiple of `p` in the windows of radius `n` around `0`,
`b` and `-b` is `0`. 

### `card_filter_dvd_Icc_le`

 Among the integers within `n` of `c` at most `2 n / q + 1` are multiples of `q`. 

### `sum_padicValInt_Icc_le`

 Let `p` be prime, `n ≤ p m` and `|c| + n ≤ H`. The valuations `v_p(k)` of the integers `k`
within `n` of `c` add up to at most `4 m + ⌊log_p H⌋`, with `v_p(0) = 0`. 

### `sum_twoWindows_le`

 Let `p` be prime, `n ≤ p m` and `|c| + n ≤ H`. The sum of `v_p(k) + d` over the integers `k`
within `n` of `0` or of `c` is at most `8 m + 2 ⌊log_p H⌋ + (4 n + 2) d`. 


## Points of a side and safe-move criteria for pairings

A side `S` (`New.Lift.KummerChart.PairingSide`) is a lattice `Y` with crystalline cocycles indexed
by a lattice `C`. These cocycles define the extension `S.extensionLattice` of the trivial lattice
`S.trivialLattice` by `S.kerLattice` (that is, `Y`). All of these are taken over `W(C^♭)` and cut
into letters `i`.

`L.withOrders i o` holds the elements at the letter `i` with orders at least `o a u` (`a` stands for
the prime `φ ^ a E`, `u` is a jump), `i.stepBack a` is the letter `a` steps before `i`, `k.zTauUnit`
is `z τ`, and `k.galMonoid` is the group `Γ'` of the chart.

The invariant forms `L.forms` are the `Ainf`-linear maps `μ` from `W(C^♭) ⊗ L` to `BdR` that are
`Γ'`-equivariant on `1 ⊗ L`. Such a form has type `u` at a letter if it sends the part of `1 ⊗ L` at
that letter into `hodgeFil (-u)`, where `hodgeFil n` is `tⁿ B_dR⁺`.


### `tateLattice`

 The lattice datum O(1), on which Γ acts through the cyclotomic character, with jump set {−1}
at every letter and at every embedding of O in ℂ_p (`embJumps`). The field `inClass` says that it is
crystalline over the group Γ' of the chart with jumps in these sets. 

### `JumpLattice.mem_withOrders_raisedOrdersAtZero_of_gap`

 A gap in the jumps is a gap in the pole orders. Let `L` be a lattice with a Galois action and
with a finite set `L.jumpSet i` of integers, its jumps, at each letter `i` of the chart `k`. Let `x`
in `W(C^♭) ⊗ L` have a pole of order at most `t` at `E`. Let `x` be fixed by `Γ'` modulo the vectors
without pole, which have orders `raisedOrdersAtZero 0`. If `0 ≤ h₀` and no jump at `i` lies in
`[-t, -h₀)`, then the pole of `x` has order at most `h₀`. 

 ### The extension, its kernel, and deep elements 

### `inclKer`

 The inclusion of `Y` into the extension of `C` by `Y`, as an equivariant map of lattice data. 

### `localizedProjTrivial`

 The `ℤ_[p]`-linear map from the localized Kisin module `kisinLoc` of the extension of `C` by `Y`
to `W(C^♭) ⊗ C` induced by the projection onto `C`. 

### `deepElements`

 The points of `S.extensionLattice.kisinLoc` that lie over a constant at the letter `i` (the
projection `S.constantAt i c` of some `1 ⊗ c` to `i`) and are deep for `o`, that is, fixed by
`k.galMonoid` modulo the vectors with orders `o`. For a point `x` at the letter `i` this means that
for each jump `u` at `i.stepBack a` and each form `μ` of type `u` there, the value
`valueAt a μ x = μ (φ^{-a} x)` lies in the fixed field of `Γ'` modulo
`hodgeFil (o a u) = t ^ (o a u) B_dR⁺` (`JumpLattice.mem_invariantsMod_withOrders_iff`). 

### `kerWithOrders`

 The vectors of the extension that lie over `0` and have orders `o` at the letter `i`. 

 ### Operators of a cost, pairings of sides, and points 

### `IsOperatorOfCost`

 The additive map `A` is an operator of cost `e`: for every letter `i`, all orders `o` and
every point `x` that lies over the projection of some `1 ⊗ c` to `i` and is deep for `o`, the
difference `A x - p ^ e • x` lies over `0` and has orders `o` at `i`. Here `locKisinPart Q` is the
set of the elements of `kisinLoc` that lie in `Q`. 

### `SidePairing`

 A pairing between the lattices of the sides S and S'. 

### `pointsOver`

 The points of `S.extensionLattice.kisinLoc` over `p ^ e` times the constant of `c` at the letter
`i` (the projection `S.constantAt i c` of `1 ⊗ c` to `i`) that have orders `o` and are deep for
`o'`: for each jump `u` at `i.stepBack a` and each form `μ` of type `u` there, the value
`valueAt a μ x = μ (φ^{-a} x)` lies in the fixed field of `Γ'` modulo
`hodgeFil (o' a u) = t ^ (o' a u) B_dR⁺` (`JumpLattice.mem_invariantsMod_withOrders_iff`). 

### `standardDepth`

 The depth that the walk asks of a standard point: on the lines of jump `u` it is `-u`, raised by
`t` at the level `0` and by `η` at the levels below `l`. 

### `plainDepth`

 The depth that a point at rest needs at a plain cut: `standardDepth t η l`, and `h₀` more at the
level `l`. 

### `stopOrders`

 The orders of a stop. In the walk one side moves first, to a point called the stop, and rests
there while the other side moves. The orders of a stop are at least those of the pullback by
`φ ^ l`, and at least `-u` lowered by `η` at the levels below `l`. 

### `ruleBound`

 The least sum of the orders of a move and the depth of the point at rest that the rule for `l`
allows, on lines whose jumps add up to `s`: it is `1` at the levels below `l`, `t - s` at the level
`l` and `-s` above. 

### `standardPoints`

 The standard points over `p ^ e c` at the letter `i`: their orders are `-u`, lowered by `η`
at the level `0`, and their depth is `standardDepth t η l`. 

### `stopPoints`

 The points over `p ^ e c` at the letter `i` with the orders of a stop (the depth asked for is
the same). 

### `LiesOver`

 The vector `x` lies at the letter `i`, over `p ^ e` times the constant of `c` at `i`. 

### `LiesOver.mem_letterPart`

 The vector lies in the part at the letter `i`. 

### `LiesOver.projTrivial_eq`

 Its image in the trivial lattice is `p ^ e` times the constant of `c` at `i`. 

### `wittFst_inclKer`

 Over `W(C^♭)`, the inclusion of `Y` into the extension is a section of the first projection
`S.wittFst`, and its image lies over `0`. 

### `wittPairing_wittFst_mulZeta`

 The pairing `P`, read on the first components of vectors of the two extensions, is balanced for
the multiplication by the root of unity `ζ` of `O`. 

### `isUnit_letterTeich_sub`

 The Teichmüller lifts `k.letterTeich` of two distinct letters differ by a unit of the ring `k.S`
of the chart. 

### `wittPairing_wittFst_eq_zero_of_ne`

 Vectors of the two extensions that lie at distinct letters are orthogonal under `P`. 

### `isSafe_sum`

 Let `P` be a pairing modulo `p ^ m` of two sides `S`, `S'` of the chart `k`, with lattices `Y`,
`Y'`, and let `κ` be a natural number. For each letter `i` let `u i`, `v i` be vectors in the parts
at `i` (`letterPart i`) of `W(C^♭)` tensored with the two extension lattices `Y × C`, `Y' × C'`. If
each pair `u i`, `v i` is safe for `P` and `κ`, that is, `p ^ κ` times the pairing of their
components in `Y` and `Y'` lies in the image of the ideal `W(𝔪^♭)` of Witt vectors over the maximal
ideal, then the pair of their sums over all letters is safe. 

### `exists_mem_form_cocycle_eq_coboundary`

 Let `S` be a side of the chart `k`: a lattice `Y` (`S.Carrier`) and a lattice `C`
(`S.paramLattice`) that indexes crystalline cocycles `S.cocycleMap c` with values in `Y`. Let `μ` be
an invariant form on `Y`: an `Ainf`-linear map from `W(C^♭) ⊗ Y` to `BdR` that is equivariant on
`1 ⊗ Y` for the subgroup `k.subgroup` of the chart. If its values on `1 ⊗ Y` lie in the
`BdRPlus`-submodule `W`, then `μ` sends the cocycle of `c`, restricted to `k.subgroup`, to the
coboundary `g b - b` of an element `b` of `W`. 

### `exists_linearMap_form_cocycle_eq_coboundary`

 Let `S` be a side of the chart `k`, with lattice `Y` and with cocycles `S.cocycleMap c` indexed
by the lattice `C = S.paramLattice`, and let `μ : W(C^♭) ⊗ Y → BdR` be an invariant form with values
in `W` on `1 ⊗ Y`. Then there is a linear map `f` from `C` to `W` such that `μ` sends the cocycle of
`c`, restricted to `k.subgroup`, to the coboundary `g ↦ g (f c) - f c`. 

### `exists_extend_form`

 Let `S` be a side of the chart: lattices `Y` and `C` with crystalline cocycles of `Y` indexed by
`C`, which define the extension `S.extensionLattice` of `C` by `Y`, with underlying module `Y × C`.
Let `μ` be an invariant form on `Y` whose values on `1 ⊗ Y` lie in `W`. Then some invariant form `ν`
on the extension restricts to `μ` along the inclusion `S.inclKer` of `Y` and has values in `W` on
`ainfLattice`, the `Ainf`-span of `1 ⊗ (Y × C)`. 

### `IsOperatorOfCost.apply_mem_of_kerWithOrders_le`

 Let `x` lie over a constant at the letter `i` and be deep for `o`. An operator of cost `e` sends
`x` into every submodule `M` that holds `x` and the points over `0` with orders `o`. 

### `locKisinPart_kerWithOrders_le_deepElements`

 The points of the localized Kisin module of the extension that lie over `0` and have orders
`o` at the letter `i` are deep for `o` at `i`. 

### `IsOperatorOfCost.mem_deepElements`

 An operator `A` of cost `e` keeps every depth: if `x` lies over a constant at the letter `i` and
is deep for `o`, then the same holds for `A x`. 

### `IsOperatorOfCost.comp`

 Costs add under composition: if `B` has cost `e'` and `A` has cost `e`, then `B ∘ A` has cost
`e' + e`. 

 ### Strictness of the inclusion, and points of one side 

### `mem_kisinLocAinf_of_inclKer`

 Let `S.inclKer` be the inclusion of the lattice `Y` of the side `S` into its extension by `C`,
and `S.inclKer.wittMap` that inclusion tensored with `W(C^♭)`. If the image of `y` under
`S.inclKer.wittMap` lies in `kisinLocAinf` of the extension, then `y` lies in `kisinLocAinf` of `Y`.
For a lattice `L`, this is the set of the vectors that some product of the elements `φ ^ a E` (`E`
the Eisenstein polynomial of the chart, `φ` the Frobenius) multiplies into `kisinAinf`. That module
consists of the `x` in `Ainf[1/τ] ⊗ L`, where `τ = [ε^{1/p}] - 1`, with `μ (φ ^ n x)` in `B_dR⁺` for
all `n ≥ 1` and all invariant forms `μ : W(C^♭) ⊗ L → BdR`. 

### `mem_letterPart_of_inclKer`

 A vector `y` of `S` whose image in the extension lies at the letter `i` lies at `i`. 

### `mem_withOrders_of_inclKer`

 Let `S.inclKer` be the inclusion of the lattice `Y` of the side `S` into its extension by `C`.
If the image of a vector `y` of `W(C^♭) ⊗ Y` has orders `o` at the letter `i`, then so has `y`. Here
orders `o : ℕ → ℤ → ℤ` at `i` mean: `y` is in the part at `i` of `kisinLocAinf` and, for each
integer `u` among the jumps at the letter `i.stepBack a`, `a` steps before `i`, each invariant form
`μ` of type `u` there has `μ (φ^{-a} y)` in `t ^ (o a u) B_dR⁺`. 

### `mem_kisinLoc_of_inclKer`

 Let `y` be a vector of `W(C^♭) ⊗ Y`, for the lattice `Y` of the side `S`. If the image of `y` in
the extension of `C` by `Y` lies in `kisinLoc` of the extension, then `y` lies in `kisinLoc` of `Y`.
Here `kisinLoc` is the Kisin module with all `φ^a E` inverted: it consists of the vectors that some
product of the elements `φ^a E` multiplies into the Kisin module `kisinModule`. 

### `exists_inclKer_eq_of_kerWithOrders`

 Strictness: a vector `w` of the extension that lies over `0` and has orders `o` at the letter
`i` is the image of a vector `y` of `S` with orders `o` at `i`, and `y` lies in the localized
Kisin module `kisinLoc` if `w` does. 

### `pointsOver_nonempty_of_killsCokernel`

 Let `S` be a side of the chart, with lattices `Y` and `C = S.paramLattice`. Suppose that
`p ^ κ * E ^ s`, with `E` the Eisenstein polynomial of the chart, kills the cokernel at the letter
`i` (`KillsCokernel`): it multiplies the part at `i` of `A_inf ⊗ C` into the image of the vectors of
the extension with the standard orders `stdOrders 0`. Then, for `c` in `C`, `S.pointsOver` is
nonempty: some point of the extension lies over `p ^ κ • c` at `i`. Its orders and its depth are
both `raisedOrdersAtZero (-s)`. 

### `depthOperator`

 The operator `x ↦ pr (υ (g x - x) / δ)` on `S.extensionLattice.kisinLoc`, for `g` in
`k.galMonoid` (the group `Γ'` of the chart) and `υ` in `Ainf`. Here `δ = k.zTau` is `z τ`, the
product of the coordinate `z` of the chart and `τ = [ε^{1/p}] - 1`. The element `(g x - x) / δ` lies
in the `Ainf`-span `S.extensionLattice.kisinLocAinf` of `S.extensionLattice.kisinLoc`, and the
retraction `pr = coordRetract` maps that span back to `S.extensionLattice.kisinLoc`. 

### `depthOperator_mem_withOrders`

 An operator turns depth into orders: if `g • x - x` has orders `o` at the letter `i`, then so
does `S.depthOperator g υ x`, the retraction of `υ (g x - x) / (z τ)` to the Kisin module of the
extension. 

### `projTrivial_depthOperator_eq_zero`

 The operator `S.depthOperator g υ`, the retraction of `x ↦ υ (g x - x) / (z τ)`, sends a point
over a constant at the letter `i` to a vector over `0`. 

### `depthOperator_mem_kerWithOrders`

 The operator `S.depthOperator g υ` sends an element of `S.deepElements i o` into
`S.kerWithOrders i o`, the vectors over `0` with orders `o` at `i`. 

### `exists_isOperatorOfCost_mem_hodgeFil_succ`

 One step of depth at the level `a` (the place `φ ^ a E`) for a side `S` of the chart `k`. Some
additive map `B` of cost `cost a n = v_p(n) + k.differentBound + 3 a` has the property below. Cost
`e'` means: if a point `x` lies over a constant at a letter `i` and is fixed by `Γ' = k.galMonoid`
modulo the vectors with orders `o` there, then `B x - p ^ e' • x` lies over `0` and has orders `o`
at `i`. The property: for every invariant form `μ` on the extension, if
`valueAt a μ (g • x - x) = μ (φ^{-a} (g • x - x))` lies in `hodgeFil n = tⁿ B_dR⁺` for all `g` in
`Γ'`, then the same expression for `B x` lies in `hodgeFil (n + 1)`. 

### `exists_isOperatorOfCost_and_mem_deepElements`

 Let `S` be a side of the chart `k` and `I` a finite set of steps `(a, n)`, of cost
`cost a n = v_p(n) + k.differentBound + 3 a` each. Call `x` deep for orders `o` at the letter `i`
(`deepElements`) if it lies over a constant at `i` and is fixed by `Γ'` modulo the vectors with
orders `o`. There is an additive map `A` of cost `e = ∑ cost a n` over `I`. It sends `x` deep for
`o` to an element deep for `o'` whenever `I` contains every step `(a, n)` with `o a u ≤ n < o' a u`
for a jump `u` at `i.stepBack a`, the letter `a` steps before `i`. 

### `pointsOver_nonempty_of_costs`

 Let `S.pointsOver c i e orders depth` be the points of the extension of the side `S` that
project to `p ^ e` times the component of `1 ⊗ c` at the letter `i`, have the given orders, and are
fixed by `Γ'` modulo the vectors with orders `depth`. Let `x` be such a point. If `I` contains the
steps `(a, n)` from `depth` to `depth'` at all jumps `u` at the letter `a` steps before `i`, and
`e'` is at least `e` plus their costs `cost a n = v_p(n) + k.differentBound + 3 a`, then there is a
point over `p ^ e' • c` with depth `depth'` and orders `improvedOrders orders depth'`. 

### `zTauUnit_inv_smul_sub_mem_kerWithOrders`

 Let `x` lie in `S.pointsOver c i e o₁ o`: it lies over `p ^ e` times the constant of `c` at the
letter `i`, with orders `o₁`, and is fixed by `Γ'` modulo orders `o`. Then for `g` in `k.galMonoid`
the element `(g • x - x) / (z τ)` (`k.zTauUnit⁻¹ • (g • x - x)`) lies in `S.kerWithOrders i o`. 

### `sub_mem_kerWithOrders_of_pointsOver`

 Two points `x` and `w` over the same constant, with orders `o₁` and `o₂`, differ by a vector
over `0` with orders `o₁ ⊓ o₂`. 

### `phi_pow_smul_mem_pointsOver`

 Let `φ` be the Frobenius and `S.pointsOver c j e o o'` the points over `p ^ e` times the
constant of `c` at the letter `j` with orders `o` that are fixed by `Γ'` modulo orders `o'` (the
depth). The power `φ ^ l` moves such a point at the letter `i.stepBack l`, `l` steps before `i`, to
a point at `i` over the same constant, with orders `shiftedOrders l 0 o` and depth
`shiftedOrders l 1 o'`. 

### `wittPairing_constantAt_one`

 The constant `1` of the Tate dual side at the letter `i` acts on `S.Ambient` as the projector to
the letter `i`. 

### `map_wittPairing_extensionForm`

 Let `P` be a pairing of the lattices `Y`, `Y'` of two sides, given by a form `ψ : Y ⊗ Y' → O(1)`
and a linear map `P.toZp : O → ℤ_p`, modulo `p ^ P.exponent`. Its Tate dual side is the lattice
`Hom(Y ⊗ Y', O(1))`, extended by `O` through the cocycle of `P`. Pair a vector `n` of this
extension, tensored with `W(C^♭)`, with `w ⊗ y` by `P.extensionForm`, which sends `(λ, o)` to the
form `p ^ P.exponent • λ + o • ψ`. The value, reduced modulo `p ^ P.exponent` through `P.toZp`, is
the pairing `P.wittPairing` of `y` with `w` multiplied by the projection of `n` to `W(C^♭) ⊗ O`. 
