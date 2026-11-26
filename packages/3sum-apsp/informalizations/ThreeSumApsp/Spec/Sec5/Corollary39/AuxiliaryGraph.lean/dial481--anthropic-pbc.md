---
{
  "module": "ThreeSumApsp/Spec/Sec5/Corollary39/AuxiliaryGraph.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Spec/Sec5/Corollary39/AuxiliaryGraph.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Spec/Sec5/Corollary39/AuxiliaryGraph.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The weights of the graph H as sums over lists of pairs of parts (proof of Corollary 39)

The weight of an edge of the graph H (the proof of Corollary 39) is a sum of weights of the original
graph over a list of pairs of parts that depends only on k and on the part of H.  A program for a
fixed k can therefore add these weights up one after the other.  Vertices of H, and choices of the
fixed vertices, are numbers whose digits in base n, least significant first, are the vertices of the
original graph.


### `pairsH`

 The pairs of parts whose edges are counted in the weight of an edge of H between its parts i and
i + 1: the four contributions of the proof of Corollary 39, in the order of KClique.weightH. 

### `pairSum`

 The total weight, over a list of pairs of parts, of the edges between the vertices that v
chooses in these parts. 

### `weightH_eq_pairSum`

 The weight of an edge of H is the sum over the list of pairs. 

### `vtx`

 The vertex in part p of the clique that is given by four numbers: F for the fixed vertices and
a, b, c for the three groups of parts. 

### `vtx_lt`

 The vertices are below n. 

### `cliqueOf`

 The clique given by four numbers. 

### `fixedOf_cliqueOf`

 The fixed vertices of the clique are the digits of F. 

### `vtx_groupPart`

 The vertex in part number j of a group of parts is the digit number j of the number that stands
for the group. 

### `groupOf_cliqueOf_zero`

 The vertices of the clique in the first group of parts are the digits of a. 

### `groupOf_cliqueOf_one`

 The vertices of the clique in the second group of parts are the digits of b. 

### `groupOf_cliqueOf_two`

 The vertices of the clique in the third group of parts are the digits of c. 

### `graphH_entries`

 The three weight matrices of H, entry by entry, as sums over the lists of pairs. 
