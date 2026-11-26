---
{
  "module": "Zeta23/PairCeiling/Defs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/PairCeiling/Defs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/PairCeiling/Defs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/PairCeiling/Defs.lean — shared definitions for the bandwidth-1 pair-correlation CEILING theorem
(analytic half: Stability.lean; numeric-certificate half: NumericCert.lean, RowCert.lean).

Weights s : ℕ → ℝ are the atom masses at the grid points j/N, j = 1..N (for a configuration: s j = S(j)/N).
  Csum s m        := Σ_{j=1}^{m} s j                                   (C_m)
  Cstep s N x     := Σ_{1 ≤ j ≤ N, j/N ≤ x} s j                         (right-continuous step function; = C_m on [m/N,(m+1)/N))
  Dfun s N x      := Cstep s N x − x²/2                                 (discrepancy against the GUE datum k dk)
  Efun s N x      := ∫₀ˣ Dfun                                           (integrated discrepancy)
-/
```

### `Csum`

 partial sums C_m := Σ_{j=1}^{m} s j. 

### `Cstep`

 the right-continuous step function C(x) = Σ_{1 ≤ j ≤ N, j/N ≤ x} s_j. 

### `Dfun`

 D := C − x²/2. 

### `Efun`

 E := ∫₀ˣ D. 

### `Cstep_eq_Csum_of_mem`

 on the cell [m/N, (m+1)/N) the step function equals C_m (m + 1 ≤ N). 

### `Cstep_eq_Csum_of_one_le`

 past the last atom the step function is C_N: for x ≥ 1. 

### `Cstep_eq_zero_of_lt`

 before the first atom: C = 0 for x < 1/N (in particular for x < 0). 
