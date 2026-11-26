---
{
  "module": "proof/rates/CountedRecursion/SolverCall.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/SolverCall.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/SolverCall.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The call for one pattern

* `child_eq`: the context of the call for the pattern y and the grouping x, written out: (ℓ, L, B')
  with the parent (K_ℓ, g_ℓ, λ, B, the lists, the direction, y, x).
* `child_size`: the context of each call is small: its size is bounded by the sizes of what the
  solver holds and of the number of patterns, and by K^g, g, gP and B'.
* `pattern_run`: the run for one pattern. With the calls answered as the specification says, at the
  price tc, `patternValue c` returns Z_ι within C·K^g + tc + 2 operations; and |Z_ι| ≤ 2^{gP +
  g²B₁}. 

### `child_eq`

 The context of the call for the pattern y and the grouping x. 

### `size_units`

 The size of a string of units. 

### `child_size`

 The context of a call has size at most twice the size of what the solver holds and of the number
of patterns, plus the size of K^g, plus 2g, plus 6gP (twice the bound 3gP on L), plus 2B', plus 12. 

### `pattern_run`

 **The run for one pattern.** 
