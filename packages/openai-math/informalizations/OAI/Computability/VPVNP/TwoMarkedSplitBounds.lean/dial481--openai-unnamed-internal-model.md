---
{
  "module": "OAI/Computability/VPVNP/TwoMarkedSplitBounds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/TwoMarkedSplitBounds.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/TwoMarkedSplitBounds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Endpoint estimates for the children of an exterior split

The second marked index is held in the background when applying the local
operations of Appendix A.2 to a child from Appendix A.3.


### `child_splitMarkedTerm_mutual`

 Regroup the second marked index with the background so that the child
has precisely the three movable roles used in the one-mark exterior split. 

### `value_exteriorChild_same_le`

 The ordinary endpoint bound uses the exterior level itself as the
identity wire for either child. 

### `value_exteriorChild_plus_le`

 At the column endpoint the positive branch is supplied from the row
endpoint through the level one degree higher. 

### `value_exteriorChild_minus_le`

 At the row endpoint the negative branch is supplied from the column
endpoint through the level one degree lower. 
