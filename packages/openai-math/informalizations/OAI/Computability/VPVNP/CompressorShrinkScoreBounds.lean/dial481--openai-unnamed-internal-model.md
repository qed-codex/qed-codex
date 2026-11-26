---
{
  "module": "OAI/Computability/VPVNP/CompressorShrinkScoreBounds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkScoreBounds.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkScoreBounds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Memory footprints and cursor progress of the ten score stages 

### `Region`

 Physical address information used by every score visit. 

### `Stage.limit`

 Exclusive stopping cursor for a score visit. Each axis scans `n` motif rows, while clearing
and comparison each take one call. 

### `score_frame`

 The actual score run leaves the old level header and every earlier
allocation untouched. 
