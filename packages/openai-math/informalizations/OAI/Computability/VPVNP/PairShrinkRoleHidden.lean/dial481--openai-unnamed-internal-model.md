---
{
  "module": "OAI/Computability/VPVNP/PairShrinkRoleHidden.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkRoleHidden.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkRoleHidden.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The hidden-field stage of a shrinking vertex

The native directory gives an ID and width for each absorbed field at the
vertex. A full prefix supplies exactly those fields and updates their scratch
cells. A stream ending in any one of the fields rejects.


### `hiddenReader`

 The parsed rows use the dense hidden ID as the slot number in scratch. 

### `HiddenPreserved`

 Registers outside the hidden-field loop's writes retain their values. 

### `hidden_realizes`

 Run the actual instruction table on the decoded fields. The scratch
update is computed from the entry scratch, even if other cells in the full
private memory differ. 
