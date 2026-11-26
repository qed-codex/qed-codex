---
{
  "module": "OAI/Computability/VPVNP/LiveLinkedEvaluatorRoutes.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveLinkedEvaluatorRoutes.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveLinkedEvaluatorRoutes.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# From the two tail routers to their evaluator banks

The zero flag of each router selects the corresponding gathered configuration.
A one at the last router selects the accepting sentinel, and a one at the first
router selects the initial state writer. Each pair of stages contributes its
literal ordered reports, including all tag updates, to the transcript cap.


### `router`

 The first-tail router for incoming preparation or the last-group router for outgoing
preparation. 

### `retag`

 Write the selected stage's tag into the physical group's dispatcher cell. 

### `jumpReport`

 The physical outer report of a router jump to the specified stage through the chosen branch
slot. 

### `image_retag`

 A stage-tag update outside the source cut preserves every unpacked bit. 

### `gatherMemory`

 The memory after routing into the gather, packing the cut bits into the selected state
bank, and transferring to its successor. 

### `gatherLogs`

 The router jump followed by the linked configuration-word gather reports for the selected
incident side. 

### `gatherHandoff`

 The full zero-flag route, including the gathered word array and the
transfer to the last router or terminal transition. 

### `putMemory`

 The memory after routing into an endpoint writer, storing the control word, and setting the
next stage tag. 

### `putLogs`

 The router jump and linked control-write report for preparing an evaluator endpoint. 

### `putHandoff`

 The full one-flag route writes the endpoint state and enters the next
live row with cursor zero. This includes the first group's empty evaluator. 
