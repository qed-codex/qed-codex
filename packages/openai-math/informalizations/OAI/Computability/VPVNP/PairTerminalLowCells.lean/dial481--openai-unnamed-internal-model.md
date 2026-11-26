---
{
  "module": "OAI/Computability/VPVNP/PairTerminalLowCells.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTerminalLowCells.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTerminalLowCells.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Preservation of the low counter addresses before vertex evaluation

The terminal bootstrap writes its high header. The prefix scan writes its
offset array and the total and role fields in that header. The row builder
preserves lower addresses, and the shared scan writes only the final wire
bank. This leaves the live grammar and motif words available to the first
vertex burst.


### `vertex_source_below`

 The vertex worker can replay its source on the post-scan physical
memory. At addresses below the workspace the bootstrap, prefix, row,
shared-bit and replay steps all preserve the original input word. 

### `counter_before_pairTag`

 Every live counter lies below the auxiliary shadow and the compression
workspace. The low part of the word-address layout fits without wraparound. 

### `online_counter_initial`

 The source word handed to the terminal bootstrap at a live counter
equals the original prepared nomination or zero motif word. 
