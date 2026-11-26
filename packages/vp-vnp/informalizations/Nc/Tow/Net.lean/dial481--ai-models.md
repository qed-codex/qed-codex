---
{
  "module": "Nc/Tow/Net.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Tow/Net.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Tow/Net.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The tower plan: nodes, moves, targets

Every channel has a target: what becomes of its units. `done`: they stay between a node and its parent; `edge j e`:
units of stage `j` on the edge `e`; `nxt x`: given in the relay `x`; `seg …`: end segments on a pair of a vertex.


### `Nd`

 Nodes of the tree: the chambers of all levels, and the root. 

### `nd`

 The node of a chamber. 

### `RM`

 Names of relays. 

### `RM.start`

 step `s` of the path of a batch 

### `RM.inn`

 an edge inside a vertex of type `i` 

### `RM.mid`

 an edge between vertices of its type 

### `RM.fin`

 the last stage 

### `rmEquiv`

 Relays as a sum. 

### `Tg`

 Targets. 

### `Tg.done`

 a node and its parent 

### `Tg.edge`

 an edge of stage `j` 

### `Tg.nxt`

 given in a relay 

### `Tg.seg`

 an end segment 

### `hst`

 The host of an end of an edge. 

### `tri`

 The three parties of a relay. 

### `okR`

 The relay exists. 

### `edgeO`

 An edge of stage 0, if there is one. 

### `tgR`

 Targets of the channels of relays. 

### `inpR`

 The target whose units are given in a relay. 

### `timeR`

 Times of relays. 

### `gam`

 The third chamber of an initial unit. 

### `tgB`

 The target of an initial unit. 

### `LMv`

 Names of law moves. 

### `Mv`

 Moves. 

### `kindM`

 The law of a move. 

### `atv`

 A chamber of a vertex. 

### `partM`

 The parties of a move. 

### `timeM`

 Times of moves. 

### `tgM`

 Targets of channels. 

### `Place`

 Where the nodes are among the parties. 

### `Place.pt`

 the party of a node 

### `eE`

 The order of the moves. 

### `sys`

 The system of moves. 

### `NM`

 Channels by their moves. 

### `ZM`

 Slots by their moves. 

### `eN`

 Channels by their moves. 

### `eZ`

 Slots by their moves. 
