---
{
  "module": "OAI/Computability/VPVNP/CompressorTimelineDepth.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorTimelineDepth.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorTimelineDepth.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # The stored level number of each chronological block visit

A pass advances the stored history by one level, while its calendar ordinal
advances by its number of physical rows. The current history length agrees
with the block number and shrinking or refresh index at every pass.


### `Located.depth`

 History level of a pass, counting all previous blocks and the preceding passes in the
current block. 

### `Numbered`

 Every pass in the list has its position plus `first` as its stored history depth. 
