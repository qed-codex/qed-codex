---
{
  "module": "OAI/Computability/VPVNP/CompressorShrinkSelectedTailPackets.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkSelectedTailPackets.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkSelectedTailPackets.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # The four chronological placement, role and child-directory packets 

### `tail`

 The four post-comparison visits write placements, write role rows, clear child counters,
then collect children by their new site. 

### `Footprint`

 Requires the size, term, old outgoing-incidence, and preliminary operand expressions used
by the four tail visits to read only addresses in `D`. 

### `Source`

 A source run of the visit with instruction fuel at most 65, whose header operand
expressions read only from `D` at entry. 

### `inputs`

 The entry memories for the four tail visits, taken after scoring, after placement, after
writing roles, and after clearing child counters. 

### `reports`

 The source reports from placement, role writes, child-counter clearing, and child
collection concatenated in execution order. 

### `walk`

 Each of the four visits uses the memory left by its predecessor,
including the selected layout bit and the newly materialized owner column. 
