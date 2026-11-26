---
{
  "module": "Zeta23/ThmD/WindowLocalHyps.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmD/WindowLocalHyps.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmD/WindowLocalHyps.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/ThmD/WindowLocalHyps.lean — every admissible window satisfies `LocalHypsCore`.  Assembly of Zeta23/ThmD/WindowCore.lean (Fourier/Poisson side) and
Zeta23/ThmD/PsiC.lean (ψ-majorant integrals), field by field; `b ≥ 1/2` is an input (it is a
property of the particular window — for `φ_D` it holds for large `T`, see BridgeD.lean).
-/
```

### `localHypsCore`

 **Admissible window ⇒ `LocalHypsCore`.**  For any `p : Setting` in the regime
(`0 < λ ≤ 1`, `l ≥ 1`, `X ≥ 1`) and any window `v` admissible at scale `(p.L, p.w)` with constant
`c` and `b_v ≥ 1/2`, the local data `(v̂, V, A_v, g_v, a_v, b_v)` satisfy all of §5's hypotheses. 
