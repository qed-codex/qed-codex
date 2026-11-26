---
{
  "module": "src/Lib/General/NumberTheory/ImaginaryQuadraticField.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/NumberTheory/ImaginaryQuadraticField.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/NumberTheory/ImaginaryQuadraticField.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The imaginary quadratic field ℚ(√−d): characters, Frobenius and splitting of primes

This file studies the imaginary quadratic field `K = ℚ(√-d)` (`New.QuadField`) for `d ≡ 3 mod 4`,
realised inside `ℂ`, and the Dirichlet characters attached to it. Throughout, `New.chiK d p` is the
Legendre symbol `(p / d)` of `p` modulo the prime `d`, and `New.QuadField.betaK d` is the algebraic
integer `(1 + √-d) / 2`. A finite place of `K` (`New.FinPlace`) is a nonzero prime of its ring of
integers. Below, `w` is a finite place that contains the rational prime `p`, and `w.q` is its
absolute norm. For a prime `d ≡ 7 mod 8` the file determines the ring of integers and the different
of `K`. For `d ≡ 3 mod 4` it shows how a rational prime `p` decomposes in `K`. It also proves two
consequences of lifting the exponent at `2` for integers, which do not involve `K`.

## Main definitions and results

* `New.chiK`, `New.quadTwist`: the Legendre symbol `(·/d)` as an integer-valued character, and its
  product with a complex character `χ` modulo `N`, a character modulo `N * d`.
* `New.QuadField`: the field. For `d ≡ 3` modulo `4` it is a quadratic CM field
  (the degree is `New.QuadField.finrank_eq_two`). For a prime `d ≡ 3` modulo `4` it embeds in any
  field of characteristic zero with a primitive `d`-th root of unity
  (`New.QuadField.embOfPrimitiveRoot`).
* `New.QuadField.different_eq_span_and_adjoin_betaK`: for a prime `d ≡ 7` modulo `8`, the integers
  of `K` are `ℤ[(1 + √-d) / 2]` and the different is `(√-d)`.
* `New.FinPlace.q_eq_pow_inertiaDeg`, `New.FinPlace.inertiaDeg_dvd_iff_forall_pow_eq`: the norm of
  `w` is `p ^ f` with `f` the residue degree, and `f` is the order of Frobenius;
  `New.FinPlace.exists_q_eq_pow` states both together.
* `New.QuadField.q_eq_iff_chiK_ne_neg_one`: for `d` a prime `≡ 7 mod 8`
  (`New.PrimeSevenModEight`), `w` has degree one iff the Legendre symbol `(p / d)` is not `-1`.
* `New.QuadField.span_eq_or_exists_span_eq_mul`: `p` is inert in `K`, or it is the product of two
  places of degree one; `New.QuadField.prime_inert_or_eq_mul` also lists the places above `p`.



## The field ℚ(√−d), its quadratic character and its ring of integers

`star` on `K` and on its integers is complex conjugation.


 ### Characters and `L`-functions 

### `chiK`

 For a prime d, the Legendre symbol (·/d) as an integer-valued Dirichlet character modulo d; for
d ≡ 3 mod 4 it is the character χ_K of K = ℚ(√−d). 

### `quadTwist`

 The product of `χ`, a character modulo `N`, and the Legendre symbol `(·/d)`, as a character
modulo `N * d`. 

### `entireL`

 The entire function equal to L(s, χ) if χ is not principal, and to the continuation of
(s − 1)L(s, χ) if χ is principal. 

### `chowlaSelbergConst`

 The real number `γ - Re L'/L(1, χ_K)`, with `γ` Euler's constant. The character is written as
the twist by `(·/d)` of the character modulo `1`, which for `d ≡ 3 mod 4` is `χ_K` at level
`1 * d`. For odd `d` it is not principal, so `New.entireL` of it is its `L`-function. 

### `totient_mul_totient_le_finrank`

 If a number field `M` contains primitive roots of unity of coprime orders `n` and `d`, then its
degree over `ℚ` is at least `φ(d) φ(n)`. 

 ### The field `K = ℚ(√-d)` 

### `PrimeSevenModEight`

 The natural number d is a prime congruent to 7 modulo 8. 

### `PrimeSevenModEight.mod_eight`

 `d ≡ 7` modulo `8`. 

### `QuadField`

 The subfield K = ℚ(i√d) of ℂ. 

### `sqrtNegD`

 The generator √−d = i√d of K = ℚ(i√d). 

### `minpoly_I_mul_sqrt`

 For `d ≡ 3 mod 4`, the minimal polynomial of `i√d` over `ℚ` is `X ^ 2 + d`. 

### `finrank_eq_two`

 For `d ≡ 3 mod 4`, the field `K = ℚ(√-d)` has degree `2` over `ℚ`. 

### `embOfSqrt`

 For d ≡ 3 mod 4 and y with y² = −d in a field M of characteristic zero, the embedding of
K = ℚ(i√d) into M sending i√d to y. 

### `embOfPrimitiveRoot`

 For a prime d ≡ 3 mod 4, an embedding of ℚ(√−d) in a field M of characteristic zero that
contains a primitive d-th root of unity, given by the quadratic Gauss sum. 

### `four_dvd_d_add_one`

 For `d ≡ 3 mod 4`, `4` divides `d + 1`. 

### `abs_norm_eq_norm_sq`

 For d ≡ 3 mod 4, the absolute value of the norm of x ∈ K ⊂ ℂ is |x|², as K has a single,
complex, infinite place. 

### `absNorm_span_eq_mul_star`

 For `d ≡ 3 mod 4`, the absolute norm of the ideal generated by an integer `y` of `K = ℚ(√-d)`
is `y * ȳ`, where `star y = ȳ` is the complex conjugate of `y`. 

 ### The ring of integers of `K` 

### `betaK`

 For d ≡ 3 mod 4, the algebraic integer (1 + √−d)/2 of K = ℚ(√−d). 

### `betaK_mul_one_sub`

 For `d ≡ 3 mod 4`, the element `betaK d = (1 + √-d) / 2` times its conjugate `1 - betaK d` is
the natural number `(d + 1) / 4`. The division is exact, as `4` divides `d + 1`. 

### `sqrtNegDInt`

 For d ≡ 3 mod 4, the element √−d = i√d of the ring of integers of K = ℚ(√−d), defined as
2·(1 + √−d)/2 − 1. 

### `sqrtNegDInt_sq`

 For `d ≡ 3 mod 4`, the square of the algebraic integer `√-d = 2 * betaK d - 1` is `-d`. 

### `different_eq_span_and_adjoin_betaK`

 For a prime `d ≡ 7` modulo `8`, the different ideal of the ring of integers of `K = ℚ(√-d)`
over `ℤ` is generated by `sqrtNegDInt d = 2 * betaK d - 1 = √-d`, and the subring `ℤ[betaK d]` is
the whole ring of integers of `K`, where `betaK d = (1 + √-d) / 2`. 

 ## Residue degrees, Frobenius, and 2-adic lifting the exponent 

 ### Primes above a rational prime 

### `exists_natCast_mem`

 Every rational prime `p` lies in some finite place of the number field `F`. 

### `q_eq_pow_inertiaDeg`

 If the finite place `w` lies above the prime `p`, its absolute norm `w.q` is `p ^ f`, where
`f = w.asIdeal.inertiaDeg ℤ` is the residue degree of `w`. 

### `inertiaDeg_dvd_iff_forall_pow_eq`

 The residue degree is the order of Frobenius: if the finite place `w` lies above the prime `p`,
then `x ↦ x ^ p ^ n` is the identity modulo `w` exactly when the residue degree of `w` divides
`n`. 

### `exists_q_eq_pow`

 If the finite place `w` lies above the prime `p`, there is an `f` such that the absolute norm
`w.q` is `p ^ f` and `x ↦ x ^ p ^ n` is the identity modulo `w` exactly when `f ∣ n`. This `f` is
the residue degree of `w`. 

### `mem_asIdeal_iff_of_span_eq`

 If `(a) = w`, then `w` is the only finite place that contains `a`. 

### `mem_asIdeal_iff_of_span_eq_mul`

 If `(a) = w w'`, then the finite places that contain `a` are `w` and `w'`. 

 ### Frobenius on `√-d` 

### `map_sqrtNegDInt_sq`

 For a prime `d ≡ 7 mod 8`, a ring map from the integers of `ℚ(√-d)` to a commutative ring sends
`√-d = 2 * betaK d - 1` to a square root of `-d`. 

### `chiK_two`

 For a prime `d ≡ 7 mod 8`, the Legendre symbol `chiK d 2 = (2 / d)` is `1`. 

### `chiK_eq_pow_of_sq_eq_neg`

 For a prime `d ≡ 7 mod 8`, an odd prime `p` and a square root `x` of `-d` in a ring `R` of
characteristic `p`, `x ^ (p - 1)` is the image in `R` of the Legendre symbol `(p / d)`. 

### `eq_map_betaK_pow_iff`

 For a prime `d ≡ 7 mod 8`, an odd prime `p` and a ring map `φ` from the integers of `ℚ(√-d)`
to a ring of characteristic `p`, the `n`-th power of Frobenius sends `φ (betaK d)` to the `x` with
`2 x - 1 = (p / d) ^ n φ (√-d)`. Here `betaK d = (1 + √-d) / 2`,
`sqrtNegDInt d = √-d = 2 * betaK d - 1` and `chiK d p` is the Legendre symbol `(p / d)`. 

 ### The norm `q` and the values of the Legendre symbol 

### `primeNorm`

 The number q: p² if (p/d) = −1, and p otherwise. For primes p and d ≡ 7 mod 8 it is the norm of
a prime of ℚ(√−d) above p. 

### `chiK_cases`

 For primes `p` and `d`, the Legendre symbol `chiK d p = (p / d)` is `0` if `p = d`, and it is
`1` or `-1` otherwise. 

 ### Lifting the exponent at `2` 

### `two_pow_dvd_or_of_pow_eq_one`

 If `q ^ o ≡ 1 mod 2 ^ (s + 1)` and `o ≠ 0`, then `2 ^ s` divides `(q - 1) o` or `(q + 1) o`.
This follows from lifting the exponent at `2`. 

### `two_pow_le_of_pow_eq_one`

 If q is an integer with |q| > 1, o is a nonzero natural number and q^o ≡ 1 mod 2^(s+1), then
2^s ≤ (|q| + 1)·o.

A consequence of the lifting-the-exponent lemma at the prime 2. It gives a lower bound for the
multiplicative order of q modulo 2^(s+1). 

 ## Decomposition of rational primes in K 

### `q_eq_iff_chiK_ne_neg_one`

 Let `d` be a prime `≡ 7 mod 8` and `w` a prime of `K = ℚ(√-d)` above the rational prime `p`.
Then the absolute norm `w.q` of `w` is `p` if and only if the Legendre symbol
`chiK d p = (p / d)` is not `-1`. 

### `span_eq_or_exists_span_eq_mul`

 Let `d ≡ 3 mod 4` and let `w` be a place of `K = ℚ(√-d)` over the prime `p`. Write `u.q` for
the absolute norm of a place `u`. Either `p` is inert, that is, `(p) = w` and `w` has norm `p ^ 2`,
or `(p) = w J` for a place `J`, and `w` and `J` both have norm `p` (here `J = w` is allowed: the
ramified case). 

### `prime_inert_or_eq_mul`

 Let `d ≡ 3 mod 4` and let `w` be a place of `K = ℚ(√-d)` over the prime `p`. Write `u.q` for
the absolute norm of a place `u`. There is a place `J` such that
(a) the places over `p` are exactly `w` and `J`;
(b) either `J = w` has norm `p ^ 2` (the inert case), or `w` and `J` both have norm `p` and
`(p) = w J` (here `J = w` is allowed: the ramified case). 
