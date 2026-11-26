---
{
  "module": "Nc/LowDegree.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/LowDegree.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/LowDegree.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Low degree is fast (Lemma 1)

A polynomial of degree at most `d` that is computed by an arithmetic circuit with `s` gates has, at every
point, a value that is a sum over parse trees. A parse tree with `i` leaves reads `2 * i - 1` entries of
fixed tables of the circuit and `i` coordinates of the point; only `i ≤ d` occurs.


### `IsStep`

 Entry `k` of the list `l` is a variable, a constant, or the sum or product of two earlier entries. 

### `Computes`

 `p` is computed by an arithmetic circuit with `s` gates (inputs and constants count as gates). 

### `line`

 `p` along the line through 0 and `u`. 
