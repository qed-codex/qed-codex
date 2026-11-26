---
{
  "module": "Zeta23/XiPrime/ZeroCount/Basic.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/ZeroCount/Basic.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/ZeroCount/Basic.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/XiPrime/ZeroCount/Basic.lean — small shared lemmas for ξ′ zero counting:
window arithmetic for an abstract ZeroConfig (window_union, N_add, N_mono, N_unit_windows), 1 ≤ log(|t|+3),
continuity of a logarithmic derivative at an analytic nonvanishing point.  Collected here so that
ZeroCount/Generic.lean does not need to import the Y := ξ′/Γℝ instances.
-/
```

 ### window arithmetic for an abstract ZeroConfig 

### `N_unit_windows`

 unit windows: N(a, a+k) ≤ Σ_{i<k} N(a+i, a+i+1)  (in fact =). 
