---
{
  "module": "src/Lib/ClassField/LocalDuality/DualityInequality.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/LocalDuality/DualityInequality.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/LocalDuality/DualityInequality.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The inequality of local Tate duality for orthogonal groups of cocycles

Throughout, `k` is a local field with absolute Galois group `Γ` (`New.IsLocalGalois`) and `l` is a
prime. The inequality of local duality is proved as a count of cocycles, for a finite discrete
module `M` and its dual `Hom(M, Ωˣ)`.

* `New.card_mul_card_le_of_le_pairingAnnihilator`: for `M` killed by a power of `l`, orthogonal
  groups of cocycles in `Hom(M, Ωˣ)` and `M` have `#X · #W ≤ #M ^ (2 + d)`, where `O` is the
  valuation ring of `k` and `#(O / l) = l ^ d`, if `Γ` acts by elements of `l`-power order.
* `New.DiscreteModule.HoldsCorestrictions.pairingAnnihilator_le`: annihilators descend from an open
  subgroup whose index is invertible on the module.
* `New.DiscreteModule.local_duality_card_dvd`: for an open subgroup `U` of index prime to `#M`, a
  largest orthogonal pair of cocycle groups over `U` bounds `#L^⊥ · #L` for cocycle groups `L` over
  `Γ`.

`New.Z1` is the group of continuous cocycles (not classes), `New.unitsModule` is `Ωˣ` written
additively, `unitsRep` is the action of `Γ` on this `Ωˣ` (so `H2 unitsRep` is `H²(Γ, Ωˣ)`),
`New.DiscreteModule.evalCup` is the cup product `Z¹(Hom(M, Ωˣ)) × Z¹(M) → H²(Ωˣ)`, and
`New.pairingAnnihilator b L` is the annihilator of `L` in the right-hand group of the pairing `b`.

Notions from other files:
* `New.DiscreteModule`: A discrete Γ-module over R: an R-module with the discrete topology and a
  continuous R-linear action of the topological group Γ.
* `New.DiscreteModule.cartierDual`: For finite M, the discrete Γ-module Hom(M, Ω^×) of additive maps
  to `New.unitsModule`, with (gf)(m) = g f(g⁻¹m).

## Relation to the literature

Known; see `Lib.ClassField.LocalDuality.CrystallineDuality` for sources.


### `Cohomology.char_eq_zero_of_cyclicClass_eq_zero`

 Over a local field `k`, a continuous character `χ : Γ → ℚ/ℤ` whose cyclic class `δχ ∪ w` in
`H²(Γ, Ωˣ)` vanishes for every `w` in `kˣ` is zero. 

### `DiscreteModule.HoldsCorestrictions.pairingAnnihilator_le`

 Let `k` be local, `i · [Γ : U]` act as the identity on `M`, `b : M × N → Ωˣ` an equivariant
pairing, and let `X`, `Y` contain the coboundaries and corestrictions of `X'`, `Y'`. If `X'`
contains the cup product annihilator of `Y'` over `U`, then `X` contains that of `Y`. 

### `card_dual_cocycles_le_of_trivial`

 Kummer theory in each coordinate: for a finite trivial module `M` killed by `l`, there are at
most `#M ^ (2 + d)` cocycles in `Hom(M, Ωˣ)`, where `O` is the valuation ring of `k` and
`#(O / l) = l ^ d`. 

### `eq_zero_of_evalCup_eq_zero_of_trivialOn`

 One side of the nondegeneracy of the Hilbert symbol, extended to a trivial module. Let `Γ` act
as `Gal(Ω/k)` on an algebraically closed field `Ω` of characteristic 0, with `A ∩ k` a discrete
valuation ring with finite residue field (`IsLocalGalois Γ k A`), and let `M` be a finite discrete
`Γ`-module killed by the prime `l` on which all of `Γ` acts trivially. A continuous 1-cocycle `y`
of `M` is zero if its cup product `M.evalCup x y` vanishes for every continuous 1-cocycle `x` of
`Hom(M, Ωˣ)`. 

### `card_mul_card_le_of_le_pairingAnnihilator`

 Let `k` be local with valuation ring `O` and `#(O / l) = l ^ d`. Let `M` be a finite module
killed by `l ^ r` and fixed by `Q`, where every `g : Γ` has a power `g ^ l ^ i` in `Q`. This is
`hM : FiniteKilledFixedInj (l ^ r) Q 1 0 M`, the predicate for which dévissage is stated; its last
two arguments `1` and `0` ask that `ρ 1 - 0 = id` be injective, so they impose nothing. If groups
`X` of cocycles in `Hom(M, Ωˣ)` and `W` of cocycles in `M` are orthogonal under the cup product
(`h_orth`), then `#X · #W ≤ #M ^ (2 + d)`: the form of Tate's local duality and Euler
characteristic formula used. 

### `card_mul_card_le_of_orthogonal`

 Let `M` be a finite module killed by `l ^ r` and fixed by `Q` (`hM`), where every `g : Γ` has a
power `g ^ l ^ i` in `Q`, and let `#(O / l) = l ^ d` for the valuation ring `O = A ∩ k` of the local
field `k`. If groups `X` of cocycles in `Hom(M, Ωˣ)` and `W` of cocycles in `M` are orthogonal under
the cup product `M.evalCup`, then `#X · #W ≤ #M ^ (2 + d)`. This is
`card_mul_card_le_of_le_pairingAnnihilator`, with the finiteness of `M` taken from `hM` inside the
statement.

This inequality is a numerical consequence of Tate local duality and the local Euler characteristic
formula, for 1-cocycles and `l`-primary `M` on which `Γ` acts through an `l`-group; perfectness of
the pairing is not asserted. 

### `DiscreteModule.local_duality_card_dvd`

 A divisibility form of local duality. Let `M` be finite and `U` an open subgroup of index prime
to `#M`. Let `X'`, `W'` be groups of cocycles of `U` in `Hom(M, Ωˣ)` and `M` that are orthogonal
under the cup product, with `#X' · #W'` largest among such pairs, and let `X`, `W` contain the
coboundaries and corestrictions of `X'`, `W'` (`New.DiscreteModule.HoldsCorestrictions`). Then
`#L^⊥ · #L` divides `#W · #X` for every group `L` of cocycles of `Γ` in `Hom(M, Ωˣ)`, where `L^⊥`
is the annihilator of `L` among the cocycles in `M`. 
