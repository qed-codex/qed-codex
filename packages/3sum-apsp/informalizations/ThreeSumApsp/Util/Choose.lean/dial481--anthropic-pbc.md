---
{
  "module": "ThreeSumApsp/Util/Choose.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Util/Choose.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Util/Choose.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Binomial coefficients

Upper bounds. A single summand of the binomial expansion of `(a + b) ^ n` is at most the whole sum
(`Nat.choose_mul_pow_mul_pow_le`); with `a = 1` this is `binom(n, k) * b ^ (n - k) ≤ (b + 1) ^ n`
(`Nat.choose_mul_pow_le`), which the paper uses with `b = 9`. And `binom(n, k) ≤ (e n / k) ^ k`
(`Nat.choose_le_exp_mul_div_pow`).

A lower bound. For `k ≤ n`, the largest of the `n + 1` terms `binom(n, j) k^j (n-k)^{n-j}` of the
expansion of `n^n = (k + (n-k))^n` is the one with `j = k`: the terms increase up to `j = k` and
decrease from there on. This gives the standard lower bound on a binomial coefficient
(`Nat.pow_self_le_mul_choose_mul_pow_mul_pow`), which Section 4.4 uses in the proof of Corollary 26
and, written with the entropy function as `e^{n H(k/n)}/(n+1) ≤ binom(n, k)`, in the proof of
Corollary 31.


 ## Upper bounds 

### `choose_mul_pow_mul_pow_le`

 One summand of the binomial expansion of `(a + b) ^ n` is at most `(a + b) ^ n`. 

### `choose_mul_pow_le`

 `binom(n, k) * b ^ (n - k) ≤ (b + 1) ^ n`. 

### `choose_le_exp_mul_div_pow`

 `binom(n, k) ≤ (e n / k) ^ k`: indeed `binom(n, k) ≤ n ^ k / k!`, and
`k ^ k / k! ≤ e ^ k` is one term of the exponential series. For `k = 0` both sides are `1`. 

 ## The largest term of a binomial expansion 

### `modeTerm`

 The term number `j` of the expansion of `n^n = (k + (n-k))^n`. 

### `modeTerm_succ_mul`

 The quotient of two consecutive terms is `(n - j) k / ((n - k) (j + 1))`. 

### `modeTerm_le_succ`

 The terms increase up to `j = k`. 

### `modeTerm_succ_le`

 The terms decrease from `j = k` on. 

### `modeTerm_le_mode`

 Every term is at most the term with `j = k`. 

### `pow_self_le_mul_choose_mul_pow_mul_pow`

 Proof of Corollary 26: "the standard bound binom(n, k) ≥ 1/(n+1) · n^n/(k^k (n-k)^{n-k})",
without fractions.  Of the `n + 1` terms of the expansion of `n^n = (k + (n-k))^n`, the one with
`binom(n, k)` is the largest. 
