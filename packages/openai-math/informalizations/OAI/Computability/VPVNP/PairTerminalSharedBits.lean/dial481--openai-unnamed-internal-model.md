---
{
  "module": "OAI/Computability/VPVNP/PairTerminalSharedBits.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTerminalSharedBits.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTerminalSharedBits.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The shared-bit worker on the selected terminal layout

The high header is beyond the stored row, wire and role intervals on every
selected branch. The tag and row writers preserve that header. After the
shared choices, its contents and the stored descriptor rows remain available
to each vertex, while both endpoints of each wire read the same chosen bit.


### `arena_above`

 The two arrays used to assemble the descriptor arena preserve every
external header or control word above the last role. 

### `eventually_sharedBits`

 Actual live header words and the selected final width suffice for the
physical shared-bit scan. Its numerical range is derived at the uniform
threshold, including the controller's two saved cells. 
