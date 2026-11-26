---
{
  "module": "proof/machines/ToTuring/Lib/Bool.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/ToTuring/Lib/Bool.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/ToTuring/Lib/Bool.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 Closure lemmas for `PolyT`: if the arguments are computed in polynomial time, then so are
Boolean operations on them,
`decide` of propositions built from them with logical connectives, and equality tests (class `EqT`).
The lemmas are tagged for `fun_prop`, and each
is named after the function that it certifies. 

### `EqT`

 Equality on β can be tested in polynomial time. 

### `beq'`

 `==` in polynomial time. The `BEq` instance is a separate argument, lawful but not necessarily
the one made from
`DecidableEq`: the instances of Lean's core library on pairs, options and lists are not. `EqT` is
stated with `DecidableEq`. 

### `bne'`

 `!=` in polynomial time (`BEq` as for `beq'`). 
