---
{
  "module": "OAI/Computability/VPVNP/SlotPacking.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SlotPacking.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SlotPacking.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Positions, bundles and placements for the shrinking step

Appendix C of *VP and VNP differ over every field* splits a lane into color
bits, an outgoing-slot label, a tag and an unconsumed lane. A wire whose
endpoints are both thick goes into the bundle indexed by its base arc, source
tag and remaining lane. Every other wire supplies exactly one CD demand. Its
C endpoint is thin, with ties settled by the original direction of the arc.


### `BitWord`

 A word of the given length with entries in the additive group of integers modulo two. 

### `Site`

 A packed site specified by a base vertex, a tag, and the unconsumed lane coordinate. 

### `Position`

 An old position specified by its packed site, color-bit word, and lane coordinate used to
label a slot. 

### `Arc`

 An old arc address consisting of a site, an incident slot number, and the color and
slot-label coordinates of its lane. 

### `PackingData`

 Input to Appendix C after selecting the proper coloring and tag offsets.
The bijection `slotLabel` lets the lane use a binary vector group even when
the graph's outgoing slots are labeled by `Fin d`. 

### `PackingData.slots`

 The directed regular base graph matching outgoing and incoming slots for the shrinking
  step. 

### `PackingData.color`

 The proper coloring of the base vertices used to select the bit that determines whether a
  position is thick. 

### `PackingData.slotLabel`

 Bijection from the slot-label coordinate of a lane to the index of one of the outgoing
  slots. 

### `PackingData.offset`

 Tag increment at each base vertex used when assigning a thin position to its outgoing
  bundle. 

### `PackingData.bitShift`

 Change in the color-bit word along each base arc, added to the source word when lifting
  the arc. 

### `PackingData.slotShift`

 Additive displacement of the slot-label coordinate along each base arc. 

### `PackingData.siteShift`

 Displacement of the tag and unconsumed lane coordinates along a base arc of the lifted
  site graph. 

### `sourcePosition`

 Forget the slot of an outgoing (or, dually, incoming) endpoint. 

### `siteGraph`

 Once the color bits and slot label are suppressed, bundles themselves
form a regular lift with only tag and remaining-lane coordinates. 

### `actual`

 Each old arc's permutation of the complete coordinate tuple. 

### `thick`

 Test the bit belonging to the position's base color. 

### `offsetSite`

 The bundle assignment offsets the tag while preserving the unconsumed lane. 

### `assignedBundle`

 Each thin position is assigned to its own outgoing slot at the offset tag. 

### `Motif`

 The demand motifs are indexed by all actual wires outside thick–thick bundles. 

### `C`

 On a thin–thin wire `C` is the outgoing endpoint. 

### `D`

 The old endpoint opposite `C`. 

### `not_thick_C`

 In both possible directions the designated C endpoint is thin. 

### `bundle`

 The single bundle which receives this CD demand. 

### `roleA`

 The source site of the bundle assigned to a demand motif, serving as its A site. 

### `roleB`

 The target site of the bundle assigned to a demand motif, serving as its B site. 

### `placement`

 `false` puts every thin position at the source of its assigned bundle,
`true` puts it at the destination. Every thick position stays at its packed site. 

### `roleD`

 A `D` map moves with the whole old factor at that position. 
