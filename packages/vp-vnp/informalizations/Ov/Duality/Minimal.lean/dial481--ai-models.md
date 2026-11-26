---
{
  "module": "Ov/Duality/Minimal.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Ov/Duality/Minimal.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Ov/Duality/Minimal.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Tensors up to equivalence

Tensors that are restrictions of one another are identified; their classes form a commutative monoid with a covering
relation (`Ov.Duality.Abstract`). The proofs of Proposition prop:gauge and Theorem thm:duality (`Paper/Gauges.lean`) and of
Proposition prop:extend (`Paper/Extension.lean`) work there.


### `tenSetoid`

 Tensors up to equivalence. 

### `Cls`

 The classes of tensors over I under equivalence. 

### `cls`

 The class of a tensor. 

### `rep`

 A tensor of a given class. 

### `noncomputable instance : CommMonoid (Cls K I)`

 The classes form a commutative monoid under the product. 

### `tenCover`

 The covering relation on classes: sums of restrictions. 

### `_root_.Ov.PreSpec.congr`

 Equivalent tensors have the same value. 

### `onCls`

 A gauge as a function on classes. 

### `ofCls`

 The gauge given by a function on classes. 
