---
{
  "module": "OAI/Computability/VPVNP/CompressorShrinkPhysicalWorkerInput.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkPhysicalWorkerInput.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkPhysicalWorkerInput.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The selector input at the actual shrinking branch

The AB and CD reads of the paired gather establish the exact demand
rows in its output memory. These rows and the packed term addresses
instantiate the physical worker input used by the reverse selector proof.


### `workerInput`

 Build the motif term worker's input at the end of the actual gather prefix, with the stored
demand pairs, ten-word descriptor addresses and private-fuel bound. 
