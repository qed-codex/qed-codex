---
{
  "module": "OAI/Computability/VPVNP/CompressorBundleTableReadback.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorBundleTableReadback.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorBundleTableReadback.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Typed readback of the complete rectangular bundle key table

The ID rows in the post-memory of the native append pass supply the addresses
for the complete key-gathering schedule. Every live cell of the resulting
rectangle contains the key of the corresponding thick wire or motif. The
whole schedule costs four calls-plus-probes per original arc.


### `table`

 Specialize the rectangular key table to the row stride and ID base
written by the preimage pass. 

### `Stored`

 The mathematical ID rows held in the physical count and row arrays. 

### `KeyRows`

 Physical table readback directly in terms of the original typed arcs. 

### `gather_table`

 Run the key table over the actual list memory and recover every typed
entry, with the exact original-arc cost. `Completed.frame` covers every
cell outside the written prefixes, including the original widths. 

### `fixed_gather_table`

 A single public bank supplies the cursor decoder and all three bases
for the entire gather. Its report sequence has the exact same physical
readback and cost as the row-wise schedule. 
