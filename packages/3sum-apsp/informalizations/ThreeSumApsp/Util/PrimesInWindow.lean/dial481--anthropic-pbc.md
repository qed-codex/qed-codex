---
{
  "module": "ThreeSumApsp/Util/PrimesInWindow.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Util/PrimesInWindow.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Util/PrimesInWindow.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Counting the primes in a window of ratio two

The proof of Theorem 17 says: "By the prime number theorem there are Ω(√D / log D) primes
in the range", the range being `[√D/2, √D)`, and it uses this for every `16 ≤ D ≤ n`, not only for
large `D`.  This file proves the bound for every `D ≥ 16`, with some positive constant.

## Main results

* `Nat.exists_forall_mul_div_log_le_card_primes`: there is a `c > 0` such that for every real
  `x ≥ 4` there are at least `c · x / log x` primes `p` with `x/2 ≤ p < x`;
  `Nat.exists_prime_half_le_and_lt`: there is one.
* `Nat.exists_forall_mul_sqrt_div_log_le_card_primes`: there is a `c > 0` such that for every
  natural number `D ≥ 16` there are at least `c · √D / log D` primes `p` with `√D/2 ≤ p < √D`. This
  is the sentence of the proof of Theorem 17.

## The proof

The prime number theorem is not needed: Erdős's proof of Bertrand's postulate, read as a count
instead of as an existence statement, is enough.  Write `k` for the number of primes in `(n, 2n]`.

1. Split the prime factorization of the central binomial coefficient `C(2n, n)`.  Every prime power
   in it is at most `2n` (`prod_pow_factorization_le`), so the primes up to `√(2n)` contribute at
   most `(2n)^√(2n)` and the primes in `(n, 2n]` at most `(2n)^k`.  A prime above `√(2n)` occurs at
   most once, and the primes in `(2n/3, n]` do not occur at all, so the primes in `(√(2n), n]`
   contribute at most `4^(2n/3)` (`prod_middle_le`).  Together: `centralBinom_le`.
2. An elementary estimate: `n^6 · (2n)^(6√(2n)) ≤ 2^n` for `n ≥ 16562`
   (`pow_mul_pow_sqrt_le_two_pow`).
3. With `4^n < n · C(2n, n)` the two give `2^n ≤ (2n)^(2k)`, that is, `k ≥ n / (2 log₂ (2n))`, for
   `n ≥ 16562` (`two_pow_le_of_large`).
4. A window `[x/2, x)` with real endpoints contains `(n, 2n]` for an `n ≥ x/4`
   (`exists_nat_window`).  If `n ≥ 16562`, step 3 applies.  If not, `x` is bounded, and the one
   prime of Bertrand's postulate is enough.
5. The case `x = √D`.

## Credit

Mathlib proves Bertrand's postulate by the same argument.  The proofs of `centralBinom_le` (with
`prod_middle_le`), `concaveOn_log_add_sqrt_mul_log_sub` and `log_add_sqrt_mul_log_le` are adapted
from Mathlib, Mathlib/NumberTheory/Bertrand.lean (Copyright (c) 2020 Patrick Stevens, released under
the Apache 2.0 license; authors: Patrick Stevens, Bolton Bailey).


### `bertrandPrimes`

 The primes `p` with `n < p ≤ 2n`: the primes that Bertrand's postulate is about. 

### `mem_bertrandPrimes`

 Membership in `bertrandPrimes`, spelled out. 

 ## 1. Erdős's upper bound for the central binomial coefficient 

### `prod_pow_factorization_le`

 Every prime power in `C(2n, n)` is at most `2n`, so `|s|` of them multiply to at most
`(2n)^|s|`. 

### `prod_middle_le`

 The primes in `(√(2n), n]` contribute at most `4^(2n/3)` to `C(2n, n)`: their exponent is at
most 1, it is 0 above `2n/3`, and the product of the primes up to `2n/3` is at most `4^(2n/3)`.
Adapted from Mathlib, Mathlib/NumberTheory/Bertrand.lean, Apache 2.0. 

