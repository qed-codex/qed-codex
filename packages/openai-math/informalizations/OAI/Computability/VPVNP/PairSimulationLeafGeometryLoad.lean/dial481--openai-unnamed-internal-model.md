---
{
  "module": "OAI/Computability/VPVNP/PairSimulationLeafGeometryLoad.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafGeometryLoad.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafGeometryLoad.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Reloading leaf operands at the descriptor visit

Private word `endAddr` points to the geometry array. Its first ten consecutive
words supply the leaf's descriptor fields, argument arena, and input length.
The native loader uses the DFS end pointer and the DFS unit register.


### `slot`

 The location of each leaf operand in the ten-word private geometry record. Address fields
occupy slots 0 through 5, arena fields occupy 6 through 8, and the input size occupies slot
9. 

### `Label`

 Instruction labels for the initial geometry-pointer load and the ten pairs of field loads
and cursor increments. 

### `bank`

 Physical destination register for the operand in the given geometry slot. 

### `instruction`

 Fetch the private geometry pointer, load each of its ten consecutive words into the
assigned register, and advance the pointer with the DFS unit register. 

### `Stored`

 The contents of the geometry record, independent of the incoming leaf
registers. The assembler also uses slots ten and eleven for other vertex roles. 

### `run`

 One private pointer read and ten private loads with address increments.
Registers outside the ten destinations and the cursor are preserved. 
