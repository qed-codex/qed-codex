---
{
  "module": "OAI/Computability/VPVNP/PairShrinkRoleHandoff.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkRoleHandoff.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkRoleHandoff.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Hosted operand handoffs from the traversal-level locator

The child header reader needs the popped node and the old level's directory
fields. Shrink and refresh share this two-copy entry sequence. The hidden
shrink-field reader additionally needs the selected owner and the private
buffer in which it stores absorbed fields.


### `childHandoff`

 Copy the located node and its old-level field pointer to the child reader. 

### `childHandoff_run`

 Only the two named child registers change. 

### `hiddenBaseWord`

 The cache holds 38 words. Each of the scalar stacks following it
occupies a private interval of capacity `n^40`. 

### `hiddenCount`

 One geometry-pointer load, the existing fixed literal block for the
number of scalar stacks, and twenty private reads, copies and arithmetic rows. 

### `hiddenHandoff`

 Read the geometry pointer first, even if the caller's pointer register
overlaps a destination. Synthesize the scalar-port count using the shared
zero-and-one literal routine before computing the first transient address. 

### `hiddenHandoff_run`

 The owner and old level come from the locator. The hidden-field array
starts immediately above the geometry's operand cache and all leaf scalar
stacks, and its individual slots have stride `n*n`. 

### `cachedHiddenHandoff_run`

 Save the hidden-field base in locator register eight for the map that
follows the absorbed-field scan. The extra copy takes exactly one tick. 
