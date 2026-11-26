---
{
  "module": "src/Lib/General/NumberTheory/LargeResidueField.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/NumberTheory/LargeResidueField.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/NumberTheory/LargeResidueField.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Coefficient rings with a large residue field

Adjoining the roots of unity of order `ℓ ^ k - 1` to a finite extension of `ℚ_ℓ` multiplies the
degree by at most `k` and gives a residue field with at least `ℓ ^ k - 1` elements. The extension is
unramified, but this is not needed: the ramification index is at most the degree, which grows
linearly in `k`, while `ℓ ^ k` grows faster.

* `New.Selmer.frequently_lt_card_residueField`: beyond every coefficient ring there is one whose
  residue field is large compared with the ramification index.

Notions from other files:
* `New.CoeffRing ℓ`: rings of integers of finite Galois extensions of `ℚ_ℓ` inside `ℚ̄_ℓ`, ordered
  by inclusion;
* `New.ThePrime ℓ`: the class saying that `ℓ` is prime.


### `norm_pow_natDegree_minpoly_le`

 An element `x` of `ℚ̄_ℓ` of norm less than `1` and of degree `d` over `ℚ_ℓ` satisfies
`‖x‖ ^ d ≤ ‖ℓ‖`. 

### `addVal_ell_le_finrank`

 If a coefficient ring `O`, the ring of integers of a finite Galois extension of `ℚ_ℓ`, is
contained in a finite extension `K` of `ℚ_ℓ`, then its ramification index, the valuation of `ℓ`
in `O`, is at most the degree of `K`. 

### `natDegree_minpoly_le_of_pow_eq_one`

 An element `ζ` of `ℚ̄_ℓ` with `ζ ^ (ℓ ^ k - 1) = 1`, where `k ≠ 0`, has degree at most `k` over
`ℚ_ℓ`. 

### `le_card_residueField_of_isPrimitiveRoot`

 If a coefficient ring `O`, the ring of integers of a finite Galois extension of `ℚ_ℓ`, holds a
primitive `m`-th root of unity `ζ` of `ℚ̄_ℓ` and `m` is prime to `ℓ`, then the residue field of
`O` has at least `m` elements. 

### `exists_mul_add_one_lt_pow_sub_one`

 For every natural number `a` there is a positive `k` with `a k + 1 < ℓ ^ k - 1`. 

### `frequently_lt_card_residueField`

 For every natural number `c` and every coefficient ring, that is, the ring of integers of a
finite Galois extension of `ℚ_ℓ`, there is a coefficient ring containing it whose residue field has
more than `c · e + 1` elements, where `e`, the valuation of `ℓ`, is the ramification index of the
containing ring. 
