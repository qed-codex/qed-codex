---
{
  "module": "OAI/Computability/VPVNP/CompressorRefreshArgumentPlan.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRefreshArgumentPlan.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRefreshArgumentPlan.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Constructing the refresh argument bank from level and traversal addresses

The two node numbers, their common site ordinal, the private arena and the old inverse
column are traversal inputs. The segment and term heads and the next incidence columns
are evaluated from the same packed level plan used by the native refresh builder. Its
interval frame preserves the old incidence columns through the complete execution.


### `Traversal`

 Expressions supplied by the traversal to locate the old and new node arguments at a shared
site ordinal. 

### `Traversal.arena`

 Expression for the base address of the private node argument arena. 

### `Traversal.stride`

 Expression for the number of arena words reserved per node. 

### `Traversal.child`

 Expression for the child node number indexing the old half of the refresh argument. 

### `Traversal.parent`

 Expression for the parent node number indexing the refreshed half of the argument. 

### `Traversal.site`

 Expression for the ordinal shared by the old site and its promoted site. 

### `Traversal.oldIn`

 Expression for the base of the old actual incoming incidence column. 

### `fromLevel`

 Builds the child and parent operand records from the traversal addresses and the scratch,
incidence, demand and term columns of the refresh level. 

### `describes_fromLevel`

 The packed allocation supplies every numerical operand of the endpoint setup. 

### `old_directory`

 Every old incidence read survives the packed refresh. This applies both to the
private operand setup and to future descriptor traversals reaching this older level. 

### `run_argument_data`

 Both incidence inputs and all stored fields for the native map and diagonal setups
are available together after the selected refresh level. 
