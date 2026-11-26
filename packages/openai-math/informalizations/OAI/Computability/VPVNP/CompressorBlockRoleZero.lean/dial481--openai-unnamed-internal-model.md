---
{
  "module": "OAI/Computability/VPVNP/CompressorBlockRoleZero.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorBlockRoleZero.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorBlockRoleZero.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Publishing the initial cursor role

The fourth initial visit writes the cursor role at scalar offset 27. Its
worker receives the two operands computed by the planner. The six packed
incidence columns begin after the level header, so their typed readback
survives the role write.


### `visit`

 The level-zero visit that stores the cursor role tag at header offset 27. 

### `role`

 Machine-word address of the initial level's role tag. 

### `report`

 The initial role writer's report, storing zero at the role address and returning cursor
one. 

### `run`

 The operands are evaluated at the first level header; the worker enters
at its own initial cursor zero and returns cursor one. 

### `preserve`

 The header write preserves all six base and actual incidence columns.
The column stride may exceed the exact slot count of the represented state. 

### `preserve_allocated`

 In a physical level-zero allocation the slot-capacity and exclusive
end-address bounds imply the column room required by the frame proof. 
