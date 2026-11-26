---
{
  "module": "OAI/Computability/VPVNP/PrimedCounterKernel.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedCounterKernel.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedCounterKernel.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Choice suffixes and structured executions of the preorder counter

The kernel for a node consumes a canonical word for a leaf and three words for
a binary node. Its remaining choice suffix can be passed to any further block.
These equivalences describe every successful derivation and every rejecting tape.


### `KernelExec`

 The kernel realizes exactly the finite executions whose choice prefix is available. 

### `node_kernel_iff`

 The exact node kernel, including the unused suffix and the complete post-state. 

### `completeNode_iff_exec`

 A completed node accepts precisely its finite executions that consume the entire tape. 
