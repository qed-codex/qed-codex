---
{
  "module": "Nc/Hc/Segments.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Hc/Segments.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Hc/Segments.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Rows of segments joined by exclusive-or gadgets

A row of segments is closed to a cycle. Every segment offers some options, and each option is a path from the head of
the segment to the head of the next one. An exclusive-or gadget has three vertices, two tips and a middle one, with
edges both ways between each tip and the middle. It joins two options: one runs through it in one direction, the
other in the opposite one. The cycles through all vertices correspond to the selections of one option in every
segment that use every gadget exactly once.


### `hcSum`

 The sum over the cycles through all points of a finite set of the products of the weights of their edges. 

### `Vtx`

 A vertex of the graph: the head of a segment, or one of the three vertices of a gadget. 

### `equivSum`

 The vertices as a disjoint union. 

### `card_eq`

 There is one vertex for every segment and three for every gadget. 

### `Row`

 A row of segments with gadgets: the successor of each segment, and for each gadget and each of its two sides the
option that runs through the gadget on this side. 

### `Row.next`

 the next segment 

### `Row.port`

 the option through a side of a gadget 

### `len`

 The number of gadgets on an option. 

### `slot`

 The place of a side of a gadget on its option: the gadgets of an option are put in some order. 

### `place`

 The entry of the gadget in place j on an option; behind the last gadget, the head of the next segment. 

### `after`

 The vertex that follows a side of a gadget on its option. 

### `Edge`

 The edges. 

### `weight`

 The weights of the edges: the first edge of an option carries the weight of the option, every other edge 1. 

### `NoParallel`

 No two options of one segment avoid all gadgets. 

### `Sel`

 The option at a side of a gadget is selected. 

### `Valid`

 A selection uses every gadget exactly once. 

### `side`

 The side of a gadget that is used by a selection. 

### `route`

 The successor of a vertex, for a selection and one side for every gadget. 

### `edge_route`

 The successor along a selection is always an edge. 

### `place_zero_injective`

 The first edges of different options of one segment differ. 

 ## From a selection to a cycle 

### `route_reaches`

 Following a selection that uses every gadget exactly once, one
comes from the head of any segment to every vertex. 

### `route_bijective`

 Following such a selection is a permutation of the vertices. 

### `routePerm`

 The cycle of a selection. 

### `routePerm_isCycleOn`

 It is one cycle through all vertices. 

 ## From a cycle to a selection 

### `not_two_cycle`

 In one cycle through all vertices, no two vertices are a cycle of their own if there is a third one. 

### `exists_traverse`

 A cycle through all vertices runs through every gadget in one of two
ways: from one tip over the middle to the other tip, and then on along the option of that side. 

### `exists_selection`

 In a cycle through all vertices every option that is entered at
the head of its segment is followed to its end, and every gadget lies on exactly one of these options. So the cycle
is the one of a selection that uses every gadget exactly once. 

 ## The sum 

### `hcSum_weight`

 The sum over the cycles through all vertices of the products of the edge
weights is the sum over the selections that use every gadget exactly once of the products of the weights of the
selected options, provided that no two options of one segment avoid all gadgets. 
