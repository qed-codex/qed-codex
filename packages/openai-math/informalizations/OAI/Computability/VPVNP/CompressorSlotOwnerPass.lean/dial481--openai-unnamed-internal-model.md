---
{
  "module": "OAI/Computability/VPVNP/CompressorSlotOwnerPass.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlotOwnerPass.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlotOwnerPass.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Sequential generation of the endpoint owner table

The genuine-field and padding-field workers each scan a consecutive interval of
endpoint IDs. This pass lifts a single worker's native RAM execution to the
whole interval. The single-call proof may read any cell outside the completed
prefix, since all those cells still contain their initial words.


### `Visit`

 A worker for one endpoint ID. Only the output cells of earlier calls may
have changed when the worker starts. 

### `run`

 Running the worker with successive persistent cursors fills exactly the
specified interval of the table. Both the probe count and the instruction
trace length per call are exact. 
