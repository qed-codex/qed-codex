---
{
  "module": "OAI/Computability/VPVNP/CompressorGreedyPacketFootprints.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorGreedyPacketFootprints.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorGreedyPacketFootprints.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Physical memory bounds for the six greedy packets

The color and offset initializers read the old forward and inverse mate
columns and write their own directories. Together with tag projection,
zero publication and the two readers, each stage reads from the level
data and writes only into the fresh greedy allocation.


### `color_prepare_access`

 The relocated color initializer reads old mates and writes only its fresh
color labels, headers and operand pointers. 

### `tag_prepare_access`

 The offset initializer follows the same old mate columns and writes its
disjoint offset directory. 

### `packet_access`

 Per-packet memory bounds in native execution order. The lower read bound
may be any common lower bound for the six old incidence columns. 
