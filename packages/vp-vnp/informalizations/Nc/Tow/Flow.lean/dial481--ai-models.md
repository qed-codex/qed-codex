---
{
  "module": "Nc/Tow/Flow.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Tow/Flow.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Tow/Flow.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The tower plan: numbers

`num mv` is the number of units given in a move, `alv ν` the number of alive units of a channel, `ld τ` the number
of alive units with target `τ`, as functions of the numbers `n` of initial units and of the outcomes `o`.


### `Valid`

 Every base party has at most `lhat` units at the beginning. 

### `bt`

 Initial units with target `τ`. 

### `GoodL`

 The outcome of a law move is good for `t` units. 

### `alvN`

 The number of alive units of a channel, if `t` units are given in its move. 

### `ld`

 The number of alive units with target `τ`. 

### `sqs`

 The squares of the loads of a type. 

### `IsMin`

 The type `i` is chosen at stage `j`. 

### `ActR`

 The relay is active. 

### `pr`

 The pair of a slot. 

### `slo`

 The number of slots on a pair. 

### `Fits`

 The end segments fit into `t` units at every slot. 

### `withD`

 The same vertex with another kind of law. 

### `tmin`

 The number of units at a vertex. 

### `Pick`

 The kind of law that is used at a vertex. 

### `numF`

 The number of units of a move, from the loads. 

### `numS`

 The numbers of units of the moves with times less than `τ`. 

### `tend`

 The end of time. 

### `num`

 The number of units of a move. 

### `alv`

 The number of alive units of a channel. 

### `load`

 The number of alive units with target `τ`. 

### `GoodMv`

 The outcome of a move is good: exact for relays; not too long and not too short for laws. 

### `tgTime`

 The time until which all channels with this target have been made. 

### `num_eq`

 **The numbers of units.** 
