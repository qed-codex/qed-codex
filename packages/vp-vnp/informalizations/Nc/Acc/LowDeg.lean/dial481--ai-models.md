---
{
  "module": "Nc/Acc/LowDeg.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Acc/LowDeg.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Acc/LowDeg.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Low degree is fast, over commutative rings

The parts of positive degree of the gates of a circuit, along a line, are power series that satisfy quadratic
equations; `W` sums the coefficients of products of them.


### `ser`

 The parts of positive degree along the line. 

### `exists_series`

 The quadratic equations. 

### `W`

 The sum of the coefficients of degree at most `b` of a product. 

### `Wi`

 The contribution of the product gates. 

### `sum_coeff_line`

 The parts of degree at most `N`. 

### `sum_coeff_eq_eval`

 All parts of a polynomial. 
