---
{
  "module": "OAI/Computability/VPVNP/PairTraversalControllerPrepare.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalControllerPrepare.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalControllerPrepare.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The complete read-only traversal dispatcher prefix

From the native reset state, the controller reaches a unique destination using
only ticks and reads. Every computed operand is evaluated on the entry memory.
The worker scratch registers are zero at that point. The log may be replayed
against any memory, and its exact probe count is independent of the ordinal.


### `prefixTrace`

 Chronological log of the register setup and guard instructions. 

### `prepare_trace`

 Exact native setup and guard traversal, with all operand values, the
read-only prefix and the continuation at the selected machine label. 

### `prepare`

 Prepare the worker at its selected label with its complete read-only prefix. 
