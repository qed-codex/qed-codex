---
{
  "module": "OAI/Computability/VPVNP/PairShrinkSurvivingBuffer.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkSurvivingBuffer.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkSurvivingBuffer.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Reassembling a surviving wire in private memory

Writing the numbered subdivisions at their frame offsets stores the entire
unsplit word, including when some subdivisions have width zero.


### `fill`

 The scan deposits every subdivision at its own frame offset. 

### `fill_eq`

 The private memory after the scan equals a single write of the unsplit word. 

### `fill_read`

 Reading any position of the completed destination buffer returns its bit. 
