---
{
  "module": "Nc/Cross/Inv.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Cross/Inv.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Cross/Inv.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Inversion `x ↦ 1/x` exchanges `b` and `d`: the multipliers

Definitions for the step "Reflection" of the proof of Proposition prop:identity (Paper/Identity.lean).


### `exch`

 The exchange of the sites `b` and `d`. 

### `scal`

 The multipliers of the rows (columns) of the matrix at `1/x`: `x^(2i+1)` at `a, c`, `(y−1)y^i` at `d` and `y^(i+1)` at `b`,
with `y = x²`. 

### `scal'`

 The multipliers on the other side: `1 − y` at the new site `d`. 

### `enW`

 The energy of a word. 
