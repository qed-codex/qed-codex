---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSortGatherPreserve.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSortGatherPreserve.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSortGatherPreserve.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Indexed sort lookup preserving the row counter

Copy the live row tally into the gather routine's private offset register
before fetching the record. The gather's width scratch is free during this
copy, and the original row tally is available to the next row instruction.


### `fetchPreserving`

 Copy the live unary row index into private scratch before fetching the record, preserving
the caller's index for the next operation. 
