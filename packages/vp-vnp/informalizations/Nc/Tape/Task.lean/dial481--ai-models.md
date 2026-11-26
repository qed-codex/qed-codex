---
{
  "module": "Nc/Tape/Task.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Tape/Task.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Tape/Task.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Tasks

A program is a series on the channels "side b of tape s" and "input j". Its value at an input is the sum,
over all contents of the tapes, of the weight of the program at these contents (the same word on both sides
of every tape).


### `Ch`

 Channels: the two sides of the tapes, and the inputs. 

### `Ch.tp`

 a side of a tape 

### `Ch.inp`

 an input 

### `tup`

 The words on the channels for given contents of the tapes and given inputs. 

### `contents`

 The contents of total length at most `t`. 

### `val`

 The value of a program, with contents of total length at most `t`. 

### `Bdd`

 All contents that contribute have total length at most `t`. 
