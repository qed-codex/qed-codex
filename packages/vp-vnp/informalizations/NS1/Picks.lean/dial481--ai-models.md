---
{
  "module": "NS1/Picks.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/NS1/Picks.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/NS1/Picks.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Sums over executions as sums over choices

A family of steps; step `i` chooses `a` from a list and writes the names that belong to `i`.


### `funs`

 All functions on a list of indices, with values from lists. 

### `sum_funs`

 Sums over all functions. 

### `execAll_choices`

 **Choices.** Step `i` gives, for every `a` in `opts i`, the state `ov i a st`. 

### `execAll_det`

 Deterministic steps. 

### `execAll_checks_pos`

 Checks that are passed. 

### `execAll_checks_neg`

 Checks that are not passed. 
