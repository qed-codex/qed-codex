---
{
  "module": "OAI/Computability/VPVNP/CompressorShrinkResidentDirectory.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkResidentDirectory.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkResidentDirectory.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native owner columns for hidden and map residents of a shrinking node

The dense CD array comes from the classified old-port scatter. The selected
layout supplies the absolute role rows. A scan over the motif-major order
uses exactly these two inputs to materialize each resident's packed owner.


### `oldOrder`

 Motif-major scan order for resident occurrences, with four internal fields or six party
maps per motif according to `maps`. 

### `role`

 Select the packed role of an internal field or a party map from its local index and the
chosen shrink layout. 

### `place`

 Packed site owning a given motif's field or map occurrence, found from its surviving role
under the selected layout. 

### `physical`

 Encode the owner placement as RAM words using the motif-major occurrence order and the
numerical packed-site order. 

### `Absolute`

 The dense CD directory in memory maps each motif index to its old arc's absolute role-table
index. 

### `absolute_input`

 The sorted scatter uses exactly the motif coordinate of the history cursor. 

### `Areas`

 The input rectangles may lie on either side of the fresh owner column. 

### `absolute_address`

 The quotient in the running program reads the sorted absolute-ID cell. 

### `role_address`

 Combining the scatter read and role digit identifies the actual role-word address. 

### `Written`

 Complete physical owner column and the native trace which generated it. 

### `Written.ownerAt`

 Each native owner word supplies the exact input read of the preimage collector. 

### `run`

 Scan the sorted absolute-CD input and selected role rows to form the
four-way hidden or six-way map owner column, preserving all other words. 
