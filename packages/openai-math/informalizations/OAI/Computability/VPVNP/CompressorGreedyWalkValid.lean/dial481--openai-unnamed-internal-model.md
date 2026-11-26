---
{
  "module": "OAI/Computability/VPVNP/CompressorGreedyWalkValid.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorGreedyWalkValid.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorGreedyWalkValid.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Dispatcher guards for the greedy record readers

Every call writes its vertex's label, reads the next cursor from the immutable
record header and leaves the active dispatcher frame intact. Consequently
the guard continues through all records and stops at the first address past
the directory.


### `read_induction`

 Induction along the actual reader reports. At each boundary the immutable
directory still supplies the next cursor and the memory outside the labels is
unchanged from the prepared input. 

### `read_valid`

 Guard validity for any native reader trace on a prepared operand directory.
Only the mutable labels must be disjoint from the active scheduler fields. 

### `read_valid`

 The reports of the actual assignment reader can be lifted into the linked
dispatcher under the same guard as the source reader. 
