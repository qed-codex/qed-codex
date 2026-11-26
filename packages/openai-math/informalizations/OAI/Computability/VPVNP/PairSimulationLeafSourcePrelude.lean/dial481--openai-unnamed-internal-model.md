---
{
  "module": "OAI/Computability/VPVNP/PairSimulationLeafSourcePrelude.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafSourcePrelude.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafSourcePrelude.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Staging the leaf address, full header, and private cache pointer 

### `prelude`

 Five native instructions initializing the site, header and cache-read registers. 

### `Wiring`

 Register disjointness needed to read each input before it can be overwritten. 

### `prepBank`

 Register file after the five scalar-reader initialization instructions. 
