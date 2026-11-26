---
{
  "module": "Nc/PermValiant.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/PermValiant.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/PermValiant.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Affine substitutions and the generic permanent

Entries that are affine in one variable, the generic permanent, and circuits under affine substitutions.


### `IsAffine`

 Constant, or affine in one variable. 

### `affIn`

 The constants and, for `some i`, the span of the constants and `X i`. 

### `genPerm`

 The permanent of the generic matrix. 

### `Computes.aeval`

 Substituting affine polynomials into a circuit costs a factor 5. 
