---
{
  "module": "OAI/Computability/VPVNP/MarkedEndpointOperation.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MarkedEndpointOperation.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MarkedEndpointOperation.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Acting at a single endpoint of a marked tensor

Appendix A.3 places both exterior operators at the same endpoint of the first
marked leg. One wire supplies the exterior index held by the other endpoint.
The second marked leg and all background indices pass through unchanged.


### `child_same_right_restriction`

 Apply the matrix to the old marked leg at the row endpoint, using a wire to
supply the column index. Coincident endpoints are allowed. 

### `child_same_left_restriction`

 At the column endpoint, swap the two exterior legs before applying the matrix. 

### `value_child_same_le`

 Both operators can act at either endpoint. The single exterior wire costs
its dimension raised to the distance between the two fixed endpoints. 
