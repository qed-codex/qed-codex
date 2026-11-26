---
{
  "module": "OAI/Computability/VPVNP/RAMTapeInputParametersWidthCost.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeInputParametersWidthCost.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeInputParametersWidthCost.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Cost of computing the incident width

The exact instruction count includes every copy, multiplication and scratch clear. The
largest term is proportional to the payload `(d+10)^4 * H * (d+1).choose 2`, which gives
a degree-seven bound in the combined address and bucket sizes.


### `work_eq`

 Total instruction count of the four stages, grouped by the intermediate register values. 

### `work_le`

 Bound used by the fixed live-validator clock. 
