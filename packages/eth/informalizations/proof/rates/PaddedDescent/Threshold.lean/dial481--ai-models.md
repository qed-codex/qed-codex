---
{
  "module": "proof/rates/PaddedDescent/Threshold.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/Threshold.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/Threshold.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # From which n on the overhead is paid for, and the choice of s from n

The algorithm for precision s has overheads that depend on Y = (3·K_t⁸)² and only mildly on n. This
file proves that an overhead of at most
c·Y^a·(√n + 1) is at most ⌊n/2^s⌋ as soon as n ≥ Y^(2a+2), and that s = sOf n ≥ 1 makes n that
large. Besides Params.lean, Seq.lean and Choice.lean
it uses Mathlib only. 

 ### The number of binary digits against the square root 

### `size_le_sqrt`

 The number of binary digits of n is at most 2·⌊√n⌋ + 2. 

 ### The threshold 

### `lin_lt_Ytop`

 52s + 694 < Y (far from sharp). 

### `overhead_mul_le`

 If n ≥ Y^(2a+2) then an overhead W ≤ c·Y^a·(⌊√n⌋+1), with c ≤ 2^500, satisfies W·2^s ≤ n. 

### `overhead_le_div`

 The same with the division: W ≤ ⌊n/2^s⌋. 

### `Ytop_pow_le`

 Y^p ≤ 2^(2^(t+211)), t = depthOf s, for every p ≤ 2^200. 

 ### The choice of s from n 

### `two_pow_two_pow_log2_log2_le`

 2^(2^⌊log₂⌊log₂ n⌋⌋) ≤ n as soon as n ≥ 2. 

### `sOf_mul_add_le`

 If sOf n ≥ 1 then depthOf (sOf n) + 211 ≤ ⌊log₂⌊log₂ n⌋⌋. 

### `two_pow_two_pow_sOf_le`

 If sOf n ≥ 1 then 2^(2^(depthOf (sOf n) + 211)) ≤ n. 

### `Ytop_sOf_pow_le`

 If sOf n ≥ 1 then Y^p ≤ n for Y = Ytop (sOf n) and every p ≤ 2^200. 

### `overhead_sOf_le_div`

 The threshold and the choice of s together: if sOf n ≥ 1 then an overhead W ≤ c·Y^a·(⌊√n⌋+1),
with Y = Ytop (sOf n), c ≤ 2^500 and
2a + 2 ≤ 2^200, is at most ⌊n/2^(sOf n)⌋. 
