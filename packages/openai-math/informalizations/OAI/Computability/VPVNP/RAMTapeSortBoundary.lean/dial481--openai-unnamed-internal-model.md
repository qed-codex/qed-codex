---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSortBoundary.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSortBoundary.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSortBoundary.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # The physical block moves between sorting layers

Before a cross-site layer, split the outgoing block off the incident stream.
The received block and all later fields stay in order on the incident stack.
After the row loop, release the previous local block and expose the accumulated
next block in increasing row order.


### `Port`

 Stacks holding the current and next blocks, sent and received incident data, word width,
slot count and two temporary buffers. 

### `splitCross`

 Separate the leading block of the incident stream in forward bit order. 

### `splitCost`

 Tick cost for separating a complete outgoing block of five-word records from the incident
stream and restoring it in forward bit order. 

### `advance`

 Install the completed row outputs as the input of the following layer. 
