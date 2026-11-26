---
{
  "module": "OAI/Computability/VPVNP/CursorLanes.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CursorLanes.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CursorLanes.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Designating lane coordinates on the cursor graph

Number the bits of the site address in increasing order of significance. Any
partition of these coordinates supplies a base part and a binary vector of
lanes in the sense of Section 7. At a fixed cursor and slot, the displacement
in both parts is independent of the address. This also applies to the
zero-width parallel copies of the no-flip arc.


### `addressWord`

 Little-endian binary coordinates in the additive vector group. 

### `stepShift`

 The displacement of a stay or flip slot in binary address coordinates. 

### `addressPartition`

 Reorder address coordinates into the chosen base and lane blocks. 

### `lanePositions`

 Change coordinates on positions, retaining the cursor in the base. 

### `laneGraph`

 A Section 7 lifted slot graph using any designated set of address bits as
lanes. Its arc displacements depend only on cursor and slot. 

### `laneGraph_target`

 The actual slot matching of the lifted network is the original cursor
advance and address step, transported by the position bijection. 

### `paddedLaneGraph_target`

 The Section 7 matching is exactly the regularized cursor matching under
the position bijection, including all zero-width parallel slots. 

### `paddedLaneGraph_edge`

 Each padded tensor-network edge is realized by the lifted slot matching
between its own two positions. 
