---
{
  "module": "OAI/Computability/VPVNP/CompressorGreedyReaderAccess.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorGreedyReaderAccess.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorGreedyReaderAccess.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# External memory touched by the greedy readers

As the cursor advances through the directory, only the labels can change.
The immutable row fields determine both the direct field reads and the
addresses of the indirect operand reads.


### `read_access`

 Reads in each prepared row are direct header or pointer reads, or indirect
reads at one of the row's operand addresses. Writes affect only label cells. 

### `color_read_access`

 Both direct record reads and indirect color-label reads are above the
old-column lower bound. Every write is to the fresh greedy allocation. 

### `tag_read_access`

 The offset reader dereferences only offset labels, projected displacement
words and the shared zero, and writes within the fresh allocation. 
