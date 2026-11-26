---
{
  "module": "OAI/Computability/VPVNP/CompressorBundleFixedGatherTable.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorBundleFixedGatherTable.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorBundleFixedGatherTable.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The complete key rectangle built by a single fixed native scan

The dense traversal visits the live prefixes of both row classes exactly
once and preserves all padding. The resulting key table has the same
readback and external frame as the bounded row-wise construction.


### `table_run`

 Single native table and one public parameter bank for all old IDs.
The total call count is the sum of the exact two fiber sizes over all ports. 
