---
{
  "module": "OAI/Computability/VPVNP/PairTraversalControllerStep.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalControllerStep.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalControllerStep.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native active, reset and terminal bursts of the descriptor controller

The live operand and dispatch trace contains only reads and ticks. An active
call then replays the exact reference worker trace and returns the encoded
successor site. The two boundary cases leave the external memory untouched.


### `Pass.Located`

 A reference worker occupies the physical layer selected by the controller. 

### `Pass.route`

 The controller route that runs the worker appropriate to a tag, leaf-row, or
placement-fiber pass. 

### `Pass.labels`

 Translate the chosen pass's local worker labels into the corresponding native controller
addresses. 

### `setupLen`

 Number of register-setup instructions needed to evaluate the controller's traversal
formulas. 

### `Admin`

 Bounds and read-only behavior of the administrative event prefix before a worker, including
its exact probe count and empty choice tape. 

### `active_step_trace`

 A complete active burst adds the fixed read-only operand prefix to the
actual native tag or row report and advances by exactly one site. 

### `reset_step_trace`

 Closing a level costs one read-only burst. The next level starts at zero
and the final level advances to the terminal sentinel. 

### `stop_step_trace`

 Accept once after both complete passes, with all worker memory intact. 
