---
{
  "module": "Nc/Tape/Run.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Tape/Run.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Tape/Run.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Runs of automata

A letter of a run is `none` (idle) or a letter on a channel. The value of an automaton at an input is the sum,
over all runs of length `t` that put the same word on both sides of every tape and the input on the input
channels, of their weights.


### `Letter`

 A letter of a run. 

### `emit`

 What a run emits. 

### `Matched`

 The run is matched: both sides of every tape agree, and the inputs are `u`. 

### `runVal`

 The value of an automaton with transition matrices `mu`, initial state `i` and final state `e` at the input
`u`: the sum over the matched runs of length `t`. 
