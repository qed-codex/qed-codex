---
{
  "module": "OAI/Computability/VPVNP/PairShrinkSurvivingOperands.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkSurvivingOperands.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkSurvivingOperands.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Surviving supply operands in the shrinking kernel

Each surviving wire is gathered from the numbered half-wires of the output
state. At the target this uses the incoming slot of the translated actual
arc. The two endpoints may hold independent half-wire assignments.


### `packet_field`

 Reading a resident packet's specified native slot gives the node's
actual half-field. The private memory may already contain other packets. 

### `site`

 Packed source or target site of the specified supply edge. 

### `slot`

 The native slot at the chosen end of one actual subdivision. 

### `slot_number`

 Outgoing slots retain the genuine arc number, while the incoming
slot is the second component of the lifted slot permutation's image. 

### `operand`

 Word read by the supply map from an arbitrary half-assignment at this endpoint. 

### `slot_bits`

 The physical node field is exactly the corresponding interval of the
local supply operand, at either of its endpoints. 

### `execute_slot`

 Copy one native output slot into the operand buffer from a supplied
parent packet, using the physical surviving row in level memory. 

### `nativeFill`

 Memory updates from visiting each actual output slot at this endpoint. 

### `nativeFill_eq`

 Executing the memory updates from the full row stores exactly the
surviving supply word, including its selector bits. 

### `party`

 Vertex of the six-party map which owns this end of the surviving wire. 

### `mapColumn`

 Select the incoming or outgoing column of the actual local supply map
at the active edge. Its opposite layout fields use the internal assignment. 

### `mapColumn_bits`

 The reconstructed operand is precisely the bit representation of the
surviving column on independent local half-wires. 

### `nativeFill_mapColumn`

 Reading a gathered bit gives that coordinate of the local six-party
map's actual supply basis index. 

### `selected_inputs`

 Extract exactly the three preconditions of the reverse reader from the
selected global row sweep at the physical dense ordinal of a motif and role. 
