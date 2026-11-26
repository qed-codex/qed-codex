---
{
  "module": "Zeta23/MV/Quadratic.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/MV/Quadratic.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/MV/Quadratic.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# MV step 1 — the quadratic-form bound `U ≤ 73 V` (arXiv:2203.14950 Thm 1.2 shape)

`U := Σ_{m≠n} δ_m^{3/2} δ_n^{1/2} t_m t_n/(freq m − freq n)²  ≤  73 Σ t_n² ` for nonneg `t`:
Cauchy–Schwarz `U² ≤ V·W`; `W = S + T` (diagonal/off-diagonal of the expanded square);
`S ≤ 27V` (σ=4 spacing); `T ≤ 72U` (two-point lemma); the quadratic inequality gives `U ≤ 73V`.


### `Uform`

 The quadratic form `U = Σ_{m≠n} δ_m^{3/2} δ_n^{1/2} t_m t_n/(freq m − freq n)²`. 

### `sum_erase_comm`

 Swap the two layers of an `erase`-nested double sum. 

### `sum_erase_erase_comm`

 Swap the inner two layers of the distinct-triple sum (outer index `m` fixed). 

### `Uform_le`

 **Step 1**: `U ≤ 73 Σ t²` for admissible `(freq, δ)` and nonneg `t`. 
