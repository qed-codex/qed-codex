---
{
  "module": "OAI/Computability/VPVNP/PairShrinkSurvivingColumn.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkSurvivingColumn.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkSurvivingColumn.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Gathering a surviving endpoint into the six-party map buffer

The linked column computes three pointers per subdivision. The inverse sorted
table supplies the native field's port. The row table supplies the frame.
The full column reads one resident packet and writes one complete supply word.


### `Inputs`

 Common runtime parameters of the column. The node and private destination
are supplied by the enclosing map job. 

### `Inputs.tables`

 Runtime heads and dimensions used to recover the surviving endpoint's port and
  subdivision frame. 

### `Inputs.half`

 Argument-arena geometry and incidence columns of the state containing the subdivided
  endpoint. 

### `Inputs.node`

 DFS node expression selecting the private packet that contains this endpoint's
  subdivision. 

### `Inputs.destination`

 Private base expression of the unsplit supply word being reconstructed. 

### `Inputs.setup`

 Build the reverse-copy setup for one subdivision from its oriented port, resident packet
field, unsplit destination, and interval frame. 

### `row`

 Logical rows carry the actual native fields, including zero-length subdivisions. 

### `reads`

 The actual stored packet meets every frame's private source precondition. 

### `fits`

 Each copy is from the packet below the workspace boundary into the
unsplit word above it, so earlier writes preserve all later source bits. 

### `recorded`

 Combine the actual port ordinal, packet directory and final three-word
interval image into the private worker's complete recorded row. 

### `writes_operand`

 The concatenation of these precise native writes is one unsplit word. 

### `native`

 Run the complete linked subdivision column from one resident packet.
Each iteration computes its pointers in the native register-setup machine. 
