---
{
  "module": "src/New/Congruences/Lifting/LongGap.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Lifting/LongGap.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Lifting/LongGap.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The long gap lemma for a side of a Kummer chart, by expansion in powers of E

This file concerns a side `S` over a Kummer chart, whose distinguished element is written `E`. It
defines the constants modulo `E ^ A` and expands vectors in powers of `E` with such constants as
coefficients. It then proves the long gap lemma. The proof multiplies a lift by `f(E)`, with `f`
monic of degree `N`, and takes the `N`-th Taylor coefficient of `p ^ (4 δ)` times the product.

## Main definitions and results

* `New.Lift.KummerChart.JumpLattice.constantsModE`: the constants modulo E^A, with exponents
  `New.Lift.KummerChart.JumpLattice.shiftedStdOrders`.
* `New.Lift.KummerChart.PairingSide.pointsOver_nonempty_of_long_gap`: the long gap lemma. On an
  unramified Kummer chart, if `E ^ s` kills the cokernel at `i` and `p ^ κ` kills it at
  `i.stepBack l`, the jumps at `i` and the `l - 1` letters before it are at most `g`, `3 ≤ p ^ l`,
  `A ≤ p ^ l * δ`, and there is the long gap `s + g * ∑ a < l, p ^ a < A`, then a constant of the
  trivial lattice lifts, up to a power of p, to a point of the extension at `i` with a large order
  at E at the very negative jumps.

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
* `New.Lift.KummerChart.JumpLattice.withOrders`: for a lattice `L` with a finite set of jumps at
  each letter, the vectors of W(C^♭)⊗L at a letter whose value at φ^a E on the forms of jump u is
  divisible by t^{c(a,u)}; they are said to have the orders `c`.
* `New.Lift.KummerChart.PairingSide`, `New.Lift.KummerChart.PairingSide.KillsCokernel`: one side of
  a pairing: lattices Y and C (`paramLattice`), an O-linear map `cocycleMap` from C to the
  crystalline cocycles Z_f(Y), and for each letter a finite set of integers that contains 0, the
  jumps. The extension `extensionLattice` of C by Y maps by `projTrivial` to `trivialLattice`, the
  lattice C with trivial action. `KillsCokernel`: `p ^ κ * E ^ s` multiplies the part of A_inf ⊗ C
  at a letter into the image of the standard module of level 0 of the extension.
* `New.Lift.KummerChart.PairingSide.pointsOver`: `S.pointsOver c i e o d` is the set of the vectors
  `x` of the Kisin module of the extension, with all φ^a E inverted, that lie over `p ^ e c` at `i`,
  have the orders `o` and have the depth `d`: every `g • x - x` with `g` in Γ' has exponents `d`.

## Relation to the literature

See `New.Congruences.Lifting.CutExponentBounds` for related work.


### `JumpLattice.shiftedStdOrders`

 The system of exponents obtained from the standard one of level `l` (`0` for `a < l`, `-u` for
`a ≥ l`) by adding `o u` at `a = 0`, that is, at `E`. Here `a` stands for the element φ^a E. 

### `JumpLattice.constantsModE`

 The constants modulo `E ^ A` at the letter `i` of a lattice `L`. Let `x` lie in
`L.stdOrdersPart l i`: in the Kisin module of `L` with all `φ^a E` inverted, at `i`, with the
standard orders of level `l`. This means that the value at `φ^a E` of each form of jump `u` is
divisible by `t ^ c`, where `c` is `0` for `a < l` and `-u` for `a ≥ l`. It is a constant if every
`g • x - x`, for `g` in the subgroup `Γ'` of the chart, has these orders raised by `A` at `E`, that
is, at `a = 0`. The constants form a ℤ_p-module. 

### `JumpLattice.mem_withOrders_shiftedStdOrders_of_le`

 If `x` has the standard orders of level `l` raised by `o` at `E`, it has them raised by any
`o' ≤ o`. 

### `JumpLattice.frobEUnit_zpow_smul_mem_withOrders_shiftedStdOrders`

 The power `E ^ m` adds `m` to the exponents `o` by which the standard ones are raised at `E`.
Here `k.frobEUnit 0` is `E` as a unit. 

### `JumpLattice.wittFq_smul_mem_constantsModE`

 The constants modulo `E ^ A` are stable under multiplication by the unramified Witt vectors
`W(𝔽_{p^f})`. 

### `JumpLattice.Hom.wittMap_mem_constantsModE`

 A map of lattices `F : L → L'` sends constants modulo `E ^ A` to constants modulo `E ^ A`, if
the jump sets of `L'` lie in those of `L`. 

### `JumpLattice.mem_withOrders_of_add_E_smul_mem`

 The standard orders of level `l` (`stdOrders l`) are `0` for `a < l` and `-u` for `a ≥ l`;
`shiftedStdOrders l o` adds `o u` to them at `a = 0`. Let `0 < l`, let `ξ` be a constant modulo
`E ^ A` (standard orders, and all `g • ξ - ξ` with `g ∈ Γ'` have them raised by `A` at `a = 0`) and
let `y` have the standard orders. If `ξ + E • y` has the orders `shiftedStdOrders l o`, then `ξ` has
the standard orders raised by `A` at `a = 0` on the jumps `u` with `0 < o u`. 

### `JumpLattice.mem_withOrders_of_expansion_mem`

 Let `0 < l`, let all `ξ n` be constants modulo `E ^ A` and let `y` have the standard orders. If
`∑ n ≤ N, E ^ n • ξ n + E ^ (N + 1) • y` has the standard orders raised by `o ≤ A` at `E`, then
`ξ N` has them raised by `A` at the jumps `u` with `N < o u`. 

### `JumpLattice.letterProj_mem_constantsModE`

 The forms of `L` are the `A_inf`-linear maps `μ : W(C^♭) ⊗ L → B_dR` that are equivariant on
`1 ⊗ L` for the subgroup `Γ'` (`k.subgroup`) of the chart; `toGp` maps it to the Galois group. Let
`0 < l`. Let `x` lie in the image under `φ ^ l` of the `A_inf`-module `L.kisinAinf`, and let all
forms take values at `x` in the field `𝒦₀ = k.valueField 0`. Let `g μ(x) - μ(x)` lie in
`hodgeFil A = t ^ A B_dR⁺` for all forms `μ` and all `g` in `Γ'`. Then the projection
`L.letterProj i x` of `x` to the letter `i` is a constant modulo `E ^ A`: it has the standard
orders of level `l`, and every `g • y - y` for this projection `y` has them raised by `A` at
`E`. 

### `exists_expansion_pow_E`

 On an unramified chart (`E = z + p`), every `s` in the ring `k.S = Λ⟦z⟧` has an expansion in
powers of `E` with coefficients in `Λ = WittFq k.f = W(𝔽_{p^f})`: there are `w n` such that
`s = ∑ n < N, E ^ n * w n` modulo `E ^ N` for all `N`. 

### `JumpLattice.exists_taylor_expansion_of_mem_stdOrdersPart`

 Expansion in powers of `E` with nearly invariant coefficients, on an unramified chart (`e = 1`).
Let `x` be a vector of the Kisin module of `L` with all `φ^a E` inverted at the letter `i`, with the
standard orders of level `l`: the value at `φ^a E` on the jump `u` has order `0` for `a < l` and
`-u` for `a ≥ l`. Let `0 < l`, `3 ≤ p ^ l`, and let `δ` be a natural number with `A ≤ p ^ l * δ`;
the price of the expansion is the factor `p ^ (4 * δ)`. Then there are constants `ξ n` modulo
`E ^ A` such that for every `N` the vector `p ^ (4 * δ) • x` is `∑ n < N, E ^ n • ξ n` plus `E ^ N`
times a vector of `L.stdOrdersPart l i`. 

### `JumpLattice.exists_isMonicOfDegree_aeval_smul_mem`

 On an unramified chart, let `y` be a vector of `W(C^♭) ⊗ L` with orders
`raisedOrdersAtZero (-s)` at the letter `i`: the value at `φ^a E` of a form of jump `u` is divisible
by `t` to the power `-u - s` for `a = 0` and `-u` for the other `a`. Then there is a monic `f` in
`ℤ[X]` of degree `s + g * ∑ j < l, p ^ j` such that `f(E) • y` has orders `g - u` at `φ^a E` for
`a < l` and `-u` for `a ≥ l`. 

### `PairingSide.projTrivial_coeff_sub_mem_withOrders`

 Let `0 < l`, let `f` be monic of degree `N < A`, let all `ξ n` be constants modulo `E ^ A` in
the extension and let `y` have the standard orders. Suppose that `projTrivial` sends
`∑ n ≤ N, E ^ n • ξ n + E ^ (N + 1) • y` to `p ^ e • f(E) • c`, where `c` stands for
`S.constantAt i c`, the image of `1 ⊗ c` at the letter `i`. Then it sends `ξ N` to `p ^ e • c` up to
a vector that has the standard orders raised by `A` at `E`. 

### `PairingSide.exists_lift_pow_smul_of_killsCokernel_stepBack`

 Let `p ^ κ` kill the cokernel of the side `S` at the letter `l` steps before `i`. Let `z` be a
vector of the trivial lattice `S.trivialLattice` at `i` with the standard orders of level `l`
(`stdOrdersPart l i`). Then `p ^ κ • z` is the image under `projTrivial` of a vector of the
extension `S.extensionLattice` with the same exponents at `i`. 

### `PairingSide.exists_wittMap_sub_smul_constantAt_mem_of_long_gap`

 The Taylor coefficient in the long gap lemma. Let `S` be a side, with lattices Y and
`C = S.paramLattice`, cocycles, and a finite jump set `S.jumpSet` at each letter. Let the chart be
unramified (`E = z + p` and `e = 1`). Let `0 < l`, `3 ≤ p ^ l` and `A ≤ p ^ l δ`. Let `E ^ s` kill
the cokernel at `i` (`KillsCokernel i 0 s`: it multiplies `A_inf ⊗ C` at `i` into the image of the
extension of level `0`). Let the jumps at the `l` letters `i.stepBack a` (`a` Frobenius steps before
`i`, `a < l`) be at most `g`, and let `N = s + g (1 + p + ⋯ + p ^ (l - 1)) < A`. Then for each `c`
in `C` there is a `ξ` in `constantsModE l A i` of the extension lattice, a constant modulo `E ^ A`.
It has the standard orders of level `l` (`0` below `l`, `-u` on the jump `u` from `l` on), raised by
`A` at `E` at the jumps `u < -N`. Moreover `projTrivial` sends `ξ` to `p ^ (4 δ) • S.constantAt i c`
up to a vector of the trivial lattice with these orders raised by `A` at `E` at every jump. 

### `PairingSide.pointsOver_nonempty_of_long_gap`

 Long gap, for a side `S` with lattice `C = S.paramLattice` and finite jump sets at the letters.
Let the chart be unramified, `3 ≤ p ^ l` and `A ≤ p ^ l δ`. Let `p ^ κ` kill the cokernel at the
letter `l` steps before `i`, and `E ^ s` the cokernel at `i`. Let the jumps at the `l` letters up to
`i` be at most `g`, and let `N = s + g (1 + p + ⋯ + p ^ (l - 1)) < A`. Then for each `c` in `C` the
extension has a point `x` at `i` over `p ^ (κ + 4 δ) c` with the standard orders of level `l`,
raised by `A` at `E` at the jumps `u < -N`, such that all `γ x - x` with `γ` in the subgroup `Γ'` of
the chart have the standard orders raised by `A` at `E` at every jump. 
