---
{
  "module": "OAI/Computability/VPVNP/SlotRegularization.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SlotRegularization.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SlotRegularization.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Regularizing labeled wire slots

In Section 7.2 and Appendix C of *VP and VNP differ over every field*,
surviving role edges carry an identifier for their motif, role pair and
subdivision number. Once their two base-endpoint fibers have a common size,
the fibers can be numbered separately. Parallel dummy edges fill any
deficit. All numbering is at the base, so it transports along the remaining
lane without depending on widths.


### `SlotIndexing`

 Both endpoint numberings of a set of identified arcs, with their lane
displacements. The incoming slot of an ID is the target of its outgoing slot. 

### `SlotIndexing.graph`

 The lifted slot graph implementing the given source, target, and lane displacement for
  every arc identifier. 

### `SlotIndexing.outgoing`

 The bijection assigning each arc identifier its source base vertex and local outgoing
  slot number. 

### `SlotIndexing.incoming`

 The bijection assigning each arc identifier its target base vertex and local incoming
  slot number. 

### `SlotIndexing.actualTarget`

 At any absolute source lane the ID gives both slot addresses and the
destination lane, with the same endpoint numberings at every translate. 

### `numberFiber`

 Number each endpoint fiber by its ID order. 

### `PaddedId`

 Padding attaches one new ID per missing outgoing slot at each base. 

### `paddedSource`

 All padded arcs leave the vertex in their ID. 

### `paddedTarget`

 The added slots advance the base through a common permutation. 

### `paddedShift`

 Dummy arcs preserve the remaining lane. 

### `paddedWidth`

 For arbitrary widths, including lane-dependent ones, assign zero to
each dummy arc. 

### `paddedSlotIndexing`

 A common deficit in the two endpoint counts can be padded to degree
`d`. Real slots keep their ID order inside each fiber and dummy slots follow
them. The next-base permutation may be the cyclic shift on the tag. 

### `paddedSlot_numbers`

 The two slot numbers of a real ID can be recovered from the two local
incidence lists alone. Each is the number of smaller IDs in its list. 

### `paddedSlot_dummy_numbers`

 Dummy slots follow the genuine incidence list in both numberings. 

### `cycleTags`

 Cyclic dummy slots change only the tag of the new base. 
