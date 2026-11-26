---
{
  "module": "OAI/Computability/VPVNP/AdviceReturnBit.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/AdviceReturnBit.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/AdviceReturnBit.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Returning the result bit of a circuit evaluation

The interpreter leaves the last gate value on top of the stack of intermediate
values. The caller needs that one bit on its result stack and the valuation
stack empty for the next evaluation.


### `takeTopAndClear`

 Save the head bit, drain the source stack and prepend that bit to the
destination. An empty source rejects. 

### `takeTopAndClear_runs`

 Each discarded bit costs one pop. The other three steps read the answer,
test the empty source and push the answer on the destination. 
