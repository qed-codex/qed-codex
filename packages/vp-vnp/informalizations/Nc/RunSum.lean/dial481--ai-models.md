---
{
  "module": "Nc/RunSum.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/RunSum.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/RunSum.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The value of an automaton is a sum over finite domains


### `RD`

 The hidden variables: letters, states, places, contents. 

### `RE`

 Their domains. 

### `RV`

 The bits: the code and the hidden bits. 

### `vEm`

 The bit "the letter at step `τ` is `a`". 

### `vSt`

 The bit "the state before step `τ` is `q`". 

### `vPl`

 The bit "the place of `z` before step `τ` is `m`". 

### `vCt`

 The bit "tape `s` holds `x` at place `p`". 

### `RS`

 The rules that carry weights. 

### `RH`

 The rules that forbid. 

### `sLits`

 The literals of a rule with a weight. 

### `hLits`

 The literals of a rule that forbids. 

### `active`

 The rules that are in force. 

### `gEm`

 The letters. 

### `gSt`

 The states. 

### `gPl`

 The places. 

### `gCt`

 The contents. 

### `Hard`

 No rule in force is violated. 

### `rLits`

 The literals of all rules. 

### `rWt`

 The weights of all rules. 
