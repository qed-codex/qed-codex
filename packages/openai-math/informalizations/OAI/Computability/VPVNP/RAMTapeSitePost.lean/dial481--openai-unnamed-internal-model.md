---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSitePost.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSitePost.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSitePost.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Exact path count for the finite site memory pass

The post-pass starts with the raw padded records, the two successor payloads
and the unread sorting suffix. The one fixed table computes the layout and
executes every sort and predecessor check. Both accepting and rejecting
executions halt within the same budget.


### `complete`

 Prepare and run the sorting stages, then check boundary records and all accumulated flags. 

### `budget`

 Step budget covering sorting initialization, all sorting stages, flag tests, and the final
boundary scan. 

### `complete_spec`

 At every time above the explicit cutoff, every continuation sees the same
closed decision, and every computation path has halted. 
