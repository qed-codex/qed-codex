---
{
  "module": "src/Lib/General/NumberTheory/CoefficientInclusion.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/NumberTheory/CoefficientInclusion.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/NumberTheory/CoefficientInclusion.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Coefficient rings inside the ring of all integral elements

Elementary facts on the inclusion of a coefficient ring into `ℤ̄_ℓ`, and a divisibility statement
for geometric sums in a ring with a divisibility-reflecting map to `ℤ̄_ℓ`.

* `New.CoeffRing.toIntQpBar`: the inclusion, which reflects divisibility
  (`New.CoeffRing.dvd_of_toIntQpBar_dvd`).
* `New.Selmer.pow_dvd_geom_sum`: for `α` near `1`, a high power of `ℓ` divides `∑ i < ℓ ^ N, α ^ i`.

Notions from other files:
* `New.CoeffRing`: rings of integers of finite Galois extensions of `ℚ_ℓ` inside `ℚ̄_ℓ`;
  `New.CoeffRing.normLength` rescales `ℕ∞`-valued lengths over such a ring, a uniformiser `ϖ` having
  length `v(ϖ)`, so that lengths over different rings are comparable.
* `New.ellVal`: the valuation `v` on `ℚ̄_ℓ` with `v ℓ = 1`, cut off below at `0`; `New.intQpBar ℓ`
  is the ring `ℤ̄_ℓ` of integral elements; throughout, the instance `ThePrime ℓ` fixes `ℓ` as the
  prime in play.


### `CoeffRing.toIntQpBar`

 The inclusion of a coefficient ring `O` (the ring of integers of a finite Galois extension of
`ℚ_ℓ` inside `ℚ̄_ℓ`) into the ring `ℤ̄_ℓ` of all integral elements. 

### `CoeffRing.toIntQpBar_comp_inclusion`

 For coefficient rings `O ≤ O'`, including `O` into `O'` and then into `ℤ̄_ℓ` is the inclusion
of `O` into `ℤ̄_ℓ`. 

### `CoeffRing.dvd_of_toIntQpBar_dvd`

 The inclusion `toIntQpBar` of a coefficient ring (the integers of a finite Galois extension of
`ℚ_ℓ`) into the ring `ℤ̄_ℓ` of integral elements of `ℚ̄_ℓ` reflects divisibility. 

### `CoeffRing.normLength_addVal_eval₂`

 Let `O ≤ O'` be coefficient rings, `P` a polynomial over `O` and `x` a point with coordinates
in `O'`. The exponent of a uniformiser `ϖ` in `P(x) ∈ O'`, rescaled by `normLength` (that is,
multiplied by `v(ϖ)`), is the normalised valuation `v = ellVal` of the value in `ℤ̄_ℓ` that is
obtained by mapping `P` and `x` there with the inclusions `toIntQpBar`. 

### `CoeffRing.eventually_exists_toIntQpBar_eq`

 Finitely many elements of `ℤ̄_ℓ` lie in all sufficiently large coefficient rings `O` (rings of
integers of finite Galois extensions of `ℚ_ℓ` in `ℚ̄_ℓ`, ordered by inclusion), that is, they are
in the image of the inclusion `O.toIntQpBar`. 

### `pow_dvd_geom_sum`

 Let `f` be a ring map from `O` to `ℤ̄_ℓ = intQpBar ℓ`, the integral elements of `ℚ̄_ℓ`, that
reflects divisibility. If `r ≤ 1`, `v(f(α - 1)) ≥ r` for the valuation `v = ellVal` with
`v(ℓ) = 1`, and `M ≤ N r`, then `ℓ ^ M` divides `∑ i < ℓ ^ N, α ^ i`. 
