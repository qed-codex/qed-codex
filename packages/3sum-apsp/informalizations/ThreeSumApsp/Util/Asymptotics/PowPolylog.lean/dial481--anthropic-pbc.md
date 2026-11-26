---
{
  "module": "ThreeSumApsp/Util/Asymptotics/PowPolylog.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Util/Asymptotics/PowPolylog.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Util/Asymptotics/PowPolylog.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Calculating with `O(n^a)` and `Õ(n^a)`

Closure properties of the two classes `IsBigOPow f a`, that is `f(n) = O(n^a)`, and
`IsPowPolylog f a`, that is `f(n) = O(n^a (log n)^{O(1)})`, which the paper writes `Õ(n^a)`.

A bound enters by `of_abs_le`, by `of_isBigO`, or from the model functions (`isBigOPow_rpow`,
`isBigOPow_natCast_pow`, `isBigOPow_const`, `isPowPolylog_rpow_mul_log_pow`, `isPowPolylog_log_pow`,
and for rounded powers `isBigOPow_ceil_rpow`, `isBigOPow_floor_rpow` and their inverses;
`IsBigOPow.natCeil` for rounding in general). Both classes are closed under sums, constant factors
and passing to a smaller function (`mono_left`). A product has the exponent `a + b` and a power the
exponent `a * k` (`pow`, `rpow`), to be brought to the wanted form by `mono`, which asks only for an
inequality between exponents. Substituting `n ↦ size n` multiplies nonnegative exponents
(`IsBigOPow.comp`, `IsPowPolylog.comp`), for `size n = O(n^μ)`, and then `log (size n) = Õ(1)`
(`IsBigOPow.isPowPolylog_log_natCast`). The classes are related by `IsBigOPow.isPowPolylog` and,
with a loss in the exponent, `IsPowPolylog.isBigOPow`; `eventually_abs_le` absorbs the constant as
well.


 ### `O(n^a)` 

### `isBigOPow_rpow`

 `n ^ a = O(n^a)`. 

### `isBigOPow_natCast_pow`

 `n ^ k = O(n^k)` for a natural number `k`. 

### `isBigOPow_natCast`

 `n = O(n^1)`. 

### `isBigOPow_const`

 A constant is `O(n^0)`. 

### `of_abs_le`

 A bound `|f n| ≤ C * n ^ a` from some `n₀` on gives `f = O(n^a)`. 

### `of_isBigO`

 If `g = O(n^a)` and `f = O(g)`, then `f = O(n^a)`. 

### `mono_left`

 If `|f n| ≤ |g n|` for all large `n` and `g = O(n^a)`, then `f = O(n^a)`. 

### `mono_left_of_nonneg`

 If `0 ≤ f n ≤ g n` for all large `n` and `g = O(n^a)`, then `f = O(n^a)`. 

### `mono`

 The exponent may be raised. 

### `add`

 `O(n^a) + O(n^a) = O(n^a)`. 

### `mul`

 `O(n^a) · O(n^b) = O(n^(a+b))`. 

### `rpow`

 `O(n^a) ^ r = O(n^(a r))` for a real exponent `r ≥ 0`. 

### `pow`

 `O(n^a) ^ k = O(n^(a k))` for a natural number `k`. 

### `const_mul`

 Constant factors are absorbed. 

### `abs`

 If `f = O(n^a)` then `|f| = O(n^a)`. 

### `eventually_abs_le`

 The constant is absorbed: if `f = O(n^a)` and `a < b`, then `|f n| ≤ n ^ b` for all large `n`.


### `isPowPolylog`

 `O(n^a) ⊆ Õ(n^a)`. 

### `IsBigOPow.natCeil`

 Rounding up keeps the class: if `f = O(n^a)` with `a ≥ 0`, then `⌈f n⌉ = O(n^a)`. 

### `isBigOPow_ceil_rpow`

 `⌈n ^ μ⌉ = O(n^μ)` for `μ ≥ 0`. 

### `isBigOPow_floor_rpow`

 `⌊n ^ μ⌋ = O(n^μ)`. 

### `isBigOPow_inv_ceil_rpow`

 `⌈n ^ μ⌉⁻¹ = O(n^(-μ))`. 

### `isBigOPow_inv_floor_rpow`

 `⌊n ^ μ⌋⁻¹ = O(n^(-μ))` for `μ ≥ 0`. 

 ### `Õ(n^a)` 

### `isPowPolylog_rpow_mul_log_pow`

 `n ^ a * (log n) ^ e = Õ(n^a)`. 

### `isPowPolylog_rpow_mul_log`

 `n ^ a * log n = Õ(n^a)`. 

### `isPowPolylog_rpow`

 `n ^ a = Õ(n^a)`. 

### `isPowPolylog_log_pow`

 `(log n) ^ e = Õ(1)`. 

### `isPowPolylog_log`

 `log n = Õ(1)`. 

### `isPowPolylog_const`

 A constant is `Õ(1)`. 

### `of_abs_le`

 A bound `|f n| ≤ C * (n ^ a * (log n) ^ e)` from some `n₀` on gives `f = Õ(n^a)`. 

### `of_isBigO`

 If `g = Õ(n^a)` and `f = O(g)`, then `f = Õ(n^a)`. 

### `mono_left`

 If `|f n| ≤ |g n|` for all large `n` and `g = Õ(n^a)`, then `f = Õ(n^a)`. 

### `mono_left_of_nonneg`

 If `0 ≤ f n ≤ g n` for all large `n` and `g = Õ(n^a)`, then `f = Õ(n^a)`. 

### `mono`

 The exponent may be raised. 

### `add`

 `Õ(n^a) + Õ(n^a) = Õ(n^a)`. 

### `const_mul`

 Constant factors are absorbed. 

### `mul_const`

 Constant factors are absorbed. 

### `mul`

 `Õ(n^a) · Õ(n^b) = Õ(n^(a+b))`. 

### `pow`

 `Õ(n^a) ^ k = Õ(n^(a k))` for a natural number `k`. 

### `rpow`

 `Õ(n^a) ^ r = Õ(n^(a r))` for a real exponent `r ≥ 0`. 

### `abs`

 If `f = Õ(n^a)` then `|f| = Õ(n^a)`. 

### `congr`

 If `f = Õ(n^a)` and `g n = f n` for all large `n`, then `g = Õ(n^a)`. 

### `isBigOPow`

 Logarithms are absorbed: `Õ(n^a) ⊆ O(n^b)` for `a < b`. 

### `eventually_abs_le`

 The constant and the logarithms are absorbed: if `f = Õ(n^a)` and `a < b`, then `|f n| ≤ n ^ b`
for all large `n`. 

### `IsBigOPow.isPowPolylog_log_natCast`

 If `size n = O(n^μ)` for some `μ`, then `log (size n) = Õ(1)`. 

### `IsBigOPow.comp`

 Substituting a size: if `G(s) = O(s^a)` and `size n = O(n^μ)` with `a, μ ≥ 0`, then
`G(size n) = O(n^(a μ))`. The sizes need not tend to infinity. 

### `IsPowPolylog.comp`

 Substituting a size: if `G(s) = Õ(s^a)` and `size n = O(n^μ)` with `a, μ ≥ 0`, then
`G(size n) = Õ(n^(a μ))`. The sizes need not tend to infinity. 

### `isPowPolylog_rpow_mul_log_add_one_pow`

 `n ^ a * (log n + 1) ^ e = Õ(n^a)`. 

### `isPowPolylog_log_mul_rpow`

 `log (c * n ^ κ) = Õ(1)`. 
