---
{
  "module": "OAI/Computability/VPVNP/CompressorGreedyReadProgress.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorGreedyReadProgress.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorGreedyReadProgress.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Cursor progress of the native greedy readers

The immutable header of each color or offset record supplies the address of
the next record. The last header returns the exclusive bound. These are the
cursor comparisons used to replay the native reports in the online schedule.


### `read_progress`

 The actual reader advances by one directory record per report, even if
there are no scheduler control cells in its input memory. 

### `color_read_progress`

 Cursor guards for the native color reader in the shrinking run. 

### `tag_read_progress`

 Cursor guards for the native offset reader in the shrinking run. 