### `centralBinom_le`

 Erdős's bound, keeping the primes of `(n, 2n]`:
`C(2n, n) ≤ (2n)^√(2n) · 4^(2n/3) · (2n)^k`, where `k` is the number of primes in `(n, 2n]`.
Mathlib proves the case `k = 0` on the way to Bertrand's postulate
(`centralBinom_le_of_no_bertrand_prime`).  Adapted from Mathlib, Mathlib/NumberTheory/Bertrand.lean,
Apache 2.0. 

 ## 2. The elementary estimate `n^6 · (2n)^(6√(2n)) ≤ 2^n` for `n ≥ 16562` 

### `concaveOn_log_add_sqrt_mul_log_sub`

 For `a ≥ 0` the function `log x + √(2x) · log (2x) - a x` is concave for `x > 1/2`.
Adapted from Mathlib, Mathlib/NumberTheory/Bertrand.lean, Apache 2.0 (there inside
`Bertrand.real_main_inequality`, for `a = log 4 / 3`). 

### `log_add_sqrt_mul_log_le`

 `log x + √(2x) · log (2x) ≤ (log 2 / 6) · x` for `x ≥ 16562`.  The difference of the two sides
is concave, it is nonnegative at `x = 2` and nonpositive at `x = 16562 = 2 · 91²` (where
`√(2x) = 182`; the only numerical input is `91^13 ≤ 2^85`), so it is nonpositive from there on.
Adapted from Mathlib, Mathlib/NumberTheory/Bertrand.lean, Apache 2.0 (the same argument proves
`Bertrand.real_main_inequality` there, with other numbers). 

### `pow_mul_pow_sqrt_le_two_pow`

 The same estimate for natural numbers, without logarithms. 

 ## 3. The count for `n ≥ 16562` 

### `two_pow_le_of_large`

 `2^n ≤ (2n)^(2k)` for `n ≥ 16562`.  If it failed, the sixth power of
`4^n < n · (2n)^√(2n) · 4^(2n/3) · (2n)^k` would give
`2^(12n) < (n^6 (2n)^(6√(2n))) · 2^(8n) · 2^(3n) ≤ 2^(12n)`. 

### `mul_log_two_le_card_bertrandPrimes_mul_log`

 The count of step 3 with natural logarithms: `n log 2 ≤ 2 k log (2n)`. 

 ## 4. Half-open windows `[x/2, x)` with real endpoints 

### `exists_nat_window`

 For a real `x ≥ 4` the natural number `n = ⌈x/2⌉ - 1`, written below as `(⌈x⌉ - 1) / 2`,
satisfies `n ≥ 1`, `n ≥ x/4` and `2n < x`, and every natural number in `(n, 2n]` lies in `[x/2, x)`.


### `exists_prime_half_le_and_lt`

 For every real `x ≥ 4` there is a prime `p` with `x/2 ≤ p < x`, by Bertrand's postulate. 

### `div_log_le_card_of_large`

 If `(n, 2n]` lies in the window and `n ≥ x/4` is large, the window has at least `x / (12 log x)`
primes: `(x/4) log 2 ≤ n log 2 ≤ 2 k log (2n) ≤ 2 k log x`, and `log 2 ≥ 2/3`. 

### `exists_forall_mul_div_log_le_card_primes`

 There is a `c > 0` such that, for every real `x ≥ 4`, every finite set of natural numbers that
contains all primes `p` with `x/2 ≤ p < x` has at least `c · x / log x` elements.  (This form
applies to the set of those primes however it is written down.) 

 ## 5. The window `[√D/2, √D)` of the proof of Theorem 17 

### `exists_forall_mul_sqrt_div_log_le_card_primes`

 Proof of Theorem 17: "there are Ω(√D / log D) primes in the range".  There is a `c > 0` such
that, for every natural number `D ≥ 16`, every finite set of natural numbers that contains all
primes `p` with `√D/2 ≤ p < √D` has at least `c · √D / log D` elements. 
