---
{
  "module": "Zeta23/XiPrime/PrimeSide/Abel.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/PrimeSide/Abel.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/PrimeSide/Abel.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Part of the Zeta23 formalization.

Zeta23/XiPrime/PrimeSide/Abel.lean — ξ′ generalised-coefficient prime side: the
partial-summation step with a general diagonal density.

Proof of Thm 8.1: "Proposition PP's diagonal becomes
Σ_{N≤X} |b_N|²/N · g(log N) = ∫_0^L g(y) d(Σ_{N≤e^y} |b_N|²/N) = l ∫_0^L g(y) D₁(y/l) dy + o(·)
by Lemma 7.1(i) (Abel summation; g is Lipschitz with constant ≪ 1 and supported in [−L,L])."
Abstract in everything: weights c ≥ 0 or not, any continuous density D, any C¹ window moment g
with |g′| ≤ 2 vanishing on [L, ∞).  Mirror of Zeta23/ThmD/PP.lean's abel_sum_close (density
(log t)²/2 there ↦ l²·∫_0^{log t/l} D here), same Mathlib Abel-summation + IBP route.
-/
```

### `abel_sum_density`

 **Abel summation against a density.**  If the partial sums satisfy
`|Σ_{k≤t} c_k − l²·∫_0^{log t/l} D| ≤ η` for `1 ≤ t ≤ e^L`, and `g ∈ C¹`, `|g′| ≤ 2`, `g ≡ 0` on `[L,∞)`,
then `|Σ_{n≤e^L} c_n g(log n) − l·∫_0^L D(y/l) g(y) dy| ≤ 2ηL`. 
