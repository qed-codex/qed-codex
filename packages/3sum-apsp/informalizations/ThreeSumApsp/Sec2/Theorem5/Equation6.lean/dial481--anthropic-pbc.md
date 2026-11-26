---
{
  "module": "ThreeSumApsp/Sec2/Theorem5/Equation6.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec2/Theorem5/Equation6.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec2/Theorem5/Equation6.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Section 2.4.4: the two consequences of `N ≥ D^18`

Here `L = 19m`, `D = 4^m`, `N₀ = 3^{18m}` and `K = binom(19m, m)`.

* First consequence: `K₀ N₀ ≤ K N₀ ≤ D^18 ≤ N` (`K_mul_N0_le`, `K0_mul_N0_le`), so the padding at
  most doubles `N` (`padN_le_two_mul_of_D_pow_le`).  It follows from `binom(L, m) ≤ (eL/m)^m`
  (`Nat.choose_le_exp_mul_div_pow`) and `19e · 3^18 < 4^18` (`nineteen_mul_exp_mul_three_pow_lt`).
* Second consequence, equation (6): `10^L ≤ 2^{-m/9} N N₀` (`eq_6`).  It follows from
  `10^19 · 2^{1/9} / 3^18 < 4^18` (`ten_pow_mul_two_rpow_div_three_pow_lt`), raised to the power `m`
  (`ten_pow_div_N0_le`).


### `K_le_pow`

 Section 2.4.4: "using the general bound binom(L, m) ≤ (eL/m)^m, we have
K = binom(19m, m) ≤ (19e)^m".  The general bound is `Nat.choose_le_exp_mul_div_pow`.

NOTE.  The printed bound divides by `m`.  In Lean a quotient by 0 is 0 and `0^0 = 1`, so for `m = 0`
both sides are 1 and no hypothesis `m ≥ 1` is needed. 

### `nineteen_mul_exp_mul_three_pow_lt`

 Section 2.4.4: "19e · 3^18 < 4^18". 

### `four_pow_eq`

 `4^{18m} = D^18`. 

### `K_mul_N0_le_D_pow`

 Section 2.4.4: "so K N₀ ≤ (19e · 3^18)^m ≤ 4^{18m}", and `4^{18m} = D^18`. 

### `K_mul_N0_le`

 Section 2.4.4, the first consequence of `N ≥ D^18`: "K N₀ ≤ D^18 ≤ N." 

### `K0_mul_N0_le`

 Section 2.4.4, the first consequence of `N ≥ D^18`: "and hence K₀ N₀ ≤ K N₀ ≤ D^18 ≤ N." 

### `padN_le_two_mul_of_D_pow_le`

 Section 2.4.4: "This means the padding at most doubles N". 

### `ten_pow_mul_two_rpow_div_three_pow_lt`

 Section 2.4.4: "10^19 · 2^{1/9} / 3^18 < 4^18". 

### `ten_pow_div_N0_le`

 Section 2.4.4: "so 10^L · 2^{m/9} / N₀ ≤ D^18", for `L = 19m`. 

### `eq_6`

 **Equation (6)**, the second consequence of `N ≥ D^18`: "10^L ≤ 2^{-m/9} N N₀", for
`L = 19m`. 
