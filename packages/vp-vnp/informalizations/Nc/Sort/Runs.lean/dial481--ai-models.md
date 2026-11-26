---
{
  "module": "Nc/Sort/Runs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Sort/Runs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Sort/Runs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Programs given by their structured runs

A series on channels is described by a family of runs: every run emits words on the channels and has a weight.
The sum of the series over all words with given projections is the sum of the weights of the runs that emit
these projections.


### `IsRuns`

 The series is described by runs with emissions em and weights wt. 

### `Runs`

 There is a series of dimension at most n with these runs. 

### `IsRuns.kstar`

 The star: the runs are the lists of runs. 

### `chanWord`

 The word on the channels, channel by channel. 

### `pick`

 One of finitely many families of words, with weights. 

### `const`

 Fixed words. 

### `pi`

 A sequence of choices. 
