---
{
  "module": "OAI/Computability/VPVNP/PairTraversalNativeLayer.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalNativeLayer.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalNativeLayer.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Translating the complete preimage directory of a selected term

Every old position occurs in one placement fiber. After the placement scan
has collected those fibers in old-site order, the descriptor builder reads
and translates each identifier once and publishes one header per new site.


### `raw_rows_of_preimages`

 All source rows expected by the native layer builder occur in the completed
placement directory. The order of each row is the selected local reader's order. 

### `preimage_input_before`

 The whole source row, including any unused slots, is below the next layer's base.
The corresponding count is strictly below that base even if the row capacity is zero. 

### `stepLayer_sum_ids_length`

 The placement fibers partition the old positions. 

### `native_step_layer`

 Build one selected term's descriptor layer from its completed preimage pass.
Every old site costs one read and one write, and every new site costs three
header probes. The capacity bounds apply separately to the source directory
and to the reserved destination rows. 
