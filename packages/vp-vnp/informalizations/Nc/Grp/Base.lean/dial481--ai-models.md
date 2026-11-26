---
{
  "module": "Nc/Grp/Base.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Grp/Base.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Grp/Base.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The program of a base party

The automaton is simulated (or the part of the input is taken); the letters of every tape are cut into segments for the
partners; the strings of the partners are cut into units.


### `Item`

 Items: flags and letters of a tape. 

### `encI`

 As a tree. 

### `encA`

 Strings as a tree. 

### `segOne`

 One tape. 

### `segStepF`

 Step: argument ((flags, letters), strings). 

### `segsL`

 Several tapes (the last one first). 

### `segsF`

 Several tapes: argument (items, strings). 
