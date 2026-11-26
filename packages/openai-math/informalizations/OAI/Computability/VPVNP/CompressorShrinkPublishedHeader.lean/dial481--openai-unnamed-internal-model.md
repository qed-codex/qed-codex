---
{
  "module": "OAI/Computability/VPVNP/CompressorShrinkPublishedHeader.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkPublishedHeader.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkPublishedHeader.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Reading the shrinking term header from the tight block layout

The physical scalar and pointer publishers supply the eight kinds of
metadata used by the shrinking term launches. The first scratch table
lies beyond the header, so writes to the shrinking arena preserve every
one of these cells.


### `firstTable`

 Index zero among the six level tables, whose published pointer gives the first shrinking
scratch address. 
