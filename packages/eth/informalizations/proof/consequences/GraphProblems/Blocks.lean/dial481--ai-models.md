---
{
  "module": "proof/consequences/GraphProblems/Blocks.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/GraphProblems/Blocks.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/GraphProblems/Blocks.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Corollary 7: satisfaction of formulas by assignments to all natural numbers

`Sat f φ` says that the assignment f : ℕ → Bool makes a literal of every clause of φ true, and
`sat_append` splits it over the two parts of φ ++ χ. An assignment a to x₀ … xₙ₋₁
is extended by false to all natural numbers (`ext`), and `ext_val` says that this extension agrees
with a on x₀ … xₙ₋₁. 

### `Sat`

 f makes a literal of every clause of φ true. 

 ### Assignments as functions on all natural numbers 
