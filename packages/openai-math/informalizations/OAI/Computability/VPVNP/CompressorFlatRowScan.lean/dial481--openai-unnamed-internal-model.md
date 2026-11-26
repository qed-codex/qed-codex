---
{
  "module": "OAI/Computability/VPVNP/CompressorFlatRowScan.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorFlatRowScan.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorFlatRowScan.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Visiting every bundle in one online calendar stage

The persistent cursor of a calendar visit is the bundle ordinal. Its report
updates that bundle's bank and advances the cursor. A finite stage list may
therefore transpose the fixed per-bundle operations while retaining the
input columns and every previously completed bank.


### `walk`

 Compose the calendar visits in their actual list order, retaining the
post-memory for all stages. 
