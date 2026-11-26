---
{
  "module": "OAI/Computability/VPVNP/LiveCutAssignments.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveCutAssignments.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveCutAssignments.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Raw cut assignments of the two live modes

The cut at the midpoint carries the accumulated exponents. Each later
interior cut carries a configuration of the evaluator. The two missing
endpoint cuts have unique empty strings. Local agreement of neighboring
mode flags forces a single flag throughout the whole chain.


### `firstCut`

 The cut following a first-half group, counting from the first interior cut through the
midpoint. 

### `laterCut`

 An interior cut strictly after the midpoint, indexed by its position among the evaluator
configuration cuts. 

### `liveCutEquiv`

 Raw physical cuts are exactly the first-half and tail fields with no
extra choices for either missing endpoint. 

### `commonMode`

 Equality at every interior group propagates the first mode flag to all
interior cuts. The case of a single interior cut needs no comparisons. 
