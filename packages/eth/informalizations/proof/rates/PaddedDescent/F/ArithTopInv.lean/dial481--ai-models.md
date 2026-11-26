---
{
  "module": "proof/rates/PaddedDescent/F/ArithTopInv.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/ArithTopInv.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/ArithTopInv.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The invariant at the top, and the budgets of the top

The invariant of the descent holds at the top level for the network of marks; the fixed numbers X,
Z, Qm, Wm, L of `PaddedDescent/F/ArithGlob.lean` satisfy what the
invariant needs of them; all overheads together are below n/2^s; the enumerations of the rebalancing
at the top (colourings, states, labels, indices of a table) and the rounds of the walk fit under a
pad
of length 2^(8·X); the number of layers is large enough. Everywhere s is the precision, n the number
of variables, and the only hypothesis that ties them is
Y⁶ ≤ n for Y = `Ytop s`. No programs occur here. 

 ### K_t, g_t and Y 

### `one_le_Ktop`

 1 ≤ K_t. 

### `one_le_Ytop`

 1 ≤ Y. 

### `Ktop_le_gtop`

 K_t ≤ `gtop` = 3·K_t⁸. 

### `gtop_pos`

 `gtop` is positive. 

### `gtop_le_Ytop`

 `gtop` is at most its square Y. 

### `hundred_Ktop_pow_four_le`

 100·K_t⁴ ≤ Y. 

### `hundred_Ktop_sq_le`

 100·K_t² ≤ Y. 

### `Ytop_ge`

 100 ≤ Y. 

### `Ytop_sq_le`

 Y² ≤ n follows from Y⁶ ≤ n. 

### `hundred_Ytop_le`

 100·Y ≤ n follows from Y⁶ ≤ n. 

 ### The bounds Ub and Pb of the network of marks 

### `lin_le_two_pow`

 s + 8 ≤ 8·2^s. 

### `coeff_le`

 4·(s + 8)⁶ ≤ 2^(6s+20). 

### `cube_le_Ytop`

 8·(s + 8)³ + 1 ≤ Y. 

### `Ubof_le`

 Ub ≤ 4·(s + 8)⁶·n + 8·(s + 8)²·Y, for every width k ≤ s. 

### `coeff_le_Ktop`

 4·(s + 8)⁶·2^s ≤ K_t. 

### `size_coeff_le_Ktop`

 16·(β + 2)·(Δ + 4)·2^s ≤ K_t, with β = `betaOf s`, for every Δ ≤ 2^β. 

 ### What the invariant needs of the fixed numbers 

### `Zof_ge`

 25·K_t² ≤ 2·Z. 

### `Zof_le_Qmof`

 Z ≤ Qm. 

### `rest_le_Zof`

 K_t² + 8·(s + 8)²·Y ≤ Z. 

### `Qmof_lt`

 Qm + 1 ≤ 2^L. 

### `lt_two_pow_Lof`

 n < 2^L. 

### `poly_le`

 The polynomial factor in the length of an instance is at most 2^(2L). 

 ### All overheads together are below n/2^s 

### `Lof_le`

 L ≤ 2·Y·(⌊√n⌋+1). 

### `small`

 The sum of all overheads: 5·Z + L·(2·K_t² + 2) + 1 + K_t ≤ ⌊n/2^s⌋. 

### `exponents_le`

 One inequality that dominates the exponents of all budgets. 

### `Ytop_le_Xof`

 65·Y ≤ X. 

 ### The invariant at the top 

### `four_mul_Pbof_le`

 4·g·Pb ≤ K_t·X, for g = `gtop s`. 

### `inv_at_top`

 The invariant holds at the top level, for the instance that the rebalancing makes of a network
of marks. 

 ### The budgets at the top, and the rounds of the walk 

### `two_pow_le_of_le`

 A power of two with exponent at most 8·X is at most the length F of the pad, if 2^(8·X) ≤ F. 

### `top_col`

 Field col of NetFits: the colourings at the top. 

### `top_st`

 Field st of NetFits: the states of a class at the top. 

### `top_lab`

 Field lab of NetFits: the labels inside a class at the top. 

### `top_tab`

 Field tab of NetFits: the indices of a table at the top. 

### `top_rounds`

 Conjunct 3 of StAW: the rounds of the walk. 

 ### The layers 

### `layers_last`

 Field last of MarkFits: after `layersOf s` divisions, each of which keeps at most two thirds of
the clauses, fewer than n + 2 clauses are left. 

### `clauses_le`

 Field m_le of MarkFits: the number of clauses is at most 2^β·(n + 1). 
