---
{
  "module": "Ov/Duality/PreSpec.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Ov/Duality/PreSpec.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Ov/Duality/PreSpec.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Gauges

A gauge (in Lean: `PreSpec`) is what a spectral point becomes when "multiplicative"
is weakened to "submultiplicative". Such a function is easy to write down, as an infimum over
certificates; `Paper.prop_gauge` finds a spectral point below it.
(Paper: the subsection "Gauges". The zero tensor is covered by the empty family, so a gauge is 0 at it.)


### `PreSpec`

 A gauge on the parties I: a real function p ≥ 0 on tensors with p(1) = 1,
p(st) ≤ p(s)p(t), and p(s) ≤ ∑ p(b k) whenever s is a sum of restrictions of the b k. 

### `mono`

 A gauge is monotone under restriction. 
