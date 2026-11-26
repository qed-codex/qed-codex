---
{
  "module": "Nc/CaseI/Hub.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/CaseI/Hub.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/CaseI/Hub.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Two hubs for a balanced set

The end of the pair {a, b}, a < b, at a stands at e_a / 2 and the end at b at -e_a / 2. For a balanced set A there is a
point x of norm 2 / (9 √k) such that the sum of the distances from the ends in A to x and from the other ends to -x is at
most k (k - 1) / 2 - 4 k / 81.


### `endPos`

 The position of an end. 

### `Sep`

 The pair is separated by A. 

### `hubDir`

 The direction of the hubs: at a, the number of pairs {a, b}, a < b, that A separates, with the sign of a. 

### `sideSign`

 The sign of a node. 

### `sum_sep`

 The number of pairs that a set separates. 
