---
{
  "module": "proof/machines/ToTuring/Poly/Range.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/ToTuring/Poly/Range.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/ToTuring/Poly/Range.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 `IsPolyT` is closed under the loops of `StepMachines/Prog/Range.lean`, for a polynomial-time
bound `N`. 

### `foldRange`

 The general loop: `M` is run on `(a, i)` for `i < N a` and its results are folded by `g`,
starting from `c₀ a`.
It is polynomial-time in every step if `M` is and `N`, `g` and `c₀` are polynomial-time. 

### `firstRange`

 The loop that looks for the first `i` whose result satisfies `p`. 

### `sumRange`

 The loop that adds up the integer results. 

### `prodRange`

 The loop that multiplies the integer results. 
