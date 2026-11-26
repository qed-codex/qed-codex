---
{
  "module": "Nc/CaseI/Geo.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/CaseI/Geo.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/CaseI/Geo.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The points of the lower bound for the complete network

In ℝ^k the ends (a, b), a ≠ b, stand at p a b = (e_a − e_b)/(2√2), so that p a b and p b a have distance one.
For a balanced set A ⊂ [k] there is a point x with ‖x‖ = 1/(6√k) such that the distances from p a b to x (a ∈ A)
and to −x (a ∉ A) add up to at most k(k−1)/2 − k/12.


### `uvec`

 e_a − e_b, divided by √2. 

### `pvec`

 The place of the end (a, b). 

### `dist_half_le`

 The distance from half a unit vector. 

### `vvec`

 The direction for the set A. 

### `qnum`

 |A|·(k − |A|)·k. 

### `sg`

 The sign of a. 
