---
{
  "module": "OAI/Computability/VPVNP/RAMProcessorScanBounds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorScanBounds.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorScanBounds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Bounds and emitted events of a private segment

A returned segment has no internal probe records. Every terminal or external
instruction consumes a fuel unit. The remaining fuel also bounds the total
growth of the private log when several segments are executed in one call.


### `externalOrTerminal`

 Callbacks that return control from the private scan to the site processor, namely external
reads or writes, state returns, acceptance and rejection. 
