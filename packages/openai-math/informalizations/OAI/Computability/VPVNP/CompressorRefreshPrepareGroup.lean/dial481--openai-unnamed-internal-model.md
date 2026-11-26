---
{
  "module": "OAI/Computability/VPVNP/CompressorRefreshPrepareGroup.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRefreshPrepareGroup.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRefreshPrepareGroup.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native refresh prefix before reading the selected term

The gather, bundle, offset and demand scans execute from the current graph
with empty choice tapes. They produce the numerical input to the motif
worker even when the caller has not selected a term.


### `stages`

 The deterministic refresh prefix, consisting of the gather, bundle and offset scans
followed by one demand scan for each tie. 

### `rest`

 Refresh stages after demand preparation, in the order of term selection, supply, expander
table rows, output slots and the base scan. 

### `window`

 The actual contiguous block interval before the selector. 

### `Prepared`

 The reported prefix run materializes the segment fields and the actual block demand widths
in its post-memory, writes within the planned arena, uses empty choice tapes and incurs its
stated exact charge. 

### `install`

 Execute the complete deterministic refresh prefix without receiving a
choice. The compiled program sees the block's dense demand coordinates at
the post - memory of these exact packets. 
