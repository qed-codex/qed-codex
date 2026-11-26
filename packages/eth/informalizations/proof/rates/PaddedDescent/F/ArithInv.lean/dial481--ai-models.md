---
{
  "module": "proof/rates/PaddedDescent/F/ArithInv.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/ArithInv.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/ArithInv.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The invariant of the descent through the levels

An instance at level j has K_j nodes, labels of at most Λ bits and entries of at most B bits, and
the work list has at most cnt members. This file
states four inequalities (`Inv`) between these numbers and a few numbers that stay fixed during the
descent, proves that one level preserves them,
and derives from them the exponents of all the budgets of one level. No programs occur here. It is
groundwork for a rate theorem on top of the Lean
proof in this development that 3-SAT is decided in time O(2^{δn}) for every δ > 0 (which follows
from Theorem 2 of the paper). 

### `Inv`

 The four inequalities at level j. The numbers t (top level), X, Z, Qm, Wm, L stay fixed. With Q =
K_j²·Λ:
`geo`: Q ≤ (10000/8963)^j·X + Z; `crude`: Q ≤ Qm; `bits`: (B + 16·Qm)·K_j³ ≤ Wm; `count`:
cnt·2^(2·L·K_j²) ≤ 2^(2·L·K_t²). 

### `Kseq_succ_sq`

 K_{j+1}² = g_j⁴. 

### `Kseq_succ_cube`

 K_{j+1}³ = (g_j·g_j)³. 

### `Kseq_mono`

 K_i ≤ K_j for i ≤ j. 

### `pow_succ_le_mul_Kseq`

 10000^(j+1) ≤ 8963^(j+1)·K_j. 

### `pow_le_mul_Kseq`

 10000^j ≤ 8963^j·K_j. 

### `geo_step`

 The arithmetic of `Inv.step`, line `geo`, with plain variables (a = 8963^j, b = 10000^j, q' =
K²Λ', q = g⁴Λ, G = g⁴). 

### `bits_step`

 The arithmetic of `Inv.step`, line `bits`, with plain variables (K3 = K³, G6 = (g·g)³, G3 = g³,
q = g⁴Λ). 

### `count_step`

 The arithmetic of `Inv.step`, line `count`, with plain variables. 

### `Inv.step`

 One level preserves the invariant. 

### `Inv.mul_le`

 From the invariant at level j: K_j·Λ ≤ X + Z. 

### `Inv.succ_le`

 From the invariant at level j+1: g_j⁴·Λ ≤ K_j·(X + Z). 

### `Inv.st_le`

 The exponent of the settings of one group of the grouping, which has at most 2g/K nodes (as in
the proof of Lemma 1): Pn·(2g/K) ≤ 4·(X + Z). 

### `Inv.lab_le`

 The exponent of the labels of one node inside a group: Pn ≤ 2·(X + Z). 

### `Inv.pat_le`

 The patterns of one instance: (Λ+1)^nRect g ≤ 2^(L·K_t²). 

### `col_le`

 The groupings of the g nodes into K groups, functions [g] → [K] as in the proof of Lemma 1: K^g
≤ 2^(K_t). 

### `Inv.work_le`

 The work list at level j: cnt·instLen K_j Λ B + 2 ≤ 2^(2·L·K_t² + X + Z + Lw + 1). 

### `Inv.bottom_le`

 The brute force at the bottom: K₀(K₀−1)/2·Λ ≤ X + Z. 
