---
{
  "module": "Zeta23/RvM/ReZeroCount.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/RvM/ReZeroCount.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/RvM/ReZeroCount.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/RvM/ReZeroCount.lean — the Jensen half (J) of Backlund's bound:
the number of zeros of Re ζ(σ + iT) on σ ∈ [1/2, 2] is ≪ log T.
Route: g(z) := (ζ(z+iT) + ζ(z−iT))/2 is analytic away from 1 ± iT and equals Re ζ(σ+iT) for real σ
(riemannZeta_conj); g(2) = Re ζ(2+iT) ≥ 2 − π²/6 > 1/3; rescale |z−2| ≤ 1.9 to the unit disc and
apply the ported PNT+ ZerosBound (r = 0.8, R = 0.9) with zeta_growth_right on both summands.
Used by Zeta23/RvM/Backlund.lean for backlund_horizontal.
-/
```

### `finite_zeros_closedBall`

 zeros of a function analytic on (a neighbourhood of each point of) an open ball are finite in
any closed sub-ball, given one nonvanishing point. 

### `symZeta`

 the symmetrised function g_T(z) := (ζ(z+iT) + ζ(z−iT))/2; equals Re ζ(σ+iT) for real σ. 

### `symZeta_ofReal`

 for real σ (and σ + iT ≠ 1), g_T(σ) is the real number Re ζ(σ + iT). 

### `reZeroSet_card_le_of_growth`

 **(J) the Jensen half of Backlund's bound**, parametric in the growth data (A, C) of ζ to the
right of σ = 0.15: for T ≥ 4, #{σ ∈ [1/2,2] : Re ζ(σ+iT) = 0} ≤ (1/log(0.9/0.8))·(|log 6C| + 2·max A 0)·log T. 

### `reZeroSet_card_le`

 **(J) the Jensen half of Backlund's bound**: #{σ ∈ [1/2,2] : Re ζ(σ+iT) = 0} ≪ log T. 

### `reZeroSet_card_le_at`

 explicit form at zeta_growth_right_at's literal data (A, C) = (1, 20/3):
ncard ≤ (1/log(0.9/0.8))·(|log 40| + 2)·log T (≈ 48.3·log T) for T ≥ 4. 
