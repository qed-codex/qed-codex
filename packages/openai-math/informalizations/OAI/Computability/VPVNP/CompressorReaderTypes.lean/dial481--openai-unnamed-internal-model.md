---
{
  "module": "OAI/Computability/VPVNP/CompressorReaderTypes.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorReaderTypes.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorReaderTypes.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Fixed ports of the advised compressor-coordinate reader

The index and scalar values vary with the model, while the set of advice and
workspace ports below is the same for every prime, length and operation.


### `K`

 Raw advice-port type used for Macaulay matrix entries by the compressor coordinate reader. 

### `Parts`

 Denominator, raw, and side preparation components for the selected coordinate advice. 

### `Advice`

 Advice ports for the compressor's selected coordinate preparation over the raw Macaulay
port bank. 

### `Work`

 Working ports used by the selected coordinate preparation routines. 

### `Ports`

 Combined reader port type separating advised inputs from working storage. 
