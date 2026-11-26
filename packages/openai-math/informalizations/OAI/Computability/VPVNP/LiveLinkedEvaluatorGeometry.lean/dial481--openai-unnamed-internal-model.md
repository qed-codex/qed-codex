---
{
  "module": "OAI/Computability/VPVNP/LiveLinkedEvaluatorGeometry.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveLinkedEvaluatorGeometry.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveLinkedEvaluatorGeometry.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Physical allocation for the linked evaluator routes

The old and new evaluator banks follow the distributed-header buffers. Each has
exactly one word per control or tape field. The scratch region follows both
banks, so the same upper bound on the shadow base controls every address.


### `radius`

 The evaluator tape-window radius computed at this group's public geometry. 

### `k`

 Number of words in a physical evaluator configuration at the group's window radius. 

### `cutSource`

 The first source bit cell used by the incoming or outgoing configuration gather. 

### `limit`

 The shadow base, used as an upper bound for the evaluator configuration banks and
transition scratch. 

### `Addresses`

 Ordered physical intervals in the real public operand bank. 

### `geometryFit`

 One global address fit and the table and burst sizes imply the native
transition and gather geometry, for the true length-dependent radius. 
