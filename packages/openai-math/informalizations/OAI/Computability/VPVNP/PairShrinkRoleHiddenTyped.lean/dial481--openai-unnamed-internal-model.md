---
{
  "module": "OAI/Computability/VPVNP/PairShrinkRoleHiddenTyped.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkRoleHiddenTyped.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkRoleHiddenTyped.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The hidden-stage reader on the actual owned half-wires

The native hidden directory keeps the same IDs and field lengths for every
assignment at a fixed vertex. Reading an arbitrary full tape prefix recovers
a unique assignment on its owned fields. Reading a specified assignment's
encoding returns those exact rows and preserves an arbitrary suffix.


### `hiddenReader_typed`

 All accepted raw rows at a selected vertex determine one and only one
typed hidden assignment on the consumed prefix. 

### `hiddenReader_encoded`

 Starting on a genuine hidden assignment and any continuation returns the
precise dense-ID rows of that assignment, together with their native stores. 
