---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordsTermLayout.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsTermLayout.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsTermLayout.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Choosing the common layout after the native term scan

The width cells read by the score passes are the cells written by the fused term
worker on the very same admitted motif choices. A legal term stream therefore
determines one global layout, and the scratch for its score does not overwrite
any earlier term words.


### `stored_of_term_run`

 All eight exact inputs to the score scan are physically present immediately after
the actual fused term execution. 

### `choose_layout`

 From the supplied physical demand pairs, every admitted sequence gives an actual
term scan followed by the deterministic eight-axis layout computation. 
