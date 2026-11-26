---
{
  "module": "ThreeSumApsp/Util/Ceil.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Util/Ceil.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Util/Ceil.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Ceilings of quotients and logarithms, floors and ceilings of roots

General facts about natural and real numbers. The quotient of two natural numbers, rounded up, is
Mathlib's `a ⌈/⌉ b`. It is computed by `Nat.ceilDiv_eq_add_pred_div : a ⌈/⌉ b = (a + b - 1) / b`.
It is the ceiling of the real quotient (`Nat.ceil_div_eq_ceilDiv`) and the least `k` with
`a ≤ k * b` (`Nat.ceilDiv_le_iff`, `Nat.lt_ceilDiv_iff`), so `a ≤ a ⌈/⌉ b * b < a + b`
(`Nat.le_ceilDiv_mul`, `Nat.ceilDiv_mul_lt`). The power of `b` with exponent `⌈log_b n⌉` is at most
`b * n` (`Nat.pow_clog_le_mul`). A natural number is compared with an `e`-th root by its `e`-th
power (`Real.natCast_le_rpow_inv_iff`, `Real.rpow_inv_le_natCast_iff`). `cbrtCeil n` is the cube
root of `n`, rounded up.


 ## The ceiling of a quotient of natural numbers 

### `ceilDiv_le_iff`

 `a ⌈/⌉ b ≤ k` says that `k` pieces of size `b` cover `a`. Mathlib's `ceilDiv_le_iff_le_mul` has
`b * k` on the right. 

### `lt_ceilDiv_iff`

 `i < a ⌈/⌉ b` says that `i` pieces of size `b` do not cover `a`. 

### `le_ceilDiv_mul`

 `a ⌈/⌉ b` pieces of size `b` cover `a`. 

### `ceilDiv_mul_lt`

 `a ⌈/⌉ b` pieces of size `b` overshoot `a` by less than one piece. 

### `ceilDiv_le_ceilDiv_right`

 More to cover needs at least as many pieces. 

### `ceil_div_eq_ceilDiv`

 The ceiling of the real quotient of two natural numbers, in natural numbers. 

 ## The ceiling of a logarithm

`Real.natCeil_logb_natCast : ⌈Real.logb b n⌉₊ = Nat.clog b n` passes from real to natural numbers,
and `Nat.le_pow_clog : 1 < b → x ≤ b ^ Nat.clog b x` is the lower bound. 

### `pow_clog_le_mul`

 Rounding `n ≥ 1` up to a power of `b` costs at most a factor `b`. 

 ## Roots

The `e`-th root of `t` is written `(t : ℝ) ^ ((e : ℝ)⁻¹)`. With these two lemmas,
`Nat.le_floor_iff` and `Nat.ceil_le`, its floor and its ceiling are described by powers of natural
numbers. 

### `natCast_le_rpow_inv_iff`

 `x` is at most the `e`-th root of `t` exactly if `x ^ e ≤ t`. 

### `rpow_inv_le_natCast_iff`

 The `e`-th root of `t` is at most `x` exactly if `t ≤ x ^ e`. 

### `cbrtCeil`

 The cube root of `n`, rounded up: `⌈n^{1/3}⌉`. 
