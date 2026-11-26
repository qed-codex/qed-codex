---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpCRTOuterFinish.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpCRTOuterFinish.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpCRTOuterFinish.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Final cleanup and complete tape-loop costs for scalar reconstruction.
The arithmetic-middle premise below is an actual execution of a fixed command;
its concrete implementation is assembled separately from the CRT services. 

### `loopAndCleanup_run`

 Complete actual traversal and cleanup, with the physical output stack
identified. Cleanup includes the copied full node list and generated widths. 

### `controller_run`

 Join physical initialization, ordered traversal and final cleanup. The
sole remaining service premise is the arithmetic middle's actual execution
on each exact loaded state, for the binary exponent produced by initialization. 

### `traversal_index`

 With the fixed input order, the physically counted index is the current
node's original index, even though processed nodes are stored in reverse. 

### `cofactor_stream_product`

 The actual remaining ++ processed cofactor stream contains each other
node exactly once. No cancellation and no nonzero-node assumption is used. 
