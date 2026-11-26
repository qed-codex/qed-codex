---
{
  "module": "OAI/Computability/VPVNP/CompressorSlotScanFootprint.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlotScanFootprint.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlotScanFootprint.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# External events of a dense native slot scan

Each successful call advances the cursor by one. A memory invariant can
retain initialized input columns while the scan fills its output.


### `scan`

 Lift the address bounds of one empty-tape call to the entire ordinal scan. 
