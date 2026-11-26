---
{
  "module": "OAI/Computability/VPVNP/DegreeRefreshTopology.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/DegreeRefreshTopology.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/DegreeRefreshTopology.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The regular topology after a degree refresh

Section 7.3 of *VP and VNP differ over every field* promotes the port
coordinate to a base label. Each port has a single external arc, one
internal arc per expander slot, and cyclic padding arcs. The external arc
retains the old shift of the remaining lane. Internal and padding arcs
stay within a block.


### `refreshPositions`

 Relabeling the port component of the old lane leaves a bijection of positions. 

### `bundleCoordinates`

 Group old outgoing slots by their source block and slot, keeping the old
port as the last index within each bundle. The same indexing applies to
incoming slots. 

### `bundleTarget`

 A source block and slot determine the destination block and incoming slot. 

### `bundlePort`

 The port component of the displacement bijects each source bundle's
ordered segments with the old ports at the destination. 

### `actualTarget_bundleCoordinates`

 Express the original matching in bundle coordinates. The destination
block and slot are independent of the source segment, which is relabeled by
the port translation of the old arc. 

### `RefreshSlot`

 A slot is external, internal, or a copy of the cyclic padding arc. 

### `refreshSlots`

 Number the three classes of slots in their stated order. 

### `refreshBase`

 The new base slot graph has degree exactly `d₀` in both directions
and each arc joins distinct base vertices. 

### `degreeRefresh`

 The sole external wire preserves the old shift on the remaining lane.
All internal wires and cyclic padding wires have zero displacement. 

### `degreeRefresh_external`

 The old outgoing slot is the source port of the bundled external wire;
the old incoming slot is its destination port. 

### `degreeRefresh_internal`

 Expander slots connect ports of the same block with the expander's
specified outgoing and incoming slot numbers. 

### `degreeRefresh_padding`

 Each padding slot is a separate copy of the edge to the cyclic successor. 
