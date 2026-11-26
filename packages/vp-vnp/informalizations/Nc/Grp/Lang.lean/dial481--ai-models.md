---
{
  "module": "Nc/Grp/Lang.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Grp/Lang.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Grp/Lang.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Weighted lists of typed values

Programs of the tree machine whose values are encodings of typed values. `bindL`, `sumL`: weighted lists.
`Does.appT`, `Does.lettT`, `foldT`: composition and folds with typed values.


### `bindL`

 First `l`, then `f`. 

### `sumL`

 The weighted sum of a function. 

### `_root_.NS1.Does.wsum_unique`

 The weighted sums are determined by the program. 

### `_root_.NS1.Does.replace`

 Replace the list. 

### `_root_.NS1.Does.appT`

 Apply a fixed program to typed values. 

### `_root_.NS1.Does.lettT`

 `let` with typed values. 

### `_root_.NS1.Does.lettE`

 `let` with typed values and typed results. 

### `_root_.NS1.Does.ite_nil`

 The first of two formulas has the empty value: go on with the second one. 

### `_root_.NS1.Does.runT`

 Apply a program that is a value to typed values. 

### `_root_.NS1.Does.letkT`

 `let`, with the argument kept, typed values. 

### `foldL`

 The weighted list of a fold. 

### `foldT`

 A fold with a typed state. 

### `foldTG`

 A deterministic fold with a typed state. 
