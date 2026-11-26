---
{
  "module": "Paper/Heavy.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/Heavy.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/Heavy.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The paper, proof of Proposition prop:pieces: heavy nodes and pieces

A rooted tree by stages with two weights at every node: "Call a node of the tree heavy if it is the root or if
#(given nodes below)/(4M) + #(units below)/(2Ŷ) > 1/k ... A piece is a heavy node, or the subtree of a light node with
a heavy parent." A node is below itself, and the units below a node are counted at their lower ends.


### `Staged`

 A tree by stages on the nodes 0, ..., P − 1. 

### `Staged.par`

 the parent 

### `Staged.stage`

 the stage 

### `Staged.depth`

 the stage of the root 

### `Staged.root`

 the root 

### `nxt`

 One step up, resting at the root. 

### `Below`

 The node q is below p. 

### `below`

 The sum over the nodes below. 

### `kids`

 The sum over the children. 

### `Heavy`

 Heavy nodes. 

### `Head`

 Heads of pieces: heavy nodes, and light nodes with a heavy parent. 

### `top`

 The head above a node, at most d steps up. 

### `hd`

 The head of the piece of a node. 

### `rank`

 The number of a head. 

### `piece`

 The piece of a node. 

### `below_stage`

 "The sets below different nodes of one stage are disjoint." 

### `_root_.Paper.prop_pieces_heavy_few`

 "As the sets below different nodes of one stage are disjoint, each stage has fewer than k heavy nodes." 

### `_root_.Paper.prop_pieces_heavy_up`

 "Parents of heavy nodes are heavy." 

### `_root_.Paper.prop_pieces_shape`

 "A piece is a heavy node, or the subtree of a light node with a heavy parent": the head x of the piece g is a heavy
node and is the whole piece, or it is light with a heavy parent and the piece is exactly the set below it. 

### `piece_sum_le`

 A sum over a piece: one node, or the nodes below a light node. 

### `piece_boundary`

 Between two pieces there are only units at the head of either: one node for every piece. 

### `_root_.Paper.prop_pieces_count`

 "So there are at most kΛ pieces." 
