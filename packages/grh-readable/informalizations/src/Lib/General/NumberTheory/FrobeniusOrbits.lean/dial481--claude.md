---
{
  "module": "src/Lib/General/NumberTheory/FrobeniusOrbits.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/NumberTheory/FrobeniusOrbits.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/NumberTheory/FrobeniusOrbits.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Frobenius orbits of roots over finite fields and residue fields at self-conjugate places

This file collects arithmetic lemmas on finite fields and on finite places of a CM field `E`. For
`P` irreducible over a finite field with `q` elements and a root `x` of `P` in an extension `K`, the
roots of `P` in `K` are the Frobenius conjugates `x^(q^i)`, `i < deg P`. For a CM field `E` with a
primitive root of unity of order `5040`, a place fixed by conjugation has a norm that is a square,
so places of prime norm are split. The file also contains two summation lemmas.

* `New.FinPlace E`: the finite places `w` of `E`, that is, the nonzero primes of `𝓞 E`; `star w` is
  the complex conjugate of `w`.
* `w.q`: the norm of `w`, that is, the number of elements of its residue field.
* `w.IsSplit`: the statement `star w ≠ w`.

## Main definitions and results

* `New.card_selfAdjoint`: the size of a finite field with an involution that moves `√-1`.
* `New.two_notMem_of_star_eq`: if `E` contains an integer of trace `1` and even norm over its
  maximal real subfield, a place with `star w = w` does not lie above `2`;
  `New.HasPrimitiveRoot5040.isSplit_of_two_mem` is the case of the hypothesis
  `New.HasPrimitiveRoot5040 E`.
* `New.exists_sq_eq_q_of_star_eq`: if moreover `E` contains `√-1`, such a place has norm
  `w.q = r ^ 2` with `r % 4 = 3`; `New.HasPrimitiveRoot5040.exists_sq_eq_q_of_inert` is the case
  of the hypothesis `New.HasPrimitiveRoot5040 E`.
* `New.finite_prime_q_star_eq`, `New.isSplit_of_q_prime`: all but finitely many places of prime norm
  are moved by the conjugation, and all of them under the hypothesis `New.HasPrimitiveRoot5040 E`.
* `New.root_pow_card_pow_eq_self_iff`, `New.root_pow_card_pow_eq_iff_modEq`: `x^(q^n) = x` iff
  `deg P ∣ n`, and `x^(q^a) = x^(q^b)` iff `a ≡ b` modulo `deg P`.
* `New.aroots_eq_frobenius_orbit`, `New.aroots_pow_eq_frobenius_orbit`: with multiplicity, the roots
  of `P` in `K` are the `x^(q^i)` for `i < deg P`, and the roots of `P^j` are the `x^(q^i)` for
  `i < deg (P^j)`.

## Relation to the literature

Known: standard facts on finite fields and on residue fields of CM fields.


 ## Integer powers with a sum as exponent 

### `New.DiscreteSeries.zpow_sum_of_ne_zero`

 For a nonzero element `s` of a field, a power of `s` whose integer exponent is a finite sum is
the product of the powers of `s`. 


## Residue fields at self-conjugate places of a CM field

A count of the fixed points of an involution of a finite field, applied to the residue fields at
the finite places of a CM field `E` fixed by complex conjugation. If `E` has a primitive root of
unity of order `5040`, its integers contain a square root `i` of `-1` with `star i = -i`, and an `ω`
with `ω + star ω = 1` and `ω * star ω` even.


### `New.card_selfAdjoint`

 A finite field with an involution that moves a square root of `-1` has `r ^ 2` elements,
where `r`, the number of fixed points, is `3` modulo `4`. 

### `New.two_notMem_of_star_eq`

 Let the CM field `E` contain an integer `β` with `β + β̄ = 1` and `β β̄` even. Then the places
above `2` are split: a finite place `w` fixed by conjugation does not lie above `2`. 

### `New.exists_sq_eq_q_of_star_eq`

 Let the CM field `E` contain an integer `i` with `i² = -1` and `ī = -i`, and an integer `β`
with `β + β̄ = 1` and `β β̄` even. If the finite place `w` is fixed by conjugation, its norm `w.q`,
the number of elements of its residue field, is `r²` with `r ≡ 3` modulo `4`. 

### `New.finite_prime_q_star_eq`

 In a CM field `E` only finitely many places of prime norm are fixed by complex conjugation. 

### `New.HasPrimitiveRoot5040.isSplit_of_two_mem`

 If the CM field `E` contains a primitive root of unity of order `5040`, a finite place above
`2` is split, that is, moved by complex conjugation. 

### `New.HasPrimitiveRoot5040.exists_sq_eq_q_of_inert`

 If the CM field `E` contains a primitive root of unity of order `5040`, the norm `w.q` of a
finite place `w` fixed by conjugation is `r²` with `r ≡ 3` modulo `4`. 

### `New.isSplit_of_q_prime`

 If the CM field `E` contains a primitive root of unity of order `5040`, a finite place whose
norm `w.q` (the number of elements of its residue field) is prime is split, that is, moved by
complex conjugation. 

 ## Frobenius on the roots of polynomials over a finite field 

### `algebraMap_pow_card_pred_eq_one`

 The image in `K` of a unit of a finite field with `q` elements has `(q - 1)`-st power `1`. 

### `root_pow_card_pow_eq_self_iff`

 Let `P` be irreducible over a finite field with `q` elements and `x` a root of `P` in `K`. Then
`x^(q^n) = x` iff the degree of `P` divides `n`. 

### `root_pow_card_pow_eq_iff_modEq`

 Let `P` be irreducible over a finite field with `q` elements and `x` a root of `P` in `K`. Then
`x^(q^a) = x^(q^b)` iff `a ≡ b` modulo the degree of `P`. 

### `aroots_eq_frobenius_orbit`

 Let `P` be irreducible of degree `d` over a finite field with `q` elements and `x` a root of `P`
in `K`. The roots of `P` in `K`, with multiplicity, are `x, x^q, …, x^(q^(d-1))`. 

### `aroots_pow_eq_frobenius_orbit`

 With `q = |k|` and `x` a root in `K` of the irreducible `P`, the roots of `P ^ j` with
multiplicity are the `x ^ q ^ i` for `i < deg (P ^ j)`, and `x ^ q ^ deg (P ^ j) = x`. 

### `exists_pow_card_pow_eq_of_root`

 Let `P` be irreducible over a finite field with `q` elements and `x` a root of `P` in `K`. Every
root of `P` in `K` is `x^(q^i)` for some `i < deg P`. 

 ## Sums over `ℤ/N` for `N` prime 

### `New.sum_eq_add_sum_units`

 For a prime modulus `N`, every nonzero element of `ℤ/N` is a unit, so a sum over `ℤ/N` is its
term at `0` plus the sum over the units. 
