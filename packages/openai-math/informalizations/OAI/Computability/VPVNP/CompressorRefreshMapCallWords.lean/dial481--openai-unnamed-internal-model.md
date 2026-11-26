---
{
  "module": "OAI/Computability/VPVNP/CompressorRefreshMapCallWords.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRefreshMapCallWords.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRefreshMapCallWords.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The raw private descriptor of a refresh map call

The descriptor carries the actual field starts, all demand and selected payload widths,
the stored repetition word, and four private workspace heads. Its width words are
unmasked: the local port and the fixed motif determine which incident slices the map
driver subsequently uses. The integer words are recovered from the physical term and
demand tables of the selected refresh.


### `WorkHeads`

 Expressions for the four workspace addresses passed to the refresh map interpreter. 

### `WorkHeads.directory`

 Expression for the address of the map interpreter's workspace directory. 

### `WorkHeads.source`

 Expression for the base address of the map's source buffer. 

### `WorkHeads.target`

 Expression for the base address of the map's target buffer. 

### `WorkHeads.hist`

 Expression for the base address of the map's history buffer. 

### `copies`

 Reads the repetition count from word one of the selected block's strided term record. 

### `fields`

 Builds the map-call setup operands from the node field bases, stored demand and payload
widths, repetition count and workspace heads. 

### `Workspace`

 The map interpreter's ordinary numerical workspace, specialized to the chosen
refresh entry and to its actual incident wire arguments. 

### `values_eq`

 Each descriptor word computed from the level arrays is exactly the word the native
map setup expects at that ordinal. 
