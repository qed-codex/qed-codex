---
{
  "module": "src/Lib/ClassField/LocalDuality/KummerFiniteness.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/LocalDuality/KummerFiniteness.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/LocalDuality/KummerFiniteness.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Index of l-th powers in a local field and finiteness of Kummer 1-cocycles

Let `L` be a local field with ring of integers `O`. `New.IsLocalGalois Γ L A` makes `Γ` the absolute
Galois group of `L`, acting on an algebraic closure `Ω` and stabilising its valuation ring `A`; then
`O = A ∩ L` is `New.valRingBelow L A`, a discrete valuation ring with finite residue field. Absolute
values `|x|` are the multiplicative valuation `A.valuation x`. This file counts the `l`-th power
classes in `Lˣ` and deduces the number of continuous 1-cocycles `Γ → Ωˣ` killed by `n`.

## Main definitions and results

* `New.cokerKerIndex_local_units`: `#(Lˣ / Lˣ ^ l) / #μ_l(L) = l · #(O / l)`.
* `New.IsLocalGalois.card_kummer_cocycles`: there are `n² · #(O / n)` continuous 1-cocycles
  `Γ → Ωˣ` killed by `n`; `New.IsLocalGalois.card_ker_natCast_Z1_unitsModule` and
  `New.IsLocalGalois.finite_ker_natCast_Z1_unitsModule` state the count and the finiteness apart.
* `New.IsLocalGalois.finite_Z1`: a finite discrete `Γ`-module has finitely many continuous
  1-cocycles.

Notions from other files:
* `New.cokerKerIndex`: `#coker / #ker` of a linear map, a rational number that is `0` if either
  group is infinite.
* `New.DiscreteModule`: a discrete `Γ`-module over `R`: an `R`-module with the discrete topology
  and a continuous `R`-linear action of the topological group `Γ`.
* `New.Z1 ρ`: the continuous 1-cocycles of the representation `ρ`; `New.unitsModule Γ` is `Ωˣ`,
  written additively, as a discrete `Γ`-module.

## Relation to the literature

Known; see `Lib.ClassField.LocalDuality.CrystallineDuality` for sources.



## The index of l-th powers in the multiplicative group

It rests on a form of Hensel's lemma for l-th roots, proved first in the algebraic closure and then
descended by Galois invariance.


### `New.exists_root_near_one`

 Let `A` be a valuation subring of an algebraically closed field `Ω`, with absolute value
`|x| = A.valuation x`. If `r ≠ 0` and `|a - 1| ≤ |l| r`, then `a` has an `l`-th root `z` with
`|z - 1| ≤ r`. 

### `New.exists_local_root_near_one`

 Hensel's lemma for `l`-th roots in a local field `L` with absolute Galois group `Γ`
(`New.IsLocalGalois Γ L A`), where `|x| = A.valuation x`: if `0 < r < |l|` and `|a - 1| ≤ |l| r`,
then `a = x ^ l` for some `x` in `L` with `|x - 1| ≤ r`. 

### `New.IsLocalGalois.finite_quotient_span_singleton`

 In a local field `L` with absolute Galois group `Γ` (`New.IsLocalGalois Γ L A`), the quotient of
the integers `O = New.valRingBelow L A` by a nonzero principal ideal is finite. 

### `New.eq_one_of_pow_eq_one_of_valuation_sub_lt`

 Let `A` be a valuation subring of `Ω` and `L → Ω` a field embedding. An `l`-th root of unity
`u` in `L` with `|u - 1| < |l|` (for the valuation of `A`) is `1`. 

### `New.IsLocalGalois.exists_surjective_ord`

 The order at the maximal ideal as an additive map. Let `L` be a local field
(`New.IsLocalGalois Γ L A`) with absolute value `|x| = A.valuation x`, `π` a uniformiser and `Y` an
additive group isomorphic to `Lˣ` (by `y`). Then some surjective `f : Y → ℤ` has
`|y a| = |π| ^ n` exactly when `f a = n`. 

### `New.cokerKerIndex_local_units`

 The index of `l`-th powers in a field `L`, where `Γ = Gal(Ω/L)` with `Ω` algebraically closed of
characteristic 0 and `O = New.valRingBelow L A` a discrete valuation ring with finite residue field
(`New.IsLocalGalois Γ L A`). Let `l ≠ 0` and let `Y` be an additive group isomorphic to `Lˣ` (by
`y`). For multiplication by `l` on `Y`, the index `#(Y / l Y) / #Y[l]` (a) is not `0`, that is, both
groups are finite; (b) equals `l · #(O / l O)`. 


## Kummer count and finiteness of continuous 1-cocycles

`New.DiscreteUnits` is Ωˣ written additively, `New.unitsModule` the same as a discrete Γ-module, and
`New.Z1` the module of continuous 1-cocycles.


### `card_kummer_cocycles`

 Kummer theory. Assume `New.IsLocalGalois Γ k A`: `Ω` is algebraically closed of characteristic
0, `Γ` is the Galois group of `Ω` over `k` and stabilises the valuation subring `A`, and
`O = New.valRingBelow k A = A ∩ k` is a discrete valuation ring with finite residue field (`k` need
not be complete). For `n ≠ 0`, let `c` be the number of continuous 1-cocycles `Γ → Ωˣ` killed by `n`
(those with values in the `n`-th roots of unity). Then (a) `c > 0`, which says that the group is
finite, since `Nat.card` of an infinite type is `0`; (b) `c = n² · #(O / n O)`.

It is proved from Hilbert 90, the multiplicativity of `New.cokerKerIndex` along
`1 → kˣ → Ωˣ → Z¹ → 1`, and `New.cokerKerIndex_local_units` on `kˣ`, not from Tate's local Euler
characteristic formula; it is a variant of Kummer theory; it counts 1-cocycles rather than
cohomology classes with values in the n-th roots of unity. 

### `finite_ker_natCast_Z1_unitsModule`

 Let `k` be a local field with absolute Galois group `Γ` (`New.IsLocalGalois Γ k A`) and let
`n ≠ 0`. The continuous 1-cocycles `Γ → Ωˣ` killed by `n` form a finite group. 

### `card_ker_natCast_Z1_unitsModule`

 Assume `New.IsLocalGalois Γ k A`: `Ω` is algebraically closed of characteristic 0, `Γ` is the
Galois group of `Ω` over `k` and stabilises the valuation subring `A`, and
`O = New.valRingBelow k A = A ∩ k` is a discrete valuation ring with finite residue field (`k` need
not be complete). Then for `n ≠ 0`, the number of continuous 1-cocycles `Γ → Ωˣ` killed by `n` is
`n² · #(O / n O)`. 

### `finite_Z1`

 If `k` is a local field with absolute Galois group `Γ` (`New.IsLocalGalois Γ k A`), then for
every finite discrete `Γ`-module `M` over a commutative ring `R`, the module `Z¹(Γ, M)` of
continuous 1-cocycles is finite.

A case of the finiteness of Galois cohomology of a local field: degree one, in characteristic 0,
stated for continuous 1-cocycles of a finite module rather than for H¹. 
