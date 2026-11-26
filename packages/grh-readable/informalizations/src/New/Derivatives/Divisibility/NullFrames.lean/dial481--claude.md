---
{
  "module": "src/New/Derivatives/Divisibility/NullFrames.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Divisibility/NullFrames.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Divisibility/NullFrames.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The change of directions

This file gives matrices over the integers of `ℂ_p`, one for each place and height, that change
given directions. For a divisor `π` of `p`, the pairings `∑ β_a ^ p ^ e * β'_a` of new directions at
a place and at its partner become divisible by `π`, apart from the exempt pairs of heights, which
involve a marked place. The valuations of the determinants, one for each column, add up to at most
the deduction: `v(π)` times the sum of the numbers `New.deductionTerm`.

## Main definitions and results

* `New.deductionTerm`: the term of the deduction for a place, a partner and an exponent `e`.
* `New.CongruenceChoice`, `New.exists_congruenceChoice_cost_eq_and_covers`: which congruences are
  imposed for a place and a partner; a choice of cost `New.deductionTerm` covers the pairs of
  heights that are not exempt (`New.IsExemptPair`).
* `New.newDirection`, `New.exists_newDirection_dvd`: integral changes of direction at each place
  and height that make the pairings that are not exempt divisible by `π`, and whose determinants
  cost at most the deduction.

Notions from other files:
* `New.valRingCp p`: the integers of `ℂ_p`.



## Changing the directions

Finitely many congruences on the rows of one matrix are met by elimination, at the price of the
product of the moduli.


### `New.exists_det_dvd_and_dvd_mulVec`

 One step of elimination over the integers `valRingCp p` of `ℂ_p`. Given the values `a k` of a
linear form on the rows of a matrix and a modulus `α`, there are row operations `u`, with
determinant dividing `α`, after which `α` divides all values. 

### `New.exists_det_dvd_prod_and_dvd_mulVec`

 For finitely many linear forms with coefficient vectors `A i` and moduli `α i` over the integers
`valRingCp p` of `ℂ_p`, there is a square matrix `g`, with determinant dividing the product of the
moduli, such that `α i` divides the value of the `i`-th form on every row of `g`. 

### `New.dvd_sum_pow_mul_of_root_dvd`

 Let `π` divide `p`, and let `root x` be a `p ^ e`-th root of `x`. If `root π` divides the linear
form `∑ root (y' a) * β a`, then `π` divides the pairing `∑ β a ^ p ^ e * y' a`, as `p ^ e`-th
powers are additive modulo `p`. 

### `New.dotProduct_sum_mul`

 The value of the form with coefficients `∑ a, x a * y a k` on a row `u` is the pairing of `x`
with the combination of the vectors `y · k` given by `u`. 

### `New.deductionTerm`

 The term of the deduction, in units of `v(π)`, for a place `σ`, a partner `σ'` and an exponent
`e`, when `κ σ h` is the number of columns of height `h` at `σ`, counted only for `h < n'`, and
`ev` is the set of marked places. Let `t σ` be the number of columns of height one (`0` if `σ` is
marked), `r σ` the number of columns of height other than one, and `B σ` the sum of their heights,
that is, their number of boxes. The term is the real number
`min (t σ / p ^ e) (r σ' + t σ') + r σ / p ^ e + min (B σ / p ^ e) (B σ')`. 

### `New.IsExemptPair`

 The pair of heights `h` at the place `σ` and `h'` at the place `σ'` is exempt for the set `ev`
of marked places: `h = 1`, and either `σ` is marked or `h' = 1` and `σ'` is marked. 

### `New.CongruenceChoice`

 A choice of congruences for a place (the source) and its partner: for each height `h`, which
of four kinds of congruence are imposed on the rows of height `h`. 

### `New.CongruenceChoice.sourceEntries`

 Congruences on all `h` entries of each row at the source. 

### `New.CongruenceChoice.sourcePairing`

 One congruence on the pairing of each row at the source with direction `0` at the partner. 

### `New.CongruenceChoice.partnerEntries`

 Congruences on all `h` entries of each row at the partner. 

### `New.CongruenceChoice.partnerPairing`

 One congruence on the pairing of each row at the partner with direction `0` at the source. 

### `New.PairingSide`

 The two sides of a pairing from a place to its partner. 

### `New.PairingSide.source`

 The side of the place itself. 

### `New.PairingSide.partner`

 The side of the partner. 

### `place`

 The place of a side, for a pairing from `σ` to `σ'`. 

### `rootExponent`

 For a pairing at the exponent `e`, congruences on a side are taken modulo a `p ^ r`-th root of
`π`, where `r` is this number: `e` at the source and `0` at the partner. 

### `sourceCount`

 The number of congruences on a row of height `h` at the source. 

### `partnerCount`

 The number of congruences on a row of height `h` at the partner. 

### `cost`

 The number of congruences on the heights `h < N`, counted once for each of the `κ h` columns
at the source, with weight `1 / p ^ e`, and once for each of the `κ' h` columns at the partner. 

### `Covers`

 The pair of heights `h` at the source and `h'` at the partner is covered by one of the four
kinds of congruence. A congruence on a pairing counts only if the height on the other side is
one. 

### `imposes`

 Whether a congruence is imposed on the rows of height `h` on the given side, on the pairing
(`none`) or on the entry `k` (`some k`). 

### `New.exists_congruenceChoice_cost_eq_and_covers`

 For a place `σ`, a partner `σ'` and an exponent `e` there is a choice of congruences
(`CongruenceChoice`): for each height, whether a row at `σ`, and a row at `σ'`, gets one congruence
on its pairing with direction `0` at the other place, one on each entry, or both. Its `cost`, the
number of congruences on all columns with those at `σ` weighted by `1 / p ^ e`, equals
`deductionTerm`. Each pair of heights `h` at `σ` and `h'` at `σ'` that is not exempt is covered
(`Covers`): there are congruences on the entries of one of the two rows, or on the pairing of one of
them and the other height is one. 

### `New.congruenceModulus`

 The moduli of the congruences on the rows of height `h` at the place `τ`, when `c e σ` is the
choice of congruences for the place `σ` and its partner `pr e σ` at the exponent `e ∈ S`. They are
indexed by `e`, `σ`, the side of the pairing from `σ` to `pr e σ` and the form (`none` for the
pairing, `some k` for an entry). If `τ` is the place of that side and `c e σ` imposes the
congruence, the modulus is `root e` at `σ` and `root 0` at `pr e σ`; otherwise it is `1`. 

### `New.norm_rpow_sum_cost_eq_prod_congruenceModulus`

 Let `c e σ` be a choice of congruences for each exponent `e ∈ S`, place `σ` and partner
`pr e σ`, let `κ τ h` be the number of columns of height `h` at the place `τ`, and let `root e` be a
`p ^ e`-th root of `π`. The modulus `congruenceModulus` of the congruence indexed by
`(e, σ, side, form)`, on the rows of height `h` at `τ`, is `root e` at the side `σ` and `root 0` at
the side `pr e σ`, if that side is the place `τ` and the congruence is imposed; otherwise it is `1`.
The product of all moduli, over all `τ` and `h < N` and once for each of the `κ τ h` columns, has
norm `‖π‖` raised to the sum over `e` and `σ` of the `cost` of `c e σ`: the number of congruences
imposed on all columns of height less than `N` at `σ`, divided by `p ^ e`, plus the number of those
at `pr e σ`. 

### `New.newDirection`

 Coordinate `a` of the new direction `k` for the place `τ` and the height `h`: the combination
`∑ k' : Fin h, g τ h k k' * y τ a k'` of the given directions `y τ · k'`. 

### `New.exists_newDirection_dvd`

 **Changing the directions.** Let `π` divide `p` in the integers `valRingCp p` of `ℂ_p`, and let
`y τ a k'` be coordinate `a` of direction `k'` at the place `τ`. There are square matrices `g τ h`,
one for each place and height, such that the new directions `newDirection g y τ h k a = ∑ k' : Fin
h, g τ h k k' * y τ a k'` have two properties. First, for `e ∈ S`, the pairing
`∑ a, β a ^ p ^ e * β' a` of a new direction `β` of height `h` at `τ` with a new direction `β'` of
height `h'` at the partner `pr e τ` is divisible by `π`, unless the pair of heights is exempt.
Second, the determinants of the `g τ h`, one for each of the `κ τ h` columns of height `h < N`, have
total valuation at most `v(π)` times the sum of `deductionTerm` over `e ∈ S` and places `τ`. 
