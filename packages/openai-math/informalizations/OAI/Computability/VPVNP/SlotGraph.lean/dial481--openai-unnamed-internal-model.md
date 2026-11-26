---
{
  "module": "OAI/Computability/VPVNP/SlotGraph.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SlotGraph.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SlotGraph.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Indexed directed regular wire graphs

In Section 7 of *VP and VNP differ over every field* each vertex has `d`
outgoing and `d` incoming slots. A permutation sends each outgoing slot to
the unique incoming slot of its arc. The two numberings are independent.
An arc translates its source lane by its own displacement.


### `SlotGraph`

 A directed multigraph with separate incoming and outgoing slot numberings. 

### `SlotGraph.target`

 The permutation matching each outgoing base slot to the incoming base slot at the other
  end of its directed arc. 

### `LiftedSlots`

 A base slot graph equipped with its lane displacements. 

### `LiftedSlots.base`

 The directed slot graph whose arcs are lifted over the lane group. 

### `LiftedSlots.displacement`

 The lane increment assigned to each outgoing base slot, added to the source lane to
  obtain the target lane. 

### `actualTarget`

 Match each actual outgoing slot to its actual incoming slot. The inverse
recovers the source base arc and subtracts its displacement. 

### `actualTarget_translate`

 Slot endpoints move together when all lanes translate by a common offset. 

### `actualGraph`

 Forget the lane structure, retaining the full directed regular graph. 
