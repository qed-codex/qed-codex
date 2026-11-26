---
{
  "module": "OAI/Computability/VPVNP/LiveEvaluatorTailCostFacts.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorTailCostFacts.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorTailCostFacts.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Resource bounds for native tail-group calls

The incoming and outgoing configuration gathers read one bit cell per bit and
write one cell per word. The two routing decisions and control-word writes
have constant cost. The final transition uses its native preparation and
cell-scan reports. These estimates apply before stage linking.


### `gather_cost`

 Each native gather report charges exactly one read per bit and one write. 

### `route_cost`

 An accepting exit reads the tested flag. A transfer also writes the next stage tag. 

### `putState_cost`

 The accepted-state sentinel and the initial control tag both cost two units. 

### `frames_cost`

 A successful call publishes all four advice frames in nineteen writes
following its one length read. 

### `transition_at_callFuel`

 Any successful segment can replay the same reports with the evaluator's
fixed clock because every route through its body is acyclic. 

### `transition_cost`

 A completed transition scans both tapes over their entire radius. 
