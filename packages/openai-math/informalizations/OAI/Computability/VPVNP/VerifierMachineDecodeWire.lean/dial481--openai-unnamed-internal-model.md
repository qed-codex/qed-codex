---
{
  "module": "OAI/Computability/VPVNP/VerifierMachineDecodeWire.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/VerifierMachineDecodeWire.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/VerifierMachineDecodeWire.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The output wires of the coefficient machine's table decoder

A wire can test validity, recognize the empty program, or request a specific instruction at a
specific row and branch. A request records both tape updates and the target state.


### `InstructionKey`

 The target state and the two symbol-and-motion pairs tested by an instruction query at
input length `n`. 

### `DecoderWire`

 A decoder output testing validity, the empty program, or the instruction in a specific
transition slot. 

### `rowInstruction`

 Read one branch slot of a row. A one-branch row uses the false slot. 

### `KeyMatches`

 The queried target, writes, and movements all agree with the literal instruction, comparing
target indices by value. 

### `wireHolds`

 The predicate on a decoded program expressed by a particular decoder output wire. 

### `queryAllowed`

 The global check on the running state count for the requested output. 

### `keepRow`

 Local constraint at the indexed row. 

### `RowsKeep`

 Every indexed row passes the requested decoder test, including the queried branch when its
row is reached. 
