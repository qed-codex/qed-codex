---
{
  "module": "OAI/Computability/VPVNP/ShrinkLocalMaps.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ShrinkLocalMaps.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ShrinkLocalMaps.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Demand rows of the six maps at their packed sites

A and B read their respective slices of the old bundle from whole vertex
factors placed at their sites. C and D read the two ends of their old wire,
including the reversal when its source is thick. The resulting matrix row
indices agree with the global demand indices used in the conversion identity.


### `shrinkPlacedHalf`

 Use the coordinates of the old packed site to access its placed old factors. 

### `shrinkLocalDemandArg`

 Each party reads only the demand coordinates located at its own site. 

### `shrinkLocalDemandArg_eval`

 On the restrictions of a global assignment, the local rows read precisely
the four demand words of the unplaced six-party identity. 
