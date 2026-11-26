---
{
  "module": "Zeta23/ZeroSide/TightMult.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ZeroSide/TightMult.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ZeroSide/TightMult.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/ZeroSide/TightMult.lean — Lemma R (Zeta23/ZeroSide/RankTraceMult.lean) is TIGHT, for every c > 0, on the configurations
"on-line atoms with integer multiplicities m_j ≤ c on orthonormal vectors ⊕ b pair-blocks Q = c·Π_b":
    2c·tr(P+Q) − ‖P+Q‖_F² = Σ_j k_c(m_j) + c²·b      (equality in rank_trace_mult_k / _k_le).
At c = 2 this says: simple zeros (m=1, k₂=3), DOUBLE zeros (m=2, k₂=4) and TIGHT PAIRS (a Q-block of eigenvalue 2, priced c²=4 per
pair) are all extremal simultaneously — the certificate (tr Ĝ, ‖Ĝ‖_F², integer atoms m_j on vectors of norm ≤ 1, n₊(Q) ≤ p) provably
cannot separate an on-line double zero from an off-line pair at depth → 0, and cannot be improved by any further inequality consuming
only these quantities.
-/
```

### `v`

 orthonormal on-line vectors: the standard basis vectors of the first r slots. 

### `mR`

 real multiplicities. 

### `Q`

 the pair blocks: c × (projection onto the last b slots). 

### `lemmaR_tight`

 **Lemma R is tight**: for on-line multiplicities 1 ≤ m_j ≤ c on orthonormal vectors and b pair-blocks of eigenvalue c,
   2c·tr(P+Q) − ‖P+Q‖² = Σ_j k_c(m_j) + c²b   — equality in rank_trace_mult_k. 

### `lemmaR_tight'`

 … with the hypotheses of Lemma R all met exactly (m_j ≥ 0, ‖v_j‖² = 1 ≤ 1, n₊(Q) = b). 

### `lemmaR_tight_two`

 c = 2: simples (m=1), doubles (m=2) and tight pairs are simultaneously extremal:
   4·tr − ‖·‖² = 3·#{m=1} + 4·#{m=2} + 4·b. 
