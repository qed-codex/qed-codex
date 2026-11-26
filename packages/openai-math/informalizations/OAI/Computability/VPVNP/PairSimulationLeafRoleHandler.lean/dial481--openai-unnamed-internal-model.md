---
{
  "module": "OAI/Computability/VPVNP/PairSimulationLeafRoleHandler.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafRoleHandler.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafRoleHandler.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Exactness of the cursor-leaf segment in the eleven-operand vertex table

The physical domain contains the node packet, the 38 cached auxiliary operands
and the ten geometry words reached through the DFS end pointer. Together these
determine the parser on the actual private memory at entry.


### `stored_actual`

 The domain's typed scratch contains the complete physical record used at entry. 

### `addressFields`

 Read the decoder's row or shadow field from its corresponding slot in the ten geometry
words. 

### `parser`

 The parser uses the field words stored in the geometry record. 

### `Domain`

 The saved scratch and node satisfy the leaf visit's input conditions, and the same scratch
stores the geometry record used to decode its address. 
