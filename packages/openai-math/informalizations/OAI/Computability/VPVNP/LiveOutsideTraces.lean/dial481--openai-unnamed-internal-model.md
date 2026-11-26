---
{
  "module": "OAI/Computability/VPVNP/LiveOutsideTraces.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveOutsideTraces.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveOutsideTraces.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Outside costs of the actual live group reports

The outer dispatcher reads its tag once per call and can write a successor
tag on an accepting handoff. The bounds below charge these events on the
real header and router logs, along with the private instruction events.


### `Resources`

 Total cost, maximal call cost, and maximal private instruction count.
A report logs every instruction except its final return or acceptance. 

### `headerReports`

 Reports of the actual header stage after the outer D dispatch and
handoff. This map does not add a microcall. 

### `header_resources`

 Every successful physical header path, at any admissible caller clock,
has the same cost and private-work bound as the short compiled run. 

### `actual_header`

 The prefix executed by the outer physical machine has bounded work
at every call, even when the group clock is much larger than 154. 

### `router_jump`

 A selected jump, including the flag read, explicit route write and outer
tag read. No branch bit is charged. 

### `router_halt`

 Unit mode terminates with one flag read and one outer tag read. 
