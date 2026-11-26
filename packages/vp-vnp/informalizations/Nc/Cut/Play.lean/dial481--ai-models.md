---
{
  "module": "Nc/Cut/Play.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Cut/Play.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Cut/Play.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# One move of the play

Parties hold copies of units. A unit has two holders. The value of a position is the sum over all contents of
the copies (units that have not been seen are empty) of a joint weight, restricted to contents in which the two
copies of every current unit agree. A move takes some current units of two crossing bundles away and replaces the
condition that their copies agree by tables at the four parties and new units, summed over the outcomes.


### `Holds`

 The unit `id` is held by the party `a`. 

### `Contents`

 The contents in which only seen units, at their holders, are not empty. 

### `Agree`

 The copies of all units in `Cur` agree. 

### `posVal`

 The value of a position. 

### `ext`

 Write common contents of the new units into the copies of their holders. 

### `Common`

 Common contents of units: empty outside `New`. 

### `sum_contents_union`

 Contents for `Seen ∪ New` whose copies of the new units agree = old contents and common contents. 
