---
{
  "module": "proof/machines/ToTuring/Closure/Basic.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/ToTuring/Closure/Basic.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/ToTuring/Closure/Basic.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 Closure of the class `PolyT` under identity, constants, composition, pairing, projections and
the constructors of
Option, sums and lists. Every public lemma is in the form that the tactic `fun_prop` uses. 

 The operations of the machine on the words of values. 

### `pb_lin`

 a·t + b is below a polynomial if t is. 

### `const`

 Drop x; push the word of b. 

### `comp`

 Run the fragment of g, then that of f. 

### `prodMk`

 Duplicate x; f on the copy on top; exchange; g on x, now on top; exchange; make the pair. 

 Constructors. Each of them is written as a pair. 
