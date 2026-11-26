---
{
  "module": "OAI/Computability/VPVNP/PairSimulationLeafFieldCode.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafFieldCode.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafFieldCode.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Private RAM instructions that stage one scalar leaf field

Only the destination length, value, and one arithmetic temporary are
written. Source words occupy a fixed register bank shared by every field.
The field number and its operand register are selected by finite control.


### `Out`

 The three writable scalar-staging destinations holding the field length, field value and
arithmetic temporary. 

### `Reg`

 Named staging registers for the three outputs, constants and site geometry, and the virtual
machine's indexed public operands. 

### `Rhs`

 A scalar-staging expression that copies one register or applies a binary word operation to
two registers. 

### `Line`

 One scalar-staging assignment, pairing a writable destination with the expression whose
word it receives. 

### `code`

 The fixed assignments that compute a field's stack length and source word from the leaf's
geometry and cached operands. 

### `instruction`

 Compile a scalar-staging assignment to a host copy or binary instruction that jumps to the
supplied continuation. 

### `Rhs.eval`

 Evaluate a scalar-staging expression against the current named register values using
machine-word arithmetic. 

### `applyLine`

 Update the named destination register with the value of one staging assignment. 

### `applyPhysical`

 Perform a staging assignment in the host register bank using the physical placement of its
source and destination registers. 

### `run`

 Each row makes an actual private step in the supplied parent table. 
