---
{
  "module": "OAI/Computability/VPVNP/RAMTapePrivateISAKernels.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapePrivateISAKernels.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapePrivateISAKernels.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Private load and store kernels in the RAM instruction bank

The log's ten native ports are installed in the architectural bank. A normal
completion returns directly to the caller with the two operand ports staged.


### `logLoad`

 Scan the private log for a staged address. 

### `logStore`

 Add the staged address and value to the head of the private log. 
