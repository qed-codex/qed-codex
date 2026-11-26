---
{
  "module": "OAI/Computability/VPVNP/PairTraversalControllerReference.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalControllerReference.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalControllerReference.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Chronological traversal passes and their reset-entry calls

The reference jobs write one layer of role tags at a time, then the leaf
and each successive fiber layer. A site's call uses exactly the memory
left by earlier sites of its own pass and all preceding passes.


### `tagJobs`

 Role jobs advance the descriptor base after every layer. 

### `tagJobs_at`

 The indexed job uses the same descriptor base as the controller's
tag-parameter lookup. 

### `rowJob`

 The row job uses the exact public directory of its original worker. 

### `Reference`

 Consecutive passes start at ordinal zero and retain external memory. 

### `Sites`

 Each step retains its full trace and uses the incremented site ordinal. 
