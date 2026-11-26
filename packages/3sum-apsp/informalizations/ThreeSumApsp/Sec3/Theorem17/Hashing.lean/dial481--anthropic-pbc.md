---
{
  "module": "ThreeSumApsp/Sec3/Theorem17/Hashing.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec3/Theorem17/Hashing.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec3/Theorem17/Hashing.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Theorem 17, first step: hashing modulo a prime

The first step of the proof of Theorem 17 reduces the weights modulo a prime `p` in the range
`[√D/2, √D)` with few false positives.

* **Counting.**  The number of triples with `S(a,b,c) ≡ 0 (mod p)` is `F(p) + Z₀`
  (`TriangleInstance.countZeroMod_eq`), and it can be read off the product of two matrices over
  `ℤ[x]/(x^p − 1)` (`TriangleInstance.coeff_matP_mul_matQ`,
  `TriangleInstance.F_add_Z₀_eq_sum_coeff`).  There are fewer than `√D` primes in the range
  (`card_primesInRange_lt`).
* **Selecting.**  The prime with the smallest count exists
  (`TriangleInstance.exists_isSelectedPrime`) and has the fewest false positives
  (`TriangleInstance.IsSelectedPrime.F_le`).
* **The bound on `F(p)`**, `TriangleInstance.F_le_of_le_card_primesInRange` and
  `TriangleInstance.exists_F_le`.  A triple is a false positive of at most `log_{√D/2}(3n^ν)` primes
  in the range (`TriangleInstance.card_falsePositive_primes_le`), so the numbers `F(q)` add up to at
  most `n³` times that (`TriangleInstance.sum_F_le`); there are `Ω(√D/log D)` primes in the range
  (`exists_le_card_primesInRange`); `F(p)` is at most the average
  (`TriangleInstance.IsSelectedPrime.F_mul_card_le_sum`); and `log D ≤ 4 log(√D/2)`
  (`log_le_four_mul_log_sqrt_div_two`).  The constant of the bound has a name,
  `Hashing.falsePositiveConst`.


 ### The primes in the range 

### `mem_primesInRange`

 Proof of Theorem 17, "a prime p ∈ [√D/2, √D)": the primes in the range are the primes `p` with
`√D/2 ≤ p < √D`.  (The bound `p < D` in the definition excludes none of them.) 

 ### The ring `ℤ[x]/(x^p − 1)` 

### `CyclicRing`

 Proof of Theorem 17: "the ring ℤ[x]/(x^p − 1)".  (`Polynomial.C 1` is the constant polynomial
1.) 

### `x`

 The element `x` of `ℤ[x]/(x^p − 1)`. 

### `coeff`

 Proof of Theorem 17: "the coefficient of x^r" in an element `z` of `ℤ[x]/(x^p − 1)`, for `0 ≤ r
< p`, as a linear map: the coefficient of `x^r` in the unique polynomial of degree less than `p`
that represents `z` (Mathlib's `AdjoinRoot.modByMonicHom` gives that polynomial; it asks for the
fact that `x^p − 1` is monic, which holds as `p ≠ 0`). 

### `coeff_apply`

 The coefficient, in terms of the representing polynomial. 

### `x_pow_self`

 In `ℤ[x]/(x^p − 1)` we have `x^p = 1`. 

### `coeff_x_pow`

 The coefficient of `x^r` in the power `x^k` of `ℤ[x]/(x^p − 1)` is 1 if `r = k mod p` and 0
otherwise. 

### `eq_add_toNat_emod_iff`

 A number `r < p` is the sum of the residues of `u` and `v` in `{0, …, p − 1}`, reduced modulo
`p`, exactly if `u + v ≡ r`. 

 ### Counting the triples with `S(a,b,c) ≡ 0 (mod p)` 

### `IsFalsePositive`

 Proof of Theorem 17: "A false positive of p is a triple (a,b,c) with S(a,b,c) ≠ 0 and p ∣
S(a,b,c)". 

### `F`

 Proof of Theorem 17: "let F(p) denote the number of false positives of p". 

### `Z₀`

 Proof of Theorem 17: "Z₀, the number of zero triangles". 

### `countZeroMod_eq`

 Proof of Theorem 17: "This number is the number of false positives F(p) plus Z₀, the number of
zero triangles, which does not depend on p." 

### `matP`

 Proof of Theorem 17: "let P[a,c] := x^{w(a,c) mod p}", a matrix over `ℤ[x]/(x^p − 1)`.  `w mod
p` is the residue in `{0, …, p − 1}`. 

### `matQ`

 Proof of Theorem 17: "and Q[c,b] := x^{w(b,c) mod p}". 

### `coeff_matP_mul_matQ`

 Proof of Theorem 17: "the coefficient of x^r in (PQ)[a,b] is the number of c ∈ C with w(a,c) +
w(b,c) ≡ r (mod p)". 

### `F_add_Z₀_eq_sum_coeff`

 Proof of Theorem 17: "then F(p) + Z₀ is the sum over the pairs (a,b) ∈ A × B of the coefficient
of x^{−w(a,b) mod p} in (PQ)[a,b]". 

### `card_primesInRange_lt`

 Proof of Theorem 17: "the fewer than √D primes in the range". 

 ### Selecting the prime 

### `exists_isSelectedPrime`

 Proof of Theorem 17.  There is a prime to select. 

### `IsSelectedPrime.F_le`

 Proof of Theorem 17: "We select the prime with the smallest count, which is also the prime with
the fewest false positives". 

 ### The bound on the number of false positives of the selected prime 

### `abs_S_le`

 Proof of Theorem 17: "|S(a,b,c)| ≤ 3n^ν". 

### `card_falsePositive_primes_le`

 Proof of Theorem 17: "a triple with S(a,b,c) ≠ 0 is a false positive exactly of the primes in
the range that divide S(a,b,c).  Since 0 < |S(a,b,c)| ≤ 3n^ν and these primes are at least √D/2,
there are at most log_{√D/2}(3n^ν) of them." 

### `sum_F_le`

 Proof of Theorem 17: "Hence the numbers of false positives of all the primes in the range add up
to at most n³ log_{√D/2}(3n^ν)." 

### `exists_le_card_primesInRange`

 Proof of Theorem 17: "By the prime number theorem there are Ω(√D/log D) primes in the range".

NOTE.  The proof of Theorem 17 needs this for every `D ≥ 16`, not only for large `D`, and so it is
stated.  It follows from a counting form of Bertrand's postulate; the prime number theorem is not
needed. 

### `TriangleInstance.IsSelectedPrime.F_mul_card_le_sum`

 Proof of Theorem 17: "F(p) is at most the average over them", multiplied out. 

### `log_le_four_mul_log_sqrt_div_two`

 Proof of Theorem 17: "log D = O(log(√D/2)) for D ≥ 16". 

### `TriangleInstance.F_le_of_le_card_primesInRange`

 Proof of Theorem 17: "F(p) is at most the average over them, so [...] F(p) = O(n³
log(3n^ν)/√D)": if there are at least `c √D/log D` primes in the range, then `F(p) ≤ (4/c) n³
log(3n^κ)/√D`. 

### `TriangleInstance.exists_F_le`

 Proof of Theorem 17: "F(p) = O(n³ log(3n^ν)/√D) = O(ν n³ log n/√D)". 

### `Hashing.falsePositiveConst`

 A name for the constant in "F(p) = [...] = O(ν n³ log n/√D)", for the bounds on running times
that are built on this one. 

### `Hashing.one_le_falsePositiveConst`

 The constant is at least 1. 

### `Hashing.F_le_falsePositiveConst_mul`

 Proof of Theorem 17: "F(p) = [...] = O(ν n³ log n/√D)", with `Hashing.falsePositiveConst` as the
constant. 
