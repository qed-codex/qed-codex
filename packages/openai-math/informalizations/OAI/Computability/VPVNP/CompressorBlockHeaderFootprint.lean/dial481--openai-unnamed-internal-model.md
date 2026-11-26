---
{
  "module": "OAI/Computability/VPVNP/CompressorBlockHeaderFootprint.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorBlockHeaderFootprint.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorBlockHeaderFootprint.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Read and write addresses of the compressor's header visits

All reads of the initial scalar publisher come from the immutable cursor
bank in level zero. The relabel and successor workers read the old header.
The head publisher reads the new level's dimensions and level zero's
capacity. Their report logs can therefore be replayed on memories agreeing
from the first level header onwards.


### `Data`

 External addresses at or above the first level header, where descriptor data are read and
written. 

### `substep`

 The complete three-report header log is confined to the descriptor data
suffix, including reads used to compute array capacities from level zero. 
