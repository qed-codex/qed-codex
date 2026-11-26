---
{
  "module": "OAI/Computability/VPVNP/PairSimulationLeafCoordinates.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafCoordinates.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafCoordinates.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Decoding a cursor processor from its initial traversal row 

### `index_bit`

 The compressor encodes its first binary coordinate at the most
significant bit of the integer. 

### `site_number`

 Undo the order change between the cursor's little-endian address and
the compressor's two big-endian coordinate blocks. 
