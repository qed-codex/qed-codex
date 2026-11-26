---
{
  "module": "OAI/Computability/VPVNP/PairVertexLocatedBodyLinks.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairVertexLocatedBodyLinks.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairVertexLocatedBodyLinks.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The actual PC and register placements of a selected nonleaf stage


### `stagePC`

 Map the instructions of one scheduled body into the normalized family dispatch layout. 

### `stageBank`

 Embed a selected body's original register bank using its locator-first ordering and its own
tail register block. 

### `commonLocator`

 Place the single locator bank shared by all normalized stage bodies in the enclosing
machine. 

### `shared_locator`

 Each stage, in its own original register order, reads the same locator registers
written by the header scan. No register copies or extra labels are required. 

### `stage_rows`

 The source stage sees its original numerical code and the relocated source registers. 
