---
{
  "module": "proof/rates/PaddedDescent/Seq.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/Seq.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/Seq.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The sequence K_j

K_j = 2^(k_j) with k_j = 104·2^j − 2j − 96 in closed form; K_{j+1} = g_j²; K_j lies between 256·4^j
and 2^(104·2^j); small facts about K_j, g_j and
the numbers K_t, Y of the top level. Besides Params.lean it uses Mathlib only. 

 ### The exponents k_j 

### `kseq_closed`

 The closed form: k_j + 2j + 96 = 104·2^j. 

### `kseq_ge`

 94j + 8 ≤ k_j. 

### `kseq_le`

 k_j ≤ 104·2^j. 

### `kseq_strictMono`

 k_j grows strictly with j. 

 ### K_j and g_j 

### `Kseq_zero`

 K₀ = 256. 

### `gseq_eq`

 g_j = 2^(k_j + 47 + j). 

### `Kseq_succ_eq_mul`

 K_{j+1} = g_j·g_j. 

### `Kseq_succ_eq_sq`

 K_{j+1} = g_j². 

### `Kseq_lower`

 Lower bound: 256·4^j ≤ K_j. 

### `Kseq_ge`

 256 ≤ K_j. 

### `Kseq_pos`

 K_j is positive. 

### `Kseq_upper`

 Upper bound: K_j ≤ 2^(104·2^j). 

### `Kseq_strictMono`

 K_j grows strictly with j. 

### `two_pow_mul_Kseq_le_gseq`

 2^47·K_j ≤ g_j. 

### `Kseq_le_gseq`

 K_j ≤ g_j. 

 ### The top level 

### `gtop_eq`

 `gtop` = 3·K_t⁸, the number of nodes of the network of a formula. 

### `Ytop_eq_sq`

 Y is the square of `gtop`. 

### `Ytop_eq`

 Y = 9·K_t¹⁶. 

### `two_pow_le_kseq`

 2^j ≤ k_j: the exponents grow like 104·2^j. 

### `two_pow_le_Ktop`

 2^e ≤ K_t for every e ≤ 2^t, t the number of levels. 

### `Ktop_lower`

 2^(52s+692) ≤ K_t (far from sharp: k_t ≥ 94·(⌊19s/3⌋ + 700) + 8). 

### `Ktop_pos`

 K_t is positive. 

### `mul_Ktop_pow_le_Ytop`

 C·K_t^e ≤ Y for e ≤ 15 and C ≤ 2^500. 

### `Ktop_le_Ytop`

 K_t ≤ Y. 

### `Ytop_pos`

 Y is positive. 

### `Ytop_lower`

 2^(52s+694) ≤ Y (far from sharp, like `Ktop_lower`). 

### `Ytop_le`

 Y ≤ 2^(2^(t+11)), t the number of levels. 
