---
{
  "module": "OAI/Computability/VPVNP/RAMTapeInputParametersTriangle.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeInputParametersTriangle.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeInputParametersTriangle.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Computing the triangular sorting-layer count on unary stacks

The outer counter starts at the source value. After each pop, its remaining
value is copied to the destination and one additional mark is pushed. This
adds the successive integers from the source value down to one.


### `triangleAdd`

 Add the number of unordered pairs from `d+1` elements to the destination,
where `d` is the number of unary marks on the source stack. 

### `triangleAdd_runs`

 Exact deterministic tick count. The output updates only the destination. 

### `triangleAdd_cost_le`

 A quadratic bound for the fixed routine, valid also on a zero source. 
